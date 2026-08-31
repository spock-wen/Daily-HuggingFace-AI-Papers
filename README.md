<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-25-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6980+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">25</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">25</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">709</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6980+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 31, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering</b> ⭐ 67</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28281) • [📄 arXiv](https://arxiv.org/abs/2608.28281) • [📥 PDF](https://arxiv.org/pdf/2608.28281)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AMAP-ML/LoopArena)

> Excited to share LoopArena, a benchmark for Loop Engineering that measures how well a model can guide a fixed coding agent through long-running software development tasks. LoopArena evaluates this ability at three complementary levels, from indivi...

</details>

<details>
<summary><b>2. DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.18524) • [📄 arXiv](https://arxiv.org/abs/2608.18524) • [📥 PDF](https://arxiv.org/pdf/2608.18524)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 We introduce DART-SD , a topology-aware self-distillation framework for multi-turn tool-calling agents. Existing SFT and RL methods typically treat tool-use trajectories as linear sequences, which can incorrectly penalize valid alternative explo...

</details>

<details>
<summary><b>3. Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Mengkang Hu, Lixin Liu, Xilin Xia, Zhezheng Hao, Tianfu Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28122) • [📄 arXiv](https://arxiv.org/abs/2608.28122) • [📥 PDF](https://arxiv.org/pdf/2608.28122)

**💻 Code:** [⭐ Code](https://github.com/GeminiLight/awesome-agentic-artifact-creation) • [⭐ Code](https://github.com/huggingface)

> 🗺️ Excited to share our comprehensive survey on agentic artifact creation! We reviewed 200+ papers across six families (textual, vision, audio, video, spatio, and behavioral). We frame them as a stateful construction process with three key compone...

</details>

<details>
<summary><b>4. Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.27550) • [📄 arXiv](https://arxiv.org/abs/2608.27550) • [📥 PDF](https://arxiv.org/pdf/2608.27550)

**💻 Code:** [⭐ Code](https://github.com/starVLA/VLAct) • [⭐ Code](https://github.com/huggingface)

> Strong, open, and research-friendly. VLAct releases the data, models, and complete training/fine-tuning pipeline, with full continued pre-training requiring only 16 GPUs . It achieves 92.5% on RoboTwin 2.0 and ranks #6 on RoboDojo by Success Rate,...

</details>

<details>
<summary><b>5. Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning</b> ⭐ 202</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.27549) • [📄 arXiv](https://arxiv.org/abs/2608.27549) • [📥 PDF](https://arxiv.org/pdf/2608.27549)

**💻 Code:** [⭐ Code](https://github.com/mirros-lab/code-as-world) • [⭐ Code](https://github.com/huggingface)

> Pixels are evidence of the physical world, not its ontology. A pixel-level observation records how the world appears at a particular moment and from a particular viewpoint, but does not directly specify what exists within it, how it is structured,...

</details>

<details>
<summary><b>6. J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.26582) • [📄 arXiv](https://arxiv.org/abs/2608.26582) • [📥 PDF](https://arxiv.org/pdf/2608.26582)

**💻 Code:** [⭐ Code](https://github.com/GyoukChu/J-Zero) • [⭐ Code](https://github.com/huggingface)

> Frozen Judge set the upper bound of self-evolving LLMs. By co-evolving Judge with the current frontier of self-evolution, a highly performant and sustained self-evolution can be realized.

</details>

<details>
<summary><b>7. Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction</b> ⭐ 229</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.27529) • [📄 arXiv](https://arxiv.org/abs/2608.27529) • [📥 PDF](https://arxiv.org/pdf/2608.27529)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/amap-cvlab/ABot-Recon)

> ABot-Recon turns a single continuous video into a globally consistent 3D reconstruction in real time. Whether walking around a building with a phone, driving through city streets with a dashcam, or flying a drone over a campus, it reconstructs lon...

</details>

<details>
<summary><b>8. ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28476) • [📄 arXiv](https://arxiv.org/abs/2608.28476) • [📥 PDF](https://arxiv.org/pdf/2608.28476)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent/ContextPilot)

> ContextPilot extends context management with planning, structured memory, and soft context offloading. Its context-aware partial rollout focuses exploration on sensitive context-editing decisions, while fine-grained credit assignment trains interm...

</details>

<details>
<summary><b>9. LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency in Video Generation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28460) • [📄 arXiv](https://arxiv.org/abs/2608.28460) • [📥 PDF](https://arxiv.org/pdf/2608.28460)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yixuan-Ding-ZJU/LayerRecall)

> Autoregressive video diffusion enables scalable long-video generation by producing chunks from a bounded recent context. While recency-based caching preserves local continuity, it evicts historical cues needed when subjects, objects, scenes, or at...

</details>

<details>
<summary><b>10. Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090</b> ⭐ 37</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.27370) • [📄 arXiv](https://arxiv.org/abs/2608.27370) • [📥 PDF](https://arxiv.org/pdf/2608.27370)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/thu-pacman/Puro-Megatron)

> How much would it cost to pretrain a 2B LLM from scratch? $1M? $100K? Puro-2B matches Qwen2-1.5B for under $5,090, trained on RTX 5090s — with a fully open training recipe!

</details>

<details>
<summary><b>11. Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail Divergent Knowledge</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28478) • [📄 arXiv](https://arxiv.org/abs/2608.28478) • [📥 PDF](https://arxiv.org/pdf/2608.28478)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent/ElephantBench)

> ElephantBench is a closed-book knowledge probe for evaluating whether a language model remembers long-tail facts and whether it recalls the different verified accounts associated with those facts. The benchmark contains 1,094 questions using two f...

</details>

<details>
<summary><b>12. StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24777) • [📄 arXiv](https://arxiv.org/abs/2608.24777) • [📥 PDF](https://arxiv.org/pdf/2608.24777)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zheng977/StepGuard)

> LLM-based agents can interact with external environments through tool invocation, but this capability also introduces security risks such as file modification, information leakage, and unauthorized actions. Existing guardrails often evaluate compl...

</details>

<details>
<summary><b>13. Paint What You See: Benchmarking Dexterous Visual Tool Use in Multimodal Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.25417) • [📄 arXiv](https://arxiv.org/abs/2608.25417) • [📥 PDF](https://arxiv.org/pdf/2608.25417)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OOOHS/EASEL)

> Evaluation is shifting from static QA toward agentic settings where models act through external tools. We identify a critical yet underexplored capability within this space - dexterous visual tool use: fine-grained, closed-loop parameterized visua...

</details>

<details>
<summary><b>14. Act with Intent: Distilling Behavior Intent for Vision-Language-Action Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23478) • [📄 arXiv](https://arxiv.org/abs/2608.23478) • [📥 PDF](https://arxiv.org/pdf/2608.23478)

**💻 Code:** [⭐ Code](https://github.com/Leesangoh/INDI) • [⭐ Code](https://github.com/huggingface)

> What if VLA action decoders knew not only what action to execute, but also what the behavior is trying to achieve? We introduce Intention Distillation (INDI), which distills behavior-level intent from a frozen teacher VLM into the VLA action decod...

</details>

<details>
<summary><b>15. Locate Anything in Videos: Rethinking Efficient Generative Spatio-Temporal Video Grounding</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28192) • [📄 arXiv](https://arxiv.org/abs/2608.28192) • [📥 PDF](https://arxiv.org/pdf/2608.28192)

**💻 Code:** [⭐ Code](https://github.com/mbzuai-oryx/ParallelTubeDecoding) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>16. PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24115) • [📄 arXiv](https://arxiv.org/abs/2608.24115) • [📥 PDF](https://arxiv.org/pdf/2608.24115)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/worv-ai/PonderPounce)

> We’re excited to share PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control . Many robot tasks require remembering information that is no longer visible, such as a briefly shown target, an earlier instruction, or a demons...

</details>

<details>
<summary><b>17. Fast Weight Attention for Continual Learning</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Shuzhen Li, Jichen Feng, Jasper Zhang, Steve Ta, yifAI

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.27763) • [📄 arXiv](https://arxiv.org/abs/2608.27763) • [📥 PDF](https://arxiv.org/pdf/2608.27763)

**💻 Code:** [⭐ Code](https://github.com/yifanzhang-pro/fast-weight-attention) • [⭐ Code](https://github.com/huggingface)

> Fast Weight Attention for Continual Learning

</details>

<details>
<summary><b>18. Ring Forcing: Towards Precise Long-Term Memory for Autoregressive Video Diffusion</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yujia Zeng, Yuchen Lin, Brandon Y. Feng, chenguolin, BowenXue

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.26794) • [📄 arXiv](https://arxiv.org/abs/2608.26794) • [📥 PDF](https://arxiv.org/pdf/2608.26794)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>19. Video Generative Models as Geometry Learner</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiankang Deng, Xiatian Zhu, Zhensong Zhang, Jifei Song, Haosen Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28549) • [📄 arXiv](https://arxiv.org/abs/2608.28549) • [📥 PDF](https://arxiv.org/pdf/2608.28549)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. Rubric-to-Code Credit Assignment for Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.27906) • [📄 arXiv](https://arxiv.org/abs/2608.27906) • [📥 PDF](https://arxiv.org/pdf/2608.27906)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>21. StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24804) • [📄 arXiv](https://arxiv.org/abs/2608.24804) • [📥 PDF](https://arxiv.org/pdf/2608.24804)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> On ITBench, Qwen3.5-27B with an evolved harness beats GPT-5.5 on the baseline harness by 19.2 points. More capable models do not always make better enterprise agents. With the right harness, a smaller open-weight model can outperform a larger fron...

</details>

<details>
<summary><b>22. LMSM: LLM Security Framework Inspired by Linux Security Modules</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.25697) • [📄 arXiv](https://arxiv.org/abs/2608.25697) • [📥 PDF](https://arxiv.org/pdf/2608.25697)

**💻 Code:** [⭐ Code](https://github.com/xiuyuz/LMSM) • [⭐ Code](https://github.com/huggingface)

> LMSM converts pluggable model-internal evidence into per-request decisions and selective enforcement under continuous batching. By separating evidence backends from policy and enforcement, it provides a stable path for adopting stronger interpreta...

</details>

<details>
<summary><b>23. Training, learning and inference: unified dynamics of neural systems</b> ⭐ 0</summary>

<br/>

**👥 Authors:** wind342

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.20965) • [📄 arXiv](https://arxiv.org/abs/2608.20965) • [📥 PDF](https://arxiv.org/pdf/2608.20965)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wind342/gfg-training-learning-inference-experiments)

> This work presents an experiment-first causal study of training, learning, inference, and feedback in realized neural networks. Across Transformer/Adam, ResNet/SGD momentum, and diffusion U-Net/AdamW systems, the same core relation structure is pr...

</details>

<details>
<summary><b>24. GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Lawrence B. Hsieh, Pengfei Wei, Junyu Chen, Yiqun Sun

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.25375) • [📄 arXiv](https://arxiv.org/abs/2608.25375) • [📥 PDF](https://arxiv.org/pdf/2608.25375)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dukesun99/GGSS)

> GGSS (Geodesic-Gated Spherical Steering) is an inference-time debiasing method for generative vision-language models. GGSS reduces demographic bias in a frozen VLM by installing a lightweight forward hook on the vision-to-language projection layer...

</details>

<details>
<summary><b>25. Language Chain in Alignment: Cross-lingual Ranking Preference Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23149) • [📄 arXiv](https://arxiv.org/abs/2608.23149) • [📥 PDF](https://arxiv.org/pdf/2608.23149)

**💻 Code:** [⭐ Code](https://github.com/dltmddbs100/CRPO) • [⭐ Code](https://github.com/huggingface)

> The alignment of Large Language Models heavily relies on English-centric high-quality preference data, which often leads to suboptimal performance in other languages. In this paper, we propose Cross-lingual Ranking Preference Optimization~(CRPO), ...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 25 |
| 📅 Today | [`2026-08-31.json`](data/daily/2026-08-31.json) | 25 |
| 📆 This Week | [`2026-W35.json`](data/weekly/2026-W35.json) | 25 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 709 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-31 | 25 | [View JSON](data/daily/2026-08-31.json) |
| 📄 2026-08-30 | 23 | [View JSON](data/daily/2026-08-30.json) |
| 📄 2026-08-29 | 23 | [View JSON](data/daily/2026-08-29.json) |
| 📄 2026-08-28 | 21 | [View JSON](data/daily/2026-08-28.json) |
| 📄 2026-08-27 | 32 | [View JSON](data/daily/2026-08-27.json) |
| 📄 2026-08-26 | 14 | [View JSON](data/daily/2026-08-26.json) |
| 📄 2026-08-25 | 16 | [View JSON](data/daily/2026-08-25.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W35 | 25 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |
| 📅 2026-W32 | 156 | [View JSON](data/weekly/2026-W32.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |

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
