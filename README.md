<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-32-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5324+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">32</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">502</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5324+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 15, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. OmniDirector: General Multi-Shot Camera Cloning without Cross-Paired Data</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13432) • [📄 arXiv](https://arxiv.org/abs/2606.13432) • [📥 PDF](https://arxiv.org/pdf/2606.13432)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lisj575/OmniDirector)

> No abstract available.

</details>

<details>
<summary><b>2. APPO: Agentic Procedural Policy Optimization</b> ⭐ 46</summary>

<br/>

**👥 Authors:** Shidong Yang, Yuxiang Ji, Yong Wang, Ziyu Ma, xuc865

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12384) • [📄 arXiv](https://arxiv.org/abs/2606.12384) • [📥 PDF](https://arxiv.org/pdf/2606.12384)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AMAP-ML/APPO)

> APPO: Agentic Procedural Policy Optimization Github: https://github.com/AMAP-ML/APPO

</details>

<details>
<summary><b>3. Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents</b> ⭐ 23</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06036) • [📄 arXiv](https://arxiv.org/abs/2606.06036) • [📥 PDF](https://arxiv.org/pdf/2606.06036)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ji-shuo/MRAgent)

> No abstract available.

</details>

<details>
<summary><b>4. From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous AI</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiangqi Chen, Shuai Wang, Jiaxuan Zhu, Ziang Liu, Yongheng Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14502) • [📄 arXiv](https://arxiv.org/abs/2606.14502) • [📥 PDF](https://arxiv.org/pdf/2606.14502)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper systematically reviews the evolution of AI systems from passive, session-based chatbots to persistent, autonomous digital colleagues. In this work, we establish a comprehensive taxonomy of the underlying architectures, long-term memory ...

</details>

<details>
<summary><b>5. Orchestra-o1: Omnimodal Agent Orchestration</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13707) • [📄 arXiv](https://arxiv.org/abs/2606.13707) • [📥 PDF](https://arxiv.org/pdf/2606.13707)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zfkarl/Orchestra-o1)

> Orchestra-o1 is an open-source omnimodal agent orchestration framework that supports agentic tasks involving omnimodal perception, web search, computation, and more. We also provide an 8B model trained with agentic RL to serve as the main orchestr...

</details>

<details>
<summary><b>6. HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hanlin Teng, Weicheng Meng, Kang Zhao, Shuo Lu, Tingyang Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14249) • [📄 arXiv](https://arxiv.org/abs/2606.14249) • [📥 PDF](https://arxiv.org/pdf/2606.14249)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>7. Rethinking RAG in Long Videos: What to Retrieve and How to Use It?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13141) • [📄 arXiv](https://arxiv.org/abs/2606.13141) • [📥 PDF](https://arxiv.org/pdf/2606.13141)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> If you have any question about the paper, please contact yuholee@kaist.ac.kr

</details>

<details>
<summary><b>8. OmniVideo-100K: A Dataset for Audio-Visual Reasoning through Structured Scripts and Evidence Chains</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14702) • [📄 arXiv](https://arxiv.org/abs/2606.14702) • [📥 PDF](https://arxiv.org/pdf/2606.14702)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MiG-NJU/OmniVideo-100K)

> No abstract available.

</details>

<details>
<summary><b>9. From AGI to ASI</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12683) • [📄 arXiv](https://arxiv.org/abs/2606.12683) • [📥 PDF](https://arxiv.org/pdf/2606.12683)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> https://x.com/scychan_brains/status/2066272306218021011?s=46

</details>

<details>
<summary><b>10. Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Yukang Chen, Chufan Shi, Zicheng Lin, Yiran Xu, Yiming Ren

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.30789) • [📄 arXiv](https://arxiv.org/abs/2605.30789) • [📥 PDF](https://arxiv.org/pdf/2605.30789)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/qishisuren123/S2L-PO)

> We recently open-sourced S2L-PO (Small-to-Large Policy Optimization). S2L-PO addresses the issue of rollout diversity in reinforcement learning for large model inference. Its core idea is to leverage the inherent diversity of small models to act a...

</details>

<details>
<summary><b>11. RedAct: Redacting Agent Capability Traces for Procedural Skill Protection</b> ⭐ 12</summary>

<br/>

**👥 Authors:** Yi R. Fung, Zhitao He, xushuwen23

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10813) • [📄 arXiv](https://arxiv.org/abs/2606.10813) • [📥 PDF](https://arxiv.org/pdf/2606.10813)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XuShuwenn/RedAct)

> 🛡️ RedAct: Protecting agent traces from procedural skill leakage What if the traces released for transparency and debugging also become tutorials for copying an agent’s private skills? 👀 Agent traces can reveal formulas, thresholds, tool choices, ...

</details>

<details>
<summary><b>12. Measuring Epistemic Resilience of LLMs Under Misleading Medical Context</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12291) • [📄 arXiv](https://arxiv.org/abs/2606.12291) • [📥 PDF](https://arxiv.org/pdf/2606.12291)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> LLMs can ace medical exams, but do they preserve good medical judgment when misleading context is present? MedMisBench is a new benchmark that measures whether LLMs maintain correct medical judgment when plausible but misleading medical context is...

</details>

<details>
<summary><b>13. LLM Agents Can See Code Repositories</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14061) • [📄 arXiv](https://arxiv.org/abs/2606.14061) • [📥 PDF](https://arxiv.org/pdf/2606.14061)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/cslsolow/SeeRepo)

> SeeRepo lets a coding agent look at a repo more like a developer would: not just reading files one by one, but seeing how files, classes, functions, and dependencies connect. It gives the agent a visual map alongside the code, so it can find the r...

</details>

<details>
<summary><b>14. Skip a Layer or Loop It? Learning Program-of-Layers in LLMs</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06574) • [📄 arXiv](https://arxiv.org/abs/2606.06574) • [📥 PDF](https://arxiv.org/pdf/2606.06574)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tianyi-lab/PoLar)

> This paper asks whether LLM inference really needs to follow the same fixed layer order for every input. We introduce PoLar, a program-of-layers framework that treats frozen transformer layers as reusable functions. Instead of always executing all...

</details>

<details>
<summary><b>15. RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14700) • [📄 arXiv](https://arxiv.org/abs/2606.14700) • [📥 PDF](https://arxiv.org/pdf/2606.14700)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> RepFusion repurposes a frozen multimodal LLM as a noisy latent encoder for text-to-image generation, providing strong denoising priors in representation space and enabling test-time scaling via repeated MLLM conditioning.

</details>

<details>
<summary><b>16. Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14409) • [📄 arXiv](https://arxiv.org/abs/2606.14409) • [📥 PDF](https://arxiv.org/pdf/2606.14409)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. MBench: A Comprehensive Benchmark on Memory Capability for Video World Models</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00793) • [📄 arXiv](https://arxiv.org/abs/2606.00793) • [📥 PDF](https://arxiv.org/pdf/2606.00793)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/study-overflow/MBench)

> MBench is a benchmark for the memory capability of long-video world models. Most existing benchmarks reward single-frame quality or short-horizon prompt following. MBench targets a harder question: when a subject leaves the frame and returns, when...

</details>

<details>
<summary><b>18. VISTA: View-Consistent Self-Verified Training for GUI Grounding</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14579) • [📄 arXiv](https://arxiv.org/abs/2606.14579) • [📥 PDF](https://arxiv.org/pdf/2606.14579)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZJUSCL/VISTA)

> VISTA introduces View-Consistent Self-Verified Training for GUI grounding, addressing a key limitation of applying GRPO to coordinate prediction: rollouts from a single screenshot view often collapse into all-success or all-failure groups, providi...

</details>

<details>
<summary><b>19. Avatar V: Scaling Video-Reference Avatar Video Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13872) • [📄 arXiv](https://arxiv.org/abs/2606.13872) • [📥 PDF](https://arxiv.org/pdf/2606.13872)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. The Hidden Power of Scaling Factor in LoRA Optimization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Anqi Li, Guoqiang Gong, Jiaxing Wang, Haoran Li, Zicheng Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12883) • [📄 arXiv](https://arxiv.org/abs/2606.12883) • [📥 PDF](https://arxiv.org/pdf/2606.12883)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Maybe the first systematic study (empirical + theoretical)  of LoRA's scaling factor $\alpha$ from an optimization perspective! Recent studies highlight that a large learning rate ($\eta$) is crucial for LoRA optimization. However, this paper poin...

</details>

<details>
<summary><b>21. RhymeFlow: Training-Free Acceleration for Video Generation with Asynchronous Denoising Flow Scheduling</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06309) • [📄 arXiv](https://arxiv.org/abs/2606.06309) • [📥 PDF](https://arxiv.org/pdf/2606.06309)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Simon-Dcs/RhymeFlow)

> This paper introduces Asynchronous Denoising Flow Scheduling for video generation acceleration, achieving 1.93x speed up on CogVideoX-v1.5, 1.66x on Wan 2.1 and 2.60x on HunyuanVideo. Only these keyframes undergo dense, step-by-step denoising to e...

</details>

<details>
<summary><b>22. ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yichen Qian, Jinwang Wang, Wenjun Zhang, Hangjie Yuan, Sicheng Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14697) • [📄 arXiv](https://arxiv.org/abs/2606.14697) • [📥 PDF](https://arxiv.org/pdf/2606.14697)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/alibaba-damo-academy/ClinHallu)

> Code and datasets: https://github.com/alibaba-damo-academy/ClinHallu

</details>

<details>
<summary><b>23. When is Your LLM Steerable?</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11599) • [📄 arXiv](https://arxiv.org/abs/2606.11599) • [📥 PDF](https://arxiv.org/pdf/2606.11599)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Fcr09/SteerBoost)

> Main contributions: We curate a dataset of steering that covers steered responses of multiple LLMs under different prompts, concepts, and steering strengths. It enables fine-grained analysis of the latent dynamics of steering in LLMs. We developed...

</details>

<details>
<summary><b>24. Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Jun-Peng Jiang, Hao-Xuan Ma, Yulan Hu, Wenlin Liu, hug-ye

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13657) • [📄 arXiv](https://arxiv.org/abs/2606.13657) • [📥 PDF](https://arxiv.org/pdf/2606.13657)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SydCS/OPD-Param-Analysis)

> On-policy distillation is attractive because it appears to offer the best of both worlds: the student trains on its own on-policy generations, as in reinforcement learning, while still receiving dense teacher supervision, as in distillation. Yet t...

</details>

<details>
<summary><b>25. P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning</b> ⭐ 37</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11152) • [📄 arXiv](https://arxiv.org/abs/2606.11152) • [📥 PDF](https://arxiv.org/pdf/2606.11152)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SpatiaOS/P3D-Bench)

> No abstract available.

</details>

<details>
<summary><b>26. μ_0: A Scalable 3D Interaction-Trace World Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Amir Hossein Shahidzadeh, Jonghun Shin, Jusuk Lee, Yoonkyo Jung, Seungjae Lee

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.13769) • [📄 arXiv](https://arxiv.org/abs/2606.13769) • [📥 PDF](https://arxiv.org/pdf/2606.13769)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>27. Benchmarking AI Agents for Addressing Scientific Challenges Across Scales</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Wenxin Long, Lisa Xinyi Chen, Antonia Panescu, Allen Xin Wang, Tianyu Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.12736) • [📄 arXiv](https://arxiv.org/abs/2606.12736) • [📥 PDF](https://arxiv.org/pdf/2606.12736)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HelloWorldLTY/SciAgentArena)

> AI agents are increasingly being developed to accelerate scientific discovery, yet their practical capabilities in real research settings remain poorly understood. Existing benchmarks for AI agents rarely capture the complexity, heterogeneity, and...

</details>

<details>
<summary><b>28. AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization</b> ⭐ 73</summary>

<br/>

**👥 Authors:** Xuan Lu, Anhao Zhao, Yingqi Fan, Wenqi Xu, Junlong Tong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14694) • [📄 arXiv](https://arxiv.org/abs/2606.14694) • [📥 PDF](https://arxiv.org/pdf/2606.14694)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EIT-NLP/StreamingLLM)

> No abstract available.

</details>

<details>
<summary><b>29. AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuxiang Zhang, Qihui Zhu, Zhenyu Wu, Bin Wang, Shouwei Ruan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08952) • [📄 arXiv](https://arxiv.org/abs/2606.08952) • [📥 PDF](https://arxiv.org/pdf/2606.08952)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Heathcliff-saku/AlloSpatial)

> Spatial reasoning is one of the most stubborn blind spots in today's multimodal foundation models. A system that can write code, analyze images, and hold a fluent conversation will still stumble on something as basic as how far the door is from th...

</details>

<details>
<summary><b>30. WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.08670) • [📄 arXiv](https://arxiv.org/abs/2606.08670) • [📥 PDF](https://arxiv.org/pdf/2606.08670)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sisinflab/WaveDiT)

> One full-size 3D brain. Every voxel, no lossy latent. Size isn't the only hard part: wavelet bands aren't statistically equal, high-frequency anatomy is sparse, heavy-tailed, and grows sharper as noise becomes a brain. So we built Morpheus: a sche...

</details>

<details>
<summary><b>31. ActiveMimic: Egocentric Video Pretraining with Active Perception</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yichen Zhu, Ziyi Ye, Tianyi Lu, Guojin Zhong, Xingyao Lin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06194) • [📄 arXiv](https://arxiv.org/abs/2606.06194) • [📥 PDF](https://arxiv.org/pdf/2606.06194)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project Page: https://activemimic.github.io/

</details>

<details>
<summary><b>32. CARVE: Certified Affordable Repair of Vetoed Maneuvers via Envelopes for Interactive Driving</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yifan Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02641) • [📄 arXiv](https://arxiv.org/abs/2606.02641) • [📥 PDF](https://arxiv.org/pdf/2606.02641)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> If you have any question about this paper, please contact: yuholee@kaist.ac.kr .

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 32 |
| 📅 Today | [`2026-06-15.json`](data/daily/2026-06-15.json) | 32 |
| 📆 This Week | [`2026-W24.json`](data/weekly/2026-W24.json) | 32 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 502 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-15 | 32 | [View JSON](data/daily/2026-06-15.json) |
| 📄 2026-06-14 | 44 | [View JSON](data/daily/2026-06-14.json) |
| 📄 2026-06-13 | 44 | [View JSON](data/daily/2026-06-13.json) |
| 📄 2026-06-12 | 35 | [View JSON](data/daily/2026-06-12.json) |
| 📄 2026-06-11 | 27 | [View JSON](data/daily/2026-06-11.json) |
| 📄 2026-06-10 | 35 | [View JSON](data/daily/2026-06-10.json) |
| 📄 2026-06-09 | 36 | [View JSON](data/daily/2026-06-09.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W24 | 32 | [View JSON](data/weekly/2026-W24.json) |
| 📅 2026-W23 | 247 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 502 | [View JSON](data/monthly/2026-06.json) |
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
