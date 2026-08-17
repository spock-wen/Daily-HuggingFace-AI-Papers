<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-18-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6687+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">18</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">416</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6687+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 17, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systematic Evaluation of Detectors, Generators and Social Dissemination</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14391) • [📄 arXiv](https://arxiv.org/abs/2608.14391) • [📥 PDF](https://arxiv.org/pdf/2608.14391)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/24029100313/RA-Bench)

> A Systematic Evaluation of Detectors, Generators and Social Dissemination

</details>

<details>
<summary><b>2. Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13417) • [📄 arXiv](https://arxiv.org/abs/2608.13417) • [📥 PDF](https://arxiv.org/pdf/2608.13417)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 We are excited to share Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development . 🔍 As AI agents increasingly tackle long-horizon research and engineering tasks, evaluating them by final scores alone i...

</details>

<details>
<summary><b>3. Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Lixin Gu, Jiaye Ge, Ning Ding, Jifeng Ding, Kai Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14290) • [📄 arXiv](https://arxiv.org/abs/2608.14290) • [📥 PDF](https://arxiv.org/pdf/2608.14290)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>4. MobileMem: Learning from a Year of Mobile Experiences</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13606) • [📄 arXiv](https://arxiv.org/abs/2608.13606) • [📥 PDF](https://arxiv.org/pdf/2608.13606)

**💻 Code:** [⭐ Code](https://github.com/zjunlp/MobileMem) • [⭐ Code](https://github.com/huggingface)

> MobileMem, a benchmark and framework for studying on-device long-term memory, grounded in a year-scale collection of mobile experiences.

</details>

<details>
<summary><b>5. HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13555) • [📄 arXiv](https://arxiv.org/abs/2608.13555) • [📥 PDF](https://arxiv.org/pdf/2608.13555)

**💻 Code:** [⭐ Code](https://github.com/GalaxyGeneralRobotics/HumanTracker) • [⭐ Code](https://github.com/huggingface)

> We introduce HumanTracker, a comprehensive and human-aligned benchmark for humanoid motion tracking, together with HumanScore, a preference-aligned metric that better reflects human judgments. Our goal is to move beyond simple kinematic errors and...

</details>

<details>
<summary><b>6. CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Image Editing</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14546) • [📄 arXiv](https://arxiv.org/abs/2608.14546) • [📥 PDF](https://arxiv.org/pdf/2608.14546)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zqyzzz/CPI-benchmark)

> CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Image Editing

</details>

<details>
<summary><b>7. Claim-Level Reliability Assessment for Efficient Test-Time Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11994) • [📄 arXiv](https://arxiv.org/abs/2608.11994) • [📥 PDF](https://arxiv.org/pdf/2608.11994)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/WeiboAI/CLR)

> We introduce CLR (Claim-Level Reliability Assessment) , a training-free test-time scaling method previously used in VibeThinker-3B . CLR is built on a simple idea that exploits the asymmetry between solving and falsification to improve reasoning r...

</details>

<details>
<summary><b>8. Forecast Collapse in Time-Series Foundation Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14106) • [📄 arXiv](https://arxiv.org/abs/2608.14106) • [📥 PDF](https://arxiv.org/pdf/2608.14106)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We find a surprising failure mode, forecast collapse , of Time Series Foundation Models (TSFMs). Despite their strong performance across general time-series benchmarks, we observe that TSFMs can generate overly smooth or near-constant forecasts th...

</details>

<details>
<summary><b>9. Latent On-Policy Self-Distillation</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13040) • [📄 arXiv](https://arxiv.org/abs/2608.13040) • [📥 PDF](https://arxiv.org/pdf/2608.13040)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bingreeky/LOPD)

> Github: https://github.com/bingreeky/LOPD Enabling agents to learn from experience and internalize it into their policy has become a central problem in self-evolving AI. On-policy self-distillation (OPSD) offers an effective pathway by using a pri...

</details>

<details>
<summary><b>10. Marionette: Predicting World States, Rendering Geometry, Painting Appearance</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kaipeng Zhang, Qiang Li, Chuanhao Li, Zhen Li, Zian Meng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14530) • [📄 arXiv](https://arxiv.org/abs/2608.14530) • [📥 PDF](https://arxiv.org/pdf/2608.14530)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> https://youtu.be/bLLtwXVcqEc

</details>

<details>
<summary><b>11. Second Thought: Reasoning in Parallel as LLM Agents Act and Observe</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13667) • [📄 arXiv](https://arxiv.org/abs/2608.13667) • [📥 PDF](https://arxiv.org/pdf/2608.13667)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A new idle window for test-time scaling 😃

</details>

<details>
<summary><b>12. PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuxuan Tian, Jifan Zhao, Ruike Chen, Yanqing Shen, Yuyang Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14284) • [📄 arXiv](https://arxiv.org/abs/2608.14284) • [📥 PDF](https://arxiv.org/pdf/2608.14284)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> An easy-to-use toolkit for fine-grained robot process assessment, with progress-aware metrics, progress judge benchmarking, and visualization tools.

</details>

<details>
<summary><b>13. Scaling Domain Data Repetition in LLM Pretraining</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14071) • [📄 arXiv](https://arxiv.org/abs/2608.14071) • [📥 PDF](https://arxiv.org/pdf/2608.14071)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Multimodal Model Diffing for Feature Discovery and Control</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09928) • [📄 arXiv](https://arxiv.org/abs/2608.09928) • [📥 PDF](https://arxiv.org/pdf/2608.09928)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hunarbatra/MMDiff)

> We introduce MMDiff, a multimodal model-diffing pipeline to discover task-specific features in MLLMs and enable targeted feature-level control. 🌟 MMDiff diffs a base-LM SAE against a multimodal SAE to isolate vision-adapted features, making it eas...

</details>

<details>
<summary><b>15. Verifier-Induced Support Reshaping in On-Policy Optimization</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.00220) • [📄 arXiv](https://arxiv.org/abs/2608.00220) • [📥 PDF](https://arxiv.org/pdf/2608.00220)

**💻 Code:** [⭐ Code](https://github.com/sylvain-wei/verifier-induced-support-reshaping) • [⭐ Code](https://github.com/huggingface)

> What happens when on-policy RLVR improves the objective in front of it, but makes successful behavior for the next objective harder to sample? In this paper, we study this effect across mathematical reasoning and constrained instruction following....

</details>

<details>
<summary><b>16. Dion3: Full-Stack Orthogonal Updates</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11612) • [📄 arXiv](https://arxiv.org/abs/2608.11612) • [📥 PDF](https://arxiv.org/pdf/2608.11612)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/microsoft/dion)

> Dion3 is a full stack optimization of muon-like updates yielding up to an observed factor of 6 reduction in optimizer time and an extra centinat of performance with code available at https://github.com/microsoft/dion . The time improvements includ...

</details>

<details>
<summary><b>17. SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kewang Deng, Xuanke Shi, Siyi Xie, Jianhua Li, Jinsheng Quan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.14138) • [📄 arXiv](https://arxiv.org/abs/2608.14138) • [📥 PDF](https://arxiv.org/pdf/2608.14138)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>18. Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Inference Overhead via Decoupled Embedding Prediction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12209) • [📄 arXiv](https://arxiv.org/abs/2608.12209) • [📥 PDF](https://arxiv.org/pdf/2608.12209)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 18 |
| 📅 Today | [`2026-08-17.json`](data/daily/2026-08-17.json) | 18 |
| 📆 This Week | [`2026-W33.json`](data/weekly/2026-W33.json) | 18 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 416 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-17 | 18 | [View JSON](data/daily/2026-08-17.json) |
| 📄 2026-08-16 | 32 | [View JSON](data/daily/2026-08-16.json) |
| 📄 2026-08-15 | 32 | [View JSON](data/daily/2026-08-15.json) |
| 📄 2026-08-14 | 19 | [View JSON](data/daily/2026-08-14.json) |
| 📄 2026-08-13 | 18 | [View JSON](data/daily/2026-08-13.json) |
| 📄 2026-08-12 | 19 | [View JSON](data/daily/2026-08-12.json) |
| 📄 2026-08-11 | 17 | [View JSON](data/daily/2026-08-11.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W33 | 18 | [View JSON](data/weekly/2026-W33.json) |
| 📅 2026-W32 | 156 | [View JSON](data/weekly/2026-W32.json) |
| 📅 2026-W31 | 166 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 416 | [View JSON](data/monthly/2026-08.json) |
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
