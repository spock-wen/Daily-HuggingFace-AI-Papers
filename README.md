<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-47-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8494+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">47</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">47</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">733</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8494+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 12, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. S-Space: Exploring Spatial Workspace in Multimodal Language Models</b> ⭐ 244</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13527) • [📄 arXiv](https://arxiv.org/abs/2610.13527) • [📥 PDF](https://arxiv.org/pdf/2610.13527)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mirros-lab/s-space)

> What does it mean for an AI to understand space? 🌌 Not just to recognize what is in front of it, but to build an internal world: where things are, how they relate, and how that world changes when the viewpoint changes. We found evidence that multi...

</details>

<details>
<summary><b>2. DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12572) • [📄 arXiv](https://arxiv.org/abs/2610.12572) • [📥 PDF](https://arxiv.org/pdf/2610.12572)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/vanzll/DiffusionART)

> An efficient, stable and scalable diffusion RL algorithm, achieving 12× fewer GPU hours than DiffusionNFT and Flow-GRPO-Fast in video generation.

</details>

<details>
<summary><b>3. Reflex: Visually Grounded Reactive Humanoid Control</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12772) • [📄 arXiv](https://arxiv.org/abs/2610.12772) • [📥 PDF](https://arxiv.org/pdf/2610.12772)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ToberJ/reflex)

> Humans effortlessly react to the world; they adeptly return a tennis shot, catch a falling cup, step aside from a passing cart, or pass a box tossed during truck unloading. These everyday actions require anticipating a moving target and reflexivel...

</details>

<details>
<summary><b>4. SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12611) • [📄 arXiv](https://arxiv.org/abs/2610.12611) • [📥 PDF](https://arxiv.org/pdf/2610.12611)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MrKiing-Jin/SoftwareGym)

> SoftwareGym is an environment synthesis pipeline for computer-use agents (CUAs). It constructs interactive environments by synthesizing runnable software applications with diverse interfaces and executable functionality, and validates them through...

</details>

<details>
<summary><b>5. EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13021) • [📄 arXiv](https://arxiv.org/abs/2609.36012) • [📥 PDF](https://arxiv.org/pdf/2610.13021)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PKU-VaLuE-Lab/EmbodiedCLBench)

> Thank you for sharing EmbodiedCLBench—the separation between experience acquisition on basic tasks and reuse on unseen compositions, including the limits of gains from additional experience, is valuable for our survey's evaluation discussion, and ...

</details>

<details>
<summary><b>6. VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs</b> ⭐ 40</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07987) • [📄 arXiv](https://arxiv.org/abs/2610.07987) • [📥 PDF](https://arxiv.org/pdf/2610.07987)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/FFY0/VisionWeave)

> We're excited to share our latest work, VisionWeave! As multimodal models move toward long-horizon interaction with both digital and real-world environments, visual token efficiency has become a critical bottleneck for practical deployment. We arg...

</details>

<details>
<summary><b>7. Here the World in Stereo: Learning Dynamic Spatial Correspondence for Immersive Joint Video-Audio Generation</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Zheyu Zhang, Tianxiao Chen, Chengcheng Liu, Hanmo Chen, ptjiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38748) • [📄 arXiv](https://arxiv.org/abs/2609.38748) • [📥 PDF](https://arxiv.org/pdf/2609.38748)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/vivoCameraResearch/StereoBind)

> Recent joint video-audio generation models have achieved strong semantic correspondence and temporal synchronization. However, applications such as AR/VR and interactive gaming further require stereo audio to provide an immersive sense, which rema...

</details>

<details>
<summary><b>8. ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13395) • [📄 arXiv](https://arxiv.org/abs/2610.13395) • [📥 PDF](https://arxiv.org/pdf/2610.13395)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Acm1011/ProgramGym)

> No abstract available.

</details>

<details>
<summary><b>9. Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12984) • [📄 arXiv](https://arxiv.org/abs/2610.12984) • [📥 PDF](https://arxiv.org/pdf/2610.12984)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/china-qijizhifeng/Work2Skill)

> We’re sharing Work2Skill, a framework that turns human desktop demonstrations into reusable skills for computer-use agents. Our work brings together three components: WorkRecorder captures synchronized screen recordings, mouse and keyboard events,...

</details>

<details>
<summary><b>10. Continually Post-training Small Models via Synthetic Self-distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13113) • [📄 arXiv](https://arxiv.org/abs/2610.13113) • [📥 PDF](https://arxiv.org/pdf/2610.13113)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Synthetic Self-Distillation enables effective continual learning for small language models by using a minimally larger, same-family aligner to provide high-quality, in-distribution supervision.

</details>

<details>
<summary><b>11. SepGen: Multi-Stem Audio-Video Separation and Generation in a Single Model</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Lior Wolf, Idan Szpektor, Yonatan Bitton, Rajaei Khatib, AviadDahan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.11361) • [📄 arXiv](https://arxiv.org/abs/2610.11361) • [📥 PDF](https://arxiv.org/pdf/2610.11361)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AviadDahan/SepGen)

> SepGen extends a pretrained audio-video generator to emit the video, the audio-mix, and one waveform per captioned source (a stem) in a single sampling run. The same weights generate stems from text or separate them from an observed scene, so each...

</details>

<details>
<summary><b>12. Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12341) • [📄 arXiv](https://arxiv.org/abs/2610.12341) • [📥 PDF](https://arxiv.org/pdf/2610.12341)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/THU-CST-SAST/AAArena)

> In Learning Beyond Gradients, Jiayi Weng (@trinkle23897) discusses Heuristic Learning (HL): an agent acts as the learner, using experience and feedback to directly improve executable structures such as programs. Looking back, isn't every contestan...

</details>

<details>
<summary><b>13. SoloQ: Calibration-Free Quantization for Diffusion Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07121) • [📄 arXiv](https://arxiv.org/abs/2610.07121) • [📥 PDF](https://arxiv.org/pdf/2610.07121)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence</b> ⭐ 52</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37712) • [📄 arXiv](https://arxiv.org/abs/2609.37712) • [📥 PDF](https://arxiv.org/pdf/2609.37712)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/inclusionAI/PolyOCR-Venus)

> Meet PolyOCR-Venus , a family of OCR models for reading, locating, parsing, and reasoning over text in images. (｡•̀ᴗ-)✧ 🔍 A shared interface for diverse OCR tasks. The 2B and 9B models bring text recognition, grounding, document parsing, informati...

</details>

<details>
<summary><b>15. RSI-Anything: Unlocking Recursive Self-Improvement with World Models</b> ⭐ 281</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13912) • [📄 arXiv](https://arxiv.org/abs/2610.13912) • [📥 PDF](https://arxiv.org/pdf/2610.13912)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Gen-Verse/RSI-Anything)

> Code: https://github.com/Gen-Verse/RSI-Anything

</details>

<details>
<summary><b>16. Learning Representations to Guide Pixel Diffusion Transformers</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12978) • [📄 arXiv](https://arxiv.org/abs/2610.12978) • [📥 PDF](https://arxiv.org/pdf/2610.12978)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Pan-Zihao/Representation-Guidance)

> TL;DR: Can a plain Transformer generate high-quality images directly in pixel space, with no VAE and no specialized pixel decoder? We show that it can, provided its internal representation is both properly formed and actively exploited . 🔍 Two ins...

</details>

<details>
<summary><b>17. Contextual Correction of Parallel Draftsfor Speculative Decoding</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Itamar Zimerman, Omer Luxembourg, Harel Lidar, Tal-Gonen, RoyEisenstadtTD

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12570) • [📄 arXiv](https://arxiv.org/abs/2610.12570) • [📥 PDF](https://arxiv.org/pdf/2610.12570)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/two-delta/DCOCO)

> DCOCO makes parallel speculative decoding faster by restoring dependencies that diffusion-based drafters lose when predicting multiple future tokens simultaneously. Instead of committing to one token per position, it scores multiple candidates usi...

</details>

<details>
<summary><b>18. InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13944) • [📄 arXiv](https://arxiv.org/abs/2610.13944) • [📥 PDF](https://arxiv.org/pdf/2610.13944)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InternLM/InstantFusion)

> With InstantFusion, we explore a shared latent interface that aligns latent states across different image generators. This is our attempt to explore whether generative models can share a latent space. We’d love to hear your thoughts!

</details>

<details>
<summary><b>19. Inducing Process Supervision from Outcome-Only Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36641) • [📄 arXiv](https://arxiv.org/abs/2609.36641) • [📥 PDF](https://arxiv.org/pdf/2609.36641)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RUCBM/TIPS)

> Can strong process reward models emerge from outcome-only reinforcement learning? We introduce TIPS (Thinking-Induced Process Supervision), a simple framework that trains generative PRMs using only outcome-level correctness rewards, without human ...

</details>

<details>
<summary><b>20. Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark</b> ⭐ 21</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13947) • [📄 arXiv](https://arxiv.org/abs/2610.13947) • [📥 PDF](https://arxiv.org/pdf/2610.13947)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/physicalvision/Artisan)

> 🔥 Meet ARTISAN: a multi-agent pipeline for generating physically plausible articulated 3D assets. 🔥 Plus a comprehensive benchmark: spatial fidelity, physical plausibility, robot task performance & human preference. 🌐 Project page: https://physica...

</details>

<details>
<summary><b>21. SWE-Duel: Towards a Self-Scaling Arena for Coding Agents</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12569) • [📄 arXiv](https://arxiv.org/abs/2610.12569) • [📥 PDF](https://arxiv.org/pdf/2610.12569)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sweduel/SWE-Duel)

> Hi everyone👋 Static coding benchmarks don't last long. Their tasks leak into training data, and stronger agents saturate them. In SWE-Duel, we try a different approach: coding agents create tasks for each other at evaluation time, so there's nothi...

</details>

<details>
<summary><b>22. Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Zeren Zhang, Ziwei Chen, Junwei Yang, Xiaobo Liang, AlexMashiro

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09788) • [📄 arXiv](https://arxiv.org/abs/2610.09788) • [📥 PDF](https://arxiv.org/pdf/2610.09788)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EADMO/LatentGRM)

> The interesting idea here is that a reward model doesn’t need to spell out every evaluation step to make a good judgment. LatentGRM compresses rubric-based reasoning into continuous latent states, keeping judgment accuracy competitive while cuttin...

</details>

<details>
<summary><b>23. MetaKernelBench: Measuring GPU Kernel Knowledge Transfer Beyond Code</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05014) • [📄 arXiv](https://arxiv.org/abs/2610.05014) • [📥 PDF](https://arxiv.org/pdf/2610.05014)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YIGE24/MetaKernelBench)

> This paper introduces MetaKernelBench, which asks: Does the memory a GPU kernel agent distills from one DSL help a fresh attempt at the same problem in another DSL?

</details>

<details>
<summary><b>24. GraphDecisionBench: Benchmarking System One Models on Graph Tasks</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Li Zhao, Yapu Zhang, Xianliang Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06354) • [📄 arXiv](https://arxiv.org/abs/2610.06354) • [📥 PDF](https://arxiv.org/pdf/2610.06354)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VictorYXL/GraphDecisionBench)

> Large language models (LLMs) are increasingly explored for graph understanding and decision-making, while System One models such as Jev select directly from supplied options. However, the capabilities of System One models on graph-related tasks re...

</details>

<details>
<summary><b>25. DataVista: Diagnosing Multimodal LLMs on Data Video Understanding</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Zhouan Shen, Yinghao Tang, Jiayi Zhu, Zhenyang Wang, Yupeng Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.11993) • [📄 arXiv](https://arxiv.org/abs/2610.11993) • [📥 PDF](https://arxiv.org/pdf/2610.11993)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKUSTDial/DataVista)

> Data video is a media form that integrates data visualization with video narrative, widely adopted in news reporting and business analysis. Compared with general video understanding, data video understanding places greater emphasis on accurately r...

</details>

<details>
<summary><b>26. Recurrent Harness for Agentic Continual Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yang Song, Yangtian Zhang, Jianyu Wang, Zhiyun Lu, Yuxin Xiao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12668) • [📄 arXiv](https://arxiv.org/abs/2610.12668) • [📥 PDF](https://arxiv.org/pdf/2610.12668)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We propose to improve agentic continual learning through online adaptation of a recurrent harness.

</details>

<details>
<summary><b>27. From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39566) • [📄 arXiv](https://arxiv.org/abs/2609.39566) • [📥 PDF](https://arxiv.org/pdf/2609.39566)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VinyehShaw/CASE)

> CASE: From Given to Gathered Evidence Clinical reasoning is not merely about interpreting evidence, but also about knowing what evidence to seek. Existing medical AI benchmarks primarily evaluate reasoning over preselected information, overlooking...

</details>

<details>
<summary><b>28. MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13181) • [📄 arXiv](https://arxiv.org/abs/2610.13181) • [📥 PDF](https://arxiv.org/pdf/2610.13181)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LCGLiChenge/MixTok)

> adaptive image tokenizer with global 1D tokens and sparse 2D refinement

</details>

<details>
<summary><b>29. TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10288) • [📄 arXiv](https://arxiv.org/abs/2610.10288) • [📥 PDF](https://arxiv.org/pdf/2610.10288)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/phai-lab/touchscale)

> Introducing TouchScale: 500 Hours of Human Vision and Touch TouchScale pairs egocentric RGB-D and wrist RGB video with dense, full-hand tactile measurements from both hands. It spans approximately 2,000 predefined task descriptions, recorded with ...

</details>

<details>
<summary><b>30. Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12939) • [📄 arXiv](https://arxiv.org/abs/2610.12939) • [📥 PDF](https://arxiv.org/pdf/2610.12939)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Exploring a principled approach for finding multiple high information/diverse layers in a language model which can be used for boosting speculative decoding draft models.

</details>

<details>
<summary><b>31. Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution</b> ⭐ 14</summary>

<br/>

**👥 Authors:** Siqi Li, Bingjun Luo, GUALIN

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37950) • [📄 arXiv](https://arxiv.org/abs/2609.37950) • [📥 PDF](https://arxiv.org/pdf/2609.37950)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bingjunluo/Video-RSI)

> We introduce Video-RSI , a framework for recursive self-improvement of video understanding agents through harness evolution. Instead of updating model weights, Video-RSI enables the agent to revisit the original training videos used for evolution,...

</details>

<details>
<summary><b>32. Rethinking Relative Policy Differences Transfer of On-Policy Distillation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13205) • [📄 arXiv](https://arxiv.org/abs/2610.13205) • [📥 PDF](https://arxiv.org/pdf/2610.13205)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/KnowledgeXLab/A2-OPD)

> Can on-policy distillation transfer an improvement without requiring a stronger teacher? In Rethinking Relative Policy Differences Transfer of On-Policy Distillation, we study how the log-probability difference between a proxy expert and a proxy r...

</details>

<details>
<summary><b>33. Universal Textual Teaching for LLMs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Huan-WhoRegisteredMyName, alexlu9911

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12114) • [📄 arXiv](https://arxiv.org/abs/2610.12114) • [📥 PDF](https://arxiv.org/pdf/2610.12114)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper introduces Universal Textual Teaching (UTT), a parameter-update-free framework that distills observed Teacher-Student knowledge gaps into a textual, interpretable, and reusable natural-language artifact.

</details>

<details>
<summary><b>34. PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13171) • [📄 arXiv](https://arxiv.org/abs/2610.13171) • [📥 PDF](https://arxiv.org/pdf/2610.13171)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Nan-Jiang-Group/PreSTO)

> We propose to accelerate Power Sampling by prefetching its future proposals several steps away.

</details>

<details>
<summary><b>35. When Do Biological Reasoning Models Use Their Biological Inputs?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sham M. Kakade, Hanlin Zhang, Lukas Fesser, Nikitha Thoduguli, Ada Fang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.00898) • [📄 arXiv](https://arxiv.org/abs/2610.00898) • [📥 PDF](https://arxiv.org/pdf/2610.00898)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Do biological reasoning models actually use the biological inputs they receive? We investigate this question across six models spanning DNA, protein, and single-cell tasks, using input perturbations, evidence conflicts, linear probes, and reasonin...

</details>

<details>
<summary><b>36. The value of information and the emergence of communication in evolved e-puck robots</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13118) • [📄 arXiv](https://arxiv.org/abs/2610.13118) • [📥 PDF](https://arxiv.org/pdf/2610.13118)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ferdiex/easagru)

> This paper investigates when communication emerges in evolutionary robotics and how its emergence depends on the value of information available to autonomous agents. Using evolved e-puck robots reconstructed in PyBullet and validated against Webot...

</details>

<details>
<summary><b>37. Stateless Language Agents: Scaling Long-Horizon Automated Research</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07625) • [📄 arXiv](https://arxiv.org/abs/2610.07625) • [📥 PDF](https://arxiv.org/pdf/2610.07625)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Alex-q-z/stateless-language-agents)

> .

</details>

<details>
<summary><b>38. AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13627) • [📄 arXiv](https://arxiv.org/abs/2610.13627) • [📥 PDF](https://arxiv.org/pdf/2610.13627)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/nat-nischw/AMLworld-Compact)

> TL;DR: Evaluating LLMs on million-scale graphs shouldn't cost a fortune. We introduce AMLworld-Compact, reducing AML graph evaluation targets by up to 611x using the HT-Coreset protocol (importance-weighted downsampling) while preserving unbiased ...

</details>

<details>
<summary><b>39. Less from More: Reinforcing Sparse Video Reasoning from Dense References</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10893) • [📄 arXiv](https://arxiv.org/abs/2610.10893) • [📥 PDF](https://arxiv.org/pdf/2610.10893)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lmsdss/SAVER)

> SAVER learns from dense video views to reason with sparse frames. It pairs dense and sparse views in a shared policy and uses a reliability-gated reference reward: the dense prediction guides the sparse one only when its grounding reward is higher...

</details>

<details>
<summary><b>40. When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts Is Often Better</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.11291) • [📄 arXiv](https://arxiv.org/abs/2610.11291) • [📥 PDF](https://arxiv.org/pdf/2610.11291)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>41. QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36760) • [📄 arXiv](https://arxiv.org/abs/2609.36760) • [📥 PDF](https://arxiv.org/pdf/2609.36760)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multi-Head Latent Attention (MLA) enables expressive multi-head attention with compact caches for its content and decoupled RoPE paths, yet cache memory still scales linearly with context length and batch size. In this work, we establish a systema...

</details>

<details>
<summary><b>42. MAMHOI: Factorizing Scene-Aware Human-Object Interaction through Affordances</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12416) • [📄 arXiv](https://arxiv.org/abs/2610.12416) • [📥 PDF](https://arxiv.org/pdf/2610.12416)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LeiMingyuan/MAMHOI) • [⭐ Code](https://github.com/LeiMingyuan/MAMHOI-project-page)

> We introduce MAMHOI, a framework for generating scene-aware human–object interactions in complex 3D environments. Our key observation is that this task requires two complementary capabilities: understanding where an interaction can be feasibly per...

</details>

<details>
<summary><b>43. Encore: Few-Shot Agentic Discovery of Manipulation Strategies</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37359) • [📄 arXiv](https://arxiv.org/abs/2609.37359) • [📥 PDF](https://arxiv.org/pdf/2609.37359)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YIFANK/encore)

> Few-shot demonstrations act as a search prior for coding agents: ENCORE distills them into packs the agent reads to write and freeze policy programs, reaching 96.3% on sealed LIBERO-PRO perturbations and solving underspecified RoboDojo tasks that ...

</details>

<details>
<summary><b>44. ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13316) • [📄 arXiv](https://arxiv.org/abs/2610.13316) • [📥 PDF](https://arxiv.org/pdf/2610.13316)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/atfortes/ThinkDrag)

> ThinkDrag turns sparse drag handles into semantic image edits. It can first infer the intended transformation, then use that visual reasoning trace to guide generation. Users can also add text prompts to disambiguate edit intent.

</details>

<details>
<summary><b>45. When to Rethink: Learning Multi-Perspective Self-Verification for Vision-Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yicheng Lin, Morris Yu-Chao Huang, Si-Yuan Lu, Hanruo Zhu, Ziquan Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07018) • [📄 arXiv](https://arxiv.org/abs/2610.07018) • [📥 PDF](https://arxiv.org/pdf/2610.07018)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/misswayguy/Motive)

> 🧠 MOTIVE: When to Rethink Learning Multi-Perspective Self-Verification for Vision-Language Models We introduce MOTIVE , a framework that helps vision-language models decide when to trust an answer and when to rethink , using complementary verifica...

</details>

<details>
<summary><b>46. Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yoonkyo Jung, Jonguk Cheon, Yeonsoo Park, Sungha Kim, jlee-larr

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12470) • [📄 arXiv](https://arxiv.org/abs/2610.12470) • [📥 PDF](https://arxiv.org/pdf/2610.12470)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> From a single human video, we extract task structure and use it to train dexterous RL policies that generalize beyond the input demonstration.

</details>

<details>
<summary><b>47. Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jihyo Kim, Hoyun Song, Inho Won, SeungWoo Song, HyeonSeok Lim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09607) • [📄 arXiv](https://arxiv.org/abs/2610.09607) • [📥 PDF](https://arxiv.org/pdf/2610.09607)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning (EMNLP 2026 Findings Paper)

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 47 |
| 📅 Today | [`2026-10-12.json`](data/daily/2026-10-12.json) | 47 |
| 📆 This Week | [`2026-W41.json`](data/weekly/2026-W41.json) | 47 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 733 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-12 | 47 | [View JSON](data/daily/2026-10-12.json) |
| 📄 2026-10-11 | 72 | [View JSON](data/daily/2026-10-11.json) |
| 📄 2026-10-10 | 72 | [View JSON](data/daily/2026-10-10.json) |
| 📄 2026-10-09 | 55 | [View JSON](data/daily/2026-10-09.json) |
| 📄 2026-10-08 | 52 | [View JSON](data/daily/2026-10-08.json) |
| 📄 2026-10-07 | 51 | [View JSON](data/daily/2026-10-07.json) |
| 📄 2026-10-06 | 48 | [View JSON](data/daily/2026-10-06.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W41 | 47 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 733 | [View JSON](data/monthly/2026-10.json) |
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
