<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-14-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6240+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">14</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">67</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">552</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6240+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 30, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27205) • [📄 arXiv](https://arxiv.org/abs/2607.27205) • [📥 PDF](https://arxiv.org/pdf/2607.27205)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/H-EmbodVis/TurboVLA)

> Vision-language-action (VLA) models commonly adopt an LLM-centric V→L→A pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this desi...

</details>

<details>
<summary><b>2. HumanCLAW: Can Vision-Language Models Act Through a Body?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27180) • [📄 arXiv](https://arxiv.org/abs/2607.27180) • [📥 PDF](https://arxiv.org/pdf/2607.27180)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Human-CLAW/HumanCLAW)

> A model may know where the sofa is, yet still not know how to move its body there and sit down. We call this ability Action Intelligence , and HumanCLAW makes it measurable without tying it to motor control. This is a first step toward models that...

</details>

<details>
<summary><b>3. DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.25675) • [📄 arXiv](https://arxiv.org/abs/2607.25675) • [📥 PDF](https://arxiv.org/pdf/2607.25675)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can an AI system improve not only its answers, but also the criteria it uses to judge those answers? We introduce DecoEvo, a score-decoupled co-evolution framework that jointly evolves a solver and a rubric generator in text space. By extracting s...

</details>

<details>
<summary><b>4. CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yue Wang, Ruina Hu, Jiapeng Li, Chengqi Li, Lai Wei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.25294) • [📄 arXiv](https://arxiv.org/abs/2607.25294) • [📥 PDF](https://arxiv.org/pdf/2607.25294)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/IamLihua/CLBench-V)

> Excited to share CLBench-V , a new benchmark evaluating whether multimodal models can truly learn from context—from grounding evidence to acquiring new knowledge.

</details>

<details>
<summary><b>5. CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.25659) • [📄 arXiv](https://arxiv.org/abs/2607.25659) • [📥 PDF](https://arxiv.org/pdf/2607.25659)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> CoRT addresses a simple but important mismatch in rubric-guided RL: rich criterion-level feedback is ultimately collapsed into one response-level advantage and broadcast uniformly to every generated token. By replaying the same response with and w...

</details>

<details>
<summary><b>6. CAST: Game Solvers as Turn-Level Teachers for LLM Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.25308) • [📄 arXiv](https://arxiv.org/abs/2607.25308) • [📥 PDF](https://arxiv.org/pdf/2607.25308)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Wloner0809/CAST)

> Training LLMs to play long-horizon games with RLVR is hard: the reward is a single 0/1 signal at the very end, so the model never learns which move actually won or lost the game. This is the classic credit-assignment problem. CAST fixes this by re...

</details>

<details>
<summary><b>7. SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yueqing Sun, Zishan Xu, Zhengxi Lu, Yuxin Chen, Zhiyuan Yao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.26784) • [📄 arXiv](https://arxiv.org/abs/2607.26784) • [📥 PDF](https://arxiv.org/pdf/2607.26784)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Within-yao/SkillRise)

> We introduce SkillRise, a unified RL framework where a single policy alternates between solving tasks and curating an evolving skill document across related tasks, with decoupled credit assignment enabling cross-task skill transfer and test-time s...

</details>

<details>
<summary><b>8. OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Zhenghai Chen, Jingjia Cao, Qi Bao, Yusai Zhao, Jingbo Zhou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27155) • [📄 arXiv](https://arxiv.org/abs/2607.27155) • [📥 PDF](https://arxiv.org/pdf/2607.27155)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/baidu-frontier-research/OmegaUse-OfficeVal)

> No abstract available.

</details>

<details>
<summary><b>9. Can AI agents conduct open-ended AI research? Early evidence from two case studies</b> ⭐ 0</summary>

<br/>

**👥 Authors:** David Africa, Stephan Rabanser, Andrew Schwartz, Sayash Kapoor, Peter Kirgis

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27191) • [📄 arXiv](https://arxiv.org/abs/2607.27191) • [📥 PDF](https://arxiv.org/pdf/2607.27191)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. Explicit Layer Modeling for Video Object Insertion and Layer Decomposition</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.25802) • [📄 arXiv](https://arxiv.org/abs/2607.25802) • [📥 PDF](https://arxiv.org/pdf/2607.25802)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/KyujinHan/DBL-Diffusion)

> Release the paper on arXiv! Check out DBL-Diffusion’s amazing layered video generation capabilities🔥

</details>

<details>
<summary><b>11. GPT-Red: Automated Red Teaming via Self-Play at Scale</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.26115) • [📄 arXiv](https://arxiv.org/abs/2607.26115) • [📥 PDF](https://arxiv.org/pdf/2607.26115)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Adrian Wood, Ads Dawson

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.26314) • [📄 arXiv](https://arxiv.org/abs/2607.26314) • [📥 PDF](https://arxiv.org/pdf/2607.26314)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/GangGreenTemperTatum/stealthbench)

> Stealth, the discipline of achieving an objective without revealing your presence, capabilities, or collected intelligence, is what separates sophisticated operators from detectable ones. Elite security researchers and advanced persistent threats ...

</details>

<details>
<summary><b>13. Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems</b> ⭐ 21</summary>

<br/>

**👥 Authors:** alizahidraja

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24117) • [📄 arXiv](https://arxiv.org/abs/2607.24117) • [📥 PDF](https://arxiv.org/pdf/2607.24117)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/alizahidraja/isnad)

> Author here. Multi-agent pipelines fail silently: an unreliable intermediate link degrades the output while the final answer stays fluent and confident. Existing work largely verifies the agent's identity and permissions, not the truth and corrobo...

</details>

<details>
<summary><b>14. SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.26791) • [📄 arXiv](https://arxiv.org/abs/2607.26791) • [📥 PDF](https://arxiv.org/pdf/2607.26791)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Alibaba-NLP/qqr/tree/main/data/secrespond)

> We introduce SecRespond , a benchmark for evaluating AI agents on real-world post-compromise incident response. It includes 10 reproducible cyber ranges across Linux and Windows, frozen forensic disk snapshots, synthetic security-product evidence,...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 14 |
| 📅 Today | [`2026-07-30.json`](data/daily/2026-07-30.json) | 14 |
| 📆 This Week | [`2026-W30.json`](data/weekly/2026-W30.json) | 67 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 552 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-30 | 14 | [View JSON](data/daily/2026-07-30.json) |
| 📄 2026-07-29 | 15 | [View JSON](data/daily/2026-07-29.json) |
| 📄 2026-07-28 | 24 | [View JSON](data/daily/2026-07-28.json) |
| 📄 2026-07-27 | 14 | [View JSON](data/daily/2026-07-27.json) |
| 📄 2026-07-26 | 22 | [View JSON](data/daily/2026-07-26.json) |
| 📄 2026-07-25 | 22 | [View JSON](data/daily/2026-07-25.json) |
| 📄 2026-07-24 | 16 | [View JSON](data/daily/2026-07-24.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W30 | 67 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |
| 📅 2026-W27 | 133 | [View JSON](data/weekly/2026-W27.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 552 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |

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
