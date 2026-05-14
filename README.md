<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-34-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4148+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">34</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">162</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">384</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4148+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** May 14, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. MinT: Managed Infrastructure for Training and Serving Millions of LLMs</b> ⭐ 17</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13779) • [📄 arXiv](https://arxiv.org/abs/2605.13779) • [📥 PDF](https://arxiv.org/pdf/2605.13779)

**💻 Code:** [⭐ Code](https://github.com/MindLab-Research/mindlab-toolkit)

> MinT: Managed Infrastructure for Training and Serving Millions of LLMs

</details>

<details>
<summary><b>2. AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation</b> ⭐ 78</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13724) • [📄 arXiv](https://arxiv.org/abs/2605.13724) • [📥 PDF](https://arxiv.org/pdf/2605.13724)

**💻 Code:** [⭐ Code](https://github.com/NVlabs/AnyFlow)

> We have open-sourced the code, model and demo. 📄Paper: https://arxiv.org/abs/2605.13724 💻Code: https://github.com/NVlabs/AnyFlow 🎨Pre-trained Models: https://huggingface.co/collections/nvidia/anyflow 🎬Demo: https://nvlabs.github.io/AnyFlow/demo

</details>

<details>
<summary><b>3. MulTaBench: Benchmarking Multimodal Tabular Learning with Text and Image</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10616) • [📄 arXiv](https://arxiv.org/abs/2605.10616) • [📥 PDF](https://arxiv.org/pdf/2605.10616)

> Many real-world prediction problems combine structured features with text or images: clinical records with X-rays, real-estate metadata with street-view photos, product listings with descriptions and images. But current approaches usually force on...

</details>

<details>
<summary><b>4. Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13831) • [📄 arXiv](https://arxiv.org/abs/2605.13831) • [📥 PDF](https://arxiv.org/pdf/2605.13831)

> Long-context modeling is becoming a core capability of modern large vision-language models (LVLMs), enabling sustained context management across long-document understanding, video analysis, and multi-turn tool use in agentic workflows. Yet practic...

</details>

<details>
<summary><b>5. Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12411) • [📄 arXiv](https://arxiv.org/abs/2605.12411) • [📥 PDF](https://arxiv.org/pdf/2605.12411)

> AI agents will increasingly need to interact with unfamiliar AI counterparts in settings like negotiation and bargaining. In this paper, we ask: can we predict the next decision of a black-box AI agent after seeing only a few prior interactions? W...

</details>

<details>
<summary><b>6. Edit-Compass & EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Yuran Wang, Xuanyu Zhu, Yi-Fan Zhang, Yang Shi, Xuehai Bai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13062) • [📄 arXiv](https://arxiv.org/abs/2605.13062) • [📥 PDF](https://arxiv.org/pdf/2605.13062)

**💻 Code:** [⭐ Code](https://github.com/bxhsort/Edit-Compass-and-EditReward-Compass)

> Recent image editing models have achieved remarkable progress in instruction following, multimodal understanding, and complex visual editing. However, existing benchmarks often fail to faithfully reflect human judgment, especially for strong front...

</details>

<details>
<summary><b>7. TrackCraft3R: Repurposing Video Diffusion Transformers for Dense 3D Tracking</b> ⭐ 28</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12587) • [📄 arXiv](https://arxiv.org/abs/2605.12587) • [📥 PDF](https://arxiv.org/pdf/2605.12587)

**💻 Code:** [⭐ Code](https://github.com/cvlab-kaist/TrackCraft3r)

> Dense 3D tracking from monocular video is fundamental to dynamic scene under- standing. While recent 3D foundation models provide reliable per-frame geometry, recovering object motion in this geometry remains challenging and benefits from strong m...

</details>

<details>
<summary><b>8. Qwen-Image-VAE-2.0 Technical Report</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13565) • [📄 arXiv](https://arxiv.org/abs/2605.13565) • [📥 PDF](https://arxiv.org/pdf/2605.13565)

**💻 Code:** [⭐ Code](https://github.com/alibaba/OmniDoc-TokenBench)

> Qwen-Image-VAE-2.0 Technical Report

</details>

<details>
<summary><b>9. Many-Shot CoT-ICL: Making In-Context Learning Truly Learn</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dit-Yan Yeung, Mo Yu, Lemao Liu, Tsz Ting Chung

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13511) • [📄 arXiv](https://arxiv.org/abs/2605.13511) • [📥 PDF](https://arxiv.org/pdf/2605.13511)

> We believe this work provides a step toward bridging ICL from pattern matching to in-context test time learning with two principles proposed, showing that reasoning performance relies on demonstrations being both understandable to the model and sm...

</details>

<details>
<summary><b>10. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13757) • [📄 arXiv](https://arxiv.org/abs/2605.13757) • [📥 PDF](https://arxiv.org/pdf/2605.13757)

**💻 Code:** [⭐ Code](https://github.com/ZGC-EmbodyAI/FrameSkip)

> TLDR : FrameSkip is a data-layer framework that improves VLA training by selectively retaining only the most informative frames—based on action variation, visual-action coherence, and task-progress cues—rather than uniformly sampling all trajector...

</details>

<details>
<summary><b>11. The DAWN of World-Action Interactive Models</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11550) • [📄 arXiv](https://arxiv.org/abs/2605.11550) • [📥 PDF](https://arxiv.org/pdf/2605.11550)

**💻 Code:** [⭐ Code](https://github.com/COOWAI/DAWN)

> Existing World Action Models (WAMs) largely miss this reciprocity, treating world prediction and action generation as either isolated parallel branches or rigid predict-then-plan pipelines. We formalize this perspective as World-Action Interactive...

</details>

<details>
<summary><b>12. Learning Agentic Policy from Action Guidance</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Ziyu Ma, Shidong Yang, Yong Wang, Zengbin Wang, Yuxiang Ji

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12004) • [📄 arXiv](https://arxiv.org/abs/2605.12004) • [📥 PDF](https://arxiv.org/pdf/2605.12004)

**💻 Code:** [⭐ Code](https://github.com/AMAP-ML/ActGuide-RL)

> Explore agentic RL through action data, without SFT.

</details>

<details>
<summary><b>13. Asymmetric Flow Models</b> ⭐ 290</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12964) • [📄 arXiv](https://arxiv.org/abs/2605.12964) • [📥 PDF](https://arxiv.org/pdf/2605.12964)

**💻 Code:** [⭐ Code](https://github.com/Lakonik/LakonLab)

> JiT x0-prediction is not enough for pixel generation. AsymFlow introduces rank-asymmetric flow parameterization for scalable pixel generation. Core Method Velocity prediction has a data term and a noise term. AsymFlow makes them rank-asymmetric: D...

</details>

<details>
<summary><b>14. Retrieval is Cheap, Show Me the Code: Executable Multi-Hop Reasoning for Retrieval-Augmented Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12975) • [📄 arXiv](https://arxiv.org/abs/2605.12975) • [📥 PDF](https://arxiv.org/pdf/2605.12975)

**💻 Code:** [⭐ Code](https://github.com/GasolSun36/PyRAG)

> Retrieval is Cheap, Show Me the Code: Executable Multi-Hop Reasoning for Retrieval-Augmented Generation

</details>

<details>
<summary><b>15. PresentAgent-2: Towards Generalist Multimodal Presentation Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11363) • [📄 arXiv](https://arxiv.org/abs/2605.11363) • [📥 PDF](https://arxiv.org/pdf/2605.11363)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/PresentAgent-2)

> The code has been open-sourced.

</details>

<details>
<summary><b>16. RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ying-Cong Chen, Wenhang Ge, Yingjie Xu, Sirui Chen, Harold Haodong Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13775) • [📄 arXiv](https://arxiv.org/abs/2605.13775) • [📥 PDF](https://arxiv.org/pdf/2605.13775)

> https://arxiv.org/pdf/2605.13775

</details>

<details>
<summary><b>17. HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Bingzhe Li, Qiannan Li, Guanpeng Li, Yi Li, Dongming Jiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09942) • [📄 arXiv](https://arxiv.org/abs/2605.09942) • [📥 PDF](https://arxiv.org/pdf/2605.09942)

**💻 Code:** [⭐ Code](https://github.com/FredJiang0324/HAGE_MVPReview)

> HAGE is a principled memory system for long-term conversation memory and multi-hop reasoning. It represents memory across four orthogonal relational graphs — Semantic, Temporal, Causal, and Entity — and introduces a co-evolutionary training framew...

</details>

<details>
<summary><b>18. Offline Preference Optimization for Rectified Flow with Noise-Tracked Pairs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Min Zhang, Xiaoyin Xu, Hengyuan Cao, Qichao Wang, Yunhong Lu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09433) • [📄 arXiv](https://arxiv.org/abs/2605.09433) • [📥 PDF](https://arxiv.org/pdf/2605.09433)

> T2I Preference Optimization

</details>

<details>
<summary><b>19. Revisiting DAgger in the Era of LLM-Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12913) • [📄 arXiv](https://arxiv.org/abs/2605.12913) • [📥 PDF](https://arxiv.org/pdf/2605.12913)

> DAgger is back for the agent era: we revisit it for LLM agents and place SFT, RL, OPD, and DAgger under one unified post-training lens. Using our training recipe, 4B SWE agents beat published 8B systems, while 8B agents approach 32B-scale performa...

</details>

<details>
<summary><b>20. Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Franck Dernoncourt, Ryan A. Rossi, Van Cuong Pham, Chaitra Hegde, Chien Van Nguyen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12825) • [📄 arXiv](https://arxiv.org/abs/2605.12825) • [📥 PDF](https://arxiv.org/pdf/2605.12825)

**💻 Code:** [⭐ Code](https://github.com/chiennv2000/orthrus)

> Fast, lossless LLM inference via dual-view diffusion decoding. Code: https://github.com/chiennv2000/orthrus

</details>

<details>
<summary><b>21. Results and Retrospective Analysis of the CODS 2025 AssetOpsBench Challenge</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08518) • [📄 arXiv](https://arxiv.org/abs/2605.08518) • [📥 PDF](https://arxiv.org/pdf/2605.08518)

> Competition retrospectives are useful when they explain what a leaderboard measured, how hidden evaluation changed conclusions, and which design patterns were rewarded. We revisit the CODS 2025 challenge, a privacy-aware Codabench competition on i...

</details>

<details>
<summary><b>22. MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jinwei Xiao, Mingye Zhu, Yueqing Sun, Ziang Ye, Yuxin Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13037) • [📄 arXiv](https://arxiv.org/abs/2605.13037) • [📥 PDF](https://arxiv.org/pdf/2605.13037)

> No abstract available.

</details>

<details>
<summary><b>23. AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Benjamin Steenhoek, Shengjie Ma, Xiaomin Li, Gaurav Mittal, Priyam Sahoo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12925) • [📄 arXiv](https://arxiv.org/abs/2605.12925) • [📥 PDF](https://arxiv.org/pdf/2605.12925)

**💻 Code:** [⭐ Code](https://github.com/microsoft/code-agent-state-trajectories)

> Github: https://github.com/microsoft/code-agent-state-trajectories

</details>

<details>
<summary><b>24. Context Training with Active Information Seeking</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13050) • [📄 arXiv](https://arxiv.org/abs/2605.13050) • [📥 PDF](https://arxiv.org/pdf/2605.13050)

> No abstract available.

</details>

<details>
<summary><b>25. Frequency Bias and OOD Generalization in Neural Operators under a Variable-Coefficient Wave Equation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** An Luo, Runlong Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12997) • [📄 arXiv](https://arxiv.org/abs/2605.12997) • [📥 PDF](https://arxiv.org/pdf/2605.12997)

> Neural Operators

</details>

<details>
<summary><b>26. Visual Aesthetic Benchmark: Can Frontier Models Judge Beauty?</b> ⭐ 29</summary>

<br/>

**👥 Authors:** Fengqing Jiang, Yuanyuan Chen, Chunjiang Liu, Yuetai Li, Yichen Feng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12684) • [📄 arXiv](https://arxiv.org/abs/2605.12684) • [📥 PDF](https://arxiv.org/pdf/2605.12684)

**💻 Code:** [⭐ Code](https://github.com/BakeLab/Visual-Aesthetic-Benchmark)

> No abstract available.

</details>

<details>
<summary><b>27. ShapeCodeBench: A Renewable Benchmark for Perception-to-Program Reconstruction of Synthetic Shape Scenes</b> ⭐ 1</summary>

<br/>

**👥 Authors:** shivamk3r

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11680) • [📄 arXiv](https://arxiv.org/abs/2605.11680) • [📥 PDF](https://arxiv.org/pdf/2605.11680)

**💻 Code:** [⭐ Code](https://github.com/shivamk3r/shape-code-bench)

> ShapeCodeBench is a synthetic multimodal benchmark for perception-to-program reconstruction: models infer executable drawing programs from rendered shape scenes. The v1 release is intentionally small but challenging: the best multimodal exact-matc...

</details>

<details>
<summary><b>28. Position: LLM Inference Should Be Evaluated as Energy-to-Token Production</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kaiyong Zhao, Peijie Dong, Zhenheng Tang, Shimiao Yuan, Xiang Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11733) • [📄 arXiv](https://arxiv.org/abs/2605.11733) • [📥 PDF](https://arxiv.org/pdf/2605.11733)

> LLM inference is still evaluated mainly as a model or software problem: accuracy, latency, throughput, and hardware utilization. This is incomplete. At deployment scale, the relevant output is a quality-conditioned token produced under joint const...

</details>

<details>
<summary><b>29. MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10268) • [📄 arXiv](https://arxiv.org/abs/2605.10268) • [📥 PDF](https://arxiv.org/pdf/2605.10268)

**💻 Code:** [⭐ Code](https://github.com/iiGray/MemReread)

> 📖 Overview MemReread is a memory-guided LLM agent that decomposes the task to isolate its highest-priority sub-question based on its memory, then performs rereading guided by the generated sub-question, and directly answers according to the sub-me...

</details>

<details>
<summary><b>30. The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08737) • [📄 arXiv](https://arxiv.org/abs/2605.08737) • [📥 PDF](https://arxiv.org/pdf/2605.08737)

> https://lixin.ai/ListOPD

</details>

<details>
<summary><b>31. Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.13087) • [📄 arXiv](https://arxiv.org/abs/2605.13087) • [📥 PDF](https://arxiv.org/pdf/2605.13087)

> No abstract available.

</details>

<details>
<summary><b>32. F-GRPO: Factorized Group-Relative Policy Optimization for Unified Candidate Generation and Ranking</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12995) • [📄 arXiv](https://arxiv.org/abs/2605.12995) • [📥 PDF](https://arxiv.org/pdf/2605.12995)

> F-GRPO: Factorized Group-Relative Policy Optimization for Unified Candidate Generation and Ranking

</details>

<details>
<summary><b>33. WriteSAE: Sparse Autoencoders for Recurrent State</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jack Young

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12770) • [📄 arXiv](https://arxiv.org/abs/2605.12770) • [📥 PDF](https://arxiv.org/pdf/2605.12770)

**💻 Code:** [⭐ Code](https://github.com/JackYoung27/writesae)

> WriteSAE extends sparse autoencoders to the matrix-recurrent write site by making decoder atoms rank-1 outer products, matching the native k_t v_t^T cache update. The main results are 92.4% atom-substitution win rate over matched-norm ablation at ...

</details>

<details>
<summary><b>34. SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.05704) • [📄 arXiv](https://arxiv.org/abs/2605.05704) • [📥 PDF](https://arxiv.org/pdf/2605.05704)

**💻 Code:** [⭐ Code](https://github.com/ljj-cyber/SafeHarbor)

> With the rapid evolution of foundation models, Large Language Model (LLM) agents have demonstrated increasingly powerful tool-use capabilities. However, this proficiency introduces significant security risks, as malicious actors can manipulate age...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 34 |
| 📅 Today | [`2026-05-14.json`](data/daily/2026-05-14.json) | 34 |
| 📆 This Week | [`2026-W19.json`](data/weekly/2026-W19.json) | 162 |
| 🗓️ This Month | [`2026-05.json`](data/monthly/2026-05.json) | 384 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-05-14 | 34 | [View JSON](data/daily/2026-05-14.json) |
| 📄 2026-05-13 | 42 | [View JSON](data/daily/2026-05-13.json) |
| 📄 2026-05-12 | 48 | [View JSON](data/daily/2026-05-12.json) |
| 📄 2026-05-11 | 38 | [View JSON](data/daily/2026-05-11.json) |
| 📄 2026-05-10 | 38 | [View JSON](data/daily/2026-05-10.json) |
| 📄 2026-05-09 | 38 | [View JSON](data/daily/2026-05-09.json) |
| 📄 2026-05-08 | 25 | [View JSON](data/daily/2026-05-08.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W19 | 162 | [View JSON](data/weekly/2026-W19.json) |
| 📅 2026-W18 | 158 | [View JSON](data/weekly/2026-W18.json) |
| 📅 2026-W17 | 120 | [View JSON](data/weekly/2026-W17.json) |
| 📅 2026-W16 | 156 | [View JSON](data/weekly/2026-W16.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-05 | 384 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |
| 🗓️ 2025-12 | 787 | [View JSON](data/monthly/2025-12.json) |

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
