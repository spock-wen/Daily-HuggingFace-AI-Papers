<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-30-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3337+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">30</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">54</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">176</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3337+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** April 09, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding</b> ⭐ 279</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05015) • [📄 arXiv](https://arxiv.org/abs/2604.05015) • [📥 PDF](https://arxiv.org/pdf/2604.05015)

**💻 Code:** [⭐ Code](https://github.com/MME-Benchmarks/Video-MME-v2)

> Video-MME-v2: Towards the Next Stage in Video Understanding Evaluation Technical Report : https://arxiv.org/pdf/2604.05015 Project Page : https://video-mme-v2.netlify.app/ Leaderboard : https://video-mme-v2.netlify.app/#leaderboard GitHub : https:...

</details>

<details>
<summary><b>2. Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents</b> ⭐ 340</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06132) • [📄 arXiv](https://arxiv.org/abs/2604.06132) • [📥 PDF](https://arxiv.org/pdf/2604.06132)

**💻 Code:** [⭐ Code](https://github.com/claw-eval/claw-eval)

> Claw-Eval

</details>

<details>
<summary><b>3. Learning to Retrieve from Agent Trajectories</b> ⭐ 27</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04949) • [📄 arXiv](https://arxiv.org/abs/2604.04949) • [📥 PDF](https://arxiv.org/pdf/2604.04949)

**💻 Code:** [⭐ Code](https://github.com/Yuqi-Zhou/LRAT)

> Key insights: We identify a fundamental misalignment between human-centric retrieval training and agentic search, and formulate learning to retrieve from agent trajectories as a new retrieval paradigm. In this setting, supervision is derived from ...

</details>

<details>
<summary><b>4. ACES: Who Tests the Tests? Leave-One-Out AUC Consistency for Code Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yali Du, Zheng Xie, Yun-Ji Zhang, richardodliu, sun0o0

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.03922) • [📄 arXiv](https://arxiv.org/abs/2604.03922) • [📥 PDF](https://arxiv.org/pdf/2604.03922)

> Selecting LLM-generated code candidates using LLM-generated tests is challenging because the tests themselves may be incorrect. Existing methods either treat all tests equally or rely on ad-hoc heuristics to filter unreliable tests. Yet determinin...

</details>

<details>
<summary><b>5. GBQA: A Game Benchmark for Evaluating LLMs as Quality Assurance Engineers</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Zhiyang Chen, Chios Chen, Tsumugii

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.02648) • [📄 arXiv](https://arxiv.org/abs/2604.02648) • [📥 PDF](https://arxiv.org/pdf/2604.02648)

**💻 Code:** [⭐ Code](https://github.com/camel-ai/GBQA)

> Accepted as a workshop paper at the Fourteenth International Conference on Learning Representations (ICLR 2026)

</details>

<details>
<summary><b>6. ThinkTwice: Jointly Optimizing Large Language Models for Reasoning and Self-Refinement</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.01591) • [📄 arXiv](https://arxiv.org/abs/2604.01591) • [📥 PDF](https://arxiv.org/pdf/2604.01591)

**💻 Code:** [⭐ Code](https://github.com/CSSLab/ThinkTwice)

> We introduce ThinkTwice, a simple two-phase framework that jointly optimizes LLMs to solve reasoning problems and refine the answers, based on Group Relative Policy Optimization (GRPO). In each pair of training steps, ThinkTwice first optimizes th...

</details>

<details>
<summary><b>7. Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision</b> ⭐ 26</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04934) • [📄 arXiv](https://arxiv.org/abs/2604.04934) • [📥 PDF](https://arxiv.org/pdf/2604.04934)

**💻 Code:** [⭐ Code](https://github.com/snuvclab/vanast)

> Given a human image and one or more garment images, our method generates virtual try-on with human image animation conditioned on a pose video while preserving identity.

</details>

<details>
<summary><b>8. Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning</b> ⭐ 25</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05404) • [📄 arXiv](https://arxiv.org/abs/2604.05404) • [📥 PDF](https://arxiv.org/pdf/2604.05404)

**💻 Code:** [⭐ Code](https://github.com/sqs-ustc/tool-reasoning-framework-PTE)

> In real-world Tool-Integrated Reasoning (TIR) scenarios, a major source of inefficiency is that the toolcalls create pauses between LLM requests and cause KV-cache eviction. Also, the long, unfiltered response returned by external tools inflates t...

</details>

<details>
<summary><b>9. Watch Before You Answer: Learning from Visually Grounded Post-Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05117) • [📄 arXiv](https://arxiv.org/abs/2604.05117) • [📥 PDF](https://arxiv.org/pdf/2604.05117)

**💻 Code:** [⭐ Code](https://github.com/reacher-z/vidground)

> TL;DR: We find that 40-60% of questions in popular video understanding benchmarks (VideoMME, MMVU, etc.) can be answered from text alone, and the same problem also exists in post-training datasets. VidGround is a simple fix: keep only the visually...

</details>

<details>
<summary><b>10. MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU</b> ⭐ 61</summary>

<br/>

**👥 Authors:** Yanfang Ye, Lichao Sun, Hanchi Sun, Zhengqing Yuan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05091) • [📄 arXiv](https://arxiv.org/abs/2604.05091) • [📥 PDF](https://arxiv.org/pdf/2604.05091)

**💻 Code:** [⭐ Code](https://github.com/DLYuanGod/MegaTrain)

> We present MegaTrain, a memory-centric system that efficiently trains 100B+ parameter large language models at full precision on a single GPU. Unlike traditional GPU-centric systems, MegaTrain stores parameters and optimizer states in host memory ...

</details>

<details>
<summary><b>11. How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04323) • [📄 arXiv](https://arxiv.org/abs/2604.04323) • [📥 PDF](https://arxiv.org/pdf/2604.04323)

**💻 Code:** [⭐ Code](https://github.com/UCSB-NLP-Chang/Skill-Usage)

> Agent skills, which are reusable, domain-specific knowledge artifacts, have become a popular mechanism for extending LLM-based agents, yet formally benchmarking skill usage performance remains scarce. Existing skill benchmarking efforts focus on o...

</details>

<details>
<summary><b>12. General Multimodal Protein Design Enables DNA-Encoding of Chemistry</b> ⭐ 46</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05181) • [📄 arXiv](https://arxiv.org/abs/2604.05181) • [📥 PDF](https://arxiv.org/pdf/2604.05181)

**💻 Code:** [⭐ Code](https://github.com/DISCO-design/DISCO)

> DISCO (DIffusion for Sequence-structure CO-design) is a multimodal generative model that simultaneously co-designs protein sequences and 3D structures, conditioned on and co-folded with arbitrary biomolecules — including small-molecule ligands, DN...

</details>

<details>
<summary><b>13. Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06170) • [📄 arXiv](https://arxiv.org/abs/2604.06170) • [📥 PDF](https://arxiv.org/pdf/2604.06170)

**💻 Code:** [⭐ Code](https://github.com/MAXNORM8650/papercircle)

> accepted to ACL main for oral presentation. publicly released the website at https://papercircle.vercel.app/ and the code at https://github.com/MAXNORM8650/papercircle

</details>

<details>
<summary><b>14. ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05172) • [📄 arXiv](https://arxiv.org/abs/2604.05172) • [📥 PDF](https://arxiv.org/pdf/2604.05172)

**💻 Code:** [⭐ Code](https://github.com/benchflow-ai/ClawsBench)

> We introduce ClawsBench, a benchmark for evaluating both capability and safety of LLM productivity agents in simulated workspaces. Key highlights: • 5 high-fidelity mock services (Gmail, Calendar, Docs, Drive, Slack) validated against real APIs wi...

</details>

<details>
<summary><b>15. DARE: Diffusion Large Language Models Alignment and Reinforcement Executor</b> ⭐ 170</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04215) • [📄 arXiv](https://arxiv.org/abs/2604.04215) • [📥 PDF](https://arxiv.org/pdf/2604.04215)

**💻 Code:** [⭐ Code](https://github.com/yjyddq/DARE)

> Diffusion large language models (dLLMs) are emerging as a compelling alternative to dominant autoregressive models, replacing strictly sequential token generation with iterative denoising and parallel generation dynamics. However, their open-sourc...

</details>

<details>
<summary><b>16. In-Place Test-Time Training</b> ⭐ 28</summary>

<br/>

**👥 Authors:** Di He, Ge Zhang, Kai Hua, Shengjie Luo, Guhao Feng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06169) • [📄 arXiv](https://arxiv.org/abs/2604.06169) • [📥 PDF](https://arxiv.org/pdf/2604.06169)

**💻 Code:** [⭐ Code](https://github.com/ByteDance-Seed/In-Place-TTT)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API AllMem: A Memory-centric Recipe for Efficient Long-context Modeling (2026) ...

</details>

<details>
<summary><b>17. Demystifying When Pruning Works via Representation Hierarchies</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.24652) • [📄 arXiv](https://arxiv.org/abs/2603.24652) • [📥 PDF](https://arxiv.org/pdf/2603.24652)

**💻 Code:** [⭐ Code](https://github.com/CASE-Lab-UMD/Pruning-on-Representations)

> Network pruning, which removes less important parameters or architectures, is often expected to improve efficiency while preserving performance. However, this expectation does not consistently hold across language tasks: pruned models can perform ...

</details>

<details>
<summary><b>18. MedGemma 1.5 Technical Report</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fayaz Jamil, Timo Kohlberger, Fereshteh Mahvar, Chufan Gao, Andrew Sellergren

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05081) • [📄 arXiv](https://arxiv.org/abs/2604.05081) • [📥 PDF](https://arxiv.org/pdf/2604.05081)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API MedGPT-oss: Training a General-Purpose Vision-Language Model for Biomedicin...

</details>

<details>
<summary><b>19. Action Images: End-to-End Policy Learning via Multiview Video Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuncong Yang, Yilin Zhao, Qiao Sun, Zixian Gao, Haoyu Zhen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06168) • [📄 arXiv](https://arxiv.org/abs/2604.06168) • [📥 PDF](https://arxiv.org/pdf/2604.06168)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action ...

</details>

<details>
<summary><b>20. MMEmb-R1: Reasoning-Enhanced Multimodal Embedding with Pair-Aware Selection and Adaptive Control</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06156) • [📄 arXiv](https://arxiv.org/abs/2604.06156) • [📥 PDF](https://arxiv.org/pdf/2604.06156)

> MLLMs have been successfully applied to multimodal embedding tasks, yet their generative reasoning capabilities remain underutilized. Directly incorporating chain-of-thought reasoning into embedding learning introduces two fundamental challenges. ...

</details>

<details>
<summary><b>21. Experience Transfer for Multimodal LLM Agents in Minecraft Game</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hao Ni, Huadong Jian, Songbo Zhang, Jun Liu, Chenghao Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05533) • [📄 arXiv](https://arxiv.org/abs/2604.05533) • [📥 PDF](https://arxiv.org/pdf/2604.05533)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving E...

</details>

<details>
<summary><b>22. FactReview: Evidence-Grounded Reviews with Literature Positioning and Execution-Based Claim Verification</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04074) • [📄 arXiv](https://arxiv.org/abs/2604.04074) • [📥 PDF](https://arxiv.org/pdf/2604.04074)

> Peer review in ML is under real pressure — submission volumes keep growing, but reviewer bandwidth doesn't scale with it. This paper tackles a critical piece of the problem: grounding automated reviews in actual evidence rather than just reading t...

</details>

<details>
<summary><b>23. QiMeng-PRepair: Precise Code Repair via Edit-Aware Reward Optimization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Li Ding, Yuanbo Wen, Jiaming Guo, Rui Zhang, kcxain

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05963) • [📄 arXiv](https://arxiv.org/abs/2604.05963) • [📥 PDF](https://arxiv.org/pdf/2604.05963)

**💻 Code:** [⭐ Code](https://github.com/kcxain/QiMeng-PRepair)

> How to process over-editing?

</details>

<details>
<summary><b>24. Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04979) • [📄 arXiv](https://arxiv.org/abs/2604.04979) • [📥 PDF](https://arxiv.org/pdf/2604.04979)

**💻 Code:** [⭐ Code](https://github.com/KRLabsOrg/squeez)

> Coding agents can waste most of their context window re-reading noisy tool output. Squeez is a LoRA-tuned Qwen 3.5 2B model that extracts only the relevant lines from raw tool observations (pytest, grep, git log, kubectl, build logs, etc.), removi...

</details>

<details>
<summary><b>25. Context-Value-Action Architecture for Value-Driven Large Language Model Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05939) • [📄 arXiv](https://arxiv.org/abs/2604.05939) • [📥 PDF](https://arxiv.org/pdf/2604.05939)

> The core problem of behavioral rigidity in Large Language Model (LLM)-based agents and the motivation for the proposed Context Value Action (CVA) architecture. While LLMs have shown promise in simulating human behavior across various domains—rangi...

</details>

<details>
<summary><b>26. Scientific Graphics Program Synthesis via Dual Self-Consistency Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tianwei Lin, Sijing Li, Honglin Lin, Yun Zhu, Juekai Lin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06079) • [📄 arXiv](https://arxiv.org/abs/2604.06079) • [📥 PDF](https://arxiv.org/pdf/2604.06079)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Chart Specification: Structural Representations for Incentivizing VLM Reaso...

</details>

<details>
<summary><b>27. CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05467) • [📄 arXiv](https://arxiv.org/abs/2604.05467) • [📥 PDF](https://arxiv.org/pdf/2604.05467)

**💻 Code:** [⭐ Code](https://github.com/jainsid24/cue-r)

> CUE-R introduces an intervention-based framework for evaluating retrieved evidence in RAG systems - going beyond final answer accuracy to measure what each evidence item actually did once a reasoning model acted on it. We perturb evidence via remo...

</details>

<details>
<summary><b>28. REAM: Merging Improves Pruning of Experts in LLMs</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04356) • [📄 arXiv](https://arxiv.org/abs/2604.04356) • [📥 PDF](https://arxiv.org/pdf/2604.04356)

**💻 Code:** [⭐ Code](https://github.com/SamsungSAILMontreal/ream)

> Excited to share the REAM paper, the full code and GLM-4.5-Air-REAM is coming in couple days!

</details>

<details>
<summary><b>29. Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.03619) • [📄 arXiv](https://arxiv.org/abs/2604.03619) • [📥 PDF](https://arxiv.org/pdf/2604.03619)

**💻 Code:** [⭐ Code](https://github.com/beotborry/TABLeT)

> We introduce TABLeT, a simple and scalable framework for long-range voxel-wise 4D fMRI dynamics modeling. TABLeT uses a pre-trained 2D natural-image autoencoder to tokenize each 3D fMRI volume into just 27 continuous tokens, enabling much longer t...

</details>

<details>
<summary><b>30. Expert-Choice Routing Enables Adaptive Computation in Diffusion Language Models</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.01622) • [📄 arXiv](https://arxiv.org/abs/2604.01622) • [📥 PDF](https://arxiv.org/pdf/2604.01622)

**💻 Code:** [⭐ Code](https://github.com/zhangshuibai/EC-DLM)

> We show that expert-choice (EC) routing is a better fit for diffusion language models (DLMs) than token-choice routing: it gives deterministic load balancing, 2× faster convergence, and enables timestep-dependent adaptive computation. Pretrained T...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 30 |
| 📅 Today | [`2026-04-09.json`](data/daily/2026-04-09.json) | 30 |
| 📆 This Week | [`2026-W14.json`](data/weekly/2026-W14.json) | 54 |
| 🗓️ This Month | [`2026-04.json`](data/monthly/2026-04.json) | 176 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-04-09 | 30 | [View JSON](data/daily/2026-04-09.json) |
| 📄 2026-04-08 | 2 | [View JSON](data/daily/2026-04-08.json) |
| 📄 2026-04-07 | 17 | [View JSON](data/daily/2026-04-07.json) |
| 📄 2026-04-06 | 5 | [View JSON](data/daily/2026-04-06.json) |
| 📄 2026-04-05 | 45 | [View JSON](data/daily/2026-04-05.json) |
| 📄 2026-04-04 | 45 | [View JSON](data/daily/2026-04-04.json) |
| 📄 2026-04-03 | 3 | [View JSON](data/daily/2026-04-03.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W14 | 54 | [View JSON](data/weekly/2026-W14.json) |
| 📅 2026-W13 | 125 | [View JSON](data/weekly/2026-W13.json) |
| 📅 2026-W12 | 120 | [View JSON](data/weekly/2026-W12.json) |
| 📅 2026-W11 | 133 | [View JSON](data/weekly/2026-W11.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-04 | 176 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
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
