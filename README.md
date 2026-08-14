<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-19-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6605+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">92</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">334</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6605+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 14, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation</b> ⭐ 23</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13489) • [📄 arXiv](https://arxiv.org/abs/2608.13489) • [📥 PDF](https://arxiv.org/pdf/2608.13489)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AMAP-ML/DreamX-Phi)

> At the time of writing, DreamX-Phi 1.0 achieves first place on Track 1 and second place on Track 2 of the WorldArena 2.0 Challenge. Model weights and inference code will be made publicly available ( https://github.com/AMAP-ML/DreamX-Phi ) after th...

</details>

<details>
<summary><b>2. LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers</b> ⭐ 2.34k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06867) • [📄 arXiv](https://arxiv.org/abs/2608.06867) • [📥 PDF](https://arxiv.org/pdf/2608.06867)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ulab-uiuc/LLMRouter)

> 🚀 LLMRouter is a comprehensive ecosystem for LLM routing — spanning benchmarking, algorithm development, and real-world/agentic deployment . 📊 Broad Benchmark Coverage: xRouteBench goes far beyond conventional single-turn text routing, covering 5 ...

</details>

<details>
<summary><b>3. Intern-S2-Preview: Scientific Agentic Foundation Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kai Chen, Guanzhou Chen, Chiyu Chen, Jiaqi Cao, Lei Bai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13505) • [📄 arXiv](https://arxiv.org/abs/2608.13505) • [📥 PDF](https://arxiv.org/pdf/2608.13505)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>4. DarwinX: Evolving Agent Harnesses Through Natural Selection</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.07545) • [📄 arXiv](https://arxiv.org/abs/2608.07545) • [📥 PDF](https://arxiv.org/pdf/2608.07545)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We freeze the base model and evolve only the harness — prompts, tools, skills, control flow — by label-free natural selection: variants are scored on measured fitness (avg@k, no gold solutions), survivors are kept, and complementary ones are merge...

</details>

<details>
<summary><b>5. AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13560) • [📄 arXiv](https://arxiv.org/abs/2608.13560) • [📥 PDF](https://arxiv.org/pdf/2608.13560)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yaxin9Luo/AutoDesign)

> We also provide live demo at: https://designanything.ai/ , though, we recommend to locally install for the best experience. We also welcome the community to submit issues or propose PR, together, we can continously improve autodesign.

</details>

<details>
<summary><b>6. Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12743) • [📄 arXiv](https://arxiv.org/abs/2608.12743) • [📥 PDF](https://arxiv.org/pdf/2608.12743)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Spatial Memory Agent introduces a practical, parameter-update-free approach to improving frozen VLMs on spatial reasoning. By distilling verified experience into transferable memory and calibrating retrieval reliability, SMA delivers consistent ga...

</details>

<details>
<summary><b>7. Alaya-EVOKE: From Linear-Scaling Supervision to Endless World</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kaipeng Zhang, Chuanhao Li, Yifan Zhan, Gongxuan Wang, Yuanyang Yin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13546) • [📄 arXiv](https://arxiv.org/abs/2608.13546) • [📥 PDF](https://arxiv.org/pdf/2608.13546)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SII-YuanyangYin/Evoke)

> Code: https://github.com/SII-YuanyangYin/Evoke Page: https://evoke-world.github.io/Evoke/ YouTube Demo: https://youtu.be/QX7PBBaBGdc

</details>

<details>
<summary><b>8. PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Yiyang Wang, Zhiyuan Xu, Minghong Cai, Xi Chen, Kaixin Ding

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13552) • [📄 arXiv](https://arxiv.org/abs/2608.13552) • [📥 PDF](https://arxiv.org/pdf/2608.13552)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kxding/PlayWorld)

> PlayWorld, a new benchmark for interactive video world models. World models vary substantially in action granularity and response speed, so executing the same fixed action sequence often fails to bring them to the same state, making fair compariso...

</details>

<details>
<summary><b>9. Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12149) • [📄 arXiv](https://arxiv.org/abs/2608.12149) • [📥 PDF](https://arxiv.org/pdf/2608.12149)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/StartluxLabs/Massive-Activations-HLA)

> We present the first systematic study of Massive activations (MAs) in layer-interleaved HLA LLMs and uncover two architecture-aligned morphologies: MAs consistently spike immediately before full attention layers, forming pre-attention spikes (PAS)...

</details>

<details>
<summary><b>10. UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11752) • [📄 arXiv](https://arxiv.org/abs/2608.11752) • [📥 PDF](https://arxiv.org/pdf/2608.11752)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/uniswap-av/UniSwap)

> We present UniSwap, a framework for streaming joint audio-visual identity replacement in talking videos. Unlike existing methods that optimize appearance and voice using separate models, UniSwap performs joint transfer within a single audio-visual...

</details>

<details>
<summary><b>11. LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.11745) • [📄 arXiv](https://arxiv.org/abs/2608.11745) • [📥 PDF](https://arxiv.org/pdf/2608.11745)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/liveanimate/LiveAnimate)

> In this work, we present LiveAnimate, which brings 14B-parameter video Diffusion Transformers to real-time streaming inference (19.63 FPS on 2x H100) for interactive full-body animation. We focus on solving the quality degradation and memory explo...

</details>

<details>
<summary><b>12. H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13049) • [📄 arXiv](https://arxiv.org/abs/2608.13049) • [📥 PDF](https://arxiv.org/pdf/2608.13049)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Rongdingyi/H2R-Bench)

> Large-scale manipulation data is essential for robot learning, yet collecting robot demonstrations remains expensive and difficult to scale. Meanwhile, abundant egocentric human manipulation videos provide rich behavioral experiences, but transfer...

</details>

<details>
<summary><b>13. How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08975) • [📄 arXiv](https://arxiv.org/abs/2608.08975) • [📥 PDF](https://arxiv.org/pdf/2608.08975)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MingLiiii/Dissecting_AI_Reviews)

> How Can Rhetoric Reward Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review 🤔🤔 We already know that rewriting a paper can affect AI review scores. But how exactly does rhetoric matter? Which rhetorical choices move AI revi...

</details>

<details>
<summary><b>14. Full-bandwidth transformer</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08888) • [📄 arXiv](https://arxiv.org/abs/2608.08888) • [📥 PDF](https://arxiv.org/pdf/2608.08888)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Was there a study of comparative scaling laws for this design? It seems that having to do multiple passes during training may require more training compute, and it is not clear to me that a normal transformer trained with the same compute wouldn't...

</details>

<details>
<summary><b>15. An AI4AI Framework for Visual Token Pruning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhiqin Yang, Yuhan Liu, Wei Song, Wenli Huang, Zhen Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.07193) • [📄 arXiv](https://arxiv.org/abs/2608.07193) • [📥 PDF](https://arxiv.org/pdf/2608.07193)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>16. LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation</b> ⭐ 1.16k</summary>

<br/>

**👥 Authors:** Fuhao Li, Jiahe Huang, Junmai Wang, Zixuan Liu, Dongfang Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12990) • [📄 arXiv](https://arxiv.org/abs/2608.12990) • [📥 PDF](https://arxiv.org/pdf/2608.12990)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LycheeMem/LycheeMem)

> code: https://github.com/LycheeMem/LycheeMem

</details>

<details>
<summary><b>17. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wynne Hsu, Mong-Li Lee, Tianjie Ju, Hao Fei, Bobo Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.13558) • [📄 arXiv](https://arxiv.org/abs/2608.13558) • [📥 PDF](https://arxiv.org/pdf/2608.13558)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>18. SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.10538) • [📄 arXiv](https://arxiv.org/abs/2608.10538) • [📥 PDF](https://arxiv.org/pdf/2608.10538)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DANG-ai/SKILLER)

> Project and code: https://github.com/DANG-ai/SKILLER

</details>

<details>
<summary><b>19. CW-BASS v2: Saturation-Aware Pseudo-Label Selection for Semi-Supervised Segmentation under Foundation-Model Teachers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.12773) • [📄 arXiv](https://arxiv.org/abs/2608.12773) • [📥 PDF](https://arxiv.org/pdf/2608.12773)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/psychofict/CW-BASS-v2)

> Author here. Pseudo-label selection rules — dynamic thresholds, per-class curricula, soft confidence weights — were designed for noisy, under-confident ResNet teachers. A DINOv2 teacher changes the regime: confidence saturates (98% of Pascal pixel...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 19 |
| 📅 Today | [`2026-08-14.json`](data/daily/2026-08-14.json) | 19 |
| 📆 This Week | [`2026-W32.json`](data/weekly/2026-W32.json) | 92 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 334 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-14 | 19 | [View JSON](data/daily/2026-08-14.json) |
| 📄 2026-08-13 | 18 | [View JSON](data/daily/2026-08-13.json) |
| 📄 2026-08-12 | 19 | [View JSON](data/daily/2026-08-12.json) |
| 📄 2026-08-11 | 17 | [View JSON](data/daily/2026-08-11.json) |
| 📄 2026-08-10 | 19 | [View JSON](data/daily/2026-08-10.json) |
| 📄 2026-08-09 | 30 | [View JSON](data/daily/2026-08-09.json) |
| 📄 2026-08-08 | 30 | [View JSON](data/daily/2026-08-08.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W32 | 92 | [View JSON](data/weekly/2026-W32.json) |
| 📅 2026-W31 | 166 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 334 | [View JSON](data/monthly/2026-08.json) |
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
