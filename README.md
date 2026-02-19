<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-25-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-2347+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">25</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">133</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">828</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">2347+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** February 19, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** tlenusik, Olegario228, therem, andreuka18, AntonKorznikov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14111) • [📄 arXiv](https://arxiv.org/abs/2602.14111) • [📥 PDF](https://arxiv.org/pdf/2602.14111)

> TL;DR: SAEs might not actually be learning meaningful features - they're barely better than random baselines. We run two experiments: (1) On synthetic data with known ground-truth features, SAEs achieve 71% explained variance but recover only ~9% ...

</details>

<details>
<summary><b>2. SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks</b> ⭐ 413</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12670) • [📄 arXiv](https://arxiv.org/abs/2602.12670) • [📥 PDF](https://arxiv.org/pdf/2602.12670)

**💻 Code:** [⭐ Code](https://github.com/benchflow-ai/skillsbench)

> GitHub: https://github.com/benchflow-ai/skillsbench Website: https://skillsbench.ai/

</details>

<details>
<summary><b>3. GLM-5: from Vibe Coding to Agentic Engineering</b> ⭐ 1.1k</summary>

<br/>

**👥 Authors:** wangcunxiang, yitianlian, Stanislas, zxdu20, think2try

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15763) • [📄 arXiv](https://arxiv.org/abs/2602.15763) • [📥 PDF](https://arxiv.org/pdf/2602.15763)

**💻 Code:** [⭐ Code](https://github.com/zai-org/GLM-5)

> So excited to see new SOTA llm! Qwen3.5 is not alone!

</details>

<details>
<summary><b>4. Does Socialization Emerge in AI Agent Society? A Case Study of Moltbook</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14299) • [📄 arXiv](https://arxiv.org/abs/2602.14299) • [📥 PDF](https://arxiv.org/pdf/2602.14299)

**💻 Code:** [⭐ Code](https://github.com/MingLiiii/Moltbook_Socialization)

> Does Socialization Emerge in AI Agent Society? A Case Study of Moltbook

</details>

<details>
<summary><b>5. UniT: Unified Multimodal Chain-of-Thought Test-time Scaling</b> ⭐ 0</summary>

<br/>

**👥 Authors:** daixl1992, Ziqi, Jetp, haoyum1997, liangyuch

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12279) • [📄 arXiv](https://arxiv.org/abs/2602.12279) • [📥 PDF](https://arxiv.org/pdf/2602.12279)

> UniT framework enables unified multimodal models to perform iterative reasoning and refinement through chain-of-thought test-time scaling, improving both generation and understanding capabilities.

</details>

<details>
<summary><b>6. ResearchGym: Evaluating Language Model Agents on Real-World AI Research</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Arman Cohan, Manasi Patwardhan, anikethh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15112) • [📄 arXiv](https://arxiv.org/abs/2602.15112) • [📥 PDF](https://arxiv.org/pdf/2602.15112)

**💻 Code:** [⭐ Code](https://github.com/Anikethh/ResearchGym)

> A benchmark and execution environment for evaluating LLM agents on the full arc for closed-loop research, through ideation, implementation and autonomous improvement . We find that LLMs can rarely beat strong human baselines and struggle to reliab...

</details>

<details>
<summary><b>7. jina-embeddings-v5-text: Task-Targeted Embedding Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15547) • [📄 arXiv](https://arxiv.org/abs/2602.15547) • [📥 PDF](https://arxiv.org/pdf/2602.15547)

> our 5th gen of jina embeddings

</details>

<details>
<summary><b>8. Revisiting the Platonic Representation Hypothesis: An Aristotelian View</b> ⭐ 10</summary>

<br/>

**👥 Authors:** Maria Brbić, Shuo Wen, FabianGroeger

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14486) • [📄 arXiv](https://arxiv.org/abs/2602.14486) • [📥 PDF](https://arxiv.org/pdf/2602.14486)

**💻 Code:** [⭐ Code](https://github.com/mlbio-epfl/aristotelian)

> Are neural nets across modalities really converging to the same representation as they scale, as the Platonic Representation Hypothesis suggests? We show that  common representational similarity metrics are confounded by network width & depth. We ...

</details>

<details>
<summary><b>9. Understanding vs. Generation: Navigating Optimization Dilemma in Multimodal Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Liwei Wang, Di He, Shuyang Gu, Mendel192, sen-ye

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15772) • [📄 arXiv](https://arxiv.org/abs/2602.15772) • [📥 PDF](https://arxiv.org/pdf/2602.15772)

**💻 Code:** [⭐ Code](https://github.com/sen-ye/R3)

> Current research in multimodal models faces a key challenge where enhancing generative capabilities often comes at the expense of understanding, and vice versa. We analyzed this trade-off and identify the primary cause might be the potential confl...

</details>

<details>
<summary><b>10. On Surprising Effectiveness of Masking Updates in Adaptive Optimizers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15322) • [📄 arXiv](https://arxiv.org/abs/2602.15322) • [📥 PDF](https://arxiv.org/pdf/2602.15322)

> Randomly masking parameter updates in adaptive optimizers yields curvature-regularization; Magma, momentum-aligned masking, is a drop-in that improves LLM perplexity (about 19% vs Adam, 9% vs Muon) with minimal overhead.

</details>

<details>
<summary><b>11. COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15200) • [📄 arXiv](https://arxiv.org/abs/2602.15200) • [📥 PDF](https://arxiv.org/pdf/2602.15200)

> No abstract available.

</details>

<details>
<summary><b>12. Panini: Continual Learning in Token Space via Structured Memory</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vwani Roychowdhury, Chenda Duan, Mehmet Yigit Turali, Pavan Holur, Shreyas Rajesh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15156) • [📄 arXiv](https://arxiv.org/abs/2602.15156) • [📥 PDF](https://arxiv.org/pdf/2602.15156)

**💻 Code:** [⭐ Code](https://github.com/roychowdhuryresearch/gsw-memory)

> Panini introduces a non-parametric continual learning framework where an LLM's knowledge grows not by updating weights, but by structuring each new document into a Generative Semantic Workspace (GSW) — an entity- and event-aware network of QA pair...

</details>

<details>
<summary><b>13. TAROT: Test-driven and Capability-adaptive Curriculum Reinforcement Fine-tuning for Code Generation with Large Language Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Jiasi Shen, Sayak Paul, Fan Wang, Juyong Jiang, chansung

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15449) • [📄 arXiv](https://arxiv.org/abs/2602.15449) • [📥 PDF](https://arxiv.org/pdf/2602.15449)

**💻 Code:** [⭐ Code](https://github.com/deep-diver/TAROT)

> https://github.com/deep-diver/TAROT

</details>

<details>
<summary><b>14. STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zeyu He, UestcJay, KehuaSheng, zzzzl-h, ShiqiLiu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15620) • [📄 arXiv](https://arxiv.org/abs/2602.15620) • [📥 PDF](https://arxiv.org/pdf/2602.15620)

> STAPO stabilizes RL for LLMs by masking spurious token updates that dominate gradients, improving entropy stability and reasoning performance.

</details>

<details>
<summary><b>15. Visual Persuasion: What Influences Decisions of Vision-Language Models?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Pattie Maes, nikhilsingh, pranavmr, mcherep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15278) • [📄 arXiv](https://arxiv.org/abs/2602.15278) • [📥 PDF](https://arxiv.org/pdf/2602.15278)

> Treats VLM visual choices as latent utility and reveals preferences via edited images to map visual factors shaping decisions, enabling interpretability, auditing, and governance of image-based AI agents.

</details>

<details>
<summary><b>16. The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15382) • [📄 arXiv](https://arxiv.org/abs/2602.15382) • [📥 PDF](https://arxiv.org/pdf/2602.15382)

**💻 Code:** [⭐ Code](https://github.com/xz-liu/heterogeneous-latent-mas)

> This is an ongoing project. We are actively working on improving the performance, and will include more experiments, baselines, and analyses in the near future. Also, the artifacts used in the preprint (trained codec checkpoints) will be released ...

</details>

<details>
<summary><b>17. Prescriptive Scaling Reveals the Evolution of Language Model Capabilities</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sham Kakade, Jikai Jin, vsyrgk, hlzhang109

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15327) • [📄 arXiv](https://arxiv.org/abs/2602.15327) • [📥 PDF](https://arxiv.org/pdf/2602.15327)

> We introduce prescriptive scaling, a framework for predicting the attainable downstream performance of language models given a fixed pre-training compute budget. Rather than modeling average trends, we estimate high-quantile capability boundaries ...

</details>

<details>
<summary><b>18. A Trajectory-Based Safety Audit of Clawdbot (OpenClaw)</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14364) • [📄 arXiv](https://arxiv.org/abs/2602.14364) • [📥 PDF](https://arxiv.org/pdf/2602.14364)

**💻 Code:** [⭐ Code](https://github.com/tychenn/clawdbot_report)

> We present a trajectory-based safety audit of Clawdbot (OpenClaw), a self-hosted tool-using AI agent. We evaluate 34 test cases across 6 risk dimensions and find a non-uniform safety profile (58.9% overall pass rate): the agent handles well-scoped...

</details>

<details>
<summary><b>19. HLE-Verified: A Systematic Verification and Structured Revision of Humanity's Last Exam</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaogang Li, Boyu Yang, Jinghang Wang, Zhihai Wang, skylenage

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13964) • [📄 arXiv](https://arxiv.org/abs/2602.13964) • [📥 PDF](https://arxiv.org/pdf/2602.13964)

> Humanity's Last Exam (HLE) has become a widely used benchmark for evaluating frontier large language models on challenging, multi-domain questions. However, community-led analyses have raised concerns that HLE contains a non-trivial number of nois...

</details>

<details>
<summary><b>20. Learning Native Continuation for Action Chunking Flow Policies</b> ⭐ 0</summary>

<br/>

**👥 Authors:** leo-guo, piiswrong, Yingdong-Hu, psdem, lyfeng001

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12978) • [📄 arXiv](https://arxiv.org/abs/2602.12978) • [📥 PDF](https://arxiv.org/pdf/2602.12978)

> Action chunking enables Vision Language Action (VLA) models to run in real time, but naive chunked execution often exhibits discontinuities at chunk boundaries. Real-Time Chunking (RTC) alleviates this issue but is external to the policy, leading ...

</details>

<details>
<summary><b>21. Causal-JEPA: Learning World Models through Object-Level Latent Interventions</b> ⭐ 28</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11389) • [📄 arXiv](https://arxiv.org/abs/2602.11389) • [📥 PDF](https://arxiv.org/pdf/2602.11389)

**💻 Code:** [⭐ Code](https://github.com/galilai-group/cjepa)

> Code: https://github.com/galilai-group/cjepa

</details>

<details>
<summary><b>22. ClinAlign: Scaling Healthcare Alignment from Clinician Preference</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Lei Liu, Benyou, dannygjj, Xidong, ShiweiLyu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.09653) • [📄 arXiv](https://arxiv.org/abs/2602.09653) • [📥 PDF](https://arxiv.org/pdf/2602.09653)

**💻 Code:** [⭐ Code](https://github.com/AQ-MedAI/ClinAlign)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Automated Rubrics for Reliable Evaluation of Medical Dialogue Systems (2026...

</details>

<details>
<summary><b>23. Geometry-Aware Rotary Position Embedding for Consistent Video World Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.07854) • [📄 arXiv](https://arxiv.org/abs/2602.07854) • [📥 PDF](https://arxiv.org/pdf/2602.07854)

> No abstract available.

</details>

<details>
<summary><b>24. Detecting Overflow in Compressed Token Representations for Retrieval-Augmented Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12235) • [📄 arXiv](https://arxiv.org/abs/2602.12235) • [📥 PDF](https://arxiv.org/pdf/2602.12235)

> We address  an important yet underexplored problem in soft compression for retrieval-augmented generation: detecting when compressed token representations lose task-relevant information. We introduce the concept of token overflow to describe the r...

</details>

<details>
<summary><b>25. How Much Reasoning Do Retrieval-Augmented Models Add beyond LLMs? A Benchmarking Framework for Multi-Hop Inference over Hybrid Knowledge</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.10210) • [📄 arXiv](https://arxiv.org/abs/2602.10210) • [📥 PDF](https://arxiv.org/pdf/2602.10210)

**💻 Code:** [⭐ Code](https://github.com/junhongmit/HybridRAG-Bench)

> Modern LLM systems increasingly rely on retrieval-augmented generation (RAG) and knowledge-graph-augmented reasoning (KG-RAG) to handle knowledge-intensive tasks. But how much reasoning do these systems truly add beyond the base LLM’s parametric k...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 25 |
| 📅 Today | [`2026-02-19.json`](data/daily/2026-02-19.json) | 25 |
| 📆 This Week | [`2026-W07.json`](data/weekly/2026-W07.json) | 133 |
| 🗓️ This Month | [`2026-02.json`](data/monthly/2026-02.json) | 828 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-02-19 | 25 | [View JSON](data/daily/2026-02-19.json) |
| 📄 2026-02-18 | 35 | [View JSON](data/daily/2026-02-18.json) |
| 📄 2026-02-17 | 32 | [View JSON](data/daily/2026-02-17.json) |
| 📄 2026-02-16 | 41 | [View JSON](data/daily/2026-02-16.json) |
| 📄 2026-02-15 | 41 | [View JSON](data/daily/2026-02-15.json) |
| 📄 2026-02-14 | 41 | [View JSON](data/daily/2026-02-14.json) |
| 📄 2026-02-13 | 47 | [View JSON](data/daily/2026-02-13.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W07 | 133 | [View JSON](data/weekly/2026-W07.json) |
| 📅 2026-W06 | 293 | [View JSON](data/weekly/2026-W06.json) |
| 📅 2026-W05 | 357 | [View JSON](data/weekly/2026-W05.json) |
| 📅 2026-W04 | 214 | [View JSON](data/weekly/2026-W04.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-02 | 828 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |
| 🗓️ 2025-12 | 787 | [View JSON](data/monthly/2025-12.json) |

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
