<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-36-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5107+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">36</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">62</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">285</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5107+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 09, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. SWE-Explore: Benchmarking How Coding Agents Explore Repositories</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.07297) • [📄 arXiv](https://arxiv.org/abs/2606.07297) • [📥 PDF](https://arxiv.org/pdf/2606.07297)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Qiushao-E/SWE-Explore-Bench)

> Is your coding agent good at exploring repositories?

</details>

<details>
<summary><b>2. On the Geometry of On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.07082) • [📄 arXiv](https://arxiv.org/abs/2606.07082) • [📥 PDF](https://arxiv.org/pdf/2606.07082)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> On-policy distillation (OPD) is increasingly used to improve large language model reasoning, but its training dynamics remain poorly understood. We characterize the trajectory of OPD updates in parameter space and compare it with supervised fine-t...

</details>

<details>
<summary><b>3. Latent Spatial Memory for Video World Models</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09828) • [📄 arXiv](https://arxiv.org/abs/2606.09828) • [📥 PDF](https://arxiv.org/pdf/2606.09828)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/microsoft/LatentSpatialMemory)

> Latent Spatial Memory stores persistent 3D scene content directly as latent tokens in video world models.

</details>

<details>
<summary><b>4. LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Rong Shan, Zihan Guo, Tianyi Xu, Chenyu Zhou, Aofan Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06087) • [📄 arXiv](https://arxiv.org/abs/2606.06087) • [📥 PDF](https://arxiv.org/pdf/2606.06087)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Shanghai Jiao Tong University, Sun Yat-sen University, Shanghai Innovation Institute, and OPPO Research Institute unveil LatentSkil, turning agent text skills into plug-and-play weight skills.

</details>

<details>
<summary><b>5. CoVEBench: Can Video Editing Models Handle Complex Instructions?</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08415) • [📄 arXiv](https://arxiv.org/abs/2606.08415) • [📥 PDF](https://arxiv.org/pdf/2606.08415)

**💻 Code:** [⭐ Code](https://github.com/NJU-LINK/CoVEBench) • [⭐ Code](https://github.com/huggingface)

> We introduce CoVEBench, a fine-grained checklist benchmark to evaluate text-guided video editing models on complex, compositional instructions.

</details>

<details>
<summary><b>6. FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09079) • [📄 arXiv](https://arxiv.org/abs/2606.09079) • [📥 PDF](https://arxiv.org/pdf/2606.09079)

**💻 Code:** [⭐ Code](https://github.com/libertywing/FlashMemory-Deepseek-V4) • [⭐ Code](https://github.com/huggingface)

> Conventional LLMs keep the full KV cache loaded during decoding, causing a severe GPU memory bottleneck for ultra-long context serving. In this report, we propose Lookahead Sparse Attention (LSA), a novel inference paradigm powered by a Neural Mem...

</details>

<details>
<summary><b>7. SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09669) • [📄 arXiv](https://arxiv.org/abs/2606.09669) • [📥 PDF](https://arxiv.org/pdf/2606.09669)

**💻 Code:** [⭐ Code](https://github.com/Hongcheng-Gao/SpatialWorld/blob/main/SpatialWorld.pdf) • [⭐ Code](https://github.com/Hongcheng-Gao/SpatialWorld) • [⭐ Code](https://github.com/huggingface)

> The paper can be also found in https://github.com/Hongcheng-Gao/SpatialWorld/blob/main/SpatialWorld.pdf

</details>

<details>
<summary><b>8. Human Psychometric Questionnaires Mischaracterize LLM Behavior</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2509.10078) • [📄 arXiv](https://arxiv.org/abs/2509.10078) • [📥 PDF](https://arxiv.org/pdf/2509.10078)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We examine whether human psychometric questionnaires can serve as reliable tools for characterizing and predicting LLM behavior in everyday user interactions. We analyze eight open-source LLMs by comparing their value and personality profiles deri...

</details>

<details>
<summary><b>9. Echo-Memory: A Controlled Study of Memory in Action World Models</b> ⭐ 78</summary>

<br/>

**👥 Authors:** Haoran Li, Jie Huang, Yuxuan Bian, Zeyue Xue, Wayne King

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09803) • [📄 arXiv](https://arxiv.org/abs/2606.09803) • [📥 PDF](https://arxiv.org/pdf/2606.09803)

**💻 Code:** [⭐ Code](https://github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Memory) • [⭐ Code](https://github.com/huggingface)

> Echo-Memory is a controlled study that systematically evaluates memory mechanisms in action-conditioned world models to address challenges in long-term scene consistency and object retention.

</details>

<details>
<summary><b>10. OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09826) • [📄 arXiv](https://arxiv.org/abs/2606.09826) • [📥 PDF](https://arxiv.org/pdf/2606.09826)

**💻 Code:** [⭐ Code](https://github.com/mxlin043/OmniGameArena) • [⭐ Code](https://github.com/huggingface)

> OmniGameArena is a real-time benchmark of 12 new Unreal Engine 5 games (7 Solo, 3 PvP, 2 Coop). They share one action interface, so commercial VLMs, open-weight VLMs, and specialized game policies are all tested the same way. On top of the cold-st...

</details>

<details>
<summary><b>11. AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09811) • [📄 arXiv](https://arxiv.org/abs/2606.09811) • [📥 PDF](https://arxiv.org/pdf/2606.09811)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> At a Glance: Make world-action models fast enough for real-time robot control. Use a slow video DiT as a reusable long-horizon world planner and a fast action DiT as a closed-loop executor. Adapt cached planner context to the current observation t...

</details>

<details>
<summary><b>12. Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08348) • [📄 arXiv](https://arxiv.org/abs/2606.08348) • [📥 PDF](https://arxiv.org/pdf/2606.08348)

**💻 Code:** [⭐ Code](https://github.com/DataArcTech/Bayesian-Agent) • [⭐ Code](https://github.com/huggingface)

> Bayesian vs. Frequentist for Skill Evolving: Injecting a Cumulative, Auditable, and Transferable Belief State The greatest advantage of the Bayesian approach for skill evolving is that it goes beyond the stateless "observe failure → patch" cycle. ...

</details>

<details>
<summary><b>13. Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Yihao Liu, Siyuan Huang, Pengyu Cheng, Gangwei Jiang, Tao Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03980) • [📄 arXiv](https://arxiv.org/abs/2606.03980) • [📥 PDF](https://arxiv.org/pdf/2606.03980)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Qwen-Applications/Skill-RM)

> Reward models (RMs) provide critical feedback signals for LLM post-training, notably in reinforced fine-tuning (RFT) and reinforcement learning (RL) pipelines. However, current reward evaluation relies on heterogeneous criteria such as rule-based ...

</details>

<details>
<summary><b>14. SwiftVR: Real-Time One-Step Generative Video Restoration</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Chi Zhang, Haibin Huang, Xinlin Zhong, Xiangyu Chen, Jiaqi Yan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09516) • [📄 arXiv](https://arxiv.org/abs/2606.09516) • [📥 PDF](https://arxiv.org/pdf/2606.09516)

**💻 Code:** [⭐ Code](https://github.com/H-oliday/SwiftVR) • [⭐ Code](https://github.com/huggingface)

> SwiftVR is a one-step generative video restoration framework designed for real-time streaming. While recent one-step diffusion methods reduce the number of denoising steps, they still struggle with high-resolution deployment due to expensive spati...

</details>

<details>
<summary><b>15. SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yue Shen, Jie Feng, Dan Yang, Junjie Wang, Zequn Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.07074) • [📄 arXiv](https://arxiv.org/abs/2606.07074) • [📥 PDF](https://arxiv.org/pdf/2606.07074)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> slim searcher for search agent efficiency

</details>

<details>
<summary><b>16. Answer Presence Drives RAG Rewriting Gains</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yueping He, Li Zhang, Ke Yang, Yueying Hua, Yuejie Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05633) • [📄 arXiv](https://arxiv.org/abs/2606.05633) • [📥 PDF](https://arxiv.org/pdf/2606.05633)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Primary Contribution The paper does not propose a new mitigation or rewriter. Instead, it provides a rigorous evaluation standard, releasing the intervention runner and sentinel panel so that future claims of rewriter-driven gains can be strictly ...

</details>

<details>
<summary><b>17. End-to-End Context Compression at Scale</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Zaiqian Chen, Nimit Kalra, Haozhe Chen, Sean McLeish, Ang Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09659) • [📄 arXiv](https://arxiv.org/abs/2606.09659) • [📥 PDF](https://arxiv.org/pdf/2606.09659)

**💻 Code:** [⭐ Code](https://github.com/LeonLixyz/LCLM) • [⭐ Code](https://github.com/huggingface)

> Introduces Latent Context Language Models (LCLMs), an encoder-decoder framework that compresses long-context prompts into compact latent embeddings, significantly improving efficiency for memory-constrained LLM inference and long-horizon agentic t...

</details>

<details>
<summary><b>18. Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09380) • [📄 arXiv](https://arxiv.org/abs/2606.09380) • [📥 PDF](https://arxiv.org/pdf/2606.09380)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Trace tournaments can provide denser reward signals when verifier rewards are identical.

</details>

<details>
<summary><b>19. Trajectory-Refined Distillation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08432) • [📄 arXiv](https://arxiv.org/abs/2606.08432) • [📥 PDF](https://arxiv.org/pdf/2606.08432)

**💻 Code:** [⭐ Code](https://github.com/louieworth/trd) • [⭐ Code](https://github.com/huggingface)

> On-policy distillation (OPD) has become a central post-training tool for large language models (LLMs), providing dense per-token teacher supervision along the student's own rollouts. In this work, we identify a common structural cause underlying O...

</details>

<details>
<summary><b>20. DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning</b> ⭐ 32</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.07299) • [📄 arXiv](https://arxiv.org/abs/2606.07299) • [📥 PDF](https://arxiv.org/pdf/2606.07299)

**💻 Code:** [⭐ Code](https://github.com/baidubce/qianfan-deepresearch) • [⭐ Code](https://github.com/huggingface)

> Deep Research technical report by the DuMate Team.

</details>

<details>
<summary><b>21. Why Muon Outperforms Adam: A Curvature Perspective</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhuoran Yang, Dirk Bergemann, Jiaxiang Li, Fengzhuo Zhang, Shuche Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04662) • [📄 arXiv](https://arxiv.org/abs/2606.04662) • [📥 PDF](https://arxiv.org/pdf/2606.04662)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Muon improves training efficiency over Adam in large language-model training by about two times, but the local geometric source of this advantage remains unclear. Our work takes a first step toward demystifying Muon's superiority over Adam from a ...

</details>

<details>
<summary><b>22. Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Srishti Yadav, Wm. Matthew Kennedy, Jenny Chim, Anka Reuel, Avijit Ghosh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09809) • [📄 arXiv](https://arxiv.org/abs/2606.09809) • [📥 PDF](https://arxiv.org/pdf/2606.09809)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Evaluation Cards provide a structured, operational reporting layer for AI evaluation, improving transparency and comparability by integrating benchmark, model, and run metadata into a unified, interpretable record.

</details>

<details>
<summary><b>23. Optical Reasoning: Rethinking Images as an Expressive Reasoning Medium Beyond Text</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09585) • [📄 arXiv](https://arxiv.org/abs/2606.09585) • [📥 PDF](https://arxiv.org/pdf/2606.09585)

**💻 Code:** [⭐ Code](https://github.com/ModalityDance/Optical-Reasoning) • [⭐ Code](https://github.com/huggingface)

> Optical reasoning introduces a new paradigm that uses images alone as an expressive reasoning medium for both language and multimodal tasks, moving beyond text-based and interleaved-modal Chain-of-Thought reasoning. With typographic and graphical ...

</details>

<details>
<summary><b>24. Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fanrui Zhang, Zekai Lin, Yujie Zhang, Wenjie Li, Haoran Sun

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09365) • [📄 arXiv](https://arxiv.org/abs/2606.09365) • [📥 PDF](https://arxiv.org/pdf/2606.09365)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> SkeMex is a training-free self-evolution framework that allows medical agents to accumulate, organize, and reuse valuable reasoning skills from experience, leading to more effective and generalizable clinical decision-making.

</details>

<details>
<summary><b>25. Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08960) • [📄 arXiv](https://arxiv.org/abs/2606.08960) • [📥 PDF](https://arxiv.org/pdf/2606.08960)

**💻 Code:** [⭐ Code](https://github.com/few-sh/harden-v0) • [⭐ Code](https://github.com/huggingface)

> Automatically hardening benchmarks and training environments with the hacker–fixer loop. Paper: https://arxiv.org/abs/2606.08960 Code: https://github.com/few-sh/harden-v0

</details>

<details>
<summary><b>26. PBSD: Privileged Bayesian Self-Distillation for Long-Horizon Credit Assignment</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09348) • [📄 arXiv](https://arxiv.org/abs/2606.09348) • [📥 PDF](https://arxiv.org/pdf/2606.09348)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Long-horizon agentic tasks pose a fundamental credit assignment challenge for outcome-base reinforcement learning: trajectory-level rewards verify final correctness but provide limited guidance on which intermediate reasoning steps or tool interac...

</details>

<details>
<summary><b>27. OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chenyun Zhang, Jiyuan Shi, Weiji Xie, Jiakun Zheng, Zehao Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08548) • [📄 arXiv](https://arxiv.org/abs/2606.08548) • [📥 PDF](https://arxiv.org/pdf/2606.08548)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> OASIS is a framework that leverages 3D generative asset reconstruction and simulation-based teleoperation to train high-performance, zero-shot visuomotor policies for humanoid loco-manipulation tasks.

</details>

<details>
<summary><b>28. Chiaroscuro Attention: Spending Compute in the Dark</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08327) • [📄 arXiv](https://arxiv.org/abs/2606.08327) • [📥 PDF](https://arxiv.org/pdf/2606.08327)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A few threads I'd love to explore with the community: Routing collapse as a design principle — the router rejected RBF entirely and the purpose-built DCT+Attn variant beat all 3-operator versions. Has anyone seen analogous collapse behaviour in Mo...

</details>

<details>
<summary><b>29. Cosine Misleads: Auxiliary Losses Reshape Vision Language Models, Not Their Latents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05753) • [📄 arXiv](https://arxiv.org/abs/2606.05753) • [📥 PDF](https://arxiv.org/pdf/2606.05753)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/xiuyuz/cosine-misleads)

> Latent visual reasoning (LVR) inserts supervised latent tokens between perception and answer generation in vision-language models (VLMs). The field uses alignment between these latents and their visual targets, i.e., cosine similarity or mean squa...

</details>

<details>
<summary><b>30. Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05122) • [📄 arXiv](https://arxiv.org/abs/2606.05122) • [📥 PDF](https://arxiv.org/pdf/2606.05122)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YiShan05/SEE_official)

> Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own output? We find that the ability is largely present before any targeted training: prompted few-shot, a...

</details>

<details>
<summary><b>31. Text-to-Image Models Need Less from Text Encoders Than You Think</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tomer Michaeli, Tamar Rott Shaham, Noa Cohen, Nurit Spingarn

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03715) • [📄 arXiv](https://arxiv.org/abs/2606.03715) • [📥 PDF](https://arxiv.org/pdf/2606.03715)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Text-to-image models rely on text prompts as their primary interface to human intent. Prompts are encoded by a text encoder into embeddings that condition the image generation process. Beyond individual token meanings, text embeddings encode conte...

</details>

<details>
<summary><b>32. Lean4Agent: Formal Modeling and Verification for Agent Workflow and Trajectory</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06523) • [📄 arXiv](https://arxiv.org/abs/2606.06523) • [📥 PDF](https://arxiv.org/pdf/2606.06523)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RickySkywalker/Lean4Agent)

> This paper introduces Lean4Agent , to the best of our knowledge, the first framework that uses Lean4 to model and verify agent behavior. Lean4Agent introduces FormalAgentLib , an extensible Lean4 library for formally modeling and verifying agent w...

</details>

<details>
<summary><b>33. PIPE-Cypher: Automatic Enterprise Benchmark Generation for Text-to-Cypher Systems</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08481) • [📄 arXiv](https://arxiv.org/abs/2606.08481) • [📥 PDF](https://arxiv.org/pdf/2606.08481)

**💻 Code:** [⭐ Code](https://github.com/suraj-ranganath/PIPE-Cypher) • [⭐ Code](https://github.com/huggingface)

> PIPE-Cypher is a synthetic data pipeline that creates balanced, executable, privacy-aware NL-to-Cypher benchmarks for enterprise knowledge graphs. The value here is that enterprise graphs are highly differentiated: their schemas, terminology, quer...

</details>

<details>
<summary><b>34. Set-Based Transformer for Atmospheric Compensation in Standoff LWIR Hyperspectral Imaging</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hoover Rueda-Chacon, Jeferson Acevedo, Nicolas Quintero, Fabian Perez

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08324) • [📄 arXiv](https://arxiv.org/abs/2606.08324) • [📥 PDF](https://arxiv.org/pdf/2606.08324)

**💻 Code:** [⭐ Code](https://github.com/Factral/SAE-LWIR) • [⭐ Code](https://github.com/huggingface)

> github: https://github.com/Factral/SAE-LWIR

</details>

<details>
<summary><b>35. Honest Lying: Understanding Memory Confabulation in Reflexive Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.29463) • [📄 arXiv](https://arxiv.org/abs/2605.29463) • [📥 PDF](https://arxiv.org/pdf/2605.29463)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Reflexion-style agents rely on self-generated reflections as memory, implicitly assuming that agents can accurately diagnose their own failures. We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store conf...

</details>

<details>
<summary><b>36. EMMA: Extracting Multiple physical parameters from Multimodal Data</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.24047) • [📄 arXiv](https://arxiv.org/abs/2605.24047) • [📥 PDF](https://arxiv.org/pdf/2605.24047)

**💻 Code:** [⭐ Code](https://github.com/ImpactLabASU/EMMA-CVPR2026) • [⭐ Code](https://github.com/huggingface)

> To the best of our knowledge this is the first work towards multi-modal physics parameter estimation. Published in CVPR 2026

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 36 |
| 📅 Today | [`2026-06-09.json`](data/daily/2026-06-09.json) | 36 |
| 📆 This Week | [`2026-W23.json`](data/weekly/2026-W23.json) | 62 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 285 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-09 | 36 | [View JSON](data/daily/2026-06-09.json) |
| 📄 2026-06-08 | 26 | [View JSON](data/daily/2026-06-08.json) |
| 📄 2026-06-07 | 50 | [View JSON](data/daily/2026-06-07.json) |
| 📄 2026-06-06 | 0 | [View JSON](data/daily/2026-06-06.json) |
| 📄 2026-06-05 | 33 | [View JSON](data/daily/2026-06-05.json) |
| 📄 2026-06-04 | 32 | [View JSON](data/daily/2026-06-04.json) |
| 📄 2026-06-03 | 21 | [View JSON](data/daily/2026-06-03.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W23 | 62 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |
| 📅 2026-W20 | 243 | [View JSON](data/weekly/2026-W20.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 285 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |

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
