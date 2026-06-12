<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-35-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5204+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">35</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">159</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">382</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5204+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 12, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13681) • [📄 arXiv](https://arxiv.org/abs/2606.13681) • [📥 PDF](https://arxiv.org/pdf/2606.13681)

**💻 Code:** [⭐ Code](https://github.com/Aiden0526/EvoArena) • [⭐ Code](https://github.com/huggingface)

> Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align thei...

</details>

<details>
<summary><b>2. InterleaveThinker: Reinforcing Agentic Interleaved Generation</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Zoey Guo, Kaituo Feng, Manyuan Zhang, Harry Lee, Dian Zheng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13679) • [📄 arXiv](https://arxiv.org/abs/2606.13679) • [📥 PDF](https://arxiv.org/pdf/2606.13679)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhengdian1/InterleaveThinker)

> hf: https://huggingface.co/InterleaveThinker

</details>

<details>
<summary><b>3. SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13673) • [📄 arXiv](https://arxiv.org/abs/2606.13673) • [📥 PDF](https://arxiv.org/pdf/2606.13673)

**💻 Code:** [⭐ Code](https://github.com/NVlabs/SpatialClaw) • [⭐ Code](https://github.com/huggingface)

> "Code is the right action interface for spatial reasoning!!" SpatialClaw lets a VLM-backed agent write Python in a persistent kernel, composing perception modules, inspecting intermediate results, and revising its strategy across steps. It is trai...

</details>

<details>
<summary><b>4. MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13473) • [📄 arXiv](https://arxiv.org/abs/2606.13473) • [📥 PDF](https://arxiv.org/pdf/2606.13473)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>5. WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces</b> ⭐ 30</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09426) • [📄 arXiv](https://arxiv.org/abs/2606.09426) • [📥 PDF](https://arxiv.org/pdf/2606.09426)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/weavebench/WeaveBench)

> We introduce WeaveBench, a long-horizon benchmark with 114 tasks across 8 real-world domains, where agents must interleave GUI and CLI/code operations in a single trajectory on a real Ubuntu desktop. The best frontier model reaches only 41.2% Pass...

</details>

<details>
<summary><b>6. MiniMax Sparse Attention</b> ⭐ 145</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13392) • [📄 arXiv](https://arxiv.org/abs/2606.13392) • [📥 PDF](https://arxiv.org/pdf/2606.13392)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MiniMax-AI/MSA)

> our high-performance MSA kernel library is now open-source

</details>

<details>
<summary><b>7. FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Shuo Tang, Xiaoqing Xiang, Yimeng Chen, Jia Deng, ziyang1060

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12087) • [📄 arXiv](https://arxiv.org/abs/2606.12087) • [📥 PDF](https://arxiv.org/pdf/2606.12087)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RUCAIBox/FORT-Searcher)

> Training deep search agents requires verifiable questions whose answers remain unavailable until sufficient evidence has been acquired through search. Existing synthesis methods often increase apparent difficulty by enriching graph structures, but...

</details>

<details>
<summary><b>8. LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories</b> ⭐ 39</summary>

<br/>

**👥 Authors:** Yanshuo Liu, Xi Chen, Xinjie Liu, Baochang Ren, Ningyu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13578) • [📄 arXiv](https://arxiv.org/abs/2606.13578) • [📥 PDF](https://arxiv.org/pdf/2606.13578)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zjunlp/LabVLA)

> No abstract available.

</details>

<details>
<summary><b>9. Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Runtao Liu, Wei Wei, Youyang Zhai, Jianmin Chen, Jiaqi-hkust

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08063) • [📄 arXiv](https://arxiv.org/abs/2606.08063) • [📥 PDF](https://arxiv.org/pdf/2606.08063)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jqtangust/Robust-U1)

> Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in visual understanding, yet their performance degrades significantly under real-world visual corruptions. While existing robustness enhancement approaches exist, they a...

</details>

<details>
<summary><b>10. HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13289) • [📄 arXiv](https://arxiv.org/abs/2606.13289) • [📥 PDF](https://arxiv.org/pdf/2606.13289)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🔱 Meet HYDRA-X — a 7B native unified multimodal model where one ViT-based tokenizer drives 5 tasks: image/video understanding, image/video generation, and image editing. Three core contributions: 🎯 Less attention is more. Local causal tubelet atte...

</details>

<details>
<summary><b>11. N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Linchao Zhu, Peng Di, Hang Yu, Xukun Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10768) • [📄 arXiv](https://arxiv.org/abs/2606.10768) • [📥 PDF](https://arxiv.org/pdf/2606.10768)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJUSCL/N-GRPO)

> N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization Github: https://github.com/ZJUSCL/N-GRPO

</details>

<details>
<summary><b>12. EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13662) • [📄 arXiv](https://arxiv.org/abs/2606.13662) • [📥 PDF](https://arxiv.org/pdf/2606.13662)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/THU-Team-Eureka/EurekAgent)

> As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent b...

</details>

<details>
<summary><b>13. VIA-SD: Verification via Intra-Model Routing for Speculative Decoding</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yi Yang, Yunqiu Xu, Yang He, Yuchen Xian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12243) • [📄 arXiv](https://arxiv.org/abs/2606.12243) • [📥 PDF](https://arxiv.org/pdf/2606.12243)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project page: https://zju-xyc.github.io/VIA-SD-Project-Page/

</details>

<details>
<summary><b>14. VideoMDM: Towards 3D Human Motion Generation From 2D Supervision</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Or Litany, Merav Keidar, Gal Michael Harari, Amir Mann

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13364) • [📄 arXiv](https://arxiv.org/abs/2606.13364) • [📥 PDF](https://arxiv.org/pdf/2606.13364)

**💻 Code:** [⭐ Code](https://github.com/Amir-Mann/VideoMDM_release) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>15. From 2D Grids to 1D Tokens: Reforming Shared Representations for Multimodal Image Fusion</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yi Yang, Yang He, Yunqiu Xu, Yuchen Xian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12303) • [📄 arXiv](https://arxiv.org/abs/2606.12303) • [📥 PDF](https://arxiv.org/pdf/2606.12303)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project page: https://zju-xyc.github.io/1D-Fusion-Project-Page/

</details>

<details>
<summary><b>16. MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13376) • [📄 arXiv](https://arxiv.org/abs/2606.13376) • [📥 PDF](https://arxiv.org/pdf/2606.13376)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Orange-3DV-Team/MoVerse)

> MoVerse is a real-time video world model that transforms a single narrow-field-of-view image into an interactively navigable environment by lifting a topology-aware 360° panorama into a persistent 3D Gaussian scaffold, achieving high-fidelity scen...

</details>

<details>
<summary><b>17. Visual Para-Thinker++: A Single-Policy Multi-Agent Framework for Visual Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiaze Li, Yifei Gao, Hongyu Wang, Haoran Xu, zizhaotong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09290) • [📄 arXiv](https://arxiv.org/abs/2606.09290) • [📥 PDF](https://arxiv.org/pdf/2606.09290)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Visual ParaThinker++

</details>

<details>
<summary><b>18. HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12882) • [📄 arXiv](https://arxiv.org/abs/2606.12882) • [📥 PDF](https://arxiv.org/pdf/2606.12882)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mandyyyyii/HarnessBridge)

> HarnessBridge

</details>

<details>
<summary><b>19. High-Fidelity Two-Step Image Generation via Teacher-Aligned End-to-End Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12575) • [📄 arXiv](https://arxiv.org/abs/2606.12575) • [📥 PDF](https://arxiv.org/pdf/2606.12575)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Z-Image Turbo++, a high-quality 2-step image generation model distilled from the 8-step Z-Image Turbo teacher. With distribution-aligned adversarial learning, step-decoupled parameterization, and end-to-end training with iterative reg...

</details>

<details>
<summary><b>20. SG-OPD: Sign-Gated On-Policy Distillation via Sign-Consistency Gating and Phased Teacher Sampling</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaofeng Zhang, Yifei Gao, Hongyu Wang, Haoran Xu, williamljz

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09304) • [📄 arXiv](https://arxiv.org/abs/2606.09304) • [📥 PDF](https://arxiv.org/pdf/2606.09304)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> SG-OPD

</details>

<details>
<summary><b>21. Where, What, Why, and Importance: Structured Defect Grounding for Text-to-Image Feedback</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06113) • [📄 arXiv](https://arxiv.org/abs/2606.06113) • [📥 PDF](https://arxiv.org/pdf/2606.06113)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/nianbai006/SDG)

> All code, datasets and model weights are publicly available. https://huggingface.co/collections/P1n3/sdg github： https://github.com/nianbai006/SDG

</details>

<details>
<summary><b>22. TreeSeeker: Tree-Structured Trial, Error, and Return in Deep Search</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Pu Zhao, Fangkai Yang, Lu Wang, Zhuofan Shi, mingzhema

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11662) • [📄 arXiv](https://arxiv.org/abs/2606.11662) • [📥 PDF](https://arxiv.org/pdf/2606.11662)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We propose TreeSeeker, a framework for deep-search agents that explicitly models trial-and-error during long-horizon web research. In practice, deep search is not only a reasoning problem — it is also a search-control problem. Agents often face se...

</details>

<details>
<summary><b>23. EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fandong Meng, Xianfeng Zeng, Lianzhe Huang, Yunhan Wang, Krystalan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13120) • [📄 arXiv](https://arxiv.org/abs/2606.13120) • [📥 PDF](https://arxiv.org/pdf/2606.13120)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> EvoBrowseComp is a search agent benchmark of 400 English and 400 Chinese contamination-free complex questions synthesized via live-web traversal.

</details>

<details>
<summary><b>24. Surflo: Consistent 3D Surface Flow Model with Global State</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ko Nishino, Jiahui Lei, Nicolas Dufour, Shu Nakamura, Antoine Guédon

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13644) • [📄 arXiv](https://arxiv.org/abs/2606.13644) • [📥 PDF](https://arxiv.org/pdf/2606.13644)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>25. Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12674) • [📄 arXiv](https://arxiv.org/abs/2606.12674) • [📥 PDF](https://arxiv.org/pdf/2606.12674)

**💻 Code:** [⭐ Code](https://github.com/IBM/Evoflux) • [⭐ Code](https://github.com/huggingface)

> Evoflux tackles a practical bottleneck for small (1.5B–4B) tool-using agents: with only a few hundred teacher traces available, should that scarce supervision go into fine-tuning the model's weights, or into search at inference time? The paper ref...

</details>

<details>
<summary><b>26. MaskAlign: Token-Subset Representation Alignment for Efficient Diffusion Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08788) • [📄 arXiv](https://arxiv.org/abs/2606.08788) • [📥 PDF](https://arxiv.org/pdf/2606.08788)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>27. Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yinhong Liu, Shengen Wu, Chao Chen, Jiayu Yang, EasonFan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13106) • [📄 arXiv](https://arxiv.org/abs/2606.13106) • [📥 PDF](https://arxiv.org/pdf/2606.13106)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper introduces a pair of learned boundary tokens (/) that mark where latent reasoning begins and ends, making hidden-state-recurrence latent CoT both trainable with standard on-policy RL (GRPO) and open to direct mechanistic probing and cau...

</details>

<details>
<summary><b>28. WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Andrea Bajcsy, Gokul Swamy, Jesse Farebrother, Yilin Wu, Arnav Kumar Jain

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13672) • [📄 arXiv](https://arxiv.org/abs/2606.13672) • [📥 PDF](https://arxiv.org/pdf/2606.13672)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/arnavkj1995/WEAVER)

> No abstract available.

</details>

<details>
<summary><b>29. PianoKontext: Expressive Performance Rendering from Deadpan Context</b> ⭐ 1</summary>

<br/>

**👥 Authors:** realfolkcode

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12282) • [📄 arXiv](https://arxiv.org/abs/2606.12282) • [📥 PDF](https://arxiv.org/pdf/2606.12282)

**💻 Code:** [⭐ Code](https://github.com/realfolkcode/pianokontext) • [⭐ Code](https://github.com/huggingface)

> Expressive performance rendering (EPR) aims to generate realistic performances constrained on sequences of notes. However, flow matching audio editing models manipulate only synchronized music samples of the same duration, limiting their understan...

</details>

<details>
<summary><b>30. IDEAL: In-DEpth ALignment Makes A Discrete Representation AutoEncoder</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Yixuan Ren, Lingyu Kong, Junke Wang, Zijie Diao, Row11n

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11096) • [📄 arXiv](https://arxiv.org/abs/2606.11096) • [📥 PDF](https://arxiv.org/pdf/2606.11096)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Row11n/IDEAL)

> IDEAL: In-DEpth ALignment Makes A Discrete Representation AutoEncoder

</details>

<details>
<summary><b>31. MuJoCo-Drones-Gym: A GPU-Accelerated Multi-Drone Simulator for Control and Reinforcement Learning</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08039) • [📄 arXiv](https://arxiv.org/abs/2606.08039) • [📥 PDF](https://arxiv.org/pdf/2606.08039)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tau-intelligence/MuJoCo-drones-gym)

> We present MuJoCo-Drones-Gym, an open-source Gymnasium-compatible multi-drone environment built on top of the MuJoCo physics engine. Multi-drone environment for RL with MuJoCo, with GPU vectorization, wind models, domain randomization, and curricu...

</details>

<details>
<summary><b>32. ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13572) • [📄 arXiv](https://arxiv.org/abs/2606.13572) • [📥 PDF](https://arxiv.org/pdf/2606.13572)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> An agentic framework for enhancing multimodal medical reasoning in Indian Languages.

</details>

<details>
<summary><b>33. Flash-GMM: A Memory-Efficient Kernel for Scalable Soft Clustering</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10896) • [📄 arXiv](https://arxiv.org/abs/2606.10896) • [📥 PDF](https://arxiv.org/pdf/2606.10896)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/IBM/Flash-GMM)

> Have a look at https://github.com/IBM/Flash-GMM

</details>

<details>
<summary><b>34. Leveraging Morphology for Historical Script Metrological Analysis</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09446) • [📄 arXiv](https://arxiv.org/abs/2606.09446) • [📥 PDF](https://arxiv.org/pdf/2606.09446)

**💻 Code:** [⭐ Code](https://github.com/raphael-baena/morphology4metrology) • [⭐ Code](https://github.com/huggingface)

> Advances in handwritten text recognition have enabled large-scale transcription of historical documents, but still provide limited access to interpretable visual measurements for paleography, the study of historical scripts. In this paper, our mai...

</details>

<details>
<summary><b>35. Revisiting Articulated Parts Perception in Robot Manipulation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08103) • [📄 arXiv](https://arxiv.org/abs/2606.08103) • [📥 PDF](https://arxiv.org/pdf/2606.08103)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/enlighten0707/Geometric_Primary_Structure)

> We are surrounded by various objects with movable, articulated parts, e.g., box, handle, door. An accurate and generalizable perception of articulated parts is essential to enhance robotic manipulation capabilities. Building on this need, recent e...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 35 |
| 📅 Today | [`2026-06-12.json`](data/daily/2026-06-12.json) | 35 |
| 📆 This Week | [`2026-W23.json`](data/weekly/2026-W23.json) | 159 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 382 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-12 | 35 | [View JSON](data/daily/2026-06-12.json) |
| 📄 2026-06-11 | 27 | [View JSON](data/daily/2026-06-11.json) |
| 📄 2026-06-10 | 35 | [View JSON](data/daily/2026-06-10.json) |
| 📄 2026-06-09 | 36 | [View JSON](data/daily/2026-06-09.json) |
| 📄 2026-06-08 | 26 | [View JSON](data/daily/2026-06-08.json) |
| 📄 2026-06-07 | 50 | [View JSON](data/daily/2026-06-07.json) |
| 📄 2026-06-06 | 0 | [View JSON](data/daily/2026-06-06.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W23 | 159 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |
| 📅 2026-W20 | 243 | [View JSON](data/weekly/2026-W20.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 382 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |

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
