<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-51-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-10263+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">51</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">131</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">862</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">10263+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 25, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Antom 3-in-1 Transformer: A Payment Foundation Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.25403) • [📄 arXiv](https://arxiv.org/abs/2611.25403) • [📥 PDF](https://arxiv.org/pdf/2611.25403)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Antom 3-in-1 Transformer , a payment foundation model from Ant International. It brings sequence (transaction histories), tabular (features), and graph (relational) representations into one backbone with task-conditioned fusion, built...

</details>

<details>
<summary><b>2. Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Haiyan Yin, Long-Kai Huang, Yichen Liu, Jie-Jing Shao, Jiaqi Su

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28947) • [📄 arXiv](https://arxiv.org/abs/2611.28947) • [📥 PDF](https://arxiv.org/pdf/2611.28947)

**💻 Code:** [⭐ Code](https://github.com/SuJQ0722/NightWatch) • [⭐ Code](https://github.com/huggingface)

> This is an automated message from the ResearchStudio team. We created an interactive ResearchStudio Reel for this paper. It includes a visual poster , a video , and a blog , all available for download in editable formats. Open the ResearchStudio R...

</details>

<details>
<summary><b>3. Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32884) • [📄 arXiv](https://arxiv.org/abs/2611.32884) • [📥 PDF](https://arxiv.org/pdf/2611.32884)

**💻 Code:** [⭐ Code](https://github.com/declare-lab/RLVB) • [⭐ Code](https://github.com/huggingface)

> Lazy agents answer against their own beliefs. VLM agents on long tasks often commit to an answer while their own stated belief still names several possible answers, for example writing "Possible: cups 2, 4" and then answering cup 4. RLVB (Reinforc...

</details>

<details>
<summary><b>4. Rewirable Circuits in Transformers with Loom Attention</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Xingyuan Yuan, Shengping Li, Qingye Meng, xiaoda99

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30634) • [📄 arXiv](https://arxiv.org/abs/2611.30634) • [📥 PDF](https://arxiv.org/pdf/2611.30634)

**💻 Code:** [⭐ Code](https://github.com/Caiyun-AI/LoomFormer) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! Author here — happy to share LoomFormer , along with our JAX/Pallas training code, PyTorch/Triton inference kernels, and 300B-token 2.8B checkpoints (including a matched mHC-Pythia-2.8B baseline). TL;DR: Why layer-wise residual routin...

</details>

<details>
<summary><b>5. ACAP: Asynchronous Coding Agents for Efficient Robot Control</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31205) • [📄 arXiv](https://arxiv.org/abs/2611.31205) • [📥 PDF](https://arxiv.org/pdf/2611.31205)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We are introducing ACAP: Asynchronous Coding Agents as Policy . A robot policy built from persistent coding agents that reason and act asynchronously. A single coding agent can issue parallel motion commands, but every decision still passes throug...

</details>

<details>
<summary><b>6. Self-Evolving Evaluation Environments for Computer-Use Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30962) • [📄 arXiv](https://arxiv.org/abs/2611.30962) • [📥 PDF](https://arxiv.org/pdf/2611.30962)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> CUA-SEE reconceptualizes evaluation as a dynamic, closed-loop process where tasks, executable verifiers, and agent rollout evidence continuously inform and refine one another.

</details>

<details>
<summary><b>7. S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28649) • [📄 arXiv](https://arxiv.org/abs/2611.28649) • [📥 PDF](https://arxiv.org/pdf/2611.28649)

**💻 Code:** [⭐ Code](https://github.com/KANABOON1/S-Mind) • [⭐ Code](https://github.com/huggingface)

> Spatial intelligence, the ability to reason about 3D space from visual observations, becomes essential as multimodal large language models (MLLMs) move into the physical world. Beyond perceiving each view, it rests on two cornerstones of human cog...

</details>

<details>
<summary><b>8. PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement</b> ⭐ 30</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32554) • [📄 arXiv](https://arxiv.org/abs/2611.32554) • [📥 PDF](https://arxiv.org/pdf/2611.32554)

**💻 Code:** [⭐ Code](https://github.com/yangcaoai/PartAgent_Agent_for_3D_Part_Seg) • [⭐ Code](https://github.com/huggingface)

> We present PartAgent, a training-free agentic framework for 3D part segmentation built upon two complementary modules: (i) Structural–Semantic Expert Integration combines regions predicted by the 3D expert with multiview semantic evidence from the...

</details>

<details>
<summary><b>9. LingSante MedGuard Technical Report</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.25509) • [📄 arXiv](https://arxiv.org/abs/2611.25509) • [📥 PDF](https://arxiv.org/pdf/2611.25509)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/LingSante-MedGuard) • [⭐ Code](https://github.com/huggingface)

> We introduce LingSante MedGuard, a medical guardrail that reviews AI responses for safety, compliance, and ethics. It distills supervision from a medical guardrail teacher and six capability experts into a unified model. The 27B model achieves 87....

</details>

<details>
<summary><b>10. Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33010) • [📄 arXiv](https://arxiv.org/abs/2611.33010) • [📥 PDF](https://arxiv.org/pdf/2611.33010)

**💻 Code:** [⭐ Code](https://github.com/iPPLab/robodojo-mirror) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. ThinkMorph-SSL: Scaling Interleaved Multimodal Reasoning with Pretext Tasks</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Huichen Wang, Yunzhuo Hao, Yiming Liu, Linjie Li, Jiawei Gu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32183) • [📄 arXiv](https://arxiv.org/abs/2611.32183) • [📥 PDF](https://arxiv.org/pdf/2611.32183)

**💻 Code:** [⭐ Code](https://github.com/ThinkMorph/ThinkMorph-SSL) • [⭐ Code](https://github.com/huggingface)

> Models that reason with intermediate images are usually trained on traces built for one task family at a time. Self-supervised pretext tasks need no such traces, because the original image is the answer. ThinkMorph-SSL turns these tasks into inter...

</details>

<details>
<summary><b>12. KMed-31B Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.28719) • [📄 arXiv](https://arxiv.org/abs/2611.28719) • [📥 PDF](https://arxiv.org/pdf/2611.28719)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> KMed-31B is a medical LLM developed by the NAVER KMed team for on-premises deployment with limited hardware. The report introduces: • MOPD² (Multi-teacher On-policy Delta Distillation), extending OPD² to integrate task-specific specialists into a ...

</details>

<details>
<summary><b>13. Qwen-Image-HD: Autoregressive Diffusion for High Definition Image Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Donghao Zhou, Zikai Zhou, Shengming Yin, Zekai Zhang, Zihao Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32736) • [📄 arXiv](https://arxiv.org/abs/2611.32736) • [📥 PDF](https://arxiv.org/pdf/2611.32736)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds</b> ⭐ 10</summary>

<br/>

**👥 Authors:** Ruize Yang, Shenghan Zheng, Pei-lin Li, Jieming Li, Qingle Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32649) • [📄 arXiv](https://arxiv.org/abs/2611.32649) • [📥 PDF](https://arxiv.org/pdf/2611.32649)

**💻 Code:** [⭐ Code](https://github.com/ICLWorld/ICLWorld) • [⭐ Code](https://github.com/huggingface)

> Can an agent learn your rule from one demonstration, then follow it, on a computer and with a robot? 🤖 ICL benchmarks today are mostly offline, text or static images, and prone to contamination. Meanwhile robot agents increasingly rely on in-conte...

</details>

<details>
<summary><b>15. PhyCoVE: Benchmarking Physical Counterfactual Video Editing across Diverse Material Dynamics</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29184) • [📄 arXiv](https://arxiv.org/abs/2611.29184) • [📥 PDF](https://arxiv.org/pdf/2611.29184)

**💻 Code:** [⭐ Code](https://github.com/Hammour-steak/PhyCoVE) • [⭐ Code](https://github.com/huggingface)

> 🔥 Can video editing models understand physics? Remove a stone before it drops into a full glass of water, and the water should never overflow. Make it heavier, and the splash should grow. A physical edit changes not only how a scene looks, but how...

</details>

<details>
<summary><b>16. CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuki M. Asano, Tijmen Blankevoort, Dawid J. Kopiczko

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33148) • [📄 arXiv](https://arxiv.org/abs/2611.33148) • [📥 PDF](https://arxiv.org/pdf/2611.33148)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> .

</details>

<details>
<summary><b>17. Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30986) • [📄 arXiv](https://arxiv.org/abs/2611.30986) • [📥 PDF](https://arxiv.org/pdf/2611.30986)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Luo-Yihong/iTDM)

> Hi everyone! 👋 Excited to share our new work iTDM (Instantaneous Trajectory Distribution Matching) for reinforcing diffusion and flow-matching models! TL;DR: Existing forward diffusion RL methods (enabling fast deterministic ODE rollouts without t...

</details>

<details>
<summary><b>18. MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32462) • [📄 arXiv](https://arxiv.org/abs/2611.32462) • [📥 PDF](https://arxiv.org/pdf/2611.32462)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Paper link: https://arxiv.org/pdf/2611.32462

</details>

<details>
<summary><b>19. LeadVLA: Learning Follower-Aware Route Execution for Robot Leading</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zibo Zhang, Yuchen Zhou, Bingyi Xia, Hanjing Ye, Tianle Zeng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30149) • [📄 arXiv](https://arxiv.org/abs/2611.30149) • [📥 PDF](https://arxiv.org/pdf/2611.30149)

**💻 Code:** [⭐ Code](https://github.com/louiszengCN/LeadVLA_CODE) • [⭐ Code](https://github.com/huggingface)

> LeadVLA will be fully open-sourced! We'll gradually release our model checkpoints, code, and simulator. Stay tuned! 🚀 Follow our GitHub repo for updates: https://github.com/louiszengCN/LeadVLA_CODE For more DEMO, check our project page: https://lo...

</details>

<details>
<summary><b>20. RoomTokens: Masked Diffusion over Structured Tokens for Indoor Scene Synthesis</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30219) • [📄 arXiv](https://arxiv.org/abs/2611.30219) • [📥 PDF](https://arxiv.org/pdf/2611.30219)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/3dlg-hcvc/RoomToken)

> Our goal is to generate complete, physically plausible 3D indoor scenes from an architecture plan. MDiRT, our masked diffusion model, generates RoomTokens across height slices, with each token encoding semantic class, instance color, and facing. T...

</details>

<details>
<summary><b>21. Coding4Games: Can Modern Coding Agents Play Modern Video Games?</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31974) • [📄 arXiv](https://arxiv.org/abs/2611.31974) • [📥 PDF](https://arxiv.org/pdf/2611.31974)

**💻 Code:** [⭐ Code](https://github.com/GVCLab/Coding4Games) • [⭐ Code](https://github.com/huggingface)

> Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language ...

</details>

<details>
<summary><b>22. On-Policy Codec Distillation for Efficient All-in-One Video Generation</b> ⭐ 19</summary>

<br/>

**👥 Authors:** Zezhou Cheng, Matheus Gadelha, Oindrila Saha, Kevin Blackburn-Matzen, HikariDawn

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31184) • [📄 arXiv](https://arxiv.org/abs/2611.31184) • [📥 PDF](https://arxiv.org/pdf/2611.31184)

**💻 Code:** [⭐ Code](https://github.com/Kiteretsu77/CodecOPSD) • [⭐ Code](https://github.com/huggingface)

> Most condition tokens in video generation are redundant, and a video codec can tell where they are. 🚀 We are thrilled to introduce CodecOPSD, which drops 66% of them with almost no quality loss. ✅ Works on MiniMax-H3 Ref2VA, MiniMax-H3-Image, Cosm...

</details>

<details>
<summary><b>23. VenusOCR2.0: Towards Efficient and Effective Document Parsing</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32617) • [📄 arXiv](https://arxiv.org/abs/2611.32617) • [📥 PDF](https://arxiv.org/pdf/2611.32617)

**💻 Code:** [⭐ Code](https://github.com/flow3rdown/VenusOCR) • [⭐ Code](https://github.com/huggingface)

> https://github.com/flow3rdown/VenusOCR

</details>

<details>
<summary><b>24. SpecEngineeringBench: Evaluating Coding Agents as Autonomous Specification Engineers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32973) • [📄 arXiv](https://arxiv.org/abs/2611.32973) • [📥 PDF](https://arxiv.org/pdf/2611.32973)

**💻 Code:** [⭐ Code](https://github.com/TokenWave-AI/SpecEngineeringBench) • [⭐ Code](https://github.com/huggingface)

> We propose SpecEngineeringBench, a benchmark of 100 multi-defect instances across 78 Python repositories that evaluates coding agents on hint-free test generation and defect discovery. Evaluations of seven frontier agents show a stark disconnect b...

</details>

<details>
<summary><b>25. LoopDVR: Looped Transformer for Efficient Dense Visual Recognition</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32067) • [📄 arXiv](https://arxiv.org/abs/2611.32067) • [📥 PDF](https://arxiv.org/pdf/2611.32067)

**💻 Code:** [⭐ Code](https://github.com/Intellindust-AI-Lab/LoopDVR) • [⭐ Code](https://github.com/huggingface)

> Achieving exceptional parameter efficiency via looped Transformer.

</details>

<details>
<summary><b>26. Mega-MMDF and DeepfakeBench-MM: Benchmarking Multimodal Deepfake Detection Across Diverse Forgery Pipelines</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2510.22622) • [📄 arXiv](https://arxiv.org/abs/2510.22622) • [📥 PDF](https://arxiv.org/pdf/2510.22622)

**💻 Code:** [⭐ Code](https://github.com/SCLBD/DeepfakeBench-MM) • [⭐ Code](https://github.com/huggingface)

> We introduce a million-scale multimodal deepfake dataset and a benchmark for multimodal deepfake detection

</details>

<details>
<summary><b>27. Residual Guidance for Real-Time Interactive Video Generation</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32820) • [📄 arXiv](https://arxiv.org/abs/2611.32820) • [📥 PDF](https://arxiv.org/pdf/2611.32820)

**💻 Code:** [⭐ Code](https://github.com/nahyeonkaty/residual-guidance) • [⭐ Code](https://github.com/huggingface)

> Autoregressive video models often ignore a new prompt given mid-generation, as the cached context pulls the video back. Residual Guidance is a training-free, plug-and-play fix that makes the video follow the new prompt while staying continuous.

</details>

<details>
<summary><b>28. PINE: Point, Instance and Normal Estimation in One-Step Diffusion Model</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29389) • [📄 arXiv](https://arxiv.org/abs/2611.29389) • [📥 PDF](https://arxiv.org/pdf/2611.29389)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/PINE) • [⭐ Code](https://github.com/huggingface)

> 🚀 We release PINE, a one-step Omni Diffusion Transformer that jointly predicts the point map, surface normals, and instance map of an image in a single forward pass! 🧩 PINE integrates 3D geometry and semantics via token streams with stream masks, ...

</details>

<details>
<summary><b>29. Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31358) • [📄 arXiv](https://arxiv.org/abs/2611.31358) • [📥 PDF](https://arxiv.org/pdf/2611.31358)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce Nemotron-Labs-VisualCreation, an agentic framework that connects these capabilities through Pixel as Code. Image Generation Gal...

</details>

<details>
<summary><b>30. Separating Measurement Failures from Defence Failures in Split Language-Model Privacy</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31752) • [📄 arXiv](https://arxiv.org/abs/2611.31752) • [📥 PDF](https://arxiv.org/pdf/2611.31752)

**💻 Code:** [⭐ Code](https://github.com/setloop-io/Separating-Measurement-Failures-from-Defence-Failures-in-Split-Language-Model-Privacy) • [⭐ Code](https://github.com/huggingface)

> Split-training privacy evaluations fail through distinct mechanisms. Evaluators can overlook an exposed gradient channel, align reconstructions against shifted labels, or deploy uncalibrated probes before testing a candidate defence, while calibra...

</details>

<details>
<summary><b>31. AdProducer: Towards Agentic Advertising Video Generation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31466) • [📄 arXiv](https://arxiv.org/abs/2611.31466) • [📥 PDF](https://arxiv.org/pdf/2611.31466)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lky-ang/AdProducer)

> Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelli...

</details>

<details>
<summary><b>32. Clinical3D-Bench: Evaluating and Improving Spatial Intelligence of Multimodal LLMs in Hospital Environments</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32094) • [📄 arXiv](https://arxiv.org/abs/2611.32094) • [📥 PDF](https://arxiv.org/pdf/2611.32094)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Clinical3D-Bench tests whether MLLMs can reason about 3D space in hospital rooms: 3,368 multiple-choice questions on 569 photorealistic walkthrough clips across 8 question types, with exact answers computed from the 3D scenes and per-frame instanc...

</details>

<details>
<summary><b>33. LoopedWAM: Looped World Action Models for Elastic Inference</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.25595) • [📄 arXiv](https://arxiv.org/abs/2611.25595) • [📥 PDF](https://arxiv.org/pdf/2611.25595)

**💻 Code:** [⭐ Code](https://github.com/anhdao69/LoopedWAM) • [⭐ Code](https://github.com/huggingface)

> TL;DR: LoopedWAM is a 0.58B world action model that loops a shared 6-block core, running 30 layers from 12 stored blocks. No robot pretraining: 96.1% LIBERO, 91.9% RoboTwin 2.0, 7.4× less GPU memory than Fast-WAM. One checkpoint (LoopedWAM-E) lets...

</details>

<details>
<summary><b>34. Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models with Adjustable Depth</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31977) • [📄 arXiv](https://arxiv.org/abs/2611.31977) • [📥 PDF](https://arxiv.org/pdf/2611.31977)

**💻 Code:** [⭐ Code](https://github.com/WinterCCC/Distill-to-Loop) • [⭐ Code](https://github.com/huggingface)

> Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models with Adjustable Depth

</details>

<details>
<summary><b>35. GRAPE-Bench: When Vision Degrades, Does Video Reasoning Hold?</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jianshu Zhang, Jinxi He, Tianshi Ming, Junyi He, Ce Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.33020) • [📄 arXiv](https://arxiv.org/abs/2611.33020) • [📥 PDF](https://arxiv.org/pdf/2611.33020)

**💻 Code:** [⭐ Code](https://github.com/zhangce01/GRAPE-Bench) • [⭐ Code](https://github.com/huggingface)

> 🍇 GRAPE-Bench tests whether video reasoning holds when vision degrades: 🌧️ 12 synthetic corruptions plus real driving footage at night and in rain, snow and fog, ❓ three questions per video from a safety-relevant basic judgment to a hard reasoning...

</details>

<details>
<summary><b>36. Do learned image captioning metrics generalize? Auditing duplicated samples in human-judgment benchmarks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Longjiang Guo, Chunlong Xia, Jin Li, hutmorning

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30488) • [📄 arXiv](https://arxiv.org/abs/2611.30488) • [📥 PDF](https://arxiv.org/pdf/2611.30488)

**💻 Code:** [⭐ Code](https://github.com/morninghut/ic-dataset-audit) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We're excited to share our recent work: Do Learned Image Captioning Metrics Generalize? Auditing Duplicated Samples in Human-Judgment Benchmarks How reliable are the reported gains of learned image captioning metrics? To find out, we ...

</details>

<details>
<summary><b>37. Interpretable Prototype-Conditioned Adaptation for Weather Forecasting</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.25848) • [📄 arXiv](https://arxiv.org/abs/2611.25848) • [📥 PDF](https://arxiv.org/pdf/2611.25848)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project page: https://zhixuanli.github.io/projects/li2026protocast

</details>

<details>
<summary><b>38. Can an Agent Trust Its Own Zoom? Cross-Magnification Provenance Verification for Whole-Slide Images</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhongxing Xu, Jianxiang Qi, Zizhuo Gong, Yiran Song, Yan Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29150) • [📄 arXiv](https://arxiv.org/abs/2611.29150) • [📥 PDF](https://arxiv.org/pdf/2611.29150)

**💻 Code:** [⭐ Code](https://github.com/Yan2266336/PyraFault) • [⭐ Code](https://github.com/huggingface)

> Visual agents navigate whole-slide images through magnified observations associated with claimed locations. However, a visually plausible observation does not necessarily originate from its claimed location, particularly across magnifications and ...

</details>

<details>
<summary><b>39. SpatialArena: Where Do Geometric Foundation Models Stand?</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Jifei Song, Zhensong Zhang, Su Ee Tan, Haosen Yang, Yu Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32816) • [📄 arXiv](https://arxiv.org/abs/2611.32816) • [📥 PDF](https://arxiv.org/pdf/2611.32816)

**💻 Code:** [⭐ Code](https://github.com/mvp-ai-lab/SpatialArena) • [⭐ Code](https://github.com/huggingface)

> GitHub: https://github.com/mvp-ai-lab/SpatialArena Project Page: https://mvp-ai-lab.github.io/SpatialArena/ Dataset: https://huggingface.co/datasets/mvp-lab/SpatialArena-Dataset

</details>

<details>
<summary><b>40. Measuring Layer-wise Intrinsic Dimensionality of FFNs in LLMs via PCA</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Daehee Kim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32782) • [📄 arXiv](https://arxiv.org/abs/2611.32782) • [📥 PDF](https://arxiv.org/pdf/2611.32782)

**💻 Code:** [⭐ Code](https://github.com/naver-ai/lidf) • [⭐ Code](https://github.com/huggingface)

> NeurIPS 2026 poster. We measure the intrinsic dimensionality of each FFN layer with PCA, using a single forward pass on unlabeled text. Across 58 open-weight LLMs, middle layers tend to have higher intrinsic dimensionality than edge layers. As a f...

</details>

<details>
<summary><b>41. Factorized Context Attention: From Emulated to Native Grid Probing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32423) • [📄 arXiv](https://arxiv.org/abs/2611.32423) • [📥 PDF](https://arxiv.org/pdf/2611.32423)

**💻 Code:** [⭐ Code](https://github.com/mohammad2012191/FCA) • [⭐ Code](https://github.com/huggingface)

> Grid probing is attention in disguise, so we run it inside the model. Encode a book or an hour of video once, then answer each new question in as little as a tenth of the time. Training-free, frozen models.

</details>

<details>
<summary><b>42. Align the Pair, Not the Sample: Representation Alignment for Faster and Better One-Step Generato</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Han Zhang, Aoran Wang, Encheng Su, Xuantuo Huang, Mingxiao Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29547) • [📄 arXiv](https://arxiv.org/abs/2611.29547) • [📥 PDF](https://arxiv.org/pdf/2611.29547)

**💻 Code:** [⭐ Code](https://github.com/Mingxiao-Li/RePrime) • [⭐ Code](https://github.com/huggingface)

> One-step generation is fast at inference — but painfully slow to train. We found a placement for REPA that cuts Priming's training by 2× and its OT post-training by 4×, while improving FID. Meet RePrime.

</details>

<details>
<summary><b>43. Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription of Handwritten Portuguese Essays</b> ⭐ 1</summary>

<br/>

**👥 Authors:** tardellirs

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.29874) • [📄 arXiv](https://arxiv.org/abs/2611.29874) • [📥 PDF](https://arxiv.org/pdf/2611.29874)

**💻 Code:** [⭐ Code](https://github.com/tardellirs/escriba-ocr) • [⭐ Code](https://github.com/tardellirs/escriba-ocr/blob/main/bench/token_types.py) • [⭐ Code](https://github.com/huggingface)

> Escriba-OCR-1B is a 1B-parameter OCR model that transcribes handwritten Brazilian Portuguese essays exactly as the student wrote them: misspellings, line breaks, struck-through words and insertions included. Feedback tools and research on learner ...

</details>

<details>
<summary><b>44. FATCAT: Fault Injection Attacks Targeting Chip-level Alignment</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Lejla Batina, Lukasz Chmielewski, Zhuoran Liu, Ilia Shumailov, Peter Horvath

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31129) • [📄 arXiv](https://arxiv.org/abs/2611.31129) • [📥 PDF](https://arxiv.org/pdf/2611.31129)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Turns out you can break alignment of a robot by zapping the accelerator, huh??

</details>

<details>
<summary><b>45. InstructReplay: Replaying Assistant Turns to Preserve General Behavior During Factual Fine-Tuning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32918) • [📄 arXiv](https://arxiv.org/abs/2611.32918) • [📥 PDF](https://arxiv.org/pdf/2611.32918)

**💻 Code:** [⭐ Code](https://github.com/xiaofengShi/InstructReplay) • [⭐ Code](https://github.com/huggingface)

> Fine-tuning an instruction-tuned language model on new facts often erodes its general abilities. We find that standard fine-tuning lowers instruction-following, reasoning and coding benchmarks by 35 points on average, and that these losses track a...

</details>

<details>
<summary><b>46. RECAP: Training Long-horizon LLM Agents with Context Compaction</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Michael Moor, Maria Brbic, Yulun Jiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31258) • [📄 arXiv](https://arxiv.org/abs/2611.31258) • [📥 PDF](https://arxiv.org/pdf/2611.31258)

**💻 Code:** [⭐ Code](https://github.com/eth-medical-ai-lab/recap) • [⭐ Code](https://github.com/huggingface)

> How can we train AI agents to solve long-horizon tasks with limited context? We introduce RECAP🎞️, an RL recipe for training long-horizon agents with context compaction. The central idea is simple: a good summary should preserve the agent’s behavi...

</details>

<details>
<summary><b>47. Foresight Forcing: Learning Spatial Foresight for Robotic Manipulation</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Jiarui Chen, Wendi Chen, Zhaoyuan Wan, Zhixuan Liang, anson233

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.30963) • [📄 arXiv](https://arxiv.org/abs/2611.30963) • [📥 PDF](https://arxiv.org/pdf/2611.30963)

**💻 Code:** [⭐ Code](https://github.com/anson2333/ForesightForcing) • [⭐ Code](https://github.com/huggingface)

> Foresight Forcing learns action-relevant spatial transition representations via a frozen 3D foundation model, and predicts them at inference without future observations or the 3D teacher. It achieves SOTA on RoboTwin 2.0 Full (95.01%) and outperfo...

</details>

<details>
<summary><b>48. Small Learned Projections for Semantic-Reversal-Aware Retrieval with Spectral Acceleration: A Four-Domain Empirical Study</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31442) • [📄 arXiv](https://arxiv.org/abs/2611.31442) • [📥 PDF](https://arxiv.org/pdf/2611.31442)

**💻 Code:** [⭐ Code](https://github.com/pelloran-inc/pelloran-safety-lens) • [⭐ Code](https://github.com/huggingface)

> Dense retrievers fail adversarially: swap a document A for a near-copy B that differs by one small meaning-changing edit (a "trap"), and raw cosine over E5-Large-v2 ranks the trap in the top-10 for 82–100% of queries at a 5,000-pool. We show a sma...

</details>

<details>
<summary><b>49. ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32639) • [📄 arXiv](https://arxiv.org/abs/2611.32639) • [📥 PDF](https://arxiv.org/pdf/2611.32639)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ReFocus-Robotics/ReFocus)

> Online reinforcement learning (RL) enables vision-language-action policies to improve through environmental interaction. However, in long-horizon manipulation, sparse success/failure feedback provides little information about where policies encoun...

</details>

<details>
<summary><b>50. RoMo Hands: A Large Scale Richly Organized Text to Hand Motion Dataset</b> ⭐ 27</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.31766) • [📄 arXiv](https://arxiv.org/abs/2611.31766) • [📥 PDF](https://arxiv.org/pdf/2611.31766)

**💻 Code:** [⭐ Code](https://github.com/RoMoDataset/motion-toolbox) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We're excited to share RoMo Hands (NeurIPS 2026) — a large-scale, text-paired 3D bimanual hand motion dataset and benchmark. Highlights: Scale: 541,929 in-the-wild bimanual MANO sequences ( 884 hours , 95.5M frames at 30 fps) — >10× l...

</details>

<details>
<summary><b>51. EEGJev: A System One Decision Model and Benchmark for Multi-Task EEG Question Answering</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Kazunori D. Yamada, dengzhe-hou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.32100) • [📄 arXiv](https://arxiv.org/abs/2611.32100) • [📥 PDF](https://arxiv.org/pdf/2611.32100)

**💻 Code:** [⭐ Code](https://github.com/dengzhe-hou/EEGJev) • [⭐ Code](https://github.com/huggingface)

> We introduce EEGJev, a decision model that uses EEG and a question to score candidate answers in one pass, and EEGJev-Bench, which covers six question types across 19 public EEG sources. The benchmark includes paired questions on the same recordin...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 51 |
| 📅 Today | [`2026-11-25.json`](data/daily/2026-11-25.json) | 51 |
| 📆 This Week | [`2026-W47.json`](data/weekly/2026-W47.json) | 131 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 862 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-25 | 51 | [View JSON](data/daily/2026-11-25.json) |
| 📄 2026-11-24 | 60 | [View JSON](data/daily/2026-11-24.json) |
| 📄 2026-11-23 | 20 | [View JSON](data/daily/2026-11-23.json) |
| 📄 2026-11-22 | 50 | [View JSON](data/daily/2026-11-22.json) |
| 📄 2026-11-21 | 50 | [View JSON](data/daily/2026-11-21.json) |
| 📄 2026-11-20 | 39 | [View JSON](data/daily/2026-11-20.json) |
| 📄 2026-11-19 | 43 | [View JSON](data/daily/2026-11-19.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W47 | 131 | [View JSON](data/weekly/2026-W47.json) |
| 📅 2026-W46 | 268 | [View JSON](data/weekly/2026-W46.json) |
| 📅 2026-W45 | 193 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 862 | [View JSON](data/monthly/2026-11.json) |
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
