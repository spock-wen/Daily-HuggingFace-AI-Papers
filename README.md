<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-20-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6367+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">20</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">96</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6367+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 03, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement</b> ⭐ 138</summary>

<br/>

**👥 Authors:** Huazheng Wang, Jing Shi, Qinsi Wang, Benjamin-eecs, timecuriosity

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23802) • [📄 arXiv](https://arxiv.org/abs/2607.23802) • [📥 PDF](https://arxiv.org/pdf/2607.23802)

**💻 Code:** [⭐ Code](https://github.com/wangqinsi1/RLSVR) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wangqinsi1/RLSVR/tree/SpyRL)

> [COLM 2026] From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement

</details>

<details>
<summary><b>2. N_0-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens</b> ⭐ 31</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23782) • [📄 arXiv](https://arxiv.org/abs/2607.23782) • [📥 PDF](https://arxiv.org/pdf/2607.23782)

**💻 Code:** [⭐ Code](https://github.com/neoteai/N0-VTLA) • [⭐ Code](https://github.com/huggingface)

> Hi all, author here 👋 We're excited to share N0-VTLA, a vision–tactile–language–action (VTLA) foundation model built for two things current VLA backbones struggle with: fine-grained contact-rich manipulation with real tactile feedback control, and...

</details>

<details>
<summary><b>3. Meshy T2: Fast Native Mesh Generation with Flow Matching</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zangyueyang Xian, Siyuan Shen, Yuhao Long, Rendong Liang, bluestyle97

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28675) • [📄 arXiv](https://arxiv.org/abs/2607.28675) • [📥 PDF](https://arxiv.org/pdf/2607.28675)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>4. AISPA: User-Centric System Prompt Auditing for Large Language Model Applications</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28617) • [📄 arXiv](https://arxiv.org/abs/2607.28617) • [📥 PDF](https://arxiv.org/pdf/2607.28617)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SystemPromptIndex/SystemPromptIndex)

> YOUR AGENT HAS A HIDDENT AGENDA! Introducing SystemPromptIndex SystemPromptIndex is the first and largest system prompt index, created to advance transparency and accountability in AI system prompts. It also introduces AISPA ( Artificial Intellige...

</details>

<details>
<summary><b>5. QQWorld: Quantile-Quantile Matching for World Model Regularization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiangyu Xu, Xiaoyu Hu, Zhoushun Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28415) • [📄 arXiv](https://arxiv.org/abs/2607.28415) • [📥 PDF](https://arxiv.org/pdf/2607.28415)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> QQWorld improves latent world models with a quantile-quantile matching objective that aligns projected latent samples with rank-matched Gaussian quantiles, boosting planning success.

</details>

<details>
<summary><b>6. Scaling Properties of Text Conditioning in Visual Generation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Haoqi Fan, Hongyi Yuan, Chaorui Deng, Andy1621, heheyas

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.29679) • [📄 arXiv](https://arxiv.org/abs/2607.29679) • [📥 PDF](https://arxiv.org/pdf/2607.29679)

**💻 Code:** [⭐ Code](https://github.com/heheyas/context-scaling) • [⭐ Code](https://github.com/huggingface)

> We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the...

</details>

<details>
<summary><b>7. N_0-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation</b> ⭐ 48</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23783) • [📄 arXiv](https://arxiv.org/abs/2607.23783) • [📥 PDF](https://arxiv.org/pdf/2607.23783)

**💻 Code:** [⭐ Code](https://github.com/neoteai/N0-TWAM) • [⭐ Code](https://github.com/huggingface)

> Hi everyone — author here! 👋 Excited to share N₀-TWAM, a tactile-native world-action model for contact-rich manipulation. Code and pretrained checkpoints are already out: Code: https://github.com/neoteai/N0-TWAM Project page: https://research.neot...

</details>

<details>
<summary><b>8. Fewer Clarifications, Better Code: Benchmarking Cross-Session Personalized Ambiguity Adaptation in Coding Assistants</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.26611) • [📄 arXiv](https://arxiv.org/abs/2607.26611) • [📥 PDF](https://arxiv.org/pdf/2607.26611)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce CAPA, which characterizes personalized coding ambiguity through six mechanisms and injects these mechanisms into unambiguous executable tasks using a controlled three-stage generation pipeline. CAPA contains 600 coding sessions across...

</details>

<details>
<summary><b>9. Enhancing Rubric-based RL via Self-Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shenzhi Yang, Shuai Zhu, Chao Ye, Yuhang Yang, Mingxuan Xia

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.18082) • [📄 arXiv](https://arxiv.org/abs/2607.18082) • [📥 PDF](https://arxiv.org/pdf/2607.18082)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce CriPO ( Criterion-Distilled Policy Optimization ), a simple on-policy framework that improves rubric-based reinforcement learning for open-ended LLM post-training. We identify two overlooked failure modes— Unexplored Criteria and Supp...

</details>

<details>
<summary><b>10. ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Simon Suo, Zhaoqi Li, Eli Stewart, Adrian Lyjak, Boyang Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.29677) • [📄 arXiv](https://arxiv.org/abs/2607.29677) • [📥 PDF](https://arxiv.org/pdf/2607.29677)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. Evaluation-Verification Reward for Consistent Multi-Reference Image Editing</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Lei Sun, Meng Yu, Xiaochen Lv, Pengfei Zhang, Yingmao Miao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.29025) • [📄 arXiv](https://arxiv.org/abs/2607.29025) • [📥 PDF](https://arxiv.org/pdf/2607.29025)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. Mental World Modeling</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27201) • [📄 arXiv](https://arxiv.org/abs/2607.27201) • [📥 PDF](https://arxiv.org/pdf/2607.27201)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mental-world/Mentis)

> 🧠 Mental World Modeling (Project Page) From simulating physical scenes to simulating the minds that act within them. TL;DR: A world model can reconstruct the physical scene correctly and still predict the wrong human action. Why? Because human dec...

</details>

<details>
<summary><b>13. One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28443) • [📄 arXiv](https://arxiv.org/abs/2607.28443) • [📥 PDF](https://arxiv.org/pdf/2607.28443)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can every robot predict the same future collective state using only local observations and bandwidth-limited neighbor messages? We introduce CS-JEPA, a fully decentralized predictive architecture that transfers across unseen swarm topologies and s...

</details>

<details>
<summary><b>14. Toward Robust and 3D-Aware RGB-NIR Imaging in the Dark</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Zhihang Zhong, Qingtian Zhu, Yifan Zhan, Mingze Ma, Muyao Niu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.29684) • [📄 arXiv](https://arxiv.org/abs/2607.29684) • [📥 PDF](https://arxiv.org/pdf/2607.29684)

**💻 Code:** [⭐ Code](https://github.com/MyNiuuu/3DarkFusion) • [⭐ Code](https://github.com/huggingface)

> 3DarkFusion fuses extremely noisy RGB with Near-Infrared (NIR) in 3D space via neural rendering -- no clean RGB supervision needed, robust even under severe noise interference.

</details>

<details>
<summary><b>15. SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Emmett J. Ientilucci, Ramesh Bhatta, Lalit Joshi, Sagar Lekhak, prasannareddyp

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28996) • [📄 arXiv](https://arxiv.org/abs/2607.28996) • [📥 PDF](https://arxiv.org/pdf/2607.28996)

**💻 Code:** [⭐ Code](https://github.com/PrasannaPulakurthi/SULAND_v2) • [⭐ Code](https://github.com/huggingface)

> We release SULAND_v2, a refined RGB surface-landmine dataset and an IID/OOD object-detection benchmark for UAV/UGV-based mine-action survey support. Public RGB landmine datasets are scarce, so each one disproportionately shapes which methods get t...

</details>

<details>
<summary><b>16. ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Xirui Kang, Yuan Gao, Peng Cheng, Haoyi Niu, Dongxiu Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27924) • [📄 arXiv](https://arxiv.org/abs/2607.27924) • [📥 PDF](https://arxiv.org/pdf/2607.27924)

**💻 Code:** [⭐ Code](https://github.com/Dstate/ODEWorld) • [⭐ Code](https://github.com/huggingface)

> ODEWorld explores continuous-time world modeling by learning a latent ODE velocity field instead of discrete-time transitions. The approach provides elegant properties such as arbitrary temporal resolution and backward prediction, and shows promis...

</details>

<details>
<summary><b>17. Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Models in Commonsense Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Cheng Yang, Yijie Lu, Shijie Zheng, Chenhao Xue, Zheng Wu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28478) • [📄 arXiv](https://arxiv.org/abs/2607.28478) • [📥 PDF](https://arxiv.org/pdf/2607.28478)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> As large language models (LLMs) continue to advance in complex reasoning tasks, they have learned to heavily prioritize explicit conditions provided in the input. However, in everyday commonsense reasoning, this mechanism exposes a critical vulner...

</details>

<details>
<summary><b>18. Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Nenghai Yu, Weiming Zhang, Lingyao Zhu, wpydcr

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27951) • [📄 arXiv](https://arxiv.org/abs/2607.27951) • [📥 PDF](https://arxiv.org/pdf/2607.27951)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper studies LLM safety through a game theoretic lens and develops a safety trilemma involving Useful Capability, Reliable Safety, and Open Access. It rigorously shows that, for dual use tasks where attackers can reproduce the contextual evi...

</details>

<details>
<summary><b>19. SGTP: Sampling-based Game-Theoretic Planning for Real-Time Multi-Vehicle Autonomous Racing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.25388) • [📄 arXiv](https://arxiv.org/abs/2607.25388) • [📥 PDF](https://arxiv.org/pdf/2607.25388)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhouhengli/SGTP-Racer)

> Proposed Sampling-based Game-Theoretic Planning (SGTP) framework for multi-behavior autonomous racing. SGTP combines GPU-accelerated sampling-based planning with game-theoretic best-response reasoning, using a new game-aware cost to favor competit...

</details>

<details>
<summary><b>20. In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous Driving System Testing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15820) • [📄 arXiv](https://arxiv.org/abs/2607.15820) • [📥 PDF](https://arxiv.org/pdf/2607.15820)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This study provides a comprehensive industry-grounded overview of ADS testing, proposes an evidence-centered closed-loop testing framework to provide actionable guidance for ADS testing, and outlines important directions for future research and pr...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 20 |
| 📅 Today | [`2026-08-03.json`](data/daily/2026-08-03.json) | 20 |
| 📆 This Week | [`2026-W31.json`](data/weekly/2026-W31.json) | 20 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 96 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-03 | 20 | [View JSON](data/daily/2026-08-03.json) |
| 📄 2026-08-02 | 38 | [View JSON](data/daily/2026-08-02.json) |
| 📄 2026-08-01 | 38 | [View JSON](data/daily/2026-08-01.json) |
| 📄 2026-07-31 | 31 | [View JSON](data/daily/2026-07-31.json) |
| 📄 2026-07-30 | 14 | [View JSON](data/daily/2026-07-30.json) |
| 📄 2026-07-29 | 15 | [View JSON](data/daily/2026-07-29.json) |
| 📄 2026-07-28 | 24 | [View JSON](data/daily/2026-07-28.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W31 | 20 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 96 | [View JSON](data/monthly/2026-08.json) |
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
