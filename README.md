<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-24-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7606+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">24</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">24</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">626</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7606+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 28, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31620) • [📄 arXiv](https://arxiv.org/abs/2609.31620) • [📥 PDF](https://arxiv.org/pdf/2609.31620)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Hongyang-Du/FuseReg)

> FuseReg: Mitigating the Reconstruction–Generation Gap in RAEs Representation Autoencoders fuse features from multiple encoder layers into a shared latent space. However, reconstruction and generation prefer different parts of the hierarchy: Decode...

</details>

<details>
<summary><b>2. RayOrch: Programming and Executing Lineage-Controlled Multi-Grain Dataflows for Foundation-Model Data Preparation</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.18703) • [📄 arXiv](https://arxiv.org/abs/2609.18703) • [📥 PDF](https://arxiv.org/pdf/2609.18703)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenDCAI/RayOrch)

> We introduce RayOrch, a distributed data pipeline system for multimodal foundation model data preparation. Like Ray Data and Daft, it targets large scale data processing. RayOrch is designed for pipelines with multiple stages and levels of granula...

</details>

<details>
<summary><b>3. Block Sparse Attention with Log-Linear Complexity</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31093) • [📄 arXiv](https://arxiv.org/abs/2609.31093) • [📥 PDF](https://arxiv.org/pdf/2609.31093)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> arxiv.org/abs/2609.31093

</details>

<details>
<summary><b>4. InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kaiwen Song, Baole Fang, Zizun Li, Xingyu Miao, ghy0324

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31394) • [📄 arXiv](https://arxiv.org/abs/2609.31394) • [📥 PDF](https://arxiv.org/pdf/2609.31394)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>5. Tactile-JEPA: Topology-Aware Self-Supervised Representation Learning for Distributed Tactile Sensors</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Semen Budennyy, Andrey Sakhovskiy, Bosbobos, LizaKovtun

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24385) • [📄 arXiv](https://arxiv.org/abs/2609.24385) • [📥 PDF](https://arxiv.org/pdf/2609.24385)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/E-Kovtun/tactile)

> 🤖 Better robot touch starts with better representations. Introducing Tactile-JEPA : self-supervised learning for distributed tactile sensors that respects how sensing elements connect across the skin. By predicting masked embeddings at local and g...

</details>

<details>
<summary><b>6. Enhancing Photogrammetric Digital Surface Models with Pretrained Diffusion Models and Multimodal Conditioning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31199) • [📄 arXiv](https://arxiv.org/abs/2609.31199) • [📥 PDF](https://arxiv.org/pdf/2609.31199)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large-scale Digital Surface Models (DSMs) can be produced cost-effectively from satellite images via stereo-photogrammetry. However, the resulting 3D maps are often contaminated by noise, outliers, and voids. On the other hand, aerial LiDAR provid...

</details>

<details>
<summary><b>7. FoMo: Forking Moment in Generative Trajectory as a Perceptual Distance</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.25716) • [📄 arXiv](https://arxiv.org/abs/2609.25716) • [📥 PDF](https://arxiv.org/pdf/2609.25716)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/JHLew/FoMo)

> NeurIPS 2026

</details>

<details>
<summary><b>8. Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.30216) • [📄 arXiv](https://arxiv.org/abs/2609.30216) • [📥 PDF](https://arxiv.org/pdf/2609.30216)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/godxue1/Jev_in_the_wild)

> First large-scale, data-driven survey and analysis of the Jev decision model, covering 2,170 GitHub projects across real-world applications, usage patterns, and its emerging ecosystem.

</details>

<details>
<summary><b>9. TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.30222) • [📄 arXiv](https://arxiv.org/abs/2609.30222) • [📥 PDF](https://arxiv.org/pdf/2609.30222)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Existing point tracking models face a fundamental tradeoff: they can either track a sparse set of query points over long horizons, or track all points across only short clips. We introduce TrackEverything, a 3D point tracker that breaks this trade...

</details>

<details>
<summary><b>10. SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.29050) • [📄 arXiv](https://arxiv.org/abs/2609.29050) • [📥 PDF](https://arxiv.org/pdf/2609.29050)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SLCA-GRPO/SLCA-GRPO)

> Tool-calling RL often broadcasts one trajectory-level GRPO advantage across both tool-call and summary tokens, allowing summary rewards to distort tool decisions. SLCA-GRPO (Segment-Locked Credit Assignment) normalizes tool and summary rewards ind...

</details>

<details>
<summary><b>11. CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2601.06352) • [📄 arXiv](https://arxiv.org/abs/2601.06352) • [📥 PDF](https://arxiv.org/pdf/2601.06352)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> CARD combines cluster-level adaptation with reward-guided decoding for personalized text generation. It learns LoRA adapters for groups of users with shared stylistic patterns, then captures individual preferences through lightweight preference ve...

</details>

<details>
<summary><b>12. Do Implicit Personalization and Explicit Styles Conflict? PsPLUG: A Lightweight Plug-in for Balancing Personalization and Style in Customized LLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2601.06362) • [📄 arXiv](https://arxiv.org/abs/2601.06362) • [📥 PDF](https://arxiv.org/pdf/2601.06362)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> PsPLUG studies a tension in personalized LLMs: explicit style instructions can undermine the implicit user preferences a model has learned. The method learns a user-specific residual after accounting for the requested style, and lets users adjust ...

</details>

<details>
<summary><b>13. AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuan Yuan, Jin Mo Yang, Young Min Cho, Yusen Zhang, Raphael Shu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31590) • [📄 arXiv](https://arxiv.org/abs/2609.31590) • [📥 PDF](https://arxiv.org/pdf/2609.31590)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Game Arena: Strategic LLM Evaluation in Competitive Environments</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31473) • [📄 arXiv](https://arxiv.org/abs/2609.31473) • [📥 PDF](https://arxiv.org/pdf/2609.31473)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>15. IndicBankBench: Evaluating Safety and Reliability of Language Model Assistants in Indian Retail Banking</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.29167) • [📄 arXiv](https://arxiv.org/abs/2609.29167) • [📥 PDF](https://arxiv.org/pdf/2609.29167)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/npci/IndicBankBench)

> How do we tell whether a banking assistant handled a customer’s request correctly, rather than just producing a plausible final answer? We’re sharing IndicBankBench: 799 synthetic retail-banking cases across 20 primary axes, evaluated in a mock ba...

</details>

<details>
<summary><b>16. TRACE: Temporal Audit and Condition-aware Evaluation of Streaming Video Understanding</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.30670) • [📄 arXiv](https://arxiv.org/abs/2609.30670) • [📥 PDF](https://arxiv.org/pdf/2609.30670)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/om-ai-lab/trace-bench)

> Streaming video understanding requires models to interpret evidence as it arrives, yet current evaluations often report task scores without specifying when evidence becomes valid, how visual history is maintained, or how responses are triggered. T...

</details>

<details>
<summary><b>17. ZooWork-ShopRanker: An Open, Preference-Aligned E-Commerce Reranker</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ning Hu, Shuxuan Liu, Siqiao Xue

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31002) • [📄 arXiv](https://arxiv.org/abs/2609.31002) • [📥 PDF](https://arxiv.org/pdf/2609.31002)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Open rerankers trained for general web retrieval transfer imperfectly to e-commerce, where ranking decisions depend not only on topical relevance but also on user preferences, product constraints, and comparative product fit. These preference sign...

</details>

<details>
<summary><b>18. VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models</b> ⭐ 81</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04355) • [📄 arXiv](https://arxiv.org/abs/2609.04355) • [📥 PDF](https://arxiv.org/pdf/2609.04355)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/scy-v/VLA-Precision)

> arxiv:2609.04355

</details>

<details>
<summary><b>19. Evidence-Grounded Auditing of Identification Assumptions in Climate-Policy Causal Evaluations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ricardo Correia, Isabel M. Parra, Yong Xie, Yonghong Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.30867) • [📄 arXiv](https://arxiv.org/abs/2609.30867) • [📥 PDF](https://arxiv.org/pdf/2609.30867)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yonghongzhang-io/ARGUS)

> ARGUS audits the evidence that difference-in-differences studies report for their identification assumptions: it maps each paper onto an 11-dimension assumption–implication–evidence rubric, flags risk per dimension, and abstains when the evidence ...

</details>

<details>
<summary><b>20. Depth-adaptive Inference of Looped Language Models via Continuous Depth Batching</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09444) • [📄 arXiv](https://arxiv.org/abs/2608.09444) • [📥 PDF](https://arxiv.org/pdf/2608.09444)

**💻 Code:** [⭐ Code](https://github.com/kschwethelm/continuous-depth-batching) • [⭐ Code](https://github.com/huggingface)

> Ever wondered why LLMs are using the same forward pass and thus the same compute for every single token no matter how hard the prediction is? The solution: looped LMs can use less compute for "easy" tokens and more for "hard" ones. The problem: to...

</details>

<details>
<summary><b>21. Paragraph Boundaries Are Not White Space:Compression Depth as the Signature of Hierarchical Structure</b> ⭐ 0</summary>

<br/>

**👥 Authors:** ShuyangXiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23551) • [📄 arXiv](https://arxiv.org/abs/2609.23551) • [📥 PDF](https://arxiv.org/pdf/2609.23551)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ShuyangenFrance/hrope)

> Does a Transformer actually "see" paragraph structure, or just token distance? We use hierarchical RoPE (separate paragraph / sentence / token channels) and intervene on the paragraph coordinate while holding the token sequence fixed. Key finding:...

</details>

<details>
<summary><b>22. Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.28660) • [📄 arXiv](https://arxiv.org/abs/2609.28660) • [📥 PDF](https://arxiv.org/pdf/2609.28660)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tsadja/morphometric)

> One human demonstration. Any multi-fingered hand. Zero-shot sim-to-real visuomotor policy. All videos are 1x speed fully autonomous, and we include continuous, uncut trials.

</details>

<details>
<summary><b>23. MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.30837) • [📄 arXiv](https://arxiv.org/abs/2609.30837) • [📥 PDF](https://arxiv.org/pdf/2609.30837)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TURLEing/MOPD-Router)

> This work introduces MOPD-Router, a label-free framework that routes multi-teacher on-policy distillation signals at the token level; With ExpertAlign metric, it consistently outperforms prompt-level hard routing across two data regimes and studen...

</details>

<details>
<summary><b>24. BoundInk: Boundary-Aware Online Handwriting Generation</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.02103) • [📄 arXiv](https://arxiv.org/abs/2604.02103) • [📥 PDF](https://arxiv.org/pdf/2604.02103)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jinsu0000/cashg-official)

> Context-Aware Stylized Online Handwriting Generation

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 24 |
| 📅 Today | [`2026-09-28.json`](data/daily/2026-09-28.json) | 24 |
| 📆 This Week | [`2026-W39.json`](data/weekly/2026-W39.json) | 24 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 626 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-28 | 24 | [View JSON](data/daily/2026-09-28.json) |
| 📄 2026-09-27 | 22 | [View JSON](data/daily/2026-09-27.json) |
| 📄 2026-09-26 | 22 | [View JSON](data/daily/2026-09-26.json) |
| 📄 2026-09-25 | 18 | [View JSON](data/daily/2026-09-25.json) |
| 📄 2026-09-24 | 24 | [View JSON](data/daily/2026-09-24.json) |
| 📄 2026-09-23 | 18 | [View JSON](data/daily/2026-09-23.json) |
| 📄 2026-09-22 | 21 | [View JSON](data/daily/2026-09-22.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W39 | 24 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 626 | [View JSON](data/monthly/2026-09.json) |
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
