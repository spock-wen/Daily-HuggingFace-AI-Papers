<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-53-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-10316+-orange?style=for-the-badge&logo=academia)](data/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/AtharvaDomale/Daily-HuggingFace-AI-Papers?style=social)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/stargazers)

**Automatically updated every day at 00:00 UTC** ⏰

[📊 View Data](data/) | [🔍 Latest Papers](data/latest.json) | [📅 Archives](#-historical-archives) | [⭐ Star This Repo](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers)

</div>

---

## 🎯 Why This Repo?

- ✅ **Saves 30+ minutes** of daily paper hunting
- ✅ **Organized archives** - daily, weekly, and monthly snapshots
- ✅ **Direct links** to arXiv, PDFs, and GitHub repositories
- ✅ **Machine-readable JSON** format for easy integration
- ✅ **Zero maintenance** - fully automated via GitHub Actions
- ✅ **Historical data** - track AI research trends over time

---

## 🚀 Who Is This For?

<table>
<tr>
<td align="center">🔬<br/><b>Researchers</b><br/>Stay current with latest developments</td>
<td align="center">💼<br/><b>ML Engineers</b><br/>Discover SOTA techniques</td>
<td align="center">📚<br/><b>Students</b><br/>Learn from cutting-edge research</td>
</tr>
<tr>
<td align="center">🏢<br/><b>Companies</b><br/>Track AI trends & competition</td>
<td align="center">📰<br/><b>Content Creators</b><br/>Find topics for blogs & videos</td>
<td align="center">🤖<br/><b>AI Enthusiasts</b><br/>Explore the latest in AI</td>
</tr>
</table>

---

## ⚡ Quick Start

### 1️⃣ Get Today's Papers (cURL)

```bash
curl https://raw.githubusercontent.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/main/data/latest.json
```

### 2️⃣ Python Integration

```python
import requests
import pandas as pd

# Load latest papers
url = "https://raw.githubusercontent.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/main/data/latest.json"
papers = requests.get(url).json()

# Convert to DataFrame for analysis
df = pd.DataFrame(papers)
print(f"📚 Today's papers: {len(df)}")

# Filter by stars
trending = df[df['stars'].astype(int) > 10]
print(f"🔥 Trending papers: {len(trending)}")
```

### 3️⃣ JavaScript/Node.js

```javascript
const fetch = require('node-fetch');

async function getTodaysPapers() {
  const response = await fetch(
    'https://raw.githubusercontent.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/main/data/latest.json'
  );
  const papers = await response.json();
  
  console.log(`📚 Found ${papers.length} papers today!`);
  papers.forEach(paper => {
    console.log(`\n📄 ${paper.title}`);
    console.log(`⭐ ${paper.stars} stars`);
    console.log(`🔗 ${paper.details.arxiv_page_url}`);
  });
}

getTodaysPapers();
```

---

## 📈 Statistics

<table>
<tr>
<td align="center"><b>📄 Today</b><br/><font size="5">53</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">184</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">915</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">10316+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 26, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Real2SimLab: A Unified Platform for Real-to-Simulation Transfer</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34849) • [📄 arXiv](https://arxiv.org/abs/2611.34849) • [📥 PDF](https://arxiv.org/pdf/2611.34849)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Real2SimHub/Real2SimLab)

> Real2SimHub: a community to build the infrastructure of real-to-simulation together.

</details>

<details>
<summary><b>2. Sage-Med: Scaling Medical Multimodal Intelligence</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34575) • [📄 arXiv](https://arxiv.org/abs/2611.34575) • [📥 PDF](https://arxiv.org/pdf/2611.34575)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Sage-Med/Sage-Med-Preview)

> Hi everyone! 👋 We are the Sage-Med Team , excited to share our paper: Sage-Med: Scaling Medical Multimodal Intelligence . TL;DR: We benchmarked 77 models across 238 clinical tasks (61 public + 13 private multi-center benchmarks from 14 hospitals a...

</details>

<details>
<summary><b>3. Mixture-of-Loops Transformer</b> ⭐ 44</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34923) • [📄 arXiv](https://arxiv.org/abs/2611.34923) • [📥 PDF](https://arxiv.org/pdf/2611.34923)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hustvl/MoLT)

> Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as ...

</details>

<details>
<summary><b>4. VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34237) • [📄 arXiv](https://arxiv.org/abs/2611.34237) • [📥 PDF](https://arxiv.org/pdf/2611.34237)

**💻 Code:** [⭐ Code](https://github.com/Kling-Keye/VibeVideoAgent) • [⭐ Code](https://github.com/huggingface)

> Awesome Agent solution for code2video tasks～～～

</details>

<details>
<summary><b>5. DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers</b> ⭐ 41</summary>

<br/>

**👥 Authors:** Wei Zhang, Pengfei Xiong, Yuanliu Liu, OneCreamBox

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30844) • [📄 arXiv](https://arxiv.org/abs/2611.30844) • [📥 PDF](https://arxiv.org/pdf/2611.30844)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OneBoxCream/DyLoMo-DiT)

> DyLoMo-DiT is a new diffusion Transformer architecture that gets more out of the same parameters: the middle layers run in a weight-shared loop, sparse experts decide which parameters each image token uses, and the number of loops changes with the...

</details>

<details>
<summary><b>6. PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33144) • [📄 arXiv](https://arxiv.org/abs/2611.33144) • [📥 PDF](https://arxiv.org/pdf/2611.33144)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DAGroup-PKU/PyRUA-Lean/tree/dex)

> Github Repo: https://github.com/DAGroup-PKU/PyRUA-Lean/tree/dex

</details>

<details>
<summary><b>7. Improving and Expanding Video Editing Capabilities Without Videos</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34941) • [📄 arXiv](https://arxiv.org/abs/2611.34941) • [📥 PDF](https://arxiv.org/pdf/2611.34941)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HorizonWind2004/i2v-transfer)

> Fully Open-sourced! We introduce Image-to-Video Transfer (I2VT), which improves pretrained video editors and expands them to new editing tasks using an image editor. Our intuition is that an image is simply a one-frame video, so editing images wel...

</details>

<details>
<summary><b>8. DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34420) • [📄 arXiv](https://arxiv.org/abs/2611.34420) • [📥 PDF](https://arxiv.org/pdf/2611.34420)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mossbee/DocSEAM)

> No abstract available.

</details>

<details>
<summary><b>9. HOG-WAM: Improving Visual Robustness through Future Gradient Prediction</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34811) • [📄 arXiv](https://arxiv.org/abs/2611.34811) • [📥 PDF](https://arxiv.org/pdf/2611.34811)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/iPPLab/HOG-WAM)

> No abstract available.

</details>

<details>
<summary><b>10. Playfulness as Feedback for Agentic Game Development</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33457) • [📄 arXiv](https://arxiv.org/abs/2611.33457) • [📥 PDF](https://arxiv.org/pdf/2611.33457)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/showlab/Play2Evolve)

> Coding agents can generate runnable games from natural-language descriptions. However, a runnable game does not guarantee an excellent gameplay experience for players. In our view, a playful game should provide 1) reliable core functionality, 2) a...

</details>

<details>
<summary><b>11. EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34466) • [📄 arXiv](https://arxiv.org/abs/2611.34466) • [📥 PDF](https://arxiv.org/pdf/2611.34466)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YurunChen/EgoUseBench)

> AI wearables, such as smart glasses, extend the context available to agents beyond digital environments to users' everyday physical surroundings. With these devices, computer tasks can originate from users' ongoing real-world activities rather tha...

</details>

<details>
<summary><b>12. AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34347) • [📄 arXiv](https://arxiv.org/abs/2611.34347) • [📥 PDF](https://arxiv.org/pdf/2611.34347)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIRIS-bench/AIRIS)

> Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate...

</details>

<details>
<summary><b>13. Let Vision-Language Models Generate Images through Their Representations</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31237) • [📄 arXiv](https://arxiv.org/abs/2611.31237) • [📥 PDF](https://arxiv.org/pdf/2611.31237)

**💻 Code:** [⭐ Code](https://github.com/the-jb/integral) • [⭐ Code](https://github.com/huggingface)

> We investigate how multimodal knowledge acquired through understanding can be leveraged for image generation. To this end, we introduce Integral, a framework that extends pretrained VLMs with image generation, and demonstrate the importance of sha...

</details>

<details>
<summary><b>14. High-Fidelity Image Matting with Pixel-Space Diffusion Transformers</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Baiang Li, Yufan Wei, Xin Lin, Juanxi, WhiteYC

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34929) • [📄 arXiv](https://arxiv.org/abs/2611.34929) • [📥 PDF](https://arxiv.org/pdf/2611.34929)

**💻 Code:** [⭐ Code](https://github.com/White-YC/pixelmatte) • [⭐ Code](https://github.com/huggingface)

> Project page: https://white-yc.github.io/pixelmatte/ .

</details>

<details>
<summary><b>15. FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34128) • [📄 arXiv](https://arxiv.org/abs/2611.34128) • [📥 PDF](https://arxiv.org/pdf/2611.34128)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/vLAR-group/FoundSurface)

> FoundSurface (NeurIPS'26) is a foundation surface reconstruction model. Jointly trained on 9 diverse large-scale datasets, it recovers 3D scene surfaces from unposed images in a single feed-forward pass. For every pixel of a target view, it predic...

</details>

<details>
<summary><b>16. Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation</b> ⭐ 2.91k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34907) • [📄 arXiv](https://arxiv.org/abs/2611.34907) • [📥 PDF](https://arxiv.org/pdf/2611.34907)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NVlabs/LongLive)

> No abstract available.

</details>

<details>
<summary><b>17. What Is Redundant at High Resolution? Efficient Attention and Feed-Forward Design for All-in-One Image Restoration</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33636) • [📄 arXiv](https://arxiv.org/abs/2611.33636) • [📥 PDF](https://arxiv.org/pdf/2611.33636)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dslisleedh/HiGLR)

> Hi everyone! 👋 I'm the first author of this paper. TL;DR: We ask what is actually redundant at high resolution in multi-scale all-in-one image restoration (AIO-IR) networks, and use the answer to build HiGLR , a fast and memory-efficient AIO-IR mo...

</details>

<details>
<summary><b>18. Target-Part Preference Optimization for Part-Aware 3D Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Lina Yao, Sevvandi Kandanaarachchi, Rui Li, Zishan Qin, SteveZeyuZhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30472) • [📄 arXiv](https://arxiv.org/abs/2611.30472) • [📥 PDF](https://arxiv.org/pdf/2611.30472)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! I’m Taylor, the first author of PartDPO. We study how to improve part-aware 3D generation with limited part-level annotations. Our approach learns preferences over individual parts while retaining geometric supervision, without changi...

</details>

<details>
<summary><b>19. Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33925) • [📄 arXiv](https://arxiv.org/abs/2611.33925) • [📥 PDF](https://arxiv.org/pdf/2611.33925)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aim-uofa/WorldReforge)

> Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations. Off the happy path, when a grasp is misaligned or mistimed and the object is pushed, tilted, or slips, thei...

</details>

<details>
<summary><b>20. Beyond Self-Consistency: Recursive Self-Improvement at Test Time</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30965) • [📄 arXiv](https://arxiv.org/abs/2611.30965) • [📥 PDF](https://arxiv.org/pdf/2611.30965)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/uanu2002/TT-RSI)

> Most test-time methods for LLMs vote : sample independent answers and trust the majority, both to pick the final answer and to build training targets. That wastes earlier reasoning, and when the majority is wrong, training on it reinforces the err...

</details>

<details>
<summary><b>21. ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33143) • [📄 arXiv](https://arxiv.org/abs/2611.33143) • [📥 PDF](https://arxiv.org/pdf/2611.33143)

**💻 Code:** [⭐ Code](https://github.com/rxjfighting/ROAM-Bench) • [⭐ Code](https://github.com/huggingface)

> Introducing ROAM-Bench, a benchmark for evaluating embodied active spatial intelligence through evidence verification! As illustrated in the teaser, counting mugs can require exploring multiple rooms and opening closed storage. We check both the f...

</details>

<details>
<summary><b>22. Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28010) • [📄 arXiv](https://arxiv.org/abs/2611.28010) • [📥 PDF](https://arxiv.org/pdf/2611.28010)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Generating PPTX presentations is a structured task that requires semantic planning, visual composition, precise layout, and editability, motivating collaboration among specialized agents. However, programmatic methods offer editability but often p...

</details>

<details>
<summary><b>23. SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33915) • [📄 arXiv](https://arxiv.org/abs/2611.33915) • [📥 PDF](https://arxiv.org/pdf/2611.33915)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZeyangGuan/SEEK-Agentic-Robot-Manipulation)

> General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific demonstrations or training. However, the robot retains what it learns only in the model's working...

</details>

<details>
<summary><b>24. iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33922) • [📄 arXiv](https://arxiv.org/abs/2611.33922) • [📥 PDF](https://arxiv.org/pdf/2611.33922)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGeeksGroup/iMFPO)

> 🚀 We’re excited to introduce iMFPO , a one-step generative policy optimization framework for efficient embodied control! By combining drift-aware velocity alignment with reward-driven policy optimization, iMFPO enables direct action generation wit...

</details>

<details>
<summary><b>25. RoboEvo^2: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Haoyuan Li, Xuzhao Huang, Wei Huang, Jiehong Lin, Chenzhi Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34675) • [📄 arXiv](https://arxiv.org/abs/2611.34675) • [📥 PDF](https://arxiv.org/pdf/2611.34675)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kaiknower/RoboEvo2)

> Introducing RoboEvo² , a framework in which a robot's policy and its coding-agent harness improve each other. Policy failures tell the coding agent what to repair; verified repairs become reusable agent skills and new policy training data. Over ro...

</details>

<details>
<summary><b>26. Loupe: Reinforcing Knowledge-Intensive Video Generation Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31895) • [📄 arXiv](https://arxiv.org/abs/2611.31895) • [📥 PDF](https://arxiv.org/pdf/2611.31895)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present Loupe, an agentic framework for knowledge-intensive video generation that addresses the challenges of missing factual knowledge, entity appearances, and temporal relationships in user prompts. Loupe autonomously leverages text search, i...

</details>

<details>
<summary><b>27. Letting Models Manage Their Own Context: Where We Stand</b> ⭐ 2.33k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34147) • [📄 arXiv](https://arxiv.org/abs/2611.34147) • [📥 PDF](https://arxiv.org/pdf/2611.34147)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/nvidia-nemo/labs-OO-Agents)

> We gave models control over their own context: on OfficeQA Pro v2, GPT nearly triples its score at tight budgets, and Kimi gains with up to 41% fewer input tokens. This opens a new co-design frontier: models trained to manage their own context, se...

</details>

<details>
<summary><b>28. Demystifying the Autoresearch Harness: How Context and Skills Shape Self-Evolving Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28244) • [📄 arXiv](https://arxiv.org/abs/2611.28244) • [📥 PDF](https://arxiv.org/pdf/2611.28244)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What actually drives long-horizon, self-evolving autoresearch agents? This paper systematically demystifies agent harness design across context and skill management on MLE-Bench and KernelBench. Rather than rolling summaries or complex skill conso...

</details>

<details>
<summary><b>29. DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot Data</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33579) • [📄 arXiv](https://arxiv.org/abs/2611.33579) • [📥 PDF](https://arxiv.org/pdf/2611.33579)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wongyun-yu/DexEngine)

> We present DexEngine, a simulation pipeline that turns human hand–object demonstrations into physically executable whole-robot data. From 9 human datasets, it generates about 5,200 clips for each of four dexterous hands, augmented into 65K traject...

</details>

<details>
<summary><b>30. DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yongyi Su, Yueci Deng, Xuanning Zhou, Xinyue Yao, Ruixiang Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34671) • [📄 arXiv](https://arxiv.org/abs/2611.34671) • [📥 PDF](https://arxiv.org/pdf/2611.34671)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DemoFoundry generates action-labeled robot demonstrations for new scenes. A coding agent reconstructs the workspace and programs the task in simulation. A video renderer turns the resulting motion into photorealistic observations using a single RG...

</details>

<details>
<summary><b>31. Change the Base, Change the Game: Rethinking Pan-sharpening</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32002) • [📄 arXiv](https://arxiv.org/abs/2611.32002) • [📥 PDF](https://arxiv.org/pdf/2611.32002)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/KAIST-VICLab/PanBase)

> Change the Base, Change the Game: Rethinking Pan-sharpening Why start with a blurry base when sharp spatial detail is already available?

</details>

<details>
<summary><b>32. LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Zhiyuan Li, Hongyu Liu, Le Li, Sijie Zhao, Jiachen An

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34912) • [📄 arXiv](https://arxiv.org/abs/2611.34912) • [📥 PDF](https://arxiv.org/pdf/2611.34912)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MeiGen-AI/LiveVAE)

> LiveVAE: a streaming video VAE built on causal window attention. Distilled from pretrained video VAEs (MiniMax-H3, Wan2.2), it keeps their latent space and replaces both encoder and decoder directly, running up to 13.4× faster end to end.

</details>

<details>
<summary><b>33. OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32473) • [📄 arXiv](https://arxiv.org/abs/2611.32473) • [📥 PDF](https://arxiv.org/pdf/2611.32473)

**💻 Code:** [⭐ Code](https://github.com/cszhilu1998/OmniPersist) • [⭐ Code](https://github.com/huggingface)

> The camera turns away. The world should go on. OmniPersist couples perspective video generation with an evolving sparse panoramic world to preserve dynamic subjects beyond the field of view. The generated perspective video and corresponding panora...

</details>

<details>
<summary><b>34. Puzzling-Bench: Evaluating Language Models on 23,777 Human-Written Puzzles with Community-Verified Answers</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Sai Karthik Navuluru, Chien Van Nguyen, Li Li, Abhinav Sharma, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34331) • [📄 arXiv](https://arxiv.org/abs/2611.34331) • [📥 PDF](https://arxiv.org/pdf/2611.34331)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/a1bhinav/puzzling-bench)

> No abstract available.

</details>

<details>
<summary><b>35. SIA: Selective Image Analogy</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33894) • [📄 arXiv](https://arxiv.org/abs/2611.33894) • [📥 PDF](https://arxiv.org/pdf/2611.33894)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/alimohammadiamirhossein/selective-image-analogy)

> One before/after example often holds several edits, and image analogy methods give you no say in which ones transfer. SIA lets you pick which edits carry over to your image and leave the rest out, from the same example. Try the interactive demo on...

</details>

<details>
<summary><b>36. 3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33835) • [📄 arXiv](https://arxiv.org/abs/2611.33835) • [📥 PDF](https://arxiv.org/pdf/2611.33835)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGeeksGroup/3DCoCav3)

> We present 3D CoCa v3 , a geometry-aware framework for urban 3D scene understanding. It combines a Pyramid Vision Encoder with Multi-view Scene Graph (MSG) supervision to enhance multi-view geometric representation learning and 3D-language alignme...

</details>

<details>
<summary><b>37. CONCOR: Benchmarking Contrastive Decoding for Visual Hallucination Mitigation Beyond Final-Output Performance</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30460) • [📄 arXiv](https://arxiv.org/abs/2611.30460) • [📥 PDF](https://arxiv.org/pdf/2611.30460)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce CONCOR (Contrastive Correction Evaluation), a controlled benchmark that directly evaluates the competition between ground-truth and different types of hallucinated candidates using the Contrastive Grounding Margin (CGM).

</details>

<details>
<summary><b>38. AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mengdi Wang, Jichen Feng, Minchen Luo, Chengran Li, Guangyuan Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33093) • [📄 arXiv](https://arxiv.org/abs/2611.33093) • [📥 PDF](https://arxiv.org/pdf/2611.33093)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/frontiereval/AIChipBench)

> AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design

</details>

<details>
<summary><b>39. WorldBridge: Bridging Scattered Views for Coherent 3D World Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34079) • [📄 arXiv](https://arxiv.org/abs/2611.34079) • [📥 PDF](https://arxiv.org/pdf/2611.34079)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Generating coherent and explorable 3D worlds from scattered images with little or no visual overlap is a fundamental and long-standing challenge in computer vision.

</details>

<details>
<summary><b>40. Edit Recommendation: Can LLMs Anticipate Edit Requests from Users, and When?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Daisuke Kikuta

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21155) • [📄 arXiv](https://arxiv.org/abs/2611.21155) • [📥 PDF](https://arxiv.org/pdf/2611.21155)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ntt-dkiku/llm-edit-recommendation)

> We evaluate LLM's ability to predict user's next edit requests, and propose decision model-based gating for selective recommendation.

</details>

<details>
<summary><b>41. When Does Reasoning Help Entity Disambiguation? Small LLMs In-Domain and Under Shift</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30334) • [📄 arXiv](https://arxiv.org/abs/2611.30334) • [📥 PDF](https://arxiv.org/pdf/2611.30334)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/samyhaff/ed-study)

> Entity disambiguation (mapping ambiguous mentions in text to entities in a knowledge base) is a foundational step in tasks such as knowledge graph construction, question answering, and information extraction. Recent work has applied LLMs to this p...

</details>

<details>
<summary><b>42. Efficient Video Retrieval Augmented Generation via Token Allocation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32938) • [📄 arXiv](https://arxiv.org/abs/2611.32938) • [📥 PDF](https://arxiv.org/pdf/2611.32938)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Efficient long-video understanding requires identifying relevant evidence while minimizing the tokens processed by vision-language models (VLMs). Existing video retrieval-augmented generation (RAG) methods rely on frame selection and token compres...

</details>

<details>
<summary><b>43. Evaluation-Free Recursive Self-Improvement for Coding Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Piotr Piękos, Nanbo Li, Yimeng Chen, Guowei Rong, Zhe Ren

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21056) • [📄 arXiv](https://arxiv.org/abs/2611.21056) • [📥 PDF](https://arxiv.org/pdf/2611.21056)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 Can coding agents recursively improve themselves without evaluating candidate agents on downstream tasks? We introduce ELITE (Explore-then-Integrate) , a new approach to recursive self-improvement that shifts from evaluation-driven candidate sel...

</details>

<details>
<summary><b>44. Lost in Translation, Not in Confidence: Benchmarking and Calibrating Multilingual Decision Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33307) • [📄 arXiv](https://arxiv.org/abs/2611.33307) • [📥 PDF](https://arxiv.org/pdf/2611.33307)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Decision models are language models finetuned to return a probability for each option of a typed query, which routers and guardrails threshold directly. They are built on multilingual bases but ranked almost entirely in English. We evaluate 25 top...

</details>

<details>
<summary><b>45. When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34777) • [📄 arXiv](https://arxiv.org/abs/2611.34777) • [📥 PDF](https://arxiv.org/pdf/2611.34777)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL

</details>

<details>
<summary><b>46. Collect for Coverage, Replay with Evidence: Adaptive and Efficient On-Policy Distillation for Long-Horizon Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34756) • [📄 arXiv](https://arxiv.org/abs/2611.34756) • [📥 PDF](https://arxiv.org/pdf/2611.34756)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Collect for Coverage, Replay with Evidence: Adaptive and Efficient On-Policy Distillation for Long-Horizon Agents

</details>

<details>
<summary><b>47. A Mesh for Every Moment</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Ira Kemelmacher-Shlizerman, Jeong Joon Park, royorel

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34939) • [📄 arXiv](https://arxiv.org/abs/2611.34939) • [📥 PDF](https://arxiv.org/pdf/2611.34939)

**💻 Code:** [⭐ Code](https://github.com/royorel/MEMO) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>48. Speak When You See It: Proactive Task Assistants Should Wait for Evidence, Not the Clock</b> ⭐ 1</summary>

<br/>

**👥 Authors:** bhc6

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30895) • [📄 arXiv](https://arxiv.org/abs/2611.30895) • [📥 PDF](https://arxiv.org/pdf/2611.30895)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bhc6/speak-when-you-see-it)

> TL;DR: Existing benchmarks often reward timing-based shortcuts rather than genuine visual understanding. This paper introduces ECT, encouraging models to make decisions based on visual evidence instead of elapsed time. A simple yet effective appro...

</details>

<details>
<summary><b>49. SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled Video Generation</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34064) • [📄 arXiv](https://arxiv.org/abs/2611.34064) • [📥 PDF](https://arxiv.org/pdf/2611.34064)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zju3dv/SPARC)

> We present SPARC, a geometry-guided attention pruning framework that turns the native self-attention of pretrained video diffusion transformers into a unified mechanism for camera control and persistent scene memory. Our key insight is that attent...

</details>

<details>
<summary><b>50. Negative-Only Policy Optimization for One-Sided Verifiable Rewards</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17287) • [📄 arXiv](https://arxiv.org/abs/2611.17287) • [📥 PDF](https://arxiv.org/pdf/2611.17287)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> NeurIPS 2026 Spotlight A failed unit test tells us a program is wrong. Passing a few tests still leaves its correctness uncertain. Can we train a policy using only the failures we trust? We introduce Negative-Only Policy Optimization (NOPO), which...

</details>

<details>
<summary><b>51. GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32335) • [📄 arXiv](https://arxiv.org/abs/2611.32335) • [📥 PDF](https://arxiv.org/pdf/2611.32335)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InSAI-Lab/GOLD-SLAM)

> GOLD-SLAM combines LiDAR, IMU, and 360° imagery for localization and 3D Gaussian mapping. It uses visual tracks outside the LiDAR field of view to improve pose estimation and measured LiDAR depth to guide panoramic reconstruction. We also release ...

</details>

<details>
<summary><b>52. Simulator-as-Proxy World Model for Robot Manipulation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32786) • [📄 arXiv](https://arxiv.org/abs/2611.32786) • [📥 PDF](https://arxiv.org/pdf/2611.32786)

**💻 Code:** [⭐ Code](https://github.com/TingtingLiao/SimPWM) • [⭐ Code](https://github.com/huggingface)

> SimPWM uses a rule-based 4D simulator as the proxy for a video world model: the simulator decides what moves under the actions, and the video model renders how it looks.

</details>

<details>
<summary><b>53. SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.34750) • [📄 arXiv](https://arxiv.org/abs/2611.34750) • [📥 PDF](https://arxiv.org/pdf/2611.34750)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> LLM agents have made remarkable progress in robot manipulation, yet they suffer from expensive inference, dense step-by-step control, and tool bottlenecks. We introduce SOLVE, a training-free, versatile and efficient agent policy: a multimodal LLM...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 53 |
| 📅 Today | [`2026-11-26.json`](data/daily/2026-11-26.json) | 53 |
| 📆 This Week | [`2026-W47.json`](data/weekly/2026-W47.json) | 184 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 915 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-26 | 53 | [View JSON](data/daily/2026-11-26.json) |
| 📄 2026-11-25 | 51 | [View JSON](data/daily/2026-11-25.json) |
| 📄 2026-11-24 | 60 | [View JSON](data/daily/2026-11-24.json) |
| 📄 2026-11-23 | 20 | [View JSON](data/daily/2026-11-23.json) |
| 📄 2026-11-22 | 50 | [View JSON](data/daily/2026-11-22.json) |
| 📄 2026-11-21 | 50 | [View JSON](data/daily/2026-11-21.json) |
| 📄 2026-11-20 | 39 | [View JSON](data/daily/2026-11-20.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W47 | 184 | [View JSON](data/weekly/2026-W47.json) |
| 📅 2026-W46 | 268 | [View JSON](data/weekly/2026-W46.json) |
| 📅 2026-W45 | 193 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 915 | [View JSON](data/monthly/2026-11.json) |
| 🗓️ 2026-10 | 1640 | [View JSON](data/monthly/2026-10.json) |
| 🗓️ 2026-09 | 781 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |

---

## ✨ Features

- 🔄 **Automated Daily Updates** - Runs every day at midnight UTC
- 📊 **Comprehensive Data** - Abstracts, authors, links, and metadata
- 🗄️ **Historical Archives** - Daily, weekly, and monthly snapshots
- 🔗 **Direct Links** - arXiv, PDF, GitHub repos, and HuggingFace pages
- 📈 **Trending Papers** - Star counts and popularity metrics
- 💾 **JSON Format** - Easy to parse and integrate into your projects
- 🎨 **Clean Interface** - Beautiful, organized README

---

## 🚀 Usage

### View Papers

- **Latest Papers**: Check this README (updated daily)
- **JSON Data**: Download from [`data/latest.json`](data/latest.json)
- **Historical Data**: Browse the [`data/`](data/) directory

### Integrate Into Your Project

```python
import requests

# Get latest papers
response = requests.get('https://raw.githubusercontent.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/main/data/latest.json')
papers = response.json()

for paper in papers:
    print(f"Title: {paper['title']}")
    print(f"arXiv: {paper['details']['arxiv_page_url']}")
    print(f"PDF: {paper['details']['pdf_url']}")
```

### Use as RSS Alternative

Monitor this repo for daily AI paper updates:
- ⭐ Star this repository
- 👀 Watch for notifications
- 🔔 Enable "All Activity" for daily updates

---

## 📊 Data Structure

```
data/
├── daily/              # Individual day snapshots
│   ├── 2024-12-04.json
│   ├── 2024-12-05.json
│   └── ...
├── weekly/             # Cumulative weekly papers
│   ├── 2024-W48.json
│   └── ...
├── monthly/            # Cumulative monthly papers
│   ├── 2024-12.json
│   └── ...
└── latest.json         # Most recent scrape
```

### JSON Schema

```json
{
  "title": "Paper Title",
  "paper_url": "https://huggingface.co/papers/...",
  "authors": ["Author 1", "Author 2"],
  "stars": "42",
  "scraped_date": "2024-12-04",
  "details": {
    "abstract": "Paper abstract...",
    "arxiv_page_url": "https://arxiv.org/abs/...",
    "pdf_url": "https://arxiv.org/pdf/...",
    "github_links": ["https://github.com/..."],
    "metadata": {}
  }
}
```

---

## 🛠️ How It Works

This repository uses:

- **[Crawl4AI](https://github.com/unclecode/crawl4ai)** - Modern web scraping framework
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** - HTML parsing
- **[GitHub Actions](https://github.com/features/actions)** - Automated daily runs
- **Python 3.11+** - Data processing and generation

### Workflow

1. 🕐 GitHub Actions triggers at 00:00 UTC daily
2. 🔍 Scrapes HuggingFace Papers page
3. 📥 Downloads detailed info for each paper
4. 💾 Saves to daily/weekly/monthly archives
5. 📝 Generates this beautiful README
6. ✅ Commits and pushes updates

---

## 🤝 Contributing

Found a bug or have a feature request? 

- 🐛 [Report Issues](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/issues)
- 💡 [Submit Ideas](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/discussions)
- 🔧 [Pull Requests Welcome](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/pulls)

---

## 📜 License

MIT License - feel free to use this data for your own projects!

See [LICENSE](LICENSE) for more details.

---

## 🌟 Star History

If you find this useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=AtharvaDomale/Daily-HuggingFace-AI-Papers&type=Date)](https://star-history.com/#AtharvaDomale/Daily-HuggingFace-AI-Papers&Date)

---

## 📬 Contact & Support

- 💬 [GitHub Discussions](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/discussions)
- 🐛 [Issue Tracker](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/issues)
- ⭐ Don't forget to star this repo!

---

<div align="center">

**Made with ❤️ for the AI Community**

[⬆ Back to Top](#-daily-huggingface-ai-papers)

</div>
