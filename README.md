<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-24-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9796+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">125</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">395</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9796+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 13, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.15777) • [📄 arXiv](https://arxiv.org/abs/2611.15777) • [📥 PDF](https://arxiv.org/pdf/2611.15777)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/holdrain/SO-Arena)

> SO-Arena benchmarks the capabilities and decision reliability of System One models across 11 domains, revealing that strong task performance does not guarantee stable decisions or recognition of missing correct options. Homepage: https://lichenlil...

</details>

<details>
<summary><b>2. BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14815) • [📄 arXiv](https://arxiv.org/abs/2611.14815) • [📥 PDF](https://arxiv.org/pdf/2611.14815)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> BirdDreams: A driving world model with accurate ego control and traffic that can react. BirdDreams is a driving world model that generates driving video and a bird’s-eye view of the scene from a single camera image.  It follows input ego trajector...

</details>

<details>
<summary><b>3. G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13004) • [📄 arXiv](https://arxiv.org/abs/2611.13004) • [📥 PDF](https://arxiv.org/pdf/2611.13004)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DAGroup-PKU/G-STAR)

> Discrete autoregressive models offer a scalable framework for image generation. However, they face a fundamental trade-off: long token sequences preserve representation quality but slow generation, while aggressive spatial compression reduces repr...

</details>

<details>
<summary><b>4. Duo: A Reciprocal World Model for Full-Duplex Interaction</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.15131) • [📄 arXiv](https://arxiv.org/abs/2611.15131) • [📥 PDF](https://arxiv.org/pdf/2611.15131)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/inclusionAI/Duo)

> arXiv: https://arxiv.org/abs/2611.15131 Homepage: https://duo-v1.github.io/ Github: https://github.com/inclusionAI/Duo Hugging Face Model: https://huggingface.co/collections/inclusionAI/duo-v1

</details>

<details>
<summary><b>5. PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16748) • [📄 arXiv](https://arxiv.org/abs/2611.16748) • [📥 PDF](https://arxiv.org/pdf/2611.16748)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DAGroup-PKU/PhysLoop)

> PhysLoop is a physics-aware harness for building controllable video training data and repairing physically inconsistent video at inference time. The project video shows how the harness works and presents examples of video generation and repair. Co...

</details>

<details>
<summary><b>6. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17167) • [📄 arXiv](https://arxiv.org/abs/2611.17167) • [📥 PDF](https://arxiv.org/pdf/2611.17167)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJU-REAL/decision-agents)

> Decision models output typed decisions (e.g., a probability over candidate actions), so the same model can act as an Actor (choose actions), a Judge (evaluate actions already taken), or a Teacher (score every action to provide step-level rewards f...

</details>

<details>
<summary><b>7. On the Design of Hyper-Connections: Simplification, Stability, and Scalability</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05984) • [📄 arXiv](https://arxiv.org/abs/2611.05984) • [📥 PDF](https://arxiv.org/pdf/2611.05984)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aHapBean/SimpleHC)

> We introduce SimpleHC, one of the fastest Hyper-Connections variants to date, reducing repeated memory access through a simpler design. It adds just 2.4% training overhead at the largest tested width while maintaining competitive performance with ...

</details>

<details>
<summary><b>8. TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17331) • [📄 arXiv](https://arxiv.org/abs/2611.17331) • [📥 PDF](https://arxiv.org/pdf/2611.17331)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NVlabs/DVSM)

> Test-time Baking (TTB) turns cross-view attention layers into fixed-size MLP layers at test time, each fit like a light field in latent space. Rendering then needs no 3D representation and costs the same at any number of input views, at the qualit...

</details>

<details>
<summary><b>9. Open Vision Banana: A Fully Open Recipe for Generative Visual Perception</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.15844) • [📄 arXiv](https://arxiv.org/abs/2611.15844) • [📥 PDF](https://arxiv.org/pdf/2611.15844)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenVisionBanana/OpenVisionBanana)

> A Fully Open Recipe for Generative Visual Perception

</details>

<details>
<summary><b>10. Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17060) • [📄 arXiv](https://arxiv.org/abs/2611.17060) • [📥 PDF](https://arxiv.org/pdf/2611.17060)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ropedia/Ropedia-Xperience-2)

> Introducing Xperience 2 from Ropedia: a gold standard for scaling Physical AI environments and behaviors. Real-robot data is expensive. DROID's 350 hours of demonstrations took 50 operators a full year, and a real robot can't retry a task the way ...

</details>

<details>
<summary><b>11. WorldDraft: If Code Builds the World, Can Video Models Just Render It?</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Chenfei Liao, Weilin Ruan, Wen-Jie Shu, Zhiyu Hou, Harold328

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16217) • [📄 arXiv](https://arxiv.org/abs/2611.16217) • [📥 PDF](https://arxiv.org/pdf/2611.16217)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/KevinHuge/WorldDraft)

> If Code Builds the World, Can Video Models Just Render It?

</details>

<details>
<summary><b>12. Factored One-sided Adam-Moment for Practical and Scalable SOAP</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16905) • [📄 arXiv](https://arxiv.org/abs/2611.16905) • [📥 PDF](https://arxiv.org/pdf/2611.16905)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/naver-ai/foam)

> We introduce FOAM, a lightweight SOAP variant that preconditions only the input side and factors the rotated second moment, halving SOAP’s optimizer state and removing one of its two eigen-decompositions. FOAM matches strong SOAP and Muon baseline...

</details>

<details>
<summary><b>13. UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16517) • [📄 arXiv](https://arxiv.org/abs/2611.16517) • [📥 PDF](https://arxiv.org/pdf/2611.16517)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can hybrid attention support both understanding and visual generation? UniSpark brings full attention and recurrent linear attention into a shared Mixture-of-Transformer-Experts backbone.

</details>

<details>
<summary><b>14. Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08318) • [📄 arXiv](https://arxiv.org/abs/2611.08318) • [📥 PDF](https://arxiv.org/pdf/2611.08318)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DAGroup-PKU/PyRUA-Lean/tree/RSIJudge)

> https://github.com/DAGroup-PKU/PyRUA-Lean/tree/RSIJudge

</details>

<details>
<summary><b>15. Agent-R^2: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08219) • [📄 arXiv](https://arxiv.org/abs/2611.08219) • [📥 PDF](https://arxiv.org/pdf/2611.08219)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJU-REAL/Agent-R2)

> Real productivity work means turning heterogeneous files (annual reports, spreadsheets, PDFs) into deliverables with the right format and evidence. LLM agents still struggle here: workflows are long, files are messy, and success criteria are fine-...

</details>

<details>
<summary><b>16. Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chu Wang, Ziyuan Wang, Genliang Zhu, chen-ai-researcher

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41453) • [📄 arXiv](https://arxiv.org/abs/2610.41453) • [📥 PDF](https://arxiv.org/pdf/2610.41453)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Tool timeouts can leave AI agents facing ambiguous tool outcomes and partial execution: an action may have failed, committed or remained in flight while other workflow steps have already completed. We formulate evidence-guided task recovery over a...

</details>

<details>
<summary><b>17. DeepStress: Stress-Testing Deep Search Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.13920) • [📄 arXiv](https://arxiv.org/abs/2607.13920) • [📥 PDF](https://arxiv.org/pdf/2607.13920)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! This is the first paper of my PhD, which I presented at the Workshop on Agent Behavior earlier this year at COLM! In this paper, we look at how we can use a simulated environment to test our search agents in "difficult" situations and...

</details>

<details>
<summary><b>18. Structured Confidence Perturbation via Fisher Geometry for Adversarial Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14046) • [📄 arXiv](https://arxiv.org/abs/2611.14046) • [📥 PDF](https://arxiv.org/pdf/2611.14046)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Adversarial training is often plagued by "pseudo-attacks"—perturbations that significantly increase the loss value but fail to truly alter the model's confidence structure. To address this, we propose two complementary approaches to directly attac...

</details>

<details>
<summary><b>19. HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12872) • [📄 arXiv](https://arxiv.org/abs/2611.12872) • [📥 PDF](https://arxiv.org/pdf/2611.12872)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ViktorAxelsen/HiVe-Mem)

> As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed...

</details>

<details>
<summary><b>20. Do Multimodal Models Decide Consistently on Equivalent Optical Spectra?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Genliang Zhu, Ziyuan Wang, chen-ai-researcher

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00428) • [📄 arXiv](https://arxiv.org/abs/2611.00428) • [📥 PDF](https://arxiv.org/pdf/2611.00428)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A spectrum can be given to a model as a table in nanometers or as a plot in photon energy, and the decision should not depend on which one it sees. When the data needed for an answer are missing, the model should say so. We test representation inv...

</details>

<details>
<summary><b>21. Humanized but Still True? Auditing Facts and Detection in AI-Text Humanizers</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Genliang Zhu, Ziyuan Wang, chen-ai-researcher

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00359) • [📄 arXiv](https://arxiv.org/abs/2611.00359) • [📥 PDF](https://arxiv.org/pdf/2611.00359)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AI "humanizers" rewrite machine-generated text so that detectors classify it as human-written. Public leaderboards score evasion and embedding similarity, but not whether checkable details survive. We check whether numbers, dates, person and organ...

</details>

<details>
<summary><b>22. From Large Language Models to Efficient System One Models via Adaptive Computation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Minh-Anh Nguyen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16321) • [📄 arXiv](https://arxiv.org/abs/2611.16321) • [📥 PDF](https://arxiv.org/pdf/2611.16321)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/minhkks/NestOne)

> Transferring LLMs into System One decision models typically replaces the language modeling head with a decision head while retaining the full backbone, making every decision pay for all layers. Yet it remains unclear how much depth such decisions ...

</details>

<details>
<summary><b>23. JustRUA: A Controlled Study of GPT-6 Robot-Use Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Cheng Yin, Mingqi Gao, Xuanwei Shi, Yufan Dang, Zefan Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16009) • [📄 arXiv](https://arxiv.org/abs/2611.16009) • [📥 PDF](https://arxiv.org/pdf/2611.16009)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZefanW/JustRUA)

> JustRUA is a controlled study of GPT-6 Astra robot-use agents on RoboDojo. We take the designs recent systems add (harness, action interface, reuse of experience, scene geometry) and test them one at a time in one framework. The harness we end up ...

</details>

<details>
<summary><b>24. A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jingjing Jiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14256) • [📄 arXiv](https://arxiv.org/abs/2611.14256) • [📥 PDF](https://arxiv.org/pdf/2611.14256)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jingjing12110/SE-MMAgents)

> Self-Evolving Multimodal Agents

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 24 |
| 📅 Today | [`2026-11-13.json`](data/daily/2026-11-13.json) | 24 |
| 📆 This Week | [`2026-W45.json`](data/weekly/2026-W45.json) | 125 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 395 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-13 | 24 | [View JSON](data/daily/2026-11-13.json) |
| 📄 2026-11-12 | 18 | [View JSON](data/daily/2026-11-12.json) |
| 📄 2026-11-11 | 29 | [View JSON](data/daily/2026-11-11.json) |
| 📄 2026-11-10 | 26 | [View JSON](data/daily/2026-11-10.json) |
| 📄 2026-11-09 | 28 | [View JSON](data/daily/2026-11-09.json) |
| 📄 2026-11-08 | 32 | [View JSON](data/daily/2026-11-08.json) |
| 📄 2026-11-07 | 32 | [View JSON](data/daily/2026-11-07.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W45 | 125 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 395 | [View JSON](data/monthly/2026-11.json) |
| 🗓️ 2026-10 | 1640 | [View JSON](data/monthly/2026-10.json) |
| 🗓️ 2026-09 | 781 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |

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
