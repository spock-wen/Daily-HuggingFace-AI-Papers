<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-18-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6586+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">73</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">315</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6586+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 13, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Jie Li, Yi Liu, Yixu Wang, Xin Wang, Yunhao Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.00677) • [📄 arXiv](https://arxiv.org/abs/2608.00677) • [📥 PDF](https://arxiv.org/pdf/2608.00677)

**💻 Code:** [⭐ Code](https://github.com/AI45Lab/OpenART) • [⭐ Code](https://github.com/huggingface)

> AI agents operate in persistent environments where early state changes can influence decisions far into the future. Unlike conventional language-model interactions, agent behavior is mediated through a shared state that is repeatedly modified and ...

</details>

<details>
<summary><b>2. AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12307) • [📄 arXiv](https://arxiv.org/abs/2608.12307) • [📥 PDF](https://arxiv.org/pdf/2608.12307)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Paper Link: https://arxiv.org/pdf/2608.12307 A strong model can transfer capability to a weaker model at test time by automatically building an inference harness.

</details>

<details>
<summary><b>3. Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill</b> ⭐ 505</summary>

<br/>

**👥 Authors:** Desan Dai, Chris D Yan, Yiran Wang, Biao Wu, Zhuoyang Qian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11924) • [📄 arXiv](https://arxiv.org/abs/2608.11924) • [📥 PDF](https://arxiv.org/pdf/2608.11924)

**💻 Code:** [⭐ Code](https://github.com/Spark-To-Paper-Skills/spark-to-paper-skills) • [⭐ Code](https://github.com/huggingface)

> 🚀 Spark-to-Paper is now on Hugging Face Daily Papers: drop in a one-line research idea and get an end-to-end draft with verified citations, auto-run experiments, and editable vector figures.

</details>

<details>
<summary><b>4. Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in Interactive Narratives</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Runnan Wang, Ka Hou Kam, Bei Shi, Jianhao Yan, Yingpeng Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08160) • [📄 arXiv](https://arxiv.org/abs/2608.08160) • [📥 PDF](https://arxiv.org/pdf/2608.08160)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yingpengma/NCP-Bench)

> We release our data, code and prompt templates in https://github.com/yingpengma/NCP-Bench .

</details>

<details>
<summary><b>5. StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shifang Zhao, Hongkai Li, Longxuan Deng, Zixiang Li, Yuyang Yin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12314) • [📄 arXiv](https://arxiv.org/abs/2608.12314) • [📥 PDF](https://arxiv.org/pdf/2608.12314)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>6. Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically Consistent 3D Vision Foundation Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10708) • [📄 arXiv](https://arxiv.org/abs/2608.10708) • [📥 PDF](https://arxiv.org/pdf/2608.10708)

**💻 Code:** [⭐ Code](https://github.com/CMLab-Korea/Self-Geometry) • [⭐ Code](https://github.com/huggingface)

> Excited to share our new work: Self-Geometry! 🎉 TL;DR: A GT-free, plug-and-play test-time adaptation pipeline that imposes explicit multi-view geometric constraints on pretrained 3D Vision Foundation Models, using 2D pixel correspondences as pseud...

</details>

<details>
<summary><b>7. From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-Based Video Dereflection</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11562) • [📄 arXiv](https://arxiv.org/abs/2608.11562) • [📥 PDF](https://arxiv.org/pdf/2608.11562)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Interesting work on video reflection removal , a problem that has received much less attention than single-image reflection removal. The paper proposes a closed-loop approach combining physics-grounded reflection synthesis, diffusion-based video d...

</details>

<details>
<summary><b>8. ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment of LLM-based Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11878) • [📄 arXiv](https://arxiv.org/abs/2608.11878) • [📥 PDF](https://arxiv.org/pdf/2608.11878)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MurrayTom/ToolHazard)

> In this study, we propose ToolHazard, a scalable adversarial environment synthesis framework that enables agent security evaluation and adversarial alignment across broader application domains.

</details>

<details>
<summary><b>9. Persistent Recursive Worlds Enable Autonomous Software Evolution</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10450) • [📄 arXiv](https://arxiv.org/abs/2608.10450) • [📥 PDF](https://arxiv.org/pdf/2608.10450)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EMI-Group/genesis)

> One only needs to describe what the software should become. Genesis recursively creates local responsibilities, instantiates finite-lived agents where needed, validates what comes back, and carries accepted consequences forward as one persistent s...

</details>

<details>
<summary><b>10. MBA: Multimodal Benchmark and Agents for Real-World Business Ideation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11616) • [📄 arXiv](https://arxiv.org/abs/2608.11616) • [📥 PDF](https://arxiv.org/pdf/2608.11616)

**💻 Code:** [⭐ Code](https://github.com/hchoi256/MBA) • [⭐ Code](https://github.com/huggingface)

> Business opportunities exist in the real world—not just in text. Yet most AI-driven business ideation remains largely text-centric, overlooking rich visual signals from products, environments, interfaces, and everyday scenes. We introduce MBA: Mul...

</details>

<details>
<summary><b>11. AVA-Encoder: Towards Agent-Native Video Representation Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhijing Zhang, Tian Xueyun, Haozhe Wang, Jinpeng Yu, Chuyue Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12313) • [📄 arXiv](https://arxiv.org/abs/2608.12313) • [📥 PDF](https://arxiv.org/pdf/2608.12313)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. Agent Safety Should Be a Runtime Contract</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenhao Wang, Jusheng Zhang, Yi Han, Albus W. Ng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11274) • [📄 arXiv](https://arxiv.org/abs/2608.11274) • [📥 PDF](https://arxiv.org/pdf/2608.11274)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Agent safety shouldn’t stop at training: our new paper argues for runtime contracts that block dangerous actions and require checkable evidence that agents actually did what they claim.

</details>

<details>
<summary><b>13. The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chaochao Lu, Lai Wei, Bo Peng, zhwang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06270) • [📄 arXiv](https://arxiv.org/abs/2608.06270) • [📥 PDF](https://arxiv.org/pdf/2608.06270)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenCausaLab/CauAudit)

> Thinking-with-images models interleave reasoning with visual operations such as crop-and-zoom. Aggregate accuracy gains often look like successful tool-use, but many rollouts do not actually rely on the returned visual evidence. This work formulat...

</details>

<details>
<summary><b>14. AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mohammad Reza Taesiri, Harold Chaput, Fernando De Mesentier Silva, Xuankang Zhu, Marjan Moodi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11216) • [📄 arXiv](https://arxiv.org/abs/2608.11216) • [📥 PDF](https://arxiv.org/pdf/2608.11216)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>15. Hand Visibility Detector: Per-Keypoint Visibility Estimation for Hands</b> ⭐ 30</summary>

<br/>

**👥 Authors:** Takuma Yagi, Atsushi Hashimoto, Rintaro Yanagi, Masashi Hatano, Ryosei Hara

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11574) • [📄 arXiv](https://arxiv.org/abs/2608.11574) • [📥 PDF](https://arxiv.org/pdf/2608.11574)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ryhara/hand_visibility_detector)

> It predicts the visibility of each hand joint 👋 We hope researchers across HCI, robotics, hand-object interaction, and beyond will find hand visibility estimation useful in their own work! The code has been available on GitHub for a while, and I’m...

</details>

<details>
<summary><b>16. Simplex Relaxation for Discrete Diffusion</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xulei Yang, Jaehong Yoon, Satoshi Hayakawa, Patrick Pynadath, Jinya Sakurai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10615) • [📄 arXiv](https://arxiv.org/abs/2608.10615) • [📥 PDF](https://arxiv.org/pdf/2608.10615)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> .

</details>

<details>
<summary><b>17. NeuPAT: Neuron-aware Plasticity Allocation Tuning for Language-Preserving MLLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08107) • [📄 arXiv](https://arxiv.org/abs/2608.08107) • [📥 PDF](https://arxiv.org/pdf/2608.08107)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multimodal expansion of large language models (LLMs) enables new perceptual capabilities but often compromises the language intelligence acquired during pretraining. In this work, we investigate this phenomenon from the perspective of internal ada...

</details>

<details>
<summary><b>18. AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06729) • [📄 arXiv](https://arxiv.org/abs/2608.06729) • [📥 PDF](https://arxiv.org/pdf/2608.06729)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> While Vision-Language-Action (VLA) models have advanced embodied AI, their fundamentally reactive paradigm severely limits performance in partially observable and long-horizon tasks. When restricted to a single wrist-mounted camera, they inevitabl...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 18 |
| 📅 Today | [`2026-08-13.json`](data/daily/2026-08-13.json) | 18 |
| 📆 This Week | [`2026-W32.json`](data/weekly/2026-W32.json) | 73 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 315 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-13 | 18 | [View JSON](data/daily/2026-08-13.json) |
| 📄 2026-08-12 | 19 | [View JSON](data/daily/2026-08-12.json) |
| 📄 2026-08-11 | 17 | [View JSON](data/daily/2026-08-11.json) |
| 📄 2026-08-10 | 19 | [View JSON](data/daily/2026-08-10.json) |
| 📄 2026-08-09 | 30 | [View JSON](data/daily/2026-08-09.json) |
| 📄 2026-08-08 | 30 | [View JSON](data/daily/2026-08-08.json) |
| 📄 2026-08-07 | 17 | [View JSON](data/daily/2026-08-07.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W32 | 73 | [View JSON](data/weekly/2026-W32.json) |
| 📅 2026-W31 | 166 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 315 | [View JSON](data/monthly/2026-08.json) |
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
