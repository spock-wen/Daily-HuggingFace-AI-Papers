<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-19-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3737+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">19</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">29</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">579</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3737+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** April 28, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. World-R1: Reinforcing 3D Constraints for Text-to-Video Generation</b> ⭐ 23</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24764) • [📄 arXiv](https://arxiv.org/abs/2604.24764) • [📥 PDF](https://arxiv.org/pdf/2604.24764)

**💻 Code:** [⭐ Code](https://github.com/microsoft/World-R1)

> World-R1: Reinforcing 3D Constraints for Text-to-Video Generation

</details>

<details>
<summary><b>2. ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning</b> ⭐ 23</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24300) • [📄 arXiv](https://arxiv.org/abs/2604.24300) • [📥 PDF](https://arxiv.org/pdf/2604.24300)

**💻 Code:** [⭐ Code](https://github.com/3dlg-hcvc/revsi)

> Check our project page: https://3dlg-hcvc.github.io/revsi/

</details>

<details>
<summary><b>3. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Bojun Zou, Ruhao Liu, Weiqi Huang, Bo Yin, Qi Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.23775) • [📄 arXiv](https://arxiv.org/abs/2604.23775) • [📥 PDF](https://arxiv.org/pdf/2604.23775)

**💻 Code:** [⭐ Code](https://github.com/LiQiiiii/Awesome-VLA-Safety)

> GitHub Repo: https://github.com/LiQiiiii/Awesome-VLA-Safety

</details>

<details>
<summary><b>4. From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company</b> ⭐ 57</summary>

<br/>

**👥 Authors:** Lee Ka Yiu, Yuxuan Huang, Zhiyuan He, Yu Fu, fredreick

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.22446) • [📄 arXiv](https://arxiv.org/abs/2604.22446) • [📥 PDF](https://arxiv.org/pdf/2604.22446)

**💻 Code:** [⭐ Code](https://github.com/1mancompany/OneManCompany)

> OneManCompany (OMC) reframes multi-agent systems as a self-organising company—capable of hiring, restructuring, and reviewing its own work during execution, rather than operating as a fixed, pre-defined team. Instead of scaling capability by stack...

</details>

<details>
<summary><b>5. ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents</b> ⭐ 80</summary>

<br/>

**👥 Authors:** Xiangyan Liu, Guanzheng Chen, Zijian Wu, Lingxiao Du, Fanqing Meng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.23781) • [📄 arXiv](https://arxiv.org/abs/2604.23781) • [📥 PDF](https://arxiv.org/pdf/2604.23781)

**💻 Code:** [⭐ Code](https://github.com/evolvent-ai/ClawMark)

> Language-model agents are increasingly used as persistent coworkers that assist users across multiple working days. During such workflows, the surrounding environment may change independently of the agent: new emails arrive, calendar entries shift...

</details>

<details>
<summary><b>6. Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24198) • [📄 arXiv](https://arxiv.org/abs/2604.24198) • [📥 PDF](https://arxiv.org/pdf/2604.24198)

> DataPRM is an environment-aware generative process reward model that actively verifies execution and distinguishes error types, significantly improving LLM performance on dynamic data analysis tasks.

</details>

<details>
<summary><b>7. SketchVLM: Vision language models can annotate images to explain thoughts and guide users</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Trung Bui, Mohammad Reza Taesiri, Hung Huy Nguyen, Logan Bolton, Brandon Collins

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.22875) • [📄 arXiv](https://arxiv.org/abs/2604.22875) • [📥 PDF](https://arxiv.org/pdf/2604.22875)

> Demo: https://sketch-vlm-demo.vercel.app/

</details>

<details>
<summary><b>8. Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tianhong Li, Shoufa Chen, Xiaoke Huang, Weiming Ren, Zhiheng Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24763) • [📄 arXiv](https://arxiv.org/abs/2604.24763) • [📥 PDF](https://arxiv.org/pdf/2604.24763)

> No abstract available.

</details>

<details>
<summary><b>9. Efficient Agent Evaluation via Diversity-Guided User Simulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.21480) • [📄 arXiv](https://arxiv.org/abs/2604.21480) • [📥 PDF](https://arxiv.org/pdf/2604.21480)

> Treat agent evaluation as a tree, not repeated full rollouts. We branch from key decision points with diverse user responses to uncover new failures with less compute.

</details>

<details>
<summary><b>10. Stabilizing Efficient Reasoning with Step-Level Advantage Selection</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24003) • [📄 arXiv](https://arxiv.org/abs/2604.24003) • [📥 PDF](https://arxiv.org/pdf/2604.24003)

**💻 Code:** [⭐ Code](https://github.com/HanNight/SAS)

> No abstract available.

</details>

<details>
<summary><b>11. OmniShotCut: Holistic Relational Shot Boundary Detection with Shot-Query Transformer</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Zezhou Cheng, Jiahui Zhang, Zhipeng Tang, Guangyi Xu, Boyang Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24762) • [📄 arXiv](https://arxiv.org/abs/2604.24762) • [📥 PDF](https://arxiv.org/pdf/2604.24762)

**💻 Code:** [⭐ Code](https://github.com/UVA-Computer-Vision-Lab/OmniShotCut)

> OmniShotCut is a sensitive and more informative SoTA on the Shot Boundary Detection task. OmniShotCut can detect shot changes of the video in diverse sources (anime, vlog, game, shorts, sports, screen recording, etc.), and recognize Sudden Jump an...

</details>

<details>
<summary><b>12. For-Value: Efficient Forward-Only Data Valuation for finetuning LLMs and VLMs</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Zixin Ding, Minghui Chen, Jiaming Zhang, Qi Zeng, Wenlong Deng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2508.10180) • [📄 arXiv](https://arxiv.org/abs/2508.10180) • [📥 PDF](https://arxiv.org/pdf/2508.10180)

**💻 Code:** [⭐ Code](https://github.com/vengdeng/For-Value-Efficient-Forward-Only-Data-Valuation-for-finetuning)

> Data valuation is essential for enhancing the transparency and accountability of large language models (LLMs) and vision-language models (VLMs). However, existing methods typically rely on gradient computations, making them computationally prohibi...

</details>

<details>
<summary><b>13. Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.19548) • [📄 arXiv](https://arxiv.org/abs/2604.19548) • [📥 PDF](https://arxiv.org/pdf/2604.19548)

**💻 Code:** [⭐ Code](https://github.com/unikcc/ReTAS)

> A few things from the paper: (1) Multi-agent self-reflection has a built-in cognitive trap. The same model attributes the same failure to opposite sources just because we re-label its role. When it acts and then self-reflects, it blames external f...

</details>

<details>
<summary><b>14. ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.23099) • [📄 arXiv](https://arxiv.org/abs/2604.23099) • [📥 PDF](https://arxiv.org/pdf/2604.23099)

**💻 Code:** [⭐ Code](https://github.com/google-deepmind/proeval)

> No abstract available.

</details>

<details>
<summary><b>15. Discovering Agentic Safety Specifications from 1-Bit Danger Signals</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Víctor Gallego

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.23210) • [📄 arXiv](https://arxiv.org/abs/2604.23210) • [📥 PDF](https://arxiv.org/pdf/2604.23210)

> @ librarian-bot recommend

</details>

<details>
<summary><b>16. ATTN-FIQA: Interpretable Attention-based Face Image Quality Assessment with Vision Transformers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.22841) • [📄 arXiv](https://arxiv.org/abs/2604.22841) • [📥 PDF](https://arxiv.org/pdf/2604.22841)

**💻 Code:** [⭐ Code](https://github.com/gurayozgur/ATTN-FIQA)

> Interpretable Attention-based Face Image Quality Assessment

</details>

<details>
<summary><b>17. EX-FIQA: Leveraging Intermediate Early eXit Representations from Vision Transformers for Face Image Quality Assessment</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.22842) • [📄 arXiv](https://arxiv.org/abs/2604.22842) • [📥 PDF](https://arxiv.org/pdf/2604.22842)

**💻 Code:** [⭐ Code](https://github.com/gurayozgur/EX-FIQA)

> Early Exits for Face Image Quality Assessment

</details>

<details>
<summary><b>18. Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Pradeep Kumar Jayaraman, Kamal Rahimi Malekshan, Farzaneh Askari, Mohammadmehdi Ataei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.24479) • [📄 arXiv](https://arxiv.org/abs/2604.24479) • [📥 PDF](https://arxiv.org/pdf/2604.24479)

> No abstract available.

</details>

<details>
<summary><b>19. Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.22782) • [📄 arXiv](https://arxiv.org/abs/2604.22782) • [📥 PDF](https://arxiv.org/pdf/2604.22782)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 19 |
| 📅 Today | [`2026-04-28.json`](data/daily/2026-04-28.json) | 19 |
| 📆 This Week | [`2026-W17.json`](data/weekly/2026-W17.json) | 29 |
| 🗓️ This Month | [`2026-04.json`](data/monthly/2026-04.json) | 579 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-04-28 | 19 | [View JSON](data/daily/2026-04-28.json) |
| 📄 2026-04-27 | 10 | [View JSON](data/daily/2026-04-27.json) |
| 📄 2026-04-26 | 22 | [View JSON](data/daily/2026-04-26.json) |
| 📄 2026-04-25 | 22 | [View JSON](data/daily/2026-04-25.json) |
| 📄 2026-04-24 | 15 | [View JSON](data/daily/2026-04-24.json) |
| 📄 2026-04-23 | 16 | [View JSON](data/daily/2026-04-23.json) |
| 📄 2026-04-22 | 49 | [View JSON](data/daily/2026-04-22.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W17 | 29 | [View JSON](data/weekly/2026-W17.json) |
| 📅 2026-W16 | 156 | [View JSON](data/weekly/2026-W16.json) |
| 📅 2026-W15 | 125 | [View JSON](data/weekly/2026-W15.json) |
| 📅 2026-W14 | 147 | [View JSON](data/weekly/2026-W14.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-04 | 579 | [View JSON](data/monthly/2026-04.json) |
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
