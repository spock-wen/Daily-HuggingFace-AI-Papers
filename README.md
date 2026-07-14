<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-12-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5964+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">12</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">25</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">276</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5964+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 14, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. ABot-N1: Toward a General Visual Language Navigation Foundation Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.10383) • [📄 arXiv](https://arxiv.org/abs/2607.10383) • [📥 PDF](https://arxiv.org/pdf/2607.10383)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>2. ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.10350) • [📄 arXiv](https://arxiv.org/abs/2607.10350) • [📥 PDF](https://arxiv.org/pdf/2607.10350)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present ABot-AgentOS, a general robotic Agent Operating System that sits above low-level controllers and provides a deliberative agent layer for scene-conditioned planning, context-isolated skill execution, multi-stage verification, multi-modal...

</details>

<details>
<summary><b>3. Weak-to-Strong Generalization via Direct On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05394) • [📄 arXiv](https://arxiv.org/abs/2607.05394) • [📥 PDF](https://arxiv.org/pdf/2607.05394)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> RLVR is powerful, but repeating it for every larger target model is expensive: each target must generate its own rollouts and rediscover useful learning signals from sparse outcome rewards. Can RL on a small, weaker model improve a stronger studen...

</details>

<details>
<summary><b>4. 4D Human-Scene Reconstruction from Low-Overlap Captures</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.09125) • [📄 arXiv](https://arxiv.org/abs/2607.09125) • [📥 PDF](https://arxiv.org/pdf/2607.09125)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Four cameras around a room, roughly 90° apart, with barely any overlap between neighboring views. COLMAP doesn't even register them. That's the setting we went after. Our insight: backgrounds and humans want different priors, so we stop making one...

</details>

<details>
<summary><b>5. LightMem-Ego: Your AI Memory for Everyday Life</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11487) • [📄 arXiv](https://arxiv.org/abs/2607.11487) • [📥 PDF](https://arxiv.org/pdf/2607.11487)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> LightMem-Ego: Bringing lifelong memory to AI assistants on smartphones and AI glasses, enabling them to see, remember, and help with your daily life.

</details>

<details>
<summary><b>6. AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation and Verification</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11849) • [📄 arXiv](https://arxiv.org/abs/2607.11849) • [📥 PDF](https://arxiv.org/pdf/2607.11849)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce AdvancedMathBench, a benchmark suite designed to evaluate advanced mathematical reasoning capabilities.

</details>

<details>
<summary><b>7. Metacognition in LLMs: Foundations, Progress, and Opportunities</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11881) • [📄 arXiv](https://arxiv.org/abs/2607.11881) • [📥 PDF](https://arxiv.org/pdf/2607.11881)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Metacognition is a foundational component of intelligence that has become increasingly recognized as a cornerstone of capable, transparent AI systems. While LLMs have made significant progress, it remains unclear when, how, or to what extent they ...

</details>

<details>
<summary><b>8. Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm via Proxy-Guided Update Signals</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11505) • [📄 arXiv](https://arxiv.org/abs/2607.11505) • [📥 PDF](https://arxiv.org/pdf/2607.11505)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Post-training is essential for refining the domain-specific capabilities of large language models (LLMs), yet existing reward optimization and distribution matching methods tightly couple policy exploration with distribution alignment. This coupli...

</details>

<details>
<summary><b>9. NeuroCogMap Reveals Cognitive Organization of Large Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Qipeng Wang, Qi Li, Qiang Ma, Haolang Lu, Zhongxiang Sun

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.00397) • [📄 arXiv](https://arxiv.org/abs/2607.00397) • [📥 PDF](https://arxiv.org/pdf/2607.00397)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> NeuroCogMap maps reproducible cognitive organization within large language models, revealing how functional systems support capabilities, break down in model pathologies, align with human cortical activity and inform cognitive-model discovery.

</details>

<details>
<summary><b>10. Motion4Motion: Motion Transfer Across Subjects at Inference</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Gang Yu, Xianfang Zeng, Duomin Wang, Zixin Yin, Ling-Hao Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11644) • [📄 arXiv](https://arxiv.org/abs/2607.11644) • [📥 PDF](https://arxiv.org/pdf/2607.11644)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.09362) • [📄 arXiv](https://arxiv.org/abs/2607.09362) • [📥 PDF](https://arxiv.org/pdf/2607.09362)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/nxnai/CtrlVTON)

> CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation VITON-HD-edit dataset: https://huggingface.co/datasets/NXN-Labs/VITON-HD-edit GitHub: https://github.com/nxnai/CtrlVTON Project page: COMING SOON! Our previous work: htt...

</details>

<details>
<summary><b>12. LATO.2: Factorized 3D Mesh Generation with Vertex and Topology Flow</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Huipeng Guo, Youjia Zhang, Junkai Lin, Tianhao Zhao, Hang Long

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.10623) • [📄 arXiv](https://arxiv.org/abs/2607.10623) • [📥 PDF](https://arxiv.org/pdf/2607.10623)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 12 |
| 📅 Today | [`2026-07-14.json`](data/daily/2026-07-14.json) | 12 |
| 📆 This Week | [`2026-W28.json`](data/weekly/2026-W28.json) | 25 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 276 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-14 | 12 | [View JSON](data/daily/2026-07-14.json) |
| 📄 2026-07-13 | 13 | [View JSON](data/daily/2026-07-13.json) |
| 📄 2026-07-12 | 23 | [View JSON](data/daily/2026-07-12.json) |
| 📄 2026-07-11 | 23 | [View JSON](data/daily/2026-07-11.json) |
| 📄 2026-07-10 | 19 | [View JSON](data/daily/2026-07-10.json) |
| 📄 2026-07-09 | 7 | [View JSON](data/daily/2026-07-09.json) |
| 📄 2026-07-08 | 26 | [View JSON](data/daily/2026-07-08.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W28 | 25 | [View JSON](data/weekly/2026-W28.json) |
| 📅 2026-W27 | 133 | [View JSON](data/weekly/2026-W27.json) |
| 📅 2026-W26 | 165 | [View JSON](data/weekly/2026-W26.json) |
| 📅 2026-W25 | 155 | [View JSON](data/weekly/2026-W25.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 276 | [View JSON](data/monthly/2026-07.json) |
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
