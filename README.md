<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-19-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6568+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">55</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">297</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6568+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 12, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. ComBodied Agents: a New Paradigm of Human-Centric Agentic AI</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Feixiang Wang, Zhibin Wang, Rui Feng, Xingyao Wang, Qianggang Ding

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10915) • [📄 arXiv](https://arxiv.org/abs/2608.10915) • [📥 PDF](https://arxiv.org/pdf/2608.10915)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> COMBODIED AGENTS

</details>

<details>
<summary><b>2. Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Linsi Wu, Zecong Tang, Junhao Shen, Jiayu Liu, Qing Zong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10299) • [📄 arXiv](https://arxiv.org/abs/2608.10299) • [📥 PDF](https://arxiv.org/pdf/2608.10299)

**💻 Code:** [⭐ Code](https://github.com/zongqing0068/awesome-co-evolution) • [⭐ Code](https://github.com/huggingface)

> Agentic systems are increasingly expected to improve after deployment, yet single-entity self-evolution is often bounded by a static learning context, such as fixed tasks and feedback. This survey focuses on co-evolution in agentic systems, a mult...

</details>

<details>
<summary><b>3. Articulated Object Reconstruction from Rest-State Observation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27749) • [📄 arXiv](https://arxiv.org/abs/2607.27749) • [📥 PDF](https://arxiv.org/pdf/2607.27749)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Recovers part geometry and joint parameters from a single resting-state observation, exported directly as a simulation-ready URDF.

</details>

<details>
<summary><b>4. Beyond Pixels: From Video Priors to 4D Worlds</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yi Yang, Ruijie Quan, Zhenglin Zhou, Xiaolong Shen, Zihao Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10744) • [📄 arXiv](https://arxiv.org/abs/2608.10744) • [📥 PDF](https://arxiv.org/pdf/2608.10744)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Great method

</details>

<details>
<summary><b>5. AdvFD: Boosting Visual Generation via Adversarial Fr'echet Distance Loss</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11205) • [📄 arXiv](https://arxiv.org/abs/2608.11205) • [📥 PDF](https://arxiv.org/pdf/2608.11205)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Fréchet distance has recently emerged as an effective distribution-level objective for generator post-training. However, directly optimizing it can cause Fréchet hacking: the target metric keeps improving while visual quality and Fréchet alignment...

</details>

<details>
<summary><b>6. Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.07645) • [📄 arXiv](https://arxiv.org/abs/2608.07645) • [📥 PDF](https://arxiv.org/pdf/2608.07645)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RealLcz/MGM)

> Excited to share Mendel Gödel Machine (MGM)! 🧬 Recent self-evolving agents have shown that agents can improve themselves through iterative evaluation and modification. But in many existing systems, each evolution step is still driven by only a sin...

</details>

<details>
<summary><b>7. Ex-Omni-2D: Expressive Omni-Modal Dialogue Models with Native Visual Presence</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Yiwen Guo, Tianshu Yu, Xiaoying Tang, Zhipeng Li, Haoyu Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10720) • [📄 arXiv](https://arxiv.org/abs/2608.10720) • [📥 PDF](https://arxiv.org/pdf/2608.10720)

**💻 Code:** [⭐ Code](https://github.com/LOGO-CUHKSZ/Ex-Omni-2D-Code) • [⭐ Code](https://github.com/huggingface)

> What if an omni-modal dialogue model could not only listen and speak, but also appear? Ex-Omni-2D generates coordinated text, personalized speech, and expressive avatar video within a unified dialogue framework. We would love to hear your thoughts...

</details>

<details>
<summary><b>8. SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xuan Jin, Yantao Zhang, Chao Liu, Hongqiang Lin, Xiaofan Bai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11079) • [📄 arXiv](https://arxiv.org/abs/2608.11079) • [📥 PDF](https://arxiv.org/pdf/2608.11079)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>9. SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Personal Information</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenjie Fu, Yulun Zhu, Shaofan Liu, Zhuohui Sheng, Junjie Ye

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10692) • [📄 arXiv](https://arxiv.org/abs/2608.10692) • [📥 PDF](https://arxiv.org/pdf/2608.10692)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> https://huggingface.co/datasets/Junjie-Ye/SPIEval

</details>

<details>
<summary><b>10. VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10875) • [📄 arXiv](https://arxiv.org/abs/2608.10875) • [📥 PDF](https://arxiv.org/pdf/2608.10875)

**💻 Code:** [⭐ Code](https://github.com/evolvent-ai/VibeLifeBench) • [⭐ Code](https://github.com/huggingface)

> Most agent benchmarks give a clear instruction and a frozen sandbox. Real life gives neither: the task runs for weeks, the constraints that matter are never said out loud, and the world keeps moving while nobody is prompting the agent. In VibeLife...

</details>

<details>
<summary><b>11. Reference-Free Post-Training of Open Large Language Models for Multilingual Machine Translation</b> ⭐ 66</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10812) • [📄 arXiv](https://arxiv.org/abs/2608.10812) • [📥 PDF](https://arxiv.org/pdf/2608.10812)

**💻 Code:** [⭐ Code](https://github.com/xiaomi-research/gemmax) • [⭐ Code](https://github.com/huggingface)

> Try the live demo: https://huggingface.co/spaces/xiaomi-research/milmmt-46-translation

</details>

<details>
<summary><b>12. DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10636) • [📄 arXiv](https://arxiv.org/abs/2608.10636) • [📥 PDF](https://arxiv.org/pdf/2608.10636)

**💻 Code:** [⭐ Code](https://github.com/Ryenhails/NanoVDR) • [⭐ Code](https://github.com/huggingface)

> Quick follow-up on NanoVDR: we distilled an 8B visual document retriever down to a 457M document tower and a 70M query tower by simply reproducing the frozen Qwen3-VL-Embedding-8B page embeddings under cosine distance. No relevance labels, no nega...

</details>

<details>
<summary><b>13. UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zitong Wang, Peize Li, Bin Gu, Lei Xin, arnodjiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08627) • [📄 arXiv](https://arxiv.org/abs/2608.08627) • [📥 PDF](https://arxiv.org/pdf/2608.08627)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 UniMoMo , a practical approach for compressing MoE-based recommendation models. The main idea is simple but effective: instead of merging experts based on parameter similarity, UniMoMo looks at how experts actually behave on calibration data and...

</details>

<details>
<summary><b>14. Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Nischal Ashok Kumar, Evan William Ciccarelli, Kirat Arora, Reshma Ashok, Harshitha Kolukuluru

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08389) • [📄 arXiv](https://arxiv.org/abs/2608.08389) • [📥 PDF](https://arxiv.org/pdf/2608.08389)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>15. TSDS-Toolbox: A Toolbox for Measuring Time-Series Dataset Similarity</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Franck Dernoncourt, Ryan A. Rossi, Hongjie Chen, Yen-Ku Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08119) • [📄 arXiv](https://arxiv.org/abs/2608.08119) • [📥 PDF](https://arxiv.org/pdf/2608.08119)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>16. iFAN: Inference-Aware Learning for Plain Mask Transformers</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jingling Fu, Lichen Ma, Haoyang Tong, Yu He, Fang Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.03216) • [📄 arXiv](https://arxiv.org/abs/2608.03216) • [📥 PDF](https://arxiv.org/pdf/2608.03216)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> iFAN: Inference-Aware Learning for Plain Mask Transformers

</details>

<details>
<summary><b>17. JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiawei Yang, Jiate Li, Jike Zhong, Wei Yang, Shawn Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.27670) • [📄 arXiv](https://arxiv.org/abs/2607.27670) • [📥 PDF](https://arxiv.org/pdf/2607.27670)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Dataset: https://huggingface.co/datasets/ShawnLi02/JigShape-Train

</details>

<details>
<summary><b>18. DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Shafiq Joty, Md Tahmid Rahman Laskar, Ridwan Mahbub, Mohammed Saidul Islam, Mizanur Rahman

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10366) • [📄 arXiv](https://arxiv.org/abs/2608.10366) • [📥 PDF](https://arxiv.org/pdf/2608.10366)

**💻 Code:** [⭐ Code](https://github.com/vis-nlp/DSAgentBench) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>19. Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Pedro Reviriego, Gonzalo Martínez, Javier Conde, Ori Rottenstreich, Tadanobu Chuyo Kamijo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09900) • [📄 arXiv](https://arxiv.org/abs/2608.09900) • [📥 PDF](https://arxiv.org/pdf/2608.09900)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large language model evaluations typically focus on performance under nominal conditions, creating an illusion of capability where models comfortably walk a narrow, highly optimized generation corridor. In real-world deployments, however, complex ...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 19 |
| 📅 Today | [`2026-08-12.json`](data/daily/2026-08-12.json) | 19 |
| 📆 This Week | [`2026-W32.json`](data/weekly/2026-W32.json) | 55 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 297 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-12 | 19 | [View JSON](data/daily/2026-08-12.json) |
| 📄 2026-08-11 | 17 | [View JSON](data/daily/2026-08-11.json) |
| 📄 2026-08-10 | 19 | [View JSON](data/daily/2026-08-10.json) |
| 📄 2026-08-09 | 30 | [View JSON](data/daily/2026-08-09.json) |
| 📄 2026-08-08 | 30 | [View JSON](data/daily/2026-08-08.json) |
| 📄 2026-08-07 | 17 | [View JSON](data/daily/2026-08-07.json) |
| 📄 2026-08-06 | 23 | [View JSON](data/daily/2026-08-06.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W32 | 55 | [View JSON](data/weekly/2026-W32.json) |
| 📅 2026-W31 | 166 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 297 | [View JSON](data/monthly/2026-08.json) |
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
