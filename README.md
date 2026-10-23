<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-36-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9113+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">36</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">235</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1352</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9113+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 23, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30926) • [📄 arXiv](https://arxiv.org/abs/2610.30926) • [📥 PDF](https://arxiv.org/pdf/2610.30926)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Songlin1998/ShotVerse2.0)

> Cinematic video generation requires both temporal inference from limited inputs (i.e., sparse rather than frame-by-frame guidance) and factor-aware control of character, scene, action, and camera. Multimodal large language models (MLLMs) offer use...

</details>

<details>
<summary><b>2. Deep Search in Real-World Web Environments</b> ⭐ 14</summary>

<br/>

**👥 Authors:** Shao-Rong Su, Shilin Yan, Zhe Huang, Xiaomin Yu, hchen272

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30181) • [📄 arXiv](https://arxiv.org/abs/2610.30181) • [📥 PDF](https://arxiv.org/pdf/2610.30181)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yu-xm/OpenDS)

> Deep Search in the Real-World Web Environments

</details>

<details>
<summary><b>3. Editing Images into Reusable Layers via Compositional Edit-Prior Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24738) • [📄 arXiv](https://arxiv.org/abs/2610.24738) • [📥 PDF](https://arxiv.org/pdf/2610.24738)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce LayerEditor , a unified framework that couples instruction-guided image editing with controllable generation of reusable RGBA layers. Given a source image, an editing instruction, and a requested layer count, LayerEditor jointly gener...

</details>

<details>
<summary><b>4. WeVisOne-VL: Unified Visual Perception from Objects to Pixels</b> ⭐ 44</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31329) • [📄 arXiv](https://arxiv.org/abs/2610.31329) • [📥 PDF](https://arxiv.org/pdf/2610.31329)

**💻 Code:** [⭐ Code](https://github.com/Tencent/WeVisOne-VL) • [⭐ Code](https://github.com/huggingface)

> We present WeVisOne-VL (WeChat Vision All-in-One), a powerful VLM that unifies object-level and pixel-level perception through structured next-token prediction. Github: https://github.com/Tencent/WeVisOne-VL Model: https://huggingface.co/collectio...

</details>

<details>
<summary><b>5. Toward Recursive Self-Improvement in Physical AI</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.29677) • [📄 arXiv](https://arxiv.org/abs/2610.29677) • [📥 PDF](https://arxiv.org/pdf/2610.29677)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Physical2RSI/Awesome-Physical2RSI)

> Toward Recursive Self-Improvement in Physical AI Recursive self-improvement (RSI) asks for more than a better robot: the process that produces improvements should itself get better. Digital agents already rewrite their own code and check each vers...

</details>

<details>
<summary><b>6. IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30949) • [📄 arXiv](https://arxiv.org/abs/2610.30949) • [📥 PDF](https://arxiv.org/pdf/2610.30949)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems

</details>

<details>
<summary><b>7. Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiang Shi, Yuliang Liu, Hao Sun, Siyuan Sun, Rubin-Wei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25100) • [📄 arXiv](https://arxiv.org/abs/2610.25100) • [📥 PDF](https://arxiv.org/pdf/2610.25100)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Deep Fusion Memory (DFM) , a chunk-level parametric memory architecture that enables LLMs to incorporate external knowledge without retrieval at inference time. DFM introduces two key ideas: Efficient memory construction: A causal mem...

</details>

<details>
<summary><b>8. LaLa-World: Scaling Latent World Models with Natural Language Actions</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27851) • [📄 arXiv](https://arxiv.org/abs/2610.27851) • [📥 PDF](https://arxiv.org/pdf/2610.27851)

**💻 Code:** [⭐ Code](https://github.com/junha1125/LaLa-World) • [⭐ Code](https://github.com/huggingface)

> TL;DR A La nguage-conditioned La tent World model ( LaLa-World ) uses natural language as a shared action interface to learn from simulation, robotics, images, and videos. It predicts future visual representations for efficient planning across dom...

</details>

<details>
<summary><b>9. What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Zhiheng Liu, Zecong Tang, Weitong Lian, kaixuanwang, Lruca

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23987) • [📄 arXiv](https://arxiv.org/abs/2610.23987) • [📥 PDF](https://arxiv.org/pdf/2610.23987)

**💻 Code:** [⭐ Code](https://github.com/LRuca/GAFU) • [⭐ Code](https://github.com/huggingface)

> 🚀 We are excited to share our latest work: "What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal Models" ! Unified multimodal models (UMMs) can generate images with rich visual details. But can the internal representat...

</details>

<details>
<summary><b>10. Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient MoE</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27598) • [📄 arXiv](https://arxiv.org/abs/2610.27598) • [📥 PDF](https://arxiv.org/pdf/2610.27598)

**💻 Code:** [⭐ Code](https://github.com/InternLM/Intern-S2-Mobius) • [⭐ Code](https://github.com/huggingface)

> A comparison between the Vanilla and Meta-Expert models shows that, when trained under the optimal settings of the Vanilla model at varying depths and scales, models with Meta Experts achieve loss comparable to the Vanilla baselines while using on...

</details>

<details>
<summary><b>11. Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26233) • [📄 arXiv](https://arxiv.org/abs/2610.26233) • [📥 PDF](https://arxiv.org/pdf/2610.26233)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Tool-using voice agents often leave users waiting after speech ends, even when actionable information arrives earlier in the request. Speculative approaches begin work during speech, but chunk-bounded or interrupt-on-update generation can truncate...

</details>

<details>
<summary><b>12. Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28416) • [📄 arXiv](https://arxiv.org/abs/2610.28416) • [📥 PDF](https://arxiv.org/pdf/2610.28416)

**💻 Code:** [⭐ Code](https://github.com/code2video-compass/Code2Video-Compass) • [⭐ Code](https://github.com/huggingface)

> We introduce Code2Video-Compass, a comprehensive benchmark for general-purpose code-based video generation across text-to-video, image-to-video, and video-to-video settings. The benchmark comprises 2,104 tasks spanning 10 categories and 24 subtype...

</details>

<details>
<summary><b>13. Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic Compression and Balanced Discrete Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31305) • [📄 arXiv](https://arxiv.org/abs/2610.31305) • [📥 PDF](https://arxiv.org/pdf/2610.31305)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! We’re excited to share Cola2, a follow-up to Cola that combines dynamic semantic compression with joint learning of continuous representations and discrete text generation. With a Qwen-initialized decoder, Cola2 surpasses Llama-3-8B o...

</details>

<details>
<summary><b>14. RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Minseong Bae, Sehyung Kim, Jihwan Park, Minseok Joo, Injae Kim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27712) • [📄 arXiv](https://arxiv.org/abs/2610.27712) • [📥 PDF](https://arxiv.org/pdf/2610.27712)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mlvlab/RLSplat)

> We present RLSplat , a feed-forward 3D Gaussian Splatting method that enables resource-aware inference through direct Gaussian budget control. By generating exactly the requested number of Gaussians, RLSplat allows users to adapt inference cost to...

</details>

<details>
<summary><b>15. RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19705) • [📄 arXiv](https://arxiv.org/abs/2610.19705) • [📥 PDF](https://arxiv.org/pdf/2610.19705)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LaughKing/RouteWeaver)

> LLM routing dynamically selects and coordinates heterogeneous language models across diverse tasks. However, existing approaches are largely built around a predefined execution paradigm, such as single-round, multi-round, or agentic routing, which...

</details>

<details>
<summary><b>16. Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Aibek Alanov, maksim64, Ivan1008

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.28889) • [📄 arXiv](https://arxiv.org/abs/2610.28889) • [📥 PDF](https://arxiv.org/pdf/2610.28889)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TLDR: Policy-Mask trains a REINFORCE policy that jointly picks the timestep, layer, and exactly b channels of a frozen diffusion model, then distills the selected features into a student that runs without the teacher. At 128 of 1280 channels, it b...

</details>

<details>
<summary><b>17. Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31158) • [📄 arXiv](https://arxiv.org/abs/2610.31158) • [📥 PDF](https://arxiv.org/pdf/2610.31158)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/marinero4972/OmniDR-Bench)

> OmniDR-Bench

</details>

<details>
<summary><b>18. Self-Distilling Future Video Representations for World Action Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30320) • [📄 arXiv](https://arxiv.org/abs/2610.30320) • [📥 PDF](https://arxiv.org/pdf/2610.30320)

**💻 Code:** [⭐ Code](https://github.com/suhyeok-jang/FRED) • [⭐ Code](https://github.com/huggingface)

> We introduce FRED , a framework that trains World Action Models (WAMs) to generate better future video representations in a single denoising step, by self-distilling from noisy ground-truth futures and conditioning on short history observations. F...

</details>

<details>
<summary><b>19. Verus-Insight: Towards Explainable Artifact Detection in AI-Generated Videos</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yuqi Tang, Tengfei Liu, Qixun Wang, Zhuoran Zhang, DogNeverSleep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30866) • [📄 arXiv](https://arxiv.org/abs/2610.30866) • [📥 PDF](https://arxiv.org/pdf/2610.30866)

**💻 Code:** [⭐ Code](https://github.com/zhangzhuoran997997/Verus-Insight) • [⭐ Code](https://github.com/huggingface)

> Recent advances in video generation have made synthetic videos increasingly realistic, placing greater demands on reliable AI-generated video detection. Existing artifact-based detectors typically identify generation artifacts as evidence for sour...

</details>

<details>
<summary><b>20. Rethinking Sequence Compression with Test-time Regression</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31574) • [📄 arXiv](https://arxiv.org/abs/2610.31574) • [📥 PDF](https://arxiv.org/pdf/2610.31574)

**💻 Code:** [⭐ Code](https://github.com/Sphere-AI-Lab/ttr-compressor) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We introduce TTR-Compressor, a superior and fully practical alternative to standard pooling and projection-based compression. It shows strong empirical gains both as a compressor for block-wise sparse attention in efficient LLMs and a...

</details>

<details>
<summary><b>21. Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30755) • [📄 arXiv](https://arxiv.org/abs/2610.30755) • [📥 PDF](https://arxiv.org/pdf/2610.30755)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Litmeb/RAW-RAG)

> RAW-RAG challenges the necessity of complex agentic memory for long-term conversation understanding. By combining dense retrieval and reranking over raw history, it ranks first among compared memory systems in six of seven settings across four ben...

</details>

<details>
<summary><b>22. RTAformer: Relation-Transition-Aware Transformer for Video Scene Graph Generation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yukyung Choi, Geuntaek Lim, HeoJaeYeon

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20091) • [📄 arXiv](https://arxiv.org/abs/2610.20091) • [📥 PDF](https://arxiv.org/pdf/2610.20091)

**💻 Code:** [⭐ Code](https://github.com/sejong-rcv/RTAformer) • [⭐ Code](https://github.com/huggingface)

> We introduce RTAformer , accepted at ACCV 2026, for Video Scene Graph Generation (VidSGG). Existing temporal models often retain outdated relation predictions even after the underlying relationships change. We identify this failure mode as Relatio...

</details>

<details>
<summary><b>23. AgentVQA: A Unified Benchmark for Agentic Visual Understanding</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31494) • [📄 arXiv](https://arxiv.org/abs/2610.31494) • [📥 PDF](https://arxiv.org/pdf/2610.31494)

**💻 Code:** [⭐ Code](https://github.com/zlab-princeton/AgentVQA) • [⭐ Code](https://github.com/huggingface)

> AgentVQA is an offline benchmark for evaluating visual understanding in realistic agentic scenarios, without the cost of running agents in interactive environments. It brings together 1,000 human-verified examples from 23 datasets across five doma...

</details>

<details>
<summary><b>24. AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31466) • [📄 arXiv](https://arxiv.org/abs/2610.31466) • [📥 PDF](https://arxiv.org/pdf/2610.31466)

**💻 Code:** [⭐ Code](https://github.com/AlayaLab/AnyGameRenderer) • [⭐ Code](https://github.com/huggingface)

> AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative render...

</details>

<details>
<summary><b>25. MolLean: A Process-Verifiable Language for Chemical Reasoning</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Yatao Bian, phenixace

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20459) • [📄 arXiv](https://arxiv.org/abs/2610.20459) • [📥 PDF](https://arxiv.org/pdf/2610.20459)

**💻 Code:** [⭐ Code](https://github.com/phenixace/Open-MolLean) • [⭐ Code](https://github.com/huggingface)

> MolLean turns chemical reasoning into executable, checked steps. Direct chain-of-thought can miscount atoms, invent functional groups, or claim a property improved without measuring it. MolLean ties declared edits and claims to an explicit molecul...

</details>

<details>
<summary><b>26. F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31623) • [📄 arXiv](https://arxiv.org/abs/2610.31623) • [📥 PDF](https://arxiv.org/pdf/2610.31623)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jrryzh/F2G-Pose)

> We’re sharing F2G-Pose, accepted at NeurIPS 2026! From a single segmented RGB-D observation, it predicts category-level 6D object pose, metric size, and a completed shape in the camera frame in one forward pass. It lifts frozen foundation visual f...

</details>

<details>
<summary><b>27. Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30882) • [📄 arXiv](https://arxiv.org/abs/2610.30882) • [📥 PDF](https://arxiv.org/pdf/2610.30882)

**💻 Code:** [⭐ Code](https://github.com/kouzhizhuo/wait-provenance) • [⭐ Code](https://github.com/huggingface)

> Reinforcement learning (RL) is credited with teaching reasoning models to write {wait} before reconsidering a step, yet large RL accuracy gains do not require the word. This view can confuse what RL discovers with what a model inherits from its tr...

</details>

<details>
<summary><b>28. SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31062) • [📄 arXiv](https://arxiv.org/abs/2610.31062) • [📥 PDF](https://arxiv.org/pdf/2610.31062)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Dataset: https://huggingface.co/datasets/Plurai/SCOPE

</details>

<details>
<summary><b>29. Reading, Writing, Sharing, and Interacting with the World through Video</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shuicheng Yan, Ziwei Liu, Bobo Li, Meng Luo, Shengqiong Wu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31668) • [📄 arXiv](https://arxiv.org/abs/2610.31668) • [📥 PDF](https://arxiv.org/pdf/2610.31668)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>30. What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31576) • [📄 arXiv](https://arxiv.org/abs/2610.31576) • [📥 PDF](https://arxiv.org/pdf/2610.31576)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> .

</details>

<details>
<summary><b>31. TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25376) • [📄 arXiv](https://arxiv.org/abs/2610.25376) • [📥 PDF](https://arxiv.org/pdf/2610.25376)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/hku-sail/TILDE)

> Can we transfer the capabilities of pretrained embodied foundation models without repeating expensive action pretraining? TILDE addresses this challenge by distilling teacher knowledge across demonstrations, student-induced rollouts, and teacher-e...

</details>

<details>
<summary><b>32. SEAM: Spectral Embedding Alignment and Merging for Low-Resource TTS</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26252) • [📄 arXiv](https://arxiv.org/abs/2610.26252) • [📥 PDF](https://arxiv.org/pdf/2610.26252)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Train a TTS with less Data.

</details>

<details>
<summary><b>33. Skeleton-Grounded Latent Action Model for Robot World Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiang Deng, Jianzong Wang, Yuxin Jiang, Jiayi Lin, Qi Lv

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31474) • [📄 arXiv](https://arxiv.org/abs/2610.31474) • [📥 PDF](https://arxiv.org/pdf/2610.31474)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> SkeLAM learns structured latent actions from visual transitions with skeleton supervision, separating robot motion from complementary visual changes. This structure supports action-conditioned world modeling and robot action adaptation through a s...

</details>

<details>
<summary><b>34. Foundation4D: Towards a unified perception and reconstruction model for autonomous vehicles</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30340) • [📄 arXiv](https://arxiv.org/abs/2610.30340) • [📥 PDF](https://arxiv.org/pdf/2610.30340)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>35. SplatLab: Autonomous Scientific Discovery for 3DGS Research</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30468) • [📄 arXiv](https://arxiv.org/abs/2610.30468) • [📥 PDF](https://arxiv.org/pdf/2610.30468)

**💻 Code:** [⭐ Code](https://github.com/seemandhar/SplatLab) • [⭐ Code](https://github.com/huggingface)

> What if AI could actually do scientific research, not just generate ideas or write papers? Excited to share SplatLab (NeurIPS 2026) , an autonomous AI scientist for 3D Gaussian Splatting (3DGS). Starting from a single prompt (or no prompt at all) ...

</details>

<details>
<summary><b>36. MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22951) • [📄 arXiv](https://arxiv.org/abs/2610.22951) • [📥 PDF](https://arxiv.org/pdf/2610.22951)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/giakhuyendihoc/MambaAct)

> Hi everyone! 👋 We're excited to share MambaAct , an efficient action expert for flow-matching VLAs. Flow-matching VLAs like π0.5 run their action expert many times during denoising, which makes inference a bottleneck for real-time control. MambaAc...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 36 |
| 📅 Today | [`2026-10-23.json`](data/daily/2026-10-23.json) | 36 |
| 📆 This Week | [`2026-W42.json`](data/weekly/2026-W42.json) | 235 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1352 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-23 | 36 | [View JSON](data/daily/2026-10-23.json) |
| 📄 2026-10-22 | 41 | [View JSON](data/daily/2026-10-22.json) |
| 📄 2026-10-21 | 49 | [View JSON](data/daily/2026-10-21.json) |
| 📄 2026-10-20 | 55 | [View JSON](data/daily/2026-10-20.json) |
| 📄 2026-10-19 | 54 | [View JSON](data/daily/2026-10-19.json) |
| 📄 2026-10-18 | 84 | [View JSON](data/daily/2026-10-18.json) |
| 📄 2026-10-17 | 84 | [View JSON](data/daily/2026-10-17.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W42 | 235 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1352 | [View JSON](data/monthly/2026-10.json) |
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
