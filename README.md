<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-37-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5532+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">37</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">46</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">710</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5532+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 23, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale Tool Ecosystems</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.22388) • [📄 arXiv](https://arxiv.org/abs/2606.22388) • [📥 PDF](https://arxiv.org/pdf/2606.22388)

**💻 Code:** [⭐ Code](https://github.com/JiayuJeff/PlanBench-XL) • [⭐ Code](https://github.com/huggingface)

> Excited to share PlanBench-XL! We built this benchmark to evaluate whether LLM agents can really plan over long horizons in large, imperfect tool ecosystems, where they must iteratively retrieve tools, call them, and recover from missing, failing,...

</details>

<details>
<summary><b>2. EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23654) • [📄 arXiv](https://arxiv.org/abs/2606.23654) • [📥 PDF](https://arxiv.org/pdf/2606.23654)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/FrontisAI/EnterpriseClawBench)

> Most agent benchmarks use synthetic tasks. EnterpriseClawBench is distilled from a large archive of real proprietary workplace sessions, agents reading heterogeneous files, calling tools, and shipping actual business artifacts, turned into 852 rep...

</details>

<details>
<summary><b>3. KaLM-Reranker-V1: Fast but Not Late Interaction for Compressed Document Reranking</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.22807) • [📄 arXiv](https://arxiv.org/abs/2606.22807) • [📥 PDF](https://arxiv.org/pdf/2606.22807)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present KaLM-Reranker-V1, a fast but not late-interaction (FBNL) reranker that decouples query and passage computation while retaining expressive relevance modeling. Built on an encoder-decoder architecture, KaLM-Reranker-V1 uses the encoder to...

</details>

<details>
<summary><b>4. World Action Models: A Survey</b> ⭐ 217</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.20781) • [📄 arXiv](https://arxiv.org/abs/2606.20781) • [📥 PDF](https://arxiv.org/pdf/2606.20781)

**💻 Code:** [⭐ Code](https://github.com/world-action-models/awesome-world-action-models) • [⭐ Code](https://github.com/huggingface)

> World Action Models (WAMs) are embodied predictive-action models that make a forecast of the future available to action. Recent WAMs repurpose large video generation models, and a parallel line relies on language or vision-language backbones witho...

</details>

<details>
<summary><b>5. DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams</b> ⭐ 4</summary>

<br/>

**👥 Authors:** SongLin Dong, Jiangyang Li, Zijian Cai, Zeyu Guo, Cong Wan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21337) • [📄 arXiv](https://arxiv.org/abs/2606.21337) • [📥 PDF](https://arxiv.org/pdf/2606.21337)

**💻 Code:** [⭐ Code](https://github.com/vancyland/DataClaw0) • [⭐ Code](https://github.com/huggingface)

> Make any data you want

</details>

<details>
<summary><b>6. CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.22883) • [📄 arXiv](https://arxiv.org/abs/2606.22883) • [📥 PDF](https://arxiv.org/pdf/2606.22883)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce CLI-Universe, a principled synthesis engine that constructs terminal-agent tasks.

</details>

<details>
<summary><b>7. EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21649) • [📄 arXiv](https://arxiv.org/abs/2606.21649) • [📥 PDF](https://arxiv.org/pdf/2606.21649)

**💻 Code:** [⭐ Code](https://github.com/MiG-NJU/EvoEmbedding) • [⭐ Code](https://github.com/MiG-NJU/EvoEmbedding/tree/main) • [⭐ Code](https://github.com/huggingface)

> EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory

</details>

<details>
<summary><b>8. HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xu Shen, Yao Liu, Jingyi Shen, Wei Chen, tzt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.20097) • [📄 arXiv](https://arxiv.org/abs/2606.20097) • [📥 PDF](https://arxiv.org/pdf/2606.20097)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization

</details>

<details>
<summary><b>9. BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.22138) • [📄 arXiv](https://arxiv.org/abs/2606.22138) • [📥 PDF](https://arxiv.org/pdf/2606.22138)

**💻 Code:** [⭐ Code](https://github.com/QizhiPei/BioMatrix) • [⭐ Code](https://github.com/huggingface)

> We present BioMatrix, the first multimodal foundation model that natively integrates sequences, structures, and natural language for both molecules and proteins within a single decoder-only architecture. Existing biological foundation models pursu...

</details>

<details>
<summary><b>10. Learning from Your Own Mistakes: Constructing Learnable Micro-Reflective Trajectories for Self-Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18844) • [📄 arXiv](https://arxiv.org/abs/2606.18844) • [📥 PDF](https://arxiv.org/pdf/2606.18844)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. OpenRath: Session-Centered Runtime State for Agent Systems</b> ⭐ 659</summary>

<br/>

**👥 Authors:** Ruilin Xu, Zhijie Wang, smallkang2025

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19409) • [📄 arXiv](https://arxiv.org/abs/2606.19409) • [📥 PDF](https://arxiv.org/pdf/2606.19409)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Rath-Team/OpenRath)

> OpenRath proposes a PyTorch-like programming model for multi-agent, multi-session systems, centered on a first-class Session runtime value. Instead of reconstructing transcripts, tool traces, memory events, workspace placement, and branch provenan...

</details>

<details>
<summary><b>12. Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18648) • [📄 arXiv](https://arxiv.org/abs/2606.18648) • [📥 PDF](https://arxiv.org/pdf/2606.18648)

**💻 Code:** [⭐ Code](https://github.com/yigengjiang/physci-deepresearch) • [⭐ Code](https://github.com/huggingface)

> Excited to share our paper: Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark . We introduce PhySciBench , a benchmark for evaluating deep-research agents in the physical sciences, and DelveAgent , a modular m...

</details>

<details>
<summary><b>13. SkillHarness: Harnessing Safe Skills for Computer-Use Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.20636) • [📄 arXiv](https://arxiv.org/abs/2606.20636) • [📥 PDF](https://arxiv.org/pdf/2606.20636)

**💻 Code:** [⭐ Code](https://github.com/YurunChen/SkillHarness) • [⭐ Code](https://github.com/huggingface)

> We introduce SkillHarness, a framework for safer skill learning and reuse in computer-use agents. Existing skill-learning methods usually extract reusable skills from successful trajectories, but in dynamic environments this can encode unsafe beha...

</details>

<details>
<summary><b>14. DailyReport: An Open-ended Benchmark for Evaluating Search Agents on Daily Search Tasks</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Ziwen Wang, Mingyang Zhu, Wei Liu, Jingxuan Han, wagoriginal

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12871) • [📄 arXiv](https://arxiv.org/abs/2606.12871) • [📥 PDF](https://arxiv.org/pdf/2606.12871)

**💻 Code:** [⭐ Code](https://github.com/AGI-Eval-Official/DailyReport) • [⭐ Code](https://github.com/huggingface)

> Search Agents (SAs) typically leverage large language models (LLMs) to support complex information-seeking tasks by autonomously exploring web sources and synthesizing information into comprehensive responses. For SAs evaluation, prior benchmarks ...

</details>

<details>
<summary><b>15. Unlimited OCR Works</b> ⭐ 756</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23050) • [📄 arXiv](https://arxiv.org/abs/2606.23050) • [📥 PDF](https://arxiv.org/pdf/2606.23050)

**💻 Code:** [⭐ Code](https://github.com/baidu/Unlimited-OCR) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>16. Self-Compacting Language Model Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chuanyang Jin, Xi Wang, William Jurayj, Jingyu Zhang, Tianjian Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23525) • [📄 arXiv](https://arxiv.org/abs/2606.23525) • [📥 PDF](https://arxiv.org/pdf/2606.23525)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. PoLAR: Factorizing Extent and Mode in Latent Actions for Robot Policy Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21139) • [📄 arXiv](https://arxiv.org/abs/2606.21139) • [📥 PDF](https://arxiv.org/pdf/2606.21139)

**💻 Code:** [⭐ Code](https://github.com/joon-stack/PoLAR) • [⭐ Code](https://github.com/huggingface)

> PoLAR factorizes latent robot actions into radial extent and directional mode, so latent actions can separately capture how far a transition moves and what mode of behavior it follows. This gives a more structured latent space for downstream polic...

</details>

<details>
<summary><b>18. Exploring the Design Space of Reward Backpropagation for Flow Matching</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11075) • [📄 arXiv](https://arxiv.org/abs/2606.11075) • [📥 PDF](https://arxiv.org/pdf/2606.11075)

**💻 Code:** [⭐ Code](https://github.com/RuoyuWang-2077/FlowBP) • [⭐ Code](https://github.com/huggingface)

> We introduce FlowBP , a unified framework for direct reward backpropagation in flow-matching models. Instead of treating the backward pass as a fixed approximation, FlowBP makes the surrogate backward trajectory itself a design object, exposing fo...

</details>

<details>
<summary><b>19. Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23085) • [📄 arXiv](https://arxiv.org/abs/2606.23085) • [📥 PDF](https://arxiv.org/pdf/2606.23085)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Long-horizon tasks are common in real-world robotic deployments, yet failure detection for such tasks remains underexplored. Detecting failures in long-horizon robotic tasks is particularly challenging because failure onset is often ambiguous and ...

</details>

<details>
<summary><b>20. Training Open Models for Agentic Phone Use</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23049) • [📄 arXiv](https://arxiv.org/abs/2606.23049) • [📥 PDF](https://arxiv.org/pdf/2606.23049)

**💻 Code:** [⭐ Code](https://github.com/PhoneBuddyAI/phonebuddy) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>21. Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21906) • [📄 arXiv](https://arxiv.org/abs/2606.21906) • [📥 PDF](https://arxiv.org/pdf/2606.21906)

**💻 Code:** [⭐ Code](https://github.com/QwenLM/Confident-Decoding) • [⭐ Code](https://github.com/huggingface)

> 💡 Deeper is Not Always Better: Bypassing the "Alignment Tax" in LLMs Standard practice assumes that the deeper a layer is in an autoregressive LLM, the more accurate its token representation becomes. In our latest collaborative research in Qwen Te...

</details>

<details>
<summary><b>22. Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.20002) • [📄 arXiv](https://arxiv.org/abs/2606.20002) • [📥 PDF](https://arxiv.org/pdf/2606.20002)

**💻 Code:** [⭐ Code](https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod/examples/research_cod) • [⭐ Code](https://github.com/huggingface)

> To achieve a vision for LLM-based long-lifecycle agents, we present a general framework of end-to-end RL, our proof-of-concept implementations, and some promising empirical results. GitHub: https://github.com/agentscope-ai/Trinity-RFT/tree/researc...

</details>

<details>
<summary><b>23. Tmax: A simple recipe for terminal agents</b> ⭐ 58</summary>

<br/>

**👥 Authors:** Nathan Lambert, Teng Xiao, Rulin Shao, Junjie Oscar Yin, Hamish Ivison

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23321) • [📄 arXiv](https://arxiv.org/abs/2606.23321) • [📥 PDF](https://arxiv.org/pdf/2606.23321)

**💻 Code:** [⭐ Code](https://github.com/hamishivi/tmax) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>24. Causal Discovery in the Era of Agents</b> ⭐ 1.64k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23608) • [📄 arXiv](https://arxiv.org/abs/2606.23608) • [📥 PDF](https://arxiv.org/pdf/2606.23608)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/py-why/causal-learn)

> We propose an online agentic version for causal discovery,  which aims to discover causal relations based on observational data. The platform is available at causallearn.com.

</details>

<details>
<summary><b>25. Safe Few-Step Generation via Velocity Editing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23267) • [📄 arXiv](https://arxiv.org/abs/2606.23267) • [📥 PDF](https://arxiv.org/pdf/2606.23267)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project Page: https://uzn36.github.io/VESFlow/

</details>

<details>
<summary><b>26. Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11897) • [📄 arXiv](https://arxiv.org/abs/2606.11897) • [📥 PDF](https://arxiv.org/pdf/2606.11897)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Notes2Skills converts informal lab notebooks into source-linked, certainty-aware skills for scientific agents.

</details>

<details>
<summary><b>27. UniverSat: Resolution- and Modality-Agnostic Transformers for Earth Observation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Loic Landrieu, Clement Mallet, Nicolas Gonthier, Guillaume Astruc, Yohann Perron

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23503) • [📄 arXiv](https://arxiv.org/abs/2606.23503) • [📥 PDF](https://arxiv.org/pdf/2606.23503)

**💻 Code:** [⭐ Code](https://github.com/gastruc/UniverSat) • [⭐ Code](https://github.com/huggingface)

> Versatile Vision Transformer that uses a single Universal Patch Encoder to process satellite data from any sensor, modality, or resolution.

</details>

<details>
<summary><b>28. Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23557) • [📄 arXiv](https://arxiv.org/abs/2606.23557) • [📥 PDF](https://arxiv.org/pdf/2606.23557)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kaist-cvml/DR-MV3D)

> DR-MV3D introduces a map-grounded dense reward framework for multi-view 3D visual question answering, improving cross-view spatial reasoning by supervising global map construction, view-trajectory planning, and egocentric grounding with verifiable...

</details>

<details>
<summary><b>29. MeshFlow: Mesh Generation with Equivariant Flow Matching</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Alexander Rush, Qixing Huang, Jing Nathan Yan, Kiyohiro Nakayama, Qi Sun

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23489) • [📄 arXiv](https://arxiv.org/abs/2606.23489) • [📥 PDF](https://arxiv.org/pdf/2606.23489)

**💻 Code:** [⭐ Code](https://github.com/qiisun/MeshFlow) • [⭐ Code](https://github.com/huggingface)

> Excited to share MeshFlow — a new approach that can generate meshes with a fraction of seconds, while achieving state-of-the-art generation quality. Secret sources? Instead of autoregressive models, use equivariant flow-matching! Code and pretrain...

</details>

<details>
<summary><b>30. Tapered Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Aaron Courville, Ali Behrouz, Reza Bayat

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.23670) • [📄 arXiv](https://arxiv.org/abs/2606.23670) • [📥 PDF](https://arxiv.org/pdf/2606.23670)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>31. PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.22540) • [📄 arXiv](https://arxiv.org/abs/2606.22540) • [📥 PDF](https://arxiv.org/pdf/2606.22540)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/INCEPTIONwang/PolicyTrim)

> Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency. While existing efforts predominantly focus on compute-centric efficiency to red...

</details>

<details>
<summary><b>32. Counsel: A Meta-Evaluation Dataset for Agentic Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21627) • [📄 arXiv](https://arxiv.org/abs/2606.21627) • [📥 PDF](https://arxiv.org/pdf/2606.21627)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Meta-evaluating LLMJ critiques on agentic tasks, such as Tau-Bench

</details>

<details>
<summary><b>33. CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action and Learning in Knowledge-Intensive Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21777) • [📄 arXiv](https://arxiv.org/abs/2606.21777) • [📥 PDF](https://arxiv.org/pdf/2606.21777)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ashwinn-v/CalVerT)

> Excited to share CalVerT, a flexible+easy method that augments QA agents w/ telemetry about how certain and grounded their answers are. Works training-free (+3.7 F1 2Wiki, +4.7 WiTQA), and trained (+5.9 HotpotQA w/ GRPO) while cutting over retriev...

</details>

<details>
<summary><b>34. HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.22778) • [📄 arXiv](https://arxiv.org/abs/2606.22778) • [📥 PDF](https://arxiv.org/pdf/2606.22778)

**💻 Code:** [⭐ Code](https://github.com/hakari-bench/hakari-bench) • [⭐ Code](https://www.google.com/search?q=https://github.com/hakari-bench/hakari-bench) • [⭐ Code](https://github.com/huggingface)

> Evaluating and selecting the right retrieval configuration for RAG or semantic search has become notoriously difficult. While heavy-scale benchmarks like MTEB/MMTEB are comprehensive, they are too heavy to run repeatedly during iterative developme...

</details>

<details>
<summary><b>35. Improving Text-to-Music Generation with Human Preference Rewards</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.21670) • [📄 arXiv](https://arxiv.org/abs/2606.21670) • [📥 PDF](https://arxiv.org/pdf/2606.21670)

**💻 Code:** [⭐ Code](https://github.com/ntu-musicailab/ICME26-ATTM-GC-MeanAudio) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yonghyunk1m/TTM-HumanPref)

> Can a human preference reward improve a small text-to-music model, without new labels or scale up? Our ICME 2026 ATTM Grand Challenge (Efficiency Track) entry puts an open human preference reward ( TuneJury , trained on judgments from Music Arena ...

</details>

<details>
<summary><b>36. Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19750) • [📄 arXiv](https://arxiv.org/abs/2606.19750) • [📥 PDF](https://arxiv.org/pdf/2606.19750)

**💻 Code:** [⭐ Code](https://github.com/DarrienMcKenzie/manifold-bandits) • [⭐ Code](https://github.com/huggingface)

> Excited to share Manifold Bandits. When using RL to train LLMs, training efficiency depends not only on the strength of the policy optimization algorithm, but also on which problems the model sees at each point in training. Many adaptive curriculu...

</details>

<details>
<summary><b>37. FastMix: Fast Data Mixture Optimization via Gradient Descent</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14971) • [📄 arXiv](https://arxiv.org/abs/2606.14971) • [📥 PDF](https://arxiv.org/pdf/2606.14971)

**💻 Code:** [⭐ Code](https://github.com/hrtan/fastmix) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hrtan/fastmix%5D)

> Excited to share our team's (Tencent Hunyuan, HKU, CUHK) work from last year: "Fast Data Mixture Optimization via Gradient Descent", which has been accepted to ICLR 2026! TL;DR: We reformulate the data sampling ratio assignment into a bilevel opti...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 37 |
| 📅 Today | [`2026-06-23.json`](data/daily/2026-06-23.json) | 37 |
| 📆 This Week | [`2026-W25.json`](data/weekly/2026-W25.json) | 46 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 710 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-23 | 37 | [View JSON](data/daily/2026-06-23.json) |
| 📄 2026-06-22 | 9 | [View JSON](data/daily/2026-06-22.json) |
| 📄 2026-06-21 | 34 | [View JSON](data/daily/2026-06-21.json) |
| 📄 2026-06-20 | 34 | [View JSON](data/daily/2026-06-20.json) |
| 📄 2026-06-19 | 25 | [View JSON](data/daily/2026-06-19.json) |
| 📄 2026-06-18 | 16 | [View JSON](data/daily/2026-06-18.json) |
| 📄 2026-06-17 | 21 | [View JSON](data/daily/2026-06-17.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W25 | 46 | [View JSON](data/weekly/2026-W25.json) |
| 📅 2026-W24 | 194 | [View JSON](data/weekly/2026-W24.json) |
| 📅 2026-W23 | 247 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 710 | [View JSON](data/monthly/2026-06.json) |
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
