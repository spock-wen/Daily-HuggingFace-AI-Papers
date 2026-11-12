<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-18-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9772+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">101</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">371</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9772+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 12, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Scaling Mathematical Proof Supervision from Structured Textbooks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40394) • [📄 arXiv](https://arxiv.org/abs/2610.40394) • [📥 PDF](https://arxiv.org/pdf/2610.40394)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing TOME-Math , a large-scale mathematical proof supervision corpus built from 2,118 university-level textbooks , containing 380K structured QA records . Unlike conventional math datasets that flatten knowledge into isolated question-answe...

</details>

<details>
<summary><b>2. SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yunxin Liu, Xin Ding, Zixu Hao, Xiangyu Li, Genming Cui

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13410) • [📄 arXiv](https://arxiv.org/abs/2611.13410) • [📥 PDF](https://arxiv.org/pdf/2611.13410)

**💻 Code:** [⭐ Code](https://github.com/air-embodied-brain/SteerDistill) • [⭐ Code](https://github.com/huggingface)

> SteerDistill: sub-4-bit LLM agents. A quantized agent can miss a task requirement and fail the whole task. SteerDistill trains it to avoid these mistakes through closed-loop teacher steering . A frozen BF16 teacher guides student retries and refin...

</details>

<details>
<summary><b>3. Incentivizing Self-Learning in Large Language Models via Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39671) • [📄 arXiv](https://arxiv.org/abs/2610.39671) • [📥 PDF](https://arxiv.org/pdf/2610.39671)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We study self-learning—autonomously retrieving, studying, and applying knowledge from long-form reference materials on the fly.

</details>

<details>
<summary><b>4. Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.22237) • [📄 arXiv](https://arxiv.org/abs/2608.22237) • [📥 PDF](https://arxiv.org/pdf/2608.22237)

**💻 Code:** [⭐ Code](https://github.com/Zedong-Liu/SparseReading) • [⭐ Code](https://github.com/huggingface)

> Hi, we’re the authors of SparseRead! We built it for a problem you might recognize: you ask an agent to explain one error, and it reads the entire log. SparseRead lets the agent preview a file, read the relevant sections with source locations, and...

</details>

<details>
<summary><b>5. Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Matteo Mordacchini, Patrizio Dazzi, Emanuele Carlini, SaulUrso

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10193) • [📄 arXiv](https://arxiv.org/abs/2611.10193) • [📥 PDF](https://arxiv.org/pdf/2611.10193)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most LLM routing approaches select a single model per prompt, while ensembling introduces a different question: which models should we combine, and how many are actually worth invoking? In this paper, we introduce PISA, a cost-aware single-model r...

</details>

<details>
<summary><b>6. GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13028) • [📄 arXiv](https://arxiv.org/abs/2611.13028) • [📥 PDF](https://arxiv.org/pdf/2611.13028)

**💻 Code:** [⭐ Code](https://github.com/ljbro/GTAGym) • [⭐ Code](https://github.com/huggingface)

> Code: https://github.com/ljbro/GTAGym Data: https://huggingface.co/datasets/OpenMOSS-Team/GTAVBench

</details>

<details>
<summary><b>7. Evolving Infra: Agent-Adaptive LLM Serving at Scale</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12304) • [📄 arXiv](https://arxiv.org/abs/2611.12304) • [📥 PDF](https://arxiv.org/pdf/2611.12304)

**💻 Code:** [⭐ Code](https://github.com/mit-han-lab/EvolvingInfra) • [⭐ Code](https://github.com/huggingface)

> Agentic workloads are a major source of LLM inference demand. Existing prefill--decode (PD) disaggregated serving systems offer limited flexibility for runtime adaptation of compute allocation and KV cache management, and rely on coarse signals th...

</details>

<details>
<summary><b>8. Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12869) • [📄 arXiv](https://arxiv.org/abs/2611.12869) • [📥 PDF](https://arxiv.org/pdf/2611.12869)

**💻 Code:** [⭐ Code](https://github.com/ExplainableML/prh-closer-look) • [⭐ Code](https://github.com/huggingface)

> Where does alignment emerge? In later layers (not the final ones) and within a small subspace of ~100 dimensions. Does the capability-alignment trend still hold? It does, but it depends on the data: with clean, informative captions, stronger langu...

</details>

<details>
<summary><b>9. Mixed Signals: Weight-Space Programming for EEG and ECG</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13758) • [📄 arXiv](https://arxiv.org/abs/2611.13758) • [📥 PDF](https://arxiv.org/pdf/2611.13758)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can a language model train a neural network just by reasoning about its weights, with no gradient descent? We tested this on small EEG and ECG networks: Starting from an empty EEG network, Opus wrote every weight and matched gradient-descent train...

</details>

<details>
<summary><b>10. Module-Aware Optimization for Graph Neural Networks</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Bracha Shapira, Moshe Eliasof, Haggai Roitman, Guy Hadad

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08379) • [📄 arXiv](https://arxiv.org/abs/2611.08379) • [📥 PDF](https://arxiv.org/pdf/2611.08379)

**💻 Code:** [⭐ Code](https://github.com/guy-hadad/GraphMuon) • [⭐ Code](https://github.com/huggingface)

> Different optimizers impose different geometries on parameter updates. Adaptive methods such as Adam and AdamW use coordinate-wise updates, while matrix-aware optimizers such as Muon utilize weight-matrix structure through orthogonalized updates. ...

</details>

<details>
<summary><b>11. CogBattery: Human-Referenced Evaluation of Cognitive Task Behavior and Structure in Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kazunori D Yamada, Fangzhou Lin, Lingyu Jiang, dengzhe-hou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24999) • [📄 arXiv](https://arxiv.org/abs/2607.24999) • [📥 PDF](https://arxiv.org/pdf/2607.24999)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dengzhe-hou/CogBattery)

> CogBattery compares 54 open-weight language models with human data on text adaptations of 13 cognitive paradigms. Matching the direction of a human effect does not mean matching human errors or confidence calibration. Leaderboard and community sub...

</details>

<details>
<summary><b>12. WMIP: A Working-Memory-Inspired Programmable Probe of Cumulative State Tracking in Large Language Models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Fangzhou Lin, Zirui Li, Deng Li, Lingyu Jiang, dengzhe-hou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.27343) • [📄 arXiv](https://arxiv.org/abs/2603.27343) • [📥 PDF](https://arxiv.org/pdf/2603.27343)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dengzhe-hou/WMIP)

> We introduce WMIP, a programmable probe of cumulative state tracking in LLMs. Across 18 LLMs, single-step arithmetic reaches 84.9%, but core items with three to seven updates drop to 31.7%, and from 50 updates on no model exceeds 10%. With instruc...

</details>

<details>
<summary><b>13. Precision on Demand: Escalating Weight Bits at Uncertain Decoding Steps in a Small Local Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Aliyas Ahmad Misri, Logesh L, Mohammed Nayeem Khan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14418) • [📄 arXiv](https://arxiv.org/abs/2611.14418) • [📥 PDF](https://arxiv.org/pdf/2611.14418)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Precision on Demand: Escalating Weight Bits at Uncertain Decoding Steps in a Small Local Model

</details>

<details>
<summary><b>14. Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Jieyu Zhang, Kanchana Ranasinghe, Kai Li, Zixian Ma, Chenhao Zheng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08286) • [📄 arXiv](https://arxiv.org/abs/2611.08286) • [📥 PDF](https://arxiv.org/pdf/2611.08286)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SalesforceAIResearch/Interactive-Visual-Gym)

> We introduce Interactive Visual Gym, a framework for evaluating and training visual interaction models in closed loop with simulated human users. IVG-Bench covers 315 interaction scenarios across cooking, household manipulation, and mobile interfa...

</details>

<details>
<summary><b>15. FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13766) • [📄 arXiv](https://arxiv.org/abs/2611.13766) • [📥 PDF](https://arxiv.org/pdf/2611.13766)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/santoshrajkumar/fame-qp)

> PyPI: https://pypi.org/project/fame-qp/

</details>

<details>
<summary><b>16. CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yueqi Zhang, Zhouheng Yao, Honghui Yang, Zhanwei Zhang, dayll

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05862) • [📄 arXiv](https://arxiv.org/abs/2611.05862) • [📥 PDF](https://arxiv.org/pdf/2611.05862)

**💻 Code:** [⭐ Code](https://github.com/Da1yuqin/CARTBench) • [⭐ Code](https://github.com/huggingface)

> We introduce CARTBench, a benchmark for evaluating shopping advice for Complex and Ambiguous Requests with Timelines. It contains 169 timestamped shopping cases across 17 retail domains, with 1,603 product records and 1,328 case-specific rubric cr...

</details>

<details>
<summary><b>17. Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Aliyas Ahmad Misri, Logesh L, Mohammed Nayeem Khan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14413) • [📄 arXiv](https://arxiv.org/abs/2611.14413) • [📥 PDF](https://arxiv.org/pdf/2611.14413)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models

</details>

<details>
<summary><b>18. PolyRoute: A Twelve-Language and Code-Mixed Benchmark for Typed-Decision Routing, with Baselines and a Leaderboard</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sarun Kumar K S, Mohammed Nayeem Khan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13843) • [📄 arXiv](https://arxiv.org/abs/2611.13843) • [📥 PDF](https://arxiv.org/pdf/2611.13843)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> PolyRoute: A Twelve-Language and Code-Mixed Benchmark for Typed-Decision Routing, with Baselines and a Leaderboard

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 18 |
| 📅 Today | [`2026-11-12.json`](data/daily/2026-11-12.json) | 18 |
| 📆 This Week | [`2026-W45.json`](data/weekly/2026-W45.json) | 101 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 371 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-12 | 18 | [View JSON](data/daily/2026-11-12.json) |
| 📄 2026-11-11 | 29 | [View JSON](data/daily/2026-11-11.json) |
| 📄 2026-11-10 | 26 | [View JSON](data/daily/2026-11-10.json) |
| 📄 2026-11-09 | 28 | [View JSON](data/daily/2026-11-09.json) |
| 📄 2026-11-08 | 32 | [View JSON](data/daily/2026-11-08.json) |
| 📄 2026-11-07 | 32 | [View JSON](data/daily/2026-11-07.json) |
| 📄 2026-11-06 | 24 | [View JSON](data/daily/2026-11-06.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W45 | 101 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 371 | [View JSON](data/monthly/2026-11.json) |
| 🗓️ 2026-10 | 1640 | [View JSON](data/monthly/2026-10.json) |
| 🗓️ 2026-09 | 781 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |

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
