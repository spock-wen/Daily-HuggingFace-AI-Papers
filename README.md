<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-26-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5841+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">26</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">35</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">153</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5841+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 07, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. UI-MOPD: Multi-Platform On-Policy Distillation for Continual GUI Agent Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fazhan Liu, Chengzhen Duan, Zhehao Yu, Alan Chen, Niu Lian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04425) • [📄 arXiv](https://arxiv.org/abs/2607.04425) • [📥 PDF](https://arxiv.org/pdf/2607.04425)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> UI-MOPD: Multi-Platform On-Policy Distillation for Continual GUI Agent Learning

</details>

<details>
<summary><b>2. ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04438) • [📄 arXiv](https://arxiv.org/abs/2607.04438) • [📥 PDF](https://arxiv.org/pdf/2607.04438)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ResearchStudio - Reel From paper to poster, video, blog, and reel — Automating the Last Mile of Research Dissemination. ResearchStudio streamlines the final steps of a research project — the materials a paper needs after the writing is done. Drop ...

</details>

<details>
<summary><b>3. ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes</b> ⭐ 84</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04439) • [📄 arXiv](https://arxiv.org/abs/2607.04439) • [📥 PDF](https://arxiv.org/pdf/2607.04439)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/microsoft/ResearchStudio)

> From a research problem to a reviewer-defensible idea card — Automating the First Mile of Research Ideation. ResearchStudio-Idea is a reusable research ideation skill suite that assists researchers in developing well-grounded research proposals. I...

</details>

<details>
<summary><b>4. PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Changhu Wang, Dongdong Yu, Qihang Cao, Zhaoqing Wang, Sensen Gao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05373) • [📄 arXiv](https://arxiv.org/abs/2607.05373) • [📥 PDF](https://arxiv.org/pdf/2607.05373)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>5. OmniOpt: Taxonomy, Geometry, and Benchmarking of Modern Optimizers</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04033) • [📄 arXiv](https://arxiv.org/abs/2607.04033) • [📥 PDF](https://arxiv.org/pdf/2607.04033)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenRaiser/OmniOpt)

> Optimizer selection for large scale model training is constrained by compute, memory, tuning budget, and task diversity, yet the landscape of over one hundred methods remains fragmented. We introduce OmniOpt, a unified survey and benchmark cookboo...

</details>

<details>
<summary><b>6. GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation</b> ⭐ 118</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.02642) • [📄 arXiv](https://arxiv.org/abs/2607.02642) • [📥 PDF](https://arxiv.org/pdf/2607.02642)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/open-gigaai/giga-world-1)

> Code： https://github.com/open-gigaai/giga-world-1 Model： https://huggingface.co/open-gigaai/Giga-World-1 Data： https://huggingface.co/datasets/open-gigaai/CVPR-2026-WorldModel-Track-Dataset Benchmark： https://huggingface.co/spaces/open-gigaai/CVPR...

</details>

<details>
<summary><b>7. EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots</b> ⭐ 33</summary>

<br/>

**👥 Authors:** Donglin Yang, Linqing Zhong, Liyao Wang, Yang Yi, Heqing Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.02646) • [📄 arXiv](https://arxiv.org/abs/2607.02646) • [📥 PDF](https://arxiv.org/pdf/2607.02646)

**💻 Code:** [⭐ Code](https://github.com/Noietch/EVA-CLIENT) • [⭐ Code](https://github.com/huggingface)

> EVA-Client: One Client, Full Cycle For robot policies, training frameworks have converged: OpenPI, LeRobot, StarVLA, and VLA Foundry solve much of the training-side stack. The real-robot side should not still be a patchwork of project-specific scr...

</details>

<details>
<summary><b>8. Wan-Streamer v0.2: Higher Resolution, Same Latency</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04443) • [📄 arXiv](https://arxiv.org/abs/2607.04443) • [📥 PDF](https://arxiv.org/pdf/2607.04443)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A latency-preserving Wan Streamer upgrade: from 192p close-up calls to 640×368 clearer calls and scene-grounded mid-shot agents, still at 25 fps with ~200 ms model-side latency.

</details>

<details>
<summary><b>9. Vision Pretraining for Dense Spatial Perception</b> ⭐ 65</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05247) • [📄 arXiv](https://arxiv.org/abs/2607.05247) • [📥 PDF](https://arxiv.org/pdf/2607.05247)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Robbyant/lingbot-vision)

> A novel SSL pretraining for spatial perception with a STRONG depth model, LingBot-Depth 2.0

</details>

<details>
<summary><b>10. InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuyin Yang, Hao Li, Xiaoxu Xu, Junhao Cai, Haoxiang Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04988) • [📄 arXiv](https://arxiv.org/abs/2607.04988) • [📥 PDF](https://arxiv.org/pdf/2607.04988)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InternRobotics/InternVLA-A-series)

> Hi, I'm the author of this paper, can you add the opensource code link? https://github.com/InternRobotics/InternVLA-A-series

</details>

<details>
<summary><b>11. Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jaewoo Kang, Jungwoo Park, Junha Jung, Suhyeong Park

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04605) • [📄 arXiv](https://arxiv.org/abs/2607.04605) • [📥 PDF](https://arxiv.org/pdf/2607.04605)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dmis-lab/SaMer)

> Multi-vector vision-language retrieval preserves fine-grained visual evidence through maximum-similarity late interaction, but dense image-side tokens make storage and scoring expensive. Existing token compression methods reduce this cost, yet the...

</details>

<details>
<summary><b>12. dOPSD: On-Policy Self-Distillation for Diffusion Language Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Xinchao Wang, Qi Li, Phuong Tuan Dat

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04428) • [📄 arXiv](https://arxiv.org/abs/2607.04428) • [📥 PDF](https://arxiv.org/pdf/2607.04428)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tuandattt/dOPSD)

> Github Repo: https://github.com/tuandattt/dOPSD

</details>

<details>
<summary><b>13. Perceptual Flow Matching for Few-Step Generative Modeling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.03524) • [📄 arXiv](https://arxiv.org/abs/2607.03524) • [📥 PDF](https://arxiv.org/pdf/2607.03524)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. LLM-as-a-Verifier: A General-Purpose Verification Framework</b> ⭐ 409</summary>

<br/>

**👥 Authors:** Yixing Jiang, Yuejiang Liu, Pranav Atreya, Shulu Li, Jacky Kwok

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05391) • [📄 arXiv](https://arxiv.org/abs/2607.05391) • [📥 PDF](https://arxiv.org/pdf/2607.05391)

**💻 Code:** [⭐ Code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>15. KVpop -- Key-Value Cache Compression with Predictive Online Pruning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05061) • [📄 arXiv](https://arxiv.org/abs/2607.05061) • [📥 PDF](https://arxiv.org/pdf/2607.05061)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Key-value (KV) cache growth is a major bottleneck in autoregressive decoding, as memory and bandwidth scale linearly with context length. Existing KV eviction methods often rely on static heuristics or proxy scores, which poorly track future token...

</details>

<details>
<summary><b>16. EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05155) • [📄 arXiv](https://arxiv.org/abs/2607.05155) • [📥 PDF](https://arxiv.org/pdf/2607.05155)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. Multiplayer Interactive World Models with Representation Autoencoders</b> ⭐ 103</summary>

<br/>

**👥 Authors:** Aditya Makkar, Chris Mulder, Adrien Ramanana Rahary, Václav Volhejn, Anthony Hu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05352) • [📄 arXiv](https://arxiv.org/abs/2607.05352) • [📥 PDF](https://arxiv.org/pdf/2607.05352)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mira-wm/mira)

> No abstract available.

</details>

<details>
<summary><b>18. Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.01793) • [📄 arXiv](https://arxiv.org/abs/2607.01793) • [📥 PDF](https://arxiv.org/pdf/2607.01793)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yunhao-Feng/Vera)

> LLM agents increasingly perform autonomous actions through external tools, leading to complex and evolving safety risks. However, existing safety testing targets expert-designed safety violations, and the corresponding outcomes are evaluated by ha...

</details>

<details>
<summary><b>19. Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhijiang Guo, Renyang Liu, Tianyi Wu, Luu Anh Tuan, Mingzhe Du

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.01764) • [📄 arXiv](https://arxiv.org/abs/2607.01764) • [📥 PDF](https://arxiv.org/pdf/2607.01764)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Repository-level vulnerability reproduction is a demanding software engineering (SE) task: an agent must inspect a codebase, infer the input grammar that reaches a vulnerable path, construct a proof-of-conceptv(PoC), and verify that the crash disa...

</details>

<details>
<summary><b>20. MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sagie Benaim, Hadar Averbuch-Elor, galfiebelman

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05376) • [📄 arXiv](https://arxiv.org/abs/2607.05376) • [📥 PDF](https://arxiv.org/pdf/2607.05376)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A video diffusion framework generates long, multi-view consistent videos by combining temporal and view-wise autoregression through 4D geometric bridging and spatio-temporal distillation techniques.

</details>

<details>
<summary><b>21. PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Ruoxi Xu, Hanshu Zhou, Jiawei Chen, Boxi Cao, Zhuoqun Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.02881) • [📄 arXiv](https://arxiv.org/abs/2607.02881) • [📥 PDF](https://arxiv.org/pdf/2607.02881)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/icip-cas/PraMem)

> Long-horizon behavior prediction aims to infer a user's next action based on a lengthy historical sequence, playing a crucial role in artificial intelligence field. The rise of large language models (LLMs) offers a promising direction for sequenti...

</details>

<details>
<summary><b>22. GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Abinaya Dinesh, Rome-1, alessiotoniolo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11688) • [📄 arXiv](https://arxiv.org/abs/2602.11688) • [📥 PDF](https://arxiv.org/pdf/2602.11688)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/atoniolo76/GORGO)

> In load-balancing for LLM inference, TTFT consists of three distinct costs: network latency, prefill time, and queueing delay. While cache-aware policies aim to reuse existing KV-cache, these policies cannot balance load effectively, causing E2E l...

</details>

<details>
<summary><b>23. Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.05390) • [📄 arXiv](https://arxiv.org/abs/2607.05390) • [📥 PDF](https://arxiv.org/pdf/2607.05390)

**💻 Code:** [⭐ Code](https://github.com/lhy0807/deform360) • [⭐ Code](https://github.com/huggingface)

> 198 daily-life deformable objects. 1,980 interactions. 41 surround-view cameras and bimanual tactile grippers — a foundation for benchmarking 2D and 3D world models on real-world deformable dynamics.

</details>

<details>
<summary><b>24. CONFLUX: A Latent Diusion Model for 3D Chest-CT Synthesis with RL Post-Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.02998) • [📄 arXiv](https://arxiv.org/abs/2607.02998) • [📥 PDF](https://arxiv.org/pdf/2607.02998)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> CONFLUX is a conditional rectified-flow model for full-volume 3D chest-CT synthesis, with GRPO reinforcement-learning post-training that sharpens control over the requested clinical findings. Flow matching trains the generator to match the data di...

</details>

<details>
<summary><b>25. Speaker-Disentangled Chunk-Wise Regression for Syllabic Tokenization</b> ⭐ 46</summary>

<br/>

**👥 Authors:** Takahiro Shinozaki, Takuma Okamoto, Kota Kawakita, Ryota Komatsu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.04064) • [📄 arXiv](https://arxiv.org/abs/2607.04064) • [📥 PDF](https://arxiv.org/pdf/2607.04064)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ryota-komatsu/speaker_disentangled_hubert)

> In this IEEE OJSP paper, we introduce SylReg-LM 7B, an efficiently scalable interleaved syllable-text language model!

</details>

<details>
<summary><b>26. PixCon: Clean-Positive Contrastive Learning for Foundation-Model Semi-Supervised Segmentation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.03068) • [📄 arXiv](https://arxiv.org/abs/2607.03068) • [📥 PDF](https://arxiv.org/pdf/2607.03068)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/psychofict/PixCon)

> Foundation backbones change the semi-supervised segmentation regime: with a DINOv2 teacher, a strict confidence threshold already retains a measured ~98%-clean pseudo-label set, so the remaining accuracy lives in how the embedding space is structu...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 26 |
| 📅 Today | [`2026-07-07.json`](data/daily/2026-07-07.json) | 26 |
| 📆 This Week | [`2026-W27.json`](data/weekly/2026-W27.json) | 35 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 153 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-07 | 26 | [View JSON](data/daily/2026-07-07.json) |
| 📄 2026-07-06 | 9 | [View JSON](data/daily/2026-07-06.json) |
| 📄 2026-07-05 | 27 | [View JSON](data/daily/2026-07-05.json) |
| 📄 2026-07-04 | 27 | [View JSON](data/daily/2026-07-04.json) |
| 📄 2026-07-03 | 20 | [View JSON](data/daily/2026-07-03.json) |
| 📄 2026-07-02 | 22 | [View JSON](data/daily/2026-07-02.json) |
| 📄 2026-07-01 | 22 | [View JSON](data/daily/2026-07-01.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W27 | 35 | [View JSON](data/weekly/2026-W27.json) |
| 📅 2026-W26 | 165 | [View JSON](data/weekly/2026-W26.json) |
| 📅 2026-W25 | 155 | [View JSON](data/weekly/2026-W25.json) |
| 📅 2026-W24 | 194 | [View JSON](data/weekly/2026-W24.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 153 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |

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
