<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-29-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9754+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">29</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">83</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">353</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9754+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 11, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. World In-Context Learning for Agentic Robot Manipulation</b> ⭐ 36</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12885) • [📄 arXiv](https://arxiv.org/abs/2611.12885) • [📥 PDF](https://arxiv.org/pdf/2611.12885)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ArcheOne-AI/RoboScript)

> Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recor...

</details>

<details>
<summary><b>2. Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14320) • [📄 arXiv](https://arxiv.org/abs/2611.14320) • [📥 PDF](https://arxiv.org/pdf/2611.14320)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yukyeongleee/wikitrace)

> Don’t just trust your memory. A bad lesson can make an agent fail a task it could solve without memory. We introduce WikiTrace to reduce this memory-induced degradation. WikiTrace links each lesson to its original run and a diagnosis of the outcom...

</details>

<details>
<summary><b>3. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ammar Ali, Hadi Salloum

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14210) • [📄 arXiv](https://arxiv.org/abs/2611.14210) • [📥 PDF](https://arxiv.org/pdf/2611.14210)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TheQuantumGOAT/Tree-Ising)

> MIT's GPT-6 Astra agent repaired Qwen3.5-0.8B's reasoning loops by rewriting its weights over 158 turns and 89.7M tokens. Tree-Ising beats that edit with no LLM at all: 54.6% vs 51.7% on MATH-500, ahead on all five math benchmarks, using 4 forward...

</details>

<details>
<summary><b>4. Few-Step Streaming Video Generation via Condition Shifting</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14033) • [📄 arXiv](https://arxiv.org/abs/2611.14033) • [📥 PDF](https://arxiv.org/pdf/2611.14033)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/shengshu-ai/Vidu-S)

> Hi everyone! We’re sharing our latest work extending APEX from image generation to few-step streaming video generation . Condition Shifting lets the generator and fake estimator share one network, removing the separate fake-score network and reduc...

</details>

<details>
<summary><b>5. dNaViT: Discrete Codes are General-Purpose Visual Representations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12426) • [📄 arXiv](https://arxiv.org/abs/2611.12426) • [📥 PDF](https://arxiv.org/pdf/2611.12426)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce dNaViT: Discrete Codes are General-Purpose Visual Representations. dNaViT is a native-resolution visual tokenizer that combines residual modulation, grouped product quantization, and progressive three-stage training to preserve both s...

</details>

<details>
<summary><b>6. MMDM: Measuring Massive Multitask Decision Making</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14309) • [📄 arXiv](https://arxiv.org/abs/2611.14309) • [📥 PDF](https://arxiv.org/pdf/2611.14309)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mmdm-benchmark/mmdm)

> System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cove...

</details>

<details>
<summary><b>7. DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.11166) • [📄 arXiv](https://arxiv.org/abs/2611.11166) • [📥 PDF](https://arxiv.org/pdf/2611.11166)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share DexForesight , our latest work from the Sharpa Foundation Model Team ! Project Page: https://dexforesight.github.io/ Most existing dexterous manipulation models rely primarily on RGB observations. However, even in simple pick-and-...

</details>

<details>
<summary><b>8. DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03142) • [📄 arXiv](https://arxiv.org/abs/2611.03142) • [📥 PDF](https://arxiv.org/pdf/2611.03142)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jianke0604/DepthGraft)

> Scaling depth is a key route to stronger large language models, but Pre-LN architectures often suffer from depth-wise information dilution, limiting the effective use of deep layers. While cross-layer connectivity has proven effective at mitigatin...

</details>

<details>
<summary><b>9. WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12527) • [📄 arXiv](https://arxiv.org/abs/2611.12527) • [📥 PDF](https://arxiv.org/pdf/2611.12527)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sh-lee-prml/WaveGen)

> WaveGen is a truly end-to-end text-to-waveform model that generates speech directly, without external codecs or vocoders. It achieves state-of-the-art performance among TTS models trained on Emilia. We release the source code and checkpoints, incl...

</details>

<details>
<summary><b>10. ProTEUS: A mutation-resolved world model for closed-loop protein evolution</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Wojciech Matusik, Peter Yichen Chen, Guangxue Xu, Minghao Guo, Yikun Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13348) • [📄 arXiv](https://arxiv.org/abs/2611.13348) • [📥 PDF](https://arxiv.org/pdf/2611.13348)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yikunpku/ProTEUS)

> No abstract available.

</details>

<details>
<summary><b>11. PhysOPSD: Code as Privilege for Physically Plausible Video Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12411) • [📄 arXiv](https://arxiv.org/abs/2611.12411) • [📥 PDF](https://arxiv.org/pdf/2611.12411)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aigc3d/PhysOPSD)

> Empowering generation with coding agents: Recent approaches use coding agents to replace parts of the video generation process. We explore how coding agents can empower the generator itself. Executable code supplies structured physical supervision...

</details>

<details>
<summary><b>12. Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14488) • [📄 arXiv](https://arxiv.org/abs/2611.14488) • [📥 PDF](https://arxiv.org/pdf/2611.14488)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bennidict23/memory-clock)

> We asked a robot to repeat a task three times. Two 5-second pauses made it stop after two. On RoboMME, those pauses cut a released memory VLA’s success from 47/50 to 16/50. Hide the same pause frames from memory, and success returns to 45/50. The ...

</details>

<details>
<summary><b>13. EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12934) • [📄 arXiv](https://arxiv.org/abs/2611.12934) • [📥 PDF](https://arxiv.org/pdf/2611.12934)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ranranrannervous/EarthRecord)

> EarthRecord asks whether multimodal agents can turn four decades of raw satellite imagery into reliable land-change analysis. For each question, the agent works in an offline sandbox (Python, shell, image viewer) on the record of one site as distr...

</details>

<details>
<summary><b>14. Market-Conditioned JEPA: Learning from Unpredictable Market Shocks</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13572) • [📄 arXiv](https://arxiv.org/abs/2611.13572) • [📥 PDF](https://arxiv.org/pdf/2611.13572)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenFinMind/MC-JEPA)

> No abstract available.

</details>

<details>
<summary><b>15. ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Zijin Hong, Junlin Xie, Hao Wu, Jiaying Yang, Xu Luo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13482) • [📄 arXiv](https://arxiv.org/abs/2611.13482) • [📥 PDF](https://arxiv.org/pdf/2611.13482)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Frankluox/ExRL)

> [CoRL 2026 R2RL Oral] ExRL enables sample-efficient online improvement of long-chunk robot policies like VLAs and WAMs by RL. It learns how much of each predicted chunk to execute using a lightweight RL policy, improving task performance across si...

</details>

<details>
<summary><b>16. Micius-Flash: Lightweight Agentic Intelligence for Engineering</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10015) • [📄 arXiv](https://arxiv.org/abs/2611.10015) • [📥 PDF](https://arxiv.org/pdf/2611.10015)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present Micius-Flash , an open-source 27B multimodal model designed for semiconductor engineering and scientific applications. Micius combines a knowledge-tree-driven data pipeline, specialized expert models, and Multi-Teacher On-Policy Distill...

</details>

<details>
<summary><b>17. FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.07464) • [📄 arXiv](https://arxiv.org/abs/2611.07464) • [📥 PDF](https://arxiv.org/pdf/2611.07464v1)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 The User Signed Off. The Backtest Was Wrong. Can We Trust AI Agents with Financial Work? 📄 “FinCosmos: An Open-World Evaluation Paradigm for Agents in Finance” AI agents no longer just answer questions. They search the Web, call data APIs, write...

</details>

<details>
<summary><b>18. Are Dense Rewards Worth Their Tokens in GRPO?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13560) • [📄 arXiv](https://arxiv.org/abs/2611.13560) • [📥 PDF](https://arxiv.org/pdf/2611.13560)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> RLVR trains language models to reason by rewarding correct final answers. A widely used algorithm, group- relative policy optimization (GRPO), gives every token of a solution the same credit, so dense process rewards have been proposed to credit i...

</details>

<details>
<summary><b>19. Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable Time Series</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12955) • [📄 arXiv](https://arxiv.org/abs/2611.12955) • [📥 PDF](https://arxiv.org/pdf/2611.12955)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Sachithx/ConceptTime)

> CONCEPTTIME uses predictive surprise from a frozen probabilistic forecaster to jointly identify segment boundaries and learn an interpretable vocabulary of temporal concepts. A lightweight classifier predicts from the concept sequence, while dista...

</details>

<details>
<summary><b>20. Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12184) • [📄 arXiv](https://arxiv.org/abs/2611.12184) • [📥 PDF](https://arxiv.org/pdf/2611.12184)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zou-group/BVSR)

> Blind Variation withholds most of the task description at ideation time, so independent generations stop converging on the same idea. Selective Retention trains a selector on proposal–outcome pairs from the same task and spends verification budget...

</details>

<details>
<summary><b>21. Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12865) • [📄 arXiv](https://arxiv.org/abs/2611.12865) • [📥 PDF](https://arxiv.org/pdf/2611.12865)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Even when task rewards accurately measure useful work and contextual requirements are explicit, RL can make agents more capable while reinforcing violations of those requirements. In Shortcuts and Boundaries, we construct scalable, verifiable rewa...

</details>

<details>
<summary><b>22. EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yuxiang Zhang, Lei Zhang, Bin Wang, Ruizhe Fan, Changti Wu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13907) • [📄 arXiv](https://arxiv.org/abs/2611.13907) • [📥 PDF](https://arxiv.org/pdf/2611.13907)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ChangtiWu/EVAThink)

> EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding When should a video VLM think, and when should it answer directly? We introduce EVAThink , which learns to make this choice based on the sufficiency of ava...

</details>

<details>
<summary><b>23. Learning to Act with World Models by Valuing What Comes Next</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12200) • [📄 arXiv](https://arxiv.org/abs/2611.12200) • [📥 PDF](https://arxiv.org/pdf/2611.12200)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/nuskonghou/wm-ppo)

> TL;DR. A sparse terminal reward says little about individual steps, yet each state transition can change the chances of success long before the reward arrives. WM-PPO learns from this information: a world model trained on real transitions predicts...

</details>

<details>
<summary><b>24. MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10649) • [📄 arXiv](https://arxiv.org/abs/2611.10649) • [📥 PDF](https://arxiv.org/pdf/2611.10649)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/huawei-csl/MACaQ)

> Hey everyone! My team at Huawei-CSL is open sourcing  🐵 MACAQ, the quantizer we’ve been using internally over the past few months. If you’re into local AI inference, give it a try and create your own GGUFs! We’d love to hear what you build and how...

</details>

<details>
<summary><b>25. Are Causal Neuron Circuits Unique and Transferable?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** omtekyav

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13885) • [📄 arXiv](https://arxiv.org/abs/2611.13885) • [📥 PDF](https://arxiv.org/pdf/2611.13885)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/omtekyav/causal-neuron-circuits)

> This paper started from a question about Goodfire's Lion King example ( Neural networks are already clean ), where removing an 18-neuron group in Qwen3-32B makes the model answer "Simba" instead of "Scar". Such a demonstration shows that the group...

</details>

<details>
<summary><b>26. Lipschitz-Controlled Flow Matching for Robust Image Restoration</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13995) • [📄 arXiv](https://arxiv.org/abs/2611.13995) • [📥 PDF](https://arxiv.org/pdf/2611.13995)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We investigate how small perturbations in degraded images can lead to large changes in the outputs of flow-matching restoration models. We introduce a Lipschitz-aware architecture and a sensitivity regularization strategy to make these models more...

</details>

<details>
<summary><b>27. TorchCurves: Differentiable Parametric Curves</b> ⭐ 70</summary>

<br/>

**👥 Authors:** Alex Shtoff

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14516) • [📄 arXiv](https://arxiv.org/abs/2611.14516) • [📥 PDF](https://arxiv.org/pdf/2611.14516)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/alexshtf/torchcurves)

> A PyTorch library for vectorized and differentiable parametric curves with learnable coefficients. Give each numerical feature its own curve, and a single call of the form Y = curves(X) turns every scalar in the batch into a point on its feature’s...

</details>

<details>
<summary><b>28. The Surprising Effectiveness of Deleting Weights in LLM Post-Training</b> ⭐ 41</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10866) • [📄 arXiv](https://arxiv.org/abs/2611.10866) • [📥 PDF](https://arxiv.org/pdf/2611.10866)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/agentic-learning-ai-lab/deleting-weights)

> We find that just deleting (zeroing) under 0.1% of an LLM's pretrained weights, with no other change, matches full fine-tuning at scale across RL, SFT, and self-distillation, while forgetting less. Deletion Tuning learns which weights to delete th...

</details>

<details>
<summary><b>29. Sable: A Small-Field Sumcheck Argument for Bit-Exact Inference of Large Language Models</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14083) • [📄 arXiv](https://arxiv.org/abs/2611.14083) • [📥 PDF](https://arxiv.org/pdf/2611.14083)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/moonmath-ai/Sable)

> Sable (Small-field Argument for Bit-exact LLM Execution) proves that a language model with committed weights produced a given reply to a given prompt, bit for bit. A client that receives the reply and the proof can check, without the GPU that ran ...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 29 |
| 📅 Today | [`2026-11-11.json`](data/daily/2026-11-11.json) | 29 |
| 📆 This Week | [`2026-W45.json`](data/weekly/2026-W45.json) | 83 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 353 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-11 | 29 | [View JSON](data/daily/2026-11-11.json) |
| 📄 2026-11-10 | 26 | [View JSON](data/daily/2026-11-10.json) |
| 📄 2026-11-09 | 28 | [View JSON](data/daily/2026-11-09.json) |
| 📄 2026-11-08 | 32 | [View JSON](data/daily/2026-11-08.json) |
| 📄 2026-11-07 | 32 | [View JSON](data/daily/2026-11-07.json) |
| 📄 2026-11-06 | 24 | [View JSON](data/daily/2026-11-06.json) |
| 📄 2026-11-05 | 32 | [View JSON](data/daily/2026-11-05.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W45 | 83 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 353 | [View JSON](data/monthly/2026-11.json) |
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
