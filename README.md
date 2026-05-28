<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-39-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4661+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">39</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">122</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">897</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4661+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** May 28, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. ProRL: Effective Reinforcement Learning for Proactive Recommendation via Rectified Policy Gradient Estimation</b> ⭐ 28</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28293) • [📄 arXiv](https://arxiv.org/abs/2605.28293) • [📥 PDF](https://arxiv.org/pdf/2605.28293)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hongruhou89/ProRL)

> Standard policy gradients are fundamentally broken for proactive recommendation. ProRL fixes them with rectified gradient estimation. Proactive Recommender Systems aim to gradually shift user preferences toward target items through carefully desig...

</details>

<details>
<summary><b>2. Agent Explorative Policy Optimization for Multimodal Agentic Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28774) • [📄 arXiv](https://arxiv.org/abs/2605.28774) • [📥 PDF](https://arxiv.org/pdf/2605.28774)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AXPO (Agent Explorative Policy Optimization) addresses the thinking-acting gap in multimodal agentic reasoning by resampling tool calls in failed rollouts to improve training signal and model performance.

</details>

<details>
<summary><b>3. From Pixels to Words -- Towards Native One-Vision Models at Scale</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuwei Niu, Yuhao Dong, Penghao Wu, Jiahao Wang, Haiwen Diao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28820) • [📄 arXiv](https://arxiv.org/abs/2605.28820) • [📥 PDF](https://arxiv.org/pdf/2605.28820)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EvolvingLMMs-Lab/NEO)

> NEO-ov is a native encoder-free vision-language foundation model designed for single-image, multi-image, video understanding, and spatial intelligence. Unlike modular VLMs that connect separate image encoders and language decoders through multi-st...

</details>

<details>
<summary><b>4. Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28816) • [📄 arXiv](https://arxiv.org/abs/2605.28816) • [📥 PDF](https://arxiv.org/pdf/2605.28816)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Gamma-World is a generative multi-agent world model that uses Simplex Rotary Agent Encoding and Sparse Hub Attention for efficient, scalable, and action-conditioned interactive simulations.

</details>

<details>
<summary><b>5. Self-Improving Language Models with Bidirectional Evolutionary Search</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28814) • [📄 arXiv](https://arxiv.org/abs/2605.28814) • [📥 PDF](https://arxiv.org/pdf/2605.28814)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Embodied-Minds-Lab/BES)

> We propose Bidirectional Evolutionary Search (BES), a search framework that couples forward candidate evolution with backward goal decomposition.

</details>

<details>
<summary><b>6. ResearchMath-14K: Scaling Research-Level Mathematics via Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28003) • [📄 arXiv](https://arxiv.org/abs/2605.28003) • [📥 PDF](https://arxiv.org/pdf/2605.28003)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We release a collection of 14k research-level (mostly open) math . Link to Dataset: https://huggingface.co/datasets/amphora/ResearchMath-14k

</details>

<details>
<summary><b>7. MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28732) • [📄 arXiv](https://arxiv.org/abs/2605.28732) • [📥 PDF](https://arxiv.org/pdf/2605.28732)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zjunlp/MemTrace)

> We introduce MemTrace, a framework that traces how memories evolve inside LLM systems, automatically pinpoints where failures occur, and uses these signals to self-correct memory pipelines for more reliable long-term reasoning.

</details>

<details>
<summary><b>8. DenoiseRL: Bootstrapping Reasoning Models to Recover from Noisy Prefixes</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28421) • [📄 arXiv](https://arxiv.org/abs/2605.28421) • [📥 PDF](https://arxiv.org/pdf/2605.28421)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ALEX-nlp/DenoiseRL)

> Welcome everyone to join the discussion!

</details>

<details>
<summary><b>9. Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28775) • [📄 arXiv](https://arxiv.org/abs/2605.28775) • [📥 PDF](https://arxiv.org/pdf/2605.28775)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sujiikim/LearnWeak)

> We introduce LearnWeak, an automated training framework for domain specialization of small computer-use agents (CUAs) that requires no human trajectory annotation, constructs synthetic training datasets focused on the student’s weaknesses, and tra...

</details>

<details>
<summary><b>10. GEM: Generative Supervision Helps Embodied Intelligence</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28548) • [📄 arXiv](https://arxiv.org/abs/2605.28548) • [📥 PDF](https://arxiv.org/pdf/2605.28548)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhaorw02/GEM)

> Project Page: https://zhaorw02.github.io/GEM/ GitHub: https://github.com/zhaorw02/GEM Huggingface: https://huggingface.co/zzzrw/GEM-2B

</details>

<details>
<summary><b>11. ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.26340) • [📄 arXiv](https://arxiv.org/abs/2605.26340) • [📥 PDF](https://arxiv.org/pdf/2605.26340)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/scientist-one/generated-artifacts)

> We audited 75 AI-generated research papers and found that every baseline exhibits at least one systematic integrity failure: unsupported claims, fabricated citations, or method-code misalignment. ScientistOne introduces Chain-of-Evidence — every c...

</details>

<details>
<summary><b>12. OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28691) • [📄 arXiv](https://arxiv.org/abs/2605.28691) • [📥 PDF](https://arxiv.org/pdf/2605.28691)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PKU-YuanGroup/OSP-Next)

> Quick Overview:

</details>

<details>
<summary><b>13. Rethinking Memory as Continuously Evolving Connectivity</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28773) • [📄 arXiv](https://arxiv.org/abs/2605.28773) • [📥 PDF](https://arxiv.org/pdf/2605.28773)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce FluxMem, a self-evolving memory framework that continuously rewires and refines an agent’s memory connections through feedback and experience, enabling more adaptive and reliable long-term reasoning in dynamic environments.

</details>

<details>
<summary><b>14. Triplet-Block Diffusion RWKV</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Anyi Rao, Yunya Song, Zhaolong Su, Yiyang Luo, leonardklin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.25969) • [📄 arXiv](https://arxiv.org/abs/2605.25969) • [📥 PDF](https://arxiv.org/pdf/2605.25969)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/leonardodalinky/B3D-RWKV)

> B³D-RWKV tackles a fundamental tension in language model design: diffusion models need bidirectional attention, but efficient linear models like RWKV are strictly causal/unidirectional. This paper bridges that gap with a novel triplet-block layout...

</details>

<details>
<summary><b>15. Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28109) • [📄 arXiv](https://arxiv.org/abs/2605.28109) • [📥 PDF](https://arxiv.org/pdf/2605.28109)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce IB-Score, a novel metric grounded in Information Bottleneck theory that evaluates policy's exploration-exploitation balance by quantifying the trade-off between step-level reasoning diversity and mutual information shared with the cor...

</details>

<details>
<summary><b>16. LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28721) • [📄 arXiv](https://arxiv.org/abs/2605.28721) • [📥 PDF](https://arxiv.org/pdf/2605.28721)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Closed-book performance on BrowseComp vs. LiveBrowseComp

</details>

<details>
<summary><b>17. Guiding LLM Post-training Data Engineering with Model Internals from Sparse Autoencoders</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Lei Hou, Zijun Yao, Jinwu Hu, Zao Dai, Yi Jing

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27354) • [📄 arXiv](https://arxiv.org/abs/2605.27354) • [📥 PDF](https://arxiv.org/pdf/2605.27354)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper proposes a method to predict data diversity, difficulty, and quality with SAE signals, which guides LLM RL post-training data engineering.

</details>

<details>
<summary><b>18. Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.23163) • [📄 arXiv](https://arxiv.org/abs/2605.23163) • [📥 PDF](https://arxiv.org/pdf/2605.23163)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> End-to-end autonomous driving via Vision-Language-Action (VLA) models demands a precarious balance between high-fidelity trajectory planning and efficient inference. Existing paradigms typically fall short: autoregressive (AR) VLAs are memory-band...

</details>

<details>
<summary><b>19. HRBench: Benchmarking and Understanding Thinking-Mode Switch Strategies in Hybrid-Reasoning LLMs</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28398) • [📄 arXiv](https://arxiv.org/abs/2605.28398) • [📥 PDF](https://arxiv.org/pdf/2605.28398)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/usail-hkust/HRBench)

> This paper introduces HRBench, a unified evaluation framework for studying thinking-mode switching in hybrid reasoning LLMs.

</details>

<details>
<summary><b>20. OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yizhen Zhang, Chufan Shi, Jiale Liu, Bowei Liu, Xinchen Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28805) • [📄 arXiv](https://arxiv.org/abs/2605.28805) • [📥 PDF](https://arxiv.org/pdf/2605.28805)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Cominclip/OmniVerifier)

> Code: https://github.com/Cominclip/OmniVerifier

</details>

<details>
<summary><b>21. Less is More: Early Stopping Rollout for On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27028) • [📄 arXiv](https://arxiv.org/abs/2605.27028) • [📥 PDF](https://arxiv.org/pdf/2605.27028)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Early stopping method for OPD! The paper diagnoses the "Off-policy Teacher Decay" problem for On-policy Distillation(OPD) - the later position in the trajectory is actually harmful! This is because the trajectory from the student is off-policy to ...

</details>

<details>
<summary><b>22. VibeSearchBench: Benchmarking Long-horizon Proactive Search in the Wild</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27882) • [📄 arXiv](https://arxiv.org/abs/2605.27882) • [📥 PDF](https://arxiv.org/pdf/2605.27882)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VibeBench/VibeSearchBench)

> 🚀 Introducing VibeSearchBench — a new benchmark that exposes a striking gap between how LLM agents are evaluated and how real users actually search. 💡 The problem. Today's search benchmarks (BrowseComp, WideSearch, DeepSearchQA…) all assume over-s...

</details>

<details>
<summary><b>23. GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27491) • [📄 arXiv](https://arxiv.org/abs/2605.27491) • [📥 PDF](https://arxiv.org/pdf/2605.27491)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AgibotTech/GE-Sim-V2)

> Project Page: https://ge-sim-v2.github.io/

</details>

<details>
<summary><b>24. Lost in Sampling: Assessing Lexical Reachability in LLMs via the Word Coverage Score (WCS)</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Javier Coronado-Blázquez, Tairan Fu, Carlos Arriaga, Javier Conde, Samer Awad

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27268) • [📄 arXiv](https://arxiv.org/abs/2605.27268) • [📥 PDF](https://arxiv.org/pdf/2605.27268)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Modern Large Language Models (LLMs) are often criticized for producing repetitive and homogeneous text, despite possessing vast latent vocabularies. While previous research has focused on model knowledge and training data, we investigate the role ...

</details>

<details>
<summary><b>25. SkillGrad: Optimizing Agent Skills Like Gradient Descent</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jinghui Chen, Lu Lin, Bochuan Cao, Yifan Lan, Hanyu Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27760) • [📄 arXiv](https://arxiv.org/abs/2605.27760) • [📥 PDF](https://arxiv.org/pdf/2605.27760)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> SkillGrad views agent skills as optimizable parameters and improves them through iterative trajectory analysis, textual momentum, and skill patching. It significantly outperforms related methods without changing model weights.

</details>

<details>
<summary><b>26. Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal Coefficient Calibration</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Shiming Xiang, Xiaohan Wang, Lin Chen, Jiajun Chai, Zili Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28184) • [📄 arXiv](https://arxiv.org/abs/2605.28184) • [📥 PDF](https://arxiv.org/pdf/2605.28184)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MarkXCloud/RL-MTP)

> No abstract available.

</details>

<details>
<summary><b>27. CubePart: An Open-Vocabulary Part-Controllable 3D Generator</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Daiqing Li, Inaki Navarro, Jean-Philippe Fauconnier, Kangle Deng, Yiheng Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28763) • [📄 arXiv](https://arxiv.org/abs/2605.28763) • [📥 PDF](https://arxiv.org/pdf/2605.28763)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Roblox/cube/tree/main/cubepart)

> Github: https://github.com/Roblox/cube/tree/main/cubepart

</details>

<details>
<summary><b>28. AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Nicole Koenigstein

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27466) • [📄 arXiv](https://arxiv.org/abs/2605.27466) • [📥 PDF](https://arxiv.org/pdf/2605.27466)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Nicolepcx/AgensFlow)

> AgensFlow introduces an open-source coordination-policy substrate for multi-agent systems. Instead of hard-coding agent workflows upfront, the framework keeps the underlying models frozen and learns over the coordination graph: model × skill × rol...

</details>

<details>
<summary><b>29. Chartographer: Counterfactual Chart Generation for Evaluating Vision-Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Freda Shi, Jesse C. Cresswell, Dae Yon Hwang, Yifan Jiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27311) • [📄 arXiv](https://arxiv.org/abs/2605.27311) • [📥 PDF](https://arxiv.org/pdf/2605.27311)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> interesting read

</details>

<details>
<summary><b>30. ESC-Skills: Discovering and Self-Evolving Skills for Emotional Support Conversations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27908) • [📄 arXiv](https://arxiv.org/abs/2605.27908) • [📥 PDF](https://arxiv.org/pdf/2605.27908)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aliyun/qwen-dianjin)

> ESC-Skills: Discovering and Self-Evolving Skills for Emotional Support Conversations

</details>

<details>
<summary><b>31. PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28819) • [📄 arXiv](https://arxiv.org/abs/2605.28819) • [📥 PDF](https://arxiv.org/pdf/2605.28819)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Sphere-AI-Lab/PEFT-Arena)

> A stability-plasticity benchmark and geometry-based diagnosis of parameter-efficient finetuning.

</details>

<details>
<summary><b>32. AI Research Agents Narrow Scientific Exploration</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yi Yang, Yixuan Tang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27905) • [📄 arXiv](https://arxiv.org/abs/2605.27905) • [📥 PDF](https://arxiv.org/pdf/2605.27905)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ⚠️ AI research agents promise to accelerate science, but this study finds they actually narrow it. What do you think it would take for AI agents to genuinely broaden scientific exploration? 🤗

</details>

<details>
<summary><b>33. Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.26457) • [📄 arXiv](https://arxiv.org/abs/2605.26457) • [📥 PDF](https://arxiv.org/pdf/2605.26457)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/formal-verif-is-cool/verus-spec-gym)

> We release VERUS-SpecBench and VERUS-SpecGym, a benchmark and agentic environment for evaluating whether language models can translate informal programming intent into faithful Verus specifications. The core contribution is an executable-specifica...

</details>

<details>
<summary><b>34. Advancing Creative Physical Intelligence in Large Multimodal Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.26396) • [📄 arXiv](https://arxiv.org/abs/2605.26396) • [📥 PDF](https://arxiv.org/pdf/2605.02910)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/CreativityBench/MM-CreativityBench)

> Paper: https://arxiv.org/pdf/2605.26396 Website: https://creativitybench.github.io/mm-creativitybench.github.io/ Github: https://github.com/CreativityBench/MM-CreativityBench CreativityBench (First Release): https://arxiv.org/pdf/2605.02910

</details>

<details>
<summary><b>35. AgentFugue: Agent Scaling for Long-Horizon Tasks through Collective Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tong Zhao, Jiongnan Liu, Shuting Wang, Hongjin Qian, Yuyang Hu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.24486) • [📄 arXiv](https://arxiv.org/abs/2605.24486) • [📥 PDF](https://arxiv.org/pdf/2605.24486)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Recent progress on long-horizon agentic tasks has been driven largely by scaling up individual agents through stronger models, better tools, and more effective scaffolding. In contrast, much less is understood about scaling out: whether multiple p...

</details>

<details>
<summary><b>36. AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28655) • [📄 arXiv](https://arxiv.org/abs/2605.28655) • [📥 PDF](https://arxiv.org/pdf/2605.28655)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AutoScientists is a decentralized team of AI agents that self-organizes to perform long-running scientific experimentation, improving exploration efficiency across biomedical and machine learning optimization tasks.

</details>

<details>
<summary><b>37. Revealing Algorithmic Deductive Circuits for Logical Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Naoya Inoue, Tien Huu Dang, Phuong Minh Nguyen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27824) • [📄 arXiv](https://arxiv.org/abs/2605.27824) • [📥 PDF](https://arxiv.org/pdf/2605.27824)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Revealing Algorithmic Deductive Circuits for Logical Reasoning

</details>

<details>
<summary><b>38. Clark Hash: Stateless Sparse Johnson-Lindenstrauss Quantization for Neural Embeddings</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Clark Labs Inc, Stanislav Kirdey

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28034) • [📄 arXiv](https://arxiv.org/abs/2605.28034) • [📥 PDF](https://arxiv.org/pdf/2605.28034)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/clark-labs-inc/clark-hash)

> Paper: Clark Hash: Stateless Sparse Johnson-Lindenstrauss Quantization for Neural Embeddings arXiv: 2605.28034 [cs.AI] Author: Stanislav Kirdey, Clark Labs Inc Date: 2026-05-28

</details>

<details>
<summary><b>39. PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Weifeng Su, Yiu-ming Cheung, Hongmin Cai, Junli Gong, Yuchen Guo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27762) • [📄 arXiv](https://arxiv.org/abs/2605.27762) • [📥 PDF](https://arxiv.org/pdf/2605.27762)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 39 |
| 📅 Today | [`2026-05-28.json`](data/daily/2026-05-28.json) | 39 |
| 📆 This Week | [`2026-W21.json`](data/weekly/2026-W21.json) | 122 |
| 🗓️ This Month | [`2026-05.json`](data/monthly/2026-05.json) | 897 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-05-28 | 39 | [View JSON](data/daily/2026-05-28.json) |
| 📄 2026-05-27 | 28 | [View JSON](data/daily/2026-05-27.json) |
| 📄 2026-05-26 | 34 | [View JSON](data/daily/2026-05-26.json) |
| 📄 2026-05-25 | 21 | [View JSON](data/daily/2026-05-25.json) |
| 📄 2026-05-24 | 49 | [View JSON](data/daily/2026-05-24.json) |
| 📄 2026-05-23 | 49 | [View JSON](data/daily/2026-05-23.json) |
| 📄 2026-05-22 | 31 | [View JSON](data/daily/2026-05-22.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W21 | 122 | [View JSON](data/weekly/2026-W21.json) |
| 📅 2026-W20 | 243 | [View JSON](data/weekly/2026-W20.json) |
| 📅 2026-W19 | 310 | [View JSON](data/weekly/2026-W19.json) |
| 📅 2026-W18 | 158 | [View JSON](data/weekly/2026-W18.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-05 | 897 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
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
