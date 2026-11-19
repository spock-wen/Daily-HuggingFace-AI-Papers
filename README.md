<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-43-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9993+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">43</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">129</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">592</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9993+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 19, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Jeveration: System One Models Now Generate</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24738) • [📄 arXiv](https://arxiv.org/abs/2611.24738) • [📥 PDF](https://arxiv.org/pdf/2611.24738)

**💻 Code:** [⭐ Code](https://github.com/Carol-lyh/Jeveration) • [⭐ Code](https://github.com/huggingface)

> System One models such as Jev return decisions through fast, parallel prediction. In this paper, we introduce Jeveration, showing that the same decision paradigm can also generate high-quality images in a single forward pass. Jeveration builds on ...

</details>

<details>
<summary><b>2. The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23068) • [📄 arXiv](https://arxiv.org/abs/2611.23068) • [📥 PDF](https://arxiv.org/pdf/2611.23068)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: Much of the current community effort on agent evolution / RSI (across skills, harnesses, memory, etc.) is focusing on the wrong bottleneck. Proposing better artifacts is actually quite easy—the real challenge is reliably identifying whether...

</details>

<details>
<summary><b>3. ALIVE: Making Streaming Video Models Interactive</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21366) • [📄 arXiv](https://arxiv.org/abs/2611.21366) • [📥 PDF](https://arxiv.org/pdf/2611.21366)

**💻 Code:** [⭐ Code](https://github.com/lijinzhao30/ALIVE) • [⭐ Code](https://github.com/huggingface)

> 🚀 From Passive Video Understanding to Proactive, Interactive AI Assistants! We introduce ALIVE, an interactive streaming video model that goes beyond simply watching and answering questions. ALIVE enables three key capabilities: 🔵  Proactive Monit...

</details>

<details>
<summary><b>4. PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Hyunwoo J. Kim, Sojin Lee, Minseo Yoon, KyleBae1017

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.11318) • [📄 arXiv](https://arxiv.org/abs/2611.11318) • [📥 PDF](https://arxiv.org/pdf/2611.11318)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yms020615/PROLA)

> PROLA introduces Predictive Spatiotemporal Weather Downscaling (PSWD), a new task that jointly addresses future weather prediction and spatiotemporal resolution refinement. We propose a scaffold-and-correct framework and Principal-Orthogonal Low-r...

</details>

<details>
<summary><b>5. Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development</b> ⭐ 21</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24154) • [📄 arXiv](https://arxiv.org/abs/2611.24154) • [📥 PDF](https://arxiv.org/pdf/2611.24154)

**💻 Code:** [⭐ Code](https://github.com/game2player/Game2Player) • [⭐ Code](https://github.com/huggingface)

> Game2Player scales gameplay experience for visual agents by turning existing web games into verifiable environments. A coding player and a visual player test tasks, report problems, and collect training trajectories, yielding 568 games, 3,436 task...

</details>

<details>
<summary><b>6. HINT-WAM: Hindsight-Informed Training for World Action Models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Xinchao Wang, Qi Li, Phuong Tuan Dat

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24789) • [📄 arXiv](https://arxiv.org/abs/2611.24789) • [📥 PDF](https://arxiv.org/pdf/2611.24789)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tuandattt/hintwam_code)

> Project Website: https://tuandattt.github.io/hintwam/

</details>

<details>
<summary><b>7. CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Guanhua Chen, Yong Wang, Yun Chen, Zhuocheng Liang, zgxiao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24654) • [📄 arXiv](https://arxiv.org/abs/2611.24654) • [📥 PDF](https://arxiv.org/pdf/2611.24654)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> CurvDelta models the weight change ΔW directly in a low-curvature subspace. Projecting each gradient can still let an optimizer like Adam move the weights outside that space. Our parameterization keeps ΔW inside it throughout training. Our low-ran...

</details>

<details>
<summary><b>8. LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17600) • [📄 arXiv](https://arxiv.org/abs/2611.17600) • [📥 PDF](https://arxiv.org/pdf/2611.17600)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/eilamshapira/LightTAR)

> LightTAR quickly learns task-specific text and image features for tabular models, significantly improving predictive performance over standard frozen embeddings with minimal computational overhead.

</details>

<details>
<summary><b>9. WorldRuler: Interactive World Modeling under Configurable Rules</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24869) • [📄 arXiv](https://arxiv.org/abs/2611.24869) • [📥 PDF](https://arxiv.org/pdf/2611.24869)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AlayaLab/WorldRuler)

> We present WorldRuler: Interactive World Modeling under Configurable Rules, a framework for generating interactive video worlds that follow configurable rules.

</details>

<details>
<summary><b>10. Code World Model 2.0: Towards Infinite Controllable Video Generation</b> ⭐ 109</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22925) • [📄 arXiv](https://arxiv.org/abs/2611.22925) • [📥 PDF](https://arxiv.org/pdf/2611.22925)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/CodeWorldModel) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We’re sharing Invoker-Render, the video renderer behind Code World Model 2.0. It takes a structural proxy, a reference image, and a text prompt. A coarse proxy can tell the model where a character moves and let it synthesize a natural...

</details>

<details>
<summary><b>11. StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24408) • [📄 arXiv](https://arxiv.org/abs/2611.24408) • [📥 PDF](https://arxiv.org/pdf/2611.24408)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/chuangwang123/strideworld)

> Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect. Existing benchmarks mostly evaluate these p...

</details>

<details>
<summary><b>12. RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Chixiang Ma, Aosong Cheng, Sihan Chen, You Li, Ruisi Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24098) • [📄 arXiv](https://arxiv.org/abs/2611.24098) • [📥 PDF](https://arxiv.org/pdf/2611.24098)

**💻 Code:** [⭐ Code](https://github.com/Whalesong-zrs/RoughCut-Bench) • [⭐ Code](https://github.com/huggingface)

> Accepted to KDD 2027 We introduce RoughCut-Bench , a benchmark for automatic video rough-cut with large vision-language models. It covers two practical settings: visually driven editing—highlight selection, source-media ordering, and optional user...

</details>

<details>
<summary><b>13. PReMind: When Personal Memory Meets Visual Hazards</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23808) • [📄 arXiv](https://arxiv.org/abs/2611.23808) • [📥 PDF](https://arxiv.org/pdf/2611.23808)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce PReMind, a framework for safety-aware visual personalization, featuring a diagnostic benchmark for jointly evaluating visual hazard response and grounded personal-memory use, and a two-phase RL post-training scheme that integrates ada...

</details>

<details>
<summary><b>14. Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Bin Hu, Jian Huang, Tianyang Wu, Yuqi Xue, Yicheng He

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24733) • [📄 arXiv](https://arxiv.org/abs/2611.24733) • [📥 PDF](https://arxiv.org/pdf/2611.24733)

**💻 Code:** [⭐ Code](https://github.com/bruno686/CriticNPU) • [⭐ Code](https://github.com/huggingface)

> Feel free to discuss!

</details>

<details>
<summary><b>15. Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22287) • [📄 arXiv](https://arxiv.org/abs/2611.22287) • [📥 PDF](https://arxiv.org/pdf/2611.22287)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Latent diffusion needs no decoder: a linear head on a finetuned DiT matches or beats the decoder on FLUX.2 and Wan2.1, with 23% less warping error on video. Pixel diffusion recovers photorealistic texture with a separate output head, reaching 1.43...

</details>

<details>
<summary><b>16. StatePortal: Agentic Checkpoint Synthesis for Testing Deep States in Interactive Software</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23257) • [📄 arXiv](https://arxiv.org/abs/2611.23257) • [📥 PDF](https://arxiv.org/pdf/2611.23257)

**💻 Code:** [⭐ Code](https://github.com/pzy2000/State_Portal) • [⭐ Code](https://github.com/huggingface)

> Why replay long interaction sequences just to test deep states? 🚀 StatePortal uses AI agents to synthesize reusable checkpoints, making deep-state testing faster and more scalable.

</details>

<details>
<summary><b>17. Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement</b> ⭐ 52</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24651) • [📄 arXiv](https://arxiv.org/abs/2611.24651) • [📥 PDF](https://arxiv.org/pdf/2611.24651)

**💻 Code:** [⭐ Code](https://github.com/agentscope-ai/Piccolo) • [⭐ Code](https://github.com/huggingface)

> 🚀 Introducing Piccolo: #1 Multimodal Decision Model Series (0.8B–27B) Co-Evolved by AI Research Agents! Autonomous systems bottleneck on fast, reliable decisions—routing workflows, approving tool calls, filtering data, and interacting in real time...

</details>

<details>
<summary><b>18. Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14848) • [📄 arXiv](https://arxiv.org/abs/2611.14848) • [📥 PDF](https://arxiv.org/pdf/2611.14848)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Afterglow231/Tideway)

> Large language model (LLM) agents are rapidly becoming a dominant paradigm for AI applications. Recently, there is a growing demand to deploy large-scale Mixture-of-Experts (MoE) models locally on consumer PCs to balance data privacy, API costs, a...

</details>

<details>
<summary><b>19. QDA: Closed-Loop LLM Quantization Design with Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23388) • [📄 arXiv](https://arxiv.org/abs/2611.23388) • [📥 PDF](https://arxiv.org/pdf/2611.23388)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> QDA brings a coding agent into LLM quantization design. For each model and precision, the agent designs the post-training quantization recipe on its own, with no human in the loop. Its checkpoints beat the strongest public recipe on four reasoning...

</details>

<details>
<summary><b>20. WaveView: The Novel View Is in the Noise</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23994) • [📄 arXiv](https://arxiv.org/abs/2611.23994) • [📥 PDF](https://arxiv.org/pdf/2611.23994)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🌊 WaveView: The Novel View Is in the Noise Generative novel view synthesis usually gives the target camera to the diffusion model as conditioning: through extra control layers, camera positional encodings, or a reprojected depth image the model mu...

</details>

<details>
<summary><b>21. Late Entry in Looped Language Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24576) • [📄 arXiv](https://arxiv.org/abs/2611.24576) • [📥 PDF](https://arxiv.org/pdf/2611.24576)

**💻 Code:** [⭐ Code](https://github.com/Xalp/LateComer) • [⭐ Code](https://github.com/huggingface)

> TL;DR: Skipping initial passes and entering looped LLMs at the final K < T passes over a deep T-pass KV cache beats early exit; combined with pipelined cache completion and same-GEMM Wake verification in one CUDA graph, it delivers up to 5.23x (Ou...

</details>

<details>
<summary><b>22. LogT: Logically Think with Images for Visual Search</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19200) • [📄 arXiv](https://arxiv.org/abs/2611.19200) • [📥 PDF](https://arxiv.org/pdf/2611.19200)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> When answering questions about images, vision-language models (VLMs) can benefit from zooming in on small but important details, much like humans do. However, teaching VLMs when and how to zoom in typically requires complex post-training methods. ...

</details>

<details>
<summary><b>23. UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24941) • [📄 arXiv](https://arxiv.org/abs/2611.24941) • [📥 PDF](https://arxiv.org/pdf/2611.24941)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> UltraTex is a method for high-fidelity physically based rendering (PBR) texture generation for 3D assets. It focuses on aligning physical knowledge to generate detailed surface textures, with albedo, metallic, and roughness channels for rendering ...

</details>

<details>
<summary><b>24. VAE Rhythm: Temporal Decoding Traces for AI-Generated Video Detection</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21114) • [📄 arXiv](https://arxiv.org/abs/2611.21114) • [📥 PDF](https://arxiv.org/pdf/2611.21114)

**💻 Code:** [⭐ Code](https://github.com/showlab/vae-rhythm) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We are excited to share our work VAE Rhythm: Temporal Decoding Traces for AI-Generated Video Detection from Show Lab, NUS. As newer video generators learn to suppress visible artifacts, appearance-based cues become unreliable. Instead...

</details>

<details>
<summary><b>25. BiCAT: Bimanual Coordination Action Tokenization</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23499) • [📄 arXiv](https://arxiv.org/abs/2611.23499) • [📥 PDF](https://arxiv.org/pdf/2611.23499)

**💻 Code:** [⭐ Code](https://github.com/MAGICLAB-NUS/BiCAT) • [⭐ Code](https://github.com/huggingface)

> Autoregressive vision-language-action (VLA) models predict discrete action tokens with the next-token objective of their vision-language backbone, so the action tokenizer defines the interface between the policy and the robot. In bimanual manipula...

</details>

<details>
<summary><b>26. Chorus: Shared N-gram Embeddings with Layer-wise Adaptation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenyu Du, Stephen Chung

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23386) • [📄 arXiv](https://arxiv.org/abs/2611.23386) • [📥 PDF](https://arxiv.org/pdf/2611.23386)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dualverse-ai/chorus)

> N-gram embedding tables improve language models by storing learned representations of short token sequences, but recent designs commonly use separate tables at different layers, consuming substantial memory and preventing sharing. Chorus instead l...

</details>

<details>
<summary><b>27. FVScore: Specification-Driven Neuro-Symbolic Video Evaluation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22673) • [📄 arXiv](https://arxiv.org/abs/2611.22673) • [📥 PDF](https://arxiv.org/pdf/2611.22673)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing Faithfulness Video Score (FVScore), a neuro-symbolic framework for human-aligned and interpretable video generation evaluation.

</details>

<details>
<summary><b>28. Movie2Game-Bench: Holistic Evaluation of Film-to-Game Adaptation Beyond Playability</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Junjun He, Yiwen Zhang, Jialing Xie, yingmanji

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24669) • [📄 arXiv](https://arxiv.org/abs/2611.24669) • [📥 PDF](https://arxiv.org/pdf/2611.24669)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Movie2Game-Bench (M2G-bench) evaluates how AI coding agents adapt movies into playable browser games. Covering 22 films and 658 film-specific reference items, it assesses general game quality, movie-specific adaptation, and agent-based playtesting...

</details>

<details>
<summary><b>29. Out of Sight, Still in Mind: Token Compression for Omni-LLMs</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.21179) • [📄 arXiv](https://arxiv.org/abs/2607.21179) • [📥 PDF](https://arxiv.org/pdf/2607.21179)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/suho-yoo/ReMo)

> The goal of this paper is to reduce the input token cost of Omni-modal large language models (Omni-LLMs) at inference time. Omni-LLMs reason jointly over audio, video and text, but the cost of the three streams is highly unbalanced: visual tokens ...

</details>

<details>
<summary><b>30. Evidence-Based Credit Assignment for Search-Augmented Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23824) • [📄 arXiv](https://arxiv.org/abs/2611.23824) • [📥 PDF](https://arxiv.org/pdf/2611.23824)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We propose Evidence-based Credit Assignment (ECA), a training-only RL framework for search agents that scores how retrieved documents alone improve reference-answer likelihood—recovering dense step-level search credit even when all rollouts fail a...

</details>

<details>
<summary><b>31. Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yinjie Lei, Hengfu Yu, Tong Chu, Junzhuo Liu, davelee-uestc

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22668) • [📄 arXiv](https://arxiv.org/abs/2611.22668) • [📥 PDF](https://arxiv.org/pdf/2611.22668)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/davelee-uestc/chord_debiasing_public)

> We proposed CHORD (Cross-view Harmonic Outlier Reversal for Debiasing), a multi-view framework that allows samples to "sing in chorus" across diverse representation spaces to achieve robust cross-view consensus.

</details>

<details>
<summary><b>32. Learning Anisotropic Prediction Targets for Flow Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17767) • [📄 arXiv](https://arxiv.org/abs/2611.17767) • [📥 PDF](https://arxiv.org/pdf/2611.17767)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What target should a pixel flow model predict? Data, velocity, or something else? AnisoFlow makes the target fully learnable and interpretable. This improves JiT from 1.90 to 1.55 FID on ImageNet with no REPA, and removes patch artifacts in pixel ...

</details>

<details>
<summary><b>33. AVTR: Adaptive Multimodal Reasoning with Visual Imagination</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24161) • [📄 arXiv](https://arxiv.org/abs/2611.24161) • [📥 PDF](https://arxiv.org/pdf/2611.24161)

**💻 Code:** [⭐ Code](https://github.com/xiaoqian-shen/AVTR) • [⭐ Code](https://github.com/huggingface)

> Vision-Language Models increasingly rely on textual reasoning to solve advanced multimodal tasks. Despite its effectiveness, this paradigm faces two fundamental limitations. First, relying on textual reasoning alone can limit perceptual ability in...

</details>

<details>
<summary><b>34. PGPO: Prototype-Guided Progressive Obfuscation for Privacy-Preserving LLM-Enhanced Recommendation</b> ⭐ 156</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23236) • [📄 arXiv](https://arxiv.org/abs/2611.23236) • [📥 PDF](https://arxiv.org/pdf/2611.23236)

**💻 Code:** [⭐ Code](https://github.com/Shengxiang-Lin/PGPO) • [⭐ Code](https://github.com/huggingface)

> Keywords: LLM-Enhanced Recommendation; Privacy-Preserving; Reinforcement Learning TL;DR: PGPO protects item side information in LLM-enhanced recommendation by inducing semantic shift while preserving relational topology, reducing embedding inversi...

</details>

<details>
<summary><b>35. Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23751) • [📄 arXiv](https://arxiv.org/abs/2611.23751) • [📥 PDF](https://arxiv.org/pdf/2611.23751)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/middle-chunjie/AnyS1)

> Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow

</details>

<details>
<summary><b>36. PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** N. Asokan, Jiawen Zhang, Yihan Wang, Lipeng He

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24362) • [📄 arXiv](https://arxiv.org/abs/2611.24362) • [📥 PDF](https://arxiv.org/pdf/2611.24362)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Model developers use the attacks discovered during internal red-teaming to harden agents through adversarial training before deployment, a collaborative offensive-defensive process known in cybersecurity as purple-teaming. However, we show that ac...

</details>

<details>
<summary><b>37. NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22790) • [📄 arXiv](https://arxiv.org/abs/2611.22790) • [📥 PDF](https://arxiv.org/pdf/2611.22790)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 Excited to share NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding ! 🎬 SightForge builds verifiable tasks, SightLine benchmarks fine-grained reasoning, and SightLoop enables interactive, evidence-driven video understan...

</details>

<details>
<summary><b>38. DrawScore: Evaluating Generated CAD Models against Engineering Drawings</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yunhe Ni, Zaixi Li, Zhanyu Guo, Haorui Chen, SimonLu0306

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24681) • [📄 arXiv](https://arxiv.org/abs/2611.24681) • [📥 PDF](https://arxiv.org/pdf/2611.24681)

**💻 Code:** [⭐ Code](https://github.com/UESTC-Simon/DrawScore) • [⭐ Code](https://github.com/huggingface)

> Automatic CAD generation is commonly evaluated with volumetric IoU, Chamfer Distance, and surface F-score, which barely penalize local errors that occupy only a small fraction of a part's volume or surface area, such as a misplaced hole or a slot ...

</details>

<details>
<summary><b>39. A Foundation Model to Measure and Predict Human Behaviour</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24830) • [📄 arXiv](https://arxiv.org/abs/2611.24830) • [📥 PDF](https://arxiv.org/pdf/2611.24830)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ValueByte-AI/chiron)

> Large language models (LLMs) are increasingly used to infer psychological attributes, predict individual behaviour, and simulate human populations. However, despite generating plausible responses, they often misrepresent individuals and distort po...

</details>

<details>
<summary><b>40. Recurrent Domain Incremental Adaptation of Time-Series Foundation Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24075) • [📄 arXiv](https://arxiv.org/abs/2611.24075) • [📥 PDF](https://arxiv.org/pdf/2611.24075)

**💻 Code:** [⭐ Code](https://github.com/Sachithx/PACT) • [⭐ Code](https://github.com/huggingface)

> Chart-specific residual transports and an identity-preserving gate let a frozen TSFM adapt to recurring operating conditions from 5% labels, with no condition identity at test time. Above 0.95 macro-F1 on a four-condition bearing-fault stream, wit...

</details>

<details>
<summary><b>41. IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.24102) • [📄 arXiv](https://arxiv.org/abs/2611.24102) • [📥 PDF](https://arxiv.org/pdf/2611.24102)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Organizations increasingly deploy downloaded open-weight GUI agents. A backdoored agent passes acceptance tests on clean data and misbehaves only when a visual trigger appears on screen, turning an unvetted checkpoint into a supply-chain risk. How...

</details>

<details>
<summary><b>42. Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16933) • [📄 arXiv](https://arxiv.org/abs/2611.16933) • [📥 PDF](https://arxiv.org/pdf/2611.16933)

**💻 Code:** [⭐ Code](https://github.com/Manifestro/kezek) • [⭐ Code](https://github.com/huggingface)

> Kezek splits a mono recording of two people into one track per speaker, same length and timing. Overlaps and short replies ("yeah", "mm-hm") stay on the right person's track, and the two tracks sum exactly to the input. We built it to get two-chan...

</details>

<details>
<summary><b>43. Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22033) • [📄 arXiv](https://arxiv.org/abs/2611.22033) • [📥 PDF](https://arxiv.org/pdf/2611.22033)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large language models (LLMs) are increasingly deployed as autonomous shopping agents that process multimodal product listings (consisting of visual and text data) and recommend purchases on behalf of consumers. Naturally, one might assume that mod...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 43 |
| 📅 Today | [`2026-11-19.json`](data/daily/2026-11-19.json) | 43 |
| 📆 This Week | [`2026-W46.json`](data/weekly/2026-W46.json) | 129 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 592 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-19 | 43 | [View JSON](data/daily/2026-11-19.json) |
| 📄 2026-11-18 | 30 | [View JSON](data/daily/2026-11-18.json) |
| 📄 2026-11-17 | 30 | [View JSON](data/daily/2026-11-17.json) |
| 📄 2026-11-16 | 26 | [View JSON](data/daily/2026-11-16.json) |
| 📄 2026-11-15 | 34 | [View JSON](data/daily/2026-11-15.json) |
| 📄 2026-11-14 | 34 | [View JSON](data/daily/2026-11-14.json) |
| 📄 2026-11-13 | 24 | [View JSON](data/daily/2026-11-13.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W46 | 129 | [View JSON](data/weekly/2026-W46.json) |
| 📅 2026-W45 | 193 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 592 | [View JSON](data/monthly/2026-11.json) |
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
