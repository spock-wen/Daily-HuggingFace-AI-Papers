<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-30-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9950+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">86</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">549</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9950+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 18, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22115) • [📄 arXiv](https://arxiv.org/abs/2611.22115) • [📥 PDF](https://arxiv.org/pdf/2611.22115)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XingChen-AGI)

> Xing4 LLMs

</details>

<details>
<summary><b>2. AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs</b> ⭐ 25</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17621) • [📄 arXiv](https://arxiv.org/abs/2611.17621) • [📥 PDF](https://arxiv.org/pdf/2611.17621)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SLAI-AITP/AscendGYM)

> AscendGYM

</details>

<details>
<summary><b>3. Weight-Space Programming Doesn't Need Transformers</b> ⭐ 27</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22055) • [📄 arXiv](https://arxiv.org/abs/2611.22055) • [📥 PDF](https://arxiv.org/pdf/2611.22055)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/effl-lab/Weight-Space-Programming)

> Weight-space programming from scratch.

</details>

<details>
<summary><b>4. ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21099) • [📄 arXiv](https://arxiv.org/abs/2610.08784) • [📥 PDF](https://arxiv.org/pdf/2611.21099)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/showlab/ForceHarness)

> Hi everyone! 👋 Excited to share ForceHarness , an agent harness that lets frozen API frontier models understand and use wrist force for contact-rich manipulation—with zero demonstrations and zero finetuning . Why ForceHarness? Frontier models can ...

</details>

<details>
<summary><b>5. Multi-Branch Transformer</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Hongzheng Chen, Zhiwei Xu, Chunyuan Deng, Lingjie Chen, Gaotang Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19800) • [📄 arXiv](https://arxiv.org/abs/2611.19800) • [📥 PDF](https://arxiv.org/pdf/2611.19800)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/GaotangLi/Multi-Branch-Transformer)

> Transformers are typically scaled by increasing their width or depth. In this work, we explore branching, the parallel composition of full Transformer blocks, as an additional dimension for scaling LLMs.

</details>

<details>
<summary><b>6. Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Svetlana Erofeeva, Galina Zubkova, blinoff, BearSubj13, ivanpodd

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.15348) • [📄 arXiv](https://arxiv.org/abs/2611.15348) • [📥 PDF](https://arxiv.org/pdf/2611.15348)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ivanpodd/Breath-Dx)

> 🏆 IEEE ICDM 2026 Best Paper Runner-Up (Applied Track) Hello, everyone! I'm one of the authors of Breath-Dx, the first comprehensive time-series classification benchmark for non-invasive disease screening using electronic nose (eNose) sensors. Most...

</details>

<details>
<summary><b>7. Self-Improvement Memory Enables Continual Recursive Self-Improvement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18856) • [📄 arXiv](https://arxiv.org/abs/2611.18856) • [📥 PDF](https://arxiv.org/pdf/2611.18856)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Author affiliations (as listed in the paper): Google Cloud AI · Google DeepMind · Google Cloud AI Research · The Pennsylvania State University. We started with a practical question: after spending many rounds improving an agent’s harness, what sho...

</details>

<details>
<summary><b>8. TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Tianyu Qi, Yunfeng Fan, Xiangyang Liu, flameeee, HarrisonPENG

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23143) • [📄 arXiv](https://arxiv.org/abs/2611.23143) • [📥 PDF](https://arxiv.org/pdf/2611.23143)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Livioni/TCP4D)

> Meet TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation Given monocular RGB video and initial 2D TCP queries, it recovers 6-DoF tool poses and gripper states. Its shared 4D representation also supports language...

</details>

<details>
<summary><b>9. FastFrames: Video Generation at Interactive Latency</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23226) • [📄 arXiv](https://arxiv.org/abs/2611.23226) • [📥 PDF](https://arxiv.org/pdf/2611.23226)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/apple-aiml-research/ml-fastframes)

> See our project page for videos, code, and model weights: https://apple-aiml-research.github.io/ml-fastframes/ .

</details>

<details>
<summary><b>10. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22275) • [📄 arXiv](https://arxiv.org/abs/2611.22275) • [📥 PDF](https://arxiv.org/pdf/2611.22275)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/heaveho-humanoid/Heave-Ho)

> 🤖🤝🤖 Heave-Ho: teams of humanoids collaborating on long-horizon tasks — fully decentralized, with no network communication between robots. • Low level: multi-agent post-training adds a shared residual policy on top of a frozen humanoid foundation t...

</details>

<details>
<summary><b>11. VideoNexus: Video Perception Beyond the Reasoning Context</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21392) • [📄 arXiv](https://arxiv.org/abs/2611.21392) • [📥 PDF](https://arxiv.org/pdf/2611.21392)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Awesome think with video solution for long video understanding～

</details>

<details>
<summary><b>12. π^4: A Foundation Model for 4D Scene Geometry and Motion</b> ⭐ 22</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23144) • [📄 arXiv](https://arxiv.org/abs/2611.23144) • [📥 PDF](https://arxiv.org/pdf/2611.23144)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yyfz/Pi4)

> π^4 is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, togethe...

</details>

<details>
<summary><b>13. MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.20992) • [📄 arXiv](https://arxiv.org/abs/2611.20992) • [📥 PDF](https://arxiv.org/pdf/2611.20992)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zfkarl/MedJev)

> MedJev is a system one vision-language decision model for fast and effective medical image understanding.

</details>

<details>
<summary><b>14. FMT: Lossless Image Compression in a Fixed Number of Parallel Steps</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23108) • [📄 arXiv](https://arxiv.org/abs/2611.23108) • [📥 PDF](https://arxiv.org/pdf/2611.23108)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Code will be added later. Enjoy reading !!

</details>

<details>
<summary><b>15. From Repositories to Training Environments: Scaling Long-Horizon Coding Agents with Environment Evolution Loop</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21152) • [📄 arXiv](https://arxiv.org/abs/2611.21152) • [📥 PDF](https://arxiv.org/pdf/2611.21152)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/IQuestLab/RepoFactory)

> Coding agents are taking on longer-horizon, more complex development tasks, and training also needs to cover the complete project development process. 🚀 However, existing environment construction pipelines often stop at execution and validation, l...

</details>

<details>
<summary><b>16. Beyond Answering: Learning to Speak First and Act in Streaming Video</b> ⭐ 23</summary>

<br/>

**👥 Authors:** Xintong Guo, Shuhan Li, ChjyR, Sybilhhhhh, huankguan2

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17048) • [📄 arXiv](https://arxiv.org/abs/2611.17048) • [📥 PDF](https://arxiv.org/pdf/2611.17048)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aurateam2026/Aura2.0)

> Hi Hugging Face community! 👋 We’re excited to share AURA 2.0 — Beyond Answering: Learning to Speak First and Act in Streaming Video. What if a video AI could notice something worth discussing and start the conversation, rather than always waiting ...

</details>

<details>
<summary><b>17. Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ying Wei, Yuan Wei, Sijian Ren, Deyang Kong, joeylee2333

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19244) • [📄 arXiv](https://arxiv.org/abs/2611.19244) • [📥 PDF](https://arxiv.org/pdf/2611.19244)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> On-policy distillation (OPD) transfers specialized capabilities to language-model agents, but its cross-domain effects on interaction remain unclear. We investigate how OPD reshapes ReAct interaction patterns across mathematics, ALFWorld, and τ2-b...

</details>

<details>
<summary><b>18. ResWAM: Learning What Changes, Not What Stays, for World-Action Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19559) • [📄 arXiv](https://arxiv.org/abs/2611.19559) • [📥 PDF](https://arxiv.org/pdf/2611.19559)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OPTML-Group/ResWAM)

> ResWAM is a world-action model for robot manipulation that learns to predict what changes in the scene (the residual), and it uses this change-focused prediction to guide action generation.

</details>

<details>
<summary><b>19. VisualArtifactSpec 1.0: Evaluating Visual Artifacts under Task Specifications</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21382) • [📄 arXiv](https://arxiv.org/abs/2611.21382) • [📥 PDF](https://arxiv.org/pdf/2611.21382)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Accio-Lab/VisualArtifactSpec)

> We introduce VisualArtifactSpec 1.0 (VAS) , a benchmark for evaluating agent-authored visual artifacts. VAS includes 211 creation and modification tasks across 4 artifact families: 📊 Presentations: creating decks from scratch, working with templat...

</details>

<details>
<summary><b>20. Do LLM Agents Still Need to Be Told How to Self-Improve?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23219) • [📄 arXiv](https://arxiv.org/abs/2611.23219) • [📥 PDF](https://arxiv.org/pdf/2611.23219)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ssundaram21/self-org)

> TL;DR: We give an LLM agent a general self-improvement goal, a budget, and basic tools for collecting experience and editing text. We do not give it real tasks or an explicit recipe. Sufficiently capable models successfully compose their own self-...

</details>

<details>
<summary><b>21. MPEG-Diffusion: Mixed-Resolution Video Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12069) • [📄 arXiv](https://arxiv.org/abs/2611.12069) • [📥 PDF](https://arxiv.org/pdf/2611.12069)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> MPEG Diffusion for video gen: high-resolution on important subjects, low-res on the background to save compute while keeping visual quality. It features: Close to full-res DiT self-select high-res regions Up to 4.8× faster (30% tokens)

</details>

<details>
<summary><b>22. Regularized Score Centering</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21791) • [📄 arXiv](https://arxiv.org/abs/2611.21791) • [📥 PDF](https://arxiv.org/pdf/2611.21791)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Asynchronous reinforcement learning increases training throughput, but data from stale policies and numerical mismatch between training and inference can destabilize learning. To stabilize off-policy learning, score centering (SC) removes the effe...

</details>

<details>
<summary><b>23. MillBill: A Machining Agent with Geometric Feedback</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Anton Konushin, Andrey Kuznetsov, Soslan Kabisov, Artem Slavin, Gennadii Savrasov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22565) • [📄 arXiv](https://arxiv.org/abs/2611.22565) • [📥 PDF](https://arxiv.org/pdf/2611.22565)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kulibinai/MillBill) • [⭐ Code](https://github.com/kulibinai/millbill)

> Can a language model program a CNC machine without computing a single coordinate? 🛠️ MillBill turns a B-rep part, its stock and its material into G-code for indexed 3-axis milling. The LLM only makes the machining decisions: operations, tools, cut...

</details>

<details>
<summary><b>24. CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Andrey Kuznetsov, Gennadii Savrasov, Soslan Kabisov, Nikita Gavrilov, Oleg Pavlov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.22563) • [📄 arXiv](https://arxiv.org/abs/2611.22563) • [📥 PDF](https://arxiv.org/pdf/2611.22563)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kulibinai/cadmageddon)

> CADMAGEDDON: mesh → editable CAD with one open-weight model, no frontier API needed 🛠️ Most mesh-to-CAD systems make a model write the whole program, including every coordinate and dimension. We split each feature in two: • geometric instruments d...

</details>

<details>
<summary><b>25. AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.21421) • [📄 arXiv](https://arxiv.org/abs/2611.21421) • [📥 PDF](https://arxiv.org/pdf/2611.21421)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce AuXSpec, a Lean framework that pairs each declarative postcondition with an executable postcondition, so test cases can check generated specifications by execution. 🔐 This unlocks execution-based reinforcement learning for formal spec...

</details>

<details>
<summary><b>26. PanDWM: Panoramic 4D Driving World Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.19857) • [📄 arXiv](https://arxiv.org/abs/2611.19857) • [📥 PDF](https://arxiv.org/pdf/2611.19857)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGeeksGroup/PanDWM)

> We present PanDWM, a panoramic 4D driving world model that generates view-consistent 360° scenes from multi-camera layouts. Our approach combines a causal generative model with a feed-forward 3D Gaussian decoder for efficient dynamic scene reconst...

</details>

<details>
<summary><b>27. The Noise Floor of a Quantization Comparison: Engine, restart, batch and kernel drift, measured against 8-bit and 4-bit effects in two decision models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.15671) • [📄 arXiv](https://arxiv.org/abs/2611.15671) • [📥 PDF](https://arxiv.org/pdf/2611.15671)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Level5Tech/clef-quant-bench)

> We measured how much a quantized model's decisions move for reasons that have nothing to do with quantization: a different serving engine, a restart, a different batch size or kernel. On Cloudflare's Clef and Clef-flash, those alone move up to 0.9...

</details>

<details>
<summary><b>28. M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** AiTi Aw, Longyin Zhang, Shuo Sun, Hoang Phan, ngqtrung

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23034) • [📄 arXiv](https://arxiv.org/abs/2611.23034) • [📥 PDF](https://arxiv.org/pdf/2611.23034)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ngquangtrung57/M3OPD-Reasoner)

> M3OPD-Reasoner is a fully open recipe that post-trains Qwen3.5-9B into one reasoning model for image STEM, image perception and video. 🌐 Project page: https://ngquangtrung57.github.io/m3opd-reasoner-page/ 💻 Code: https://github.com/ngquangtrung57/...

</details>

<details>
<summary><b>29. TPHC: Improving Hyper-Connections with Tensor-Parallel Grouped Updates</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kefeng Zhang, Jianchao Tan, Haoyi Wu, You Wu, Xinying Hu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.23026) • [📄 arXiv](https://arxiv.org/abs/2611.23026) • [📥 PDF](https://arxiv.org/pdf/2611.23026)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wuyou2002/TPHC)

> By aligning HC stream updates with TP shards, TPHC delivers consistent gains over mHC without adding parameters or FLOPs. The three of us, sharing co-first authorship and now in our final year of university, began this project back in 2024, and it...

</details>

<details>
<summary><b>30. Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08922) • [📄 arXiv](https://arxiv.org/abs/2611.08922) • [📥 PDF](https://arxiv.org/pdf/2611.08922)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/StanfordMIMI/Glyph)

> Can model interpretability help us learn something new about human health? Glyph is a framework for AI-accelerated clinical science. It uses sparse autoencoders to uncover patterns in multimodal clinical data hidden within foundation models, turni...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 30 |
| 📅 Today | [`2026-11-18.json`](data/daily/2026-11-18.json) | 30 |
| 📆 This Week | [`2026-W46.json`](data/weekly/2026-W46.json) | 86 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 549 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-18 | 30 | [View JSON](data/daily/2026-11-18.json) |
| 📄 2026-11-17 | 30 | [View JSON](data/daily/2026-11-17.json) |
| 📄 2026-11-16 | 26 | [View JSON](data/daily/2026-11-16.json) |
| 📄 2026-11-15 | 34 | [View JSON](data/daily/2026-11-15.json) |
| 📄 2026-11-14 | 34 | [View JSON](data/daily/2026-11-14.json) |
| 📄 2026-11-13 | 24 | [View JSON](data/daily/2026-11-13.json) |
| 📄 2026-11-12 | 18 | [View JSON](data/daily/2026-11-12.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W46 | 86 | [View JSON](data/weekly/2026-W46.json) |
| 📅 2026-W45 | 193 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 549 | [View JSON](data/monthly/2026-11.json) |
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
