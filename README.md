<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-16-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6060+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">16</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">16</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">372</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6060+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 20, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories</b> ⭐ 72</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15330) • [📄 arXiv](https://arxiv.org/abs/2607.15330) • [📥 PDF](https://arxiv.org/pdf/2607.15330)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)

> 🚀 Xiaomi-Robotics-1 Is Here: Scaling Robot Learning with Over 100,000 Hours of Real-World Manipulation Data Foundation models in language and vision have advanced through scaling—using more data, larger models, and greater compute. Robotics, howev...

</details>

<details>
<summary><b>2. xHC: Expanded Hyper-Connections</b> ⭐ 21</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.14530) • [📄 arXiv](https://arxiv.org/abs/2607.14530) • [📥 PDF](https://arxiv.org/pdf/2607.14530)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aHapBean/xHC)

> Can residual stream width become a practical scaling axis beyond N=4? xHC achieves this in large scale language model pre-training. As Figure 2 shows, on the 18B MoE model, xHC lowers the final training loss from 1.776 to 1.758 and raises the aver...

</details>

<details>
<summary><b>3. Cura 1T: Specialized Model for Agentic Healthcare</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Deon Metelski, Steve Brown, Leon Qi, Haolin Chen, actAVA AI

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15314) • [📄 arXiv](https://arxiv.org/abs/2607.15314) • [📥 PDF](https://arxiv.org/pdf/2607.15314)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/actava-ai/Cura)

> Cura 1T leads frontier models on 5 of 6 hardest healthcare benchmarks: HealthBench Hard: 36.8 (GPT-5.5: 31.5) HealthBench Professional: 66.2 (Claude Fable 5: 66.0) MedXpertQA-Text: 60.0 (GPT-5.5: 59.6) MedXpertQA-Multimodalt: 72.2 (GPT-5.5: 77.1) ...

</details>

<details>
<summary><b>4. Loop the Loopies!</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ran Tao, Xinyu Yang, Yihao Xiao, Yilong Chen, Zitian Gao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16051) • [📄 arXiv](https://arxiv.org/abs/2607.16051) • [📥 PDF](https://arxiv.org/pdf/2607.16051)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>5. RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM</b> ⭐ 48</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11683) • [📄 arXiv](https://arxiv.org/abs/2607.11683) • [📥 PDF](https://arxiv.org/pdf/2607.11683)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RaguTeam/RAGU)

> GraphRAG doesn't have to be expensive, brittle, or messy. We're the team behind RAGU — an open-source GraphRAG engine built jointly by the Laboratory of Applied Digital Technologies at Novosibirsk State University and the Laboratory of Automated M...

</details>

<details>
<summary><b>6. RecGPT-V3 Technical Report</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Han Zhu, Gaoyang Guo, Dian Chen, Chao Yi, Bowen Zheng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15591) • [📄 arXiv](https://arxiv.org/abs/2607.15591) • [📥 PDF](https://arxiv.org/pdf/2607.15591)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 RecGPT-V3 Is Here: Making LLMs the “Intelligent Brain” of Industrial-Scale Recommender Systems From RecGPT-V1 , which pioneered intent understanding in Taobao’s recommendation pipeline, to RecGPT-V2 , which expanded the breadth and efficiency of...

</details>

<details>
<summary><b>7. From Human-Centric to Agentic Code Review: The Impact of Different Generations of Generative AI Technology on Review Quality</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.13196) • [📄 arXiv](https://arxiv.org/abs/2607.13196) • [📥 PDF](https://arxiv.org/pdf/2607.13196)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We study 1.02 million reviewed pull requests from 207 GitHub projects to examine how code review evolves across human-centric, LLM-assisted, and agentic review eras. By modeling review discussions as human–AI interaction sequences, we find that AI...

</details>

<details>
<summary><b>8. On-Policy Delta Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15161) • [📄 arXiv](https://arxiv.org/abs/2607.15161) • [📥 PDF](https://arxiv.org/pdf/2607.15161)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/naver-ai/opd2)

> We introduce On-Policy Delta Distillation (OPD²), which uses the difference between a reasoning-tuned teacher and its base model as the distillation signal. By focusing on the capability gained during reasoning tuning, OPD² consistently improves o...

</details>

<details>
<summary><b>9. Understanding Reasoning from Pretraining to Post-Training</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Micah Goldblum, Yifan Sun, Salman Rahman, Ang Li, Jingyan Shen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16097) • [📄 arXiv](https://arxiv.org/abs/2607.16097) • [📥 PDF](https://arxiv.org/pdf/2607.16097)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/pavelslab-nyu/pre2post-chess)

> We use chess as a controlled testbed for studying reasoning across the full pretraining-to-post-training pipeline. We follow the standard LLM training pipeline by pretraining language models from 5M to 1B parameters on human chess games, supervise...

</details>

<details>
<summary><b>10. Qwen-Music Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11699) • [📄 arXiv](https://arxiv.org/abs/2607.11699) • [📥 PDF](https://arxiv.org/pdf/2607.11699)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. Recursive Harness Self-Improvement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15524) • [📄 arXiv](https://arxiv.org/abs/2607.15524) • [📥 PDF](https://arxiv.org/pdf/2607.15524)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16107) • [📄 arXiv](https://arxiv.org/abs/2607.16107) • [📥 PDF](https://arxiv.org/pdf/2607.16107)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NVIDIA/audio-flamingo)

> Github: https://github.com/NVIDIA/audio-flamingo

</details>

<details>
<summary><b>13. S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Qingli Wang, Nan Xu, Lifeng Xu, Junyi Liu, Jiahao Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15686) • [📄 arXiv](https://arxiv.org/abs/2607.15686) • [📥 PDF](https://arxiv.org/pdf/2607.15686)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ScienceOne-AI/S1-Omni)

> We’re excited to share S1-Omni , a unified multimodal reasoning model for scientific understanding, prediction, and generation. S1-Omni brings heterogeneous scientific inputs—including text, material CIFs, molecular SMILES, protein sequences, spec...

</details>

<details>
<summary><b>14. DSWorld: A Data Science World Model for Efficient Autonomous Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.15901) • [📄 arXiv](https://arxiv.org/abs/2607.15901) • [📥 PDF](https://arxiv.org/pdf/2607.15901)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce DSWorld, a Data Science World Model that predicts the outcomes of data science operations before real execution. DSWorld achieves a 14× training speedup and 3–6× inference speedup for autonomous data science agents while maintaining c...

</details>

<details>
<summary><b>15. VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders</b> ⭐ 33</summary>

<br/>

**👥 Authors:** Li Jiang, Junchao Huang, Xinting Hu, Junfeng Wu, Zhihao Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.14088) • [📄 arXiv](https://arxiv.org/abs/2607.14088) • [📥 PDF](https://arxiv.org/pdf/2607.14088)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhxie0117/VideoRAE)

> VideoRAE leverages representations from frozen video foundation models to build generation-friendly video autoencoders, enabling up to 5x faster convergence in downstream video generation.

</details>

<details>
<summary><b>16. When Does Muon Help Agentic Reinforcement Learning?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Qianshan Wei, Ziqi Zhou, Zihe Huang, Jinghao Lin, Kai Ruan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16169) • [📄 arXiv](https://arxiv.org/abs/2607.16169) • [📥 PDF](https://arxiv.org/pdf/2607.16169)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Muon isn’t just for pretraining—this paper shows it can dramatically boost long-horizon agentic RL when paired with the right credit assignment strategy.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 16 |
| 📅 Today | [`2026-07-20.json`](data/daily/2026-07-20.json) | 16 |
| 📆 This Week | [`2026-W29.json`](data/weekly/2026-W29.json) | 16 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 372 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-20 | 16 | [View JSON](data/daily/2026-07-20.json) |
| 📄 2026-07-19 | 29 | [View JSON](data/daily/2026-07-19.json) |
| 📄 2026-07-18 | 29 | [View JSON](data/daily/2026-07-18.json) |
| 📄 2026-07-17 | 20 | [View JSON](data/daily/2026-07-17.json) |
| 📄 2026-07-16 | 0 | [View JSON](data/daily/2026-07-16.json) |
| 📄 2026-07-15 | 2 | [View JSON](data/daily/2026-07-15.json) |
| 📄 2026-07-14 | 12 | [View JSON](data/daily/2026-07-14.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W29 | 16 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |
| 📅 2026-W27 | 133 | [View JSON](data/weekly/2026-W27.json) |
| 📅 2026-W26 | 165 | [View JSON](data/weekly/2026-W26.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 372 | [View JSON](data/monthly/2026-07.json) |
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
