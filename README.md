<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-9-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5495+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">9</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">673</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5495+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 22, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19534) • [📄 arXiv](https://arxiv.org/abs/2606.19534) • [📥 PDF](https://arxiv.org/pdf/2606.19534)

**💻 Code:** [⭐ Code](https://github.com/MSALab-PKU/PerceptionDLM) • [⭐ Code](https://github.com/huggingface)

> 🚀 PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models We introduce PerceptionDLM, a multimodal diffusion VLM built for efficient parallel region perception. Instead of describing image regions one-by-one like autore...

</details>

<details>
<summary><b>2. GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents</b> ⭐ 63</summary>

<br/>

**👥 Authors:** Benshuo Fu, Zijun Zhao, Yimeng Chen, Yibo Yang, Ray368

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18829) • [📄 arXiv](https://arxiv.org/abs/2606.18829) • [📥 PDF](https://arxiv.org/pdf/2606.18829)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/rzhub/GateMem)

> Thanks for checking out GateMem! GateMem is a benchmark for memory governance in multi-principal shared-memory agents. Instead of only asking whether an agent can remember information, GateMem evaluates whether a persistent-memory agent can remain...

</details>

<details>
<summary><b>3. BrainG3N: A Dual-Purpose Tokenizer for Controllable 3D Brain MRI Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19651) • [📄 arXiv](https://arxiv.org/abs/2606.19651) • [📥 PDF](https://arxiv.org/pdf/2606.19651)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> BrainG3N: A Dual-Purpose Tokenizer for Controllable 3D Brain MRI Generation BrainG3N is a controllable generator for 3D brain MRI built on top of a strong self-supervised foundation encoder. A frozen 3D MAE encoder (pretrained on 35,309 volumes ac...

</details>

<details>
<summary><b>4. MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Yibo Yang, Jun Zhu, Yangyang Xu, huohua325

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.17162) • [📄 arXiv](https://arxiv.org/abs/2606.17162) • [📥 PDF](https://arxiv.org/pdf/2606.17162)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/huohua325/Memslides)

> Thanks for checking out MemSlides! MemSlides is a hierarchical memory-driven agent framework for personalized slide generation and multi-turn local revision. Links: Project page: https://memslides.github.io/ Code: https://github.com/huohua325/Mems...

</details>

<details>
<summary><b>5. WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tianhao Zhou, Yifan Chang, Haojian Huang, Jianchong Su, Yehang Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18847) • [📄 arXiv](https://arxiv.org/abs/2606.18847) • [📥 PDF](https://arxiv.org/pdf/2606.18847)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. Existing long-term memory benchmarks mainly evaluate language-centric retrieval and question answering, while e...

</details>

<details>
<summary><b>6. GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.17480) • [📄 arXiv](https://arxiv.org/abs/2606.17480) • [📥 PDF](https://arxiv.org/pdf/2606.17480)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGeeksGroup/GeneralVLA-2)

> open-sourced

</details>

<details>
<summary><b>7. Distilling Examples into Task Instructions: Enhanced In-Context Learning for Real-World B2B Conversations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Omri Allouche, Danit Berger Zalmanson, Adi Kopilov, Guy Rotman

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.15641) • [📄 arXiv](https://arxiv.org/abs/2606.15641) • [📥 PDF](https://arxiv.org/pdf/2606.15641)

**💻 Code:** [⭐ Code](https://github.com/gong-io/call-playbook) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/gong-io/call-playbook/)

> In-context learning (ICL) is the standard method for low-resource classification, yet its efficacy in specialized domains remains largely unexplored. We address the challenge of classifying semantically complex, multi-party B2B conversations, wher...

</details>

<details>
<summary><b>8. Multi-Turn Reflective Masking Elicits Reasoning in Mask Diffusion Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.16700) • [📄 arXiv](https://arxiv.org/abs/2606.16700) • [📥 PDF](https://arxiv.org/pdf/2606.16700)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What is the native form of reasoning for Mask Diffusion Models (LLaDa, DiffusionGemma, etc.)? For autoregressive language models, reasoning has largely been framed as continuation: generate a chain of thought, reflect on it, and append more tokens...

</details>

<details>
<summary><b>9. SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yang Zhao, Ziming Wang, Yuanming Li, Zeyu Zhang, Yiran Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.15659) • [📄 arXiv](https://arxiv.org/abs/2606.15659) • [📥 PDF](https://arxiv.org/pdf/2606.15659)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> https://spatialwalk.github.io/SpatialAvatar-0/

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 9 |
| 📅 Today | [`2026-06-22.json`](data/daily/2026-06-22.json) | 9 |
| 📆 This Week | [`2026-W25.json`](data/weekly/2026-W25.json) | 9 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 673 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-22 | 9 | [View JSON](data/daily/2026-06-22.json) |
| 📄 2026-06-21 | 34 | [View JSON](data/daily/2026-06-21.json) |
| 📄 2026-06-20 | 34 | [View JSON](data/daily/2026-06-20.json) |
| 📄 2026-06-19 | 25 | [View JSON](data/daily/2026-06-19.json) |
| 📄 2026-06-18 | 16 | [View JSON](data/daily/2026-06-18.json) |
| 📄 2026-06-17 | 21 | [View JSON](data/daily/2026-06-17.json) |
| 📄 2026-06-16 | 32 | [View JSON](data/daily/2026-06-16.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W25 | 9 | [View JSON](data/weekly/2026-W25.json) |
| 📅 2026-W24 | 194 | [View JSON](data/weekly/2026-W24.json) |
| 📅 2026-W23 | 247 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 673 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |

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
