<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-60-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-10212+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">60</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">80</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">811</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">10212+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 24, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29897) • [📄 arXiv](https://arxiv.org/abs/2611.29897) • [📥 PDF](https://arxiv.org/pdf/2611.29897)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGeeksGroup/MotionMamba2.0)

> 🚀 We’re excited to release Motion Mamba 2.0 , bringing autoregressive diffusion and Mamba together for long-horizon humanoid control! 🤖 Our code, models, and training data are all fully open source! 🔓 Explore the demos, try it out, and build on ou...

</details>

<details>
<summary><b>2. Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31201) • [📄 arXiv](https://arxiv.org/abs/2611.31201) • [📥 PDF](https://arxiv.org/pdf/2611.31201)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DravenALG/Embo-Harness)

> Hi everyone, author here 👋 In Embo-Harness, we study how to use frontier models to control robots well and why frontier models can work well in robotics.

</details>

<details>
<summary><b>3. WorldLeague: Benchmarking Physical Agency</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30989) • [📄 arXiv](https://arxiv.org/abs/2611.30989) • [📥 PDF](https://arxiv.org/pdf/2611.30989)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/xyangzhou/WorldLeague)

> WorldLeague benchmarks AI systems’ ability to autonomously achieve long-horizen physical goals across 60 simulated robot tasks spanning exploration, object rearrangement, and adaptation to changing environments. It evaluates VLMs, VLAs, and WAMs u...

</details>

<details>
<summary><b>4. 3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets</b> ⭐ 1.35k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30013) • [📄 arXiv](https://arxiv.org/abs/2611.30013) • [📥 PDF](https://arxiv.org/pdf/2611.30013)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenDCAI/GameFactory-3A)

> Our 3AGameFactory-motion leverages the capabilities of large models to support motion generation for a wide variety of 3D assets.

</details>

<details>
<summary><b>5. WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce</b> ⭐ 22</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30662) • [📄 arXiv](https://arxiv.org/abs/2611.30662) • [📥 PDF](https://arxiv.org/pdf/2611.30662)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent/WeMM-Ecom)

> WeMM-Ecom is a family of models developed by WeChat Vision, Tencent. It combines fine-grained e-commerce understanding with broad visual-language and reasoning capabilities and supports hybrid thinking. The WeMM-Ecom family delivers leading e-comm...

</details>

<details>
<summary><b>6. Let the Fixer Decide: Training a Code Localizer from the Fixer's Likelihood</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12164) • [📄 arXiv](https://arxiv.org/abs/2611.12164) • [📥 PDF](https://arxiv.org/pdf/2611.12164)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/misraj-ai/locfix)

> Code localizers are usually trained to predict the files a reference patch edits, but the code a fixer needs to read is not the same as the code it changes. We propose Fixer-Guided Localization (FGL): the localizer proposes several localizations, ...

</details>

<details>
<summary><b>7. A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29338) • [📄 arXiv](https://arxiv.org/abs/2611.29338) • [📥 PDF](https://arxiv.org/pdf/2611.29338)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The paper introduces nanoAstra-9B, a framework that directly trains vision-language models (VLMs) as foundation models for robotic manipulation, which achieves a 17.8% zero-shot success rate, compared with 1.4% for π0.5 and 0.2% for DreamZero. Str...

</details>

<details>
<summary><b>8. ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.26389) • [📄 arXiv](https://arxiv.org/abs/2611.26389) • [📥 PDF](https://arxiv.org/pdf/2611.26389)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Kevin-thu/ViDecide)

> We release ViDecide: Teaching video diffusion models to reason and plan step by step , which explores whether video diffusion models can reason and plan step by step, like the way language models do. Current video models often break physical or lo...

</details>

<details>
<summary><b>9. AutoPILOT: A Visual Agent Harness for Real-Time Gameplay</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28202) • [📄 arXiv](https://arxiv.org/abs/2611.28202) • [📥 PDF](https://arxiv.org/pdf/2611.28202)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper identifies a largely overlooked bottleneck in real-time visual agents: conventional harnesses execute only one action per model call, forcing agents to act slowly on stale observations. AutoPILOT allows models to delegate execution to o...

</details>

<details>
<summary><b>10. Plan4D: Generative Plannable 4D Worlds</b> ⭐ 21</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.26516) • [📄 arXiv](https://arxiv.org/abs/2611.26516) • [📥 PDF](https://arxiv.org/pdf/2611.26516)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AMAP-ML/plan4d)

> Plan4D: Generative Plannable 4D Worlds

</details>

<details>
<summary><b>11. World Models as Native Latent Action Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30898) • [📄 arXiv](https://arxiv.org/abs/2611.30898) • [📥 PDF](https://arxiv.org/pdf/2611.30898)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: The world model is the latent action model. A single pretrained video DiT reads compact latent actions from any video, brings motion back to life from them, and turns them into the foundation for pretraining a strong VLA. 🌐 Project page: ht...

</details>

<details>
<summary><b>12. RUIBench: What Makes a Good Robot-Use Interface?</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31115) • [📄 arXiv](https://arxiv.org/abs/2611.31115) • [📥 PDF](https://arxiv.org/pdf/2611.31115)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/showlab/RUIBench)

> No abstract available.

</details>

<details>
<summary><b>13. ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30597) • [📄 arXiv](https://arxiv.org/abs/2611.30597) • [📥 PDF](https://arxiv.org/pdf/2611.30597)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We propose ViDiHand2, a geometry-driven framework that reformulates VDM-based hand depth estimation from direct regression into fine-grained geometric constraint solving.

</details>

<details>
<summary><b>14. Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.27376) • [📄 arXiv](https://arxiv.org/abs/2611.27376) • [📥 PDF](https://arxiv.org/pdf/2611.27376)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/UCSB-AI/CSPD)

> Code: https://github.com/UCSB-AI/CSPD

</details>

<details>
<summary><b>15. Distilling Visual Agents from Limited Interaction Experience</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28618) • [📄 arXiv](https://arxiv.org/abs/2611.28618) • [📥 PDF](https://arxiv.org/pdf/2611.28618)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/elated-sawyer/visual-agent-distillation)

> We study how much interaction experience is needed to distill capable visual agents. With just four selected trajectories per environment , offline OPD improves a Qwen3.5-4B student from 49.17% to 82.08% on Navigation and 60.16% to 85.55% on Sokob...

</details>

<details>
<summary><b>16. DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.25419) • [📄 arXiv](https://arxiv.org/abs/2611.25419) • [📥 PDF](https://arxiv.org/pdf/2611.25419)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DiLE unifies task-guided latent-space learning, shared–private adaptation, and dynamically refreshed hard-negative distillation to preserve essential semantics and sharpen fine-grained discrimination, achieving state-of-the-art performance on MMEB...

</details>

<details>
<summary><b>17. Open Vision Banana: An Open Framework for Unified Visual Perception through Generation in RGB Space</b> ⭐ 22</summary>

<br/>

**👥 Authors:** Ming Ma, Zixiang Wang, Haoran Xu, Ruilin Yao, Xu Lin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28489) • [📄 arXiv](https://arxiv.org/abs/2611.28489) • [📥 PDF](https://arxiv.org/pdf/2611.28489)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/isLinXu/open-vision-banana)

> Vision Banana showed that a closed image generator, instruction-tuned to paint perception outputs as RGB images, becomes a generalist vision model. Does this carry over to \emph{open} generators, and if not, what fails? We answer with \textbf{Open...

</details>

<details>
<summary><b>18. Polytropos: What Do Vision-Language Model Descriptions Make of a Cultural Object?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mohsinul Kabir, Yuyan Wang, Enze Zhang, Yuechen Jiang, ChenyingLin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29355) • [📄 arXiv](https://arxiv.org/abs/2611.29355) • [📥 PDF](https://arxiv.org/pdf/2611.29355)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Polytropos evaluates what vision-language model descriptions preserve about individual cultural objects by reconstructing images from those descriptions and comparing them with the original museum photographs. The benchmark covers 374 objects from...

</details>

<details>
<summary><b>19. UUBench: Understanding the Unspoken toward Full-Duplex Multimodal Interaction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haocong He, Bin Ren, Chenfei Liao, Ye Pan, Lihanqian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30157) • [📄 arXiv](https://arxiv.org/abs/2611.30157) • [📥 PDF](https://arxiv.org/pdf/2611.30157)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We’re excited to share a preview of UUBench! 🤗 A hesitation, a raised eyebrow, or a change in tone can shift what someone means. We built UUBench to evaluate how well avatars pick up on those cues and respond appropriately. This is still a work in...

</details>

<details>
<summary><b>20. DexDuet: Learning Contact-Preserving Bimanual Dexterity from Human Demonstrations</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30495) • [📄 arXiv](https://arxiv.org/abs/2611.30495) • [📥 PDF](https://arxiv.org/pdf/2611.30495)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HaoranZhangumich/DexDuet)

> No abstract available.

</details>

<details>
<summary><b>21. GameAnything: From Any Inspirations to Playable Game Worlds</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29238) • [📄 arXiv](https://arxiv.org/abs/2611.29238) • [📥 PDF](https://arxiv.org/pdf/2611.24154)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AetherLabsAI/GameAnything)

> GameAnything: From Any Inspirations to Playable Game Worlds AI-driven game development holds the potential to transform diverse human inspirations into interactive experiences. However, existing systems and benchmarks primarily focus on explicit d...

</details>

<details>
<summary><b>22. WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming</b> ⭐ 33</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.25476) • [📄 arXiv](https://arxiv.org/abs/2611.25476) • [📥 PDF](https://arxiv.org/pdf/2611.25476)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Gen-Verse/WeightCode)

> Code: https://github.com/Gen-Verse/WeightCode

</details>

<details>
<summary><b>23. What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30207) • [📄 arXiv](https://arxiv.org/abs/2611.30207) • [📥 PDF](https://arxiv.org/pdf/2611.30207)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Arist12/SWE-Gym-Verified)

> 74% of the SWE-Gym tasks a 9B model never solves have tests that reject correct fixes. Fixing these reward labels gives +2.4 / +2.7 on SWE-bench Verified / Pro at equal data size. We release SWE-Gym-Verified: 1,087 audited tasks + the audit pipeli...

</details>

<details>
<summary><b>24. HIVE-Bench: Evaluating Patch-Level Visual Representations for Egocentric Robot Manipulation</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Yiming Wang, Yikeng Chen, Minghao Lai, Zhengtu Liang, Qiwei Liang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30813) • [📄 arXiv](https://arxiv.org/abs/2611.30813) • [📥 PDF](https://arxiv.org/pdf/2611.30813)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/KolaKivy/HIVE-Bench)

> Pretrained vision is a common start for robot learning, but most comparisons still score one pooled vector from a third-person image. Bimanual policies instead read dense patch tokens from cameras on the robot. We introduce HIVE-Bench: one shared ...

</details>

<details>
<summary><b>25. Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28833) • [📄 arXiv](https://arxiv.org/abs/2611.28833) • [📥 PDF](https://arxiv.org/pdf/2611.28833)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can a language model improve itself by editing its own weights? We explore this with a 0.8B model, achieving substantial gains on GSM8K (11.8% → 62.2%) and MATH500 (7.0% → 32.2%), while finding that the model often fails to understand what its edi...

</details>

<details>
<summary><b>26. Can Latent Reasoning Drive LLM Outputs Without a Trace?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31015) • [📄 arXiv](https://arxiv.org/abs/2611.31015) • [📥 PDF](https://arxiv.org/pdf/2611.31015)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can an LLM pursue a complex hidden objective by reasoning only in its hidden states, with no trace in its output? We show that it can. Deeper latent reasoning. We train with a linear "step predictor" that reads each intermediate step from the hidd...

</details>

<details>
<summary><b>27. SynthDCB: World Distillation for Scalable Device Control Benchmarking</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18639) • [📄 arXiv](https://arxiv.org/abs/2611.18639) • [📥 PDF](https://arxiv.org/pdf/2611.18639)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/X-LANCE/SynthDCB)

> We have release the complete dataset and code this week! Try SynthDCB and share your feedback! 🤗

</details>

<details>
<summary><b>28. Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.27689) • [📄 arXiv](https://arxiv.org/abs/2611.27689) • [📥 PDF](https://arxiv.org/pdf/2611.27689)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can a robot improve across attempts while its model parameters stay frozen? In Embodied-Harness , we explore recursive self-improvement (RSI) for robotic manipulation. The Actor follows operational guidance to carry out a task. After a failed atte...

</details>

<details>
<summary><b>29. GameDojo: Benchmarking Real-Time Interactive Agents in Video Games</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30771) • [📄 arXiv](https://arxiv.org/abs/2611.30771) • [📥 PDF](https://arxiv.org/pdf/2611.30771)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/THUSI-Lab/GameDojo)

> No abstract available.

</details>

<details>
<summary><b>30. A Pipeline-Parallel System for Depth-Recurrent Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30581) • [📄 arXiv](https://arxiv.org/abs/2611.30581) • [📥 PDF](https://arxiv.org/pdf/2611.30581)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Depth-recurrent (Looped) models raise effective depth by applying a shared stack of blocks several times. Scaling them usually requires pipeline parallelism, but commonly used interleaved 1F1B is drawn for an acyclic stage graph in which each micr...

</details>

<details>
<summary><b>31. MomentMem: Memorizing Key Moments for Robot Manipulation</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.26745) • [📄 arXiv](https://arxiv.org/abs/2611.26745) • [📥 PDF](https://arxiv.org/pdf/2611.26745)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PKU-VaLuE-Lab/MomentMem)

> 🤔 After picking up a block, can a robot still remember where it was originally placed? Is robot memory only about tracking task progress? Excited to share our recent work MomentMem: Memorizing Key Moments for Robot Manipulation ! ✨ Our goal is to ...

</details>

<details>
<summary><b>32. Distill the Correction, Not the Rewrite: Hindsight Twins for Self-Improving Text-to-Image Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31048) • [📄 arXiv](https://arxiv.org/abs/2611.31048) • [📥 PDF](https://arxiv.org/pdf/2611.31048)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Distill the Correction, Not the Rewrite: Hindsight Twins for Self-Improving Text-to-Image Models

</details>

<details>
<summary><b>33. ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents</b> ⭐ 579</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31198) • [📄 arXiv](https://arxiv.org/abs/2611.31198) • [📥 PDF](https://arxiv.org/pdf/2611.31198)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/uclanlp/OpenVLHarness)

> ToolSmith is an automatic framework to generate and compose existing tools for visual tool-use agents to better handle out-of-domain tasks.

</details>

<details>
<summary><b>34. Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Junkai Chen, Manni Cui, Zhihao Chen, Tianyi Wang, ZiAnwang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30573) • [📄 arXiv](https://arxiv.org/abs/2611.30573) • [📥 PDF](https://arxiv.org/pdf/2611.30573)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>35. Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the Edge</b> ⭐ 23</summary>

<br/>

**👥 Authors:** Christos Chatzigeorgiou, Amalia Contiero Syropoulou, Lazaros Toumanidis, Panagiotis Kasnesis

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29619) • [📄 arXiv](https://arxiv.org/abs/2611.29619) • [📥 PDF](https://arxiv.org/pdf/2611.29619)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/waldiez/wactorz/) • [⭐ Code](https://github.com/waldiez/wactorz)

> Most LLM agent frameworks run a task and exit. Wactorz is an open-source runtime in which LLM-written agents are long-lived, supervised actors: a planner turns a chat request into Python and compiles it into a new actor at runtime, and a superviso...

</details>

<details>
<summary><b>36. NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shuyang Xiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29006) • [📄 arXiv](https://arxiv.org/abs/2611.29006) • [📥 PDF](https://arxiv.org/pdf/2611.29006)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The decay exponent α in KV-cache eviction is an intrinsic property of the model: calibrated once on a single corpus, it transfers directly across domains. Attention-based accumulation (H2O) and recency-based sliding windows (StreamingLLM) are two ...

</details>

<details>
<summary><b>37. Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28227) • [📄 arXiv](https://arxiv.org/abs/2611.28227) • [📥 PDF](https://arxiv.org/pdf/2611.28227)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ifm-ai/LoRM)

> Code: https://github.com/ifm-ai/LoRM

</details>

<details>
<summary><b>38. Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models</b> ⭐ 20</summary>

<br/>

**👥 Authors:** Changti Wu, Haishan Liu, Shijie Lian, Bin Yu, Sofilyzia

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.25927) • [📄 arXiv](https://arxiv.org/abs/2611.25927) • [📥 PDF](https://arxiv.org/pdf/2611.25927)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DeepCybo-PhysAI/Fast-JEPA)

> 🎉 Introducing Fast-JEPA: fast visual-goal planning with latent world models! Fast-JEPA combines goal-directed action proposals with direct predictions of complete candidate outcomes, avoiding recursive state rollout during search refinement. 🚀 Acr...

</details>

<details>
<summary><b>39. SAVIOR: Sample-efficient Adaptation of Vision-Language Models for OCR Representation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.27319) • [📄 arXiv](https://arxiv.org/abs/2611.27319) • [📥 PDF](https://arxiv.org/pdf/2611.27319)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Author here (Hyperbots). OCR and vision-language models do well on standard benchmarks but break on patterns common in finance documents: rotated and vertical text, vendor names inside logos, fine print, degraded scans and dense multi-column pages...

</details>

<details>
<summary><b>40. Innata-0: A Native Embodied World System with Model-Agent Co-Design</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30254) • [📄 arXiv](https://arxiv.org/abs/2611.30254) • [📥 PDF](https://arxiv.org/pdf/2611.30254)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The physical world is open-ended, dynamic, and partially observable. While foundation models have advanced embodied intelligence, standalone models struggle with long-horizon execution, and simply integrating models with agents may lead to inconsi...

</details>

<details>
<summary><b>41. WorldLatent: A Unified 4D Latent Space for World Perception and Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31209) • [📄 arXiv](https://arxiv.org/abs/2611.31209) • [📥 PDF](https://arxiv.org/pdf/2611.31209)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A Unified 4D Latent Space to unify World Perception and Generation and serve as  a scalable foundation for general-purpose 4D spatial intelligence

</details>

<details>
<summary><b>42. LLMs Memorize Their Own Hallucinations During Post-Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.26863) • [📄 arXiv](https://arxiv.org/abs/2611.26863) • [📥 PDF](https://arxiv.org/pdf/2611.26863)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Reasoning-centric post-training recipes (outcome-based RL rewards) are now applied well beyond math and code. We show that on knowledge tasks, these recipes cause models to memorize the hallucinations they generate in their own reasoning chains. B...

</details>

<details>
<summary><b>43. ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Chang Zhou, Keru Zhou, Zihao Zhu, Wencan Jiang, Yicheng Xu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31053) • [📄 arXiv](https://arxiv.org/abs/2611.31053) • [📥 PDF](https://arxiv.org/pdf/2611.31053)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/xuyicheng-zju/ReWeave)

> ReWeave co-evolves an emergent physical task topology and agent harness (C, W, L) with frozen policy weights—re-reading failed trials (89% recoverable progress on RoboDojo), distilling reusable causal units across tasks, and scaling directly with ...

</details>

<details>
<summary><b>44. WeaveVLA: 3D Relational Grounding for Vision-Language-Action Models</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31126) • [📄 arXiv](https://arxiv.org/abs/2611.31126) • [📥 PDF](https://arxiv.org/pdf/2611.31126)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Kingzein/WeaveVLA)

> WeaveVLA: Enhancing Robotic Spatial Intelligence through 3D Relational Grounding Recent advances in Vision-Language-Action (VLA) models have accelerated the development of embodied intelligence. Despite their growing 3D spatial awareness, existing...

</details>

<details>
<summary><b>45. MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Pan Wang, Xiyuan Yang, Jinxi He, Jianshu Zhang, CeZhang1203

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30011) • [📄 arXiv](https://arxiv.org/abs/2611.30011) • [📥 PDF](https://arxiv.org/pdf/2611.30011)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 📡 MORSE is a streaming video memory that reads papers to fix its own failures: when a frozen video-language model keeps failing the same way, an LLM editor 🔍 searches papers, model cards and code for a fix, 🛠️ rewrites how memory stores and retrie...

</details>

<details>
<summary><b>46. Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13730) • [📄 arXiv](https://arxiv.org/abs/2611.13730) • [📥 PDF](https://arxiv.org/pdf/2611.13730)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/pelloran-inc/tritify)

> We present tritify, an open-source runtime that runs the forward pass of real models — decoder-only LLMs, MoE decoders, and the SAM 2.1 image/video stack — entirely in exact integer arithmetic, with floating point confined to offline quantization....

</details>

<details>
<summary><b>47. Prism: Hierarchical Text Detection with Minimalist Design</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.26254) • [📄 arXiv](https://arxiv.org/abs/2611.26254) • [📥 PDF](https://arxiv.org/pdf/2611.26254)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Prism, a minimalist framework for hierarchical text detection. Prism performs multi-granularity detection by attaching parallel lightweight heads to a single-scale backbone feature map, covering words, text lines, and paragraphs, and reconstructs ...

</details>

<details>
<summary><b>48. Typhoon OCR 2: From Thai Document Transcription to Multilingual, Multi-Task OCR</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.27494) • [📄 arXiv](https://arxiv.org/abs/2611.27494) • [📥 PDF](https://arxiv.org/pdf/2611.27494)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/srn-source/typhoon-ocr2)

> Open 2B/0.8B Thai–English-Chinese document parser and extractor. Open model on Thai MDPBench (80.7) and ThaiOCRBench (59.9), near its base on English benchmarks; GRPO cuts repetition loops from 3.2% to 0.7%. Weights, pip package and eval code rele...

</details>

<details>
<summary><b>49. How Complete Must an Environment Be to Train a Capable GUI Agent?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23946) • [📄 arXiv](https://arxiv.org/abs/2611.23946) • [📥 PDF](https://arxiv.org/pdf/2611.23946)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Hydr0pon1c/Mobilegym-lite)

> Graphical user interface (GUI) agents are widely trained in executable GUI environments. To lower cost, build environments in batches, and reduce manual effort, each work trades away part of the environment through its construction choices. We des...

</details>

<details>
<summary><b>50. Beyond Attention Maps: Understanding and Improving Medical MLLMs via Visual Values</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29361) • [📄 arXiv](https://arxiv.org/abs/2611.29361) • [📥 PDF](https://arxiv.org/pdf/2611.29361)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Are We Overlooking the V in MLLMs Attention? Most existing studies on MLLMs focus on improving spatial attention — teaching models where to look. But does looking at the right region necessarily lead to a correct answer? In our recent work, Beyond...

</details>

<details>
<summary><b>51. KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29590) • [📄 arXiv](https://arxiv.org/abs/2611.29590) • [📥 PDF](https://arxiv.org/pdf/2611.29590)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/cmu-l3/kernel-shift)

> KernelShift is a benchmarking pipeline and a set of environments for evaluating coding agents in kernel optimization across evolving CPU architectures (Arm Neon, SVE, SVE2 and SME2). Its agent-assisted, human-verified pipeline turns code repositor...

</details>

<details>
<summary><b>52. Single-Transformer Latent Diffusion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29064) • [📄 arXiv](https://arxiv.org/abs/2611.29064) • [📥 PDF](https://arxiv.org/pdf/2611.29064)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/haoyuhsu/Unified-LDM)

> One diffusion transformer that encodes, generates, and decodes — all backbone weights shared, modes separated only by a mode token and the timestep. Single-stage training, no DINO features, no GAN loss, no pretrained VAE. 2.08 gFID on ImageNet-1K ...

</details>

<details>
<summary><b>53. ApexID: Hierarchical Learning for Multi-Species Animal Re-Identification</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29723) • [📄 arXiv](https://arxiv.org/abs/2611.29723) • [📥 PDF](https://arxiv.org/pdf/2611.29723)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MIA-AI-Team/ApexID-Hierarchical-Learning-for-Multi-Species-Animal-Re-Identification-Official-Repo)

> ApexID explores animal re-identification through hierarchical identity and animal-category supervision, combining fine-grained identity discrimination with balanced category-level learning to improve recognition across diverse animal datasets

</details>

<details>
<summary><b>54. From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zijing Hu, Xinpeng Dong, Ziyu Zhao, Nuanqiao Shan, Kairong Han

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30627) • [📄 arXiv](https://arxiv.org/abs/2611.30627) • [📥 PDF](https://arxiv.org/pdf/2611.30627)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning

</details>

<details>
<summary><b>55. MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kehui Tan, Zhongjing Du, Yunfei Li, Changwei Lv, Yuxuan Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30287) • [📄 arXiv](https://arxiv.org/abs/2611.30287) • [📥 PDF](https://arxiv.org/pdf/2611.30287)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ChenYX24/MMMem)

> We’re sharing MMMem, a multimodal memory framework that helps agents learn from completed tasks. MMMem turns past answers into reusable experiences, links them back to the original evidence, and retrieves them when they can help with a new questio...

</details>

<details>
<summary><b>56. Seeing Right, Writing Wrong: Where Short Chain-of-Thought Breaks Spatial VQA</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28665) • [📄 arXiv](https://arxiv.org/abs/2611.28665) • [📥 PDF](https://arxiv.org/pdf/2611.28665)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MING-ZCH/seeing-right-writing-wrong)

> Shows that short chain-of-thought turns spatial VQA from a perception problem into a transcription problem: once a VLM writes a spatial relation, its answer follows that sentence rather than the image, across 15 open VLMs and 6 frontier closed mod...

</details>

<details>
<summary><b>57. SWEEP-Bench: Do Embodied Policies Act on the Speed They See?</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30637) • [📄 arXiv](https://arxiv.org/abs/2611.30637) • [📥 PDF](https://arxiv.org/pdf/2611.30637)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Damin3927/SWEEP-Bench)

> We introduced SWEEP-Bench, a benchmark of 80 conveyor tasks at 13 belt speeds. Many fine-tuned policies tend to produce actions suited to the average demonstration speed, and our results suggest that past frames widen the speed range only for thos...

</details>

<details>
<summary><b>58. Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Bryan Chu, Alex Trevithick, Riccardo de Lutio, Jiahui Huang, Chen Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31239) • [📄 arXiv](https://arxiv.org/abs/2611.31239) • [📥 PDF](https://arxiv.org/pdf/2611.31239)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Generating 3D worlds with agent planned layout.

</details>

<details>
<summary><b>59. The norm axiom and factor hyperfields</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Alessandro Linzi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29473) • [📄 arXiv](https://arxiv.org/abs/2611.29473) • [📥 PDF](https://arxiv.org/pdf/2611.29473)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/linzialessandro/norm-axiom-factor-hyperfields)

> We show that the norm axiom forces every factor valued hyperfield to come from a valuation, settle the case of value group Z, and give counterexamples without the norm axiom.

</details>

<details>
<summary><b>60. UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.26103) • [📄 arXiv](https://arxiv.org/abs/2611.26103) • [📥 PDF](https://arxiv.org/pdf/2611.26103)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Welcome

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 60 |
| 📅 Today | [`2026-11-24.json`](data/daily/2026-11-24.json) | 60 |
| 📆 This Week | [`2026-W47.json`](data/weekly/2026-W47.json) | 80 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 811 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-24 | 60 | [View JSON](data/daily/2026-11-24.json) |
| 📄 2026-11-23 | 20 | [View JSON](data/daily/2026-11-23.json) |
| 📄 2026-11-22 | 50 | [View JSON](data/daily/2026-11-22.json) |
| 📄 2026-11-21 | 50 | [View JSON](data/daily/2026-11-21.json) |
| 📄 2026-11-20 | 39 | [View JSON](data/daily/2026-11-20.json) |
| 📄 2026-11-19 | 43 | [View JSON](data/daily/2026-11-19.json) |
| 📄 2026-11-18 | 30 | [View JSON](data/daily/2026-11-18.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W47 | 80 | [View JSON](data/weekly/2026-W47.json) |
| 📅 2026-W46 | 268 | [View JSON](data/weekly/2026-W46.json) |
| 📅 2026-W45 | 193 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 811 | [View JSON](data/monthly/2026-11.json) |
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
