---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class="anchor" id="about-me"></span>

<section class="home-hero">
  <div class="home-hero__glow home-hero__glow--one" aria-hidden="true"></div>
  <div class="home-hero__glow home-hero__glow--two" aria-hidden="true"></div>
  <div class="home-hero__content">
    <p class="home-hero__eyebrow"><span></span> Researcher · 3D Generative AI</p>
    <h1>Building intelligent systems that <em>create, perceive, and interact.</em></h1>
    <p class="home-hero__intro">I currently work at <a href="https://www.meshy.ai/">Meshy AI</a>, where my research centers on state-of-the-art 3D generative AI technologies. Previously, I completed my Master’s degree at <a href="https://www.shanghaitech.edu.cn/">ShanghaiTech University</a>, advised by <a href="https://faculty.sist.shanghaitech.edu.cn/faculty/hexm/index.html">Prof. Xuming He</a> in the Plus Lab at the Visual &amp; Data Intelligence Center.</p>
    <div class="research-tags" aria-label="Research interests">
      <span>Deep Learning</span>
      <span>Generative Models</span>
      <span>Embodied AI</span>
    </div>
    <div class="home-hero__actions">
      <a class="hero-button hero-button--primary" href="#publications" target="_self">Explore my work <span aria-hidden="true">&darr;</span></a>
      <a class="hero-button hero-button--secondary" href="/assets/resume.pdf">View résumé <span aria-hidden="true">&#8599;</span></a>
    </div>
  </div>
</section>

<span class="anchor" id="news"></span>

# 🔥 News

<ul class="news-list">
  <li class="news-list__featured"><time datetime="2026-09">2026.09</time><span><strong>New launch</strong> — <a href="https://mora.fun/">Mora · AI for Fun</a> is now live.</span></li>
  <li><time datetime="2026-08">2026.08</time><span><a href="https://arxiv.org/abs/2607.28675">Meshy T2</a> published.</span></li>
  <li><time datetime="2026-07">2026.07</time><span>Joined <a href="https://www.meshy.ai/">Meshy AI</a>.</span></li>
  <li><time datetime="2026-02">2026.02</time><span>One paper accepted by <strong>CVPR 2026</strong>.</span></li>
  <li><time datetime="2024-11">2024.11</time><span>One paper accepted by the International Conference on 3D Vision (<strong>3DV 2025</strong>).</span></li>
  <li><time datetime="2024-01">2024.01</time><span>One paper accepted by the International Joint Conference on Artificial Intelligence (<strong>IJCAI 2024</strong>).</span></li>
</ul>

<span class="anchor" id="internships"></span>

# 💻 Internships

<div class="timeline-list">
  <div class="timeline-item"><span class="timeline-item__date">2026.01 — 2026.06</span><div><a href="https://www.tiktok.com/"><strong>ByteDance · TikTok</strong></a><p>Generative Recommendation · Advised by Mr. Kai Feng</p></div></div>
  <div class="timeline-item"><span class="timeline-item__date">2025.04 — 2025.10</span><div><a href="https://hunyuan.tencent.com/"><strong>Tencent · Hunyuan</strong></a><p>Video Generation · Advised by Mr. Yuan Zhou</p></div></div>
  <div class="timeline-item"><span class="timeline-item__date">2024.12 — 2025.03</span><div><a href="https://www.zhiyuan-robot.com/"><strong>AGI-Bot</strong></a><p>World Model / Video Generation · Advised by Mr. Liliang Chen</p></div></div>
  <div class="timeline-item"><span class="timeline-item__date">2024.09 — 2024.12</span><div><a href="https://roboticsx.tencent.com/"><strong>Tencent · Robotics X</strong></a><p>Embodied AI, Perception and Action Collaboration Group · Advised by Mr. Yu Zheng</p></div></div>
</div>

<span class="anchor" id="publications"></span>

# 📝 Publications & Projects

