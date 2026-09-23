<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-18-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7496+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">60</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">516</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7496+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 23, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. RULER: Instance-aware Rubric Rewards for SVG Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25270) • [📄 arXiv](https://arxiv.org/abs/2609.25270) • [📥 PDF](https://arxiv.org/pdf/2609.25270)

**💻 Code:** [⭐ Code](https://github.com/ant-research/RULER) • [⭐ Code](https://github.com/huggingface)

> Project Page: https://hangyuran.github.io/RULER/ Code: Will be released at https://github.com/ant-research/RULER

</details>

<details>
<summary><b>2. GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation</b> ⭐ 120</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24981) • [📄 arXiv](https://arxiv.org/abs/2609.24981) • [📥 PDF](https://arxiv.org/pdf/2609.24981)

**💻 Code:** [⭐ Code](https://github.com/TencentARC/GAE-GeometricAutoEncoder) • [⭐ Code](https://github.com/huggingface)

> We introduce GAE — Geometry-Native Autoencoder, which enables video generation directly in a geometry-native latent space. Built from geometry foundation model features, this compact representation serves as a shared space for perception and gener...

</details>

<details>
<summary><b>3. All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24058) • [📄 arXiv](https://arxiv.org/abs/2609.24058) • [📥 PDF](https://arxiv.org/pdf/2609.24058)

**💻 Code:** [⭐ Code](https://github.com/YesianRohn/ScriptMoE) • [⭐ Code](https://github.com/huggingface)

> All-in-one multilingual scene text recognition with a script-aware sparse MoE: top-2 script-aligned experts plus a shared expert, trained on TextMuSS-10M (10 scripts, 229 languages). 82.06% on TextMuSS-Bench; CC-OCR F1 65.71% → 80.89%.

</details>

<details>
<summary><b>4. The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25804) • [📄 arXiv](https://arxiv.org/abs/2609.25804) • [📥 PDF](https://arxiv.org/pdf/2609.25804)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wbopan/tastebench)

> Hi all, author here 👋 We study the taste of LLM agents: their ability to pick the better direction at a decision fork before the outcome is visible. 🔹 Taste-Bench : 502 decision forks mined automatically from SWE-bench Pro and METR AI R&D trajecto...

</details>

<details>
<summary><b>5. Circuit Hypernetworks for Quantum-Augmented Diffusion Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24657) • [📄 arXiv](https://arxiv.org/abs/2609.24657) • [📥 PDF](https://arxiv.org/pdf/2609.24657)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Language models can be adapted by changing the computations applied to individual tokens. Quantum circuits offer one such approach, but evaluating wider circuits inside a large model can be computationally demanding. Here we introduce HyperQ, whic...

</details>

<details>
<summary><b>6. Bellman Policy Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.15987) • [📄 arXiv](https://arxiv.org/abs/2609.15987) • [📥 PDF](https://arxiv.org/pdf/2609.15987)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Bellman Policy Optimization (BPO) is a critic-free policy optimization method derived from Policy Mirror Descent (PMD) and the Bellman equations. For autoregressive generation with terminal rewards, we use the Bellman equations to reformulate PMD ...

</details>

<details>
<summary><b>7. StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.26774) • [📄 arXiv](https://arxiv.org/abs/2609.26774) • [📥 PDF](https://arxiv.org/pdf/2609.26774)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Vector Quantization (VQ) is fundamental to discrete visual tokenizers that power modern autoregressive and masked image generation models. While recent shared-projection codebook methods have substantially advanced codebook utilization, training s...

</details>

<details>
<summary><b>8. From Pattern Recognizers to Personalized Companions: A Survey of Large Language Models in Mental Health</b> ⭐ 126</summary>

<br/>

**👥 Authors:** Chiyuan Ma, Yingjian Zou, Qianning Wang, Yucheng Zhou, GMLHUHE

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25186) • [📄 arXiv](https://arxiv.org/abs/2609.25186) • [📥 PDF](https://arxiv.org/pdf/2609.25186)

**💻 Code:** [⭐ Code](https://github.com/Emo-gml/Awesome-Mental-Health-LLMs) • [⭐ Code](https://github.com/huggingface)

> 💌

</details>

<details>
<summary><b>9. Ovis-Embedding: Pushing the Frontiers of Universal Omni-Modal Embeddings</b> ⭐ 19</summary>

<br/>

**👥 Authors:** Embedding Team

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25165) • [📄 arXiv](https://arxiv.org/abs/2609.25165) • [📥 PDF](https://arxiv.org/pdf/2609.25165)

**💻 Code:** [⭐ Code](https://github.com/ATH-MaaS/Ovis-Omni-Embedding) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.26796) • [📄 arXiv](https://arxiv.org/abs/2609.26796) • [📥 PDF](https://arxiv.org/pdf/2609.26796)

**💻 Code:** [⭐ Code](https://github.com/VILA-Lab/Flash-dLLM) • [⭐ Code](https://github.com/huggingface)

> Problem: KV caching and parallel decoding in diffusion LLMs are usually studied separately, and repeated KV-cache reads and writes make inference memory-bound, which limits real speedups. Flash-Cache: A fused Triton kernel combines QKV projection,...

</details>

<details>
<summary><b>11. Lean Pool: An AI-Maintained Archive of Formalized Mathematics</b> ⭐ 99</summary>

<br/>

**👥 Authors:** Vasily Ilin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25199) • [📄 arXiv](https://arxiv.org/abs/2609.25199) • [📥 PDF](https://arxiv.org/pdf/2609.25199)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Vilin97/lean-pool)

> Lean Pool the largest curated repository of formalized mathematics. It is grown, maintained and optimized by AI agents.

</details>

<details>
<summary><b>12. Emergent Collusion in Long-Horizon LLM Agent Interaction</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24967) • [📄 arXiv](https://arxiv.org/abs/2609.24967) • [📥 PDF](https://arxiv.org/pdf/2609.24967)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SALT-NLP/agent-collusion)

> This work studies whether collusion (a joint instruction violation driven by inter-agent behavioral influence) can emerge naturally when LLM agents interact repeatedly over long horizons. Across 10 models, it finds that collusion emerges in 94% of...

</details>

<details>
<summary><b>13. Recursive self-improvement of AI research agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.26457) • [📄 arXiv](https://arxiv.org/abs/2609.26457) • [📥 PDF](https://arxiv.org/pdf/2609.26457)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Blaming Across the Aisle: Political Contrasting and Blame Attribution in the Danish Parliament</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.26346) • [📄 arXiv](https://arxiv.org/abs/2609.26346) • [📥 PDF](https://arxiv.org/pdf/2609.26346)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Lundsfryd/BlameBERT)

> model: https://huggingface.co/Lundsfryd/BlameBERT dataset: https://huggingface.co/datasets/runetrust/blame-folketinget-dk

</details>

<details>
<summary><b>15. Geometric and Semantic Coupling for Interaction Understanding in 3D Scenes</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Xingyi Yang, Hanyang Kong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25247) • [📄 arXiv](https://arxiv.org/abs/2609.25247) • [📥 PDF](https://arxiv.org/pdf/2609.25247)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HyoKong/Segment-Snap)

> A door and its handle tell a shared story. We use their physical relationship to understand what moves, how it moves, and where to interact.

</details>

<details>
<summary><b>16. RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25636) • [📄 arXiv](https://arxiv.org/abs/2609.25636) • [📥 PDF](https://arxiv.org/pdf/2609.25636)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AutoLab-SAI-SJTU/RoboFollow)

> Paper accepted by CoRL 2026 RoboFollow is a simulation benchmark built on RoboTwin for evaluating instruction-conditioned manipulation by embodied agents. Multiple tasks share the same scene configuration, requiring policies to use language to sel...

</details>

<details>
<summary><b>17. ImIR: Image-Instruction Tuning for All-in-One Image Restoration</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Nasrin Rahimi, Yunus Bilge Kurt, Mısra Yavuz, Görkay Aydemir, suleymanaslan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25267) • [📄 arXiv](https://arxiv.org/abs/2609.25267) • [📥 PDF](https://arxiv.org/pdf/2609.25267)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/suleymanaslan/imir)

> ImIR: Image-Instruction Tuning for All-in-One Image Restoration — ACCV 2026 ImIR adapts a pretrained image-editing model to six restoration tasks: low-light enhancement, deraining, dehazing, deblurring, denoising, and JPEG artifact removal. Its ta...

</details>

<details>
<summary><b>18. ALPINE: Adaptive Localization for Parameter- and Sample-Efficient Few-Shot Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** NJ50

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.22323) • [📄 arXiv](https://arxiv.org/abs/2609.22323) • [📥 PDF](https://arxiv.org/pdf/2609.22323)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NeerajYadav-coder/alpine-fewshot)

> ALPINE is an ultra-lightweight few-shot image classification architecture designed for parameter- and sample-efficient learning. It combines fixed Gabor edge-energy guidance with a windowed, content-adaptive patch locator. Under a strictly matched...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 18 |
| 📅 Today | [`2026-09-23.json`](data/daily/2026-09-23.json) | 18 |
| 📆 This Week | [`2026-W38.json`](data/weekly/2026-W38.json) | 60 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 516 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-23 | 18 | [View JSON](data/daily/2026-09-23.json) |
| 📄 2026-09-22 | 21 | [View JSON](data/daily/2026-09-22.json) |
| 📄 2026-09-21 | 21 | [View JSON](data/daily/2026-09-21.json) |
| 📄 2026-09-20 | 24 | [View JSON](data/daily/2026-09-20.json) |
| 📄 2026-09-19 | 24 | [View JSON](data/daily/2026-09-19.json) |
| 📄 2026-09-18 | 19 | [View JSON](data/daily/2026-09-18.json) |
| 📄 2026-09-17 | 18 | [View JSON](data/daily/2026-09-17.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W38 | 60 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 516 | [View JSON](data/monthly/2026-09.json) |
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
