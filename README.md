<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-20-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7229+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">20</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">82</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">249</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7229+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 10, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Show-Harness: Just a VLM Agent Can Play Robots</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10522) • [📄 arXiv](https://arxiv.org/abs/2609.10522) • [📥 PDF](https://arxiv.org/pdf/2609.10522)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/showlab/Show-Harness)

> Project Page: https://showlab.github.io/Show-Harness/ GitHub: https://github.com/showlab/Show-Harness

</details>

<details>
<summary><b>2. Programmable World Model</b> ⭐ 37</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10540) • [📄 arXiv](https://arxiv.org/abs/2609.10540) • [📥 PDF](https://arxiv.org/pdf/2609.10540)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AlayaLab/pwm)

> No abstract available.

</details>

<details>
<summary><b>3. WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05405) • [📄 arXiv](https://arxiv.org/abs/2609.05405) • [📥 PDF](https://arxiv.org/pdf/2609.05405)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/facebookresearch/WearableQA)

> A benchmark for health reasoning over real-world wearable data. WearableQA comprises 4,084 ten-option multiple-choice questions built from the wearable time series, blood biomarkers, and demographics of 200 real users , each with up to about 500 d...

</details>

<details>
<summary><b>4. SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08149) • [📄 arXiv](https://arxiv.org/abs/2609.08149) • [📥 PDF](https://arxiv.org/pdf/2609.08149)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> SWE-Bench Pro has emerged as a standard benchmark for evaluating software engineering agents on challenging repository-level tasks. However, our analysis work show that its evaluation is undermined by two sources of unreliability: reward hacking, ...

</details>

<details>
<summary><b>5. SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09113) • [📄 arXiv](https://arxiv.org/abs/2609.09113) • [📥 PDF](https://arxiv.org/pdf/2609.09113)

**💻 Code:** [⭐ Code](https://github.com/Trae1ounG/SAEScientist) • [⭐ Code](https://github.com/huggingface)

> Introducing SAEScientist-Bench: Can AI agents conduct autonomous SAE interpretability research? We evaluate 10 agent configurations on 20 tasks covering feature discovery, activation selectivity, and steering. Agents find promising features, but s...

</details>

<details>
<summary><b>6. Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09219) • [📄 arXiv](https://arxiv.org/abs/2609.09219) • [📥 PDF](https://arxiv.org/pdf/2609.09219)

**💻 Code:** [⭐ Code](https://github.com/cxcscmu/Discovery-Certification-Protocol) • [⭐ Code](https://github.com/huggingface)

> The Discovery Certification Protocol turns AI research claims into testable evidence. Validate the gain. Challenge its recovery. Measure the contribution of feedback.

</details>

<details>
<summary><b>7. DianShi-RxnDB: A Large-Scale, Fine-Grained Organic Reaction Data Platform Built via a Fully Automated Pipeline for Researchers and AI Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06703) • [📄 arXiv](https://arxiv.org/abs/2609.06703) • [📥 PDF](https://arxiv.org/pdf/2609.06703)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> High-quality structured organic reaction data are essential for developing artificial intelligence for chemistry (AI4Chem), yet much of this knowledge remains dispersed across patent text, images, and reaction schemes. We present DianShi-RxnDB, a ...

</details>

<details>
<summary><b>8. Revisiting Complete Reasoning Traces for Post-Training</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07103) • [📄 arXiv](https://arxiv.org/abs/2609.07103) • [📥 PDF](https://arxiv.org/pdf/2609.07103)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/naver-ai/revisiting-trace)

> We study whether LLMs indeed benefit from learning complete reasoning traces. Interestingly, full reasoning traces provide only limited benefits, while partial traces remain effective even under heavy truncation. Through attention-based analyses a...

</details>

<details>
<summary><b>9. SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Han Yang, Zeyuan Yang, Furkan Ozyurt, Zhengtao Han, yyuncong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09155) • [📄 arXiv](https://arxiv.org/abs/2609.09155) • [📥 PDF](https://arxiv.org/pdf/2609.09155)

**💻 Code:** [⭐ Code](https://github.com/UMass-Embodied-AGI/SyncWorld) • [⭐ Code](https://github.com/huggingface)

> Can a world model simulate the visual consequences of robot controls in an unseen world, using just a few visual interactions as context? Meet SyncWorld: in-context robot world modeling across unseen cameras, environments & embodiments, with no do...

</details>

<details>
<summary><b>10. Φ-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?</b> ⭐ 54</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10226) • [📄 arXiv](https://arxiv.org/abs/2609.10226) • [📥 PDF](https://arxiv.org/pdf/2609.10226)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/one2piece2hello/faibench_Frontier_InfraBench)

> No abstract available.

</details>

<details>
<summary><b>11. Train Smarter, Not Harder: Switching Signal-Guided Training in Active Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06806) • [📄 arXiv](https://arxiv.org/abs/2609.06806) • [📥 PDF](https://arxiv.org/pdf/2609.06806)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/naghamo/hybridAL)

> HybridAL treats the training strategy in active learning (retrain from scratch each round, or fine-tune from the previous checkpoint) as a decision variable rather than a fixed implementation detail. The structure we found: retraining is most usef...

</details>

<details>
<summary><b>12. Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09134) • [📄 arXiv](https://arxiv.org/abs/2609.09134) • [📥 PDF](https://arxiv.org/pdf/2609.09134)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We study how agent harnesses (system prompts, tool sets, and scaffolding) and model fine-tuning should be combined. Across seven enterprise tasks, harnesses evolved with weaker models are used more effectively by stronger models,  but training wea...

</details>

<details>
<summary><b>13. AgenticGen: Reward-Guided Agentic Video Generation for Advertising</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09187) • [📄 arXiv](https://arxiv.org/abs/2609.09187) • [📥 PDF](https://arxiv.org/pdf/2609.09187)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10355) • [📄 arXiv](https://arxiv.org/abs/2609.10355) • [📥 PDF](https://arxiv.org/pdf/2609.10355)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/momentslab/awesome-efficient-videollm)

> VideoLLMs are expensive because cost scales with frames and context length, and the efficiency literature is scattered across frame sampling, encoders, connectors and the LLM itself, with no shared way to compare methods. We survey 125 papers on i...

</details>

<details>
<summary><b>15. Diffs vs. Whole Files: An Empirical Comparison of Iterative Edit-Based and Direct Generation for Flutter/Dart Code Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** bbidpa

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05779) • [📄 arXiv](https://arxiv.org/abs/2609.05779) • [📥 PDF](https://arxiv.org/pdf/2609.05779)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bbidpa/rainbow-pony)

> Hey all, quick behind-the-scenes on this What I compared: two ways to make a model edit code: regenerate the whole file in one shot; vs. write a sequence of small diffs (search/replace edits), like a human dev would. The models (all trained both w...

</details>

<details>
<summary><b>16. Puppeteer: Object-Grounded Posture-Aware Co-Speech Gesture Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.00369) • [📄 arXiv](https://arxiv.org/abs/2609.00369) • [📥 PDF](https://arxiv.org/pdf/2609.00369)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Generating co-speech gestures that are temporally coherent, semantically aligned with speech, and grounded with surrounding objects remains challenging. Prior speech-driven gesture models emphasize audio-gesture alignment but do not explicitly acc...

</details>

<details>
<summary><b>17. Reference-Based Bias Detection in LLMs via Relative Representations of Hidden States</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10060) • [📄 arXiv](https://arxiv.org/abs/2609.10060) • [📥 PDF](https://arxiv.org/pdf/2609.10060)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>18. RESCUE-BENCH: Towards Relation-Aware Multi-Party Emotional Support Conversation Systems</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09657) • [📄 arXiv](https://arxiv.org/abs/2609.09657) • [📥 PDF](https://arxiv.org/pdf/2609.09657)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tomsawyerhu/RESCUE-bench)

> This paper introduces RESCUE-BENCH , a benchmark for studying relation-aware emotional support in multi-party conversations , an aspect largely overlooked by existing emotional support systems. The authors construct RESCUE from real couple and fam...

</details>

<details>
<summary><b>19. Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning Coverage in RLVR</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hwanjo Yu, Sanghwan Jang, colin31472

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08650) • [📄 arXiv](https://arxiv.org/abs/2609.08650) • [📥 PDF](https://arxiv.org/pdf/2609.08650)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/colin31472/DATPO)

> Reinforcement Learning with Verifiable Rewards (RLVR) has been central to the recent success of Large Reasoning Models. However, while RLVR significantly improves single-sample accuracy, it often fails to expand the model's intrinsic reasoning cov...

</details>

<details>
<summary><b>20. DF26: We Cannot Tell Fake From Real Anymore</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jan Cech, Dmytro Mishkin, Ivan Samarskyi, Severyn Shykula, yermandy

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07369) • [📄 arXiv](https://arxiv.org/abs/2609.07369) • [📥 PDF](https://arxiv.org/pdf/2609.07369)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Let's generalize to fully synthetic data!

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 20 |
| 📅 Today | [`2026-09-10.json`](data/daily/2026-09-10.json) | 20 |
| 📆 This Week | [`2026-W36.json`](data/weekly/2026-W36.json) | 82 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 249 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-10 | 20 | [View JSON](data/daily/2026-09-10.json) |
| 📄 2026-09-09 | 37 | [View JSON](data/daily/2026-09-09.json) |
| 📄 2026-09-08 | 6 | [View JSON](data/daily/2026-09-08.json) |
| 📄 2026-09-07 | 19 | [View JSON](data/daily/2026-09-07.json) |
| 📄 2026-09-06 | 31 | [View JSON](data/daily/2026-09-06.json) |
| 📄 2026-09-05 | 31 | [View JSON](data/daily/2026-09-05.json) |
| 📄 2026-09-04 | 23 | [View JSON](data/daily/2026-09-04.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W36 | 82 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 249 | [View JSON](data/monthly/2026-09.json) |
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
