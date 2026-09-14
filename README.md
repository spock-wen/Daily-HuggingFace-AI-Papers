<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-10-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7308+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">10</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">10</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">328</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7308+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 14, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Feyospace-v1: How the Cyber Mercury Seven Trained Frontier Cyber Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08418) • [📄 arXiv](https://arxiv.org/abs/2609.08418) • [📥 PDF](https://arxiv.org/pdf/2609.08418)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present an end-to-end, data-centric framework for post-training open-weight language models as agentic cyber systems. The framework addresses five practical challenges in capability transfer: reasoning-signature analysis with Choulea("思维链蒸馏"), ...

</details>

<details>
<summary><b>2. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.12641) • [📄 arXiv](https://arxiv.org/abs/2609.12641) • [📥 PDF](https://arxiv.org/pdf/2609.12641)

**💻 Code:** [⭐ Code](https://github.com/MAGICLAB-NUS/LIT) • [⭐ Code](https://github.com/huggingface)

> Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that co...

</details>

<details>
<summary><b>3. Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation</b> ⭐ 201</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11115) • [📄 arXiv](https://arxiv.org/abs/2609.11115) • [📥 PDF](https://arxiv.org/pdf/2609.11115)

**💻 Code:** [⭐ Code](https://github.com/ktwu01/benchmark-radar) • [⭐ Code](https://github.com/huggingface)

> Benchmark radar is all you need when doing benchmark research! We kept running into new benchmarks while doing benchmark research, so we built a crawler that continuously collects benchmark-related signals from across the web. It pulls evidence fr...

</details>

<details>
<summary><b>4. SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.13141) • [📄 arXiv](https://arxiv.org/abs/2609.13141) • [📥 PDF](https://arxiv.org/pdf/2609.13141)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification)

> No abstract available.

</details>

<details>
<summary><b>5. COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11682) • [📄 arXiv](https://arxiv.org/abs/2609.11682) • [📥 PDF](https://arxiv.org/pdf/2609.11682)

**💻 Code:** [⭐ Code](https://github.com/Jerry-LuP/COBRA-Skills) • [⭐ Code](https://github.com/huggingface)

> COBRA-Skills: Contextual Bandits for Efficient Agent Skill Optimization 🚀 How can we optimize Agent Skills without repeatedly spending large amounts of computation on weak candidates and costly LLM-based refinement? COBRA-Skills treats skill optim...

</details>

<details>
<summary><b>6. StepAudio 3 Gen Technical Report</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Boyang Wang, Bo Zhao, Bin Lin, jerryxxx, BoyongWu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.12945) • [📄 arXiv](https://arxiv.org/abs/2609.12945) • [📥 PDF](https://arxiv.org/pdf/2609.12945)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce StepAudio 3 Gen, a general-purpose audio generation model that supports zero-shot text-to-speech (TTS), voice design, vocal generation, sound effects, music, vibe speech, and mixtures of multiple audio types within a unified framework...

</details>

<details>
<summary><b>7. PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30597) • [📄 arXiv](https://arxiv.org/abs/2608.30597) • [📥 PDF](https://arxiv.org/pdf/2608.30597)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VennTum99/PLC-DPO)

> Preference datasets often contain incorrect preference directions or weak/ambiguous pairs. PLC-DPO introduces a latent clean, flip, or tie state for each pair and uses the calibrated policy–reference margin to infer posterior-like routing weights....

</details>

<details>
<summary><b>8. SNAP3D: Physically Grounded 3D Parts for Assembly from a Single Image</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Xiaoxuan Ma, Kris Kitani, Nicolas Ugrinovic, Hao-Tang Tsui, Yu-Rou Tuan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.13146) • [📄 arXiv](https://arxiv.org/abs/2609.13146) • [📥 PDF](https://arxiv.org/pdf/2609.13146)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LucyTuan/SNAP3D)

> Video: https://www.youtube.com/watch?v=22yRDaWabwA

</details>

<details>
<summary><b>9. Online Learning with LLM Experts from Limited Feedback</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ryan A. Rossi, Koyel Mukherjee, Soumyabrata Pal, Wang Wei, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05820) • [📄 arXiv](https://arxiv.org/abs/2609.05820) • [📥 PDF](https://arxiv.org/pdf/2609.05820)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. Beyond Top-k Skill Retrieval: Diversity-Aware Skill Routing for LLM Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hongjie Chen, Samyadeep Basu, Tiankai Yang, Wang Wei, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05824) • [📄 arXiv](https://arxiv.org/abs/2609.05824) • [📥 PDF](https://arxiv.org/pdf/2609.05824)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 10 |
| 📅 Today | [`2026-09-14.json`](data/daily/2026-09-14.json) | 10 |
| 📆 This Week | [`2026-W37.json`](data/weekly/2026-W37.json) | 10 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 328 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-14 | 10 | [View JSON](data/daily/2026-09-14.json) |
| 📄 2026-09-13 | 26 | [View JSON](data/daily/2026-09-13.json) |
| 📄 2026-09-12 | 26 | [View JSON](data/daily/2026-09-12.json) |
| 📄 2026-09-11 | 17 | [View JSON](data/daily/2026-09-11.json) |
| 📄 2026-09-10 | 20 | [View JSON](data/daily/2026-09-10.json) |
| 📄 2026-09-09 | 37 | [View JSON](data/daily/2026-09-09.json) |
| 📄 2026-09-08 | 6 | [View JSON](data/daily/2026-09-08.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W37 | 10 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 328 | [View JSON](data/monthly/2026-09.json) |
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
