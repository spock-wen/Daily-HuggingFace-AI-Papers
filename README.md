<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-83-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7689+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">83</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">107</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">709</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7689+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 29, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35347) • [📄 arXiv](https://arxiv.org/abs/2609.35347) • [📥 PDF](https://arxiv.org/pdf/2609.35347)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LiXin97/DN-MOPD)

> Project page: https://lixin.ai/DN-MOPD/ . Code: https://github.com/LiXin97/DN-MOPD

</details>

<details>
<summary><b>2. YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33757) • [📄 arXiv](https://arxiv.org/abs/2609.33757) • [📥 PDF](https://arxiv.org/pdf/2609.33757)

**💻 Code:** [⭐ Code](https://github.com/multimodal-art-projection/YuE/blob/main/docs/technical_report.pdf) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/multimodal-art-projection/YuE)

> We're sharing the YuE2 technical report. YuE2 unifies symbolic and audio music generation: it first writes an editable melody-and-chord score, then renders a full song with vocals and accompaniment. The same model supports zero-shot covers and sco...

</details>

<details>
<summary><b>3. Post-Training Leaves Behavioral Shadows on Unrelated Decisions</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.29233) • [📄 arXiv](https://arxiv.org/abs/2609.29233) • [📥 PDF](https://arxiv.org/pdf/2609.29233)

**💻 Code:** [⭐ Code](https://github.com/myboker/ATD) • [⭐ Code](https://github.com/huggingface)

> Can a model teach another model to code — without ever showing it code? Surprisingly, yes. A coding-trained teacher answers thousands of unrelated prompts with just one word each. A student trained only on those answers gets better at coding — des...

</details>

<details>
<summary><b>4. TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33295) • [📄 arXiv](https://arxiv.org/abs/2609.33295) • [📥 PDF](https://arxiv.org/pdf/2609.33295)

**💻 Code:** [⭐ Code](https://github.com/ZhishanQ/TraceDance) • [⭐ Code](https://github.com/huggingface)

> An agent can complete a task while exhibiting undesirable behavior during execution. Developers need tests for the specific behaviors encountered in deployment, beyond fixed benchmark suites. We present TraceDance, an agent system that constructs ...

</details>

<details>
<summary><b>5. How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35457) • [📄 arXiv](https://arxiv.org/abs/2609.35457) • [📥 PDF](https://arxiv.org/pdf/2609.35457)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most modern multimodal large language models (MLLMs) build on a pretrained visual encoder that provides a strong visual prior. Encoder-free MLLMs instead learn visual representations directly from raw pixels, offering a simple and unified architec...

</details>

<details>
<summary><b>6. Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence</b> ⭐ 17</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35432) • [📄 arXiv](https://arxiv.org/abs/2609.35432) • [📥 PDF](https://arxiv.org/pdf/2609.35432)

**💻 Code:** [⭐ Code](https://github.com/HexaFuture/PhysicalCoding) • [⭐ Code](https://github.com/huggingface)

> Physical Coding represents task state and execution as code. Code as World records objects, relations, constraints, and progress; Code as Policy organizes actions, verification, and recovery. HexaAnything implements this interface through a Harnes...

</details>

<details>
<summary><b>7. MassAlloc Attention: Let Attention Allocate Its Own Compute</b> ⭐ 761</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32712) • [📄 arXiv](https://arxiv.org/abs/2609.32712) • [📥 PDF](https://arxiv.org/pdf/2609.32712)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKUSTDial/flash-sparse-attention)

> Sharing two recent explorations in attention design from our team. We started with two straightforward questions: Does every attention head need to repeatedly attend to the entire causal history? Once attention scores have been computed, do region...

</details>

<details>
<summary><b>8. Improving Test-Time Scaling with Adaptive Looped Transformers</b> ⭐ 85</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35748) • [📄 arXiv](https://arxiv.org/abs/2609.35748) • [📥 PDF](https://arxiv.org/pdf/2609.35748)

**💻 Code:** [⭐ Code](https://github.com/thu-nics/TaH) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>9. Duplex-MPE: Benchmarking Multi-Party Interaction in Full-Duplex Dialogue</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31948) • [📄 arXiv](https://arxiv.org/abs/2609.31948) • [📥 PDF](https://arxiv.org/pdf/2609.31948)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> When several people are talking, a voice assistant needs to know not only what to say, but whether it should speak at all. We introduce Duplex-MPE, a benchmark for selective participation in continuous multi-party conversations. It contains 2,000 ...

</details>

<details>
<summary><b>10. Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35767) • [📄 arXiv](https://arxiv.org/abs/2609.35767) • [📥 PDF](https://arxiv.org/pdf/2609.35767)

**💻 Code:** [⭐ Code](https://github.com/waltstephen/UMM-Reflection) • [⭐ Code](https://github.com/huggingface)

> Unified multimodal models can both look at and render images, so in principle they can repair their own generations: diagnose what an image gets wrong, revise it, observe the result, and diagnose again. Whether a revision helps is known only after...

</details>

<details>
<summary><b>11. EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.28236) • [📄 arXiv](https://arxiv.org/abs/2609.28236) • [📥 PDF](https://arxiv.org/pdf/2609.28236)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share EmbodiedMemory-Bench! 🚀 We study embodied memory for long-horizon interactive tasks, where agents must not only remember past observations, but also continuously update world states, learn from interaction outcomes, and reuse expe...

</details>

<details>
<summary><b>12. CompoWorld: Compositional Environment Scaling for General Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33665) • [📄 arXiv](https://arxiv.org/abs/2609.33665) • [📥 PDF](https://arxiv.org/pdf/2609.33665)

**💻 Code:** [⭐ Code](https://github.com/AllSpark-Research/CompoWorld) • [⭐ Code](https://github.com/huggingface)

> Automatically generated environments provide a scalable source of interaction data for training general agents. However, existing approaches mainly generate tasks within a single environment, while real-world workflows require agents to connect in...

</details>

<details>
<summary><b>13. Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34327) • [📄 arXiv](https://arxiv.org/abs/2609.34327) • [📥 PDF](https://arxiv.org/pdf/2609.34327)

**💻 Code:** [⭐ Code](https://github.com/tally0818/FlyBy) • [⭐ Code](https://github.com/huggingface)

> We study why small reasoning models fail despite extended reasoning, distinguishing execution bottlenecks, where the correct continuation remains internally reachable, from knowledge bottlenecks, where missing parametric knowledge hinders further ...

</details>

<details>
<summary><b>14. Recursive Harness Distillation across Agents for Robot Manipulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33378) • [📄 arXiv](https://arxiv.org/abs/2609.33378) • [📥 PDF](https://arxiv.org/pdf/2609.33378)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> paper: https://arxiv.org/abs/2609.33378

</details>

<details>
<summary><b>15. Surprising Success, Repeated Failure: Entropy-Guided Credit Assignment for Exploration in LLM Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33781) • [📄 arXiv](https://arxiv.org/abs/2609.33781) • [📥 PDF](https://arxiv.org/pdf/2609.33781)

**💻 Code:** [⭐ Code](https://github.com/wgcyeo/EAPO) • [⭐ Code](https://github.com/huggingface)

> We introduce EAPO (Entropic Advantage Policy Optimization), an entropy-guided credit-assignment method for exploration in LLM reasoning. It redistributes each response's advantage across tokens, assigning stronger penalties to low-entropy tokens i...

</details>

<details>
<summary><b>16. WorldPlay2: Extending Real-Time Interactive World Models in Control and Horizon</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Jun Zhang, Junta Wu, Tengfei Wang, Wenqiang Sun, Haiyu Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35560) • [📄 arXiv](https://arxiv.org/abs/2609.35560) • [📥 PDF](https://arxiv.org/pdf/2609.35560)

**💻 Code:** [⭐ Code](https://github.com/WorldPlay2/WorldPlay2) • [⭐ Code](https://github.com/huggingface)

> WorldPlay2 generalizes across scenes and characters, achieving long-horizon consistency alongside flexible control.

</details>

<details>
<summary><b>17. DepthBench: Measuring How Residual Connections Enable More Computational Depth</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32534) • [📄 arXiv](https://arxiv.org/abs/2609.32534) • [📥 PDF](https://arxiv.org/pdf/2609.32534)

**💻 Code:** [⭐ Code](https://github.com/keyu-wang-2002/DepthBench) • [⭐ Code](https://github.com/huggingface)

> Depth is a natural way to increase the computational capacity in Transformers, yet the contribution of deeper layers can diminish as depth grows larger. Recent approaches enhance normalization (e.g., LayerNorm Scaling) or residual connections (e.g...

</details>

<details>
<summary><b>18. Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32577) • [📄 arXiv](https://arxiv.org/abs/2609.32577) • [📥 PDF](https://arxiv.org/pdf/2609.32577)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> At Xiaomi, we developed GAGAR, a new approach for code agent reinforcement learning (RL) that introduces a groupwise agentic grader to perform online advantage redistribution. Instead of only optimizing for test passing, GAGAR enables code agents ...

</details>

<details>
<summary><b>19. Learning to Learn from Context: Synthetic Training from Perturbed Public Documents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33642) • [📄 arXiv](https://arxiv.org/abs/2609.33642) • [📥 PDF](https://arxiv.org/pdf/2609.33642)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Real-world tasks often require large language models (LLMs) to learn from complex task-specific context rather than pretrained parametric knowledge. This capability remains a weakness of LLMs, while human annotation for such task contexts is expen...

</details>

<details>
<summary><b>20. Skill2Env: Capability-Oriented Environment Synthesis from Skills for General Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33772) • [📄 arXiv](https://arxiv.org/abs/2609.33772) • [📥 PDF](https://arxiv.org/pdf/2609.33772)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Executable environments are critical for post-training agents on tasks that require tool use and multi-step interaction, but constructing executable tasks together with their environments remains difficult to scale. Skills provide reusable domain ...

</details>

<details>
<summary><b>21. Diffusion Reward Models</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33803) • [📄 arXiv](https://arxiv.org/abs/2609.33803) • [📥 PDF](https://arxiv.org/pdf/2609.33803)

**💻 Code:** [⭐ Code](https://github.com/thunlp/DRM) • [⭐ Code](https://github.com/huggingface)

> We study the multimodal structure of human preference and recast reward modeling as conditional density estimation over p(r | x, y), and propose Diffusion Reward Model that represents this distribution without committing to any parametric family. ...

</details>

<details>
<summary><b>22. QwenGyre: An Elastic Reinforcement Learning Framework for Training xLong-Horizon Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33848) • [📄 arXiv](https://arxiv.org/abs/2609.33848) • [📥 PDF](https://arxiv.org/pdf/2609.33848)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large language model (LLM) agents increasingly undertake extreme-long (xlong) horizon tasks, where a single execution can span hours, hundreds of model--environment interactions, and nearly 1M tokens per rollout. Applying online reinforcement lear...

</details>

<details>
<summary><b>23. SpatialSpeak: QA-Native Reconstruction with Local and Global Context for Spatial Chain-of-Thought Reasoning</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33616) • [📄 arXiv](https://arxiv.org/abs/2609.33616) • [📥 PDF](https://arxiv.org/pdf/2609.33616)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yangcaoai/SpatialSpeak-VLM)

> We introduce SpatialSpeak , a vision-language framework for multi-view spatial reasoning. It first learns local geometry and global scene context through QA-native reconstruction, then combines spatial chain-of-thought reasoning with visual compen...

</details>

<details>
<summary><b>24. RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Diyuan Hou, Shizhe Zhang, Shuhao Liao, EthanTaylor, KentRidgeChickenrice

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32862) • [📄 arXiv](https://arxiv.org/abs/2609.32862) • [📥 PDF](https://arxiv.org/pdf/2609.32862)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Arxiv: https://arxiv.org/abs/2609.32862 Website: https://jingsongliang.com/robofoundry/

</details>

<details>
<summary><b>25. REALM: A Coarse-to-Fine Generative Framework for Embodied Reactive Listening</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33095) • [📄 arXiv](https://arxiv.org/abs/2609.33095) • [📥 PDF](https://arxiv.org/pdf/2609.33095)

**💻 Code:** [⭐ Code](https://github.com/lipzh5/REALM) • [⭐ Code](https://github.com/huggingface)

> REALM: A Coarse-to-Fine Generative Framework for Embodied Reactive Listening Ever wonder how to make humanoid robots look like they are actually listening to you? 🤖👂 Standard talking-head models struggle with listener motions, resulting in frozen ...

</details>

<details>
<summary><b>26. AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization for RAG and Deep Research</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32472) • [📄 arXiv](https://arxiv.org/abs/2609.32472) • [📥 PDF](https://arxiv.org/pdf/2609.32472)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AdaTutoRank/AdaTutoRank)

> Document rerankers determine what evidence reaches the downstream model in RAG and deep research, yet mainstream rerankers select by relevance matching, and individually relevant documents rarely constitute the complete, complementary, non-redunda...

</details>

<details>
<summary><b>27. WideSWE: Can Coding Agents Coordinate Changes Across Repositories?</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Chen Zhi, Xingliang Wang, Baoyi Wang, wukeming11, Jinyang23

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33382) • [📄 arXiv](https://arxiv.org/abs/2609.33382) • [📥 PDF](https://arxiv.org/pdf/2609.33382)

**💻 Code:** [⭐ Code](https://github.com/ZJU-ACES-ISE/WideSWE) • [⭐ Code](https://github.com/huggingface)

> Coding-agent evaluation has progressed from resolving individual issues to carrying out long-horizon development, yet task completion is still largely assessed within a single codebase. In software ecosystems, many features and bug fixes require c...

</details>

<details>
<summary><b>28. In-Flight KV Cache with Clean Anchors for Faster Autoregressive Video Diffusion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32540) • [📄 arXiv](https://arxiv.org/abs/2609.32540) • [📥 PDF](https://arxiv.org/pdf/2609.32540)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A faster autoregressive diffusion generation pipeline that delivers higher-quality videos with consistent temporal coherence, tested on videos up to 65 seconds long.

</details>

<details>
<summary><b>29. Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34972) • [📄 arXiv](https://arxiv.org/abs/2609.34972) • [📥 PDF](https://arxiv.org/pdf/2609.34972)

**💻 Code:** [⭐ Code](https://github.com/declare-lab/delta-Vision) • [⭐ Code](https://github.com/huggingface)

> Do we really fully use the a attention mechanism?

</details>

<details>
<summary><b>30. CoWindow Attention: Full Causal Coverage Is a Collective Property</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32704) • [📄 arXiv](https://arxiv.org/abs/2609.32712) • [📥 PDF](https://arxiv.org/pdf/2609.32704)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Sharing two recent explorations in attention design from our team. We started with two straightforward questions: Does every attention head need to repeatedly attend to the entire causal history? Once attention scores have been computed, do region...

</details>

<details>
<summary><b>31. Structured Residual Connectivity Matters for Diffusion Transformers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33203) • [📄 arXiv](https://arxiv.org/abs/2609.33203) • [📥 PDF](https://arxiv.org/pdf/2609.33203)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Diffusion Transformers accumulate all preceding layers into a uniform residual stream. This homogenizes representations across depth and fixes how gradients flow. We turn this passive summation into active retrieval. Encoder-side representations a...

</details>

<details>
<summary><b>32. FlowTool: Controlling Tool Parameter in Image Retouching via Flow Matching</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35673) • [📄 arXiv](https://arxiv.org/abs/2609.35673) • [📥 PDF](https://arxiv.org/pdf/2609.35673)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> VLA model for Image Editing

</details>

<details>
<summary><b>33. SolveEdit: Benchmarking Visual Problem Solving in Generative Models</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Zehan Wang, Xuerui Qiu, Yexin Liu, Wenjie Shu, Harold328

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35504) • [📄 arXiv](https://arxiv.org/abs/2609.35504) • [📥 PDF](https://arxiv.org/pdf/2609.35504)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/WenjieShu/SolveEdit)

> Repo: https://github.com/WenjieShu/SolveEdit

</details>

<details>
<summary><b>34. Precise Editing and Flexible Referencing for Interactable Worlds</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34470) • [📄 arXiv](https://arxiv.org/abs/2609.34470) • [📥 PDF](https://arxiv.org/pdf/2609.34470)

**💻 Code:** [⭐ Code](https://github.com/leoisufa/EditWorld) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>35. Program-Verified Self-Evolution for Vision-Language Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33855) • [📄 arXiv](https://arxiv.org/abs/2609.33855) • [📥 PDF](https://arxiv.org/pdf/2609.33855)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ahmedheakl/VQS)

> Self-evolving vision-language models learn from questions they make from unlabeled images, but the labels they use are often wrong, with human checks showing 24% of majority-vote labels and 18% of model-judge labels are incorrect. VQS fixes this b...

</details>

<details>
<summary><b>36. Imprint Reader: From Weight-Update Readout to Behavioral Intervention</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jing Shao, Qihao Lin, Guanxu Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35261) • [📄 arXiv](https://arxiv.org/abs/2609.35261) • [📥 PDF](https://arxiv.org/pdf/2609.35261)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/biuboomc/SMaRT-Vibe-Alignment)

> A wish becomes a weight update without task-specific training data: vibe alignment. We train Imprint Reader to read updates and say what the model learned. Free-form readout still has a way to go, but 'prefix' scoring turns it into a vibe aligner....

</details>

<details>
<summary><b>37. SciGen-Verifier: A Multimodal Reasoner for Explainable Verification in Scientific Image Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xi Yu, Shirong Lin, Zuqi Wang, Zhengteng Lin, Jiali Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33399) • [📄 arXiv](https://arxiv.org/abs/2609.33399) • [📥 PDF](https://arxiv.org/pdf/2609.33399)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper introduces SciGen-Verify, the first benchmark for explainable verification of scientific image generation, covering instruction following, multidisciplinary reasoning, and world knowledge with a three-tier protocol over binary judgement...

</details>

<details>
<summary><b>38. Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Porter Jenkins, Yuxiao Yang, Shangzhe Li, Tianrun Yu, kzhao5

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32444) • [📄 arXiv](https://arxiv.org/abs/2609.32444) • [📥 PDF](https://arxiv.org/pdf/2609.32444)

**💻 Code:** [⭐ Code](https://github.com/kzhao5/CIS-RL) • [⭐ Code](https://github.com/huggingface)

> 👋 Hi everyone! We introduce Calibrated Importance Sampling (CIS) to address training–inference mismatch in LLM reinforcement learning. 🔍 Why it matters: Even with identical model weights, inference and training engines can assign different token p...

</details>

<details>
<summary><b>39. InfiniHand: Streaming World-Space Hand Motion Estimation from Egocentric Video</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35743) • [📄 arXiv](https://arxiv.org/abs/2609.35743) • [📥 PDF](https://arxiv.org/pdf/2609.35743)

**💻 Code:** [⭐ Code](https://github.com/infinihand/InfiniHand) • [⭐ Code](https://github.com/huggingface)

> World-space hand motion estimation from egocentric video requires recovering 3D articulated hand geometry while tracking camera egomotion. Existing approaches heavily rely on cascading independent hand pose estimators and SLAM systems, resulting i...

</details>

<details>
<summary><b>40. TT-VidT: Decoupling the Temporal Axis for Efficient Motion-Centric Video Pretraining</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33419) • [📄 arXiv](https://arxiv.org/abs/2609.33419) • [📥 PDF](https://arxiv.org/pdf/2609.33419)

**💻 Code:** [⭐ Code](https://github.com/KohakuBlueleaf/TTVidT) • [⭐ Code](https://github.com/huggingface)

> We introduce TT-VidT, a video pretraining framework that treats spatial and temporal separately instead of stacking per-frame embeddings or running one global 3D model: it outputs a per-frame "motion token," and a decoder rebuilds each frame from ...

</details>

<details>
<summary><b>41. Residual Transferability in Neural Image Watermarking</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xinchao Wang, Qi Li, Ziping Dong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32241) • [📄 arXiv](https://arxiv.org/abs/2609.32241) • [📥 PDF](https://arxiv.org/pdf/2609.32241)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>42. BaRe-Mem: Bayesian Reliability Memory for Robust and Adaptive Agent Consultation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35551) • [📄 arXiv](https://arxiv.org/abs/2609.35551) • [📥 PDF](https://arxiv.org/pdf/2609.35551)

**💻 Code:** [⭐ Code](https://github.com/declare-lab/BaRe-Mem) • [⭐ Code](https://github.com/huggingface)

> BaRe-Mem is an online Bayesian reliability memory that learns context-dependent advisor reliability from verified interactions, modulates external advice accordingly, and adaptively decides whether to consult or reason autonomously.

</details>

<details>
<summary><b>43. Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32353) • [📄 arXiv](https://arxiv.org/abs/2609.32353) • [📥 PDF](https://arxiv.org/pdf/2609.32353)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yrxxxxxxxx1007/LT-OPD)

> This paper discusses the scenario of extreme visual token reduction and leverages on-policy self-distillation to solve it.

</details>

<details>
<summary><b>44. Nereus: Adaptive Parallelism for LLM Post-Training</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mario Di Francesco, Zeke Wang, Sitong Zhang, Tuo Shi, Songlin Jiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34645) • [📄 arXiv](https://arxiv.org/abs/2609.34645) • [📥 PDF](https://arxiv.org/pdf/2609.34645)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Nereus adapts the parallel execution plan of an RL post-training job while the job runs. Resource availability, sequence length, memory pressure, and stage bottlenecks change during a run, so a plan that was good at the start can become slow or ev...

</details>

<details>
<summary><b>45. An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35505) • [📄 arXiv](https://arxiv.org/abs/2609.35505) • [📥 PDF](https://arxiv.org/pdf/2609.35505)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/UNCSciML/LSPD)

> LSPD: An RL View of On-Policy Distillation On-policy distillation (OPD) is commonly implemented with policy-gradient updates. But its reverse-KL objective also has an exact interpretation as KL-regularized reinforcement learning , with a reward de...

</details>

<details>
<summary><b>46. GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35734) • [📄 arXiv](https://arxiv.org/abs/2609.35734) • [📥 PDF](https://arxiv.org/pdf/2609.35734)

**💻 Code:** [⭐ Code](https://github.com/geoverse-nvs/GeoVerse) • [⭐ Code](https://github.com/huggingface)

> Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observe...

</details>

<details>
<summary><b>47. RenderRank: Learning to Rerank Text with Compressed Visual Tokens</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35069) • [📄 arXiv](https://arxiv.org/abs/2609.35069) • [📥 PDF](https://arxiv.org/pdf/2609.35069)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>48. Rethinking Automated Voice Similarity by Shifting from EER to Embedding Geometry</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33999) • [📄 arXiv](https://arxiv.org/abs/2609.33999) • [📥 PDF](https://arxiv.org/pdf/2609.33999)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Speaker verification (SV) models are commonly assumed to better capture nuances among speaker characteristics as verification accuracy improves, leading to their widespread use as automated proxies for human voice similarity in speech generation t...

</details>

<details>
<summary><b>49. Change the Product, Keep the Parameters: Associative Algebra Layers for Transformers</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ivan Oseledets, Ilya Koziev

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32814) • [📄 arXiv](https://arxiv.org/abs/2609.32814) • [📥 PDF](https://arxiv.org/pdf/2609.32814)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We study whether the matrix multiplication used in Transformer projections can be replaced by a different, cheaper associative product while keeping the same weight bank and parameter count. We construct an associative algebra product with a lower...

</details>

<details>
<summary><b>50. Measuring Collapse and Correction in Homogeneous-Panel LLM Debate</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35279) • [📄 arXiv](https://arxiv.org/abs/2609.35279) • [📥 PDF](https://arxiv.org/pdf/2609.35279)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LiXin97/DebateLedger)

> Accepted at NeurIPS 2026 (Evaluations and Datasets Track). Project page: https://lixin.ai/DebateLedger/

</details>

<details>
<summary><b>51. WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23033) • [📄 arXiv](https://arxiv.org/abs/2609.23033) • [📥 PDF](https://arxiv.org/pdf/2609.23033)

**💻 Code:** [⭐ Code](https://github.com/summerbro-hhj/wavefront-decoding) • [⭐ Code](https://github.com/huggingface)

> We introduce WaveFront Decoding for Looped Language Models . Check it out!

</details>

<details>
<summary><b>52. Beyond Timestamps: Decision-Aligned On-Policy Distillation for Long-Horizon Agents</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33391) • [📄 arXiv](https://arxiv.org/abs/2609.33391) • [📥 PDF](https://arxiv.org/pdf/2609.33391)

**💻 Code:** [⭐ Code](https://github.com/mingju-c/Align-OPSD) • [⭐ Code](https://github.com/huggingface)

> We introduce AlignOPSD, a framework for improving on-policy distillation in long-horizon agents. The key insight is that temporal alignment does not necessarily imply decision alignment. Existing approaches typically assign supervision based on ti...

</details>

<details>
<summary><b>53. Relic: From Multi-Agent Collaboration to Persistent Organizational Capability</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32965) • [📄 arXiv](https://arxiv.org/abs/2609.32965) • [📥 PDF](https://arxiv.org/pdf/2609.32965)

**💻 Code:** [⭐ Code](https://github.com/Hongyi-Du/Relic) • [⭐ Code](https://github.com/huggingface)

> Can AI organizations learn how to operate? RELIC turns recurring collaboration failures into governed, executable organizational protocols that persist across tasks and member turnover. Across 360 controlled runs, RELIC improves complete-contract ...

</details>

<details>
<summary><b>54. When Do Model Internals Help? Exploring the Role of Representation Engineering in LLM Safety</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Liangming Pan, Jianhui Chen, Gtynnn

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34771) • [📄 arXiv](https://arxiv.org/abs/2609.34771) • [📥 PDF](https://arxiv.org/pdf/2609.34771)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Reliable AI safeguards require both control mechanisms that reduce unsafe behavior and monitoring mechanisms that detect safety risks during model interactions. Established behavioral safeguards include alignment methods that optimize model output...

</details>

<details>
<summary><b>55. DroneWAM: Efficient World Action Model for Drone Visual Navigation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wei Xu, Hongbo Lu, Fan Liu, Liang Yao, YijunShen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33148) • [📄 arXiv](https://arxiv.org/abs/2609.33148) • [📥 PDF](https://arxiv.org/pdf/2609.33148)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/1e12Leon/DroneWAM)

> We present DroneWAM, an efficient world-action model for drone visual navigation. DroneWAM adopts JEPA-based predictive learning to model future states directly in representation space, focusing computation on predictive scene structure and motion...

</details>

<details>
<summary><b>56. Draft-KV: Learning Useful Latent Communication Between Language Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34754) • [📄 arXiv](https://arxiv.org/abs/2609.34754) • [📥 PDF](https://arxiv.org/pdf/2609.34754)

**💻 Code:** [⭐ Code](https://github.com/Svardfox/Draft-KV) • [⭐ Code](https://github.com/huggingface)

> Can language models communicate useful private information through latent representations? We introduce Draft-KV, a simple framework that lets a receiver directly reuse the KV cache produced by a sharer while drafting. Unlike prior latent communic...

</details>

<details>
<summary><b>57. TokenCast: Forecasting Token Consumption During LLM Agent Execution</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35760) • [📄 arXiv](https://arxiv.org/abs/2609.35760) • [📥 PDF](https://arxiv.org/pdf/2609.35760)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DEFENSE-SEU/TokenCast)

> TokenCast forecasts token consumption during LLM agent execution. The same task can consume over an order of magnitude more tokens across runs, because the agent's next steps depend on tool feedback and the growing context inflates the input size ...

</details>

<details>
<summary><b>58. KVCMAS: Efficient KV cache Correction for Shared Context in Multi-Agent Systems</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34060) • [📄 arXiv](https://arxiv.org/abs/2609.34060) • [📥 PDF](https://arxiv.org/pdf/2609.34060)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hjeon2k/KVCMAS)

> No abstract available.

</details>

<details>
<summary><b>59. PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation and Neutral Reconstruction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34054) • [📄 arXiv](https://arxiv.org/abs/2609.34054) • [📥 PDF](https://arxiv.org/pdf/2609.34054)

**💻 Code:** [⭐ Code](https://github.com/hjeon2k/PReCache) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>60. ColNanoVDR: Document-Free Query Distillation for Multi-Vector Visual Document Retrieval via Optimal Transport</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34899) • [📄 arXiv](https://arxiv.org/abs/2609.34899) • [📥 PDF](https://arxiv.org/pdf/2609.34899)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ryenhails/NanoVDR)

> ColNanoVDR brings NanoVDR-style document-free distillation to multi-vector visual document retrieval. We distill multi-billion-parameter multi-vector VLM retrievers (4.5B–8.8B) into a 149M text-only query encoder that scores directly against the t...

</details>

<details>
<summary><b>61. Adaptive Consistency Graph for Long-Horizon Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32754) • [📄 arXiv](https://arxiv.org/abs/2609.32754) • [📥 PDF](https://arxiv.org/pdf/2609.32754)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yunsaijc/Adaptive-Consistency-Graph)

> How can AI agents go further on long tasks—and stay connected to their original goals? As tasks grow longer, agents need to connect the original requirements, accumulated evidence, and current execution state. Even a locally reasonable decision ca...

</details>

<details>
<summary><b>62. G^2PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Wenzheng Cai, Qian Zhang, Yuxuan Sun, Haoli Bai, Ruikang Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31009) • [📄 arXiv](https://arxiv.org/abs/2609.31009) • [📥 PDF](https://arxiv.org/pdf/2609.31009)

**💻 Code:** [⭐ Code](https://github.com/G2PTQ/G2PTQ) • [⭐ Code](https://github.com/huggingface)

> G$^2$PTQ is a unified PTQ framework with Generalized Gradient Compensation that integrates both first- and second-order information under a globally supervised, block-wise optimization objective. By refreshing gradient and Hessian estimates before...

</details>

<details>
<summary><b>63. SMAT: Simple and Efficient Merge-Aware Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33437) • [📄 arXiv](https://arxiv.org/abs/2609.33437) • [📥 PDF](https://arxiv.org/pdf/2609.33437)

**💻 Code:** [⭐ Code](https://github.com/egangu/smat) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>64. KernelZero: Co-Evolving Proposer and Coder for Continuously Improved GPU Kernel Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuanbo Wen, Zhenghong Li, Zixiang Fang, Rui Zhang, kcxain

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33074) • [📄 arXiv](https://arxiv.org/abs/2609.33074) • [📥 PDF](https://arxiv.org/pdf/2609.33074)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Interesting

</details>

<details>
<summary><b>65. On-Policy Self-Distillation for Multi-Turn Image Editing</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35611) • [📄 arXiv](https://arxiv.org/abs/2609.35611) • [📥 PDF](https://arxiv.org/pdf/2609.35611)

**💻 Code:** [⭐ Code](https://github.com/liangbingzhao/MT-OPSD) • [⭐ Code](https://github.com/huggingface)

> Instruction-based image editing has achieved strong performance in single-turn settings, yet practical editing is often iterative, with each instruction applied to the output of the previous turn. We find that existing editing models degrade rapid...

</details>

<details>
<summary><b>66. Why Deterministic PRM Guidance Underperforms in Discrete Diffusion Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35472) • [📄 arXiv](https://arxiv.org/abs/2609.35472) • [📥 PDF](https://arxiv.org/pdf/2609.35472)

**💻 Code:** [⭐ Code](https://github.com/dLLM-PRM-Gap/dLLM-PRM-Gap) • [⭐ Code](https://github.com/huggingface)

> Accepted at NeurIPS 2026. We study deterministic process-reward-model (PRM) guidance for discrete diffusion reasoning under a matched forward-pass budget. On Dream-v0-Instruct-7B, deterministic PRM guidance underperforms independent sampling with ...

</details>

<details>
<summary><b>67. SkillDRE: Dual-Stage Red-Team Evolution of Agent Skills via Pre-Execution and Runtime Feedback</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sen Su, Li Sun, Yi Liu, Jingyi Yang, Pengyu Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32400) • [📄 arXiv](https://arxiv.org/abs/2609.32400) • [📥 PDF](https://arxiv.org/pdf/2609.32400)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> come look

</details>

<details>
<summary><b>68. EvolvingAvatar: Interactive 3D Head Generation That Adapts as Conversations Unfold</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35616) • [📄 arXiv](https://arxiv.org/abs/2609.35616) • [📥 PDF](https://arxiv.org/pdf/2609.35616)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 EvolvingAvatar enables interactive 3D head generation that learns during conversation. Through test-time training, it continuously adapts to user face video and dyadic audio, combining persistent conversational adaptation with transient audiovis...

</details>

<details>
<summary><b>69. VGGT-Diff: Visual Geometry Meets Diffusion for Sparse-View Novel View Synthesis</b> ⭐ 31</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33253) • [📄 arXiv](https://arxiv.org/abs/2609.33253) • [📥 PDF](https://arxiv.org/pdf/2609.33253)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/chenkangjie1123/VGGT-Diff)

> VGGT-Diff is a geometry-routed multi-view diffusion model for sparse-view novel view synthesis from six input images. Its first key innovation, the confidence-aware Visual Geometry Router (VGR), transforms VGGT-Ω features into query-aligned geomet...

</details>

<details>
<summary><b>70. ControlScope: Workflow Revision and Reliability in LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34313) • [📄 arXiv](https://arxiv.org/abs/2609.34313) • [📥 PDF](https://arxiv.org/pdf/2609.34313)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Workflow Revision and Reliability in LLM Agents

</details>

<details>
<summary><b>71. Playing to Par: Reinforcement Learning for Provably Optimal Quadrilateral Block Decompositions</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Per-Olof Persson, arjunnarayanan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32146) • [📄 arXiv](https://arxiv.org/abs/2609.32146) • [📥 PDF](https://arxiv.org/pdf/2609.32146)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ArjunNarayanan/par-quad)

> This is a reinforcement learning method that learns to create topologically optimal quadrilateral meshes starting purely from the boundary and using very general edit operations.

</details>

<details>
<summary><b>72. What masking geometry works best for EEG foundation models?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33487) • [📄 arXiv](https://arxiv.org/abs/2609.33487) • [📥 PDF](https://arxiv.org/pdf/2609.33487)

**💻 Code:** [⭐ Code](https://github.com/PierreGtch/eeg-fm-masking) • [⭐ Code](https://github.com/huggingface)

> What masking geometry works best for EEG foundation models? In this paper, we present a controlled evaluation across the MAE and JEPA frameworks.

</details>

<details>
<summary><b>73. Safe Error Correction for Language Models: Frozen-Base Adjustment with Capability Preservation</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.16145) • [📄 arXiv](https://arxiv.org/abs/2609.16145) • [📥 PDF](https://arxiv.org/pdf/2609.16145)

**💻 Code:** [⭐ Code](https://github.com/eulogik/prajna) • [⭐ Code](https://github.com/huggingface)

> Author here, happy to answer questions! This paper asks a deliberately narrow question: if you freeze a language model completely and only train a small correction module on top, how far can you get and what do you keep? The headline tradeoff, on ...

</details>

<details>
<summary><b>74. NanoForecast v0.5: Competitive Time Series Forecasting Through Training Pipeline Optimization</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31669) • [📄 arXiv](https://arxiv.org/abs/2609.31669) • [📥 PDF](https://arxiv.org/pdf/2609.31669)

**💻 Code:** [⭐ Code](https://github.com/eulogik/NanoForecast) • [⭐ Code](https://github.com/huggingface)

> NanoForecast v0.5: 6.5M-parameter forecaster that beats TimesFM (200M) on 4/6 benchmarks after fixing three training pipeline bugs (loss scope, tensor shapes, augmentation) with zero architecture changes. 43.8% MASE improvement (3.030 → 1.704) on ...

</details>

<details>
<summary><b>75. Not All Objectives Are Born Equal: Priority-Constrained Descent for Hierarchical Multi-Objective Optimization</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Mohamed I. Alhajri, DaraV

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.29521) • [📄 arXiv](https://arxiv.org/abs/2606.29521) • [📥 PDF](https://arxiv.org/pdf/2606.29521)

**💻 Code:** [⭐ Code](https://github.com/DaraVaram/priority-constrained-descent) • [⭐ Code](https://github.com/huggingface)

> We propose Priority-Constrained Descent (PCD) for training deep learning problems where a hierarchy of objectives exists. One objective serves as our primary (e.g., accuracy) while others, such as regularizers, etc... "shape" the solution. At ever...

</details>

<details>
<summary><b>76. When Privacy Moves ML-Mediated Decisions On Device: Information and Incentive Misalignment in Auctions</b> ⭐ 0</summary>

<br/>

**👥 Authors:** dipankarsarkar

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33312) • [📄 arXiv](https://arxiv.org/abs/2609.33312) • [📥 PDF](https://arxiv.org/pdf/2609.33312)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sarkar-dipankar/on-device-auction-audit)

> Moving ad auctions on device leaves the budget on a server, so devices bid against stale balances. In simulation (50 devices, 36 campaigns, 30 seeds per cell), a 50-tick sync lag drives spend to 17.7 times the frozen budget, while zero lag stays w...

</details>

<details>
<summary><b>77. How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure</b> ⭐ 0</summary>

<br/>

**👥 Authors:** dipankarsarkar

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.30074) • [📄 arXiv](https://arxiv.org/abs/2609.30074) • [📥 PDF](https://arxiv.org/pdf/2609.30074)

**💻 Code:** [⭐ Code](https://github.com/sarkar-dipankar/llm-evaluation-self-audit) • [⭐ Code](https://github.com/huggingface)

> We re-ran the same prompt-structure inference with identical calls, caching off, on 8 open models. Agreement between repeated calls ranged from Jaccard 0.39 to 0.96. Only 35 of 127 prompt-model cells were perfectly reproducible. Bootstrapping the ...

</details>

<details>
<summary><b>78. Training and Inference Dynamics of PLDR-LLMs: Row-Map Collapse, Renormalization, and Predictive Reduction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34130) • [📄 arXiv](https://arxiv.org/abs/2609.34130) • [📥 PDF](https://arxiv.org/pdf/2609.34130)

**💻 Code:** [⭐ Code](https://github.com/burcgokden/PLDR-LLM-Training-Dynamics) • [⭐ Code](https://github.com/huggingface)

> This monograph develops a unified account of training and inference in Power Law Decoder Representation language models (PLDR-LLMs). Exact finite work identities decompose changes in the absolute energy of the row-centered learned map into paramet...

</details>

<details>
<summary><b>79. How Does "English (US)" Become the Default? Triangulating Structural Bias Towards American English Across the LLM Pipeline</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Davood Rafiei, tafseer-nayeem

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04204) • [📄 arXiv](https://arxiv.org/abs/2604.04204) • [📥 PDF](https://arxiv.org/pdf/2604.04204)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tafseer-nayeem/LLM-structural-bias)

> Large language models (LLMs) are increasingly embedded in educational, professional, and public infrastructure, yet widely used platforms expose "English (US)" as a primary English setting despite the global diversity of English. We ask: How does ...

</details>

<details>
<summary><b>80. AdaGuard: An Adaptive Guard Model with User-defined Policies</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mingrui Lao, Zheng Li, Yuxiang Xie, Yifan Ding, Yunhao Feng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34241) • [📄 arXiv](https://arxiv.org/abs/2609.34241) • [📥 PDF](https://arxiv.org/pdf/2609.34241)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yunhao-Feng/AdaGuard)

> A adapative guard model of agents.

</details>

<details>
<summary><b>81. Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32821) • [📄 arXiv](https://arxiv.org/abs/2609.32821) • [📥 PDF](https://arxiv.org/pdf/2609.32821)

**💻 Code:** [⭐ Code](https://github.com/wyy-code/SRR) • [⭐ Code](https://github.com/huggingface)

> This work conducts a comprehensive analysis across s DeepSeekMoE, OLMoE, and Qwen3-MoE, by proposing a routing analysis toolkit for controlled counterfactual interventions and token-level analysis. These findings show that routing drift alone is i...

</details>

<details>
<summary><b>82. PyroAdapt: Adapting Wildfire Prediction under Spatial Heterogeneity and Temporal Shift</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12435) • [📄 arXiv](https://arxiv.org/abs/2605.12435) • [📥 PDF](https://arxiv.org/pdf/2605.12435)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Prediction of wildfire occurrence is a rare-event problem compounded by spatial heterogeneity and temporal distribution shift, as fire occurrences are vastly outnumbered by non-occurrences, and predictor--fire relationship varies across space and ...

</details>

<details>
<summary><b>83. Rolling-WAM: World Action Models with Rolling Imagination</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.30247) • [📄 arXiv](https://arxiv.org/abs/2609.30247) • [📥 PDF](https://arxiv.org/pdf/2609.30247)

**💻 Code:** [⭐ Code](https://github.com/zyinghua/Rolling-WAM) • [⭐ Code](https://github.com/huggingface)

> https://rolling-wam.github.io/

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 83 |
| 📅 Today | [`2026-09-29.json`](data/daily/2026-09-29.json) | 83 |
| 📆 This Week | [`2026-W39.json`](data/weekly/2026-W39.json) | 107 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 709 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-29 | 83 | [View JSON](data/daily/2026-09-29.json) |
| 📄 2026-09-28 | 24 | [View JSON](data/daily/2026-09-28.json) |
| 📄 2026-09-27 | 22 | [View JSON](data/daily/2026-09-27.json) |
| 📄 2026-09-26 | 22 | [View JSON](data/daily/2026-09-26.json) |
| 📄 2026-09-25 | 18 | [View JSON](data/daily/2026-09-25.json) |
| 📄 2026-09-24 | 24 | [View JSON](data/daily/2026-09-24.json) |
| 📄 2026-09-23 | 18 | [View JSON](data/daily/2026-09-23.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W39 | 107 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 709 | [View JSON](data/monthly/2026-09.json) |
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
