<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-22-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6389+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">42</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">118</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6389+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 04, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks</b> ⭐ 51</summary>

<br/>

**👥 Authors:** Shidong Yang, Yong Wang, Shun Zou, Hailang Huang, Ziyu Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01964) • [📄 arXiv](https://arxiv.org/abs/2608.01964) • [📥 PDF](https://arxiv.org/pdf/2608.01964)

**💻 Code:** [⭐ Code](https://github.com/AMAP-ML/LongHorizon-Harness) • [⭐ Code](https://github.com/huggingface)

> LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks Github: https://github.com/AMAP-ML/LongHorizon-Harness Website: https://lh-harness.pages.dev

</details>

<details>
<summary><b>2. SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zero-Shot Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.02023) • [📄 arXiv](https://arxiv.org/abs/2608.02023) • [📥 PDF](https://arxiv.org/pdf/2608.02023)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Speech and audio generation is often needed in animation dubbing, audio drama, movies, advertising, games, podcasts, and short-video production. In these scenarios, creators may need to design voices without reference recordings, control speaker s...

</details>

<details>
<summary><b>3. Progressive Agent Skill Generation via Reinforcement Learning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01678) • [📄 arXiv](https://arxiv.org/abs/2608.01678) • [📥 PDF](https://arxiv.org/pdf/2608.01678)

**💻 Code:** [⭐ Code](https://github.com/ejhshen/skill-alpha) • [⭐ Code](https://github.com/huggingface)

> Code is available at https://github.com/ejhshen/skill-alpha

</details>

<details>
<summary><b>4. VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Policy Distillation</b> ⭐ 16</summary>

<br/>

**👥 Authors:** Zhengxi Lu, Qingyao Li, Shuai Shao, Yixing Li, Kangning Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28590) • [📄 arXiv](https://arxiv.org/abs/2607.28590) • [📥 PDF](https://arxiv.org/pdf/2607.28590)

**💻 Code:** [⭐ Code](https://github.com/DeepExperience/VAD_Multimodal_OPD) • [⭐ Code](https://github.com/huggingface)

> preview

</details>

<details>
<summary><b>5. WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Liang Tan, Zitong Zhou, Jiahe Wang, Shuyao Shang, Yuxue Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.02603) • [📄 arXiv](https://arxiv.org/abs/2608.02603) • [📥 PDF](https://arxiv.org/pdf/2608.02603)

**💻 Code:** [⭐ Code](https://github.com/YuxueYang1204/worldexam) • [⭐ Code](https://github.com/huggingface)

> WorldExam is a hierarchical diagnostic benchmark for controllable video world models. Beyond visual appearance and explicit instruction following, it asks whether a model preserves a coherent world and exhibits inherent reactivity. Across camera-,...

</details>

<details>
<summary><b>6. UEmbed: Unified Sparse and Dense Multimodal Embeddings</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.02583) • [📄 arXiv](https://arxiv.org/abs/2608.02583) • [📥 PDF](https://arxiv.org/pdf/2608.02583)

**💻 Code:** [⭐ Code](https://github.com/Alibaba-NLP/UEmbed) • [⭐ Code](https://github.com/huggingface)

> UEmbed offers a new paradigm: it unifies dense and sparse embeddings in one model, while further extending sparse retrieval to unify text and multimodal inputs.

</details>

<details>
<summary><b>7. SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.02287) • [📄 arXiv](https://arxiv.org/abs/2608.02287) • [📥 PDF](https://arxiv.org/pdf/2608.02287)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> SKT is a Skill-use data synthesis pipeline based on multi-agent systems. It can automatically synthesize large-scale Skill-use tasks and generate skill-use trajectories with different harnesses and models.

</details>

<details>
<summary><b>8. WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.29613) • [📄 arXiv](https://arxiv.org/abs/2607.29613) • [📥 PDF](https://arxiv.org/pdf/2607.29613)

**💻 Code:** [⭐ Code](https://github.com/sylvestf/WCM) • [⭐ Code](https://github.com/huggingface)

> 🚀 Introducing WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning We are excited to introduce the World Critic Model (WCM) , a new approach that targets a critical yet often overlooked bottleneck in VLA reinforcement learni...

</details>

<details>
<summary><b>9. SWE-Touch: Benchmarking Coding Agents When Users Touch the Code</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.02499) • [📄 arXiv](https://arxiv.org/abs/2608.02499) • [📥 PDF](https://arxiv.org/pdf/2608.02499)

**💻 Code:** [⭐ Code](https://github.com/Trae1ounG/SWE-Touch) • [⭐ Code](https://github.com/huggingface)

> SWE-Touch: Benchmarking Coding Agents When Users Touch the Code Current coding agent benchmarks (SWE-Bench, etc.) evaluate agents working alone on a static codebase. But in real development, users actively inspect and modify code while the agent i...

</details>

<details>
<summary><b>10. CADENA: Stepwise CAD Reverse Engineering</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Daniil Ignatiev, Antonio Rodriguez, Maksim Elistratov, Gennadiy Savrasov, Soslan Kabisov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.00799) • [📄 arXiv](https://arxiv.org/abs/2608.00799) • [📥 PDF](https://arxiv.org/pdf/2608.00799)

**💻 Code:** [⭐ Code](https://github.com/zhemdi/cadena) • [⭐ Code](https://github.com/huggingface)

> CADENA reconstructs a 3D mesh as an editable parametric CAD program. Instead of emitting the whole program in one pass, it adds one operation at a time, executes the partial program, and compares the target against what has been built so far — so ...

</details>

<details>
<summary><b>11. Motion Beyond Morphology: Bootstrapping Cross-Category Motion Transfer from Abstract Motion Representations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01628) • [📄 arXiv](https://arxiv.org/abs/2608.01628) • [📥 PDF](https://arxiv.org/pdf/2608.01628)

**💻 Code:** [⭐ Code](https://github.com/miniz233/MBM) • [⭐ Code](https://github.com/huggingface)

> Project Page: https://miniz233.github.io/MotionBeyondMorphology/ Github: https://github.com/miniz233/MBM

</details>

<details>
<summary><b>12. Roomer: Reflective Object-Grounded Model Editing and Repair for 3D Indoor Layout Synthesis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01973) • [📄 arXiv](https://arxiv.org/abs/2608.01973) • [📥 PDF](https://arxiv.org/pdf/2608.01973)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Roomer attributes residual violations in synthesized 3D indoor layouts to specific object instances, applies local edits to a structured layout model, and commits each repair only after deterministic re-verification.

</details>

<details>
<summary><b>13. 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question Answering</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Kyeongbo Kong, Changwoo Baek

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01185) • [📄 arXiv](https://arxiv.org/abs/2608.01185) • [📥 PDF](https://arxiv.org/pdf/2608.01185)

**💻 Code:** [⭐ Code](https://github.com/cvsp-lab/3DZip) • [⭐ Code](https://github.com/huggingface)

> Accepted to ECCV 2026.

</details>

<details>
<summary><b>14. DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimodal Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01827) • [📄 arXiv](https://arxiv.org/abs/2608.01827) • [📥 PDF](https://arxiv.org/pdf/2608.01827)

**💻 Code:** [⭐ Code](https://github.com/Halcyon-Zhang/DeepVoyager-VL) • [⭐ Code](https://github.com/huggingface)

> A strong step toward multimodal deep research agents. DeepVoyager-VL scales vision-language reasoning to long-horizon trajectories with iterative visual and textual search, showing how agents can better solve complex real-world information-seeking...

</details>

<details>
<summary><b>15. StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a Hypergraph Field</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01954) • [📄 arXiv](https://arxiv.org/abs/2608.01954) • [📥 PDF](https://arxiv.org/pdf/2608.01954)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> StyleForge jointly selects visually coherent furniture for fixed 3D room layouts using a dynamic hypergraph style field and counterfactual energy-based test-time training.

</details>

<details>
<summary><b>16. DiffusionGemma Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.00146) • [📄 arXiv](https://arxiv.org/abs/2608.00146) • [📥 PDF](https://arxiv.org/pdf/2608.00146)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.00079) • [📄 arXiv](https://arxiv.org/abs/2608.00079) • [📥 PDF](https://arxiv.org/pdf/2608.00079)

**💻 Code:** [⭐ Code](https://github.com/zhangrongxiang/LeapTalk) • [⭐ Code](https://github.com/huggingface)

> Paper: https://arxiv.org/abs/2608.00079 Project Page: https://zhangrongxiang.github.io/leaptalk-page/ Code: https://github.com/zhangrongxiang/LeapTalk

</details>

<details>
<summary><b>18. ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to the Next Step</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.02358) • [📄 arXiv](https://arxiv.org/abs/2608.02358) • [📥 PDF](https://arxiv.org/pdf/2608.02358)

**💻 Code:** [⭐ Code](https://github.com/declare-lab/ScrambleToolBench) • [⭐ Code](https://github.com/huggingface)

> ScrambleToolBench is an interactive terminal benchmark designed to evaluate the behavioral reasoning and adaptability of autonomous agents. By obfuscating tool names and parameters, it removes the semantic cues agents typically rely on, forcing th...

</details>

<details>
<summary><b>19. Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Zhishan Zou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.00440) • [📄 arXiv](https://arxiv.org/abs/2608.00440) • [📥 PDF](https://arxiv.org/pdf/2608.00440)

**💻 Code:** [⭐ Code](https://github.com/choucisan/poplar) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. DAPD: Dual-Anchored Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01735) • [📄 arXiv](https://arxiv.org/abs/2608.01735) • [📥 PDF](https://arxiv.org/pdf/2608.01735)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DAPD aligns on-policy and reference behavior under matched information conditions.

</details>

<details>
<summary><b>21. Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hongyan Xie, Guli Zhang, Kaixuan Wang, Yang Zhou, Zixuan Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.01755) • [📄 arXiv](https://arxiv.org/abs/2608.01755) • [📥 PDF](https://arxiv.org/pdf/2608.01755)

**💻 Code:** [⭐ Code](https://github.com/hzx122/DEFT-RLVR) • [⭐ Code](https://github.com/huggingface)

> We identify an anchoring bias in autonomous-driving VLMs caused by GT-trajectory-conditioned CoT supervision. To address this issue, we introduce AD-MCQ and DEFT-RLVR, a candidate-grounded reinforcement learning framework that reformulates AD plan...

</details>

<details>
<summary><b>22. Relax Within, Balance Across: Geometry-Guided Load Balancing for Vision-Language Mixture-of-Experts</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.00574) • [📄 arXiv](https://arxiv.org/abs/2608.00574) • [📥 PDF](https://arxiv.org/pdf/2608.00574)

**💻 Code:** [⭐ Code](https://github.com/ZiangWu-77/ReBA) • [⭐ Code](https://github.com/huggingface)

> This work started from several routing phenomena that we believe may be useful beyond ReBA itself. First, mixed balance can hide large modality-specific imbalance. The standard token-level auxiliary loss only observes the combined image–text load....

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 22 |
| 📅 Today | [`2026-08-04.json`](data/daily/2026-08-04.json) | 22 |
| 📆 This Week | [`2026-W31.json`](data/weekly/2026-W31.json) | 42 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 118 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-04 | 22 | [View JSON](data/daily/2026-08-04.json) |
| 📄 2026-08-03 | 20 | [View JSON](data/daily/2026-08-03.json) |
| 📄 2026-08-02 | 38 | [View JSON](data/daily/2026-08-02.json) |
| 📄 2026-08-01 | 38 | [View JSON](data/daily/2026-08-01.json) |
| 📄 2026-07-31 | 31 | [View JSON](data/daily/2026-07-31.json) |
| 📄 2026-07-30 | 14 | [View JSON](data/daily/2026-07-30.json) |
| 📄 2026-07-29 | 15 | [View JSON](data/daily/2026-07-29.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W31 | 42 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 118 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |

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
