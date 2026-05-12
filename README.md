<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-48-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4072+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">48</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">86</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">308</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4072+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** May 12, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Soohak: A Mathematician-Curated Benchmark for Evaluating Research-level Math Capabilities of LLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09063) • [📄 arXiv](https://arxiv.org/abs/2605.09063) • [📥 PDF](https://arxiv.org/pdf/2605.09063)

> For questions or model-evaluation requests, contact guijin.son@snu.ac.kr .

</details>

<details>
<summary><b>2. Qwen-Image-2.0 Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10730) • [📄 arXiv](https://arxiv.org/abs/2605.10730) • [📥 PDF](https://arxiv.org/pdf/2605.10730)

> Qwen-Image-2.0 Technical Report

</details>

<details>
<summary><b>3. CollabVR: Collaborative Video Reasoning with Vision-Language and Video Generation Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08735) • [📄 arXiv](https://arxiv.org/abs/2605.08735) • [📥 PDF](https://arxiv.org/pdf/2605.08735)

**💻 Code:** [⭐ Code](https://github.com/Joow0n-Kim/CollabVR)

> No abstract available.

</details>

<details>
<summary><b>4. PaperFit: Vision-in-the-Loop Typesetting Optimization for Scientific Documents</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10341) • [📄 arXiv](https://arxiv.org/abs/2605.10341) • [📥 PDF](https://arxiv.org/pdf/2605.10341)

**💻 Code:** [⭐ Code](https://github.com/OpenRaiser/PaperFit)

> A LaTeX manuscript that compiles without error is not necessarily publication-ready. The resulting PDFs frequently suffer from misplaced floats, overflowing equations, inconsistent table scaling, widow and orphan lines, and poor page balance, forc...

</details>

<details>
<summary><b>5. Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09608) • [📄 arXiv](https://arxiv.org/abs/2605.09608) • [📥 PDF](https://arxiv.org/pdf/2605.09608)

**💻 Code:** [⭐ Code](https://github.com/wyy-code/GCWM)

> How should we continually post-train LLMs without causing catastrophic forgetting? We find that forgetting is not simply caused by large parameter updates. Instead, it is better understood as a state-relative update-integration failure: harmful st...

</details>

<details>
<summary><b>6. Model Merging Scaling Laws in Large Language Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2509.24244) • [📄 arXiv](https://arxiv.org/abs/2509.24244) • [📥 PDF](https://arxiv.org/pdf/2509.24244)

**💻 Code:** [⭐ Code](https://github.com/InfiXAI/Merging-Scaling-Law)

> Can we predict the returns of language model merging before trying every expert combination? We study scaling laws for LLM merging and find a compact floor-plus-tail law that predicts merged-model cross-entropy from base model size and the number ...

</details>

<details>
<summary><b>7. TMAS: Scaling Test-Time Compute via Multi-Agent Synergy</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10344) • [📄 arXiv](https://arxiv.org/abs/2605.10344) • [📥 PDF](https://arxiv.org/pdf/2605.10344)

**💻 Code:** [⭐ Code](https://github.com/george-QF/TMAS-code)

> TL;DR: TMAS improves test-time scaling by turning independent reasoning rollouts into a coordinated multi-agent process, where agents verify, summarize, reuse reliable experience, avoid redundant strategies, and are further aligned through hybrid-...

</details>

<details>
<summary><b>8. WorldReasonBench: Human-Aligned Stress Testing of Video Generators as Future World-State Predictors</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10434) • [📄 arXiv](https://arxiv.org/abs/2605.10434) • [📥 PDF](https://arxiv.org/pdf/2605.10434)

**💻 Code:** [⭐ Code](https://github.com/UniX-AI-Lab/WorldReasonBench)

> Commercial video generation systems such as Seedance2.0 and Veo3.1 have rapidly improved, strengthening the view that video generators may be evolving into "world simulators." Yet the community still lacks a benchmark that directly tests whether a...

</details>

<details>
<summary><b>9. Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08354) • [📄 arXiv](https://arxiv.org/abs/2605.08354) • [📥 PDF](https://arxiv.org/pdf/2605.08354)

**💻 Code:** [⭐ Code](https://github.com/OpenEnvision/AutoRubric-as-Reward)

> Auto-Rubric as Reward converts a small set of labeled visual supervision into readable rubric text, supports both pointwise and pairwise VLM grading, and lets practitioners freely scale up the rubric dimensions they care about. On top of that, we ...

</details>

<details>
<summary><b>10. X-OmniClaw Technical Report: A Unified Mobile Agent for Multimodal Understanding and Interaction</b> ⭐ 69</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.05765) • [📄 arXiv](https://arxiv.org/abs/2605.05765) • [📥 PDF](https://arxiv.org/pdf/2605.05765)

**💻 Code:** [⭐ Code](https://github.com/OPPO-Mente-Lab/X-OmniClaw)

> Hi HF community! If you are interested in our work or have any questions, feel free to reach out or leave a comment. I'd love to hear your thoughts!

</details>

<details>
<summary><b>11. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10923) • [📄 arXiv](https://arxiv.org/abs/2605.10923) • [📥 PDF](https://arxiv.org/pdf/2605.10923)

**💻 Code:** [⭐ Code](https://github.com/ejhshen/SLIM)

> We are delighted to present SLIM, a framework of dynamic skill lifecycle management for agentic reinforcement learning. Experiments show that SLIM outperforms the best baselines by an average of 7.1% points across ALFWorld and SearchQA. Results fu...

</details>

<details>
<summary><b>12. Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10781) • [📄 arXiv](https://arxiv.org/abs/2605.10781) • [📥 PDF](https://arxiv.org/pdf/2605.10781)

> Enough with the obedient student. Time to rebel 🧑‍🎓⚡ So far, on-policy self-distillation has pulled the student toward the teacher. But what if we force the student to follow the teacher even on paths it already got right? → Its own reasoning gets...

</details>

<details>
<summary><b>13. G-Zero: Self-Play for Open-Ended Generation from Zero Data</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Langlin Huang, Tong Zheng, Haolin Liu, Chengsong Huang, Leo-Dai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09959) • [📄 arXiv](https://arxiv.org/abs/2605.09959) • [📥 PDF](https://arxiv.org/pdf/2605.09959)

**💻 Code:** [⭐ Code](https://github.com/Chengsong-Huang/G-Zero)

> Self-evolving LLMs excel in verifiable domains but struggle in open-ended tasks, where reliance on proxy LLM judges introduces capability bottlenecks and reward hacking. To overcome this, we introduce G-Zero, a verifier-free, co-evolutionary frame...

</details>

<details>
<summary><b>14. Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Arash Behboodi, Jordi Ros-Giralt, Niccolò Grillo, Arnau Padres Masdemont, Victor Conchello Vendrell

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.07721) • [📄 arXiv](https://arxiv.org/abs/2605.07721) • [📥 PDF](https://arxiv.org/pdf/2605.07721)

> Recurrent LLM architectures have emerged as a promising approach for improving reasoning, as they enable multi-step computation in the embedding space without generating intermediate tokens. Models such as Ouro perform reasoning by iteratively upd...

</details>

<details>
<summary><b>15. Pixal3D: Pixel-Aligned 3D Generation from Images</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10922) • [📄 arXiv](https://arxiv.org/abs/2605.10922) • [📥 PDF](https://arxiv.org/pdf/2605.10922)

**💻 Code:** [⭐ Code](https://github.com/TencentARC/Pixal3D)

> Project page: https://ldyang694.github.io/projects/pixal3d/ Demo: https://huggingface.co/spaces/TencentARC/Pixal3D Code: https://github.com/TencentARC/Pixal3D

</details>

<details>
<summary><b>16. Make Each Token Count: Towards Improving Long-Context Performance with KV Cache Eviction</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09649) • [📄 arXiv](https://arxiv.org/abs/2605.09649) • [📥 PDF](https://arxiv.org/pdf/2605.09649)

**💻 Code:** [⭐ Code](https://github.com/ngocbh/trimkv)

> Can we improve long-context performance with KV cache eviction?

</details>

<details>
<summary><b>17. Mela: Test-Time Memory Consolidation based on Transformation Hypothesis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10537) • [📄 arXiv](https://arxiv.org/abs/2605.10537) • [📥 PDF](https://arxiv.org/pdf/2605.10537)

**💻 Code:** [⭐ Code](https://github.com/Musubi-ai/Mela)

> Memory consolidation, the process by which transient experiences are transformed into stable, structured representations, is a foundational organizing principle in the human brain, yet it remains largely unexplored as a design principle for modern...

</details>

<details>
<summary><b>18. SlimQwen: Exploring the Pruning and Distillation in Large MoE Model Pre-training</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Rui Men, Liangyu Wang, Bo Zheng, Zekun Wang, Shengkun Tang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08738) • [📄 arXiv](https://arxiv.org/abs/2605.08738) • [📥 PDF](https://arxiv.org/pdf/2605.08738)

> SlimQwen: Exploring the Pruning and Distillation in Large MoE Model Pre-training

</details>

<details>
<summary><b>19. RigidFormer: Learning Rigid Dynamics using Transformers</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09196) • [📄 arXiv](https://arxiv.org/abs/2605.09196) • [📥 PDF](https://arxiv.org/pdf/2605.09196)

**💻 Code:** [⭐ Code](https://github.com/Frank-ZY-Dou/Dynamics-Modeling)

> RigidFormer: Learning Rigid Dynamics with Transformers - our attempt to scale learning-based physical dynamics with Transformers. RigidFormer learns rigid dynamics with Transformers. It is a mesh-free, object-centric Transformer for multi-object r...

</details>

<details>
<summary><b>20. Reinforcing Multimodal Reasoning Against Visual Degradation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09262) • [📄 arXiv](https://arxiv.org/abs/2605.09262) • [📥 PDF](https://arxiv.org/pdf/2605.09262)

> Reinforcement Learning has significantly advanced the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet the resulting policies remain brittle against real-world visual degradations such as blur, compression artifacts, and low...

</details>

<details>
<summary><b>21. DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09269) • [📄 arXiv](https://arxiv.org/abs/2605.09269) • [📥 PDF](https://arxiv.org/pdf/2605.09269)

> Aligning Multimodal Large Language Models (MLLMs) requires reliable reward models, yet existing single-step evaluators can suffer from lazy judging, exploiting language priors over fine-grained visual verification. While rubric-based evaluation mi...

</details>

<details>
<summary><b>22. NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation</b> ⭐ 910</summary>

<br/>

**👥 Authors:** Dongxu Zhang, Zirui Wang, Yujun Wu, Qiyuan Zhu, Jinhang Xu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10813) • [📄 arXiv](https://arxiv.org/abs/2605.10813) • [📥 PDF](https://arxiv.org/pdf/2605.10813)

**💻 Code:** [⭐ Code](https://github.com/OpenRaiser/NanoResearch)

> No abstract available.

</details>

<details>
<summary><b>23. Omni-Persona: Systematic Benchmarking and Improving Omnimodal Personalization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09996) • [📄 arXiv](https://arxiv.org/abs/2605.09996) • [📥 PDF](https://arxiv.org/pdf/2605.09996)

**💻 Code:** [⭐ Code](https://github.com/oyt9306/Omni-Persona)

> We introduce Omni-Persona, the first comprehensive benchmark for omnimodal personalization spanning text, image, and audio. Built on the Persona Modality Graph (PMG), it formalizes personalization as cross-modal routing and jointly evaluates groun...

</details>

<details>
<summary><b>24. Shaping Schema via Language Representation as the Next Frontier for LLM Intelligence Expanding</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Masashi Sugiyama, Pei Fu anf Bo Han, Jingwen Fu, Yuhan Liu, Zhiqin Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09271) • [📄 arXiv](https://arxiv.org/abs/2605.09271) • [📥 PDF](https://arxiv.org/pdf/2605.09271)

> No abstract available.

</details>

<details>
<summary><b>25. LLaVA-UHD v4: What Makes Efficient Visual Encoding in MLLMs?</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Tianyu Yu, Wenshuo Ma, Chongyi Wang, Yihua Qin, PhoenixGS

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08985) • [📄 arXiv](https://arxiv.org/abs/2605.08985) • [📥 PDF](https://arxiv.org/pdf/2605.08985)

**💻 Code:** [⭐ Code](https://github.com/THUMAI-Lab/LLaVA-UHD-v4)

> We show that slice-based encoding outperforms global encoding across benchmarks, suggesting that preserving local details through sliced views can be more beneficial than applying global attention for fine-grained perception. Moreover, we introduc...

</details>

<details>
<summary><b>26. SEIF: Self-Evolving Reinforcement Learning for Instruction Following</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.07465) • [📄 arXiv](https://arxiv.org/abs/2605.07465) • [📥 PDF](https://arxiv.org/pdf/2605.07465)

**💻 Code:** [⭐ Code](https://github.com/Rainier-rq1/SEIF)

> This paper proposes SEIF , a self-evolving reinforcement learning framework for improving LLM instruction following. The main idea is to create a closed training loop where an Instructor generates increasingly challenging instructions, a Filter re...

</details>

<details>
<summary><b>27. AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08715) • [📄 arXiv](https://arxiv.org/abs/2605.08715) • [📥 PDF](https://arxiv.org/pdf/2605.08715)

**💻 Code:** [⭐ Code](https://github.com/ZBox1005/AgentForesight)

> Overview AgentForesight reframes multi-agent failure analysis from post-hoc diagnosis of completed trajectories to online auditing of unfolding ones. At each step of an unfolding trajectory, an auditor observes only the current prefix and must eit...

</details>

<details>
<summary><b>28. FlashEvolve: Accelerating Agent Self-Evolution with Asynchronous Stage Orchestration</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08520) • [📄 arXiv](https://arxiv.org/abs/2605.08520) • [📥 PDF](https://arxiv.org/pdf/2605.08520)

> FlashEvolve makes LLM agent evolution (GEPA, ACE, Meta-Harness) 3.5–4.9× faster by replacing synchronous stage execution with asynchronous workers and queues. Its key insight is that unlike opaque weight-space staleness in async RL, language-space...

</details>

<details>
<summary><b>29. SlimSpec: Low-Rank Draft LM-Head for Accelerated Speculative Decoding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10453) • [📄 arXiv](https://arxiv.org/abs/2605.10453) • [📥 PDF](https://arxiv.org/pdf/2605.10453)

> For questions contact astrlrd@nebius.com

</details>

<details>
<summary><b>30. DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10933) • [📄 arXiv](https://arxiv.org/abs/2605.10933) • [📥 PDF](https://arxiv.org/pdf/2605.10933)

> While Mixture-of-Experts (MoE) scales model capacity without proportionally increasing computation, its massive total parameter footprint creates significant storage and memory-access bottlenecks, which hinder efficient end-side deployment that si...

</details>

<details>
<summary><b>31. Injecting Distributional Awareness into MLLMs via Reinforcement Learning for Deep Imbalanced Regression</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaomeng Li, Shanshan Song, ChanganYao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.01402) • [📄 arXiv](https://arxiv.org/abs/2605.01402) • [📥 PDF](https://arxiv.org/pdf/2605.01402)

> Identifies the limitations of supervised fine-tuning for numerical regression, and introduces GRPO with batch-aware supervision for deep imbalanced regression together with a newly constructed DIR benchmark.

</details>

<details>
<summary><b>32. Metal-Sci: A Scientific Compute Benchmark for Evolutionary LLM Kernel Search on Apple Silicon</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Víctor Gallego

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09708) • [📄 arXiv](https://arxiv.org/abs/2605.09708) • [📥 PDF](https://arxiv.org/pdf/2605.09708)

**💻 Code:** [⭐ Code](https://github.com/vicgalle/metal-sci-kernels)

> @ librarian-bot recommend

</details>

<details>
<summary><b>33. Scratchpad Patching: Decoupling Compute from Patch Size in Byte-Level Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Laura Rimell, Dan Garrette, Timothy Dozat, Vasilisa Bashlovkina, Lin Zheng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09630) • [📄 arXiv](https://arxiv.org/abs/2605.09630) • [📥 PDF](https://arxiv.org/pdf/2605.09630)

> This work introduces Scratchpad Patching for byte-level language models, which inserts transient, entropy-triggered scratchpads inside patches and significantly improves modeling quality at much larger patch sizes.

</details>

<details>
<summary><b>34. FORTIS: Benchmarking Over-Privilege in Agent Skills</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Ryan Rossi, Wei Yang, Han Wang, Chenxiao Yu, Shawn Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09163) • [📄 arXiv](https://arxiv.org/abs/2605.09163) • [📥 PDF](https://arxiv.org/pdf/2605.09163)

**💻 Code:** [⭐ Code](https://github.com/lili0415/FORTIS-Benchmark)

> No abstract available.

</details>

<details>
<summary><b>35. MuSS: A Large-Scale Dataset and Cinematic Narrative Benchmark for Multi-Shot Subject-to-Video Generation</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Yuancheng Wei, Linjie Zhong, Bingyan Liu, Di Wu, Haojie Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.23789) • [📄 arXiv](https://arxiv.org/abs/2604.23789) • [📥 PDF](https://arxiv.org/pdf/2604.23789)

**💻 Code:** [⭐ Code](https://github.com/zhang-haojie/MuSS)

> TL;DR: Current video generation models often struggle with continuous narrative logic or degenerate into trivial "2D sticker" copy-paste generators. This paper introduces MuSS, a large-scale dataset and benchmark designed specifically for multi-sh...

</details>

<details>
<summary><b>36. LLiMba: Sardinian on a Single GPU -- Adapting a 3B Language Model to a Vanishing Romance Language</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Luca Ballore

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09015) • [📄 arXiv](https://arxiv.org/abs/2605.09015) • [📥 PDF](https://arxiv.org/pdf/2605.09015)

**💻 Code:** [⭐ Code](https://github.com/lballore/LLiMba)

> Sardinian, a Romance language with roughly one million speakers, has minimal presence in modern NLP. Commercial services do not support it, and current language models do not produce it reliably. We present LLiMba, a 3B parameter Sardinian-ready m...

</details>

<details>
<summary><b>37. Pushing Biomolecular Utility-Diversity Frontiers with Supergroup Relative Policy Optimization</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08659) • [📄 arXiv](https://arxiv.org/abs/2605.08659) • [📥 PDF](https://arxiv.org/pdf/2605.08659)

**💻 Code:** [⭐ Code](https://github.com/IDEA-XL/SGRPO)

> No abstract available.

</details>

<details>
<summary><b>38. SplatWeaver: Learning to Allocate Gaussian Primitives for Generalizable Novel View Synthesis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.07287) • [📄 arXiv](https://arxiv.org/abs/2605.07287) • [📥 PDF](https://arxiv.org/pdf/2605.07287)

**💻 Code:** [⭐ Code](https://github.com/yecongwan/SplatWeaver)

> SplatWeaver is a feed-forward framework that adaptively allocates Gaussian primitives based on local scene complexity. By concentrating primitives in intricate regions while maintaining sparsity in smooth areas, our approach enables a more princip...

</details>

<details>
<summary><b>39. Uncovering Entity Identity Confusion in Multimodal Knowledge Editing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.06096) • [📄 arXiv](https://arxiv.org/abs/2605.06096) • [📥 PDF](https://arxiv.org/pdf/2605.06096)

> Multimodal knowledge editing (MKE) aims to correct the internal knowledge of large vision-language models after deployment, yet the behavioral patterns of post-edit models remain underexplored. In this paper, we identify a systemic failure mode in...

</details>

<details>
<summary><b>40. CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10903) • [📄 arXiv](https://arxiv.org/abs/2605.10903) • [📥 PDF](https://arxiv.org/pdf/2605.10903)

**💻 Code:** [⭐ Code](https://github.com/OpenHelix-Team/CapVector)

> We provide a general capability extraction strategy to improve the pretrained VLAs' capability with minimum cost.

</details>

<details>
<summary><b>41. RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jiayi Chen, Jieyuan Pei, Huarui Zhang, Wenxuan Song, Huashuo Lei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10921) • [📄 arXiv](https://arxiv.org/abs/2605.10921) • [📥 PDF](https://arxiv.org/pdf/2605.10921)

**💻 Code:** [⭐ Code](https://github.com/OpenHelix-Team/RoboMemArena)

> We propose a comprehensive and challenging robotic memory benchmark RoboMemArena. The data, code, and weight are all open-sourced. Besides, we provide a leaderboard.

</details>

<details>
<summary><b>42. The Alpha Blending Hypothesis: Compositing Shortcut in Deepfake Detection</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiri Matas, Mario Fritz, Jan Cech, Andrii Yermakov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10334) • [📄 arXiv](https://arxiv.org/abs/2605.10334) • [📥 PDF](https://arxiv.org/pdf/2605.10334)

> The code will be released later this year. Though, it is similar to https://huggingface.co/collections/yermandy/gend The test dataset is here: https://huggingface.co/datasets/yermandy/GenD

</details>

<details>
<summary><b>43. Shepherd: A Runtime Substrate Empowering Meta-Agents with a Formalized Execution Trace</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiuding Sun, Dilara Soylu, Ananjan Nandi, Derek Chong, Simon Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10913) • [📄 arXiv](https://arxiv.org/abs/2605.10913) • [📥 PDF](https://arxiv.org/pdf/2605.10913)

> No abstract available.

</details>

<details>
<summary><b>44. Dystruct: Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhenyi Wang, Mubarak Shah, Bian Sun, k-zhai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09820) • [📄 arXiv](https://arxiv.org/abs/2605.09820) • [📥 PDF](https://arxiv.org/pdf/2605.09820)

> DyStruct is a training-free Bayesian decoding framework that enables flexible-length generation in discrete Diffusion Language Models (DLMs). While discrete diffusion models offer the architectural advantage of parallel decoding, they are typicall...

</details>

<details>
<summary><b>45. SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Lingjun Mao, Siddhant Hitesh Mantri, Yuhan Liu, Xiaokang Ye, Haoqiang Kang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09423) • [📄 arXiv](https://arxiv.org/abs/2605.09423) • [📥 PDF](https://arxiv.org/pdf/2605.09423)

> No abstract available.

</details>

<details>
<summary><b>46. Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09241) • [📄 arXiv](https://arxiv.org/abs/2605.09241) • [📥 PDF](https://arxiv.org/pdf/2605.09241)

**💻 Code:** [⭐ Code](https://github.com/intcomp/Sub-JEPA)

> We're releasing Sub-JEPA 🌐 LeWM (from LeCun's group) is the first end-to-end trainable JEPA world model — it uses isotropic Gaussian regularization to prevent representation collapse. Clean and effective. Our take: latent representations sit on lo...

</details>

<details>
<summary><b>47. TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09810) • [📄 arXiv](https://arxiv.org/abs/2605.09810) • [📥 PDF](https://arxiv.org/pdf/2605.09810)

> No abstract available.

</details>

<details>
<summary><b>48. 100,000+ Movie Reviews from Kazakhstan: Russian, Kazakh, and Code-Switched Texts</b> ⭐ 0</summary>

<br/>

**👥 Authors:** yeshpanovrustem

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08600) • [📄 arXiv](https://arxiv.org/abs/2605.08600) • [📥 PDF](https://arxiv.org/pdf/2605.08600)

> Accepted to NLP4DH 2026

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 48 |
| 📅 Today | [`2026-05-12.json`](data/daily/2026-05-12.json) | 48 |
| 📆 This Week | [`2026-W19.json`](data/weekly/2026-W19.json) | 86 |
| 🗓️ This Month | [`2026-05.json`](data/monthly/2026-05.json) | 308 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-05-12 | 48 | [View JSON](data/daily/2026-05-12.json) |
| 📄 2026-05-11 | 38 | [View JSON](data/daily/2026-05-11.json) |
| 📄 2026-05-10 | 38 | [View JSON](data/daily/2026-05-10.json) |
| 📄 2026-05-09 | 38 | [View JSON](data/daily/2026-05-09.json) |
| 📄 2026-05-08 | 25 | [View JSON](data/daily/2026-05-08.json) |
| 📄 2026-05-07 | 15 | [View JSON](data/daily/2026-05-07.json) |
| 📄 2026-05-06 | 17 | [View JSON](data/daily/2026-05-06.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W19 | 86 | [View JSON](data/weekly/2026-W19.json) |
| 📅 2026-W18 | 158 | [View JSON](data/weekly/2026-W18.json) |
| 📅 2026-W17 | 120 | [View JSON](data/weekly/2026-W17.json) |
| 📅 2026-W16 | 156 | [View JSON](data/weekly/2026-W16.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-05 | 308 | [View JSON](data/monthly/2026-05.json) |
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
