<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-15-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3885+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">15</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">57</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">121</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3885+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** May 07, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03849) • [📄 arXiv](https://arxiv.org/abs/2605.03849) • [📥 PDF](https://arxiv.org/pdf/2605.03849)

**💻 Code:** [⭐ Code](https://github.com/FrameX-AI/Stream-R1)

> TL;DR: Existing distribution-matching distillation (DMD) methods for streaming video diffusion treat every rollout, frame, and pixel as equally informative supervision. Stream-R1 instead reweights the DMD objective along two complementary axes, i....

</details>

<details>
<summary><b>2. Stream-T1: Test-Time Scaling for Streaming Video Generation</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.04461) • [📄 arXiv](https://arxiv.org/abs/2605.04461) • [📥 PDF](https://arxiv.org/pdf/2605.04461)

**💻 Code:** [⭐ Code](https://github.com/FrameX-AI/Stream-T1)

> While Test-Time Scaling (TTS) offers a promising direction to enhance video generation without the surging costs of training, current test-time video generation methods based on diffusion models suffer from exorbitant candidate exploration costs a...

</details>

<details>
<summary><b>3. RLDX-1 Technical Report</b> ⭐ 29</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03269) • [📄 arXiv](https://arxiv.org/abs/2605.03269) • [📥 PDF](https://arxiv.org/pdf/2605.03269)

**💻 Code:** [⭐ Code](https://github.com/RLWRLD/RLDX-1)

> While Vision-Language-Action models (VLAs) have shown remarkable progress toward human-like generalist robotic policies through the versatile intelligence (i.e., broad scene understanding and language-conditioned generalization) inherited from pre...

</details>

<details>
<summary><b>4. HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation</b> ⭐ 35</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.28196) • [📄 arXiv](https://arxiv.org/abs/2604.28196) • [📥 PDF](https://arxiv.org/pdf/2604.28196)

**💻 Code:** [⭐ Code](https://github.com/H-EmbodVis/HERMESV2)

> Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics. However, existing approaches predominantly focus on future scene generation, often overlooking comprehensive 3D scene understanding. Co...

</details>

<details>
<summary><b>5. PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Zanxin Chen, Yang Li, Junliang Ye, Chunshi Wang, Yunhan Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.05163) • [📄 arXiv](https://arxiv.org/abs/2605.05163) • [📥 PDF](https://arxiv.org/pdf/2605.05163)

**💻 Code:** [⭐ Code](https://github.com/HKU-MMLab/PhysForge)

> Accepted by ICML 2026

</details>

<details>
<summary><b>6. D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.05204) • [📄 arXiv](https://arxiv.org/abs/2605.05204) • [📥 PDF](https://arxiv.org/pdf/2605.05204)

**💻 Code:** [⭐ Code](https://github.com/vvvvvjdy/D-OPSD)

> On-Policy Self-Distillation for Diffusion Models

</details>

<details>
<summary><b>7. Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.04018) • [📄 arXiv](https://arxiv.org/abs/2605.04018) • [📥 PDF](https://arxiv.org/pdf/2605.04018)

**💻 Code:** [⭐ Code](https://github.com/yale-nlp/Bright-Pro)

> We introduce BRIGHT-Pro, an expert-annotated benchmark for multi-aspect evidence retrieval, RTriever-Synth, an aspect-decomposed synthetic training corpus, and RTriever-4B, a retriever tuned for reasoning-intensive agentic search. Our results show...

</details>

<details>
<summary><b>8. OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.05185) • [📄 arXiv](https://arxiv.org/abs/2605.05185) • [📥 PDF](https://arxiv.org/pdf/2605.05185)

**💻 Code:** [⭐ Code](https://github.com/shawn0728/OpenSearch-VL)

> Github Page: https://github.com/shawn0728/OpenSearch-VL Project Page: https://huggingface.co/OpenSearch-VL

</details>

<details>
<summary><b>9. Lightning Unified Video Editing via In-Context Sparse Attention</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenliang Zhong, Yingwei Song, Haopeng Li, Zikai Zhou, Shitong Shao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.04569) • [📄 arXiv](https://arxiv.org/abs/2605.04569) • [📥 PDF](https://arxiv.org/pdf/2605.04569)

> No abstract available.

</details>

<details>
<summary><b>10. Awaking Spatial Intelligence in Unified Multimodal Understanding and Generation</b> ⭐ 2.1k</summary>

<br/>

**👥 Authors:** Bo Wang, Wei Tang, Guoqing Ma, Wenbo Li, Lin Song

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.04128) • [📄 arXiv](https://arxiv.org/abs/2605.04128) • [📥 PDF](https://arxiv.org/pdf/2605.04128)

**💻 Code:** [⭐ Code](https://github.com/jd-opensource/JoyAI-Image)

> No abstract available.

</details>

<details>
<summary><b>11. Parameter-Efficient Multi-View Proficiency Estimation: From Discriminative Classification to Generative Feedback</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Antonio Liotta, Edoardo Bianchi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03848) • [📄 arXiv](https://arxiv.org/abs/2605.03848) • [📥 PDF](https://arxiv.org/pdf/2605.03848)

> Advances in Action Quality Assessment

</details>

<details>
<summary><b>12. APEX: Large-scale Multi-task Aesthetic-Informed Popularity Prediction for AI-Generated Music</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.03395) • [📄 arXiv](https://arxiv.org/abs/2605.03395) • [📥 PDF](https://arxiv.org/pdf/2605.03395)

**💻 Code:** [⭐ Code](https://github.com/AMAAI-Lab/apex)

> Large-scale aesthetics informed AI music hit prediction model in terms of a streams and likes-score.

</details>

<details>
<summary><b>13. ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.00380) • [📄 arXiv](https://arxiv.org/abs/2605.00380) • [📥 PDF](https://arxiv.org/pdf/2605.00380)

**💻 Code:** [⭐ Code](https://github.com/1229095296/ResRL)

> Accepted by ICML2026 poster.

</details>

<details>
<summary><b>14. MedSkillAudit: A Domain-Specific Audit Framework for Medical Research Agent Skills</b> ⭐ 515</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.20441) • [📄 arXiv](https://arxiv.org/abs/2604.20441) • [📥 PDF](https://arxiv.org/pdf/2604.20441)

**💻 Code:** [⭐ Code](https://github.com/aipoch/medical-research-skills)

> We're in the middle of a skill/agent explosion — everyone is packaging capabilities as reusable modules. But medical research skills can't just be "probably fine." A skill that generates plausible-sounding but subtly wrong study designs, or runs a...

</details>

<details>
<summary><b>15. Diffusion Model as a Generalist Segmentation Learner</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Changhao Pan, Peilin Sun, Haiyang Sun, Antao Xiang, Haoxiao Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24575) • [📄 arXiv](https://arxiv.org/abs/2604.24575) • [📥 PDF](https://arxiv.org/pdf/2604.24575)

> Diffusion Model as a Generalist Segmentation Learner

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 15 |
| 📅 Today | [`2026-05-07.json`](data/daily/2026-05-07.json) | 15 |
| 📆 This Week | [`2026-W18.json`](data/weekly/2026-W18.json) | 57 |
| 🗓️ This Month | [`2026-05.json`](data/monthly/2026-05.json) | 121 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-05-07 | 15 | [View JSON](data/daily/2026-05-07.json) |
| 📄 2026-05-06 | 17 | [View JSON](data/daily/2026-05-06.json) |
| 📄 2026-05-05 | 13 | [View JSON](data/daily/2026-05-05.json) |
| 📄 2026-05-04 | 12 | [View JSON](data/daily/2026-05-04.json) |
| 📄 2026-05-03 | 24 | [View JSON](data/daily/2026-05-03.json) |
| 📄 2026-05-02 | 24 | [View JSON](data/daily/2026-05-02.json) |
| 📄 2026-05-01 | 16 | [View JSON](data/daily/2026-05-01.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W18 | 57 | [View JSON](data/weekly/2026-W18.json) |
| 📅 2026-W17 | 120 | [View JSON](data/weekly/2026-W17.json) |
| 📅 2026-W16 | 156 | [View JSON](data/weekly/2026-W16.json) |
| 📅 2026-W15 | 125 | [View JSON](data/weekly/2026-W15.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-05 | 121 | [View JSON](data/monthly/2026-05.json) |
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
