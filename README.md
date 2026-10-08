<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-52-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8248+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">52</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">192</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">487</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8248+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 08, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization</b> ⭐ 83</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38169) • [📄 arXiv](https://arxiv.org/abs/2609.38169) • [📥 PDF](https://arxiv.org/pdf/2609.38169)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Dreamer-Toby/STEPQuant)

> 🚀 Excited to share STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization! STEPQuant enables efficient low-bit quantization of recurrent states in linear attention by addressing quantization errors across both temporal ...

</details>

<details>
<summary><b>2. Long-WAM: Scaling the Context of World-Action Models</b> ⭐ 2.66k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10528) • [📄 arXiv](https://arxiv.org/abs/2610.10528) • [📥 PDF](https://arxiv.org/pdf/2610.10528)

**💻 Code:** [⭐ Code](https://github.com/NVlabs/LongLive) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>3. nanoMuse: An Open-Source Personal Agent for Every Device You Own</b> ⭐ 229</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08699) • [📄 arXiv](https://arxiv.org/abs/2610.08699) • [📥 PDF](https://arxiv.org/pdf/2610.08699)

**💻 Code:** [⭐ Code](https://github.com/nano-muse/nanoMuse) • [⭐ Code](https://github.com/huggingface)

> nanoMuse is an open-source (GPL-3.0) counterpart to Meta's Muse: one personal agent on the phone, the computer and the web, sharing one conversation over a relay you can self-host. It has hands on the Android phone's screen and the computer's, a S...

</details>

<details>
<summary><b>4. Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08621) • [📄 arXiv](https://arxiv.org/abs/2610.08621) • [📥 PDF](https://arxiv.org/pdf/2610.08621)

**💻 Code:** [⭐ Code](https://github.com/IMBALDY/RecursiveGameCreator) • [⭐ Code](https://github.com/huggingface)

> We introduce Recursive Game Creator , an experience-oriented agentic framework that transforms playable game prototypes into engaging games through recursive development. Inspired by real game studios, our framework brings together four collaborat...

</details>

<details>
<summary><b>5. Questioning the Questions: Sustaining Self-Evolution in Reasoning Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04299) • [📄 arXiv](https://arxiv.org/abs/2610.04299) • [📥 PDF](https://arxiv.org/pdf/2610.04299)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Self-evolving reasoning models learn from their own generated questions, yet repeated self-training can lead to performance collapse. In this paper, we investigate why performance deteriorates over successive rounds and how to sustain self-evoluti...

</details>

<details>
<summary><b>6. GRACE: Generation-aware latent compression for efficient video generation</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10524) • [📄 arXiv](https://arxiv.org/abs/2610.10524) • [📥 PDF](https://arxiv.org/pdf/2610.10524)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/cvlab-kaist/GRACE)

> This work was done while the KAIST AI authors were interns at Kakao Corp. .🦁 🎬 Project page ( with extensive qualitative results ) : https://cvlab-kaist.github.io/GRACE/ 💻  Code: https://github.com/cvlab-kaist/GRACE TL;DR: GRACE compresses the VAE...

</details>

<details>
<summary><b>7. DecepEval: A Benchmark for Evaluating Deception in LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07967) • [📄 arXiv](https://arxiv.org/abs/2610.07967) • [📥 PDF](https://arxiv.org/pdf/2610.07967)

**💻 Code:** [⭐ Code](https://github.com/functy/DECEPEVAL) • [⭐ Code](https://github.com/huggingface)

> When do LLM agents become more likely to deceive? DecepEval introduces the LLM Deception Diamond framework to examine how four external conditions, pressure, incentive, opportunity, and conflict, shape LLM agent behavior across 1,532 task pairs, 3...

</details>

<details>
<summary><b>8. VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06293) • [📄 arXiv](https://arxiv.org/abs/2610.06293) • [📥 PDF](https://arxiv.org/pdf/2610.06293)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> To address the limitations of existing MLLMs in causal reasoning for Video Event Prediction (VEP), we propose VepAgent, an agentic framework that integrates causal-transition reasoning, tool-augmented reinforcement learning, and a high-quality rea...

</details>

<details>
<summary><b>9. SGF+: Decoupling Gradient Flows for Autoregressive Video Generation</b> ⭐ 15</summary>

<br/>

**👥 Authors:** Siwen Lu, Yaowei Li, Zihan Su, Haoyuwu, JunhaoZhuang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10429) • [📄 arXiv](https://arxiv.org/abs/2610.10429) • [📥 PDF](https://arxiv.org/pdf/2610.10429)

**💻 Code:** [⭐ Code](https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus) • [⭐ Code](https://github.com/huggingface)

> Paper: https://arxiv.org/abs/2610.10429 Project: https://zihan-su.github.io/self-gradient-forcing-plus Code: https://github.com/Zihan-Su/Self_Gradient_Forcing_Plus Model: https://huggingface.co/ZihanSu/Self_Gradient_Forcing_Plus

</details>

<details>
<summary><b>10. UniWAM: Unified World-Action Model</b> ⭐ 40</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02054) • [📄 arXiv](https://arxiv.org/abs/2610.02054) • [📥 PDF](https://arxiv.org/pdf/2610.02054)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/UniWAM/UniWAM)

> We introduce UniWAM, a world–action model that unifies physical reasoning, world modeling, and action prediction within a single training framework. UniWAM is trained on over 10,000 hours of robot and human egocentric data, together with visual qu...

</details>

<details>
<summary><b>11. Semifactual Credit-Augmented Policy Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40360) • [📄 arXiv](https://arxiv.org/abs/2609.40360) • [📥 PDF](https://arxiv.org/pdf/2609.40360)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DtYXs/SCAPO)

> SCAPO perturbs the prompt, holds the sampled response fixed 🔒, and turns token-level probability instability under answer-preserving interventions into finer-grained credit for RLVR.

</details>

<details>
<summary><b>12. RunningTab: Direct Workspace Interaction with Environment-Side Tabs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10444) • [📄 arXiv](https://arxiv.org/abs/2610.10444) • [📥 PDF](https://arxiv.org/pdf/2610.10444)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Agents are now taking over some of our knowledge work, but after working through a stack of files over dozens of turns, something they saw slips out of what they deliver. To tackle this, we introduce RunningTab, where the environment keeps a runni...

</details>

<details>
<summary><b>13. Tetris3D: 3D Scene Generation With Objects That Fit Together</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10539) • [📄 arXiv](https://arxiv.org/abs/2610.10539) • [📥 PDF](https://arxiv.org/pdf/2610.10539)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/cvlab-kaist/Tetris3D)

> TL;DR: Tetris3D reconstructs 3D scenes from a single image by generating objects in physical dependency order, using their neighbors as context so that shapes and poses fit together. Project page: https://cvlab-kaist.github.io/Tetris3D Github link...

</details>

<details>
<summary><b>14. WorldSonus: Bringing Sound to Worlds</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08760) • [📄 arXiv](https://arxiv.org/abs/2610.08760) • [📥 PDF](https://arxiv.org/pdf/2610.08760)

**💻 Code:** [⭐ Code](https://github.com/NoizAI/WorldSonus) • [⭐ Code](https://github.com/huggingface)

> WorldSonus, an interactive video-to-audio framework designed for real-time spatial sound synthesis in world models

</details>

<details>
<summary><b>15. ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39306) • [📄 arXiv](https://arxiv.org/abs/2609.39306) • [📥 PDF](https://arxiv.org/pdf/2609.39306)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ShengjieJin/ReSAIL)

> Can agents keep improving by distilling from their own deployment experience? In our experiments, existing self-distillation methods can lose both deployment performance and task competence with privileged information (PI) across cycles. This matt...

</details>

<details>
<summary><b>16. RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments</b> ⭐ 0</summary>

<br/>

**👥 Authors:** tangzhy, JoeYing, ShelleyHoo, Jakumetsu, LeonOverload

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10409) • [📄 arXiv](https://arxiv.org/abs/2610.10409) • [📥 PDF](https://arxiv.org/pdf/2610.10409)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/robotworldai/robotworld)

> No abstract available.

</details>

<details>
<summary><b>17. UltraText Bench: A Comprehensive Bilingual Benchmark for Evaluating Visual Text Rendering in Image Generation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09823) • [📄 arXiv](https://arxiv.org/abs/2610.09823) • [📥 PDF](https://arxiv.org/pdf/2610.09823)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LINs-lab/UltraText_Bench)

> We introduce UltraText Bench, a bilingual benchmark for dense text rendering with 432 prompts across 24 real-world scene categories. Evaluating 24 model configurations reveals a key challenge: visually clear text can still fail to preserve the req...

</details>

<details>
<summary><b>18. Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Hongbo Zhang, Yun Luo, Jianhao Yan, Han Cui, HarryFu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03185) • [📄 arXiv](https://arxiv.org/abs/2610.03185) • [📥 PDF](https://arxiv.org/pdf/2610.03185)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HancCui/opd_hacking)

> No abstract available.

</details>

<details>
<summary><b>19. Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10114) • [📄 arXiv](https://arxiv.org/abs/2610.10114) • [📥 PDF](https://arxiv.org/pdf/2610.10114)

**💻 Code:** [⭐ Code](https://github.com/OpenMOSS/Hybrid-Mechanics) • [⭐ Code](https://github.com/huggingface)

> Hello everyone! We are happy to share our latest work, Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position . arXiv: https://arxiv.org/abs/2610.10114 GitHub: https://github.com/OpenMOSS/Hybrid-Mechanics We wou...

</details>

<details>
<summary><b>20. SWE-Game: Can Coding Agents Build the Games We Want?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ruochen Fan, Xiangyu Zou, Jin Wang, Xiaoyu Chen, WaltonFuture

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33678) • [📄 arXiv](https://arxiv.org/abs/2609.33678) • [📥 PDF](https://arxiv.org/pdf/2609.33678)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce SWE-Game, a benchmark of 247 tasks grounded in 41 executable reference Godot games spanning 13 gameplay categories in 2D and 3D.

</details>

<details>
<summary><b>21. Recurrent Looped Transformer</b> ⭐ 908</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07591) • [📄 arXiv](https://arxiv.org/abs/2610.07591) • [📥 PDF](https://arxiv.org/pdf/2610.07591)

**💻 Code:** [⭐ Code](https://github.com/yifanzhang-pro/recurrent-looped-tranformer) • [⭐ Code](https://github.com/huggingface)

> Recurrent Looped Transformer

</details>

<details>
<summary><b>22. VIEScore2: Unified Image Evaluation with Spatially Grounded Explanations</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.00994) • [📄 arXiv](https://arxiv.org/abs/2610.00994) • [📥 PDF](https://arxiv.org/pdf/2610.00994)

**💻 Code:** [⭐ Code](https://github.com/TIGER-AI-Lab/VIEScore2) • [⭐ Code](https://github.com/huggingface)

> Most image evaluators give you a single score but don't show where the image goes wrong. VIEScore2 is one model that scores generated and edited images and marks the defective regions on a 16×16 grid in a single pass. A simple rule-based parser th...

</details>

<details>
<summary><b>23. On KL-Regularized Policy Optimization</b> ⭐ 182</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08963) • [📄 arXiv](https://arxiv.org/abs/2610.08963) • [📥 PDF](https://arxiv.org/pdf/2610.08963)

**💻 Code:** [⭐ Code](https://github.com/yifanzhang-pro/KLPO) • [⭐ Code](https://github.com/huggingface)

> On KL-Regularized Policy Optimization (KLPO)

</details>

<details>
<summary><b>24. Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05034) • [📄 arXiv](https://arxiv.org/abs/2610.05034) • [📥 PDF](https://arxiv.org/pdf/2610.05034)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Budget Allocation Across Questions, Trajectories, and Reads

</details>

<details>
<summary><b>25. Inverting Multi-Vector Visual Document Indices</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yu Xiao, Yao Zhang, Ryenhails

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09920) • [📄 arXiv](https://arxiv.org/abs/2610.09920) • [📥 PDF](https://arxiv.org/pdf/2610.09920)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multi-vector visual document retrievers store each page as ~1,000 patch vectors, often in a third-party vector DB, and this index is usually treated as less sensitive than the page. We show it isn't. We frame inversion as conditional document imag...

</details>

<details>
<summary><b>26. AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10047) • [📄 arXiv](https://arxiv.org/abs/2610.10047) • [📥 PDF](https://arxiv.org/pdf/2610.10047)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation

</details>

<details>
<summary><b>27. Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05289) • [📄 arXiv](https://arxiv.org/abs/2610.05289) • [📥 PDF](https://arxiv.org/pdf/2610.05289)

**💻 Code:** [⭐ Code](https://github.com/xiaobiaodu/mobile-4dgs) • [⭐ Code](https://github.com/huggingface)

> Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable performance in novel view synthesis, yet deploying both static and dynamic Gaussian representations on resource-constrained mobile devices remains challenging due to heavy st...

</details>

<details>
<summary><b>28. NAMVIS: Next-Scale Autoregressive Multi-View Image Synthesis</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Peter Wonka, Artem Komarichev, Ilya Statsenko, Ramil Khafizov, rusrakhimov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04722) • [📄 arXiv](https://arxiv.org/abs/2610.04722) • [📥 PDF](https://arxiv.org/pdf/2610.04722)

**💻 Code:** [⭐ Code](https://github.com/corl-team/namvis) • [⭐ Code](https://github.com/huggingface)

> NAMVIS replaces diffusion with next-scale autoregression for sparse-view multi-view synthesis: target views are generated coarse-to-fine in 7 scale steps, with all tokens of a scale predicted in parallel and a multi-scale PRoPE injecting camera ge...

</details>

<details>
<summary><b>29. WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round Trips for Vision-Based Web Agents on Live Websites</b> ⭐ 0</summary>

<br/>

**👥 Authors:** jianganghan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03036) • [📄 arXiv](https://arxiv.org/abs/2610.03036) • [📥 PDF](https://arxiv.org/pdf/2610.03036)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jianganghan/WebFovea)

> Author here. WebFovea is a vision-based web agent that placed 2nd in the WebRetriever Challenge 2026 (57.0/100). It works on live websites through their own UI: screenshots in, clicks and keystrokes out. Main takeaway: on real websites, many of th...

</details>

<details>
<summary><b>30. On-Policy Distillation with Negative-Policy Rollouts</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07874) • [📄 arXiv](https://arxiv.org/abs/2610.07874) • [📥 PDF](https://arxiv.org/pdf/2610.07874)

**💻 Code:** [⭐ Code](https://github.com/naver-ai/np-opd) • [⭐ Code](https://github.com/huggingface)

> How can we help OPD effectively learn what to avoid? We introduce Negative-Policy OPD (NP-OPD), which complements teacher supervision with rollouts from a lower-performing, lower-capability negative policy. This helps suppress tokens preferred by ...

</details>

<details>
<summary><b>31. Minimal Witness Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07226) • [📄 arXiv](https://arxiv.org/abs/2610.07226) • [📥 PDF](https://arxiv.org/pdf/2610.07226)

**💻 Code:** [⭐ Code](https://github.com/TSUITUENYUE/MWRL) • [⭐ Code](https://github.com/huggingface)

> I wrote an accessible introduction to this work, with interactive figures. https://tytsui.com/blog/correct-minimal-and-all/

</details>

<details>
<summary><b>32. From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09684) • [📄 arXiv](https://arxiv.org/abs/2610.09684) • [📥 PDF](https://arxiv.org/pdf/2610.09684)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/WangXinglin/PersonTTS)

> let's discuss!

</details>

<details>
<summary><b>33. QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Divyansh Srivastava, Xiang Zhang, Xiaojun Shan, Zeyuan Chen, yuchengm

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10497) • [📄 arXiv](https://arxiv.org/abs/2610.10497) • [📥 PDF](https://arxiv.org/pdf/2610.10497)

**💻 Code:** [⭐ Code](https://github.com/myc634/QuadTok) • [⭐ Code](https://github.com/huggingface)

> Code: https://github.com/myc634/QuadTok

</details>

<details>
<summary><b>34. DLoop: Looped Speculative Decoding</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07659) • [📄 arXiv](https://arxiv.org/abs/2610.07659) • [📥 PDF](https://arxiv.org/pdf/2610.07659)

**💻 Code:** [⭐ Code](https://github.com/naver-ai/DLoop) • [⭐ Code](https://github.com/huggingface)

> DLoop performs multiple drafting stages before a single verification, guided by draft-model confidence and loop-aware training. It reduces target-model forward passes and improves wall-clock speedup by 5 to 41 percent for both autoregressive and p...

</details>

<details>
<summary><b>35. PhysEvo: Astra Can Act, Let It</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Qiang Liu, Fengwei Liu, Zeyu Zhang, Wenqing Tian, zhaocheng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08995) • [📄 arXiv](https://arxiv.org/abs/2610.08995) • [📥 PDF](https://arxiv.org/pdf/2610.08995)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>36. Internalizing Agent Experience into Diffusion Model Weights via On-Policy Context Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yang Yang, Yu Cheng, Weinan Zhang, Zekai Liu, Yummytanmo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07250) • [📄 arXiv](https://arxiv.org/abs/2610.07250) • [📥 PDF](https://arxiv.org/pdf/2610.07250)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yummytanmo/D-OPCD-CoEvolution)

> Wrapping an image generation model in an agentic harness can effectively boost Text-to-Image task performance: the harness can leverage memory, skills, workflow orchestration, result verification, and iterative refinement to continually construct ...

</details>

<details>
<summary><b>37. Learning Multimodal Embeddings with Evidence-Aligned Readout</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xinlei Wang, Junfu Pu, Fuda Ye, Zirong Chen, EnjunDu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33659) • [📄 arXiv](https://arxiv.org/abs/2609.33659) • [📥 PDF](https://arxiv.org/pdf/2609.33659)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share our work EviAlign: Learning Multimodal Embeddings with Evidence-Aligned Readout! Can the semantic structure of generated evidence guide how multimodal representations are extracted? We introduce EviAlign, a framework that jointly ...

</details>

<details>
<summary><b>38. Improving Proactive AI Assistance with Hierarchical Procedural Understanding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06505) • [📄 arXiv](https://arxiv.org/abs/2610.06505) • [📥 PDF](https://arxiv.org/pdf/2610.06505)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ProactiveCoach introduces hierarchical phase–step–action guidance data, a benchmark, and a VLM learning method for timely procedural assistance that adapts to the user’s requested level of detail.

</details>

<details>
<summary><b>39. UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Ji Zhang, Hui Xiang, Dianzhi Yu, Cheng Liu, Okiii

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10164) • [📄 arXiv](https://arxiv.org/abs/2610.10164) • [📥 PDF](https://arxiv.org/pdf/2610.10164)

**💻 Code:** [⭐ Code](https://github.com/LimOkii/UniSKill) • [⭐ Code](https://github.com/huggingface)

> UniSkill uses contrastive action feedback from existing successful and failed trajectories to train skill proposals alongside an evolving agent policy, without additional rollouts for each proposal. It reaches 98.4% success on ALFWorld and 84.7% o...

</details>

<details>
<summary><b>40. SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09832) • [📄 arXiv](https://arxiv.org/abs/2610.09832) • [📥 PDF](https://arxiv.org/pdf/2610.09832)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Memory-augmented reinforcement learning strengthens LLM agents' ability to solve complex long-horizon tasks. Skills are one such form of memory, pairing instructions with an applicability condition over task types. However, retaining every skill i...

</details>

<details>
<summary><b>41. RoboQuest: Generalist Physical Agents that Search, Inspect and Test</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10388) • [📄 arXiv](https://arxiv.org/abs/2610.10388) • [📥 PDF](https://arxiv.org/pdf/2610.10388)

**💻 Code:** [⭐ Code](https://github.com/declare-lab/RoboQuest) • [⭐ Code](https://github.com/huggingface)

> RoboQuest: A benchmark for goal-directed embodied exploration. The best frontier model, GPT-6 Astra, performs at just 23%, while Opus 5.5 achieves 13%.

</details>

<details>
<summary><b>42. A self-learning scientific agent for X-ray diffraction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07862) • [📄 arXiv](https://arxiv.org/abs/2610.07862) • [📥 PDF](https://arxiv.org/pdf/2610.07862)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DeltaGanjiang/XDecomposer)

> 🚀 Also the official website for GanJiang: https://ganjiang.asia/

</details>

<details>
<summary><b>43. SheetSage2: Coherent Lead-Sheet Transcription with Synthetic Supervision</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05336) • [📄 arXiv](https://arxiv.org/abs/2610.05336) • [📥 PDF](https://arxiv.org/pdf/2610.05336)

**💻 Code:** [⭐ Code](https://github.com/multimodal-art-projection/YuE) • [⭐ Code](https://github.com/huggingface)

> We're sharing SheetSage2, a unified framework for turning music recordings into coherent, editable lead sheets and timed musical annotations. It transcribes melody, chords, beats, downbeats, key, and structure. The framework combines scalable supe...

</details>

<details>
<summary><b>44. Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02368) • [📄 arXiv](https://arxiv.org/abs/2610.02368) • [📥 PDF](https://arxiv.org/pdf/2610.02368)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>45. CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Albert Garifullin, Nikita Gavrilov, Maksim Elistratov, Gennadiy Savrasov, zhemchuzhnikov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09127) • [📄 arXiv](https://arxiv.org/abs/2610.09127) • [📥 PDF](https://arxiv.org/pdf/2610.09127)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kulibinai/cadfather)

> CADFather is an autonomous agentic system for reconstructing editable parametric CAD models from 3D meshes. A vision-language assistant coordinates CAD generation tools and numerical optimization, using visual and geometric feedback to select and ...

</details>

<details>
<summary><b>46. Salt++: Context-Aligned Post-Training for Few-Step Streaming Multimodal Generation</b> ⭐ 20</summary>

<br/>

**👥 Authors:** Fangyu Lin, Haitao Lin, Lunjie Zhu, Yutong Wang, domiso

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36995) • [📄 arXiv](https://arxiv.org/abs/2609.36995) • [📥 PDF](https://arxiv.org/pdf/2609.36995)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XingtongGe/Saltpp)

> Few-step streaming audio–video generation requires both causal modeling and step distillation. Teacher forcing pairs clean history with a noisy target, but shapes predictive contextual representations only indirectly through velocity prediction. M...

</details>

<details>
<summary><b>47. StepCAD: Mesh-to-CAD Code Generation via LLM Policy and Geometry-Guided Search</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03799) • [📄 arXiv](https://arxiv.org/abs/2610.03799) • [📥 PDF](https://arxiv.org/pdf/2610.03799)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ghadinehme/StepCAD)

> No abstract available.

</details>

<details>
<summary><b>48. EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10533) • [📄 arXiv](https://arxiv.org/abs/2610.10533) • [📥 PDF](https://arxiv.org/pdf/2610.10533)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ModalityDance/EngramEdit)

> No abstract available.

</details>

<details>
<summary><b>49. Co-Evolving Robot Orchestrators and Policies through Deployment</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09228) • [📄 arXiv](https://arxiv.org/abs/2610.09228) • [📥 PDF](https://arxiv.org/pdf/2610.09228)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Co-Evolving Robot Orchestrators and Policies through Deployment

</details>

<details>
<summary><b>50. TIDES: Implicit Time-Awareness in Selective State Space Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09742) • [📄 arXiv](https://arxiv.org/abs/2605.09742) • [📥 PDF](https://arxiv.org/pdf/2605.09742)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TaylanSoydan/TIDES)

> TL;DR: Mamba makes the step size Δ a learned function of the input, so it no longer equals the real time gap between observations. TIDES moves the input dependence onto the state matrix (Λ, B, C) instead and keeps Δ as the physical time gap: selec...

</details>

<details>
<summary><b>51. FastOPD: On-Policy Distillation for Lightweight VLA Deployment</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02832) • [📄 arXiv](https://arxiv.org/abs/2610.02832) • [📥 PDF](https://arxiv.org/pdf/2610.02832)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR FastOPD distills large foundation policies (>3B) into a compact, few-step student (451M) using teacher supervision at only a single on-policy state per trajectory, enabling efficient training and deployment across foundation VLAs and a World...

</details>

<details>
<summary><b>52. Task-Sufficient Contraction: Source Selection for Machine Information Interfaces</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08884) • [📄 arXiv](https://arxiv.org/abs/2610.08884) • [📥 PDF](https://arxiv.org/pdf/2610.08884)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What information must a machine retain for a declared task? For a fixed action set and loss, this paper identifies a reduced source that preserves every action’s regret. With finitely many actions, the reduction preserves the entire one-step rate-...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 52 |
| 📅 Today | [`2026-10-08.json`](data/daily/2026-10-08.json) | 52 |
| 📆 This Week | [`2026-W40.json`](data/weekly/2026-W40.json) | 192 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 487 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-08 | 52 | [View JSON](data/daily/2026-10-08.json) |
| 📄 2026-10-07 | 51 | [View JSON](data/daily/2026-10-07.json) |
| 📄 2026-10-06 | 48 | [View JSON](data/daily/2026-10-06.json) |
| 📄 2026-10-05 | 41 | [View JSON](data/daily/2026-10-05.json) |
| 📄 2026-10-04 | 84 | [View JSON](data/daily/2026-10-04.json) |
| 📄 2026-10-03 | 84 | [View JSON](data/daily/2026-10-03.json) |
| 📄 2026-10-02 | 66 | [View JSON](data/daily/2026-10-02.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W40 | 192 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 487 | [View JSON](data/monthly/2026-10.json) |
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
