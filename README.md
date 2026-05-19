<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-32-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4352+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">32</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">56</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">588</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4352+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** May 19, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation</b> ⭐ 1.22k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18739) • [📄 arXiv](https://arxiv.org/abs/2605.18739) • [📥 PDF](https://arxiv.org/pdf/2605.18739)

**💻 Code:** [⭐ Code](https://github.com/NVlabs/LongLive) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>2. Lance: Unified Multimodal Modeling by Multi-Task Synergy</b> ⭐ 134</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18678) • [📄 arXiv](https://arxiv.org/abs/2605.18678) • [📥 PDF](https://arxiv.org/pdf/2605.18678)

**💻 Code:** [⭐ Code](https://github.com/bytedance/Lance) • [⭐ Code](https://github.com/huggingface)

> Lance is a native unified multimodal model that supports image and video understanding, generation, and editing within a single framework (Especially  video understanding, generation and editing). Efficient at 3B scale. With only 3B active paramet...

</details>

<details>
<summary><b>3. AI for Auto-Research: Roadmap & User Guide</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Linfeng Li, Wei Chow, Xian Sun, Lingdong Kong, yingshuow

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18661) • [📄 arXiv](https://arxiv.org/abs/2605.18661) • [📥 PDF](https://arxiv.org/pdf/2605.18661)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/worldbench/awesome-ai-auto-research)

> AI for Auto-Research — the first survey of AI across the complete research lifecycle, covering idea generation, literature review, coding, writing, peer review, rebuttal, and dissemination. Project Page: https://worldbench.github.io/awesome-ai-aut...

</details>

<details>
<summary><b>4. KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.14278) • [📄 arXiv](https://arxiv.org/abs/2605.14278) • [📥 PDF](https://arxiv.org/pdf/2605.14278)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Richard-Zhang-AI/KVPO)

> We propose KVPO, a novel ODE-native Group Relative Policy Optimization (GRPO) framework that aligns streaming autoregressive video generators with human preferences through innovative causal-semantic KV cache exploration and a velocity-field surro...

</details>

<details>
<summary><b>5. SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution</b> ⭐ 201</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18401) • [📄 arXiv](https://arxiv.org/abs/2605.18401) • [📥 PDF](https://arxiv.org/pdf/2605.18401)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MemTensor/skills-vote)

> We introduce SkillsVote, a lifecycle governance framework for Agent Skills. Instead of treating long-horizon agent trajectories as disposable traces, SkillsVote converts them into reusable, executable skills with procedural guidance, while control...

</details>

<details>
<summary><b>6. Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code Synthesis</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18451) • [📄 arXiv](https://arxiv.org/abs/2605.18451) • [📥 PDF](https://arxiv.org/pdf/2605.18451)

**💻 Code:** [⭐ Code](https://github.com/YxuanAr/Code-as-Room) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>7. OProver: A Unified Framework for Agentic Formal Theorem Proving</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17283) • [📄 arXiv](https://arxiv.org/abs/2605.17283) • [📥 PDF](https://arxiv.org/pdf/2605.17283)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/multimodal-art-projection/OProver)

> Recent progress in formal theorem proving has benefited from large-scale proof generation and verifier-aware training, but agentic proving is rarely integrated into prover training, appearing only at inference time. We present OProver, a unified f...

</details>

<details>
<summary><b>8. Post-Trained MoE Can Skip Half Experts via Self-Distillation</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18643) • [📄 arXiv](https://arxiv.org/abs/2605.18643) • [📥 PDF](https://arxiv.org/pdf/2605.18643)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TsinghuaC3I/ZEDA)

> Github: https://github.com/TsinghuaC3I/ZEDA

</details>

<details>
<summary><b>9. LiteFrame: Efficient Vision Encoders Unlock Frame Scaling in Video LLMs</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17260) • [📄 arXiv](https://arxiv.org/abs/2605.17260) • [📥 PDF](https://arxiv.org/pdf/2605.17260)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jjihwan/LiteFrame)

> No abstract available.

</details>

<details>
<summary><b>10. Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17672) • [📄 arXiv](https://arxiv.org/abs/2605.17672) • [📥 PDF](https://arxiv.org/pdf/2605.17672)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/giovanni-vaccarino/PUMA)

> Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models Large Reasoning Models (LRMs) achieve strong performance by generating long chains of thought (CoT), but often overthink, continuing to reason after a solution has ...

</details>

<details>
<summary><b>11. Where Should Diffusion Enter a Language Model? Geometry-Guided Hidden-State Replacement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.14368) • [📄 arXiv](https://arxiv.org/abs/2605.14368) • [📥 PDF](https://arxiv.org/pdf/2605.14368)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper reframes continuous diffusion for language generation as a problem of finding the right internal transformer representation space, and proposes a geometry-guided Locate-and-Replace hybrid architecture to do so.

</details>

<details>
<summary><b>12. Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.14038) • [📄 arXiv](https://arxiv.org/abs/2605.14038) • [📥 PDF](https://arxiv.org/pdf/2605.14038)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/chengez/Tool-Cognition-Action)

> Excited to share our new work on the knowing–doing gap in LLM tool use. Most prior work in LLM adaptive tool use treats “tool necessity” as fixed and model-agnostic. But models have different capabilities. What GPT-5 can solve without a tool may r...

</details>

<details>
<summary><b>13. StableVLA: Towards Robust Vision-Language-Action Models without Extra Data</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18287) • [📄 arXiv](https://arxiv.org/abs/2605.18287) • [📥 PDF](https://arxiv.org/pdf/2605.18287)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.16839) • [📄 arXiv](https://arxiv.org/abs/2605.16839) • [📥 PDF](https://arxiv.org/pdf/2605.16839)

**💻 Code:** [⭐ Code](https://github.com/jiwonsong-dev/CompactAttention) • [⭐ Code](https://github.com/huggingface)

> A new paper for chunked prefill acceleration

</details>

<details>
<summary><b>15. From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17242) • [📄 arXiv](https://arxiv.org/abs/2605.17242) • [📥 PDF](https://arxiv.org/pdf/2605.17242)

**💻 Code:** [⭐ Code](https://github.com/yxwan123/TDDev) • [⭐ Code](https://github.com/huggingface)

> "Just deploy it and see if it works" — turns out that's exactly what coding agents can't do. TDDev gives them eyes (browser simulation), a rubric (acceptance tests written before code), and a feedback channel (structured repair reports), lifting w...

</details>

<details>
<summary><b>16. Measuring Maximum Activations in Open Large Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.15572) • [📄 arXiv](https://arxiv.org/abs/2605.15572) • [📥 PDF](https://arxiv.org/pdf/2605.15572)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/clx1415926/Max_act_llm)

> The dynamic range of activations is a first-order constraint for low-bit quantization, activation scaling, and stable LLM inference. Prior work characterized outlier features and massive activations on pre-2024 LLaMA-style models, and the downstre...

</details>

<details>
<summary><b>17. Targeted Neuron Modulation via Contrastive Pair Search</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12290) • [📄 arXiv](https://arxiv.org/abs/2605.12290) • [📥 PDF](https://arxiv.org/pdf/2605.12290)

**💻 Code:** [⭐ Code](https://github.com/neuron-steering) • [⭐ Code](https://github.com/NousResearch/neural-steering) • [⭐ Code](https://github.com/huggingface)

> Language models are instruction-tuned to refuse harmful requests, but the mechanisms underlying this behavior remain poorly understood. Popular steering methods operate on the residual stream and degrade output coherence at high intervention stren...

</details>

<details>
<summary><b>18. EndPrompt: Efficient Long-Context Extension via Terminal Anchoring</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.14589) • [📄 arXiv](https://arxiv.org/abs/2605.14589) • [📥 PDF](https://arxiv.org/pdf/2605.14589)

**💻 Code:** [⭐ Code](https://github.com/clx1415926/EndPrompt) • [⭐ Code](https://github.com/huggingface)

> Extending the context window of large language models typically requires training on sequences at the target length, incurring quadratic memory and computational costs that make long-context adaptation expensive and difficult to reproduce. We prop...

</details>

<details>
<summary><b>19. AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hang Wang, Jingchu Yang, Xiujin Liu, Yihao Hu, Pan Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17933) • [📄 arXiv](https://arxiv.org/abs/2605.17933) • [📥 PDF](https://arxiv.org/pdf/2605.17933)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. FINESSE-Bench: A Hierarchical Benchmark Suite for Financial Domain Knowledge and Technical Analysis in Large Language Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Denis Kokosinskii, Dmitry Zmitrovich, Alexey Khoroshilov, Nini Kamkia, KOHbDS

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.15482) • [📄 arXiv](https://arxiv.org/abs/2605.15482) • [📥 PDF](https://arxiv.org/pdf/2605.15482)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LimexAILab/FINESSE-Bench)

> We present FINESSE-Bench, a 3,993-question hierarchical benchmark suite for evaluating whether LLMs can solve professionally oriented financial tasks beyond standard public financial QA. The suite spans eight specialized datasets covering exam-sty...

</details>

<details>
<summary><b>21. Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17698) • [📄 arXiv](https://arxiv.org/abs/2605.17698) • [📥 PDF](https://arxiv.org/pdf/2605.17698)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The deployment of Large Language Models (LLMs) as autonomous economic agents introduces systemic risks that extend beyond individual capability failures. As agents transition to directly interacting with marketplaces, their collective behavior can...

</details>

<details>
<summary><b>22. Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Xiangrui Ke, Zhilei Shu, Zhao Pu, Qianyu Peng, Shangwen Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18601) • [📄 arXiv](https://arxiv.org/abs/2605.18601) • [📥 PDF](https://arxiv.org/pdf/2605.18601)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhushangwen/Incantation)

> No abstract available.

</details>

<details>
<summary><b>23. Actionable World Representation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Isabella Liu, Tianshu Tang, Jianglong Ye, Jitao Li, Kunqi Xu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18743) • [📄 arXiv](https://arxiv.org/abs/2605.18743) • [📥 PDF](https://arxiv.org/pdf/2605.18743)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>24. Code as Agent Harness</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Zihao Li, Tianxin Wei, Dongqi Fu, Katherine Tieu, Xuying Ning

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18747) • [📄 arXiv](https://arxiv.org/abs/2605.18747) • [📥 PDF](https://arxiv.org/pdf/2605.18747)

**💻 Code:** [⭐ Code](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>25. SNLP: Layer-Parallel Inference via Structured Newton Corrections</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17842) • [📄 arXiv](https://arxiv.org/abs/2605.17842) • [📥 PDF](https://arxiv.org/pdf/2605.17842)

**💻 Code:** [⭐ Code](https://github.com/phymhan/nanochat-snlp) • [⭐ Code](https://github.com/huggingface)

> We introduce Structured Newton Layer Parallelism (SNLP), a framework for accelerating Transformer inference by parallelizing computation across layers. Instead of running layers sequentially, SNLP treats the hidden-state trace across depth as a no...

</details>

<details>
<summary><b>26. SafeDiffusion-R1: Online Reward Steering for Safe Diffusion Post-Training</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18719) • [📄 arXiv](https://arxiv.org/abs/2605.18719) • [📥 PDF](https://arxiv.org/pdf/2605.18719)

**💻 Code:** [⭐ Code](https://github.com/MAXNORM8650/SafeDiffusion-R1) • [⭐ Code](https://github.com/huggingface)

> Reinforcement learning can post-train diffusion models to improve both safety and reasoning. SafeDiffusion-R1 applies online GRPO with geometry-aware reward steering in CLIP space, enabling safer diffusion generation without paired safe/unsafe ima...

</details>

<details>
<summary><b>27. A2RBench: An Automatic Paradigm for Formally Verifiable Abstract Reasoning Benchmark Generation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17278) • [📄 arXiv](https://arxiv.org/abs/2605.17278) • [📥 PDF](https://arxiv.org/pdf/2605.17278)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MAC-AutoML/A2Rbench)

> Abstract reasoning ability reflects the intelligence and generalization capacity of LLMs to extract and apply abstract rules. However, accurately measuring this ability remains challenging: existing benchmarks either rely on expensive manual annot...

</details>

<details>
<summary><b>28. Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity</b> ⭐ 1</summary>

<br/>

**👥 Authors:** pcr2120

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.17199) • [📄 arXiv](https://arxiv.org/abs/2605.17199) • [📥 PDF](https://arxiv.org/pdf/2605.17199)

**💻 Code:** [⭐ Code](https://github.com/prashantcraju/hippocampal-stability) • [⭐ Code](https://github.com/huggingface)

> The paper resolves a fundamental paradox in biological memory: how do organisms store vastly more information without proportionally more neurons? Comparing food-caching black-capped chickadees to non-caching zebra finches, shows that extreme spat...

</details>

<details>
<summary><b>29. Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sebastian Cygert, Tomasz Trzciński, Marcin Sendera, Aleksander Szymczyk, mchraba

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.18549) • [📄 arXiv](https://arxiv.org/abs/2605.18549) • [📥 PDF](https://arxiv.org/pdf/2605.18549)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> To analyze the behavior of Large Reasoning Models, we propose tracking probe trajectories based on their internal dynamics.

</details>

<details>
<summary><b>30. MixSD: Mixed Contextual Self-Distillation for Knowledge Injection</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.16865) • [📄 arXiv](https://arxiv.org/abs/2605.16865) • [📥 PDF](https://arxiv.org/pdf/2605.16865)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> MIXSD constructs distribution-aligned supervision by mixing two conditionals of the base model itself: an expert rollout that sees the injected fact and a naive rollout that reflects the original prior, choosing between them per-token via a Bernou...

</details>

<details>
<summary><b>31. AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents</b> ⭐ 16</summary>

<br/>

**👥 Authors:** Sharon Zhou, Mehdi Rezagholizadeh, Sina Rafati, Wenwen Ouyang, Sharareh Younesian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.16819) • [📄 arXiv](https://arxiv.org/abs/2605.16819) • [📥 PDF](https://arxiv.org/pdf/2605.16819)

**💻 Code:** [⭐ Code](https://github.com/AMD-AGI/AgentKernelArena) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>32. GRASP: Learning to Ground Social Reasoning in Multi-Person Non-Verbal Interactions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.15764) • [📄 arXiv](https://arxiv.org/abs/2605.15764) • [📥 PDF](https://arxiv.org/pdf/2605.15764)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Current MLLMs can describe scenes, but still struggle to understand who is interacting with whom. We introduce GRASP, a large-scale benchmark for grounded social reasoning built from gaze, gesture, and interaction events in multi-person videos. GR...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 32 |
| 📅 Today | [`2026-05-19.json`](data/daily/2026-05-19.json) | 32 |
| 📆 This Week | [`2026-W20.json`](data/weekly/2026-W20.json) | 56 |
| 🗓️ This Month | [`2026-05.json`](data/monthly/2026-05.json) | 588 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-05-19 | 32 | [View JSON](data/daily/2026-05-19.json) |
| 📄 2026-05-18 | 24 | [View JSON](data/daily/2026-05-18.json) |
| 📄 2026-05-17 | 53 | [View JSON](data/daily/2026-05-17.json) |
| 📄 2026-05-16 | 53 | [View JSON](data/daily/2026-05-16.json) |
| 📄 2026-05-15 | 42 | [View JSON](data/daily/2026-05-15.json) |
| 📄 2026-05-14 | 34 | [View JSON](data/daily/2026-05-14.json) |
| 📄 2026-05-13 | 42 | [View JSON](data/daily/2026-05-13.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W20 | 56 | [View JSON](data/weekly/2026-W20.json) |
| 📅 2026-W19 | 310 | [View JSON](data/weekly/2026-W19.json) |
| 📅 2026-W18 | 158 | [View JSON](data/weekly/2026-W18.json) |
| 📅 2026-W17 | 120 | [View JSON](data/weekly/2026-W17.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-05 | 588 | [View JSON](data/monthly/2026-05.json) |
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
