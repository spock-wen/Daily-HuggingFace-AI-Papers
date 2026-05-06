<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-17-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3870+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">17</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">42</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">106</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3870+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** May 06, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.28123) • [📄 arXiv](https://arxiv.org/abs/2604.28123) • [📥 PDF](https://arxiv.org/pdf/2604.28123)

**💻 Code:** [⭐ Code](https://github.com/XIAO4579/PRISM)

> Project Page: https://xiao4579.github.io/PRISM/ Paper： https://arxiv.org/abs/2604.28123 Code： https://github.com/XIAO4579/PRISM Data and Model： https://huggingface.co/prism-vlm

</details>

<details>
<summary><b>2. X2SAM: Any Segmentation in Images and Videos</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.00891) • [📄 arXiv](https://arxiv.org/abs/2605.00891) • [📥 PDF](https://arxiv.org/pdf/2605.00891)

**💻 Code:** [⭐ Code](https://github.com/wanghao9610/X2SAM)

> X2SAM introduces a unified segmentation MLLM framework that extends any-segmentation capabilities from images to videos, supporting generic, open-vocabulary, referring, reasoning, grounded conversation generation, interactive, and visual grounded ...

</details>

<details>
<summary><b>3. HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.02396) • [📄 arXiv](https://arxiv.org/abs/2605.02396) • [📥 PDF](https://arxiv.org/pdf/2605.02396)

**💻 Code:** [⭐ Code](https://github.com/wjn1996/HeavySkill)

> HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness HeavySkill is a test-time scaling technique that decomposes complex reasoning into two stages: Parallel Reasoning — Generate K independent reasoning trajectories concurrently Sequent...

</details>

<details>
<summary><b>4. PatRe: A Full-Stage Office Action and Rebuttal Generation Benchmark for Patent Examination</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03571) • [📄 arXiv](https://arxiv.org/abs/2605.03571) • [📥 PDF](https://arxiv.org/pdf/2605.03571)

**💻 Code:** [⭐ Code](https://github.com/AIforIP/PatRe)

> PatRe is the first benchmark to model the full patent examination lifecycle as an interactive, multi-turn process between examiner and applicant. It captures real-world dynamics such as Office Action generation and rebuttal, supporting both oracle...

</details>

<details>
<summary><b>5. Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Weizheng Wang, Linchun Li, Yumou Liu, Xuanhe Zhou, Zirui Tang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03596) • [📄 arXiv](https://arxiv.org/abs/2605.03596) • [📥 PDF](https://arxiv.org/pdf/2605.03596)

> No abstract available.

</details>

<details>
<summary><b>6. SymptomAI: Towards a Conversational AI Agent for Everyday Symptom Assessment</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Miao Liu, Marinela Cotoi, Beszel Hawkins, Fadi Yousif, Joseph Breda

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.04012) • [📄 arXiv](https://arxiv.org/abs/2605.04012) • [📥 PDF](https://arxiv.org/pdf/2605.04012)

> No abstract available.

</details>

<details>
<summary><b>7. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Chenchen Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.02801) • [📄 arXiv](https://arxiv.org/abs/2605.02801) • [📥 PDF](https://arxiv.org/pdf/2605.02801)

**💻 Code:** [⭐ Code](https://github.com/xxzcc/awesome-llm-mas-rl)

> As large language model (LLM) agents evolve from isolated tool users into coordinated teams, reinforcement learning (RL) must optimize not only individual actions but also how work is spawned, delegated, communicated, aggregated, and stopped. This...

</details>

<details>
<summary><b>8. SVGS: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors</b> ⭐ 58</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2411.18966) • [📄 arXiv](http://arxiv.org/abs/2411.18966) • [📥 PDF](https://arxiv.org/pdf/2411.18966)

**💻 Code:** [⭐ Code](https://github.com/Xrvitd/SVGS)

> Today we're releasing SVGS , a new approach for Gaussian Splatting that makes each primitive far more expressive by giving it spatially varying colors and opacity . Gaussian Splatting has become a powerful paradigm for novel view synthesis, but ex...

</details>

<details>
<summary><b>9. A Benchmark for Interactive World Models with a Unified Action Generation Framework</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuchao Huang, Ziyou Wang, Qin Wan, Yingshan Lei, Jianjie Fang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03941) • [📄 arXiv](https://arxiv.org/abs/2605.03941) • [📥 PDF](https://arxiv.org/pdf/2605.03941)

> No abstract available.

</details>

<details>
<summary><b>10. OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories</b> ⭐ 622</summary>

<br/>

**👥 Authors:** Xinyu Zhu, Keduan Huang, Shuo Tang, Rui Ye, Yuwen Du

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.04036) • [📄 arXiv](https://arxiv.org/abs/2605.04036) • [📥 PDF](https://arxiv.org/pdf/2605.04036)

**💻 Code:** [⭐ Code](https://github.com/PolarSeeker/OpenSeeker)

> No abstract available.

</details>

<details>
<summary><b>11. The TTS-STT Flywheel: Synthetic Entity-Dense Audio Closes the Indic ASR Gap Where Commercial and Open-Source Systems Fail</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03073) • [📄 arXiv](https://arxiv.org/abs/2605.03073) • [📥 PDF](https://arxiv.org/pdf/2605.03073)

**💻 Code:** [⭐ Code](https://github.com/praxelhq/stt-flywheel)

> We benchmark open-source SOTA (vasista22/whisper-{te,ta,hi}-large-v2) and commercial Deepgram Nova-3 on a synthesised entity-dense Telugu test set — content that real Indian users actually speak: digit strings, currency amounts, addresses, brand n...

</details>

<details>
<summary><b>12. TCDA: Thread-Constrained Discourse-Aware Modeling for Conversational Sentiment Quadruple Analysis</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Xiujuan Xu, Zhiqi Huang, Yifan Lyu, Xinze Che, Xinran Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.01717) • [📄 arXiv](https://arxiv.org/abs/2605.01717) • [📥 PDF](https://arxiv.org/pdf/2605.01717)

**💻 Code:** [⭐ Code](https://github.com/LiXinran6/TCDA)

> This paper has been officially accepted by IJCAI 2026 (Main Track).

</details>

<details>
<summary><b>13. SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.01466) • [📄 arXiv](https://arxiv.org/abs/2605.01466) • [📥 PDF](https://arxiv.org/pdf/2605.01466)

**💻 Code:** [⭐ Code](https://github.com/zay002/SplAttN)

> Hi everyone! I'm one of the authors of SplAttN. In this work, we tackle a common failure mode in image-guided point cloud completion: "Cross-Modal Entropy Collapse." We found that hard 3D-to-2D projection often makes the image plane too sparse, ef...

</details>

<details>
<summary><b>14. Healthcare AI GYM for Medical Agents</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Minbyul Jeong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.02943) • [📄 arXiv](https://arxiv.org/abs/2605.02943) • [📥 PDF](https://arxiv.org/pdf/2605.02943)

**💻 Code:** [⭐ Code](https://github.com/minstar/Healthcare_GYM)

> please contact minstar@upstage.ai any information for the project.

</details>

<details>
<summary><b>15. StateSMix: Online Lossless Compression via Mamba State Space Models and Sparse N-gram Context Mixing</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Roberto Tacconelli

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.02904) • [📄 arXiv](https://arxiv.org/abs/2605.02904) • [📥 PDF](https://arxiv.org/pdf/2605.02904)

**💻 Code:** [⭐ Code](https://github.com/robtacconelli/StateSMix)

> We present StateSMix, a fully self-contained lossless compressor that couples an online-trained Mamba-style State Space Model (SSM) with sparse n-gram context mixing and arithmetic coding. The model is initialised from scratch and trained token-by...

</details>

<details>
<summary><b>16. ESARBench: A Benchmark for Agentic UAV Embodied Search and Rescue</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Shuo Yang, Jianyi Zhou, Ping Chen, 4amGodvzx

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.01371) • [📄 arXiv](https://arxiv.org/abs/2605.01371) • [📥 PDF](https://arxiv.org/pdf/2605.01371)

**💻 Code:** [⭐ Code](https://github.com/4amGodvzx/ESAR)

> ESARBench is the first comprehensive benchmark specifically designed to evaluate embodied UAV agents in highly realistic Embodied Search and Rescue (ESAR) scenarios: High Fidelity: 4 large-scale environments built with UE5 + AirSim using real-worl...

</details>

<details>
<summary><b>17. Chain of Evidence: Pixel-Level Visual Attribution for Iterative Retrieval-Augmented Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wei Ye, Di Liang, Xi Wang, Ziqiang Cui, PeiyangLiu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.01284) • [📄 arXiv](https://arxiv.org/abs/2605.01284) • [📥 PDF](https://arxiv.org/pdf/2605.01284)

**💻 Code:** [⭐ Code](https://github.com/PeiYangLiu/CoE)

> Excited to share our latest work on visual RAG! 🚀 Existing iRAG systems linearise documents into plain text, which (1) breaks visual semantics in slides/charts/diagrams, (2) gives only coarse "[Source: Doc-1]" citations, and (3) leaves multi-hop r...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 17 |
| 📅 Today | [`2026-05-06.json`](data/daily/2026-05-06.json) | 17 |
| 📆 This Week | [`2026-W18.json`](data/weekly/2026-W18.json) | 42 |
| 🗓️ This Month | [`2026-05.json`](data/monthly/2026-05.json) | 106 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-05-06 | 17 | [View JSON](data/daily/2026-05-06.json) |
| 📄 2026-05-05 | 13 | [View JSON](data/daily/2026-05-05.json) |
| 📄 2026-05-04 | 12 | [View JSON](data/daily/2026-05-04.json) |
| 📄 2026-05-03 | 24 | [View JSON](data/daily/2026-05-03.json) |
| 📄 2026-05-02 | 24 | [View JSON](data/daily/2026-05-02.json) |
| 📄 2026-05-01 | 16 | [View JSON](data/daily/2026-05-01.json) |
| 📄 2026-04-30 | 8 | [View JSON](data/daily/2026-04-30.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W18 | 42 | [View JSON](data/weekly/2026-W18.json) |
| 📅 2026-W17 | 120 | [View JSON](data/weekly/2026-W17.json) |
| 📅 2026-W16 | 156 | [View JSON](data/weekly/2026-W16.json) |
| 📅 2026-W15 | 125 | [View JSON](data/weekly/2026-W15.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-05 | 106 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
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
