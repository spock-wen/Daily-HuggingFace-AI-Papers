<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-18-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-2365+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">18</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">151</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">846</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">2365+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** February 20, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. SLA2: Sparse-Linear Attention with Learnable Routing and QAT</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12675) • [📄 arXiv](https://arxiv.org/abs/2602.12675) • [📥 PDF](https://arxiv.org/pdf/2602.12675)

**💻 Code:** [⭐ Code](https://github.com/thu-ml/SLA)

> Sparse-Linear Attention2 (SLA2) can achieve 97% attention sparsity and deliver an 18.6x attention speedup while preserving generation quality.

</details>

<details>
<summary><b>2. RynnBrain: Open Embodied Foundation Models</b> ⭐ 402</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14979) • [📄 arXiv](https://arxiv.org/abs/2602.14979) • [📥 PDF](https://arxiv.org/pdf/2602.14979)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/RynnBrain)

> 🚀 We’re excited to release our paper and fully open-source RynnBrain — an embodied foundation model designed as a unified cognitive brain for real-world agents. Unlike conventional VLMs that reason purely in text or static images, RynnBrain is exp...

</details>

<details>
<summary><b>3. Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16705) • [📄 arXiv](https://arxiv.org/abs/2602.16705) • [📥 PDF](https://arxiv.org/pdf/2602.16705)

> "HERO: Learning Humanoid End-Effector ContROl for Open-Vocabulary Visual Loco-Manipulation" Project page: https://hero-humanoid.github.io/

</details>

<details>
<summary><b>4. CADEvolve: Creating Realistic CAD via Program Evolution</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Valentin Khrulkov, Gregory Ivanov, Marina Barannikov, Maksim Elistratov, zhemchuzhnikov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16317) • [📄 arXiv](https://arxiv.org/abs/2602.16317) • [📥 PDF](https://arxiv.org/pdf/2602.16317)

**💻 Code:** [⭐ Code](https://github.com/zhemdi/CADEvolve)

> Title: CADEvolve: Creating Realistic CAD via Program Evolution Paper: https://arxiv.org/abs/2602.16317 Code: https://github.com/zhemdi/CADEvolve Dataset: https://huggingface.co/datasets/kulibinai/cadevolve Models: https://huggingface.co/kulibinai/...

</details>

<details>
<summary><b>5. Empty Shelves or Lost Keys? Recall Is the Bottleneck for Parametric Factuality</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14080) • [📄 arXiv](https://arxiv.org/abs/2602.14080) • [📥 PDF](https://arxiv.org/pdf/2602.14080)

> Why do frontier LLMs make factual errors? Is it because they never learned the fact… or because they can’t access knowledge they already encoded? This paper shows: The bottleneck is not encoding; it is recall.

</details>

<details>
<summary><b>6. MAEB: Massive Audio Embedding Benchmark</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16008) • [📄 arXiv](https://arxiv.org/abs/2602.16008) • [📥 PDF](https://arxiv.org/pdf/2602.16008)

> We extended MTEB with Audio support!

</details>

<details>
<summary><b>7. Towards a Science of AI Agent Reliability</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16666) • [📄 arXiv](https://arxiv.org/abs/2602.16666) • [📥 PDF](https://arxiv.org/pdf/2602.16666)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Lin...

</details>

<details>
<summary><b>8. Multi-agent cooperation through in-context co-player inference</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16301) • [📄 arXiv](https://arxiv.org/abs/2602.16301) • [📥 PDF](https://arxiv.org/pdf/2602.16301)

> Demonstrates that in-context learning in sequence-model agents enables learning-aware co-player adaptation and emergent cooperative behavior without explicit timescale separation.

</details>

<details>
<summary><b>9. World Action Models are Zero-shot Policies</b> ⭐ 742</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15922) • [📄 arXiv](https://arxiv.org/abs/2602.15922) • [📥 PDF](https://arxiv.org/pdf/2602.15922)

**💻 Code:** [⭐ Code](https://github.com/dreamzero0/dreamzero)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Causal World Modeling for Robot Control (2026) BagelVLA: Enhancing Long-Hor...

</details>

<details>
<summary><b>10. Reinforced Fast Weights with Next-Sequence Prediction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16704) • [📄 arXiv](https://arxiv.org/abs/2602.16704) • [📥 PDF](https://arxiv.org/pdf/2602.16704)

**💻 Code:** [⭐ Code](https://github.com/princetonvisualai/ReFINE) • [⭐ Code](https://github.com/princetonvisualai/ReFINE/)

> https://github.com/princetonvisualai/ReFINE/

</details>

<details>
<summary><b>11. SAM 3D Body: Robust Full-Body Human Mesh Recovery</b> ⭐ 2.63k</summary>

<br/>

**👥 Authors:** Taosha Fan, Anushka Sagar, Don Pinkus, Devansh Kukreja, Xitong Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15989) • [📄 arXiv](https://arxiv.org/abs/2602.15989) • [📥 PDF](https://arxiv.org/pdf/2602.15989)

**💻 Code:** [⭐ Code](https://github.com/facebookresearch/sam-3d-body)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API PEAR: Pixel-aligned Expressive humAn mesh Recovery (2026) DiffProxy: Multi-...

</details>

<details>
<summary><b>12. Learning Situated Awareness in the Real World</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Rajiv Dhawan, Yongyuan Liang, Joy Hsu, Ruilin Han, Chuhan Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16682) • [📄 arXiv](https://arxiv.org/abs/2602.16682) • [📥 PDF](https://arxiv.org/pdf/2602.16682)

> SAW-Bench introduces egocentric situated awareness in real-world video, challenging models with observer-centric reasoning and six tasks, revealing a substantial human-model gap.

</details>

<details>
<summary><b>13. MMA: Multimodal Memory Agent</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16493) • [📄 arXiv](https://arxiv.org/abs/2602.16493) • [📥 PDF](https://arxiv.org/pdf/2602.16493)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/MMA)

> https://github.com/AIGeeksGroup/MMA

</details>

<details>
<summary><b>14. Learning Personalized Agents from Human Feedback</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16173) • [📄 arXiv](https://arxiv.org/abs/2602.16173) • [📥 PDF](https://arxiv.org/pdf/2602.16173)

**💻 Code:** [⭐ Code](https://github.com/facebookresearch/PAHF)

> AI agents are powerful, but don’t stay aligned with you over time. When preferences shift, they don’t adapt. You correct them once…they repeat the mistake. 🤦 Introducing PAHF: continual personalization where agents learn from feedback to stay in s...

</details>

<details>
<summary><b>15. Optimizing Few-Step Generation with Adaptive Matching Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.07345) • [📄 arXiv](https://arxiv.org/abs/2602.07345) • [📥 PDF](https://arxiv.org/pdf/2602.07345)

> This paper proposes Adaptive Matching Distillation (AMD) , a unified optimization framework that significantly stabilizes and improves few-step diffusion distillation (e.g., SDXL, Wan2.1). 💡 Key Insight: The "Forbidden Zone" The authors identify a...

</details>

<details>
<summary><b>16. Visual Memory Injection Attacks for Multi-Turn Conversations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Matthias Hein, chs20

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15927) • [📄 arXiv](https://arxiv.org/abs/2602.15927) • [📥 PDF](https://arxiv.org/pdf/2602.15927)

**💻 Code:** [⭐ Code](https://github.com/chs20/visual-memory-injection)

> We propose “visual memory injection” attacks: small image perturbations that make generative large vision-language models behave normally at first but later trigger targeted harmful responses, even after several conversation turns.

</details>

<details>
<summary><b>17. BiManiBench: A Hierarchical Benchmark for Evaluating Bimanual Coordination of Multimodal Large Language Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.08392) • [📄 arXiv](https://arxiv.org/abs/2602.08392) • [📥 PDF](https://arxiv.org/pdf/2602.08392)

**💻 Code:** [⭐ Code](https://github.com/bimanibench/BiManiBench)

> Come and see our efforts in investigating how MLLMs perform for bimanual manipulation!

</details>

<details>
<summary><b>18. OPBench: A Graph Benchmark to Combat the Opioid Crisis</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zehong Wang, Zheyuan Zhang, Yiyue Qian, Yiyang Li, Tianyi Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14602) • [📄 arXiv](https://arxiv.org/abs/2602.14602) • [📥 PDF](https://arxiv.org/pdf/2602.14602)

**💻 Code:** [⭐ Code](https://github.com/Tianyi-Billy-Ma/OPBench)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Policy4OOD: A Knowledge-Guided World Model for Policy Intervention Simulati...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 18 |
| 📅 Today | [`2026-02-20.json`](data/daily/2026-02-20.json) | 18 |
| 📆 This Week | [`2026-W07.json`](data/weekly/2026-W07.json) | 151 |
| 🗓️ This Month | [`2026-02.json`](data/monthly/2026-02.json) | 846 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-02-20 | 18 | [View JSON](data/daily/2026-02-20.json) |
| 📄 2026-02-19 | 25 | [View JSON](data/daily/2026-02-19.json) |
| 📄 2026-02-18 | 35 | [View JSON](data/daily/2026-02-18.json) |
| 📄 2026-02-17 | 32 | [View JSON](data/daily/2026-02-17.json) |
| 📄 2026-02-16 | 41 | [View JSON](data/daily/2026-02-16.json) |
| 📄 2026-02-15 | 41 | [View JSON](data/daily/2026-02-15.json) |
| 📄 2026-02-14 | 41 | [View JSON](data/daily/2026-02-14.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W07 | 151 | [View JSON](data/weekly/2026-W07.json) |
| 📅 2026-W06 | 293 | [View JSON](data/weekly/2026-W06.json) |
| 📅 2026-W05 | 357 | [View JSON](data/weekly/2026-W05.json) |
| 📅 2026-W04 | 214 | [View JSON](data/weekly/2026-W04.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-02 | 846 | [View JSON](data/monthly/2026-02.json) |
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
