<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-21-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5573+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">21</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">87</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">751</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5573+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 25, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Are We Ready For An Agent-Native Memory System?</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.24775) • [📄 arXiv](https://arxiv.org/abs/2606.24775) • [📥 PDF](https://arxiv.org/pdf/2606.24775)

**💻 Code:** [⭐ Code](https://github.com/OpenDataBox/MemoryData) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenDataBox/awesome-agent-memory)

> Please refer to our paper list at: https://github.com/OpenDataBox/awesome-agent-memory ; Please refer to our code repository at: https://github.com/OpenDataBox/MemoryData .

</details>

<details>
<summary><b>2. DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation</b> ⭐ 21</summary>

<br/>

**👥 Authors:** Cheng Chen, Junwen Pan, Rongchang Xie, Yiyang Cai, Nan Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.26058) • [📄 arXiv](https://arxiv.org/abs/2606.26058) • [📥 PDF](https://arxiv.org/pdf/2606.26058)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKUST-C4G/DomainShuttle)

> We propose DomainShuttle, an open-domain subject-driven text-to-video method that flexibly handles both in-domain fidelity and cross-domain editability by decoupling reference and video features, modeling domain attributes, and learning intrinsic ...

</details>

<details>
<summary><b>3. ShutterMuse: Capture-Time Photography Guidance with MLLMs</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Ping Huang, Wei Cheng, Tianyu Hu, Yixiao Fang, Jiayu Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.25763) • [📄 arXiv](https://arxiv.org/abs/2606.25763) • [📥 PDF](https://arxiv.org/pdf/2606.25763)

**💻 Code:** [⭐ Code](https://github.com/lijayuTnT/ShutterMuse) • [⭐ Code](https://github.com/huggingface)

> ShutterMuse is a unified multimodal large language model for capture-time photography guidance. It supports: Photographer-side guidance: keep, refine, or reject the current framing, with a composition box when refinement is needed. Subject-side gu...

</details>

<details>
<summary><b>4. Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.25041) • [📄 arXiv](https://arxiv.org/abs/2606.25041) • [📥 PDF](https://arxiv.org/pdf/2606.25041)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Wan-Streamer v0.1 is a native-streaming, end-to-end model that listens, sees, thinks, speaks, and responds on video in real time — at 25 fps with ~200 ms model-side latency, all within a single Transformer.

</details>

<details>
<summary><b>5. Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence</b> ⭐ 262</summary>

<br/>

**👥 Authors:** Haoyue Yang, Xuexin Liu, Jingyu Xiao, Qiushi Sun, Xuanle Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.15932) • [📄 arXiv](https://arxiv.org/abs/2606.15932) • [📥 PDF](https://arxiv.org/pdf/2606.15932)

**💻 Code:** [⭐ Code](https://github.com/xjywhu/Awesome-Multimodal-LLM-for-Code) • [⭐ Code](https://github.com/huggingface)

> GitHub Repo at https://github.com/xjywhu/Awesome-Multimodal-LLM-for-Code

</details>

<details>
<summary><b>6. Improved Large Language Diffusion Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.25331) • [📄 arXiv](https://arxiv.org/abs/2606.25331) • [📥 PDF](https://arxiv.org/pdf/2606.25331)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> awesome

</details>

<details>
<summary><b>7. MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.26087) • [📄 arXiv](https://arxiv.org/abs/2606.26087) • [📥 PDF](https://arxiv.org/pdf/2606.26087)

**💻 Code:** [⭐ Code](https://github.com/cvlab-kaist/MVTrack4Gen) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>8. IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.24849) • [📄 arXiv](https://arxiv.org/abs/2606.24849) • [📥 PDF](https://arxiv.org/pdf/2606.24849)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> IV-CoT introduces an elegant implicit visual reasoning mechanism for text-to-image generation, separating structural planning from semantic rendering to improve compositional fidelity in counts, spatial relations, and layouts without requiring exp...

</details>

<details>
<summary><b>9. EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies</b> ⭐ 95</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18239) • [📄 arXiv](https://arxiv.org/abs/2606.18239) • [📥 PDF](https://arxiv.org/pdf/2606.18239)

**💻 Code:** [⭐ Code](https://github.com/InternRobotics/EBench) • [⭐ Code](https://github.com/huggingface)

> EBench is a  surgical diagnosis tool for robot foundation models. It provides not a leaderboard, but A CAT scan for your policy. Here's why the field needed this, and what it actually reveals about π0, π0.5, Qwen-RobotManip, and the rest: 1/ The "...

</details>

<details>
<summary><b>10. V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.25319) • [📄 arXiv](https://arxiv.org/abs/2606.25319) • [📥 PDF](https://arxiv.org/pdf/2606.25319)

**💻 Code:** [⭐ Code](https://github.com/eVI-group-SCU/V-Zero) • [⭐ Code](https://github.com/huggingface)

> V-Zero improves fine-grained visual reasoning without annotated answer labels. The student model samples on-policy reasoning trajectories from the full image, while a teacher model replays the same trajectories with paired positive and negative vi...

</details>

<details>
<summary><b>11. Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.25473) • [📄 arXiv](https://arxiv.org/abs/2606.25473) • [📥 PDF](https://arxiv.org/pdf/2606.25473)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. UnityShots: Memory-Driven Multi-Shot Audio-Video Generation with Boundary-Aware Gating</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21661) • [📄 arXiv](https://arxiv.org/abs/2606.21661) • [📥 PDF](https://arxiv.org/pdf/2606.21661)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/JIA-Lab-research/UnityShots)

> Generating a coherent multi-shot video requires structured cross-shot memory: subject appearance, scene context, and speaker identity must persist across cuts. Existing approaches either train end-to-end over fixed-length sequences and cannot scal...

</details>

<details>
<summary><b>13. Autodata: An agentic data scientist to create high quality synthetic data</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.25996) • [📄 arXiv](https://arxiv.org/abs/2606.25996) • [📥 PDF](https://arxiv.org/pdf/2606.25996)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.24484) • [📄 arXiv](https://arxiv.org/abs/2606.24484) • [📥 PDF](https://arxiv.org/pdf/2606.24484)

**💻 Code:** [⭐ Code](https://github.com/YesianRohn/WATER) • [⭐ Code](https://github.com/huggingface)

> It constructs WATER-S, a 2M-scale synthetic artistic text dataset, and proposes WATERec, a strong STR baseline supporting arbitrary-shaped inputs. It achieves 90.40% accuracy on WordArt-Bench, the first result exceeding 90%, surpassing both genera...

</details>

<details>
<summary><b>15. The Hitchhiker's Guide to Agentic AI: From Foundations to Systems</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haggai Roitman

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.24937) • [📄 arXiv](https://arxiv.org/abs/2606.24937) • [📥 PDF](https://arxiv.org/pdf/2606.24937)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>16. Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.22565) • [📄 arXiv](https://arxiv.org/abs/2606.22565) • [📥 PDF](https://arxiv.org/pdf/2606.22565)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We aim to systematically investigate the key question: What can multimodal Chain-of-Thought reasoning do, and where and why does it fall short?

</details>

<details>
<summary><b>17. TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.26092) • [📄 arXiv](https://arxiv.org/abs/2606.26092) • [📥 PDF](https://arxiv.org/pdf/2606.26092)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing t...

</details>

<details>
<summary><b>18. RL-Index: Reinforcement Learning for Retrieval Index Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Koustava Goswami, Utkarsh Sahu, Zhisheng Qi, Nedim Lipka, Yongjia Lei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.16316) • [📄 arXiv](https://arxiv.org/abs/2606.16316) • [📥 PDF](https://arxiv.org/pdf/2606.16316)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>19. CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Franck Dernoncourt, Ryan A. Rossi, Morayo Danielle Adeyemi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.24083) • [📄 arXiv](https://arxiv.org/abs/2606.24083) • [📥 PDF](https://arxiv.org/pdf/2606.24083)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/danielle34/cavewoman)

> No abstract available.

</details>

<details>
<summary><b>20. RoPE-Aware Bit Allocation for KV-Cache Quantization</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Jiaya Jia, Yuechen Zhang, Fengfeng Liang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.24033) • [📄 arXiv](https://arxiv.org/abs/2606.24033) • [📥 PDF](https://arxiv.org/pdf/2606.24033)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/JIA-Lab-research/blockgtq)

> RoPE-Aware Bit Allocation for KV-Cache Quantization

</details>

<details>
<summary><b>21. When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.20023) • [📄 arXiv](https://arxiv.org/abs/2606.20023) • [📥 PDF](https://arxiv.org/pdf/2606.20023)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AISafetyHub/agent-tool-selection-bias)

> As LLM agents increasingly select tools autonomously, their choices among tools with different privileges become safety-relevant. However, prior tool-selection studies focus on safety-agnostic metadata preferences, leaving privilege-sensitive choi...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 21 |
| 📅 Today | [`2026-06-25.json`](data/daily/2026-06-25.json) | 21 |
| 📆 This Week | [`2026-W25.json`](data/weekly/2026-W25.json) | 87 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 751 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-25 | 21 | [View JSON](data/daily/2026-06-25.json) |
| 📄 2026-06-24 | 20 | [View JSON](data/daily/2026-06-24.json) |
| 📄 2026-06-23 | 37 | [View JSON](data/daily/2026-06-23.json) |
| 📄 2026-06-22 | 9 | [View JSON](data/daily/2026-06-22.json) |
| 📄 2026-06-21 | 34 | [View JSON](data/daily/2026-06-21.json) |
| 📄 2026-06-20 | 34 | [View JSON](data/daily/2026-06-20.json) |
| 📄 2026-06-19 | 25 | [View JSON](data/daily/2026-06-19.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W25 | 87 | [View JSON](data/weekly/2026-W25.json) |
| 📅 2026-W24 | 194 | [View JSON](data/weekly/2026-W24.json) |
| 📅 2026-W23 | 247 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 751 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |

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
