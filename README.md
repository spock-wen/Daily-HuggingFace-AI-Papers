<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-38-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9508+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">38</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">68</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">107</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9508+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 03, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Wave Forcing: Towards Speed-of-Light Streaming Video Generation</b> ⭐ 68</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00859) • [📄 arXiv](https://arxiv.org/abs/2611.00859) • [📥 PDF](https://arxiv.org/pdf/2611.00859)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SJTU-DENG-Lab/WaveForcing)

> We introduce Wave Forcing, a training and execution framework for streaming video generation. The key idea is wavefront scheduling: later video chunks begin denoising before earlier chunks finish, using their cleaner intermediate states as causal ...

</details>

<details>
<summary><b>2. CoworkOS:Scaling Agent Coworkers for Real-world Automation</b> ⭐ 46</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03178) • [📄 arXiv](https://arxiv.org/abs/2611.03178) • [📥 PDF](https://arxiv.org/pdf/2611.03178)

**💻 Code:** [⭐ Code](https://github.com/RUC-NLPIR/CoworkOS) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](http://github.com/RUC-NLPIR/CoworkOS/blob/main/CoworkOS_paper.pdf)

> Excited to share our latest work 🥳: 🌍 CoworkOS: Scaling Agent Coworkers for Real-world Automation Building a true “super AI coworker” that handles both complex productivity and long-horizon decision-making. 💡 Three pillars of Design: 1️⃣ Three-lay...

</details>

<details>
<summary><b>3. Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement</b> ⭐ 30</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40191) • [📄 arXiv](https://arxiv.org/abs/2610.40191) • [📥 PDF](https://arxiv.org/pdf/2610.40191)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/agentic-videogen/awesome-agentic-videogen)

> Video generation is evolving from end-to-end synthesis toward agentic systems that integrate planning, tool use, and feedback. Meanwhile, video world models are enabling interactive, action-conditioned environments for agents. In this survey, we e...

</details>

<details>
<summary><b>4. CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements</b> ⭐ 44</summary>

<br/>

**👥 Authors:** Congcong Wang, Zhangquan Chen, Ji Zhao, Gen Li, Xinlei Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03126) • [📄 arXiv](https://arxiv.org/abs/2611.03126) • [📥 PDF](https://arxiv.org/pdf/2611.03126)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/xlyu0106/CUA-Master)

> CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements

</details>

<details>
<summary><b>5. Advances in Agentic Computer Graphics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01860) • [📄 arXiv](https://arxiv.org/abs/2611.01860) • [📥 PDF](https://arxiv.org/pdf/2611.01860)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>6. Democratizing Robot-Use Agents: A Unified Harness with Open Models</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Xiaoyu Huang, Yuxin Zuo, Racktic, hbx, 1rubbishyuan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01560) • [📄 arXiv](https://arxiv.org/abs/2611.01560) • [📥 PDF](https://arxiv.org/pdf/2611.01560)

**💻 Code:** [⭐ Code](https://github.com/Open-RUA/uni-robot-agent) • [⭐ Code](https://github.com/huggingface)

> We introduce uni-robot-agent, a unified harness for robot-use agents with open-weight models, designed to support further training. Without privileged inputs, out-of-the-box Qwen3.8-Flash-Next achieves a RoboDojo Score of 31.39, exceeding the publ...

</details>

<details>
<summary><b>7. NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02102) • [📄 arXiv](https://arxiv.org/abs/2611.02102) • [📥 PDF](https://arxiv.org/pdf/2611.02102)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/beipo-ai/NorthCUA)

> Worlds in mind. Wonders at your fingertips. Turn intent into work — across Desktop and Web

</details>

<details>
<summary><b>8. Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27954) • [📄 arXiv](https://arxiv.org/abs/2610.27954) • [📥 PDF](https://arxiv.org/pdf/2610.27954)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/BangProx/ReTRACE)

> We investigate the recovery problem in computer-use agents and present RETRACE, a scalable pipeline for conducting the first systematic study of autonomous, model-based recovery behavior.

</details>

<details>
<summary><b>9. Reviso: Not All Visual Evidence Deserves Equal Attention in Video Captioning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuqi Tang, Tengfei Liu, zzzhu, Ryann829, DogNeverSleep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03602) • [📄 arXiv](https://arxiv.org/abs/2611.03602) • [📥 PDF](https://arxiv.org/pdf/2611.03602)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multimodal large language models (MLLMs) can generate detailed video captions, yet they may overemphasize minor details while overlooking essential context and key events. We argue that not all visual evidence deserves equal attention, as the impo...

</details>

<details>
<summary><b>10. From Fragmentation to Fusion: A Survey and Roadmap for Omnimodal Embeddings</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00172) • [📄 arXiv](https://arxiv.org/abs/2611.00172) • [📥 PDF](https://arxiv.org/pdf/2611.00172)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/codefuse-ai/Awesome-Omnimodal-Embeddings)

> Despite shared mathematical foundations, embedding research across text, vision, audio, graphs, tables, and time series remains largely fragmented into modality-specific silos. This survey and position paper argues that embedding research is quiet...

</details>

<details>
<summary><b>11. PhotoGuider: Composition-Aware Cropping and 360^{circ} View Framing with Explainable Photographic Assessments</b> ⭐ 18</summary>

<br/>

**👥 Authors:** Yu-Lun Liu, Chia-Che Chang, Kuan-Lin Chen, Yuan-Kang Lee

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02897) • [📄 arXiv](https://arxiv.org/abs/2611.02897) • [📥 PDF](https://arxiv.org/pdf/2611.02897)

**💻 Code:** [⭐ Code](https://github.com/NTUneillee/PhotoGuider) • [⭐ Code](https://github.com/huggingface)

> Traditional image cropping assumes the photograph already contains the composition worth keeping, and asks only where to crop. A full 360° scene offers no such guarantee: the viewing direction in a scene has to be discovered before anything can be...

</details>

<details>
<summary><b>12. CrossSWE: Benchmarking Cross-Repository Joint Development for Coding Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zihan Zhang, Heng Lian, Yuling Shi, zhensuuu, Silin-Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01484) • [📄 arXiv](https://arxiv.org/abs/2611.01484) • [📥 PDF](https://arxiv.org/pdf/2611.01484)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What if we pushed coding agents toward longer-horizon tasks across multiple repositories? 🔗 That's the idea behind CrossSWE ! We extend real-world software engineering tasks beyond a single repository, requiring coding agents to coordinate changes...

</details>

<details>
<summary><b>13. SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02074) • [📄 arXiv](https://arxiv.org/abs/2611.02074) • [📥 PDF](https://arxiv.org/pdf/2611.02074)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: SWE-Trail is a trajectory collector for coding-agent post-training. It uses earlier trajectories to decide where additional collection effort should go, while keeping that history out of the agent's context, so there is no train-test mismat...

</details>

<details>
<summary><b>14. When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Aleksandar Slavov, SookX, bonanc

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01815) • [📄 arXiv](https://arxiv.org/abs/2611.01815) • [📥 PDF](https://arxiv.org/pdf/2611.01815)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/3-ml/jepa-surprise)

> Hi everyone! I'm one of the authors. Our paper asks: when does a video world model's prediction error actually support a claim of physical surprise? The clearest result comes from a controlled support test. A sphere can stop on solid support or fa...

</details>

<details>
<summary><b>15. Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03092) • [📄 arXiv](https://arxiv.org/abs/2611.03092) • [📥 PDF](https://arxiv.org/pdf/2611.03092)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be me...

</details>

<details>
<summary><b>16. Diagnosing the Reference Gap: What Visual Scaffolds Can and Cannot Fix in Multimodal Reasoning</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Anh Tuan Luu, Wotao Yin, Weiwen Xu, Guizhen Chen, kenchan0226

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39419) • [📄 arXiv](https://arxiv.org/abs/2610.39419) • [📥 PDF](https://arxiv.org/pdf/2610.39419)

**💻 Code:** [⭐ Code](https://github.com/regap-bench/ReGap-Bench) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. FLAMIA: FLAsh MIcroscaling Attention for Fast and Causally Safe Training on Blackwell</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03344) • [📄 arXiv](https://arxiv.org/abs/2611.03344) • [📥 PDF](https://arxiv.org/pdf/2611.03344)

**💻 Code:** [⭐ Code](https://github.com/yandex-research/flamia-blackwell-attention) • [⭐ Code](https://github.com/huggingface)

> FLAMIA (FLAsh MIcroscaling Attention) adapts FlashAttention to Blackwell’s FP8/FP4 hardware. Its main design choices are: Selective low precision. Two main training paths: MXFP8, or NVFP4 for query–key score computation and its backward recomputat...

</details>

<details>
<summary><b>18. DecisionRank: On-Policy Distillation for Decision-Model Rerankers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42128) • [📄 arXiv](https://arxiv.org/abs/2610.42128) • [📥 PDF](https://arxiv.org/pdf/2610.42128)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency. However, transferring a generative LLM's ranking knowledge to a decision model remains challenging: the teacher expresses p...

</details>

<details>
<summary><b>19. DeFT-RAG: Decomposing Multi-Hop Questions into Self-Contained Sub-Questions with Reusable Answers</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Bingzhe Li, Dingy-Kang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37826) • [📄 arXiv](https://arxiv.org/abs/2610.37826) • [📥 PDF](https://arxiv.org/pdf/2610.37826)

**💻 Code:** [⭐ Code](https://github.com/Dingyi-Kang/DeFT-RAG) • [⭐ Code](https://github.com/huggingface)

> DeFT-RAG asks a different question about multi-hop RAG: instead of planning all sub-questions and their dependencies in advance, what if the LLM writes just one self-contained sub-question at a time? Each sub-question names every entity it asks ab...

</details>

<details>
<summary><b>20. BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41574) • [📄 arXiv](https://arxiv.org/abs/2610.41574) • [📥 PDF](https://arxiv.org/pdf/2610.41574)

**💻 Code:** [⭐ Code](https://github.com/RuurdKuiper/BYOD) • [⭐ Code](https://github.com/huggingface)

> BYOD: Build your own diffusion language model in Google Colab Can an existing instruction model learn to generate text through diffusion in a few hours on one GPU? In BYOD: Build Your Own DLM , we convert Gemma 2 9B, Llama 3.1 8B, Qwen2.5 7B, and ...

</details>

<details>
<summary><b>21. WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Juelin Li, Jiajin Wu, Hexiang Wei, Jiongxu Chen, luyh20

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39278) • [📄 arXiv](https://arxiv.org/abs/2610.39278) • [📥 PDF](https://arxiv.org/pdf/2610.39278)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/worldflow-rbs/worldflow)

> WorldFlow jointly generates future video and explicit 3D motion, combining large-scale visual pretraining with geometric supervision for more generalizable motion prediction. WorldFlow is dedicated to scaling the generalization of explicit 3D obje...

</details>

<details>
<summary><b>22. MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40293) • [📄 arXiv](https://arxiv.org/abs/2610.40293) • [📥 PDF](https://arxiv.org/pdf/2610.40293)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ShengxuanQiu/MAServeBench)

> Multi-agent collaboration fundamentally reshapes LLM serving workloads through dynamic dependencies, synchronization, and context sharing—beyond what conventional request-level benchmarks can capture. We introduce MAServeBench , a benchmark featur...

</details>

<details>
<summary><b>23. Measuring AI Agents as Teammates with Collaborative Intelligence</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02633) • [📄 arXiv](https://arxiv.org/abs/2611.02633) • [📥 PDF](https://arxiv.org/pdf/2611.02633)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zou-group/collaborative-intelligence)

> Most benchmarks measure what a model can do on its own. We built the Collaborative Intelligence Benchmark to measure how well an AI agent works as a teammate . It has 240 tasks across 8 dimensions of teamwork, from refusing an unsafe shortcut to c...

</details>

<details>
<summary><b>24. TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Mengqi Guo, Seunghun Lee, Guanli Hou, Xiaoxu Zheng, Kehong Gong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41216) • [📄 arXiv](https://arxiv.org/abs/2610.41216) • [📥 PDF](https://arxiv.org/pdf/2610.41216)

**💻 Code:** [⭐ Code](https://github.com/Garfield-kh/TinyAstral) • [⭐ Code](https://github.com/huggingface)

> TinyAstral evolves the harness (tools, feedback, memory, recovery) of a frozen ~180B robot teacher through recursive self-improvement (33.4% → 63.6% on RoboTwin), then distills it into 0.8B–4B students that run in the same harness. The 4B student ...

</details>

<details>
<summary><b>25. Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and Evaluating Transfer</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41296) • [📄 arXiv](https://arxiv.org/abs/2610.41296) • [📥 PDF](https://arxiv.org/pdf/2610.41296)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Pushing self-improvement in small language models with auxiliary rewards

</details>

<details>
<summary><b>26. Lab2Sim: Turning Real-World Experiment Videos into Interactive Virtual Experiments</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02928) • [📄 arXiv](https://arxiv.org/abs/2611.02928) • [📥 PDF](https://arxiv.org/pdf/2611.02928)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/black1948/lab2sim)

> Science experiment videos demonstrate how experiments are performed, but offer no direct interaction for learners. Turning them into virtual experiments requires not only reproducing the observed apparatus and state changes, but also enforcing the...

</details>

<details>
<summary><b>27. Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Pascal Frossard, Sanae Lotfi, Ang Li, Abdellah Rahmani, smcleish

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03526) • [📄 arXiv](https://arxiv.org/abs/2611.03526) • [📥 PDF](https://arxiv.org/pdf/2611.03526)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/arahmani1/library-of-layers)

> Computer programmers chain together the same reusable computational primitives, for example, conditional statements or loops, but in different orders to implement different algorithms. In contrast, existing language model architectures always exec...

</details>

<details>
<summary><b>28. On-Policy Self-Distillation with Teacher Evolution</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.38637) • [📄 arXiv](https://arxiv.org/abs/2610.38637) • [📥 PDF](https://arxiv.org/pdf/2610.38637)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We wanted to solve a frustrating problem in On-Policy Self-Distillation (OPSD): the "self-teacher" model often gets blinded by the privileged context and gives pretty unreliable, overconfident token-level guidance, which ends up misleading the stu...

</details>

<details>
<summary><b>29. ProVe: Proposer-Verifier Decoding</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Qi She, Yujie Zhong, Jiaxi Li, Weiwen Xu, Ziqi Jin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.27815) • [📄 arXiv](https://arxiv.org/abs/2610.27815) • [📥 PDF](https://arxiv.org/pdf/2610.27815)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Speculative decoding lets a small model draft and a large model verify. ProVe reverses the roles: the large model proposes a block of 16 tokens in one forward pass, and a verifier reads it in one more.

</details>

<details>
<summary><b>30. Cross-Primitive Consistency in Jev</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenguan Wang, Kanzhi Wu, Guikun Chen, 67L11

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.38623) • [📄 arXiv](https://arxiv.org/abs/2610.38623) • [📥 PDF](https://arxiv.org/pdf/2610.38623)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/67L1/PrimaCons-CRPR)

> /

</details>

<details>
<summary><b>31. Multi-Agent Relay Thinking</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenguan Wang, Xiaojuan Qi, Guikun Chen, Jungang Qiao, 67L11

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35219) • [📄 arXiv](https://arxiv.org/abs/2610.35219) • [📥 PDF](https://arxiv.org/pdf/2610.35219)

**💻 Code:** [⭐ Code](https://github.com/67L1/MACR) • [⭐ Code](https://github.com/huggingface)

> /

</details>

<details>
<summary><b>32. Where Do Vision Language Models Fail at 3D Reasoning?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39639) • [📄 arXiv](https://arxiv.org/abs/2610.39639) • [📥 PDF](https://arxiv.org/pdf/2610.39639)

**💻 Code:** [⭐ Code](https://github.com/leduckhai/BedBench) • [⭐ Code](https://github.com/huggingface)

> Where Do Vision Language Models Fail at 3D Reasoning? Vision-language models can get individual judgments right while struggling to recover and consistently use the exact properties of a 3D object. To characterize this gap, we introduce BedBench, ...

</details>

<details>
<summary><b>33. LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02332) • [📄 arXiv](https://arxiv.org/abs/2611.02332) • [📥 PDF](https://arxiv.org/pdf/2611.02332)

**💻 Code:** [⭐ Code](https://github.com/DebarghaG/LeanGuard) • [⭐ Code](https://github.com/huggingface)

> Tool-using language-model agents often execute actions that their domain policies forbid. We present LeanGuard, a runtime that checks every proposed tool call against a policy written in Lean4 before the call reaches the environment. Policies comb...

</details>

<details>
<summary><b>34. TaoMate-FVSR:Audio-Guided Facial Video Restoration</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03393) • [📄 arXiv](https://arxiv.org/abs/2611.03393) • [📥 PDF](https://arxiv.org/pdf/2611.03393)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TaoLiveAIGC/TaoMate-FVSR)

> Low-quality facial videos suffer from missing fine details, while AI-generated videos may additionally contain implausible teeth and lip movements that do not match the speech. Restoring the mouth region is particularly challenging: enhancing exis...

</details>

<details>
<summary><b>35. Can Large Language Model Agents Learn by Watching Tutorial Videos?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01460) • [📄 arXiv](https://arxiv.org/abs/2611.01460) • [📥 PDF](https://arxiv.org/pdf/2611.01460)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can LLM agents learn from tutorial videos, just like humans do? 🎥🧠 We introduce Tutorial Agentic Learning (TAL), a non-parametric continual learning framework that enables frozen LLM agents to learn from instructional videos without updating model...

</details>

<details>
<summary><b>36. SIMIT: Self-Improving Vision-Language Models via Imagination at Test-Time</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00053) • [📄 arXiv](https://arxiv.org/abs/2611.00053) • [📥 PDF](https://arxiv.org/pdf/2611.00053)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/monurcan/simit_paper)

> SIMIT enables VLMs to improve themselves at test time by imagining and learning from similar problems, without annotations or external models.

</details>

<details>
<summary><b>37. When Morphs Look Better: Face Image Quality as a Training-Free Signal for Morphing Attack Detection</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00074) • [📄 arXiv](https://arxiv.org/abs/2611.00074) • [📥 PDF](https://arxiv.org/pdf/2611.00074)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/gurayozgur/FIQA-as-MAD)

> Face image quality assessment (FIQA) estimates the utility of a face image for face recognition and is trained without morphs. We evaluate 17 FIQA methods from all current FIQA categories as training-free single-image morphing attack detection (MA...

</details>

<details>
<summary><b>38. Can Coding Agents Sustain Continual Evolution without Forgetting?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jia Li, Yitong Zhang, zhaoshangziqi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03219) • [📄 arXiv](https://arxiv.org/abs/2611.03219) • [📥 PDF](https://arxiv.org/pdf/2611.03219)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/THU-Agent/continual-harness-evolution)

> We conduct a comprehensive empirical study of continual harness self-evolution on coding agents, revealing substantial catastrophic forgetting as harnesses evolve across different task distributions.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 38 |
| 📅 Today | [`2026-11-03.json`](data/daily/2026-11-03.json) | 38 |
| 📆 This Week | [`2026-W44.json`](data/weekly/2026-W44.json) | 68 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 107 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-03 | 38 | [View JSON](data/daily/2026-11-03.json) |
| 📄 2026-11-02 | 30 | [View JSON](data/daily/2026-11-02.json) |
| 📄 2026-11-01 | 39 | [View JSON](data/daily/2026-11-01.json) |
| 📄 2026-10-31 | 39 | [View JSON](data/daily/2026-10-31.json) |
| 📄 2026-10-30 | 30 | [View JSON](data/daily/2026-10-30.json) |
| 📄 2026-10-29 | 9 | [View JSON](data/daily/2026-10-29.json) |
| 📄 2026-10-28 | 40 | [View JSON](data/daily/2026-10-28.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W44 | 68 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 107 | [View JSON](data/monthly/2026-11.json) |
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
