<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-9-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9332+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">9</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">120</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1571</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9332+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 29, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion Language Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35201) • [📄 arXiv](https://arxiv.org/abs/2610.35201) • [📥 PDF](https://arxiv.org/pdf/2610.35201)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJU-OmniAI/DTCA)

> Which tokens contribute most to a diffusion language model’s response? As tokens are revealed during denoising, they help shape predictions at the remaining masked positions. However, final-answer rewards provide little information about these ind...

</details>

<details>
<summary><b>2. Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32749) • [📄 arXiv](https://arxiv.org/abs/2610.32749) • [📥 PDF](https://arxiv.org/pdf/2610.32749)

**💻 Code:** [⭐ Code](https://github.com/JusperLee/Falcon) • [⭐ Code](https://github.com/huggingface)

> Falcon is a causal audio-visual target speaker extraction model that uses the target speaker's mouth video to extract their voice from noisy, overlapping speech. It combines a single-pass multi-scale time-frequency separator with an encoder-space ...

</details>

<details>
<summary><b>3. OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35684) • [📄 arXiv](https://arxiv.org/abs/2610.35684) • [📥 PDF](https://arxiv.org/pdf/2610.35684)

**💻 Code:** [⭐ Code](https://github.com/justin4ai/OmniShowcase) • [⭐ Code](https://github.com/huggingface)

> OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images What OmniShowcase offers: 🔄 Every side, consistently: Generate videos of a subject from just 4 reference images , keeping identity and 3D shape consistent eve...

</details>

<details>
<summary><b>4. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31670) • [📄 arXiv](https://arxiv.org/abs/2610.31670) • [📥 PDF](https://arxiv.org/pdf/2610.31670)

**💻 Code:** [⭐ Code](https://github.com/yunfeixie233/sensorimotor-alignment) • [⭐ Code](https://github.com/huggingface)

> The Platonic Representation Hypothesis (Huh et al, 2024) argues that as vision and language models scale, their representation spaces converge toward a shared statistical model of reality. The idea is that images and text are different projections...

</details>

<details>
<summary><b>5. TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37230) • [📄 arXiv](https://arxiv.org/abs/2610.37230) • [📥 PDF](https://arxiv.org/pdf/2610.37230)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DeepInfer recently open-sourced how DeepSeek manages the KV cache with 3FS and balances prefill and decode loads. Since some of those load balancers remain unreleased, they propose their own effective router, TAO—a tool-aware joint scheduling fram...

</details>

<details>
<summary><b>6. TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using Conversational Agents</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30161) • [📄 arXiv](https://arxiv.org/abs/2610.30161) • [📥 PDF](https://arxiv.org/pdf/2610.30161)

**💻 Code:** [⭐ Code](https://github.com/npci/TauIndianBankBench) • [⭐ Code](https://github.com/huggingface)

> Hi everyone, author here! 👋 Thanks for checking out TauIndianBankBench . TL;DR: Most agent benchmarks only check the final database state. But many required banking steps, like getting a closure quote before closing a deposit, don't change any rec...

</details>

<details>
<summary><b>7. CausGround: Causal Interaction Grounding for Adaptive Embodied Planning</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jiaming Mi, Wanyue Zhang, Jinbang Guo, Diqi He, Yijun Shen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.29702) • [📄 arXiv](https://arxiv.org/abs/2610.29702) • [📥 PDF](https://arxiv.org/pdf/2610.29702)

**💻 Code:** [⭐ Code](https://github.com/Intelligent-Interaction/CausGround) • [⭐ Code](https://github.com/huggingface)

> CausGround: Causal Interaction Grounding for Adaptive Embodied Planning Embodied planning requires more than knowing what to do. Agents must also understand when an action is executable and how it changes the world. We introduce CausGround , a non...

</details>

<details>
<summary><b>8. HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Zijian Yang, Yuheng Huang, Hengtao Li, Jiacheng Liu, yliu-cs

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34186) • [📄 arXiv](https://arxiv.org/abs/2610.34186) • [📥 PDF](https://arxiv.org/pdf/2610.34186)

**💻 Code:** [⭐ Code](https://github.com/yliu-cs/HuGe) • [⭐ Code](https://github.com/huggingface)

> HuGe (Humanoid Generalist) is a family of vision-language-action models for humanoid whole-body control. This repository provides Qwen3-VL-2B-Instruct implementations of OFT-, GR00T-, and Pi-style policies that predict SONIC motion tokens and hand...

</details>

<details>
<summary><b>9. OmniSpectra: A Unified Foundation Model for Universal Spectra Representation Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Judy Fox, Adam S. Bolton, Md Khairul Islam, xiazeyu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2601.15351) • [📄 arXiv](https://arxiv.org/abs/2601.15351) • [📥 PDF](https://arxiv.org/pdf/2601.15351)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! Co-author here 👋 Spectra from different instruments sample the same wavelengths on very different pixel grids (up to 25× apart in our training corpus). Standard sequence models position tokens by pixel index, so the same line (e.g. Hα...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 9 |
| 📅 Today | [`2026-10-29.json`](data/daily/2026-10-29.json) | 9 |
| 📆 This Week | [`2026-W43.json`](data/weekly/2026-W43.json) | 120 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1571 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-29 | 9 | [View JSON](data/daily/2026-10-29.json) |
| 📄 2026-10-28 | 40 | [View JSON](data/daily/2026-10-28.json) |
| 📄 2026-10-27 | 43 | [View JSON](data/daily/2026-10-27.json) |
| 📄 2026-10-26 | 28 | [View JSON](data/daily/2026-10-26.json) |
| 📄 2026-10-25 | 49 | [View JSON](data/daily/2026-10-25.json) |
| 📄 2026-10-24 | 50 | [View JSON](data/daily/2026-10-24.json) |
| 📄 2026-10-23 | 36 | [View JSON](data/daily/2026-10-23.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W43 | 120 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1571 | [View JSON](data/monthly/2026-10.json) |
| 🗓️ 2026-09 | 781 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |

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
