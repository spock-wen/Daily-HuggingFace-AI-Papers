<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-49-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9036+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">49</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">158</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1275</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9036+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 21, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Focused Omni-Modal GUI Agents</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26203) • [📄 arXiv](https://arxiv.org/abs/2610.26203) • [📥 PDF](https://arxiv.org/pdf/2610.26203)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/fyzhang1/FocusGUI)

> Focused Omni-Modal GUI Agents

</details>

<details>
<summary><b>2. PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27628) • [📄 arXiv](https://arxiv.org/abs/2610.27628) • [📥 PDF](https://arxiv.org/pdf/2610.27628)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 Introducing PAR, our new work on length extrapolation in looped language models. 📦 The task is simple: five boxes, one object in each. Follow a sequence of swaps, then answer what’s inside. We train the model on short sequences and test whether ...

</details>

<details>
<summary><b>3. Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Puyi Wang, Biao Jiang, Kaiqin Kong, Jihai Zhang, rickchains

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27999) • [📄 arXiv](https://arxiv.org/abs/2610.27999) • [📥 PDF](https://arxiv.org/pdf/2610.27999)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SkyworkAI/Matrix-Game)

> Github: https://github.com/SkyworkAI/Matrix-Game

</details>

<details>
<summary><b>4. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26855) • [📄 arXiv](https://arxiv.org/abs/2610.26855) • [📥 PDF](https://arxiv.org/pdf/2610.26855)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ropedia/ropedia-w0)

> Ropedia W0 is an egocentric world foundation model that learns loco-manipulation from 10K hours of human experience and transfers it across embodiments — from robot arms to humanoids, and from grippers to dexterous hands — through one shared kinem...

</details>

<details>
<summary><b>5. S-Agent 2.0: Spatial Reasoning with a General Coding Agent</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28354) • [📄 arXiv](https://arxiv.org/abs/2610.28354) • [📥 PDF](https://arxiv.org/pdf/2610.28354)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ropedia/S-Agent-2.0)

> S-Agent 2.0 is a spatial reasoning agent built on an off-the-shelf general coding agent and a command-line perception toolkit.

</details>

<details>
<summary><b>6. VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25043) • [📄 arXiv](https://arxiv.org/abs/2610.25043) • [📥 PDF](https://arxiv.org/pdf/2610.25043)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJU-OmniAI/VLA-Rolling)

> Why restart from noise when useful actions are already there? Current VLA paradigm typically execute only a short prefix before replanning with updated observations, then discard the unexecuted action tail. VLA-Rolling carries forward the unexecut...

</details>

<details>
<summary><b>7. Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition</b> ⭐ 571</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28578) • [📄 arXiv](https://arxiv.org/abs/2610.28578) • [📥 PDF](https://arxiv.org/pdf/2610.28578)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InternScience/Agents-A1)

> 🚀 We've open-sourced Sage-A1.5, a 35B MoE agentic model from Shanghai AI Laboratory! Its key strengths include: 💻 Coding: Tackles complex, multi-step coding tasks with coordinated execution and verification. 🤝 Agentic orchestration: Delegates work...

</details>

<details>
<summary><b>8. CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tiankuo Yao, Cong Pang, Jie-Jing Shao, Guibin Zhang, Jiaqi Su

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25078) • [📄 arXiv](https://arxiv.org/abs/2610.25078) • [📥 PDF](https://arxiv.org/pdf/2610.25078)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We identify the persistent "brain–body mismatch" problem in recursive self-improving agents, where an evolving execution harness (body) falls out of sync with the underlying model's capabilities (brain). To address this, we propose CoEvo-RSI, a fr...

</details>

<details>
<summary><b>9. Learning the 4D World through Point Trajectory Forecasting</b> ⭐ 10</summary>

<br/>

**👥 Authors:** Jungwoo Park, Jonghoon Lee, Dohyeon Kim, Sunghwan Hong, Byungwoo Jeon

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28594) • [📄 arXiv](https://arxiv.org/abs/2610.28594) • [📥 PDF](https://arxiv.org/pdf/2610.28594)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/rootyJeon/VPM)

> No abstract available.

</details>

<details>
<summary><b>10. SolarRenderer: Few-Step Generative Reference Rendering</b> ⭐ 153</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28630) • [📄 arXiv](https://arxiv.org/abs/2610.28630) • [📥 PDF](https://arxiv.org/pdf/2610.28630)

**💻 Code:** [⭐ Code](https://github.com/Enderfga/SolarRenderer) • [⭐ Code](https://github.com/huggingface)

> SolarRenderer turns any engine's untextured structure pass into a finished, styled video, guided by a reference first frame. The model is built on MiniMax-H3, with a control LoRA and a few-step distilled LoRA. 🎯 Precise structure. The output follo...

</details>

<details>
<summary><b>11. SWIFT: Self-guided Weak-to-strong dIFfusion models via Target extrapolation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25844) • [📄 arXiv](https://arxiv.org/abs/2610.25844) • [📥 PDF](https://arxiv.org/pdf/2610.25844)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce SWIFT , a simple and effective weak-to-strong self-guided training method. It uses a weaker model to improve a stronger diffusion model through target extrapolation , without adding inference overhead. On ImageNet-256, SWIFT surpasses...

</details>

<details>
<summary><b>12. Correction Training for Diffusion Models</b> ⭐ 65</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14136) • [📄 arXiv](https://arxiv.org/abs/2610.14136) • [📥 PDF](https://arxiv.org/pdf/2610.14136)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sunovivid/correction-training)

> ✨Correction Training for Diffusion Models✨ Donghoon Ahn¹, Runqian Wang¹, Alexei A. Efros¹, Taesung Park², Yash Belhe² ¹ UC Berkeley  ² Reve Can diffusion models generate high-quality images without classifier-free guidance? Yes! We introduce corre...

</details>

<details>
<summary><b>13. MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Ji Soo Lee, Dohwan Ko, Jongha Kim, Seohyun Lee, choisw0823

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27911) • [📄 arXiv](https://arxiv.org/abs/2610.27911) • [📥 PDF](https://arxiv.org/pdf/2610.27911)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mlvlab/MMEnterprise-Bench)

> How reliable are enterprise agents when workplace records disagree or change over time? MMEnterprise-Bench evaluates this challenge with 1,613 questions across 30 simulated collaboration projects, grounded in 7,140 textual and visual records. It t...

</details>

<details>
<summary><b>14. LLM2R: From Large Language Models to 3D Reassemblers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18604) • [📄 arXiv](https://arxiv.org/abs/2610.18604) • [📥 PDF](https://arxiv.org/pdf/2610.18604)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 3D part assembly aims to reconstruct a complete shape from a set of unassembled parts by predicting a rigid SE(3) transformation for each part. Because the placement of a part is rarely determined by its own geometry, the task demands reasoning ov...

</details>

<details>
<summary><b>15. PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning</b> ⭐ 34</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26067) • [📄 arXiv](https://arxiv.org/abs/2610.26067) • [📥 PDF](https://arxiv.org/pdf/2610.26067)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zju3dv/PhysSkin)

> No abstract available.

</details>

<details>
<summary><b>16. Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mingxuan Zhang, Xinkai WAng, Xinfeng Xia, Xiaofeng Hou, Wenfeng Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2511.14102) • [📄 arXiv](https://arxiv.org/abs/2511.14102) • [📥 PDF](https://arxiv.org/pdf/2511.14102)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ASPLOS 2027

</details>

<details>
<summary><b>17. Painting Change Map as guidance for generating painting processes</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25369) • [📄 arXiv](https://arxiv.org/abs/2610.25369) • [📥 PDF](https://arxiv.org/pdf/2610.25369)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Markus-Pobitzer/painting-change-map)

> We first predict where and when a painter worked on the canvas (a painting change map), then render the painting process from it. The Painting Change Map:

</details>

<details>
<summary><b>18. EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28444) • [📄 arXiv](https://arxiv.org/abs/2610.28444) • [📥 PDF](https://arxiv.org/pdf/2610.28444)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VisionXLab/EvaOmni)

> Hi everyone! 👋 I’m an author of EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning . We’re excited to share our work with the Hugging Face community! In this paper, we address the challenge of evaluating whether models’ answers are...

</details>

<details>
<summary><b>19. Breaking Diffusion: Parallel Reasoning with Draft Refinement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26542) • [📄 arXiv](https://arxiv.org/abs/2610.26542) • [📥 PDF](https://arxiv.org/pdf/2610.26542)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Draft Refinement Language Models (DRLMs) , a new approach to parallel reasoning that generates a complete draft and iteratively refines it , rather than generating tokens sequentially or following a diffusion reverse process. DRLM use...

</details>

<details>
<summary><b>20. Evolving Agent Interfaces</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Bhuvan Chandra Koduru, Gonzalo Gonzalez-Pumariega, Yuzhe Yang, Saaket Agashe, xw-eric

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28601) • [📄 arXiv](https://arxiv.org/abs/2610.28601) • [📥 PDF](https://arxiv.org/pdf/2610.28601)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>21. From Short Clips to Real-Time Streams: Identity-Aware Supervision and Context-Efficient Generation for Video Face Swapping</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Xuehao Wang, Haoyu Huang, Ruiqi Ma, Yuwei Liang, CrazyK828

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26681) • [📄 arXiv](https://arxiv.org/abs/2610.26681) • [📥 PDF](https://arxiv.org/pdf/2610.26681)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aim-uofa/StreamingSwap)

> Hello~ We introduce StreamingSwap, a reference-guided face swapping method for real-time video streams, preserving target attributes and motion. project page: https://aim-uofa.github.io/StreamingSwap/ code: https://github.com/aim-uofa/StreamingSwa...

</details>

<details>
<summary><b>22. DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28522) • [📄 arXiv](https://arxiv.org/abs/2610.28522) • [📥 PDF](https://arxiv.org/pdf/2610.28522)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/StartLuxLabs/DecisionPivot)

> Decision models support routing, guardrails, and output verification in LLM systems. However, item accuracy alone cannot establish whether models make correct decisions across controlled variations or assign reliable confidence to their prediction...

</details>

<details>
<summary><b>23. Event-STVG: Spatio-Temporal Video Grounding for Long-Form Event Reasoning</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Leo Jiahao Jiang, Xujie Tang, Songqi Tang, Xujia Wang, zacharyz21

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22444) • [📄 arXiv](https://arxiv.org/abs/2610.22444) • [📥 PDF](https://arxiv.org/pdf/2610.22444)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/THU-KEG/EventSTVG)

> Event-STVG introduces a challenging benchmark requiring multimodal models to perform long-form event reasoning, repeated-event disambiguation, and multi-target spatio-temporal grounding across extended video contexts.

</details>

<details>
<summary><b>24. EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24648) • [📄 arXiv](https://arxiv.org/abs/2610.24648) • [📥 PDF](https://arxiv.org/pdf/2610.24648)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/pillor9/EdgeKernelBench)

> This paper introduces EdgeKernelBench, which asks: Can LLMs generate correct and efficient kernels across heterogeneous edge devices through a unified intermediate representation? We also introduce the Layered Edge Kernel Agent (LEKA), which organ...

</details>

<details>
<summary><b>25. Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24944) • [📄 arXiv](https://arxiv.org/abs/2610.24944) • [📥 PDF](https://arxiv.org/pdf/2610.24944)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/BakeLab/Epi-results)

> We present Épi, an autonomous research agent that sustains investigations across model sessions and evolves its methods through accumulated experience. Épi combines persistent research history, hierarchical memory, branching and independent review...

</details>

<details>
<summary><b>26. FlowState: Execution State as Memory for Long-Horizon LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34565) • [📄 arXiv](https://arxiv.org/abs/2609.34565) • [📥 PDF](https://arxiv.org/pdf/2609.34565)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We explore how long-horizon LLM agents can preserve useful information without repeatedly loading their entire interaction history. FlowState maintains structured execution states linked to original tool observations, updates them as tasks progres...

</details>

<details>
<summary><b>27. Good Judgment, Bad Advice: Decision-Model Controllers Raise Agent Cost Without Improving Success</b> ⭐ 0</summary>

<br/>

**👥 Authors:** namanvats

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24649) • [📄 arXiv](https://arxiv.org/abs/2610.24649) • [📥 PDF](https://arxiv.org/pdf/2610.24649)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/namanvats/decision-model-controllers)

> Can a specialized decision model make AI agents more efficient, or does it just add overhead? We investigate whether delegating decisions like when to stop, verify, or change approach to a specialized decision model improves agent performance. Usi...

</details>

<details>
<summary><b>28. HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26426) • [📄 arXiv](https://arxiv.org/abs/2610.26426) • [📥 PDF](https://arxiv.org/pdf/2610.26426)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Rubric-based reinforcement learning enables open-ended generation using natural-language criteria as rewards, but these signals can become ineffective as the policy evolves. We identify two failure modes: non-discriminative rewards, where scores c...

</details>

<details>
<summary><b>29. Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28632) • [📄 arXiv](https://arxiv.org/abs/2610.28632) • [📥 PDF](https://arxiv.org/pdf/2610.28632)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing Joints, Camera, Action! (JCA), co-generating video and replayable 3D motion for arbitrary rigs. Given text and a rig, JCA generates video together with 3D motion that responds to the surrounding scene. It also recovers the camera, allo...

</details>

<details>
<summary><b>30. More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27406) • [📄 arXiv](https://arxiv.org/abs/2610.27406) • [📥 PDF](https://arxiv.org/pdf/2610.27406)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! 👋 Can more memory make an LLM agent worse? We study error reproduction: mistakes in stored rules or skills can shape future executions, which then produce new abstractions that regenerate the same mistakes. We propose Anti-Persistence...

</details>

<details>
<summary><b>31. Large Flow Language Models</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Seunghoon Hong, Jaehoon Yoo, Udbhav Bamba, Arnav Chavan, david3684

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28559) • [📄 arXiv](https://arxiv.org/abs/2610.28559) • [📥 PDF](https://arxiv.org/pdf/2610.28559)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lafa-gh/large-flow-lms)

> Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We pr...

</details>

<details>
<summary><b>32. λ_0: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation</b> ⭐ 25</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18950) • [📄 arXiv](https://arxiv.org/abs/2610.18950) • [📥 PDF](https://arxiv.org/pdf/2610.18950)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LambdaHumanoid/openlambda)

> Introducing λ₀ and HumanVerse, a 500-hour dataset pairing egocentric video with synchronized body and hand motion. The paper studies how scaling robot-aligned whole-body human demonstrations improves humanoid loco-manipulation. Resources: Project ...

</details>

<details>
<summary><b>33. Harness Self-Evolution for Long-Horizon Terminal Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27435) • [📄 arXiv](https://arxiv.org/abs/2610.27435) • [📥 PDF](https://arxiv.org/pdf/2610.27435)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! First author here 👋 Can an agent become more reliable by improving its harness while keeping model weights fixed? We introduce RiseHarness, a framework for iterative harness self-evolution. It studies tasks where the same agent someti...

</details>

<details>
<summary><b>34. HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24899) • [📄 arXiv](https://arxiv.org/abs/2610.24899) • [📥 PDF](https://arxiv.org/pdf/2610.24899)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This work introduces HybridResearcher, a 4B agent trained to bridge evidence across the structured and unstructured boundary, and synthesizes cross-source bridge trajectories by starting with validated single-source tasks and fabricating the missi...

</details>

<details>
<summary><b>35. Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19425) • [📄 arXiv](https://arxiv.org/abs/2610.19425) • [📥 PDF](https://arxiv.org/pdf/2610.19425)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Agentic capabilities are increasingly important for modern LLMs, yet remain difficult to evaluate during pretraining. Existing approaches typically rely on static trajectory-derived tasks or likelihood-based proxies, which are lightweight but prov...

</details>

<details>
<summary><b>36. Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27327) • [📄 arXiv](https://arxiv.org/abs/2610.27327) • [📥 PDF](https://arxiv.org/pdf/2610.27327)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing TEAL (Tool Evolution for Analytics over data Lakes), a method that builds up a library of reusable tools and usage skills for a fixed worker agent without any labels, so coding agents answering data-lake questions can reuse their data ...

</details>

<details>
<summary><b>37. OmniCam: Omni-Camera Trajectory Generation via Geometry-Grounded Pose Token Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiangyang Xue, Xuhui Zuo, Yisu Zhang, Chenjie Cao, Zhenyang Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09513) • [📄 arXiv](https://arxiv.org/abs/2610.09513) • [📥 PDF](https://arxiv.org/pdf/2610.09513)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> World Models Need Direction.

</details>

<details>
<summary><b>38. Multimodal Reranking Is a System One Decision</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yu Xiao, Yao Zhang, Zhuchenyang Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28435) • [📄 arXiv](https://arxiv.org/abs/2610.28435) • [📥 PDF](https://arxiv.org/pdf/2610.28435)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ryenhails/rerank-as-decision)

> Multimodal rerankers are usually dedicated models. We argue that a general VLM can also do the job: reranking is a System One decision , with the query and its candidates as the state and the candidates as the options. One forward pass gives one p...

</details>

<details>
<summary><b>39. EMBER: Predicting TCR--pMHC Binding Without a Docked Complex</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27334) • [📄 arXiv](https://arxiv.org/abs/2610.27334) • [📥 PDF](https://arxiv.org/pdf/2610.27334)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A new PPI classification model proposed submitted in ICLR2027

</details>

<details>
<summary><b>40. On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27190) • [📄 arXiv](https://arxiv.org/abs/2610.27190) • [📥 PDF](https://arxiv.org/pdf/2610.27190)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/chenpanli/fragility)

> TL;DR: When prompts are composed of many tasks, language models systematically reduce their reasoning effort across tasks according to a power law, causing failures on those that require more effort. By adjusting task grouping based on task fragil...

</details>

<details>
<summary><b>41. Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31002) • [📄 arXiv](https://arxiv.org/abs/2606.31002) • [📥 PDF](https://arxiv.org/pdf/2606.31002)

**💻 Code:** [⭐ Code](https://github.com/grenadeComing/beyond-compilation) • [⭐ Code](https://github.com/huggingface)

> A Lean statement can compile and still state a different theorem from the one intended. We evaluate natural-language-to-Lean statement formalization without reference Lean targets on 227 university-level statements. Compile rate overstates faithfu...

</details>

<details>
<summary><b>42. WinARDet: Compressed Window Auto-Regression for Long-Horizon Vision-Language Grounding</b> ⭐ 17</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19419) • [📄 arXiv](https://arxiv.org/abs/2610.19419) • [📥 PDF](https://arxiv.org/pdf/2610.19419)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/facias914/WinARDet)

> MLLM-based detectors formulate vision-language grounding as autoregressive coordinate generation, yet in dense scenes, they often collapse into a box repetition loop, repeatedly emitting identical boxes until the decoding budget is exhausted. We t...

</details>

<details>
<summary><b>43. HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24452) • [📄 arXiv](https://arxiv.org/abs/2610.24452) • [📥 PDF](https://arxiv.org/pdf/2610.24452)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce HumanSkill-4D , a training-free framework for selecting body parts, clothing, and matching motion intervals of animatable Gaussian avatars through natural language. For example: “Highlight the pants while both knees are deeply bent.” ...

</details>

<details>
<summary><b>44. TRACE: Tracking Multimodal Clinical Trajectories for Inpatient Risk Prediction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Minjun Kim, SuperSupermoon

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25765) • [📄 arXiv](https://arxiv.org/abs/2610.25765) • [📥 PDF](https://arxiv.org/pdf/2610.25765)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>45. PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Chengjie Wang, Yabiao Wang, Zhenye Gan, Moran Li, KSZG

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26711) • [📄 arXiv](https://arxiv.org/abs/2610.26711) • [📥 PDF](https://arxiv.org/pdf/2610.26711)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/KSZG-11/PVBench)

> PVBench is a benchmark and toolkit for evaluating the physical plausibility of AI-generated videos. It aims to systematically assess whether object motion, spatial relationships, material changes, causal behavior, and mechanical laws depicted in v...

</details>

<details>
<summary><b>46. SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26837) • [📄 arXiv](https://arxiv.org/abs/2610.26837) • [📥 PDF](https://arxiv.org/pdf/2610.26837)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: SpecKCast is a training-free method that accelerates diffusion transformers by forecasting their output in the frequency domain with a lightweight Kalman filter. Each frequency band is forecast on its own clock, and the transformer runs onl...

</details>

<details>
<summary><b>47. PhysLDM: Latent Diffusion for High-Fidelity Deformable Simulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07609) • [📄 arXiv](https://arxiv.org/abs/2610.07609) • [📥 PDF](https://arxiv.org/pdf/2610.07609)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What if physics simulation worked like video generation? 🎬 PhysLDM is a latent diffusion paradigm for high-fidelity deformable simulation: a single model predicts an entire trajectory of a high-resolution soft body at once and generalizes zero-sho...

</details>

<details>
<summary><b>48. Muse Glimmer 30B: An On-Device Agentic Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24628) • [📄 arXiv](https://arxiv.org/abs/2610.24628) • [📥 PDF](https://arxiv.org/pdf/2610.24628)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Blog post: https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model

</details>

<details>
<summary><b>49. On the Limits of Scale: Inverse Scaling in Vision-Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27360) • [📄 arXiv](https://arxiv.org/abs/2610.27360) • [📥 PDF](https://arxiv.org/pdf/2610.27360)

**💻 Code:** [⭐ Code](https://github.com/saxenarohit/vlm_inverse_scaling) • [⭐ Code](https://github.com/huggingface)

> In this paper, we investigate does scaling a vision-language model improve every capability. We compare 19 open-weight VLMs (Qwen3-VL, InternVL3.5, Gemma 3, Molmo 2; 1B to 241B) on 8 benchmarks, comparing smaller and larger models on the same ques...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 49 |
| 📅 Today | [`2026-10-21.json`](data/daily/2026-10-21.json) | 49 |
| 📆 This Week | [`2026-W42.json`](data/weekly/2026-W42.json) | 158 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1275 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-21 | 49 | [View JSON](data/daily/2026-10-21.json) |
| 📄 2026-10-20 | 55 | [View JSON](data/daily/2026-10-20.json) |
| 📄 2026-10-19 | 54 | [View JSON](data/daily/2026-10-19.json) |
| 📄 2026-10-18 | 84 | [View JSON](data/daily/2026-10-18.json) |
| 📄 2026-10-17 | 84 | [View JSON](data/daily/2026-10-17.json) |
| 📄 2026-10-16 | 69 | [View JSON](data/daily/2026-10-16.json) |
| 📄 2026-10-15 | 63 | [View JSON](data/daily/2026-10-15.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W42 | 158 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1275 | [View JSON](data/monthly/2026-10.json) |
| 🗓️ 2026-09 | 781 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |

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
