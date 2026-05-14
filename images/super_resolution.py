"""图片超分辨率工具.

依赖安装:
    pip install -r requirements.txt
    # 或:
    pip install opencv-contrib-python pillow numpy

使用示例:
    python super_resolution.py input.png output.png --model edsr --scale 2
"""

from __future__ import annotations

import os
import sys
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image

try:
    import cv2
    _HAS_DNN_SR = hasattr(cv2, "dnn_superres")
except ImportError:
    cv2 = None
    _HAS_DNN_SR = False


MODEL_DIR = Path(__file__).resolve().parent / "models"

# 预训练模型下载地址 (来自 OpenCV 官方推荐的开源仓库)
MODEL_URLS: dict[str, dict[int, str]] = {
    "edsr": {
        2: "https://github.com/Saafke/EDSR_Tensorflow/raw/master/models/EDSR_x2.pb",
        3: "https://github.com/Saafke/EDSR_Tensorflow/raw/master/models/EDSR_x3.pb",
        4: "https://github.com/Saafke/EDSR_Tensorflow/raw/master/models/EDSR_x4.pb",
    },
    "espcn": {
        2: "https://github.com/fannymonori/TF-ESPCN/raw/master/export/ESPCN_x2.pb",
        3: "https://github.com/fannymonori/TF-ESPCN/raw/master/export/ESPCN_x3.pb",
        4: "https://github.com/fannymonori/TF-ESPCN/raw/master/export/ESPCN_x4.pb",
    },
    "fsrcnn": {
        2: "https://github.com/Saafke/FSRCNN_Tensorflow/raw/master/models/FSRCNN_x2.pb",
        3: "https://github.com/Saafke/FSRCNN_Tensorflow/raw/master/models/FSRCNN_x3.pb",
        4: "https://github.com/Saafke/FSRCNN_Tensorflow/raw/master/models/FSRCNN_x4.pb",
    },
    "lapsrn": {
        2: "https://github.com/fannymonori/TF-LapSRN/raw/master/export/LapSRN_x2.pb",
        4: "https://github.com/fannymonori/TF-LapSRN/raw/master/export/LapSRN_x4.pb",
        8: "https://github.com/fannymonori/TF-LapSRN/raw/master/export/LapSRN_x8.pb",
    },
}


def _download_model(model: str, scale: int) -> Path:
    """按需下载模型文件, 已存在时直接复用."""
    if model not in MODEL_URLS or scale not in MODEL_URLS[model]:
        raise ValueError(
            f"模型 {model} 不支持 scale={scale}, "
            f"可选: {[(m, list(s.keys())) for m, s in MODEL_URLS.items()]}"
        )

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    url = MODEL_URLS[model][scale]
    dst = MODEL_DIR / Path(url).name
    if dst.exists() and dst.stat().st_size > 0:
        return dst

    print(f"[super-resolution] 下载模型 {dst.name} ...", file=sys.stderr)
    tmp = dst.with_suffix(dst.suffix + ".part")
    try:
        urllib.request.urlretrieve(url, tmp)
        os.replace(tmp, dst)
    except Exception:
        if tmp.exists():
            tmp.unlink(missing_ok=True)
        raise
    return dst


class SuperResolution:
    """基于 OpenCV dnn_superres 的图片放大器, 不可用时回退到 PIL LANCZOS."""

    SUPPORTED_MODELS = ("edsr", "espcn", "fsrcnn", "lapsrn")

    def __init__(self, model_type: str = "edsr", scale: int = 2, auto_download: bool = True):
        self.model_type = model_type.lower()
        self.scale = int(scale)
        if self.model_type not in self.SUPPORTED_MODELS:
            raise ValueError(
                f"不支持的模型类型: {model_type}, 可选: {self.SUPPORTED_MODELS}"
            )

        self._sr = None
        if _HAS_DNN_SR:
            model_path = _download_model(self.model_type, self.scale) if auto_download else None
            self._sr = cv2.dnn_superres.DnnSuperResImpl_create()
            try:
                self._sr.readModel(str(model_path))
                self._sr.setModel(self.model_type, self.scale)
            except Exception as exc:
                # 模型读取失败时, 回退到 LANCZOS, 不要让调用方崩溃
                print(
                    f"[super-resolution] 加载模型失败 ({exc}), 回退到 PIL LANCZOS",
                    file=sys.stderr,
                )
                self._sr = None
        else:
            print(
                "[super-resolution] 当前 OpenCV 未安装 contrib 模块 (cv2.dnn_superres), "
                "回退到 PIL LANCZOS。安装 opencv-contrib-python 可启用深度学习超分。",
                file=sys.stderr,
            )

    def enhance(self, img: Image.Image | np.ndarray) -> np.ndarray:
        """对图片进行超分辨率处理, 返回 BGR 顺序的 numpy.ndarray (与 OpenCV 一致)."""
        bgr = self._to_bgr(img)
        if self._sr is not None:
            return self._sr.upsample(bgr)
        # PIL 回退路径
        rgb = bgr[:, :, ::-1]
        pil = Image.fromarray(rgb)
        new_size = (pil.width * self.scale, pil.height * self.scale)
        up = pil.resize(new_size, Image.LANCZOS)
        return np.array(up)[:, :, ::-1]

    def enhance_file(self, in_path: str | os.PathLike, out_path: str | os.PathLike) -> None:
        """读取一张图片, 进行超分后保存."""
        in_path = str(in_path)
        out_path = str(out_path)
        if cv2 is not None:
            img = cv2.imread(in_path, cv2.IMREAD_COLOR)
            if img is None:
                raise FileNotFoundError(f"无法读取输入图片: {in_path}")
        else:
            pil = Image.open(in_path).convert("RGB")
            img = np.array(pil)[:, :, ::-1]

        result = self.enhance(img)
        ok = False
        if cv2 is not None:
            ok = bool(cv2.imwrite(out_path, result))
        if not ok:
            Image.fromarray(result[:, :, ::-1]).save(out_path)

    @staticmethod
    def _to_bgr(img: Image.Image | np.ndarray) -> np.ndarray:
        """统一转换为 OpenCV 习惯的 BGR uint8 数组."""
        if isinstance(img, Image.Image):
            img = np.array(img.convert("RGB"))[:, :, ::-1]
        elif isinstance(img, np.ndarray):
            if img.ndim == 2:
                img = np.stack([img] * 3, axis=-1)
            elif img.shape[-1] == 4 and cv2 is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        else:
            raise TypeError("img 必须是 numpy.ndarray 或 PIL.Image.Image")
        if img.dtype != np.uint8:
            img = np.clip(img, 0, 255).astype(np.uint8)
        return np.ascontiguousarray(img)


def _build_parser():
    import argparse

    p = argparse.ArgumentParser(description="图片超分辨率工具")
    p.add_argument("input", help="输入图片路径")
    p.add_argument("output", help="输出图片路径")
    p.add_argument(
        "--model",
        choices=SuperResolution.SUPPORTED_MODELS,
        default="lapsrn",
        help="超分模型 (默认: edsr)",
    )
    p.add_argument(
        "--scale",
        type=int,
        choices=[2, 3, 4, 8],
        default=8,
        help="放大倍数 (默认: 2; lapsrn 仅支持 2/4/8, 其他模型支持 2/3/4)",
    )
    p.add_argument(
        "--no-download",
        action="store_true",
        help="禁用自动下载模型, 仅使用本地已有的 .pb 文件",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    sr = SuperResolution(
        model_type=args.model,
        scale=args.scale,
        auto_download=not args.no_download,
    )
    sr.enhance_file(args.input, args.output)
    print(f"超分完成, 保存至 {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
