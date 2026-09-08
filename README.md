<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-6-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7172+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">6</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">25</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">192</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7172+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 08, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Unlocking Lossless Speedups in LLMs via Discrete Diffusion</b> ⭐ 44</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04010) • [📄 arXiv](https://arxiv.org/abs/2605.12825) • [📥 PDF](https://arxiv.org/pdf/2609.04010)

**💻 Code:** [⭐ Code](https://github.com/ifm-ai/uno) • [⭐ Code](https://github.com/huggingface)

> Isn't the core framework here exactly the same as Orthrus, released 4 months ago? https://arxiv.org/abs/2605.12825

</details>

<details>
<summary><b>2. FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.03241) • [📄 arXiv](https://arxiv.org/abs/2609.03241) • [📥 PDF](https://arxiv.org/pdf/2609.03241)

**💻 Code:** [⭐ Code](https://github.com/alexhuang13/FlowBalance) • [⭐ Code](https://github.com/huggingface)

> FlowBalance is a verifier-grounded self-improvement method for reasoning models. It addresses one known failure mode of OPSD on thinking models: privileged feedback can reinforce locally plausible but verifier-wrong traces. FlowBalance combines sp...

</details>

<details>
<summary><b>3. EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents</b> ⭐ 26</summary>

<br/>

**👥 Authors:** Tianwei Lin, Yuqian Yuan, Yutong Lin, Wenqiao Zhang, Thinkitin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01281) • [📄 arXiv](https://arxiv.org/abs/2609.01281) • [📥 PDF](https://arxiv.org/pdf/2609.01281)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DCDmllm/EmbodiedSkills)

> EmbodiedSkills is a unified framework for organizing VLM planning, VLA execution, and environment feedback within a single robot agent. It connects these components through a shared executable-skill interface and a six-stage loop: Observe, Plan, P...

</details>

<details>
<summary><b>4. One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.25936) • [📄 arXiv](https://arxiv.org/abs/2608.25936) • [📥 PDF](https://arxiv.org/pdf/2608.25936)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> On-Policy Self-Distillation (OPSD) makes a model teach itself using privileged information: a reference solution, a plan, environment feedback. No larger teacher is required. But the same asymmetry that creates the signal also biases it, and one f...

</details>

<details>
<summary><b>5. Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Bin Liang, Kang Peng, Zechen Sun, Zhiwei Zhang, Hiiamein

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02998) • [📄 arXiv](https://arxiv.org/abs/2609.02998) • [📥 PDF](https://arxiv.org/pdf/2609.02998)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation

</details>

<details>
<summary><b>6. What Else Needs Fixing? Exploring Cost-Effective Test-Time Compute for Revision Propagation in Artifacts Generated Through Conversation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** oookiku

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.03254) • [📄 arXiv](https://arxiv.org/abs/2609.03254) • [📥 PDF](https://arxiv.org/pdf/2609.03254)

**💻 Code:** [⭐ Code](https://github.com/ntt-dkiku/llm-revision-propagation) • [⭐ Code](https://github.com/huggingface)

> In this paper, we propose RevPropBench, a benchmark for evaluating the ability of LLMs to propagate revisions across dependent elements in conversationally generated JSON artifacts when users specify only a local change. We also explore cost-effec...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 6 |
| 📅 Today | [`2026-09-08.json`](data/daily/2026-09-08.json) | 6 |
| 📆 This Week | [`2026-W36.json`](data/weekly/2026-W36.json) | 25 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 192 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-08 | 6 | [View JSON](data/daily/2026-09-08.json) |
| 📄 2026-09-07 | 19 | [View JSON](data/daily/2026-09-07.json) |
| 📄 2026-09-06 | 31 | [View JSON](data/daily/2026-09-06.json) |
| 📄 2026-09-05 | 31 | [View JSON](data/daily/2026-09-05.json) |
| 📄 2026-09-04 | 23 | [View JSON](data/daily/2026-09-04.json) |
| 📄 2026-09-03 | 28 | [View JSON](data/daily/2026-09-03.json) |
| 📄 2026-09-02 | 21 | [View JSON](data/daily/2026-09-02.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W36 | 25 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 192 | [View JSON](data/monthly/2026-09.json) |
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
