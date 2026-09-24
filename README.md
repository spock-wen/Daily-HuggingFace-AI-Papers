<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-24-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7520+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">24</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">84</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">540</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7520+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 24, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. HappyWorld-Bench</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24308) • [📄 arXiv](https://arxiv.org/abs/2609.24308) • [📥 PDF](https://arxiv.org/pdf/2609.24308)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Evaluating world models requires assessing both the quality of the worlds they generate and their consistency and responsiveness under exploration, interaction, and modification. We introduce HappyWorld-Bench, a comprehensive benchmark that evalua...

</details>

<details>
<summary><b>2. The Past Frames the Future: Memory for Autoregressive Video Generation</b> ⭐ 30</summary>

<br/>

**👥 Authors:** Hongfei Zhang, Wen-Jie Shu, Disen Lan, Rongjin Guo, Harold328

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.28466) • [📄 arXiv](https://arxiv.org/abs/2609.28466) • [📥 PDF](https://arxiv.org/pdf/2609.28466)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HaroldChen19/Awesome-AR-Video-Memory)

> The first survey on memory mechanisms for AR video generation.

</details>

<details>
<summary><b>3. SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue</b> ⭐ 70</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.26780) • [📄 arXiv](https://arxiv.org/abs/2609.26780) • [📥 PDF](https://arxiv.org/pdf/2609.26780)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/2022hpsk/SpeakerMemR1)

> Excited to share our work on SpeakerMem-R1 ! Recent benchmarks reveal a surprising gap: general-purpose memory systems struggle with multi-party conversations and can even underperform simple BM25 retrieval in some settings. These limitations high...

</details>

<details>
<summary><b>4. Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23038) • [📄 arXiv](https://arxiv.org/abs/2609.23038) • [📥 PDF](https://arxiv.org/pdf/2609.23038)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJU-OmniAI/Spatial-Interactor)

> Understanding a scene means more than recognizing what is visible: it also requires reasoning about how space changes through interaction. We introduce Spatial-Interactor, a framework for learning local state transitions and long-horizon spatial r...

</details>

<details>
<summary><b>5. RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.22947) • [📄 arXiv](https://arxiv.org/abs/2609.22947) • [📥 PDF](https://arxiv.org/pdf/2609.22947)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/2kxx/RewardVerse)

> Reinforcement learning (RL) is vital for optimizing video generation models, with a robust reward model (RM) serving as the cornerstone. However, existing video reward models often produce unstable scalar scores because they directly map complex, ...

</details>

<details>
<summary><b>6. Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27334) • [📄 arXiv](https://arxiv.org/abs/2609.27334) • [📥 PDF](https://arxiv.org/pdf/2609.27334)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most agent memory is curated at write time: the system distills each trajectory into a fixed artifact before it knows what the next task will need, losing information and leaving a painfully delayed learning signal. JitMem flips this by storing ra...

</details>

<details>
<summary><b>7. PACT: From Credit Assignment to Critic Alignment</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.26355) • [📄 arXiv](https://arxiv.org/abs/2609.26355) • [📥 PDF](https://arxiv.org/pdf/2609.26355)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We characterize token-level credit through three conditions that uniquely determine its form, and use this perspective to understand RLOO, GAE, and on-policy distillation. These insights lead to PACT, which improves critic learning and alignment w...

</details>

<details>
<summary><b>8. Schrödinger's Code Repository: Have LLMs Learned SWE-bench or Memorized It?</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27891) • [📄 arXiv](https://arxiv.org/abs/2609.27891) • [📥 PDF](https://arxiv.org/pdf/2609.27891)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/cslsolow/Schrodinger-Repo)

> What if a code repository were like Schrödinger’s cat—its final form only revealed when the agent opens the box? We introduce Schrödinger’s Repository : at evaluation time, the same SWE task “collapses” into a behavior-equivalent but unfamiliar re...

</details>

<details>
<summary><b>9. GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25963) • [📄 arXiv](https://arxiv.org/abs/2609.25963) • [📥 PDF](https://arxiv.org/pdf/2609.25963)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Solve w.r.t different spaces

</details>

<details>
<summary><b>10. PackLab: A Comprehensive Framework for Developing, Training, and Evaluating MLLMs in Robotic Bin Packing</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23784) • [📄 arXiv](https://arxiv.org/abs/2609.23784) • [📥 PDF](https://arxiv.org/pdf/2609.23784)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Correr-Zhou/PackLab)

> Code : https://github.com/Correr-Zhou/PackLab Model : https://huggingface.co/donghao-zhou/PackLab-VLM-9B Dataset : https://huggingface.co/datasets/donghao-zhou/PackData-20K Benchmark : https://huggingface.co/datasets/donghao-zhou/PackLab-Bench

</details>

<details>
<summary><b>11. MemBodied: Recurrent Associative Memory for Vision-Language-Action Models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jianfei Yang, Raphael Yee, Bryce Goh, Navonil Majumder, Tej Deep Pala

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.28256) • [📄 arXiv](https://arxiv.org/abs/2609.28256) • [📥 PDF](https://arxiv.org/pdf/2609.28256)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/declare-lab/MemBodied)

> Recurrent Associative Memory for VLAs

</details>

<details>
<summary><b>12. WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27490) • [📄 arXiv](https://arxiv.org/abs/2609.27490) • [📥 PDF](https://arxiv.org/pdf/2609.27490)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EthanNing/WhatWorkedBench)

> Benchmarking Experimental Understanding in AI Agents

</details>

<details>
<summary><b>13. Hunyuan-A13B Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27284) • [📄 arXiv](https://arxiv.org/abs/2609.27284) • [📥 PDF](https://arxiv.org/pdf/2609.27284)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27901) • [📄 arXiv](https://arxiv.org/abs/2609.27901) • [📥 PDF](https://arxiv.org/pdf/2609.27901)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ohad204/RecCAR)

> Video is a rich representation of a physical event, capturing appearance, geometry, motion, and temporal evolution. Other modalities, such as 3D body motion or audio, encode narrower aspects of the same event. We find that joint multimodal diffusi...

</details>

<details>
<summary><b>15. Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27321) • [📄 arXiv](https://arxiv.org/abs/2609.27321) • [📥 PDF](https://arxiv.org/pdf/2609.27321)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>16. InternW0: A Foundational Physical World Model for Efficient Real-World Interactions</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhangzheng Tu, Zhe Cao, Ganlin Yang, Yao Mu, Jisong Cai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27656) • [📄 arXiv](https://arxiv.org/abs/2609.27656) • [📥 PDF](https://arxiv.org/pdf/2609.27656)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. On the Diffusibility of High-Dimensional Latents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiyao Wang, Yuanjun Xiong, Bowei Chen, Zhiyang Xu, Chao Feng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.28473) • [📄 arXiv](https://arxiv.org/abs/2609.28473) • [📥 PDF](https://arxiv.org/pdf/2609.28473)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Representation Autoencoders (RAEs) enable diffusion models to operate in the feature spaces of pretrained visual encoders. However, many off-the-shelf encoders are not optimized for faithful reconstruction, discarding fine-grained visual details. ...

</details>

<details>
<summary><b>18. EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics</b> ⭐ 16</summary>

<br/>

**👥 Authors:** Lihan Zha, Zhicheng Zheng, Yilang Liu, Zeyu Shen, Haoxiang You

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27308) • [📄 arXiv](https://arxiv.org/abs/2609.27308) • [📥 PDF](https://arxiv.org/pdf/2609.27308)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EmbodiedSWE/EmbodiedSWE)

> EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics

</details>

<details>
<summary><b>19. Calibration as a First-Class Criterion in LLM Evaluation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Katharina von der Wense, mario-sanz

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.26489) • [📄 arXiv](https://arxiv.org/abs/2609.26489) • [📥 PDF](https://arxiv.org/pdf/2609.26489)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present a position paper arguing that calibration should be measured as a primary criterion in LLM evaluation. We discuss the consequences of neglecting it for both deployment and development, and outline directions for closing this gap.

</details>

<details>
<summary><b>20. Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Nicki Skafte Detlefsen, rasgaard

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27980) • [📄 arXiv](https://arxiv.org/abs/2609.27980) • [📥 PDF](https://arxiv.org/pdf/2609.27980)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/rasgaard/whisper-encoder-layer-prune)

> Paper describes how Whisper's encoder can have many of its layers pruned away with minimal damage to downstream performance. And even then performance can be recovered effectively through distillation.

</details>

<details>
<summary><b>21. StudentBench: AI and human tutoring yield equivalent GRE learning gains</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.28470) • [📄 arXiv](https://arxiv.org/abs/2609.28470) • [📥 PDF](https://arxiv.org/pdf/2609.28470)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Handshake-AI-Research/studentbench)

> We introduce StudentBench, a suite of AI teaching evaluations and a public platform for measuring how well AI helps people learn. The paper compares AI tutoring, expert human tutoring, and a no tutoring control on Quantitative and Verbal GRE learn...

</details>

<details>
<summary><b>22. FLEET: From Logits Entropy to Enhanced Trajectories in Text Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Oleksandra Vitko, Alexiush

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.27657) • [📄 arXiv](https://arxiv.org/abs/2609.27657) • [📥 PDF](https://arxiv.org/pdf/2609.27657)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Alexiush/fleet)

> Solutions based on large language models (LLMs) often rely on temperature sampling to improve accuracy and stability by aggregating multiple samples from the completion distribution. However, this memoryless approach is inherently suboptimal: beca...

</details>

<details>
<summary><b>23. Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24815) • [📄 arXiv](https://arxiv.org/abs/2609.24815) • [📥 PDF](https://arxiv.org/pdf/2609.24815)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/D-Robotics-AI-Lab/Uranus-OSS) • [⭐ Code](https://github.com/D-Robotics-AI-Lab/Uranus-SDK)

> 🚀 Uranus : a data-driven robot simulator built around a joint-trajectory conditioned autoregressive diffusion model. 🔄 Streaming, open-ended rollout Uranus takes future joint-position trajectories online and autoregressively generates one latent f...

</details>

<details>
<summary><b>24. MemoryAthena: Adaptive Routing over Latent and Generated Memories</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25853) • [📄 arXiv](https://arxiv.org/abs/2609.25853) • [📥 PDF](https://arxiv.org/pdf/2609.25853)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OLAResearch/ATHENA)

> MemoryAthena explores a simple question: can useful memory be generated rather than only retrieved from storage? It combines direct Engram retrieval with two generated-memory pathways and learns a lightweight causal router that selectively decides...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 24 |
| 📅 Today | [`2026-09-24.json`](data/daily/2026-09-24.json) | 24 |
| 📆 This Week | [`2026-W38.json`](data/weekly/2026-W38.json) | 84 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 540 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-24 | 24 | [View JSON](data/daily/2026-09-24.json) |
| 📄 2026-09-23 | 18 | [View JSON](data/daily/2026-09-23.json) |
| 📄 2026-09-22 | 21 | [View JSON](data/daily/2026-09-22.json) |
| 📄 2026-09-21 | 21 | [View JSON](data/daily/2026-09-21.json) |
| 📄 2026-09-20 | 24 | [View JSON](data/daily/2026-09-20.json) |
| 📄 2026-09-19 | 24 | [View JSON](data/daily/2026-09-19.json) |
| 📄 2026-09-18 | 19 | [View JSON](data/daily/2026-09-18.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W38 | 84 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 540 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |

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
