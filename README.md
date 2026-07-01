<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-22-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5710+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">22</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">69</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">22</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5710+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 01, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Orca: The World is in Your Mind</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yihao Wang, tzh21, HuaihaiLyu, syq1105, cmyopu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30534) • [📄 arXiv](https://arxiv.org/abs/2606.30534) • [📥 PDF](https://arxiv.org/pdf/2606.30534)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Orca: An initial instantiation of a general world foundation model English version of video demo

</details>

<details>
<summary><b>2. Dockerless: Environment-Free Program Verifier for Coding Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.28436) • [📄 arXiv](https://arxiv.org/abs/2606.28436) • [📥 PDF](https://arxiv.org/pdf/2606.28436)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Try environment-free RL!

</details>

<details>
<summary><b>3. BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding</b> ⭐ 20</summary>

<br/>

**👥 Authors:** Xin Xiao, Mingqiao Mo, Yong Wang, Yiming Hu, Hao Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31315) • [📄 arXiv](https://arxiv.org/abs/2606.31315) • [📥 PDF](https://arxiv.org/pdf/2606.31315)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AMAP-ML/BlockPilot)

> BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding Github: https://github.com/AMAP-ML/BlockPilot

</details>

<details>
<summary><b>4. DOPD: Dual On-policy Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Guibin Zhang, Qingyi Si, Gen Li, Xinlei Yu, DogNeverSleep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30626) • [📄 arXiv](https://arxiv.org/abs/2606.30626) • [📥 PDF](https://arxiv.org/pdf/2606.30626)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DOPD: Dual On-policy Distillation

</details>

<details>
<summary><b>5. GEAR: Guided End-to-End AutoRegression for Image Synthesis</b> ⭐ 33</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.32039) • [📄 arXiv](https://arxiv.org/abs/2606.32039) • [📥 PDF](https://arxiv.org/pdf/2606.32039)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent-Hunyuan/GEAR)

> 📄 Paper: https://arxiv.org/abs/2606.32039 💻 Code: https://github.com/Tencent-Hunyuan/GEAR 🤗 Models: https://huggingface.co/collections/BinLin203 🏠 Homepage: https://linb203.github.io/gear [1/6] 🚨 Stop freezing your tokenizers! Visual Autoregressiv...

</details>

<details>
<summary><b>6. MemLearner: Learning to Query Context memory for Video World Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kaiyi Huang, Yiran Qin, Jianhong Bai, Jianxiong Gao, Jiwen Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31734) • [📄 arXiv](https://arxiv.org/abs/2606.31734) • [📥 PDF](https://arxiv.org/pdf/2606.31734)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>7. Multi-Block Diffusion Language Models</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.29215) • [📄 arXiv](https://arxiv.org/abs/2606.29215) • [📥 PDF](https://arxiv.org/pdf/2606.29215)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SJTU-DENG-Lab/mbd-lms) • [⭐ Code](https://github.com/SJTU-DENG-Lab/Diffulex)

> We introduce Multi-Block Diffusion Language Models (MBD-LMs), a unified framework that bridges the training-inference gap for practical multi-block diffusion in block diffusion language models (BD-LMs). We identify that existing Teacher Forcing an...

</details>

<details>
<summary><b>8. Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.29082) • [📄 arXiv](https://arxiv.org/abs/2606.29082) • [📥 PDF](https://arxiv.org/pdf/2606.29082)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Open-Galapagos/evolution-fine-tuning)

> Would experience designing faster GPU kernels also help close in on a long-standing open mathematical conjecture? Large Language Models (LLMs) integrated into evolutionary search have recently produced state-of-the-art solutions on optimization ta...

</details>

<details>
<summary><b>9. RedVox: Safety and Fairness Gaps in Speech Models Across Languages</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.26968) • [📄 arXiv](https://arxiv.org/abs/2606.26968) • [📥 PDF](https://arxiv.org/pdf/2606.26968)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🌍 Speech AI is going multilingual—but its safety evaluations largely aren't. We present RedVox, a multilingual benchmark for speech model safety and fairness built from real spoken interactions across five languages. Evaluating eight leading model...

</details>

<details>
<summary><b>10. Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Eunbyung Park, Jiwoo Lee, Subin Jeon, In Cho, mynameisyoomimi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.29513) • [📄 arXiv](https://arxiv.org/abs/2606.29513) • [📥 PDF](https://arxiv.org/pdf/2606.29513)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A feed-forward framework decomposes 3D scenes into instance-structured token groups from multi-view images, enabling direct object-level reconstruction, segmentation, and manipulation without 3D annotations.

</details>

<details>
<summary><b>11. Little Brains, Big Feats: Exploring Compact Language Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30062) • [📄 arXiv](https://arxiv.org/abs/2606.30062) • [📥 PDF](https://arxiv.org/pdf/2606.30062)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SibNN/SLM-RAG-EVAL)

> Can small language models be strong enough for practical RAG generation without GPUs? We benchmark 17 compact language models from 1B to 8B parameters as generators in Russian-language Retrieval-Augmented Generation systems. All candidate models w...

</details>

<details>
<summary><b>12. PolyFlow: Continuous Topology Embedding Flow Matching for Artist-style Mesh Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30673) • [📄 arXiv](https://arxiv.org/abs/2606.30673) • [📥 PDF](https://arxiv.org/pdf/2606.30673)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>13. DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Alex Jinpeng Wang, Dongxing Mao, Yilin Wang, Yizhen Gao, Siyu Yan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31537) • [📄 arXiv](https://arxiv.org/abs/2606.31537) • [📥 PDF](https://arxiv.org/pdf/2606.31537)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation

</details>

<details>
<summary><b>14. Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.32032) • [📄 arXiv](https://arxiv.org/abs/2606.32032) • [📥 PDF](https://arxiv.org/pdf/2606.32032)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yale-nlp/RLMF)

> Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, f...

</details>

<details>
<summary><b>15. Xiaomi-GUI-0 Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31410) • [📄 arXiv](https://arxiv.org/abs/2606.31410) • [📥 PDF](https://arxiv.org/pdf/2606.31410)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>16. AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Long Chen, Qifeng Chen, I Chieh Chen, Kien T. Pham

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30811) • [📄 arXiv](https://arxiv.org/abs/2606.30811) • [📥 PDF](https://arxiv.org/pdf/2606.30811)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hkust-longgroup/AVTok)

> AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation

</details>

<details>
<summary><b>17. PhotoQuilt: Training-Free Arbitrary-Resolution Photomosaics via Bootstrapped Tiled Denoising</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30968) • [📄 arXiv](https://arxiv.org/abs/2606.30968) • [📥 PDF](https://arxiv.org/pdf/2606.30968)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TLDR: PhotoQuilt is a training-free way to make photomosaics, big images where each tile is a convincing little picture on its own, yet together they form a coherent scene. It sketches the whole layout at low resolution first, then upscales and de...

</details>

<details>
<summary><b>18. BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Qihao Zheng, Shangquan Sun, Zhouheng Yao, Qirui Zhang, Haitao Wu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30319) • [📄 arXiv](https://arxiv.org/abs/2606.30319) • [📥 PDF](https://arxiv.org/pdf/2606.30319)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Modeling the bidirectional correspondence between external sensory stimuli and internal neural activity has emerged as a critical frontier in neuroscience. However, existing approaches predominantly treat brain encoding and decoding as isolated ta...

</details>

<details>
<summary><b>19. TerraDiT-Ω: Unified Spatial Control for Satellite Image Synthesis with Any Geospatial Primitive</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31029) • [📄 arXiv](https://arxiv.org/abs/2606.31029) • [📥 PDF](https://arxiv.org/pdf/2606.31029)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mvrl/TerraDiT)

> TerraDiT-Ω: Unified Spatial Control for Satellite Image Synthesis with Any Geospatial Primitive Accepted to ECCV 2026.

</details>

<details>
<summary><b>20. LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.30697) • [📄 arXiv](https://arxiv.org/abs/2606.30697) • [📥 PDF](https://arxiv.org/pdf/2606.30697)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/thotayogeswarreddy/Lumos)

> Current operating systems expose interfaces optimized for human users but not for AI agents. Humans benefit from pixels, icons, windows, visual grouping, mouse movement, and keyboard shortcuts; AI agents instead need compact semantic state, ground...

</details>

<details>
<summary><b>21. SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08671) • [📄 arXiv](https://arxiv.org/abs/2606.08671) • [📥 PDF](https://arxiv.org/pdf/2606.08671)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent/SkillHone)

> 🚀 Excited to share SkillHone, a harness for continual agent skill evolution through persistent decision history. The core idea is simple: agent skills should not only keep the final optimized artifact, but also preserve the decision history behind...

</details>

<details>
<summary><b>22. MuSViT: A Foundation Vision Model for Sheet Music Representation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31811) • [📄 arXiv](https://arxiv.org/abs/2606.31811) • [📥 PDF](https://arxiv.org/pdf/2606.31811)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OMR-PRAIG-UA-ES/MuSViT)

> Accepted at European Conference on Computer Vision (ECCV'26) Overview of MuSViT. MuSViT is pre-trained on diverse sheet music pages using Masked Autoencoders: patches are randomly masked and the model learns to reconstruct the missing content from...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 22 |
| 📅 Today | [`2026-07-01.json`](data/daily/2026-07-01.json) | 22 |
| 📆 This Week | [`2026-W26.json`](data/weekly/2026-W26.json) | 69 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 22 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-01 | 22 | [View JSON](data/daily/2026-07-01.json) |
| 📄 2026-06-30 | 32 | [View JSON](data/daily/2026-06-30.json) |
| 📄 2026-06-29 | 15 | [View JSON](data/daily/2026-06-29.json) |
| 📄 2026-06-28 | 25 | [View JSON](data/daily/2026-06-28.json) |
| 📄 2026-06-27 | 25 | [View JSON](data/daily/2026-06-27.json) |
| 📄 2026-06-26 | 18 | [View JSON](data/daily/2026-06-26.json) |
| 📄 2026-06-25 | 21 | [View JSON](data/daily/2026-06-25.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W26 | 69 | [View JSON](data/weekly/2026-W26.json) |
| 📅 2026-W25 | 155 | [View JSON](data/weekly/2026-W25.json) |
| 📅 2026-W24 | 194 | [View JSON](data/weekly/2026-W24.json) |
| 📅 2026-W23 | 247 | [View JSON](data/weekly/2026-W23.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 22 | [View JSON](data/monthly/2026-07.json) |
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