<div class="paper-box paper-box--mora">
  <div class="paper-box-image">
    <a class="mora-visual" href="https://mora.fun/" aria-label="Visit Mora">
      <span class="badge badge--mora">New · 2026</span>
      <span class="mora-mark" aria-hidden="true"><i></i><b></b></span>
      <span class="mora-wordmark">MORA</span>
      <span class="mora-tagline">AI FOR FUN</span>
    </a>
  </div>
  <div class="paper-box-text">
    <p class="paper-kicker">Featured project · Launched September 2026</p>
    <h3><a href="https://mora.fun/">Mora · AI for Fun</a></h3>
    <p>A playful AI experience built around one simple idea: AI should be fun.</p>
    <p class="paper-links"><a href="https://mora.fun/"><span aria-hidden="true">&#9672;</span> Project Website</a><span class="paper-url">mora.fun</span></p>
  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image"><div><div class="badge">Preprint</div><img src="/images/meshT2.png" alt="Meshy T2 project preview" width="100%" loading="lazy"></div></div>
  <div class="paper-box-text">
    <h3><a href="https://arxiv.org/abs/2607.28675">Meshy T2: Fast Native Mesh Generation with Flow Matching</a></h3>
    <p>Jiale Xu*, Rendong Liang*, Yuhao Long, Siyuan Shen, Zangyueyang Xian, Xiaofei Wu, Zeyi Xu, Yuanming Hu</p>
    <p class="paper-links"><a href="https://github.com/meshy-dev/meshy-t2"><span aria-hidden="true">&#9672;</span> Project</a><a href="https://arxiv.org/abs/2607.28675"><span aria-hidden="true">&#8599;</span> Paper</a></p>
  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image"><div><div class="badge">Preprint</div><img src="/images/pfvg.png" alt="PFVG project preview" width="100%" loading="lazy"></div></div>
  <div class="paper-box-text">
    <h3><a href="https://arxiv.org/abs/2510.01784">Pack and Force Your Memory: Long-form and Consistent Video Generation</a></h3>
    <p><strong>Xiaofei Wu</strong>, Guozhen Zhang, Zhiyong Xu, Yuan Zhou, Qinglin Lu, Xuming He</p>
    <p class="paper-links"><a href="https://wuxiaofei01.github.io/PFVG/"><span aria-hidden="true">&#9672;</span> Project</a><a href="https://arxiv.org/abs/2510.01784"><span aria-hidden="true">&#8599;</span> Paper</a></p>
  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image"><div><div class="badge">CVPR 2026</div><img src="/images/AffordGrasp.png" alt="AffordGrasp project preview" width="100%" loading="lazy"></div></div>
  <div class="paper-box-text">
    <h3><a href="https://arxiv.org/abs/2603.08021">AffordGrasp: Cross-Modal Diffusion for Affordance-Aware Grasp Synthesis</a></h3>
    <p><strong>Xiaofei Wu</strong>, Yi Zhang, Yumeng Liu, Yuexin Ma, Yujiao Shi, Xuming He</p>
    <p class="paper-links"><a href="https://wuxiaofei01.github.io/AffordGrasp_page"><span aria-hidden="true">&#9672;</span> Project</a><a href="https://arxiv.org/abs/2603.08021"><span aria-hidden="true">&#8599;</span> Paper</a></p>
  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image"><div><div class="badge">3DV 2025</div><img src="/images/fastgrasp.png" alt="FastGrasp project preview" width="100%" loading="lazy"></div></div>
  <div class="paper-box-text">
    <h3><a href="https://arxiv.org/abs/2411.14786">FastGrasp: Efficient Grasp Synthesis with Diffusion</a></h3>
    <p><strong>Xiaofei Wu</strong>, Tao Liu, Caoji Li, Yuexin Ma, Yujiao Shi, Xuming He</p>
    <p class="paper-links"><a href="https://github.com/wuxiaofei01/FastGrasp"><span aria-hidden="true">&#9672;</span> Project</a><a href="https://arxiv.org/abs/2411.14786"><span aria-hidden="true">&#8599;</span> Paper</a></p>
  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image"><div><div class="badge">IJCAI 2024</div><img src="/images/realdex.png" alt="RealDex project preview" width="100%" loading="lazy"></div></div>
  <div class="paper-box-text">
    <h3><a href="https://arxiv.org/abs/2402.13853">RealDex: Towards Human-like Grasping for Robotic Dexterous Hand</a></h3>
    <p>Yumeng Liu*, Yaxun Yang*, Youzhuo Wang*, <strong>Xiaofei Wu</strong>, Jiamin Wang, Yichen Yao, Sören Schwertfeger, Sibei Yang, Wenping Wang, Jingyi Yu, Xuming He, Yuexin Ma</p>
    <p class="paper-links"><a href="https://4dvlab.github.io/RealDex_page/"><span aria-hidden="true">&#9672;</span> Project</a><a href="https://arxiv.org/abs/2402.13853"><span aria-hidden="true">&#8599;</span> Paper</a></p>
  </div>
</div>

<span class="anchor" id="honors"></span>

# 🎖 Honors and Awards

<ul class="compact-list">
  <li><time>2024.12</time><span>Outstanding Student, ShanghaiTech University <strong>· Top 10%</strong></span></li>
  <li><time>2022.08</time><span>Silver Medal, Robocom Robot Developer Competition</span></li>
  <li><time>2021.06</time><span>Bronze Medal, National College Student Group Programming Competition</span></li>
  <li><time>2020.10</time><span>Gold Award, Liaoning Provincial Programming Competition <strong>· Top 5%</strong></span></li>
  <li><time>2020.09</time><span>First Class Scholarship, Northeastern University <strong>· Top 10%</strong></span></li>
  <li><time>2020.03</time><span>Outstanding Student, Northeastern University <strong>· Top 10%</strong></span></li>
</ul>

<span class="anchor" id="education"></span>

# 📖 Education

<div class="education-grid">
  <article><span>2023 — 2026</span><h3>ShanghaiTech University</h3><p>M.S. in Computer Science · Visual &amp; Data Intelligence Center</p><small>Supervised by <a href="https://faculty.sist.shanghaitech.edu.cn/faculty/hexm/index.html">Prof. Xuming He</a></small></article>
  <article><span>2019 — 2023</span><h3>Northeastern University</h3><p>B.E. in Computer Science and Technology</p><small>Shenyang, China</small></article>
</div>

<span class="anchor" id="service"></span>

# 📑 Academic Service

<p class="service-intro">Reviewer for leading journals and conferences in computer vision and artificial intelligence.</p>
<div class="service-tags"><span>IEEE Transactions on Image Processing · TIP</span><span>AAAI Conference on Artificial Intelligence</span></div>
