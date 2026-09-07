<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-19-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7166+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">19</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">186</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7166+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 07, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Iris: Climbing to the Search Frontier</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04304) • [📄 arXiv](https://arxiv.org/abs/2609.04304) • [📥 PDF](https://arxiv.org/pdf/2609.04304)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AllSpark-Research/Iris)

> We present Iris-mini and Iris-pro, two search agents trained at the 35B-A3B and 397B-A17B scales, together with the data pipeline and training recipe behind them. Tasks are reverse-constructed from the hyperlink structure of a web corpus: we autho...

</details>

<details>
<summary><b>2. Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04250) • [📄 arXiv](https://arxiv.org/abs/2609.04250) • [📥 PDF](https://arxiv.org/pdf/2609.04250)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/step-out/Motion-Omni)

> Motion-Omni replaces the speech-then-motion cascade with one end-to-end model that natively generates dialogue speech together with explicit facial expression, hand, upper-body, and lower-body motion, all from the hidden states that produce the sp...

</details>

<details>
<summary><b>3. Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Weilin Luo, Meng Fang, Yuxuan Huang, Yuxiang Chen, Yihang Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02750) • [📄 arXiv](https://arxiv.org/abs/2609.02750) • [📥 PDF](https://arxiv.org/pdf/2609.02750)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YihangChen9/Bilevel-Coordinated-Reflection)

> This paper gives a theoretical account of orchestrator-worker LLM systems by modeling them as a bilevel coordination game, showing that the workers' local-update game is an approximate potential game whose equilibrium slack depends on how well the...

</details>

<details>
<summary><b>4. WorldSculpt: Generating Compositional Worlds from Grounded Videos</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yonghao Yu, Lian Fu, Ruihan Yu, Jixuan He, Muyao Niu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05416) • [📄 arXiv](https://arxiv.org/abs/2609.05416) • [📥 PDF](https://arxiv.org/pdf/2609.05416)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AlayaLab/WorldSculpt)

> No abstract available.

</details>

<details>
<summary><b>5. Enoki: Efficient Multi-Level Hallucination Detection</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.00581) • [📄 arXiv](https://arxiv.org/abs/2609.00581) • [📥 PDF](https://arxiv.org/pdf/2609.00581)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/s-nlp/Enoki)

> Excited to share Enoki — a framework for efficient, fine-grained hallucination detection. The key idea is simple: use text-anchored relational facts as a shared representation for both claim-level verification and span-level localization. This avo...

</details>

<details>
<summary><b>6. Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive Optimization</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05258) • [📄 arXiv](https://arxiv.org/abs/2609.05258) • [📥 PDF](https://arxiv.org/pdf/2609.05258)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIOR-Research/InterOpt)

> We introduce InterOpt, an open framework for improving the interaction between large language models and optimization solvers. While LLMs have shown promising capabilities in mathematical modeling, they often struggle with ambiguous problem descri...

</details>

<details>
<summary><b>7. Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05275) • [📄 arXiv](https://arxiv.org/abs/2609.05275) • [📥 PDF](https://arxiv.org/pdf/2609.05275)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Paper Summary Layer dropout (stochastic depth) has largely vanished from LLM pretraining recipes due to reported accuracy degradation — this paper shows those degradations came from suboptimal configurations, not a fundamental limitation. With the...

</details>

<details>
<summary><b>8. RISE: Recursive Improvement via Self-Extrapolating Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05295) • [📄 arXiv](https://arxiv.org/abs/2609.05295) • [📥 PDF](https://arxiv.org/pdf/2609.05295)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>9. MaxKernel: Agentic Kernel Generation for TPUs</b> ⭐ 61</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04523) • [📄 arXiv](https://arxiv.org/abs/2609.04523) • [📥 PDF](https://arxiv.org/pdf/2609.04523)

**💻 Code:** [⭐ Code](https://github.com/AI-Hypercomputer/accelerator-agents) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. Training-Free Speech-Centric Omni Understanding with Frozen VLMs</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04242) • [📄 arXiv](https://arxiv.org/abs/2609.04242) • [📥 PDF](https://arxiv.org/pdf/2609.04242)

**💻 Code:** [⭐ Code](https://github.com/mbzuai-oryx/OmniEvalKit) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04753) • [📄 arXiv](https://arxiv.org/abs/2609.04753) • [📥 PDF](https://arxiv.org/pdf/2609.04753)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/naver-ai/beneath-cot)

> Reasoning is no longer just an emergent behavior of LLMs; it is increasingly becoming a training objective. Yet we still know little about how reasoning is represented and organized inside the model. Beneath the Surface of Chains-of-Thought addres...

</details>

<details>
<summary><b>12. When Models Edit Too Much: On the Fidelity of Minimal Code Edits</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04061) • [📄 arXiv](https://arxiv.org/abs/2609.04061) • [📥 PDF](https://arxiv.org/pdf/2609.04061)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/nreHieW/over-editing)

> Code: https://github.com/nreHieW/over-editing

</details>

<details>
<summary><b>13. Group Adaptive Clipping Policy Optimization</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.00444) • [📄 arXiv](https://arxiv.org/abs/2609.00444) • [📥 PDF](https://arxiv.org/pdf/2609.00444)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Sheng-J/GAPO)

> Group-relative policy optimization methods for reinforcement learning with verifiable rewards (RLVR) typically use a fixed importance-sampling (IS) ratio clipping boundary across all rollouts. We identify a key limitation of this design: rare corr...

</details>

<details>
<summary><b>14. The Attention Triangle in Audio-Video Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.03586) • [📄 arXiv](https://arxiv.org/abs/2609.03586) • [📥 PDF](https://arxiv.org/pdf/2609.03586)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SagiPolaczek/The-Attention-Triangle)

> Audio-video diffusion models rely on cross-modal attention to coordinate text, sound, and visual content, yet this same mechanism can introduce subtle and systematic semantic leakage. We study these models by probing and analyzing the ``attention ...

</details>

<details>
<summary><b>15. To See a World in a Living Context: Unified Indoor-Outdoor Urban World Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yiping Chen, Hongchao Fan, Yang Luo, Zilong Huang, Xiaobin Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05879) • [📄 arXiv](https://arxiv.org/abs/2608.05879) • [📥 PDF](https://arxiv.org/pdf/2608.05879)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share HoloWorld, a unified framework for indoor-outdoor 3D urban world generation. HoloWorld maintains a continuously updated cross-scale world context, enabling coherent generation from city-scale planning to individual building interi...

</details>

<details>
<summary><b>16. τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04611) • [📄 arXiv](https://arxiv.org/abs/2609.04611) • [📥 PDF](https://arxiv.org/pdf/2609.04611)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sierra-research/hyper-tau-bench)

> hyper-tau-bench

</details>

<details>
<summary><b>17. When Quantization Breaks Memory: Recurrent-State Write-Back in Low-Precision Temporal Inference</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vikas Pandey, Xavier Intes, Ismail Erbas

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04490) • [📄 arXiv](https://arxiv.org/abs/2609.04490) • [📥 PDF](https://arxiv.org/pdf/2609.04490)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We show that quantization doesn't just make individual numbers less precise in recurrent networks; it can quietly break the network's memory itself. In GRUs and LSTMs, the internal state gets saved after every time step and fed back in for the nex...

</details>

<details>
<summary><b>18. ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jun Yu, Qiang Huang, Ke Yang, Jitai Hao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02780) • [📄 arXiv](https://arxiv.org/abs/2609.02780) • [📥 PDF](https://arxiv.org/pdf/2609.02780)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/CURRENTF/ShallowStream)

> Streaming video understanding is a critical capability for real-world applications, including embodied intelligence, autonomous driving, industrial monitoring, surveillance and early warning, and wearable assistants. However, processing continuous...

</details>

<details>
<summary><b>19. AdaptVPR: Route-Aware Hard Positive Generation for Robust Visual Place Recognition</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yukun Song, Shengpeng Xu, Changwei Wang, Jingyi Zhang, shunpeng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04369) • [📄 arXiv](https://arxiv.org/abs/2609.04369) • [📥 PDF](https://arxiv.org/pdf/2609.04369)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/chenshunpeng/AdaptVPR)

> We’re excited to share AdaptVPR , a route-aware generative augmentation framework for improving Visual Place Recognition under challenging appearance shifts. AdaptVPR generates same-place hard positives through three scene-dependent routes: Global...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 19 |
| 📅 Today | [`2026-09-07.json`](data/daily/2026-09-07.json) | 19 |
| 📆 This Week | [`2026-W36.json`](data/weekly/2026-W36.json) | 19 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 186 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-07 | 19 | [View JSON](data/daily/2026-09-07.json) |
| 📄 2026-09-06 | 31 | [View JSON](data/daily/2026-09-06.json) |
| 📄 2026-09-05 | 31 | [View JSON](data/daily/2026-09-05.json) |
| 📄 2026-09-04 | 23 | [View JSON](data/daily/2026-09-04.json) |
| 📄 2026-09-03 | 28 | [View JSON](data/daily/2026-09-03.json) |
| 📄 2026-09-02 | 21 | [View JSON](data/daily/2026-09-02.json) |
| 📄 2026-09-01 | 33 | [View JSON](data/daily/2026-09-01.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W36 | 19 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 186 | [View JSON](data/monthly/2026-09.json) |
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
