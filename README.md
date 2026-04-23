<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-16-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3649+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">97</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">491</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3649+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** April 23, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.20796) • [📄 arXiv](https://arxiv.org/abs/2604.20796) • [📥 PDF](https://arxiv.org/pdf/2604.20796)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/LLaDA2.0-Uni)

> No abstract available.

</details>

<details>
<summary><b>2. DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.19859) • [📄 arXiv](https://arxiv.org/abs/2604.19859) • [📥 PDF](https://arxiv.org/pdf/2604.19859)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/DR-Venus) • [⭐ Code](https://github.com/inclusionAI/DR-Venus/tree/master/RL) • [⭐ Code](https://github.com/inclusionAI/DR-Venus/tree/master/SFT)

> Key insights: We explore how to build strong edge-scale deep research agents with small language models under limited open-data settings, focusing on both data quality and data utilization. We introduce DR-Venus, a 4B deep research agent trained e...

</details>

<details>
<summary><b>3. Near-Future Policy Optimization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dingyu Yao, Naibin Gu, Qingyi Si, Chenxu Yang, Chuanyu Qin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.20733) • [📄 arXiv](https://arxiv.org/abs/2604.20733) • [📥 PDF](https://arxiv.org/pdf/2604.20733)

> Work in progress. To be open-sourced soon. :)

</details>

