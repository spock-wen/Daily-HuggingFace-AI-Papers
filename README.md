<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-16-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6842+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">16</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">28</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">571</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6842+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 25, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Apodex 1.1: Scaling Agentic Intelligence for Complex Work</b> ⭐ 219</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23283) • [📄 arXiv](https://arxiv.org/abs/2608.23283) • [📥 PDF](https://arxiv.org/pdf/2608.23283)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ApodexAI/FrontierAgent)

> Meet Apodex 1.1: Scaling Agentic Intelligence for Complex Work Open Source Harness: https://github.com/ApodexAI/FrontierAgent Open Weights: https://huggingface.co/collections/apodex/apodex-11 We’re excited to introduce Apodex 1.1, our new model fa...

</details>

<details>
<summary><b>2. MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiajun Liu, Tingyu Qu, Qiyi Wang, Xiongwei Wu, Yi Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23035) • [📄 arXiv](https://arxiv.org/abs/2608.23035) • [📥 PDF](https://arxiv.org/pdf/2608.23035)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> MobilePA-Bench

</details>

<details>
<summary><b>3. RISE: Adaptive Imagination for World Action Models</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.20430) • [📄 arXiv](https://arxiv.org/abs/2608.20430) • [📥 PDF](https://arxiv.org/pdf/2608.20430)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/COOWAI/RISE)

> We introduce RISE, an adaptive imagination framework for World Action Models (WAMs) in autonomous driving. Instead of using a fixed rollout depth for every scene, RISE dynamically decides whether to continue imagining future latent states based on...

</details>

<details>
<summary><b>4. TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.20958) • [📄 arXiv](https://arxiv.org/abs/2608.20958) • [📥 PDF](https://arxiv.org/pdf/2608.20958)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TaoLiveAIGC/TLive-Omni)

> ✨ Highlights Timestamped Per-vGrid layout — Audio and video tokens are organized into timestamped grid with explicit boundaries, keeping audio segments adjacent to their corresponding visual content for fine-grained temporal alignment over long st...

</details>

<details>
<summary><b>5. Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervision</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.16812) • [📄 arXiv](https://arxiv.org/abs/2608.16812) • [📥 PDF](https://arxiv.org/pdf/2608.16812)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/ConceptEdit) • [⭐ Code](https://github.com/huggingface)

> 🚀 ConceptEdit : Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervision. 📄 arXiv 💻 GitHub 🤗 Dataset 🤗 Benchmark

</details>

<details>
<summary><b>6. Prime Agent: A Self-Improving RLM Harness</b> ⭐ 18.2k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23552) • [📄 arXiv](https://arxiv.org/abs/2608.23552) • [📥 PDF](https://arxiv.org/pdf/2608.23552)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PrimeIntellect-ai/prime-agent)

> No abstract available.

</details>

<details>
<summary><b>7. ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13622) • [📄 arXiv](https://arxiv.org/abs/2608.13622) • [📥 PDF](https://arxiv.org/pdf/2608.13622)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction

</details>

<details>
<summary><b>8. ReWorld: An Interactive World Model with Long-Horizon Memory</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23565) • [📄 arXiv](https://arxiv.org/abs/2608.23565) • [📥 PDF](https://arxiv.org/pdf/2608.23565)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhifeichen097/ReWorld)

> No abstract available.

</details>

<details>
<summary><b>9. GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.21833) • [📄 arXiv](https://arxiv.org/abs/2608.21833) • [📥 PDF](https://arxiv.org/pdf/2608.21833)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Danny H. K. Tsang, Yize Chen, Rengrong Xiong, Haiyuan Wan, Chen Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.19408) • [📄 arXiv](https://arxiv.org/abs/2608.19408) • [📥 PDF](https://arxiv.org/pdf/2608.19408)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. Block3D: Efficient Text-to-3D Generation via Block-Wise Diffusion</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.19567) • [📄 arXiv](https://arxiv.org/abs/2608.19567) • [📥 PDF](https://arxiv.org/pdf/2608.19567)

**💻 Code:** [⭐ Code](https://github.com/ziplab/Block3D) • [⭐ Code](https://github.com/huggingface)

> Block3D is an efficient text-to-3D generation framework that shifts the causal dependency of discrete shape tokens from individual tokens to contiguous blocks.

</details>

<details>
<summary><b>12. Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.20169) • [📄 arXiv](https://arxiv.org/abs/2608.20169) • [📥 PDF](https://arxiv.org/pdf/2608.20169)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Agent4Science-UTokyo/Task-CoEvolve)

> A major challenge for scaling recursive self-improvement, especially in harness optimization, is the cost of evolution. We introduce a fundamentally different approach that cuts the evolution cost of existing harness optimization by up to 80%. 🚀 I...

</details>

<details>
<summary><b>13. Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer Churn in Retrieval-Augmented QA</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.22856) • [📄 arXiv](https://arxiv.org/abs/2608.22856) • [📥 PDF](https://arxiv.org/pdf/2608.22856)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Same Agent, Different Answers

</details>

<details>
<summary><b>14. Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR Errors</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Zhenghua Bao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.22872) • [📄 arXiv](https://arxiv.org/abs/2608.22872) • [📥 PDF](https://arxiv.org/pdf/2608.22872)

**💻 Code:** [⭐ Code](https://github.com/ZhenghuaBao/spoken-multihop-rag) • [⭐ Code](https://github.com/huggingface)

> Speech interfaces put ASR in front of retrieval, so the query a RAG system sees is already corrupted. We test whether the standard multi-hop methods, entity-graph linking and iterative reformulation, absorb that corruption or amplify it. The findi...

</details>

<details>
<summary><b>15. TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yan Huang, Heng Fan, Qinglei Cao, Qiao Zhang, Hanzhi Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.17336) • [📄 arXiv](https://arxiv.org/abs/2608.17336) • [📥 PDF](https://arxiv.org/pdf/2608.17336)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TileMix introduces tile-centric mixed-precision attention for long-context LLM inference. Instead of applying a single precision uniformly across attention, it routes hardware-aligned tile groups between FP16 and INT8 within the same fused FlashAt...

</details>

<details>
<summary><b>16. One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Liang Chen, leoluo25933

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13610) • [📄 arXiv](https://arxiv.org/abs/2606.13610) • [📥 PDF](https://arxiv.org/pdf/2606.13610)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Accepted to EMNLP 2026 Findings.  A single polluted web page is enough to make production LLMs recommend a brand that does not exist — 27% at rank 1, 73.8% when the top three pages are swapped. Turning on reasoning makes it worse.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 16 |
| 📅 Today | [`2026-08-25.json`](data/daily/2026-08-25.json) | 16 |
| 📆 This Week | [`2026-W34.json`](data/weekly/2026-W34.json) | 28 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 571 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-25 | 16 | [View JSON](data/daily/2026-08-25.json) |
| 📄 2026-08-24 | 12 | [View JSON](data/daily/2026-08-24.json) |
| 📄 2026-08-23 | 26 | [View JSON](data/daily/2026-08-23.json) |
| 📄 2026-08-22 | 26 | [View JSON](data/daily/2026-08-22.json) |
| 📄 2026-08-21 | 15 | [View JSON](data/daily/2026-08-21.json) |
| 📄 2026-08-20 | 13 | [View JSON](data/daily/2026-08-20.json) |
| 📄 2026-08-19 | 21 | [View JSON](data/daily/2026-08-19.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W34 | 28 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |
| 📅 2026-W32 | 156 | [View JSON](data/weekly/2026-W32.json) |
| 📅 2026-W31 | 166 | [View JSON](data/weekly/2026-W31.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 571 | [View JSON](data/monthly/2026-08.json) |
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
