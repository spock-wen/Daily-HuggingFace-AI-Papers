<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-32-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9583+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">143</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">182</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9583+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 05, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. From Pixels to Actions - Towards Native Vision-Language-Action Policies</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06918) • [📄 arXiv](https://arxiv.org/abs/2611.06918) • [📥 PDF](https://arxiv.org/pdf/2611.06918)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> NEO-VLA challenges a common assumption in VLA design: that action should rely on visual representations distilled for semantic understanding. Our findings suggest that effective control instead benefits from early visual computation. Native repres...

</details>

<details>
<summary><b>2. Turns Matter: Advancing Streaming Video RL via Turn-Level Credit</b> ⭐ 53</summary>

<br/>

**👥 Authors:** Hongrui Wu, Wenqi Shao, Linghan Chen, Kanghui Tian, shuai22

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06728) • [📄 arXiv](https://arxiv.org/abs/2611.06728) • [📥 PDF](https://arxiv.org/pdf/2611.06728)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XD111ds/turn-wise-rl)

> Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design w...

</details>

<details>
<summary><b>3. GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37257) • [📄 arXiv](https://arxiv.org/abs/2610.37257) • [📥 PDF](https://arxiv.org/pdf/2610.37257)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kangverse/GameVerse)

> Dataset is released at: https://huggingface.co/datasets/Kangverse/GameVerse

</details>

<details>
<summary><b>4. FrontierPhysics: Evaluating Agents for End-to-End Physics Research</b> ⭐ 0</summary>

<br/>

**👥 Authors:** dccc2025, bDAKNDS, wenbochen111, Benjamin-eecs, bingran-you

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06910) • [📄 arXiv](https://arxiv.org/abs/2611.06910) • [📥 PDF](https://arxiv.org/pdf/2611.06910)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>5. What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06483) • [📄 arXiv](https://arxiv.org/abs/2611.06483) • [📥 PDF](https://arxiv.org/pdf/2611.06483)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/GaryStack/Rethinking-Agent-RL)

> While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth K and interaction depth T via Pass@(K,T), we show that ...

</details>

<details>
<summary><b>6. PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05320) • [📄 arXiv](https://arxiv.org/abs/2611.05320) • [📥 PDF](https://arxiv.org/pdf/2611.05320)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DAGroup-PKU/PyRUA-Lean/tree/DataFarm)

> Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, th...

</details>

<details>
<summary><b>7. EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06518) • [📄 arXiv](https://arxiv.org/abs/2611.06518) • [📥 PDF](https://arxiv.org/pdf/2611.06518)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent-Hunyuan/EmoReward)

> Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has...

</details>

<details>
<summary><b>8. StreamDuo: A Live Commentator and a Research Agent for Unseen Games</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01120) • [📄 arXiv](https://arxiv.org/abs/2611.01120) • [📥 PDF](https://arxiv.org/pdf/2611.01120)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZixianGao/StreamDuo-code)

> 🎮 Can a live AI commentator handle a game it has never seen before? We introduce StreamDuo , a two-agent framework for cross-game streaming commentary. Instead of relying solely on memorized game knowledge, a live commentator selectively queries a...

</details>

<details>
<summary><b>9. Solv3R: 3D Looped Transformer as a Multi-view Solver</b> ⭐ 102</summary>

<br/>

**👥 Authors:** Kwang Moo Yi, Yuki Ono, Sho Kagami, Andrea Tagliasacchi, jgkwak

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02857) • [📄 arXiv](https://arxiv.org/abs/2611.02857) • [📥 PDF](https://arxiv.org/pdf/2611.02857)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ubc-vision/solv3r)

> No abstract available.

</details>

<details>
<summary><b>10. Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04391) • [📄 arXiv](https://arxiv.org/abs/2611.04391) • [📥 PDF](https://arxiv.org/pdf/2611.04391)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jun-brro/h2rb-code)

> H2RB in three points Transfer human-demonstrated tasks to robots using pretrained VLAs, without target-robot demonstrations or paired human-robot trajectories. Bridge cross-embodiment perception and action gaps through hand geometry-anchored align...

</details>

<details>
<summary><b>11. VideoMemBench: How Well Do MLLMs Remember in Video Conversations?</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Mingfei Lu, Huanjin Yao, Kaituo Feng, Chao Wang, Zhengdong Hu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40131) • [📄 arXiv](https://arxiv.org/abs/2610.40131) • [📥 PDF](https://arxiv.org/pdf/2610.40131)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Oliiveralien/VideoMemBench)

> VideoMemBench evaluates in-context video memory through multi-turn video conversations with episodic and answer dependencies. The dataset, evaluation code, and leaderboard are available.

</details>

<details>
<summary><b>12. VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tianyang Hu, Tianyu Pang, Yihong Luo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06796) • [📄 arXiv](https://arxiv.org/abs/2611.06796) • [📥 PDF](https://arxiv.org/pdf/2611.06796)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Luo-Yihong/VA-TDM)

> Few-step distillation seeks to make diffusion and flow models efficient without sacrificing generation quality. While score-based distribution matching methods provide a strong foundation, accurately tracking the student's evolving distribution ac...

</details>

<details>
<summary><b>13. TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit Tokens</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01926) • [📄 arXiv](https://arxiv.org/abs/2611.01926) • [📥 PDF](https://arxiv.org/pdf/2611.01926)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Accepted to EMNLP 2026 (Main, Long) 🎉 TAC-CoT is a hybrid implicit agent that reasons in compact continuous-token blocks while still calling tools: at each step, a router decides whether to answer or call a tool, and the returned observation is fe...

</details>

<details>
<summary><b>14. MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41104) • [📄 arXiv](https://arxiv.org/abs/2610.41104) • [📥 PDF](https://arxiv.org/pdf/2610.41104)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Muon-RT is a specialized optimizer for the self-distillation family of models, in which the teacher's information is distilled into the student in an online fashion. The proposed optimizer (MUON-RT) reuses the Teacher's Trajectory and drops the Mo...

</details>

<details>
<summary><b>15. AnchorComplete: Recovering Complete Scene Meshes from Partial Point Clouds</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Andrea Vedaldi, Chuanxia Zheng, Ganlin Zhang, Weirong Chen, ismailelyamany

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03228) • [📄 arXiv](https://arxiv.org/abs/2611.03228) • [📥 PDF](https://arxiv.org/pdf/2611.03228)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: AnchorComplete turns partial point clouds into complete scene meshes, preserves observed geometry, and scales from individual rooms to large multi-room scenes through metric-scale coarse-to-fine generation. 🎥Project Page: https://wrchen530....

</details>

<details>
<summary><b>16. SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding</b> ⭐ 18</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02846) • [📄 arXiv](https://arxiv.org/abs/2611.02846) • [📥 PDF](https://arxiv.org/pdf/2611.02846)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/QwenApp/SpecOPD)

> Excited to share SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding! On-policy supervision does not have to wait for full-response rollouts. SpecOPD samples fresh draft branches at reference anchors in parallel, shares target...

</details>

<details>
<summary><b>17. VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03404) • [📄 arXiv](https://arxiv.org/abs/2611.03404) • [📥 PDF](https://arxiv.org/pdf/2611.03404)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LAW1223/VidDub)

> Video dubbing aims to synthesize lip movements that match target speech while preserving the speaker identity, head pose, and background of a source video. Existing editors are predominantly trained via self-reconstruction under original paired au...

</details>

<details>
<summary><b>18. LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05304) • [📄 arXiv](https://arxiv.org/abs/2611.05304) • [📥 PDF](https://arxiv.org/pdf/2611.05304)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mscheong01/LoopVQ)

> Looped transformers reuse the same layers across loop steps, but every loop step stores its own KV cache, so memory grows with the loop count. LoopVQ exploits the redundancy of this cache along the loop axis: it vector-quantizes channels from seve...

</details>

<details>
<summary><b>19. SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06083) • [📄 arXiv](https://arxiv.org/abs/2611.06083) • [📥 PDF](https://arxiv.org/pdf/2611.06083)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41432) • [📄 arXiv](https://arxiv.org/abs/2610.41432) • [📥 PDF](https://arxiv.org/pdf/2610.41432)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/microsoft/Hybrid-Computer-Use)

> Hi everyone, first author here 👋 Agents can write code, read the accessibility tree, and look at pixels, yet most computer-use interfaces are still built around screenshots and clicks. Hybrid Computer Use (HCU) gives agents all three channels (Cod...

</details>

<details>
<summary><b>21. PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenbo Huang, Ruiyang Si, Shulong Jiang, Jianxin Bi, Qiiiiiiiii

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06768) • [📄 arXiv](https://arxiv.org/abs/2611.06768) • [📥 PDF](https://arxiv.org/pdf/2611.06768)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce PyRUA-REAL, a framework for studying embodied recursive self-improvement through real-world robot exploration and code refinement. Coding agents retain interaction experience as persistent memory and reusable executable skills to guid...

</details>

<details>
<summary><b>22. How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40516) • [📄 arXiv](https://arxiv.org/abs/2610.40516) • [📥 PDF](https://arxiv.org/pdf/2610.40516)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/swiss-ai/msafetemp)

> We release 2M multilingual safety alignment prompts, spanning 60 languages which can be used for both training and evaluation. Using template-based approach, we achieve scalable augmentation of both harmful and benign data, which can also be cultu...

</details>

<details>
<summary><b>23. VeriSpoof: Beyond Real or Fake with One Audio LLM</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04634) • [📄 arXiv](https://arxiv.org/abs/2611.04634) • [📥 PDF](https://arxiv.org/pdf/2611.04634)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/swagshaw/verispoof)

> Hi everyone, author here 👋 VeriSpoof is an open audio LLM for unified speech deepfake forensics. Beyond real or fake , the same weights also tell you where a recording was synthesized, which system made it, whether two recordings share a source , ...

</details>

<details>
<summary><b>24. NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05648) • [📄 arXiv](https://arxiv.org/abs/2611.05648) • [📥 PDF](https://arxiv.org/pdf/2611.05648)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ChenDarYen/NitroFusion2)

> Hi, first author here. In an MMDiT, text and image tokens share every attention layer, so by mid-network the text tokens have already read the image. We use these intermediate text-token states of a frozen MMDiT as the discriminator's representati...

</details>

<details>
<summary><b>25. On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05609) • [📄 arXiv](https://arxiv.org/abs/2611.05609) • [📥 PDF](https://arxiv.org/pdf/2611.05609)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! I’m the first author of this paper. We identify a blind spot in (M)OPD for post-RL consolidation: students may not inherit their teachers’ generalization capabilities, even when they achieve near-perfect in-distribution distillation p...

</details>

<details>
<summary><b>26. GaussianRenderFormer: Transformer-based Rendering of 3D Gaussian Splats</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05593) • [📄 arXiv](https://arxiv.org/abs/2611.05593) • [📥 PDF](https://arxiv.org/pdf/2611.05593)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SVLwoof/gaussianformer)

> We present GaussianRenderFormer, a transformer that renders 3D Gaussian splats directly, with no rasterizer in the renderer. Each Gaussian becomes one token, and a decoder turns small patches of camera rays into pixels by attending to those tokens...

</details>

<details>
<summary><b>27. Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04760) • [📄 arXiv](https://arxiv.org/abs/2611.04760) • [📥 PDF](https://arxiv.org/pdf/2611.04760)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/azencot-group/KGO)

> We introduce Koopman Generative Operators (KGO) for efficient probabilistic time-series forecasting. Accepted at NeurIPS 2026. Code is available in the linked repository.

</details>

<details>
<summary><b>28. LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ilpo Viertola, Yuxuan Jiang, Kangdi Wang, Vladimir Iashin, Yusheng Dai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05988) • [📄 arXiv](https://arxiv.org/abs/2611.05988) • [📥 PDF](https://arxiv.org/pdf/2611.05988)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dalision/livefoley)

> 🔊 LiveFoley: A Plug-and-Play Sound Engine for Real-Time Interactive Worlds Streaming Video-to-Audio (V2A) is notoriously hard. We tackle two major bottlenecks in current audio generation: ⚡️The Ultra-Low Latency Challenge: Unlike turn-based AI (e....

</details>

<details>
<summary><b>29. UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Wenbo Li, Renjing Pei, Fan Li, Jingbo Lin, cszhilu1998

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06042) • [📄 arXiv](https://arxiv.org/abs/2611.06042) • [📥 PDF](https://arxiv.org/pdf/2611.06042)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mrluin/UniRestorer_plusplus)

> The proposed hierarchical model scaling strategy exhibits  approximately log-linear PSNR trends over the evaluated model-size range, with steeper fitted slopes than vanilla mixture-of-experts (MoE) scaling on out-of-distribution CDD-50 and FoundIR

</details>

<details>
<summary><b>30. Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03517) • [📄 arXiv](https://arxiv.org/abs/2611.03517) • [📥 PDF](https://arxiv.org/pdf/2611.03517)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Stop giving your coding agent more tools and start asking it better questions: that’s how KernelSeek wrote single-file CUDA kernels that beat FlashAttention-4 by 1.46x.

</details>

<details>
<summary><b>31. Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost</b> ⭐ 0</summary>

<br/>

**👥 Authors:** bonanc

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03852) • [📄 arXiv](https://arxiv.org/abs/2611.03852) • [📥 PDF](https://arxiv.org/pdf/2611.03852)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ShortReasoning In ShortReasoning , I show that rewriting a model’s earlier reasoning into compact state can shorten its newly generated reasoning without retraining. In the coding-agent case study, MiniMax M3 with external compaction cost 34% less...

</details>

<details>
<summary><b>32. DRAP: Dynamics-Risk Adaptive Plasticity for Continual Learning in Physical AI</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Oswaldo Ludwig

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05029) • [📄 arXiv](https://arxiv.org/abs/2611.05029) • [📥 PDF](https://arxiv.org/pdf/2611.05029)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/oswaldoludwig/DRAP-Dynamics-Risk-Adaptive-Plasticity)

> DRAP is a practical, physics-aware way to balance stability and plasticity for sequential adaptation of large VLA policies in robotics without storing old data.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 32 |
| 📅 Today | [`2026-11-05.json`](data/daily/2026-11-05.json) | 32 |
| 📆 This Week | [`2026-W44.json`](data/weekly/2026-W44.json) | 143 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 182 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-05 | 32 | [View JSON](data/daily/2026-11-05.json) |
| 📄 2026-11-04 | 43 | [View JSON](data/daily/2026-11-04.json) |
| 📄 2026-11-03 | 38 | [View JSON](data/daily/2026-11-03.json) |
| 📄 2026-11-02 | 30 | [View JSON](data/daily/2026-11-02.json) |
| 📄 2026-11-01 | 39 | [View JSON](data/daily/2026-11-01.json) |
| 📄 2026-10-31 | 39 | [View JSON](data/daily/2026-10-31.json) |
| 📄 2026-10-30 | 30 | [View JSON](data/daily/2026-10-30.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W44 | 143 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 182 | [View JSON](data/monthly/2026-11.json) |
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