<details>
<summary><b>4. Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.13602) • [📄 arXiv](https://arxiv.org/abs/2604.13602) • [📥 PDF](https://arxiv.org/pdf/2604.13602)

**💻 Code:** [⭐ Code](https://github.com/xhwang22/Awesome-Reward-Hacking)

> Reinforcement Learning from Human Feedback (RLHF) and related alignment paradigms have become central to steering large language models (LLMs) and multimodal large language models (MLLMs) toward human-preferred behaviors. However, these approaches...

</details>

<details>
<summary><b>5. Exploring Spatial Intelligence from a Generative Perspective</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Hao Zhong, Zekai Luo, Huanyi Zheng, Shunyao Jiang, Muzhi Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.20570) • [📄 arXiv](https://arxiv.org/abs/2604.20570) • [📥 PDF](https://arxiv.org/pdf/2604.20570)

**💻 Code:** [⭐ Code](https://github.com/aim-uofa/GSI-Bench)

> Spatial intelligence is essential for multimodal large language models, yet current benchmarks largely assess it only from an understanding perspective. We ask whether modern generative or unified multimodal models also possess generative spatial ...

</details>

<details>
<summary><b>6. WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yangzhuo Li, Qian Chen, Shengpeng Ji, leungtianle, 1f

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.14932) • [📄 arXiv](https://arxiv.org/abs/2604.14932) • [📥 PDF](https://arxiv.org/pdf/2604.14932)

> An effective post-train framework for SDM

</details>

<details>
<summary><b>7. SWE-chat: Coding Agent Interactions From Real Users in the Wild</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Diyi Yang, John Yang, Xiang Li, Vishakh Padmakumar, Joachim Baumann

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.20779) • [📄 arXiv](https://arxiv.org/abs/2604.20779) • [📥 PDF](https://arxiv.org/pdf/2604.20779)

> No abstract available.

</details>

<details>
<summary><b>8. Cortex 2.0: Grounding World Models in Real-World Industrial Deployment</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fabian Busch, Dhruv Behl, Katarina Bankovic, Walida Amer, Adriana Aida

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.20246) • [📄 arXiv](https://arxiv.org/abs/2604.20246) • [📥 PDF](https://arxiv.org/pdf/2604.20246)

> No abstract available.

</details>

<details>
<summary><b>9. Convergent Evolution: How Different Language Models Learn Similar Number Representations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.20817) • [📄 arXiv](https://arxiv.org/abs/2604.20817) • [📥 PDF](https://arxiv.org/pdf/2604.20817)

> Convergent Evolution: How Different Language Models Learn Similar Number Representations

</details>

<details>
<summary><b>10. Self-Evolving LLM Memory Extraction Across Heterogeneous Tasks</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11610) • [📄 arXiv](https://arxiv.org/abs/2604.11610) • [📥 PDF](https://arxiv.org/pdf/2604.11610)

**💻 Code:** [⭐ Code](https://github.com/ayyyq/heterogeneous-memory-extraction)

> We propose BEHEMOTH, an 18-dataset benchmark for heterogeneous memory extraction, and CluE, a cluster-based self-evolving method that consistently outperforms compared baselines.

</details>

<details>
<summary><b>11. SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18982) • [📄 arXiv](https://arxiv.org/abs/2604.18982) • [📥 PDF](https://arxiv.org/pdf/2604.18982)

**💻 Code:** [⭐ Code](https://github.com/jyyyyy0/SAVOIR)

> Training language agents for social intelligence faces a core challenge—credit assignment across multi-turn dialogues. Existing methods retrospectively distribute episode rewards via LLMs, lacking theoretical grounding. We propose SAVOIR, a princi...

</details>

<details>
<summary><b>12. ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.19720) • [📄 arXiv](https://arxiv.org/abs/2604.19720) • [📥 PDF](https://arxiv.org/pdf/2604.19720)

**💻 Code:** [⭐ Code](https://github.com/Taited/ReImagine)

> This work introduces a method for human video generation with two main components and an additional bonus model. First, we generate high-quality images from front and back human reference inputs, controlling both viewpoint and pose using SMPL-X re...

</details>

<details>
<summary><b>13. Visual Reasoning through Tool-supervised Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.19945) • [📄 arXiv](https://arxiv.org/abs/2604.19945) • [📥 PDF](https://arxiv.org/pdf/2604.19945)

> Tool-use RL for MLLMs often struggles because "learn to call the tool" and "learn to answer correctly" pull the policy in different directions. ToolsRL decouples them with a simple two-stage curriculum: first learn how to call a small set of nativ...

</details>

<details>
<summary><b>14. MMCORE: MultiModal COnnection with Representation Aligned Latent Embeddings</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yixuan Huang, Ye Wang, Jingxiang Sun, Yichun Shi, Zijie Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.19902) • [📄 arXiv](https://arxiv.org/abs/2604.19902) • [📥 PDF](https://arxiv.org/pdf/2604.19902)

> No abstract available.

</details>

<details>
<summary><b>15. CreativeGame:Toward Mechanic-Aware Creative Game Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yiwei Shi, Tieyue Yin, Shenglin Wang, Han Wang, Hongnan Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.19926) • [📄 arXiv](https://arxiv.org/abs/2604.19926) • [📥 PDF](https://arxiv.org/pdf/2604.19926)

> No abstract available.

</details>

<details>
<summary><b>16. Scaling Test-Time Compute for Agentic Coding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16529) • [📄 arXiv](https://arxiv.org/abs/2604.16529) • [📥 PDF](https://arxiv.org/pdf/2604.16529)

> Thread: https://x.com/danieljwkim/status/2046971253857378360

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 16 |
| 📅 Today | [`2026-04-23.json`](data/daily/2026-04-23.json) | 16 |
| 📆 This Week | [`2026-W16.json`](data/weekly/2026-W16.json) | 97 |
| 🗓️ This Month | [`2026-04.json`](data/monthly/2026-04.json) | 491 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-04-23 | 16 | [View JSON](data/daily/2026-04-23.json) |
| 📄 2026-04-22 | 49 | [View JSON](data/daily/2026-04-22.json) |
| 📄 2026-04-21 | 26 | [View JSON](data/daily/2026-04-21.json) |
| 📄 2026-04-20 | 3 | [View JSON](data/daily/2026-04-20.json) |
| 📄 2026-04-19 | 29 | [View JSON](data/daily/2026-04-19.json) |
| 📄 2026-04-18 | 29 | [View JSON](data/daily/2026-04-18.json) |
| 📄 2026-04-17 | 4 | [View JSON](data/daily/2026-04-17.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W16 | 97 | [View JSON](data/weekly/2026-W16.json) |
| 📅 2026-W15 | 125 | [View JSON](data/weekly/2026-W15.json) |
| 📅 2026-W14 | 147 | [View JSON](data/weekly/2026-W14.json) |
| 📅 2026-W13 | 125 | [View JSON](data/weekly/2026-W13.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-04 | 491 | [View JSON](data/monthly/2026-04.json) |
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
