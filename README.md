<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-14-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6113+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">69</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">425</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6113+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 23, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD</b> ⭐ 12</summary>

<br/>

**👥 Authors:** Linyuan Qiu, Xuhui Chen, Ruoyu Sun, Xiaodong Luo, Dongfang Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.20145) • [📄 arXiv](https://arxiv.org/abs/2607.20145) • [📥 PDF](https://arxiv.org/pdf/2607.20145)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SLAI-AITP/SLAI-T-Rex)

> Full-parameter post-training of trillion-parameter-scale MoE models introduces substantial system-level challenges for large-scale distributed training, including severe memory pressure, non-overlapped communication overhead, and inefficient kerne...

</details>

<details>
<summary><b>2. Self Gradient Forcing: Native Long Video Extrapolation</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Yawen Luo, Yaowei Li, Yuxuan Bian, Shiyi Zhang, Junhao Zhuang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.20368) • [📄 arXiv](https://arxiv.org/abs/2607.20368) • [📥 PDF](https://arxiv.org/pdf/2607.20368)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhuang2002/Self_Gradient_Forcing)

> Self Gradient Forcing: Native Long Video Extrapolation Code: https://github.com/zhuang2002/Self_Gradient_Forcing Page: https://zhuang2002.github.io/SelfGradientForcing/ HF paper: https://huggingface.co/papers/2607.20368 Arxiv: https://arxiv.org/ab...

</details>

<details>
<summary><b>3. An Exam for Active Observers</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16165) • [📄 arXiv](https://arxiv.org/abs/2607.16165) • [📥 PDF](https://arxiv.org/pdf/2607.16165)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/saccharomycetes/ActiveVision)

> Vision is a loop, not a glance. We introduce ActiveVision, a benchmark testing whether models can repeatedly observe, reason, and seek new visual evidence. Humans solve 96.1%.  The best frontier model: 10.6%. Fable 5, strong at reasoning and codin...

</details>

<details>
<summary><b>4. Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Abulhair Saparov, Dos Baha, Nischay Dhankhar

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.19604) • [📄 arXiv](https://arxiv.org/abs/2607.19604) • [📥 PDF](https://arxiv.org/pdf/2607.19604)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hdnndh/Latent-Geometry-Beyond-Search-Amortizing-Planning-in-World-Models)

> No abstract available.

</details>

<details>
<summary><b>5. Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.10169) • [📄 arXiv](https://arxiv.org/abs/2607.10169) • [📥 PDF](https://arxiv.org/pdf/2607.10169)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Aiolus-X/RIPO)

> This paper addresses a fundamental, decade-old theoretical flaw in PPO: its heuristic clipping mechanism implicitly assumes a Euclidean metric, resulting in a geometric mismatch with the underlying Riemannian manifold of policy distributions. This...

</details>

<details>
<summary><b>6. Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.19747) • [📄 arXiv](https://arxiv.org/abs/2607.19747) • [📥 PDF](https://arxiv.org/pdf/2607.19747)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Rubric4Setwise/Rubric4Setwise)

> As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation. Yet existing evaluation systems remain confined to scoring documents independently and...

</details>

<details>
<summary><b>7. Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Utkarsh Mishra, Jeonghwan Kim, Chahit Jain, Shivansh Patel, Dwipz

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.13429) • [📄 arXiv](https://arxiv.org/abs/2607.13429) • [📥 PDF](https://arxiv.org/pdf/2607.13429)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dwipddalal/Anchor-Align)

> TL;DR. Behavior cloning (BC) finetuning slowly overwrites the pretrained VLM representations a VLA relies on for visual and semantic generalization. Anchor-Align adds two objectives to standard BC: Vision-Language Anchoring (layer-wise distillatio...

</details>

<details>
<summary><b>8. FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hao Liu, Zhiying Wen, Ye Huang, Chenghuan Huang, Hao Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16190) • [📄 arXiv](https://arxiv.org/abs/2607.16190) • [📥 PDF](https://arxiv.org/pdf/2607.16190)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Video Diffusion Transformers process long spatio-temporal sequences, making self-attention the main bottleneck in high-resolution video generation. Training-free sparse attention reduces this cost, but adaptive Top-p routing creates uneven per-hea...

</details>

<details>
<summary><b>9. Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Md Tanvirul Alam

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.19790) • [📄 arXiv](https://arxiv.org/abs/2607.19790) • [📥 PDF](https://arxiv.org/pdf/2607.19790)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/maveryn/trace)

> We introduce TRACE, a taxonomy-guided environment containing 1,000 deterministic visual-reasoning tasks across 11 domains. Training Qwen2.5-VL-3B and Qwen2.5-VL-7B on 64,000 TRACE instances improves their macro-average performance across 24 extern...

</details>

<details>
<summary><b>10. SLPO: Scaling Latent Reasoning via a Surrogate Policy</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Wenjie Li, Yongqi Li, Zhiyuan Liu, Runyang You

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.19691) • [📄 arXiv](https://arxiv.org/abs/2607.19691) • [📥 PDF](https://arxiv.org/pdf/2607.19691)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ModalityDance/SLPO)

> No abstract available.

</details>

<details>
<summary><b>11. Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hiskias Dingeto

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.20379) • [📄 arXiv](https://arxiv.org/abs/2607.20379) • [📥 PDF](https://arxiv.org/pdf/2607.20379)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Reconstruction is widely used to evaluate natural-language explanations of hidden activations, but does a high reconstruction score actually mean the explanation’s specific claims are true? We find that it does not. On a released Qwen-2.5-7B verba...

</details>

<details>
<summary><b>12. G-MAD: A Game-Based Data Generation Framework for Multi-View RGB-T Aerial Object Detection</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Moongu Jeon, Namhoon Jung, Dongho Yoon, JongHyun Park, Yechan Kim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.19942) • [📄 arXiv](https://arxiv.org/abs/2607.19942) • [📥 PDF](https://arxiv.org/pdf/2607.19942)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/unique-chan/G-MAD)

> No abstract available.

</details>

<details>
<summary><b>13. SeededGrasp: Language-Guided Grasping in Complex Scenes with Multiple Embodiments</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Maria Attarian, Jasper Gerigk, Raymond Wang, Gurpreet Singh Mukker, Yang Xu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.20207) • [📄 arXiv](https://arxiv.org/abs/2607.20207) • [📥 PDF](https://arxiv.org/pdf/2607.20207)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/uoft-isl/SeededGrasp)

> No abstract available.

</details>

<details>
<summary><b>14. ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Seon Joo Kim, Gim Hee Lee, Mijin Yoo, Jeonghwan Cho, Cho In

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.20417) • [📄 arXiv](https://arxiv.org/abs/2607.20417) • [📥 PDF](https://arxiv.org/pdf/2607.20417)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 14 |
| 📅 Today | [`2026-07-23.json`](data/daily/2026-07-23.json) | 14 |
| 📆 This Week | [`2026-W29.json`](data/weekly/2026-W29.json) | 69 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 425 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-23 | 14 | [View JSON](data/daily/2026-07-23.json) |
| 📄 2026-07-22 | 19 | [View JSON](data/daily/2026-07-22.json) |
| 📄 2026-07-21 | 20 | [View JSON](data/daily/2026-07-21.json) |
| 📄 2026-07-20 | 16 | [View JSON](data/daily/2026-07-20.json) |
| 📄 2026-07-19 | 29 | [View JSON](data/daily/2026-07-19.json) |
| 📄 2026-07-18 | 29 | [View JSON](data/daily/2026-07-18.json) |
| 📄 2026-07-17 | 20 | [View JSON](data/daily/2026-07-17.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W29 | 69 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |
| 📅 2026-W27 | 133 | [View JSON](data/weekly/2026-W27.json) |
| 📅 2026-W26 | 165 | [View JSON](data/weekly/2026-W26.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 425 | [View JSON](data/monthly/2026-07.json) |
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
