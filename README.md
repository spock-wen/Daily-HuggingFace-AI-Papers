<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-32-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4962+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">140</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">140</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4962+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 04, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Cosmos 3: Omnimodal World Models for Physical AI</b> ⭐ 8.68k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02800) • [📄 arXiv](https://arxiv.org/abs/2606.02800) • [📥 PDF](https://arxiv.org/pdf/2606.02800)

**💻 Code:** [⭐ Code](https://github.com/NVIDIA/cosmos) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>2. Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02060) • [📄 arXiv](https://arxiv.org/abs/2606.02060) • [📥 PDF](https://arxiv.org/pdf/2606.02060)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NJU-LINK/DRIFT)

> No abstract available.

</details>

<details>
<summary><b>3. OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03890) • [📄 arXiv](https://arxiv.org/abs/2606.03890) • [📥 PDF](https://arxiv.org/pdf/2606.03890)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InternLM/OVO-S-Bench)

> Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. Existing benchmarks either evaluate offline over full videos or targe...

</details>

<details>
<summary><b>4. M^3Eval: Multi-Modal Memory Evaluation through Cognitively-Grounded Video Tasks</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05008) • [📄 arXiv](https://arxiv.org/abs/2606.05008) • [📥 PDF](https://arxiv.org/pdf/2606.05008)

**💻 Code:** [⭐ Code](https://github.com/PKU-VaLuE-Lab/m3eval) • [⭐ Code](https://github.com/huggingface)

> Code: https://github.com/PKU-VaLuE-Lab/m3eval

</details>

<details>
<summary><b>5. Qwen-Image-Flash: Beyond Objective Design</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03746) • [📄 arXiv](https://arxiv.org/abs/2606.03746) • [📥 PDF](https://arxiv.org/pdf/2606.03746)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Few-step distillation has become an effective strategy for accelerating advanced visual generative models, yet prior work has largely focused on distillation objectives. In this work, we revisit few-step distillation from a complementary perspecti...

</details>

<details>
<summary><b>6. Echo-Infinity: Learning Evolving Memory for Real-Time Infinite Video Generation</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Weiyang Jin, Shiyi Zhang, Songchun Zhang, Zeyue Xue, Yuxuan Bian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04527) • [📄 arXiv](https://arxiv.org/abs/2606.04527) • [📥 PDF](https://arxiv.org/pdf/2606.04527)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Infinity)

> Introducing Echo-Infinity 🚀 An autoregressive framework that moves toward real-time infinite video generation. Echo-Infinity is powered by two simple but effective recipes: ✨ an evolving learnable memory query ✨ unified relative RoPE across traini...

</details>

<details>
<summary><b>7. ThoughtFold: Folding Reasoning Chains via Introspective Preference Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03503) • [📄 arXiv](https://arxiv.org/abs/2606.03503) • [📥 PDF](https://arxiv.org/pdf/2606.03503)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ziyanliux/ThoughtFold)

> Folding redundant reasoning chains via introspective preference learning for efficient LRM inference. ( Accepted by ICML 2026 )

</details>

<details>
<summary><b>8. Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Juanzi Li, Hao Peng, Shuo Hou, Zhuoyuan Hao, Xuekang Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04923) • [📄 arXiv](https://arxiv.org/abs/2606.04923) • [📥 PDF](https://arxiv.org/pdf/2606.04923)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/THUAIS-Lab/CHERRL)

> Rubric-based RL uses an LLM-as-a-Judge (LaaJ) to score model outputs against rubrics as rewards. Policy models can exploit latent biases in the judge, leading to reward hacking and unsafe or ineffective training. In real-world settings these hacki...

</details>

<details>
<summary><b>9. Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27492) • [📄 arXiv](https://arxiv.org/abs/2605.27492) • [📥 PDF](https://arxiv.org/pdf/2605.27492)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Nexa-Language/RAMP)

> 🚀 Benchmarks are Not Enough: RAMP for Evaluating Agentic Models in Real-World Production Systems with RAMP Hi Hugging Face Community! 👋 We are excited to share our latest work that challenges the current paradigm of LLM agent evaluation benchmarks...

</details>

<details>
<summary><b>10. Streaming Communication in Multi-Agent Reasoning</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Xander Xu, Cong Chen, Wen Wang, Xiaogang Xu, Zhen Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05158) • [📄 arXiv](https://arxiv.org/abs/2606.05158) • [📥 PDF](https://arxiv.org/pdf/2606.05158)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EnVision-Research/StreamMA)

> Streaming reasoning steps between multi-agents makes the pipeline both faster and more accurate, and reveals a new step-level scaling law. We warmly welcome feedback, comments, and constructive criticism from the community.

</details>

<details>
<summary><b>11. MemTrain: Self-Supervised Context Memory Training</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yehui Tang, Zhi-Hong Deng, Haoqing Wang, Xingrun Xing, Ziheng Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03197) • [📄 arXiv](https://arxiv.org/abs/2606.03197) • [📥 PDF](https://arxiv.org/pdf/2606.03197)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A simple yet effective approach to enhancing agent memory in a general-purpose manner. By performing self-supervised training solely on Wikipedia, it produces a stronger starter checkpoint that substantially improves the effectiveness of subsequen...

</details>

<details>
<summary><b>12. Eliciting Complex Spatial Reasoning in MLLMs through Wide-Baseline Matching</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03577) • [📄 arXiv](https://arxiv.org/abs/2606.03577) • [📥 PDF](https://arxiv.org/pdf/2606.03577)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aim-uofa/ReasonMatch)

> ReasonMatch turns wide-baseline matching into a verifiable RL task for MLLMs. An 8B model trained with DCRL hits 70.5 F1 and beats GPT-5-mini on ReasonMatch-Bench—nice evidence that geometric supervision + RL can unlock spatial reasoning without C...

</details>

<details>
<summary><b>13. MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01993) • [📄 arXiv](https://arxiv.org/abs/2606.01993) • [📥 PDF](https://arxiv.org/pdf/2606.01993)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NJU-LINK/MMG2Skill)

> Abundant procedural knowledge on the Web holds great potential for helping agents solve long-horizon tasks. However, such knowledge is often multimodal, heterogeneous, noisy, and implicitly assumes human executors, making it difficult to use direc...

</details>

<details>
<summary><b>14. AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation</b> ⭐ 27</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03972) • [📄 arXiv](https://arxiv.org/abs/2606.03972) • [📥 PDF](https://arxiv.org/pdf/2606.03972)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AutoLab-SAI-SJTU/AAD-1)

> We present AAD-1, an Asymmetric Adversarial Distillation framework for One-step autoregressive image-to-video generation. State-of-the-art methods adopt adversarial distillation but suffer from motion collapse and training instability, resulting i...

</details>

<details>
<summary><b>15. MapAgent: An Industrial-Grade Agentic Framework for City-scale Lane-level Map Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04513) • [📄 arXiv](https://arxiv.org/abs/2606.04513) • [📥 PDF](https://arxiv.org/pdf/2606.04513)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/eadst/KDD-2026-MapAgent)

> Lane-level maps are critical infrastructure for autonomous driving and lane-level navigation, yet constructing and maintaining standardized lane networks for hundreds of cities remains highly labor-intensive. Recent end-to-end vectorized mapping m...

</details>

<details>
<summary><b>16. Self-Distilled Policy Gradient</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04036) • [📄 arXiv](https://arxiv.org/abs/2606.04036) • [📥 PDF](https://arxiv.org/pdf/2606.04036)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lauyikfung/SDPG)

> On-policy self-distillation, where a language model conditions on privileged context to supervise its own generations, is a promising source of dense supervision for sparse-reward reinforcement learning. Actually, it can be instantiated as an auxi...

</details>

<details>
<summary><b>17. Filter, Then Reweight: Rethinking Optimization Granularity in On-Policy Distillation</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02684) • [📄 arXiv](https://arxiv.org/abs/2606.02684) • [📥 PDF](https://arxiv.org/pdf/2606.02684)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YuYingLi0/FiRe-OPD)

> Code: https://github.com/YuYingLi0/FiRe-OPD

</details>

<details>
<summary><b>18. Audio Interaction Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yue Liao, Xiaobin Hu, Ze An, Zihang Liu, Zhifei Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05121) • [📄 arXiv](https://arxiv.org/abs/2606.05121) • [📥 PDF](https://arxiv.org/pdf/2606.05121)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The paper presents Audio-Interaction, a unified streaming model for real-time audio interaction, accompanied by the SoundFlow framework, the StreamAudio-2M dataset, and new benchmarks for proactive audio intervention. Video: https://www.youtube.co...

</details>

<details>
<summary><b>19. WebRISE: Requirement-Induced State Evaluation for MLLM-Generated Web Artifacts</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03220) • [📄 arXiv](https://arxiv.org/abs/2606.03220) • [📥 PDF](https://arxiv.org/pdf/2606.03220)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/IIGROUP/WebRISE)

> Existing benchmarks for MLLM-generated web artifacts assess interaction through local evidence and miss the requirement-induced states and transitions that determine whether a page works. We introduce WebRISE, which compiles task requirements into...

</details>

<details>
<summary><b>20. AUDITFLOW: Executable Symbolic Environments for Structured Financial Reporting Verification</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03031) • [📄 arXiv](https://arxiv.org/abs/2606.03031) • [📥 PDF](https://arxiv.org/pdf/2606.03031)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Structured financial audit verification is difficult for language-model agents because correctness depends on structured evidence rather than text alone. A model must link reported facts to taxonomy concepts, traverse calculation or dimensional re...

</details>

<details>
<summary><b>21. AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?</b> ⭐ 84</summary>

<br/>

**👥 Authors:** Jiefeng Chen, Dongfu Jiang, Yue Huang, Junda Chen, Zhangchen Xu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05080) • [📄 arXiv](https://arxiv.org/abs/2606.05080) • [📥 PDF](https://arxiv.org/pdf/2606.05080)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/autolabhq/autolab)

> No abstract available.

</details>

<details>
<summary><b>22. GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05160) • [📄 arXiv](https://arxiv.org/abs/2606.05160) • [📥 PDF](https://arxiv.org/pdf/2606.05160)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NVlabs/GRAIL)

> GRAIL is a digital pipeline that synthesizes humanoid loco-manipulation data from 3D assets and video priors, facilitating sim-to-real training of visual robot policies for complex real-world navigation and manipulation.

</details>

<details>
<summary><b>23. BraveGuard: From Open-World Threats to Safer Computer-Use Agents</b> ⭐ 27</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01166) • [📄 arXiv](https://arxiv.org/abs/2606.01166) • [📥 PDF](https://arxiv.org/pdf/2606.01166)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yunhao-Feng/BraveGuard)

> Computer-use agents extend language models from text generation to sustained interaction with files, terminals, browsers, and external tools. This shift creates safety risks that are difficult to detect from isolated prompts or final responses, be...

</details>

<details>
<summary><b>24. BenchEvolver: Frontier Task Synthesis via Solution-Centric Evolution</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01286) • [📄 arXiv](https://arxiv.org/abs/2606.01286) • [📥 PDF](https://arxiv.org/pdf/2606.01286)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/thu-wyz/BenchEvolver)

> Static benchmarks are rapidly saturating as frontier LLMs improve. On LiveCodeBench, frontier models now exceed 99% Pass@1 on easy splits and over 90% on average, making it harder to distinguish strong coding models or obtain useful training signa...

</details>

<details>
<summary><b>25. Access Sets Matter: Budgeting Expert Reads for Scalable Weight-Space Model Merging</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.29489) • [📄 arXiv](https://arxiv.org/abs/2605.29489) • [📥 PDF](https://arxiv.org/pdf/2605.29489)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wyy-code/mergepipe)

> MergePipe is the first parameter management and execution system for large-scale LLM merging. It reframes LLM merging as a data management problem, rather than a one-off script execution: explicitly model expert parameter reads as a budgeted resou...

</details>

<details>
<summary><b>26. OpenSTBench: Beyond Semantic Evaluation for Speech Translation</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Yujie Tu, Qixi Zheng, Yichi Zhang, Yuxiang Zhao, Yanjie An

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.30792) • [📄 arXiv](https://arxiv.org/abs/2605.30792) • [📥 PDF](https://arxiv.org/pdf/2605.30792)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sjtuayj/OpenSTBench)

> submitted to EMNLP 2026

</details>

<details>
<summary><b>27. STRIDE: Training Data Attribution via Sparse Recovery from Subset Perturbations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Amirali Abdullah, Florent Draye, Luke Zhang, Abir Harrasse, Rishit Dagli

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05165) • [📄 arXiv](https://arxiv.org/abs/2606.05165) • [📥 PDF](https://arxiv.org/pdf/2606.05165)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>28. Unlocking Feature Learning in Gated Delta Networks at Scale</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04048) • [📄 arXiv](https://arxiv.org/abs/2606.04048) • [📥 PDF](https://arxiv.org/pdf/2606.04048)

**💻 Code:** [⭐ Code](https://github.com/lauyikfung/gated_delta_net_mup) • [⭐ Code](https://github.com/huggingface)

> Training and scaling Large Language Models demand enormous computational resources, motivating both efficient sub-quadratic architectures and principled hyperparameter tuning methods. While the Maximal Update Parametrization (μP) has enabled zero-...

</details>

<details>
<summary><b>29. Deep Embedded Multiplicative DMD for Algebra-Preserving Koopman Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05131) • [📄 arXiv](https://arxiv.org/abs/2606.05131) • [📥 PDF](https://arxiv.org/pdf/2606.05131)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Koopman theory turns nonlinear dynamics into a linear spectral problem. In computation, however, everything depends on a hard finite-dimensional choice: the observables must be expressive, nearly invariant under the dynamics, and, ideally, compati...

</details>

<details>
<summary><b>30. MeshWeaver: Sparse-Voxel-Guided Surface Weaving for Autoregressive Mesh Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ying Shan, Wang Zhao, Jiale Xu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04688) • [📄 arXiv](https://arxiv.org/abs/2606.04688) • [📥 PDF](https://arxiv.org/pdf/2606.04688)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>31. Economy of Minds: Emerging Multi-Agent Intelligence with Economic Interactions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02859) • [📄 arXiv](https://arxiv.org/abs/2606.02859) • [📥 PDF](https://arxiv.org/pdf/2606.02859)

**💻 Code:** [⭐ Code](https://github.com/zhentingqi/EoM) • [⭐ Code](https://github.com/huggingface)

> We introduce Economy of Minds (EoM): Agents compete, trade, get wealthy, go bankrupt, and mutate, forming an evolving society where coordination and adaptation automatically emerge in a decentralized manner.

</details>

<details>
<summary><b>32. Score-Control for Hallucination Reduction in Diffusion Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vishnu Suresh Lokhande, Chau Pham, Abdul Wasi, Naresh Kumar Devulapally, Mahesh Bhosale

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00377) • [📄 arXiv](https://arxiv.org/abs/2606.00377) • [📥 PDF](https://arxiv.org/pdf/2606.00377)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bhosalems/VSM)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 32 |
| 📅 Today | [`2026-06-04.json`](data/daily/2026-06-04.json) | 32 |
| 📆 This Week | [`2026-W22.json`](data/weekly/2026-W22.json) | 140 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 140 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-04 | 32 | [View JSON](data/daily/2026-06-04.json) |
| 📄 2026-06-03 | 21 | [View JSON](data/daily/2026-06-03.json) |
| 📄 2026-06-02 | 44 | [View JSON](data/daily/2026-06-02.json) |
| 📄 2026-06-01 | 43 | [View JSON](data/daily/2026-06-01.json) |
| 📄 2026-05-31 | 59 | [View JSON](data/daily/2026-05-31.json) |
| 📄 2026-05-30 | 59 | [View JSON](data/daily/2026-05-30.json) |
| 📄 2026-05-29 | 43 | [View JSON](data/daily/2026-05-29.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W22 | 140 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |
| 📅 2026-W20 | 243 | [View JSON](data/weekly/2026-W20.json) |
| 📅 2026-W19 | 310 | [View JSON](data/weekly/2026-W19.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 140 | [View JSON](data/monthly/2026-06.json) |
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
