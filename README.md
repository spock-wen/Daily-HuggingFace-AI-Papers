<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-28-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9699+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📆 This Month</b><br/><font size="5">298</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9699+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 09, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes</b> ⭐ 34</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08264) • [📄 arXiv](https://arxiv.org/abs/2611.08264) • [📥 PDF](https://arxiv.org/pdf/2611.08264)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zju3dv/SplatAnything)

> We are excited to share our paper, SplatAnything: Gaussian Spacing Normalization for Feed-Forward 3DGS across Arbitrary Scenes ! SplatAnything is v3 of the InfiniSplat series . We are dedicated to developing high-quality feed-forward 3D Gaussian r...

</details>

<details>
<summary><b>2. P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter Priors</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03953) • [📄 arXiv](https://arxiv.org/abs/2611.03953) • [📥 PDF](https://arxiv.org/pdf/2611.03953)

**💻 Code:** [⭐ Code](https://github.com/SinuoWang/P2-MOPD) • [⭐ Code](https://github.com/huggingface)

> 🔥 Multi-teacher on-policy distillation (MOPD) is now a standard way to consolidate domain experts into one model, yet the student still has to climb to every teacher on its own, and some domains are left behind. What if the experts' weights could ...

</details>

<details>
<summary><b>3. LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06856) • [📄 arXiv](https://arxiv.org/abs/2611.06856) • [📥 PDF](https://arxiv.org/pdf/2611.06856)

**💻 Code:** [⭐ Code](https://github.com/KlingAIResearch/LongBanana) • [⭐ Code](https://github.com/huggingface)

> We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence,...

</details>

<details>
<summary><b>4. Beneath the Surface: What We Overlook When We Talk About Agent Evolution</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.07624) • [📄 arXiv](https://arxiv.org/abs/2611.07624) • [📥 PDF](https://arxiv.org/pdf/2611.07624)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/simple-agent-lab/RSIHub)

> Does a higher benchmark score really mean an agent is getting better? 🤔 In our paper, we go beyond surface-level benchmark evaluations to investigate what actually happens during agent evolution and why improvements do not always translate into be...

</details>

<details>
<summary><b>5. EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models</b> ⭐ 15</summary>

<br/>

**👥 Authors:** Haoxuan Che, Xiaozhuan Liang, Zhixuan Chen, DyJiang, Tommy-Bie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06748) • [📄 arXiv](https://arxiv.org/abs/2611.06748) • [📥 PDF](https://arxiv.org/pdf/2611.06748)

**💻 Code:** [⭐ Code](https://github.com/Tommy-Bie/EvoWorld) • [⭐ Code](https://github.com/huggingface)

> We are excited to introduce EvoWorld, a video generation framework for out-of-sight world evolution. EvoWorld combines a VLM brain with a visual renderer, enabling off-screen entities to remain active participants in an evolving world. Within a bi...

</details>

<details>
<summary><b>6. Fast and Exact Relative-Position Attention via Structure-Aware Kernels</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01182) • [📄 arXiv](https://arxiv.org/abs/2611.01182) • [📥 PDF](https://arxiv.org/pdf/2611.01182)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce an exact, FlashAttention-style algorithm for relative-position attention (DeBERTa, Shaw, Transformer-XL, and T5), using structure-aware tiling and atomic-free backward computation. At 8K tokens, it achieves up to 6.4× faster forward a...

</details>

<details>
<summary><b>7. Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription</b> ⭐ 868</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06043) • [📄 arXiv](https://arxiv.org/abs/2611.06043) • [📥 PDF](https://arxiv.org/pdf/2611.06043)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/netease-youdao/Confucius4-R2T2)

> Excited to share Confucius4-R2T2 , our stable-prefix streaming ASR model designed for real-time applications! Unlike conventional streaming ASR systems that repeatedly revise partial transcripts, R2T2 produces append-only, stable text that downstr...

</details>

<details>
<summary><b>8. Video-Coder: Reinforcing Agentic Coding for Video Generation</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09894) • [📄 arXiv](https://arxiv.org/abs/2611.09894) • [📥 PDF](https://arxiv.org/pdf/2611.09894)

**💻 Code:** [⭐ Code](https://github.com/CYWang735/Video-Coder) • [⭐ Code](https://github.com/huggingface)

> Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remain...

</details>

<details>
<summary><b>9. AgentBaton: Efficient Model Collaboration in Agentic Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35959) • [📄 arXiv](https://arxiv.org/abs/2610.35959) • [📥 PDF](https://arxiv.org/pdf/2610.35959)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> https://research.nvidia.com/labs/lpr/agentbaton/

</details>

<details>
<summary><b>10. AutoCompress: Automated Hardware-Guided Model Compression</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08290) • [📄 arXiv](https://arxiv.org/abs/2611.08290) • [📥 PDF](https://arxiv.org/pdf/2611.08290)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing AutoCompress: Automated Hardware-Guided Model Compression. Give it a model and a latency and memory constraint for your deployment, and AutoCompress automatically produces a compressed model that meets them. No manual architecture desi...

</details>

<details>
<summary><b>11. Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Chun-Mei Feng, Hongze Zhu, Wei Li, Cheng Tang, Junru Hu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09382) • [📄 arXiv](https://arxiv.org/abs/2611.09382) • [📥 PDF](https://arxiv.org/pdf/2611.09382)

**💻 Code:** [⭐ Code](https://github.com/WSP-Scope/WSP-Scope-Project) • [⭐ Code](https://github.com/huggingface)

> We systematically evaluate Weight-Space Programming through 16 editing trajectories across seven benchmarks and two model scales. Our results show uneven cross-task transfer, substantial variation across independent searches, and more limited gain...

</details>

<details>
<summary><b>12. Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaoqiu Wang, John Lam, Wenyi Li, Qingle Liu, Xinjie Lin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09017) • [📄 arXiv](https://arxiv.org/abs/2611.09017) • [📥 PDF](https://arxiv.org/pdf/2611.09017)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>13. PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36896) • [📄 arXiv](https://arxiv.org/abs/2610.36896) • [📥 PDF](https://arxiv.org/pdf/2610.36896)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present PREEN (Preset Regression via an Exemplar-based Editor Network), which casts color style transfer as regression onto the 29 parameters of a deterministic image editor. Given a content image and a style reference, PREEN predicts a preset,...

</details>

<details>
<summary><b>14. LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jun Wang, Martin Benfeghoul, Hugo Hazard, zfountas, teresadelgadoheras

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.07025) • [📄 arXiv](https://arxiv.org/abs/2611.07025) • [📥 PDF](https://arxiv.org/pdf/2611.07025)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lowram-model/lowram)

> We are excited to share LowRAM, our new KV cache compression method at test-time! LowRAM compresses keys using low-rank factorisation, while small per-head networks predict values from keys. We then keep residual corrections for the hardest-to-rec...

</details>

<details>
<summary><b>15. Hierarchical Residuals: A Minimalist Decoupling of Residual Width from Compute Width</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41711) • [📄 arXiv](https://arxiv.org/abs/2610.41711) • [📥 PDF](https://arxiv.org/pdf/2610.41711)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Residual connections underpin Transformers, but they implicitly tie the residual width carried through depth to the compute width used inside each layer. We introduce Hierarchical Residuals (HiRes), a minimalist architectural change that decouples...

</details>

<details>
<summary><b>16. Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yidan Huang, Yujin Zhou, Boqin Yin, Jingru Zeng, chuxuecao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09113) • [📄 arXiv](https://arxiv.org/abs/2611.09113) • [📥 PDF](https://arxiv.org/pdf/2611.09113)

**💻 Code:** [⭐ Code](https://github.com/ZJR-FZD/AgentDrift) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. "PRISM" Is Not All You Need: Cross-Topic Name Collisions and Scientific Paper Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01362) • [📄 arXiv](https://arxiv.org/abs/2611.01362) • [📥 PDF](https://arxiv.org/pdf/2611.01362)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Cross-Topic Name Collisions and Scientific Paper Retrieval

</details>

<details>
<summary><b>18. LLMs Don't Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06808) • [📄 arXiv](https://arxiv.org/abs/2611.06808) • [📥 PDF](https://arxiv.org/pdf/2611.06808)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 LLMs Don’t Know What They Know. Can We Trust Their Financial Predictions? Excited to share our latest research: 📄 LLMs Don’t Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting Large Language Models (LLMs) are inc...

</details>

<details>
<summary><b>19. OmniLatent: Unified Latent for 3D Part Modeling</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Minxiu Wang, Jiachen Xu, Zeqiang Lai, Yunfei Zhao, Yunhan Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09055) • [📄 arXiv](https://arxiv.org/abs/2611.09055) • [📥 PDF](https://arxiv.org/pdf/2611.09055)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. Learning to evolve by matching velocities</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00448) • [📄 arXiv](https://arxiv.org/abs/2611.00448) • [📥 PDF](https://arxiv.org/pdf/2611.00448)

**💻 Code:** [⭐ Code](https://github.com/farenga/velocity-matching) • [⭐ Code](https://github.com/huggingface)

> Can simulation be avoided when learning neural ODE surrogates of dynamical systems? We introduce Velocity Matching (VM), a simulation-free training objective with guarantees on the learned trajectories. Neural ODEs are usually trained on trajector...

</details>

<details>
<summary><b>21. Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT and LLM Layers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06844) • [📄 arXiv](https://arxiv.org/abs/2611.06844) • [📥 PDF](https://arxiv.org/pdf/2611.06844)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> New VLM Architecture

</details>

<details>
<summary><b>22. OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04720) • [📄 arXiv](https://arxiv.org/abs/2611.04720) • [📥 PDF](https://arxiv.org/pdf/2611.04720)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We are pleased to share our work, OneTrans-GSR! Paper page: https://huggingface.co/papers/2611.04720 arXiv: https://arxiv.org/abs/2611.04720 In this paper, we explore generative slate ranking for industrial recommender systems and propose OneTrans...

</details>

<details>
<summary><b>23. The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** YaoningYu, Fulucheng, Rushdog1, pennnnng, AllenJin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.07461) • [📄 arXiv](https://arxiv.org/abs/2611.07461) • [📥 PDF](https://arxiv.org/pdf/2611.07461)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> How can AI agents reliably solve real-world tasks end to end? We introduce Agent-Native Primitives, reusable building blocks that equip tools, code, knowledge, and other resources with their own LLM-powered experts. Building on this idea, HEELO dy...

</details>

<details>
<summary><b>24. Sketchpad: certified exact arithmetic with a small vision-language model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** mohsenvand

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04434) • [📄 arXiv](https://arxiv.org/abs/2611.04434) • [📥 PDF](https://arxiv.org/pdf/2611.04434)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NeoVand/sketchpad)

> Author here. Can a small model be proven exact at arithmetic on inputs of every length? 🧮 The theory If each step of a model reads only a bounded view of an external memory, exactness at all lengths reduces to exactness on a finite set of views . ...

</details>

<details>
<summary><b>25. Human-Centred, Risk-Constrained Evaluation of Financial Document Recognition: Evidence, Critical Errors, and Selective Automation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** learner-subodh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02775) • [📄 arXiv](https://arxiv.org/abs/2611.02775) • [📥 PDF](https://arxiv.org/pdf/2611.02775)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> How should we evaluate whether an AI system can be trusted to read financial documents and not merely transcribe them? Conventional OCR metrics such as character and word error rates capture transcription quality, but they can overlook something f...

</details>

<details>
<summary><b>26. Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Nikolaos Aletras, Constantinos Karouzos

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09634) • [📄 arXiv](https://arxiv.org/abs/2611.09634) • [📥 PDF](https://arxiv.org/pdf/2611.09634)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ckarouzos/lambdamix)

> 🤔 Post-training usually gives you one policy for one fixed weighting of objectives, but different users and settings call for different trade-offs. 🎛️  We introduce LambdaMix, a parameter-efficient method that learns a whole family of preference-c...

</details>

<details>
<summary><b>27. Knowing When to Teach: Learning from Teachable Prefixes in Multilingual Reasoning Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jaewon Chu, Jinwoo Seo, Jinyoung Park, Minseo Yoon, jaylacho

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08179) • [📄 arXiv](https://arxiv.org/abs/2611.08179) • [📥 PDF](https://arxiv.org/pdf/2611.08179)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Even when a teacher model has the reference solution, it can start following a student’s mistakes as they accumulate. We call this Teacher Drift, and we find that it tends to happen earlier in lower-resource languages. Our method, TOPSD, selects a...

</details>

<details>
<summary><b>28. Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.07723) • [📄 arXiv](https://arxiv.org/abs/2611.07723) • [📥 PDF](https://arxiv.org/pdf/2611.07723)

**💻 Code:** [⭐ Code](https://github.com/PROFOUND-HFMI/BILBY-MD) • [⭐ Code](https://github.com/huggingface)

> Can we trust a protein design just because its predicted structure looks correct? In our NeurIPS 2026 Evaluations & Datasets paper, we show why static motif-scaffolding benchmarks tell only part of the story. Of 55 statically successful design–pro...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 28 |
| 📅 Today | [`2026-11-09.json`](data/daily/2026-11-09.json) | 28 |
| 📆 This Week | [`2026-W45.json`](data/weekly/2026-W45.json) | 28 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 298 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-09 | 28 | [View JSON](data/daily/2026-11-09.json) |
| 📄 2026-11-08 | 32 | [View JSON](data/daily/2026-11-08.json) |
| 📄 2026-11-07 | 32 | [View JSON](data/daily/2026-11-07.json) |
| 📄 2026-11-06 | 24 | [View JSON](data/daily/2026-11-06.json) |
| 📄 2026-11-05 | 32 | [View JSON](data/daily/2026-11-05.json) |
| 📄 2026-11-04 | 43 | [View JSON](data/daily/2026-11-04.json) |
| 📄 2026-11-03 | 38 | [View JSON](data/daily/2026-11-03.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W45 | 28 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 298 | [View JSON](data/monthly/2026-11.json) |
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
