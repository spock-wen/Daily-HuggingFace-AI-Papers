<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-25-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-2477+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">25</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">66</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">958</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">2477+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** February 25, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. A Very Big Video Reasoning Suite</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20159) • [📄 arXiv](https://arxiv.org/abs/2602.20159) • [📥 PDF](https://arxiv.org/pdf/2602.20159)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API UReason: Benchmarking the Reasoning Paradox in Unified Multimodal Models (2...

</details>

<details>
<summary><b>2. VLANeXt: Recipes for Building Strong VLA Models</b> ⭐ 43</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18532) • [📄 arXiv](https://arxiv.org/abs/2602.18532) • [📥 PDF](https://arxiv.org/pdf/2602.18532)

**💻 Code:** [⭐ Code](https://github.com/DravenALG/awesome-vla) • [⭐ Code](https://github.com/DravenALG/VLANeXt)

> Project Page: https://dravenalg.github.io/VLANeXt/ Github: https://github.com/DravenALG/VLANeXt Model: https://huggingface.co/DravenALG/VLANeXt Awesome-VLA: https://github.com/DravenALG/awesome-vla

</details>

<details>
<summary><b>3. SkillOrchestra: Learning to Route Agents via Skill Transfer</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19672) • [📄 arXiv](https://arxiv.org/abs/2602.19672) • [📥 PDF](https://arxiv.org/pdf/2602.19672)

> Compound AI systems promise capabilities beyond those of individual models, yet their success depends critically on effective orchestration. Existing routing approaches face two limitations: (1) input-level routers make coarse query-level decision...

</details>

<details>
<summary><b>4. ManCAR: Manifold-Constrained Latent Reasoning with Adaptive Test-Time Computation for Sequential Recommendation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20093) • [📄 arXiv](https://arxiv.org/abs/2602.20093) • [📥 PDF](https://arxiv.org/pdf/2602.20093)

**💻 Code:** [⭐ Code](https://github.com/FuCongResearchSquad/ManCAR)

> Sequential recommendation increasingly employs latent multi-step reasoning to enhance test-time computation. Despite empirical gains, existing approaches largely drive intermediate reasoning states via target-dominant objectives without imposing e...

</details>

<details>
<summary><b>5. TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19313) • [📄 arXiv](https://arxiv.org/abs/2602.19313) • [📥 PDF](https://arxiv.org/pdf/2602.19313)

**💻 Code:** [⭐ Code](https://github.com/TOPReward/TOPReward)

> While Vision-Language-Action (VLA) models have seen rapid progress in pretraining, their advancement in Reinforcement Learning (RL) remains hampered by low sample efficiency and sparse rewards in real-world settings. Developing generalizable proce...

</details>

<details>
<summary><b>6. Mobile-O: Unified Multimodal Understanding and Generation on Mobile Device</b> ⭐ 35</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20161) • [📄 arXiv](https://arxiv.org/abs/2602.20161) • [📥 PDF](https://arxiv.org/pdf/2602.20161)

**💻 Code:** [⭐ Code](https://github.com/Amshaker/Mobile-O)

> TL;DR: Introducing Mobile-O What it is: A compact, unified multimodal model that brings both visual understanding and image generation directly to mobile devices. The Breakthrough: It eliminates cloud dependency for multimodal AI. Using a novel "M...

</details>

<details>
<summary><b>7. Agents of Chaos</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Koyena Pal, Gabriele Sarti, Avery Yen, Chris Wendler, Natalie Shapira

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20021) • [📄 arXiv](https://arxiv.org/abs/2602.20021) • [📥 PDF](https://arxiv.org/pdf/2602.20021)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API A Survey of Agentic AI and Cybersecurity: Challenges, Opportunities and Use...

</details>

<details>
<summary><b>8. Learning Cross-View Object Correspondence via Cycle-Consistent Mask Prediction</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Hongyang Wei, Jingchen Ni, Keyu Lv, Leqi Zheng, ysner

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18996) • [📄 arXiv](https://arxiv.org/abs/2602.18996) • [📥 PDF](https://arxiv.org/pdf/2602.18996)

**💻 Code:** [⭐ Code](https://github.com/shannany0606/CCMP)

> The paper has been accepted to CVPR 2026 with a high review score of 554. Our approach is intentionally simple and effective. We use a straightforward pipeline, and show that such a simple design can already achieve strong performance and generali...

</details>

<details>
<summary><b>9. SimToolReal: An Object-Centric Policy for Zero-Shot Dexterous Tool Manipulation</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16863) • [📄 arXiv](https://arxiv.org/abs/2602.16863) • [📥 PDF](https://arxiv.org/pdf/2602.16863)

**💻 Code:** [⭐ Code](https://github.com/tylerlum/simtoolreal)

> 🤖 Can a single robot policy manipulate diverse tools without ever seeing them before? Introducing SimToolReal 🔨: a generalist dexterous manipulation policy that transfers zero-shot sim→real to unseen tools + unseen tasks. All videos are 1× speed (...

</details>

<details>
<summary><b>10. DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Donghao Zhou, Zhihao Dou, Yun Shen, Zhongwei Wan, Zixuan8642

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19895) • [📄 arXiv](https://arxiv.org/abs/2602.19895) • [📥 PDF](https://arxiv.org/pdf/2602.19895)

> Reinforcement learning with verifiers (RLVR) is a central paradigm for improving large language model (LLM) reasoning, yet existing methods often suffer from limited exploration. Policies tend to collapse onto a few reasoning patterns and prematur...

</details>

<details>
<summary><b>11. RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18742) • [📄 arXiv](https://arxiv.org/abs/2602.18742) • [📥 PDF](https://arxiv.org/pdf/2602.18742)

> 🚀 RoboCurate — Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning 📄 Paper: https://arxiv.org/abs/2602.18742 ￼ 🔎 What we do: Propose RoboCurate, a synthetic robot data generation framework that improves neural trajectory...

</details>

<details>
<summary><b>12. DODO: Discrete OCR Diffusion Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16872) • [📄 arXiv](https://arxiv.org/abs/2602.16872) • [📥 PDF](https://arxiv.org/pdf/2602.16872)

> TL;DR – OCR is an almost deterministic task, which enables, in theory, parallel decoding. We realize this potential by training a Block Masked Diffusion Model. We achieve competitive results with SOTA autoregressive OCR VLMs, while decoding more t...

</details>

<details>
<summary><b>13. Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Ayushi Kishore, Jinxin Yang, Songtao Wei, Yi Li, Dongming Jiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19320) • [📄 arXiv](https://arxiv.org/abs/2602.19320) • [📥 PDF](https://arxiv.org/pdf/2602.19320)

**💻 Code:** [⭐ Code](https://github.com/FredJiang0324/Anatomy-of-Agentic-Memory)

> We present a comprehensive survey on agentic memory for LLMs, including a unified taxonomy and empirical analysis of current systems and evaluation limitations. We release the paper along with an open-source repository to support future research. ...

</details>

<details>
<summary><b>14. K-Search: LLM Kernel Generation via Co-Evolving Intrinsic World Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ion Stoica, Joseph E. Gonzalez, Ziming Mao, Shiyi Cao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19128) • [📄 arXiv](https://arxiv.org/abs/2602.19128) • [📥 PDF](https://arxiv.org/pdf/2602.19128)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API KernelBlaster: Continual Cross-Task CUDA Optimization via Memory-Augmented ...

</details>

<details>
<summary><b>15. tttLRM: Test-Time Training for Long Context and Autoregressive 3D Reconstruction</b> ⭐ 62</summary>

<br/>

**👥 Authors:** Zhiqin Chen, Wang Yifan, Hao Tan, Yuheng02, chenwang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20160) • [📄 arXiv](https://arxiv.org/abs/2602.20160) • [📥 PDF](https://arxiv.org/pdf/2602.20160)

**💻 Code:** [⭐ Code](https://github.com/cwchenwang/tttLRM)

> Project Page: https://cwchenwang.github.io/tttLRM/ . Code has been opensourced.

</details>

<details>
<summary><b>16. Nacrith: Neural Lossless Compression via Ensemble Context Modeling and High-Precision CDF Coding</b> ⭐ 7</summary>

<br/>

**👥 Authors:** robtacconelli

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19626) • [📄 arXiv](https://arxiv.org/abs/2602.19626) • [📥 PDF](https://arxiv.org/pdf/2602.19626)

**💻 Code:** [⭐ Code](https://github.com/robtacconelli/Nacrith-GPU)

> Github repository https://github.com/robtacconelli/Nacrith-GPU Try on Huggingface https://huggingface.co/spaces/robtacconelli/Nacrith-GPU

</details>

<details>
<summary><b>17. SimVLA: A Simple VLA Baseline for Robotic Manipulation</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18224) • [📄 arXiv](https://arxiv.org/abs/2602.18224) • [📥 PDF](https://arxiv.org/pdf/2602.18224)

**💻 Code:** [⭐ Code](https://github.com/LUOyk1999/SimVLA)

> A streamlined Vision-Language-Action (VLA) baseline for robotic manipulation, designed for transparency and reproducibility.

</details>

<details>
<summary><b>18. AAVGen: Precision Engineering of Adeno-associated Viral Capsids for Renal Selective Targeting</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Yousof Gheisari, Mohammadreza Ghaffarzadeh-Esfahani

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18915) • [📄 arXiv](https://arxiv.org/abs/2602.18915) • [📥 PDF](https://arxiv.org/pdf/2602.18915)

**💻 Code:** [⭐ Code](https://github.com/mohammad-gh009/AAVGen)

> AAVGen is a generative AI framework for designing adeno-associated virus (AAV) capsids with enhanced multi-trait profiles. By integrating a protein language model (ProtGPT2) with supervised fine-tuning and group sequence policy optimization (GSPO)...

</details>

<details>
<summary><b>19. Decoding ML Decision: An Agentic Reasoning Framework for Large-Scale Ranking System</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18640) • [📄 arXiv](https://arxiv.org/abs/2602.18640) • [📥 PDF](https://arxiv.org/pdf/2602.18640)

> Modern large-scale ranking systems operate within a sophisticated landscape of competing objectives, operational constraints, and evolving product requirements. Progress in this domain is increasingly bottlenecked by the engineering context constr...

</details>

<details>
<summary><b>20. Contact-Anchored Proprioceptive Odometry for Quadruped Robots</b> ⭐ 132</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.17393) • [📄 arXiv](https://arxiv.org/abs/2602.17393) • [📥 PDF](https://arxiv.org/pdf/2602.17393)

**💻 Code:** [⭐ Code](https://github.com/ShineMinxing/Ros2Go2Estimator)

> Astrall exp(3D loop): traverse 200 m horizontally + 15 m vertical change; return-to-origin errors = 0.1638 m (XY), 0.219 m (Z) for point-foot, and 0.2264 m (XY), 0.199 m (Z) for wheel-legged. Astrall raw logs not released due to data restrictions....

</details>

<details>
<summary><b>21. AssetFormer: Modular 3D Assets Generation with Autoregressive Transformer</b> ⭐ 26</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12100) • [📄 arXiv](https://arxiv.org/abs/2602.12100) • [📥 PDF](https://arxiv.org/pdf/2602.12100)

**💻 Code:** [⭐ Code](https://github.com/Advocate99/AssetFormer)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API CG-MLLM: Captioning and Generating 3D content via Multi-modal Large Languag...

</details>

<details>
<summary><b>22. SenTSR-Bench: Thinking with Injected Knowledge for Time-Series Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haotian Lin, Shuai Zhang, Xiyuan Zhang, Boran Han, Zelin He

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19455) • [📄 arXiv](https://arxiv.org/abs/2602.19455) • [📥 PDF](https://arxiv.org/pdf/2602.19455)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Time Series Reasoning via Process-Verifiable Thinking Data Synthesis and Sc...

</details>

<details>
<summary><b>23. Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19089) • [📄 arXiv](https://arxiv.org/abs/2602.19089) • [📥 PDF](https://arxiv.org/pdf/2602.19089)

**💻 Code:** [⭐ Code](https://github.com/qiisun/ani3dhuman)

> Github: https://github.com/qiisun/ani3dhuman

</details>

<details>
<summary><b>24. Large Causal Models for Temporal Causal Discovery</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dario Simionato, Bora Caglayan, MingXue Wang, Nikolaos Gkorgkolis, Nikolaos Kougioulis

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18662) • [📄 arXiv](https://arxiv.org/abs/2602.18662) • [📥 PDF](https://arxiv.org/pdf/2602.18662)

> This paper introduces Large Causal Models, foundation models for Causal Discovery (CD) on time-series data following a supervised learning scheme. It expands prior proof-of-concept approaches by combining hundends of thousands of synthetic and rea...

</details>

<details>
<summary><b>25. On the "Induction Bias" in Sequence Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18333) • [📄 arXiv](https://arxiv.org/abs/2602.18333) • [📥 PDF](https://arxiv.org/pdf/2602.18333)

> Transformers are data‑hungry in sequential tasks because they lack the right inductive bias. It’s well known that for many sequential problems (from adding numbers to step‑by‑step agentic execution and multi‑hop reasoning), transformers fail to ge...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 25 |
| 📅 Today | [`2026-02-25.json`](data/daily/2026-02-25.json) | 25 |
| 📆 This Week | [`2026-W08.json`](data/weekly/2026-W08.json) | 66 |
| 🗓️ This Month | [`2026-02.json`](data/monthly/2026-02.json) | 958 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-02-25 | 25 | [View JSON](data/daily/2026-02-25.json) |
| 📄 2026-02-24 | 18 | [View JSON](data/daily/2026-02-24.json) |
| 📄 2026-02-23 | 23 | [View JSON](data/daily/2026-02-23.json) |
| 📄 2026-02-22 | 23 | [View JSON](data/daily/2026-02-22.json) |
| 📄 2026-02-21 | 23 | [View JSON](data/daily/2026-02-21.json) |
| 📄 2026-02-20 | 18 | [View JSON](data/daily/2026-02-20.json) |
| 📄 2026-02-19 | 25 | [View JSON](data/daily/2026-02-19.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W08 | 66 | [View JSON](data/weekly/2026-W08.json) |
| 📅 2026-W07 | 197 | [View JSON](data/weekly/2026-W07.json) |
| 📅 2026-W06 | 293 | [View JSON](data/weekly/2026-W06.json) |
| 📅 2026-W05 | 357 | [View JSON](data/weekly/2026-W05.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-02 | 958 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |
| 🗓️ 2025-12 | 787 | [View JSON](data/monthly/2025-12.json) |

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
