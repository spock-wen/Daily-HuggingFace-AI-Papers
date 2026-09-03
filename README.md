<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-28-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7062+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">28</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">107</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">82</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7062+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 03, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02749) • [📄 arXiv](https://arxiv.org/abs/2609.02749) • [📥 PDF](https://arxiv.org/pdf/2609.02749)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VectorSpaceLab/AREX-Skill)

> 📄 Daily Papers： https://huggingface.co/papers/2609.02749 📄 Paper： https://arxiv.org/abs/2609.02749 💻 GitHub： https://github.com/VectorSpaceLab/AREX-Skill 🚀 DisCo CLI： https://www.npmjs.com/package/@arex-skill/disco

</details>

<details>
<summary><b>2. SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02886) • [📄 arXiv](https://arxiv.org/abs/2609.02886) • [📥 PDF](https://arxiv.org/pdf/2609.02886)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Junchao-cs/SolarWM)

> We present SolarWM , a fully open foundation for building interactive video world models from data preparation through scalable training and long-horizon inference. Open, reconfigurable data infrastructure. SolarWM converts 1.43 million canonical ...

</details>

<details>
<summary><b>3. EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02783) • [📄 arXiv](https://arxiv.org/abs/2609.02783) • [📥 PDF](https://arxiv.org/pdf/2609.02783)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/inphotoo/earlyeval)

> Your agent evaluation can be cheaper!

</details>

<details>
<summary><b>4. It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.00638) • [📄 arXiv](https://arxiv.org/abs/2609.00638) • [📥 PDF](https://arxiv.org/pdf/2609.00638)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Proud to share our work, CoGR (Co-evolving Generative Retrieval), where we train LLMs to generate retrieval keywords for both user queries and apps. CoGR follows a co-evolving training framework: we alternately optimize one side while keeping the ...

</details>

<details>
<summary><b>5. Language Models Can Control Their Own Attention</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02737) • [📄 arXiv](https://arxiv.org/abs/2609.02737) • [📥 PDF](https://arxiv.org/pdf/2609.02737)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Language models can control their own attention. Zero-shot evaluation of Gemma 4 31B shows a 52% reduction in global attention cost during decoding across 15 long-context benchmarks with 1.52pp accuracy drop.

</details>

<details>
<summary><b>6. On the Design Fundamentals of Pixel Text Representation Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01147) • [📄 arXiv](https://arxiv.org/abs/2609.01147) • [📥 PDF](https://arxiv.org/pdf/2609.01147)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> How do vision models learn to understand text directly from pixels? How can models pretrained on synthetic text rendered at ≤224×224 resolution generalize all the way to real-world 4K documents at test time? Pixel Linguist II answers these questio...

</details>

<details>
<summary><b>7. Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.21450) • [📄 arXiv](https://arxiv.org/abs/2608.21450) • [📥 PDF](https://arxiv.org/pdf/2608.21450)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce KBMR, an MLLM-based retriever designed for Knowledge-Based Visual Question Answering (KB-VQA). Instead of relying on surface-level visual similarity, KBMR learns entity-aligned semantic representations and leverages an MLLM-based sema...

</details>

<details>
<summary><b>8. HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01437) • [📄 arXiv](https://arxiv.org/abs/2609.01437) • [📥 PDF](https://arxiv.org/pdf/2609.01437)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce HarnessDev, a benchmark that evaluates whether LLMs can create and iteratively improve the agent harnesses that shape their downstream performance. Across six creator LLMs, four domains, and five benchmarks, generated harnesses show p...

</details>

<details>
<summary><b>9. ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01740) • [📄 arXiv](https://arxiv.org/abs/2609.01740) • [📥 PDF](https://arxiv.org/pdf/2609.01740)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes

</details>

<details>
<summary><b>10. Cliff: Learning Process Rewards from the First Mistake</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Gerald Friedland, Jie Hao, Ketan Ramaneti, Runhui Wang, Peixuan Han

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02817) • [📄 arXiv](https://arxiv.org/abs/2609.02817) • [📥 PDF](https://arxiv.org/pdf/2609.02817)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A paper focusing on LLM RL and reward shaping

</details>

<details>
<summary><b>11. Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29846) • [📄 arXiv](https://arxiv.org/abs/2608.29846) • [📥 PDF](https://arxiv.org/pdf/2608.29846)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Sampled-token on-policy distillation (OPD) efficiently transfers capabilities from teacher to student using student-generated tokens, requiring teacher probabilities only for sampled tokens. Yet it frequently suffers from diversity distillation fa...

</details>

<details>
<summary><b>12. Aspire: Can Models Self-Evolve from Vague Goals?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31111) • [📄 arXiv](https://arxiv.org/abs/2608.31111) • [📥 PDF](https://arxiv.org/pdf/2608.31111)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce ASPIRE, a benchmark that asks whether models can self-evolve from only a vague capability goal, without access to downstream evaluation tasks. Across 520 expert-authored items spanning six goals, agents can complete training and harne...

</details>

<details>
<summary><b>13. S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31100) • [📄 arXiv](https://arxiv.org/abs/2608.31100) • [📥 PDF](https://arxiv.org/pdf/2608.31100)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce S³Gym, an interactive benchmark that asks whether LLM agents can turn self-testing and self-judging into real self-improvement across seven text-based games. Comparing interaction history, summarized memory, and parameter training, we...

</details>

<details>
<summary><b>14. A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.00591) • [📄 arXiv](https://arxiv.org/abs/2609.00591) • [📥 PDF](https://arxiv.org/pdf/2609.00591)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>15. VibeVoice-ASR-Streaming Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02812) • [📄 arXiv](https://arxiv.org/abs/2609.02812) • [📥 PDF](https://arxiv.org/pdf/2609.02812)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> VibeVoice-ASR-Streaming, a unified streaming ASR model that continuously transcribes ''who said what'' as speech arrives,

</details>

<details>
<summary><b>16. MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30949) • [📄 arXiv](https://arxiv.org/abs/2608.30949) • [📥 PDF](https://arxiv.org/pdf/2608.30949)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/seokwon99/Multi3IR)

> EMNLP 2026; code is available at https://github.com/seokwon99/Multi3IR .

</details>

<details>
<summary><b>17. Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.18972) • [📄 arXiv](https://arxiv.org/abs/2608.18972) • [📥 PDF](https://arxiv.org/pdf/2608.18972)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A structured dataset derived from the Boston Public Library's public domain newspapers collection, produced by the Institutional Data Initiative (Harvard Law School Library) in collaboration with Boston Public Library . 1,473,635 public domain new...

</details>

<details>
<summary><b>18. Post-Training Language Models for Gold-Medal Performance in Coding Competitions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02849) • [📄 arXiv](https://arxiv.org/abs/2609.02849) • [📥 PDF](https://arxiv.org/pdf/2609.02849)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>19. PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.02272) • [📄 arXiv](https://arxiv.org/abs/2609.02272) • [📥 PDF](https://arxiv.org/pdf/2609.02272)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Daethalous/PaperCompiler)

> .

</details>

<details>
<summary><b>20. CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Linh Ngo Van, Ryan A. Rossi, Chien Van Nguyen, Huu Huy Nguyen, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01925) • [📄 arXiv](https://arxiv.org/abs/2609.01925) • [📥 PDF](https://arxiv.org/pdf/2609.01925)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>21. ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01865) • [📄 arXiv](https://arxiv.org/abs/2609.01865) • [📥 PDF](https://arxiv.org/pdf/2609.01865)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share ExecRetrieval ! We ask a simple question: can code embeddings actually distinguish correct code from near-identical buggy code? Across 939 tasks and 24 retrieval systems, the best system reaches 100% exec@10 but only 33.1% exec@1 ...

</details>

<details>
<summary><b>22. SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Junfu Pu, Enjun Du, Kuan Zhang, Fuda Ye, Zirong Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29607) • [📄 arXiv](https://arxiv.org/abs/2608.29607) • [📥 PDF](https://arxiv.org/pdf/2608.29607)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Findings of EMNLP 2026

</details>

<details>
<summary><b>23. Exploring Collaboration between a language and a non-language agent</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.00474) • [📄 arXiv](https://arxiv.org/abs/2609.00474) • [📥 PDF](https://arxiv.org/pdf/2609.00474)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> LLMs are increasingly deployed as orchestrators that coordinate specialized subagents to solve complex tasks through natural language. However, in many important domains like game playing and robotics, the strongest available agents are not langua...

</details>

<details>
<summary><b>24. Kirin: Animal Motion Generation from In-the-Wild Video</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shangzhe Wu, Jiajun Wu, James M. Rehg, Zhuoyang Pan, Brian Nlong Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01823) • [📄 arXiv](https://arxiv.org/abs/2609.01823) • [📥 PDF](https://arxiv.org/pdf/2609.01823)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>25. FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tali Dekel, Yael Vinker, Sigal Raab, mayaweiz

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.00377) • [📄 arXiv](https://arxiv.org/abs/2609.00377) • [📥 PDF](https://arxiv.org/pdf/2609.00377)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This work shows a very cool application of origami representation reconstruction from a natural video. The domain is fun, practical and underexplored. Its use of an agentic framework is practically relevant to the field.

</details>

<details>
<summary><b>26. Ignorance or Incompetence? Constructing Knowledge-Gated, Verifiable Tasks for LLM Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhao Yang, Sihan Zhu, Yu Mi, Minhao Li, zachtian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30322) • [📄 arXiv](https://arxiv.org/abs/2608.30322) • [📥 PDF](https://arxiv.org/pdf/2608.30322)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce a knowledge-gated task-construction protocol that separates agent failures caused by missing domain knowledge from failures caused by inadequate capability. The protocol uses private artefacts, leak audits, and verifiable ground truth...

</details>

<details>
<summary><b>27. Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Stefan Lüdtke, Stefan Oehmcke, ashnedungadi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30751) • [📄 arXiv](https://arxiv.org/abs/2608.30751) • [📥 PDF](https://arxiv.org/pdf/2608.30751)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR We introduce Autoregressive Mosaics (AM-Bench) to evaluate whether text-only LLMs possess genuine 2D spatial reasoning or merely translate spatial text into syntax. The Core Problem When LLMs generate code that draws an image, it remains unc...

</details>

<details>
<summary><b>28. NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01657) • [📄 arXiv](https://arxiv.org/abs/2609.01657) • [📥 PDF](https://arxiv.org/pdf/2609.01657)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 👀 @ uminaty and I are very proud to share NeoMME: a family of 260M and 800M Multimodal-Native Multilingual Encoders trained from scratch! NeoMME uses one bidirectional Transformer for text tokens and raw image patches, without a pretrained vision ...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 28 |
| 📅 Today | [`2026-09-03.json`](data/daily/2026-09-03.json) | 28 |
| 📆 This Week | [`2026-W35.json`](data/weekly/2026-W35.json) | 107 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 82 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-03 | 28 | [View JSON](data/daily/2026-09-03.json) |
| 📄 2026-09-02 | 21 | [View JSON](data/daily/2026-09-02.json) |
| 📄 2026-09-01 | 33 | [View JSON](data/daily/2026-09-01.json) |
| 📄 2026-08-31 | 25 | [View JSON](data/daily/2026-08-31.json) |
| 📄 2026-08-30 | 23 | [View JSON](data/daily/2026-08-30.json) |
| 📄 2026-08-29 | 23 | [View JSON](data/daily/2026-08-29.json) |
| 📄 2026-08-28 | 21 | [View JSON](data/daily/2026-08-28.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W35 | 107 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |
| 📅 2026-W32 | 156 | [View JSON](data/weekly/2026-W32.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 82 | [View JSON](data/monthly/2026-09.json) |
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
