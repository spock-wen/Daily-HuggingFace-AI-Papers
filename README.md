<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-22-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5732+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">22</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">91</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">44</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5732+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 02, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.28322) • [📄 arXiv](https://arxiv.org/abs/2606.28322) • [📥 PDF](https://arxiv.org/pdf/2606.28322)

**💻 Code:** [⭐ Code](https://github.com/M1chaelPeng/PerceptionRubrics) • [⭐ Code](https://github.com/huggingface)

> We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRu...

</details>

<details>
<summary><b>2. MemSyco-Bench: Benchmarking Sycophancy in Agent Memory</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Ruqin Ning, Zhimin Wei, Yunbo Tang, Zerui Chen, Zhishang Xiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.01071) • [📄 arXiv](https://arxiv.org/abs/2607.01071) • [📥 PDF](https://arxiv.org/pdf/2607.01071)

**💻 Code:** [⭐ Code](https://github.com/XMUDeepLIT/MemSyco-Bench) • [⭐ Code](https://github.com/huggingface)

> Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycoph...

</details>

<details>
<summary><b>3. TurboServe: Serving Streaming Video Generation Efficiently and Economically</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19271) • [📄 arXiv](https://arxiv.org/abs/2606.19271) • [📥 PDF](https://arxiv.org/pdf/2606.19271)

**💻 Code:** [⭐ Code](https://github.com/shengshu-ai/TurboServe) • [⭐ Code](https://github.com/huggingface)

> We present TurboServe, the first serving system designed specifically for streaming video generation workloads. TurboServe formulates serving as an online scheduling problem that jointly coordinates session placement and GPU provisioning. Its clos...

</details>

<details>
<summary><b>4. ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00466) • [📄 arXiv](https://arxiv.org/abs/2607.00466) • [📥 PDF](https://arxiv.org/pdf/2607.00466)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This papers optimizes PD disaggregation for LLM serving by proposing new routing algorithm for reducing the number of activated experts.

</details>

<details>
<summary><b>5. Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00666) • [📄 arXiv](https://arxiv.org/abs/2607.00666) • [📥 PDF](https://arxiv.org/pdf/2607.00666)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/snumprlab/dart)

> Accepted at ECCV 2026. Domain Arithmetic (DART) adapts multi-task VLAs to environmental shifts (e.g., camera-pose changes, embodiment changes) using a single demo of a single task through subspace-aligned weight arithmetic.

</details>

<details>
<summary><b>6. Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chaofan Gan, Tieyuan Chen, Siyuan Yang, Yilin Gao, Shijie Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00461) • [📄 arXiv](https://arxiv.org/abs/2607.00461) • [📥 PDF](https://arxiv.org/pdf/2607.00461)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AMVL distinguishes itself by moving beyond both discrete text and simple latent compression, using an asymmetric variational objective to ensure that high-fidelity, continuous reasoning pathways remain stable and effective when moving from trainin...

</details>

<details>
<summary><b>7. Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.01191) • [📄 arXiv](https://arxiv.org/abs/2607.01191) • [📥 PDF](https://arxiv.org/pdf/2607.01191)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJU-REAL/Perceive-to-Reason)

> This paper proposes P2R, a two-stage framework that decouples fine-grained visual reasoning into perception and reasoning, trained with PRA-GRPO, a role-aware alternating RL strategy requiring only final-answer supervision without bounding box ann...

</details>

<details>
<summary><b>8. CausalMix: Data Mixture as Causal Inference for Language Model Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.01104) • [📄 arXiv](https://arxiv.org/abs/2607.01104) • [📥 PDF](https://arxiv.org/pdf/2607.01104)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 22 pages, 3 figures, code is under review

</details>

<details>
<summary><b>9. ASPIRE: Agentic /Skills Discovery for Robotics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00272) • [📄 arXiv](https://arxiv.org/abs/2607.00272) • [📥 PDF](https://arxiv.org/pdf/2607.00272)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. BioInsight: Multi-Agent Orchestration for Interactive Biomedical Knowledge Discovery</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Desong Meng, Nanyi Jiang, Bingxuan Li, JiayuJeff, Joysw909

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.20997) • [📄 arXiv](https://arxiv.org/abs/2606.20997) • [📥 PDF](https://arxiv.org/pdf/2606.20997)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> BioInsight converts disease-centered protein evidence into an interactive evidence interface. The system uses agent-produced artifacts for search, reasoning, report writing, and dashboard construction, so users can move from high-level hypotheses ...

</details>

<details>
<summary><b>11. Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00248) • [📄 arXiv](https://arxiv.org/abs/2607.00248) • [📥 PDF](https://arxiv.org/pdf/2607.00248)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. Cross-Domain Generalization Failure in Lightweight Intrusion Detection Models for IIoT Networks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Talha Ibne Anis, Md Shihab Uddin, MD Azizul Hakim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00553) • [📄 arXiv](https://arxiv.org/abs/2607.00553) • [📥 PDF](https://arxiv.org/pdf/2607.00553)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most lightweight IDS papers for IIoT report near-perfect accuracy — but almost always tested on the same network they were trained on. We wanted to know: does that performance actually survive when the model meets a different industrial network? W...

</details>

<details>
<summary><b>13. The State-Prediction Separation Hypothesis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.01218) • [📄 arXiv](https://arxiv.org/abs/2607.01218) • [📥 PDF](https://arxiv.org/pdf/2607.01218)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Code coming soon!

</details>

<details>
<summary><b>14. ABot-M0.5: Unified Mobility-and-Manipulation World Action Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tong Lin, Dongjie Huo, Zuojin Tang, Yandan Yang, Ronghan Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00678) • [📄 arXiv](https://arxiv.org/abs/2607.00678) • [📥 PDF](https://arxiv.org/pdf/2607.00678)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/amap-cvlab/ABot-Manipulation)

> Github: https://github.com/amap-cvlab/ABot-Manipulation

</details>

<details>
<summary><b>15. Valdi: Value Diffusion World Models</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Kashyap Chitta, Christopher Lindenberg

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00917) • [📄 arXiv](https://arxiv.org/abs/2607.00917) • [📥 PDF](https://arxiv.org/pdf/2607.00917)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Kit115/ValueDiffusionWorldModels)

> No abstract available.

</details>

<details>
<summary><b>16. Autonomous Scientific Discovery via Iterative Meta-Reflection</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Oisin Mac Aodha, Sara Beery, Bingchen Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.01131) • [📄 arXiv](https://arxiv.org/abs/2607.01131) • [📥 PDF](https://arxiv.org/pdf/2607.01131)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.32029) • [📄 arXiv](https://arxiv.org/abs/2606.32029) • [📥 PDF](https://arxiv.org/pdf/2606.32029)

**💻 Code:** [⭐ Code](https://github.com/ayyyq/table-referencing) • [⭐ Code](https://github.com/huggingface)

> We define, evaluate and mitigate data referencing errors in table tasks.

</details>

<details>
<summary><b>18. AutoTrainess: Teaching Language Models to Improve Language Models Autonomously</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Kai Cai, Shilin He, Shuzheng Gao, Penghao Yin, Zhaojian Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31551) • [📄 arXiv](https://arxiv.org/abs/2606.31551) • [📥 PDF](https://arxiv.org/pdf/2606.31551)

**💻 Code:** [⭐ Code](https://github.com/simple-agent-lab/AutoTrainess) • [⭐ Code](https://github.com/huggingface)

> AutoTrainess: Teaching Language Models to Improve Language Models Autonomously

</details>

<details>
<summary><b>19. Personalization as Inverse Planning: Learning Latent Design Intents for Agentic Slide Generation via Structural Denoising</b> ⭐ 0</summary>

<br/>

**👥 Authors:** jing Gao, Haoyu Wang, Linjun Zhang, Zihan Dong, Tianci Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00407) • [📄 arXiv](https://arxiv.org/abs/2607.00407) • [📥 PDF](https://arxiv.org/pdf/2607.00407)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Slide design requires personalizing both deck themes and page layouts. Yet, current AI agent-based methods struggle with fine-grained, page-level design. Solely relying on prespecified templates or user verbose instructions, they fail to capture l...

</details>

<details>
<summary><b>20. AtomiMed: Hierarchical Atomic Fact-Checking for Universal Clinical-Aware Medical Report Evaluation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31292) • [📄 arXiv](https://arxiv.org/abs/2606.31292) • [📥 PDF](https://arxiv.org/pdf/2606.31292)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Venn2336/MRGEvalkit)

> Official submission of our paper introducing OmniMRG-Bench, a comprehensive benchmark for universal medical report evaluation across multiple imaging modalities. The paper also presents AtomiMed, a hierarchical atomic fact-checking framework that ...

</details>

<details>
<summary><b>21. NoPA: Non-Parametric Online 3D Scene Graph Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00529) • [📄 arXiv](https://arxiv.org/abs/2607.00529) • [📥 PDF](https://arxiv.org/pdf/2607.00529)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Accepted to ECCV 2026.

</details>

<details>
<summary><b>22. AI translation of literary texts is "fine", but readers still prefer human translations</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Maite Taboada, Roman Grundkiewicz, Ty Brassington, Adam Podoxin, YvesFrtl

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.26040) • [📄 arXiv](https://arxiv.org/abs/2606.26040) • [📥 PDF](https://arxiv.org/pdf/2606.26040)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yves575/lait)

> AI translation is continually getting more attention. Translating a fictional work has never been as easy and fast when using AI. So what is lost in AI literary translation? To answer this question, we asked 15 avid readers to read two novel excer...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 22 |
| 📅 Today | [`2026-07-02.json`](data/daily/2026-07-02.json) | 22 |
| 📆 This Week | [`2026-W26.json`](data/weekly/2026-W26.json) | 91 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 44 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-02 | 22 | [View JSON](data/daily/2026-07-02.json) |
| 📄 2026-07-01 | 22 | [View JSON](data/daily/2026-07-01.json) |
| 📄 2026-06-30 | 32 | [View JSON](data/daily/2026-06-30.json) |
| 📄 2026-06-29 | 15 | [View JSON](data/daily/2026-06-29.json) |
| 📄 2026-06-28 | 25 | [View JSON](data/daily/2026-06-28.json) |
| 📄 2026-06-27 | 25 | [View JSON](data/daily/2026-06-27.json) |
| 📄 2026-06-26 | 18 | [View JSON](data/daily/2026-06-26.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W26 | 91 | [View JSON](data/weekly/2026-W26.json) |
| 📅 2026-W25 | 155 | [View JSON](data/weekly/2026-W25.json) |
| 📅 2026-W24 | 194 | [View JSON](data/weekly/2026-W24.json) |
| 📅 2026-W23 | 247 | [View JSON](data/weekly/2026-W23.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 44 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |

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
