<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-30-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9920+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">56</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">519</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9920+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 17, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Sage S2.1 Flash Technical Report</b> ⭐ 22</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21072) • [📄 arXiv](https://arxiv.org/abs/2611.21072) • [📥 PDF](https://arxiv.org/pdf/2611.21072)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InternLM/Sage-S2.1-Flash)

> Try Sage S2.1 Flash for free at 👉 Sage InkStone (Duanyan)

</details>

<details>
<summary><b>2. AllocFlow: End-to-End Portfolio Trading Action Generation from Raw Market Data</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19937) • [📄 arXiv](https://arxiv.org/abs/2611.19937) • [📥 PDF](https://arxiv.org/pdf/2611.19937)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/allocflow/AllocFlow)

> Project Page: https://allocflow.github.io/

</details>

<details>
<summary><b>3. InclusionMed: Benchmarking AI for Inclusive Healthcare</b> ⭐ 27</summary>

<br/>

**👥 Authors:** The InclusionMed Collaboration

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21218) • [📄 arXiv](https://arxiv.org/abs/2611.21218) • [📥 PDF](https://arxiv.org/pdf/2611.21218)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/panuvi/inclusionmed)

> InclusionMed is an open evaluation initiative for inclusive healthcare. Through successive releases of the Atlas and Index, this open collaboration aims to ensure that the diverse healthcare needs of people worldwide guide how progress in medical ...

</details>

<details>
<summary><b>4. K2-Horizon: A Frontier Fleet of Open Source Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21003) • [📄 arXiv](https://arxiv.org/abs/2611.21003) • [📥 PDF](https://arxiv.org/pdf/2611.21003)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present K2-Horizon, a fleet of six fully open language models, from a 0.9B dense model to a 375B-A23B MoE, built for general-purpose reasoning and agentic work across math and science, software engineering, deep research, office automation, and...

</details>

<details>
<summary><b>5. SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.07222) • [📄 arXiv](https://arxiv.org/abs/2611.07222) • [📥 PDF](https://arxiv.org/pdf/2611.07222)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/saintmachines/spillway)

> Keep your LLM and AI agents. Add SPILLWAY. SPILLWAY 1.0.0, a real-time safety guard for AI agents, is the only one of seven prompt-injection defenses on AgentDojo with zero in-scope attack success in all 12 backbone-by-suite cells, and it has the ...

</details>

<details>
<summary><b>6. ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21607) • [📄 arXiv](https://arxiv.org/abs/2611.21607) • [📥 PDF](https://arxiv.org/pdf/2611.21607)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters

</details>

<details>
<summary><b>7. SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20218) • [📄 arXiv](https://arxiv.org/abs/2611.20218) • [📥 PDF](https://arxiv.org/pdf/2611.20218)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TokenWave-AI/swe-cowork-bench)

> A coding agent working within a software organization must establish what to build, collaborate with colleagues, and verify what it delivers. We introduce SWE-CoWork, a benchmark comprising 101 development assignments across 101 real repositories,...

</details>

<details>
<summary><b>8. PaperCritic: Training AI Reviewers to Assess the Soundness of Papers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17834) • [📄 arXiv](https://arxiv.org/abs/2611.17834) • [📥 PDF](https://arxiv.org/pdf/2611.17834)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> As AI conference submissions grow rapidly, AI reviewers are being considered as an alternative. However, simply imitating human reviewing is problematic because reviewing serves multiple purposes, including evaluating papers' soundness, interestin...

</details>

<details>
<summary><b>9. VoxMel TTS Technical Report</b> ⭐ 75</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20254) • [📄 arXiv](https://arxiv.org/abs/2611.20254) • [📥 PDF](https://arxiv.org/pdf/2611.20254)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VoxDance-Lab/VoxMel)

> VoxMel explores a different path for autoregressive TTS: generating directly in the continuous Mel spectrogram space, without relying on learned acoustic tokenizers. The key idea is to use wavelet decomposition to model acoustic information at dif...

</details>

<details>
<summary><b>10. Accelerate Bench: Evaluating Agents for Application-Level Program Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20882) • [📄 arXiv](https://arxiv.org/abs/2611.20882) • [📥 PDF](https://arxiv.org/pdf/2611.20882)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AdAstraAbyssoque/accelerate-bench)

> Hi Hugging Face community! We’re introducing Accelerate Bench , a benchmark for evaluating coding agents on application-level program optimization . 🧪 32 scientific workloads across 8 application areas Agents optimize complete CPU applications, in...

</details>

<details>
<summary><b>11. SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhijie Deng, Haonan Wang, Zetong Zhou, Jiachun Jin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17110) • [📄 arXiv](https://arxiv.org/abs/2611.17110) • [📥 PDF](https://arxiv.org/pdf/2611.17110)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. Calpha: Toward Native Biomolecular Intelligence in a General-Purpose Language Model</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20986) • [📄 arXiv](https://arxiv.org/abs/2611.20986) • [📥 PDF](https://arxiv.org/pdf/2611.20986)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yliust/Calpha)

> Excited to share Calpha , our open-source effort to bring native protein structure prediction into general-purpose LLMs! Instead of calling an external folding tool, Calpha equips Qwen3.5-9B with a flow-matching structure head that generates all-a...

</details>

<details>
<summary><b>13. MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos</b> ⭐ 22</summary>

<br/>

**👥 Authors:** Qi Tian, Yue Wu, Ryan Xu, Weijie Kong, Yunyang Ge

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21339) • [📄 arXiv](https://arxiv.org/abs/2611.21339) • [📥 PDF](https://arxiv.org/pdf/2611.21339)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent-Hunyuan/MovieRoll)

> Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs. To address these challenges, we present MovieRoll, a base-to-distilled framework that connects streaming fin...

</details>

<details>
<summary><b>14. Latent Feedback Is a Compute and Data Amplifier</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20404) • [📄 arXiv](https://arxiv.org/abs/2611.20404) • [📥 PDF](https://arxiv.org/pdf/2611.20404)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ifm-ai/LoRM)

> Code, data, checkpoints: https://github.com/ifm-ai/LoRM

</details>

<details>
<summary><b>15. DominoBench: Evaluating Multi-Step Physical Reasoning from Still Images</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20385) • [📄 arXiv](https://arxiv.org/abs/2611.20385) • [📥 PDF](https://arxiv.org/pdf/2611.20385)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can a vision-language model look at a still image of a chain reaction and tell who gets hit? DominoBench tests exactly that: 854 simulator-labelled scenes in minimal pairs, where one quantity moves one grid  step and one person's fate flips. What ...

</details>

<details>
<summary><b>16. LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19649) • [📄 arXiv](https://arxiv.org/abs/2611.19649) • [📥 PDF](https://arxiv.org/pdf/2611.19649)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Looped Transformers improve parameter effi- ciency by repeatedly applying the same Trans- former layers. During autoregressive decoding, however, generating each token requires several sequential passes through these layers, leading to high decodi...

</details>

<details>
<summary><b>17. Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13685) • [📄 arXiv](https://arxiv.org/abs/2611.13685) • [📥 PDF](https://arxiv.org/pdf/2611.13685)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/llong-cs/EgoGuidance)

> Can inexpensive, readily available human egocentric videos benefit embodied tasks without explicit action annotations? We design an architecture to uncover the implicit mutual information between actions and video, and explore its potential for ge...

</details>

<details>
<summary><b>18. JEPA4R: Embodied JEPA World Models with 4D Point Planning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19771) • [📄 arXiv](https://arxiv.org/abs/2611.19771) • [📥 PDF](https://arxiv.org/pdf/2611.19771)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/JEPA4R) • [⭐ Code](https://github.com/huggingface)

> JEPA4R: A point-cloud JEPA world model for robot manipulation and zero-shot sim-to-real transfer. Project page and videos: https://aigeeksgroup.github.io/JEPA4R Code: https://github.com/AIGeeksGroup/JEPA4R

</details>

<details>
<summary><b>19. Correcting Persistent Failures in Point-Cloud Grasping Policies using Human Demonstrations in Virtual Reality</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18919) • [📄 arXiv](https://arxiv.org/abs/2611.18919) • [📥 PDF](https://arxiv.org/pdf/2611.18919)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We found that RL makes a point-cloud grasping policy much better on average, but can leave particular object–pose combinations persistently unsolved. So we built a failure loop: mine those cases, show them to a person in VR, then use their two fin...

</details>

<details>
<summary><b>20. UMM-JEPA: Generative Pretraining via Masked Next-Scale Representation Prediction for Unified Multimodal Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jianbing Shen, Di Yin, Yunjia Xi, Yucheng Zhou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18668) • [📄 arXiv](https://arxiv.org/abs/2611.18668) • [📥 PDF](https://arxiv.org/pdf/2611.18668)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> UMM-JEPA proposes a generative pretraining framework based on masked next-scale representation prediction, aligning visual generation with the perceptual representations required for visual understanding.

</details>

<details>
<summary><b>21. Termination Lag: Coding Agents Solve Early but Stop Late</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14960) • [📄 arXiv](https://arxiv.org/abs/2611.14960) • [📥 PDF](https://arxiv.org/pdf/2611.14960)

**💻 Code:** [⭐ Code](https://github.com/musacim/termination-lag) • [⭐ Code](https://github.com/huggingface)

> What if coding agents already solved the problem but don't know when to stop? We studied 5 LLMs, 2 agent frameworks, and 3 SWE-bench datasets, tracking and evaluating intermediate code patches throughout agent execution. 🔍 Key findings: 38–82% of ...

</details>

<details>
<summary><b>22. LynnReal-Hand: Unlocking World Interaction with Hand Control</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Weijie Ma, Xiaofeng Mao, Chaoyang Zhang, Shaohao Rui

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21479) • [📄 arXiv](https://arxiv.org/abs/2611.21479) • [📥 PDF](https://arxiv.org/pdf/2611.21479)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LynnReal-AI/LynnReal/blob/main/docs/inference.md) • [⭐ Code](https://github.com/LynnReal-AI/LynnReal)

> Paper · Code · Inference guide

</details>

<details>
<summary><b>23. OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Xudong Liu, Shengding Jiao, Yao Chen, Yuecheng Hong, admin-blackjack

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17933) • [📄 arXiv](https://arxiv.org/abs/2611.17933) • [📥 PDF](https://arxiv.org/pdf/2611.17933)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/adminblackjack/OutfitterBench)

> Hi everyone! Author here — happy to share OutfitterBench and answer any questions. Most agent benchmarks reset constraints between tasks or model consumable inventory. We built OutfitterBench to test what happens over 200 operating days when an ag...

</details>

<details>
<summary><b>24. Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Víctor Gallego

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19537) • [📄 arXiv](https://arxiv.org/abs/2611.19537) • [📥 PDF](https://arxiv.org/pdf/2611.19537)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/vicgalle/craftax-program-policies)

> From https://github.com/vicgalle/craftax-program-policies :

</details>

<details>
<summary><b>25. Centered Ablation: Why Last-Layer Directional Ablation Under-Fires or Collapses, and a Closed-Form Fix</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20148) • [📄 arXiv](https://arxiv.org/abs/2611.20148) • [📥 PDF](https://arxiv.org/pdf/2611.20148)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/knoveleng/centered-ablation)

> At the last layer, directional ablation is exactly a logit bias scaled by a cosine with the hidden state. Hidden states share a large common mode far from the origin, so the standard direction fires on benign text and under-fires on its target. Ce...

</details>

<details>
<summary><b>26. GlyphAtlas: Disentangling Stroke Detail from Layout for Scene Text Synthesis</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yiyi Zhou, Changhai Zhou, Fr0zencr4nE

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20192) • [📄 arXiv](https://arxiv.org/abs/2611.20192) • [📥 PDF](https://arxiv.org/pdf/2611.20192)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Fr0zenCrane/GlyphAtlas)

> 🚀 Excited to introduce GlyphAtlas, a scene text synthesis model built on FLUX.1-Fill-dev—fully open-sourced with code, weights, and a 1.5M dataset! ⚠️ Why existing methods struggle: Standard approaches rely on a scene-aligned glyph image to specif...

</details>

<details>
<summary><b>27. Zuse: A Decision Model for European Languages</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06238) • [📄 arXiv](https://arxiv.org/abs/2611.06238) • [📥 PDF](https://arxiv.org/pdf/2611.06238)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> How we trained Zuse, a decision model, across 27 European languages. Decision models answer a fixed question about a document (yes/no, which category) with a probability, instead of generating text. The paper covers the training data (permissive p...

</details>

<details>
<summary><b>28. Dataset Distillation via Drifting</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vincent Sitzmann, Antonio Torralba, Giannis Daras, Angelina Quan, George Cazenavette

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16642) • [📄 arXiv](https://arxiv.org/abs/2611.16642) • [📥 PDF](https://arxiv.org/pdf/2611.16642)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Tweet: https://x.com/GCazenavette/status/2121322809532268591

</details>

<details>
<summary><b>29. A Reinforcement Learning Method to Navigate SMEFT Operator Space</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21439) • [📄 arXiv](https://arxiv.org/abs/2611.21439) • [📥 PDF](https://arxiv.org/pdf/2611.21439)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ReinforcePhysics) • [⭐ Code](https://github.com/ReinforcePhysics/ReinforceSMEFT)

> A reinforcement learning agent with a lightweight actor-critic architecture explores the Standard Model Effective Field Theory operator space to discover diverse high-quality theory hypotheses and improve global fits.

</details>

<details>
<summary><b>30. Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Wenbin Dai, Yiran Zhang, Hao Zheng, Hanbo Huang, Xuan Gong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09614) • [📄 arXiv](https://arxiv.org/abs/2605.09614) • [📥 PDF](https://arxiv.org/pdf/2605.09614)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/coder-gx/RAPO)

> RAPO: Keeping Visual Evidence in the Loop during Long-Chain Reasoning Excited to share our NeurIPS 2026 paper, Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning ! As multimodal reasoning chains grow longe...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 30 |
| 📅 Today | [`2026-11-17.json`](data/daily/2026-11-17.json) | 30 |
| 📆 This Week | [`2026-W46.json`](data/weekly/2026-W46.json) | 56 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 519 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-17 | 30 | [View JSON](data/daily/2026-11-17.json) |
| 📄 2026-11-16 | 26 | [View JSON](data/daily/2026-11-16.json) |
| 📄 2026-11-15 | 34 | [View JSON](data/daily/2026-11-15.json) |
| 📄 2026-11-14 | 34 | [View JSON](data/daily/2026-11-14.json) |
| 📄 2026-11-13 | 24 | [View JSON](data/daily/2026-11-13.json) |
| 📄 2026-11-12 | 18 | [View JSON](data/daily/2026-11-12.json) |
| 📄 2026-11-11 | 29 | [View JSON](data/daily/2026-11-11.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W46 | 56 | [View JSON](data/weekly/2026-W46.json) |
| 📅 2026-W45 | 193 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 519 | [View JSON](data/monthly/2026-11.json) |
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
