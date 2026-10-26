<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-28-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9240+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">28</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1479</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9240+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 26, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Reading, Writing, Sharing, and Interacting with the World through Video</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31668) • [📄 arXiv](https://arxiv.org/abs/2610.31668) • [📥 PDF](https://arxiv.org/pdf/2610.31668)

**💻 Code:** [⭐ Code](https://github.com/vid-gen/awesome-video-world-model) • [⭐ Code](https://github.com/huggingface)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API The Past Frames the Future: Memory for Autoregressive Video Generation (202...

</details>

<details>
<summary><b>2. UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30932) • [📄 arXiv](https://arxiv.org/abs/2610.30932) • [📥 PDF](https://arxiv.org/pdf/2610.30932)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RecGPT-Team/UserArena)

> Can simulated shoppers faithfully reproduce real users’ behavior over long shopping interactions? We introduce UserArena , an interactive benchmark grounded in real-world e-commerce data: 64,729 sessions from 11,010 users , covering 566,102 items ...

</details>

<details>
<summary><b>3. HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31162) • [📄 arXiv](https://arxiv.org/abs/2610.31162) • [📥 PDF](https://arxiv.org/pdf/2610.31162)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 We are excited to share our latest work: "HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games" ! Can an AI agent autonomously complete long-horizon tasks in Minecraft using only visual observations and native keyboard-and-mou...

</details>

<details>
<summary><b>4. RSIHub: A Composable Framework for Agent-Evolution Methods</b> ⭐ 186</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32253) • [📄 arXiv](https://arxiv.org/abs/2610.32253) • [📥 PDF](https://arxiv.org/pdf/2610.32253)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/simple-agent-lab/RSIHub)

> Hi everyone! We’re sharing RSIHub, an open-source framework for building and comparing agent-evolution methods. RSIHub lets researchers compose reusable operators to improve agent prompts, skills, tools, and orchestration, while keeping evaluation...

</details>

<details>
<summary><b>5. RynnUnify: Towards Unified Embodied Brain</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32965) • [📄 arXiv](https://arxiv.org/abs/2610.32965) • [📥 PDF](https://arxiv.org/pdf/2610.32965)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/alibaba-damo-academy/RynnUnify)

> Introduction We present RynnUnify , a Mixture-of-Transformers architecture with an autoregressive Reasoner and a rectified-flow video Generator . Built on Cosmos3, RynnUnify connects embodied understanding, spatial grounding, and long-horizon visu...

</details>

<details>
<summary><b>6. Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs</b> ⭐ 94</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27103) • [📄 arXiv](https://arxiv.org/abs/2610.27103) • [📥 PDF](https://arxiv.org/pdf/2610.27103)

**💻 Code:** [⭐ Code](https://github.com/ZiiJianLiu/Omni-Woodpecker) • [⭐ Code](https://github.com/huggingface)

> Paper: https://arxiv.org/abs/2610.27103 Code: https://github.com/ZiiJianLiu/Omni-Woodpecker

</details>

<details>
<summary><b>7. Every Weight Is a Path of Shared Discrete Decisions</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31931) • [📄 arXiv](https://arxiv.org/abs/2610.31931) • [📥 PDF](https://arxiv.org/pdf/2610.31931)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ammarali32/StateTree-Representation)

> We introduce state trees , a new representation in which every weight is a path of discrete decisions, and decisions can be shared across weights. Quantization, pruning, low-rank factorization and weight sharing all become edits on a tree, and app...

</details>

<details>
<summary><b>8. Dual Exam: Controlled Evaluation of Multimodal Agents and World Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Guohao Cai, Jingfan Chen, Xuan Zhang, Meng Chu, Zhefan Rao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31066) • [📄 arXiv](https://arxiv.org/abs/2610.31066) • [📥 PDF](https://arxiv.org/pdf/2610.31066)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Dual Exam: Controlled Evaluation of Multimodal Agents and World Models

</details>

<details>
<summary><b>9. TenetBench: A Clause-Anchored Russian Corpus for Evaluating Language Models against Professional Codes of Ethics</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sergey Bolovtsov, Marina Polukoshko, Andrey Furov, Valery Vinogradov, user-7431

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.29477) • [📄 arXiv](https://arxiv.org/abs/2610.29477) • [📥 PDF](https://arxiv.org/pdf/2610.29477)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Preprint. TenetBench tests whether LLM-generated text conflicts with specific clauses of Russian-language professional codes, using conflicting requests paired with benign alternatives based on the same scenario. In the paper's main evaluation, ea...

</details>

<details>
<summary><b>10. On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32770) • [📄 arXiv](https://arxiv.org/abs/2610.32770) • [📥 PDF](https://arxiv.org/pdf/2610.32770)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can a language model improve itself without a single human-written question or answer? We introduce On-Policy Self-Training (OPST), which reformulates on-policy self-distillation as a self-training framework, driven by self-generated question-answ...

</details>

<details>
<summary><b>11. DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama Script Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Pengfei Xu, Yuncheng Huang, Fan Liu, Siyang He, qiqi4545

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32002) • [📄 arXiv](https://arxiv.org/abs/2610.32002) • [📥 PDF](https://arxiv.org/pdf/2610.32002)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The rapid growth of microdramas has increased demand for high-quality script production. Long-form microdrama script generation with LLMs requires both diverse plot progression and long-range narrative coherence. Our observations reveal that candi...

</details>

<details>
<summary><b>12. FLOMSS: Generative Music Source Separation by Flow Matching</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Qiyu Wu, Koichi Saito, Keisuke Toyama, Zhi Zhong, ik4sumii

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17821) • [📄 arXiv](https://arxiv.org/abs/2610.17821) • [📥 PDF](https://arxiv.org/pdf/2610.17821)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> FLOMSS systematically investigates flow matching for full-band stereo music source separation (MSS). Systematic design study: We investigate prediction targets, flow paths, single- vs. multi-source modeling, and mixture consistency. Optimal Transp...

</details>

<details>
<summary><b>13. DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ziqi Cai, Xiangcheng Cao, Penghao Luo, Lixin Xiu, Zixian Gao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31734) • [📄 arXiv](https://arxiv.org/abs/2610.31734) • [📥 PDF](https://arxiv.org/pdf/2610.31734)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23234) • [📄 arXiv](https://arxiv.org/abs/2610.23234) • [📥 PDF](https://arxiv.org/pdf/2610.23234)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ✨ Highlights Role-specific learning signals — MultiAgent-OPD combines local process supervision for Searchers with outcome-based reinforcement learning for the Leader and Answerer, addressing credit assignment in hierarchical multi-agent teams. Tw...

</details>

<details>
<summary><b>15. MMVistaReason: Toward Open-Data and Post-Training Recipes for Multimodal Reasoning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.01352) • [📄 arXiv](https://arxiv.org/abs/2610.01352) • [📥 PDF](https://arxiv.org/pdf/2610.01352)

**💻 Code:** [⭐ Code](https://github.com/JackieForest/MMVistaReason) • [⭐ Code](https://github.com/huggingface)

> Open multimodal reasoning models have benefited from large-scale reasoning supervision, yet reliable post-training remains challenging due to uneven data quality, inefficient supervision construction, imbalanced difficulty, and cross-domain interf...

</details>

<details>
<summary><b>16. Building Auditable AI Text Detectors with Sparse Autoencoders</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30006) • [📄 arXiv](https://arxiv.org/abs/2610.30006) • [📥 PDF](https://arxiv.org/pdf/2610.30006)

**💻 Code:** [⭐ Code](https://github.com/google-deepmind/detectorscope) • [⭐ Code](https://github.com/huggingface)

> We propose DetectorScope---a pipeline that takes an arbitrary black-box AI detector and converts it into an auditable detector (i.e. one that is transparent about the features it uses to make its prediction). In our experiments we show that these ...

</details>

<details>
<summary><b>17. DuoLM: Fast and Effective Personalized Recommendation with Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24481) • [📄 arXiv](https://arxiv.org/abs/2610.24481) • [📥 PDF](https://arxiv.org/pdf/2610.24481)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jiangLLM/DuoLM)

> Introducing DuoLM DuoLM is a framework for fast, personalized recommendation with two jointly trained language models. An encoder turns item descriptions into compact representations that can be cached and reused across users. A ranker combines th...

</details>

<details>
<summary><b>18. LoCA: Enabling Multi-Modality in Geospatial Location Encoders</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Dimitris Christofis, Eleni Saka, Diogenis Antonopoulos, Eleanna Vali, pakoromilas

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32894) • [📄 arXiv](https://arxiv.org/abs/2610.32894) • [📥 PDF](https://arxiv.org/pdf/2610.32894)

**💻 Code:** [⭐ Code](https://github.com/eleannavali/LoCA) • [⭐ Code](https://github.com/huggingface)

> 🌍 LoCA: Enabling Multi-Modality in Geospatial Location Encoders Location encoders such as SatCLIP and GeoCLIP turn (lat, lon) into general-purpose embeddings by contrastive alignment with satellite imagery. This paper shows why this works and what...

</details>

<details>
<summary><b>19. Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xintong Han, Jiachen Xu, Zehan Wang, Wenyou Yi, Viglong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32250) • [📄 arXiv](https://arxiv.org/abs/2610.32250) • [📥 PDF](https://arxiv.org/pdf/2610.32250)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction

</details>

<details>
<summary><b>20. Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Hang Yu, Xinyi Wang, Juntu Zhao, Bohao Fan, Yufeng Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31569) • [📄 arXiv](https://arxiv.org/abs/2610.31569) • [📥 PDF](https://arxiv.org/pdf/2610.31569)

**💻 Code:** [⭐ Code](https://github.com/lyfeng001/Echo-Sim) • [⭐ Code](https://github.com/huggingface)

> Recognizing task completion and failure enables robots to stop upon success and initiate recovery or replanning after failure. Existing methods augment Vision Language Action (VLA) policies with task status signal prediction to support these execu...

</details>

<details>
<summary><b>21. Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.29552) • [📄 arXiv](https://arxiv.org/abs/2610.29552) • [📥 PDF](https://arxiv.org/pdf/2610.29552)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/devinxzhang/CycleGRPO)

> Extension of CycleGRPO (ECCV26: https://devinxzhang.github.io/CycleGRPO-Page/ )

</details>

<details>
<summary><b>22. RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27782) • [📄 arXiv](https://arxiv.org/abs/2610.27782) • [📥 PDF](https://arxiv.org/pdf/2610.27782)

**💻 Code:** [⭐ Code](https://github.com/Sphere-AI-Lab/RoboJudge) • [⭐ Code](https://github.com/huggingface)

> We introduce RoboJudge-Bench , a benchmark for evaluating multimodal LLMs as judges of embodied video generation, covering physical adherence and instruction alignment across diverse embodiments and video generators. We further present RoboJudge-T...

</details>

<details>
<summary><b>23. DISC: Domain-Integrated Similarity Cost for Time-Series Dataset</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ryan Rossi, Hongjie Chen, Yen-Ku Liu, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31288) • [📄 arXiv](https://arxiv.org/abs/2610.31288) • [📥 PDF](https://arxiv.org/pdf/2610.31288)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>24. A path-following framework on fiber bundle for variational inequalities</b> ⭐ 0</summary>

<br/>

**👥 Authors:** shb20

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00778) • [📄 arXiv](https://arxiv.org/abs/2606.00778) • [📥 PDF](https://arxiv.org/pdf/2606.00778)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/shb20tsinghua/FiberBundle_VI)

> This paper presents a general-purpose path-following algorithm that solves general variational inequalities with continuous mappings and polytope domains to arbitrary precision, achieving global linear convergence: exact for nonsingular solutions,...

</details>

<details>
<summary><b>25. The fixed-point bundle method over product-of-simplex domains arising from game equilibria</b> ⭐ 0</summary>

<br/>

**👥 Authors:** shb20

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.16158) • [📄 arXiv](https://arxiv.org/abs/2609.16158) • [📥 PDF](https://arxiv.org/pdf/2609.16158)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/shb20tsinghua/FiberBundle_VI)

> This paper extends the fiber-bundle path-following framework of arXiv:2606.00778 to product-of-simplex domains, so that the algorithm solves arbitrary m-player n-action general-sum games to arbitrary precision, inheriting global linear convergence...

</details>

<details>
<summary><b>26. HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ziyue Liu, Yuhan Bao, Boxiong Li, Bo Zhang, Xihan Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32909) • [📄 arXiv](https://arxiv.org/abs/2610.32909) • [📥 PDF](https://arxiv.org/pdf/2610.32909)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>27. SliderEdit++: Improved Slider Trajectories in Instruction-Based Image Editing</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Varun Manjunatha, Bryan Wang, Sayan Nag, Arman Zarei, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14253) • [📄 arXiv](https://arxiv.org/abs/2610.14253) • [📥 PDF](https://arxiv.org/pdf/2610.14253)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>28. Co-adaptive Rule Routing and Constraining for Structured Knowledge Retrieval</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Bing He, Jiaxi Li, Haoyu Han, Zhisheng Qi, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14465) • [📄 arXiv](https://arxiv.org/abs/2610.14465) • [📥 PDF](https://arxiv.org/pdf/2610.14465)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 28 |
| 📅 Today | [`2026-10-26.json`](data/daily/2026-10-26.json) | 28 |
| 📆 This Week | [`2026-W43.json`](data/weekly/2026-W43.json) | 28 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1479 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-26 | 28 | [View JSON](data/daily/2026-10-26.json) |
| 📄 2026-10-25 | 49 | [View JSON](data/daily/2026-10-25.json) |
| 📄 2026-10-24 | 50 | [View JSON](data/daily/2026-10-24.json) |
| 📄 2026-10-23 | 36 | [View JSON](data/daily/2026-10-23.json) |
| 📄 2026-10-22 | 41 | [View JSON](data/daily/2026-10-22.json) |
| 📄 2026-10-21 | 49 | [View JSON](data/daily/2026-10-21.json) |
| 📄 2026-10-20 | 55 | [View JSON](data/daily/2026-10-20.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W43 | 28 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1479 | [View JSON](data/monthly/2026-10.json) |
| 🗓️ 2026-09 | 781 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |

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
