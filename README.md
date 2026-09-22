<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-21-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7478+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">21</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">42</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">498</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7478+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 22, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Transferring the Intelligence of VLMs to Robotic Control</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kejin Wang, Jia-Jun Wang, Meng-Hao Guo, uyzhang, Mo-ZheHan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.22966) • [📄 arXiv](https://arxiv.org/abs/2609.22966) • [📥 PDF](https://arxiv.org/pdf/2609.22966)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Three main findings Strong performance on RoboDojo: The method achieves over 47% success rate on the challenging RoboDojo benchmark, setting a strong baseline for long-horizon robot manipulation tasks. In-Context Learning works for robotics: The p...

</details>

<details>
<summary><b>2. WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24984) • [📄 arXiv](https://arxiv.org/abs/2609.24984) • [📥 PDF](https://arxiv.org/pdf/2609.24984)

**💻 Code:** [⭐ Code](https://github.com/TencentARC/WorldCrafter) • [⭐ Code](https://github.com/huggingface)

> We introduce WorldCrafter, a video world model with a camera-queryable implicit 3D-aware memory for consistent, long-horizon scene exploration. Starting from a single image or text prompt, WorldCrafter combines historical observations, recent temp...

</details>

<details>
<summary><b>3. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24972) • [📄 arXiv](https://arxiv.org/abs/2609.24972) • [📥 PDF](https://arxiv.org/pdf/2609.24972)

**💻 Code:** [⭐ Code](https://github.com/google-research/rrsi) • [⭐ Code](https://github.com/huggingface)

> We released the Regularized Recursive Self-Improvement of Agent Harnesses! Check it out!

</details>

<details>
<summary><b>4. GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25001) • [📄 arXiv](https://arxiv.org/abs/2609.25001) • [📥 PDF](https://arxiv.org/pdf/2609.25001)

**💻 Code:** [⭐ Code](https://github.com/TencentARC/GameHorizon) • [⭐ Code](https://github.com/huggingface)

> We introduce GameHorizon, a large-scale data and evaluation suite spanning multiple temporal horizons and diverse AAA games. It serves as a standardized yardstick across a broad range of model families, including VLMs, UMMs, GUI agents, coding age...

</details>

<details>
<summary><b>5. Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24220) • [📄 arXiv](https://arxiv.org/abs/2609.24220) • [📥 PDF](https://arxiv.org/pdf/2609.24220)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> D-RAC: Universal Retrieval-Aware Ingestion of Enterprise Documents Enterprise RAG has to ingest PDFs, DOCX, PPTX, XLSX and scans — formats where text extraction breaks reading order, flattens tables and loses heading hierarchy. Agentic chunking re...

</details>

<details>
<summary><b>6. OmniEdu: Open Foundation Models for Learning and Teaching</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23088) • [📄 arXiv](https://arxiv.org/abs/2609.23088) • [📥 PDF](https://arxiv.org/pdf/2609.23088)

**💻 Code:** [⭐ Code](https://github.com/haolpku/Omni-Edu) • [⭐ Code](https://github.com/huggingface)

> Excited to release OmniEdu, an open family of 4B/9B/27B K–12 education models designed to move beyond problem solving toward curriculum understanding, student diagnosis, and effective tutoring—from Solver to Tutor.

</details>

<details>
<summary><b>7. VideoGen-Agent: Reinforcing Video Generation Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24997) • [📄 arXiv](https://arxiv.org/abs/2609.24997) • [📥 PDF](https://arxiv.org/pdf/2609.24997)

**💻 Code:** [⭐ Code](https://github.com/AndyCA111/VideoGen_Agent) • [⭐ Code](https://github.com/huggingface)

> Project page: https://andyca111.github.io/VideoGen_Agent/ Data: https://huggingface.co/datasets/andyli123princeton/VABench Code: https://github.com/AndyCA111/VideoGen_Agent

</details>

<details>
<summary><b>8. onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24983) • [📄 arXiv](https://arxiv.org/abs/2609.24983) • [📥 PDF](https://arxiv.org/pdf/2609.24983)

**💻 Code:** [⭐ Code](https://github.com/on-panda/on-panda) • [⭐ Code](https://github.com/huggingface)

> We’ve open-sourced onPanda, an interactive tool for data annotation and model inspection! 🐼 For data annotation: Reduce median annotation time by 52% . Collect both SFT and preference data in the same workflow. Produce SFT data with high on-policy...

</details>

<details>
<summary><b>9. Grounded Action Model: 3D Grounding as a Foundation for Robotics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23863) • [📄 arXiv](https://arxiv.org/abs/2609.23863) • [📥 PDF](https://arxiv.org/pdf/2609.23863)

**💻 Code:** [⭐ Code](https://github.com/GehaoZhang6/Grounded-Action-Model) • [⭐ Code](https://github.com/huggingface)

> Manipulation policies must know which objects matter and where they are, yet the pretrained backbones that current robot foundation models build on, from language in vision-language-action models (VLAs) to video generation in world-action models (...

</details>

<details>
<summary><b>10. One to More, More to One: Category-Aware Iterative Expert Training for Software Engineering Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23377) • [📄 arXiv](https://arxiv.org/abs/2609.23377) • [📥 PDF](https://arxiv.org/pdf/2609.23377)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce category-aware training for software engineering agents: Refresh–Repair–Expand iteratively develops category experts, while label-routed MOPD consolidates them into one deployable model. It achieves 58.04% on Pro-618 and 59.00% on SWE...

</details>

<details>
<summary><b>11. Deep Persona: A Psychologically Grounded Architecture and Evaluation Framework for Role-Playing Agents and Simulations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.22255) • [📄 arXiv](https://arxiv.org/abs/2609.22255) • [📥 PDF](https://arxiv.org/pdf/2609.22255)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. Harness-Zero: Harness Distillation via Agent-as-Harness</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24974) • [📄 arXiv](https://arxiv.org/abs/2609.24974) • [📥 PDF](https://arxiv.org/pdf/2609.24974)

**💻 Code:** [⭐ Code](https://github.com/metaevo-ai/harness-zero) • [⭐ Code](https://github.com/huggingface)

> Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and...

</details>

<details>
<summary><b>13. CARE: Experience-Guided Atomic Corrective Execution for Vision-Language-Action Policies</b> ⭐ 30</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24118) • [📄 arXiv](https://arxiv.org/abs/2609.24118) • [📥 PDF](https://arxiv.org/pdf/2609.24118)

**💻 Code:** [⭐ Code](https://github.com/xiaojunlan/care) • [⭐ Code](https://github.com/huggingface)

> Solve vla self-correction from data-centric point.

</details>

<details>
<summary><b>14. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Bingzhe Li, Yi Li, Dongming Jiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23986) • [📄 arXiv](https://arxiv.org/abs/2609.23986) • [📥 PDF](https://arxiv.org/pdf/2609.23986)

**💻 Code:** [⭐ Code](https://github.com/libingzheren/Jev-Mem) • [⭐ Code](https://github.com/huggingface)

> Jev-Mem introduces a System-One-controlled agentic memory architecture that separates frequent memory-management decisions from deeper language-model reasoning. On LoCoMo, it improves answer quality while substantially reducing memory-construction...

</details>

<details>
<summary><b>15. Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23658) • [📄 arXiv](https://arxiv.org/abs/2609.23658) • [📥 PDF](https://arxiv.org/pdf/2609.23658)

**💻 Code:** [⭐ Code](https://github.com/Siriuslala/physics) • [⭐ Code](https://github.com/huggingface)

> How does a video diffusion model perform motion planning, and why does it often violate physical rules? We introduce an interpretability study of motion planning in video diffusion models, identifying that RoPE-induced spatial attention decay at e...

</details>

<details>
<summary><b>16. HuRo: Robotizing Human Videos for Scalable VLA Pretraining</b> ⭐ 29</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10706) • [📄 arXiv](https://arxiv.org/abs/2609.10706) • [📥 PDF](https://arxiv.org/pdf/2609.10706)

**💻 Code:** [⭐ Code](https://github.com/3587jjh/HuRo) • [⭐ Code](https://github.com/huggingface)

> HuRo converts human egocentric videos into robot-aligned observations and actions via visual robotization and motion retargeting. Scaling HuRo data in VLA pretraining improves real-world manipulation performance and generalization, especially unde...

</details>

<details>
<summary><b>17. 1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24432) • [📄 arXiv](https://arxiv.org/abs/2609.24432) • [📥 PDF](https://arxiv.org/pdf/2609.24432)

**💻 Code:** [⭐ Code](https://github.com/BruceSheng1202/IER-OPD) • [⭐ Code](https://github.com/huggingface)

> Sparse on-policy distillation (OPD) allocates teacher supervision to a small subset of tokens in student-generated trajectories. However, useful teacher guidance can yield a noisy update when its gradient is estimated from a sampled next token. We...

</details>

<details>
<summary><b>18. Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23796) • [📄 arXiv](https://arxiv.org/abs/2609.23796) • [📥 PDF](https://arxiv.org/pdf/2609.23796)

**💻 Code:** [⭐ Code](https://github.com/VAST-AI-Research/Mira-Scene) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>19. Measuring the Checker: Mutation Analysis for GPU-Kernel Benchmark Oracles</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.22220) • [📄 arXiv](https://arxiv.org/abs/2609.22220) • [📥 PDF](https://arxiv.org/pdf/2609.22220)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Benchmarks for LLM-generated GPU kernels decide correctness with a few random inputs and a loose floating-point tolerance, and their verdicts now feed leaderboards and reinforcement-learning rewards. Recent work agrees these checkers are weak and ...

</details>

<details>
<summary><b>20. Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yong Jae Lee, Joohyung Kim, Jaden Park, Sankalp Yamsani, Trung Dao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24682) • [📄 arXiv](https://arxiv.org/abs/2609.24682) • [📥 PDF](https://arxiv.org/pdf/2609.24682)

**💻 Code:** [⭐ Code](https://github.com/trungdt880/THAW-VLA) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>21. Streaming Video Editing with Easy Adaptation</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24788) • [📄 arXiv](https://arxiv.org/abs/2609.24788) • [📥 PDF](https://arxiv.org/pdf/2609.24788)

**💻 Code:** [⭐ Code](https://github.com/YujiaHu1109/SVEET) • [⭐ Code](https://github.com/huggingface)

> In this paper, we propose SVEET, a framework that requires merely training on a pretrained bidirectional video diffusion model but supports high-quality streaming video editing in an auto-regressive fashion. To tackle this problem, we first system...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 21 |
| 📅 Today | [`2026-09-22.json`](data/daily/2026-09-22.json) | 21 |
| 📆 This Week | [`2026-W38.json`](data/weekly/2026-W38.json) | 42 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 498 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-22 | 21 | [View JSON](data/daily/2026-09-22.json) |
| 📄 2026-09-21 | 21 | [View JSON](data/daily/2026-09-21.json) |
| 📄 2026-09-20 | 24 | [View JSON](data/daily/2026-09-20.json) |
| 📄 2026-09-19 | 24 | [View JSON](data/daily/2026-09-19.json) |
| 📄 2026-09-18 | 19 | [View JSON](data/daily/2026-09-18.json) |
| 📄 2026-09-17 | 18 | [View JSON](data/daily/2026-09-17.json) |
| 📄 2026-09-16 | 18 | [View JSON](data/daily/2026-09-16.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W38 | 42 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 498 | [View JSON](data/monthly/2026-09.json) |
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
