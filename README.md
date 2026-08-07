<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-17-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6453+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">17</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">106</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">182</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6453+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 07, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05987) • [📄 arXiv](https://arxiv.org/abs/2608.05987) • [📥 PDF](https://arxiv.org/pdf/2608.05987)

**💻 Code:** [⭐ Code](https://github.com/ZethWang/AgentOPSD) • [⭐ Code](https://github.com/huggingface)

> We therefore propose AgentOPSD, a critic-free recursive turn-level credit assignment for agentic reinforcement learning. AgentOPSD aggregates token-level teacher-student log-probability gaps into turn-level evidence, recursively updates a Bayesian...

</details>

<details>
<summary><b>2. WorldClaw: Agentic 3D Open-World Generation at Scale</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05248) • [📄 arXiv](https://arxiv.org/abs/2608.05248) • [📥 PDF](https://arxiv.org/pdf/2608.05248)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>3. Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06060) • [📄 arXiv](https://arxiv.org/abs/2608.06060) • [📥 PDF](https://arxiv.org/pdf/2608.06060)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/deepglint/UniME-R1)

> Unified multimodal retrieval aims to identify candidates that satisfy complex user intent expressed through heterogeneous inputs.  Although Large Vision-Language Model (LVLM)-based retrievers are efficient and scalable, directly encoding raw multi...

</details>

<details>
<summary><b>4. EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06197) • [📄 arXiv](https://arxiv.org/abs/2608.06197) • [📥 PDF](https://arxiv.org/pdf/2608.06197)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Within-yao/EnvACE)

> Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to groun...

</details>

<details>
<summary><b>5. ChronoVision: Temporal Reasoning via Latent State Reconstruction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05631) • [📄 arXiv](https://arxiv.org/abs/2608.05631) • [📥 PDF](https://arxiv.org/pdf/2608.05631)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multimodal large language models excel at passive perception but struggle with complex visual cognitive tasks requiring multi-step temporal reasoning. This degradation largely stems from the inherent ambiguity of language-based reasoning, which of...

</details>

<details>
<summary><b>6. OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.28609) • [📄 arXiv](https://arxiv.org/abs/2607.28609) • [📥 PDF](https://arxiv.org/pdf/2607.28609)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OS-Copilot/OSReward)

> A CUA trajectory is the interleaved record of an agent's screens, actions, and reasoning. Deciding whether it fulfilled the instruction is the reward signal behind evaluation, data curation and RL. How well the models we now use as judges actually...

</details>

<details>
<summary><b>7. On-Policy Delta Distillation for Multilingual Math Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05802) • [📄 arXiv](https://arxiv.org/abs/2608.05802) • [📥 PDF](https://arxiv.org/pdf/2608.05802)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Extending On-Policy Delta Distillation (OPD²) to multilingual reasoning

</details>

<details>
<summary><b>8. HarnessOpt-Bench: Evaluating LLMs at Harness Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06301) • [📄 arXiv](https://arxiv.org/abs/2608.06301) • [📥 PDF](https://arxiv.org/pdf/2608.06301)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This is an interesting direction for evaluating how well LLMs can actually improve agent systems, not just solve individual tasks. The focus on held-out evaluation and stochastic, budgeted optimization makes the benchmark especially useful for mea...

</details>

<details>
<summary><b>9. GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05747) • [📄 arXiv](https://arxiv.org/abs/2608.05747) • [📥 PDF](https://arxiv.org/pdf/2608.05747)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Pingyue Sheng, Yangyang Zheng, Zhide Zhong, Junjie He, Junfeng Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06374) • [📄 arXiv](https://arxiv.org/abs/2608.06374) • [📥 PDF](https://arxiv.org/pdf/2608.06374)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Yalun Dai, Zhengyang Yan, Zhengshen Zhang, Haosong Peng, Yuhao Pan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05369) • [📄 arXiv](https://arxiv.org/abs/2608.05369) • [📥 PDF](https://arxiv.org/pdf/2608.05369)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yyyyu120/W2-VLA)

> 🚀 We’re excited to release W²-VLA! 🎉 Task-conditioned future wrist modeling for fine-grained robot manipulation. 🌍 Global task context guides the prediction of task-relevant future wrist latents. 🧠 W²-CoT provides structured supervision to help sh...

</details>

<details>
<summary><b>12. CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06352) • [📄 arXiv](https://arxiv.org/abs/2608.06352) • [📥 PDF](https://arxiv.org/pdf/2608.06352)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AweAI-Team/CalibForge)

> A very interesting take on agent data synthesis: instead of just generating and validating executable tasks, CalibForge uses solver behavior to actively reshape tasks into a solver-relative “ learnable zone .” The idea of calibrating task difficul...

</details>

<details>
<summary><b>13. SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hehe Fan, Xiaoxiao Sun, Yunqiu Xu, Yingzhao Jian, Yue Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05137) • [📄 arXiv](https://arxiv.org/abs/2608.05137) • [📥 PDF](https://arxiv.org/pdf/2608.05137)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project page: https://yuecheong.github.io/SmartMage/

</details>

<details>
<summary><b>14. PaDoc: Layout-Grounded Parallel Decoding for Document Parsing</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06146) • [📄 arXiv](https://arxiv.org/abs/2608.06146) • [📥 PDF](https://arxiv.org/pdf/2608.06146)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Longin-Yu/Padoc)

> End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content,...

</details>

<details>
<summary><b>15. ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Context Routing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.04956) • [📄 arXiv](https://arxiv.org/abs/2608.04956) • [📥 PDF](https://arxiv.org/pdf/2608.04956)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ContextMaster enables real-time interactive multi-shot video creation by unifying generation, reference conditioning, and editing with fixed-budget sparse context routing.

</details>

<details>
<summary><b>16. EffectLearner: World-Aware Object-Effect Reasoning for Real-World Video Object Removal</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Si Chen, Zilang Zhou, Xu He, Wanke Xia, Feier Wu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05565) • [📄 arXiv](https://arxiv.org/abs/2608.05565) • [📥 PDF](https://arxiv.org/pdf/2608.05565)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> EffectLearner enables robust real-world video object removal by jointly removing target objects and their associated effects, including shadows, reflections, lighting changes, and other complex physical interactions.

</details>

<details>
<summary><b>17. Invisible Shortcuts: Why Vision Encoders Know Your Camera</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Giorgos Tolias, Noa Garcia, Giorgos Kordopatis-Zilos, Ryan Ramos, Vladan Stojnić

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.05424) • [📄 arXiv](https://arxiv.org/abs/2608.05424) • [📥 PDF](https://arxiv.org/pdf/2608.05424)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Deep vision models exploit shortcuts, relying on cues that correlate with supervision signals. Prior work has focused on visible biases, such as object-background or texture correlations. We identify a different source of shortcut learning: invisi...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 17 |
| 📅 Today | [`2026-08-07.json`](data/daily/2026-08-07.json) | 17 |
| 📆 This Week | [`2026-W31.json`](data/weekly/2026-W31.json) | 106 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 182 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-07 | 17 | [View JSON](data/daily/2026-08-07.json) |
| 📄 2026-08-06 | 23 | [View JSON](data/daily/2026-08-06.json) |
| 📄 2026-08-05 | 24 | [View JSON](data/daily/2026-08-05.json) |
| 📄 2026-08-04 | 22 | [View JSON](data/daily/2026-08-04.json) |
| 📄 2026-08-03 | 20 | [View JSON](data/daily/2026-08-03.json) |
| 📄 2026-08-02 | 38 | [View JSON](data/daily/2026-08-02.json) |
| 📄 2026-08-01 | 38 | [View JSON](data/daily/2026-08-01.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W31 | 106 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 182 | [View JSON](data/monthly/2026-08.json) |
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
