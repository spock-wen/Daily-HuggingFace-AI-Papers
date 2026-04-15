<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-47-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3486+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">56</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">325</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3486+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** April 15, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. QuanBench+: A Unified Multi-Framework Benchmark for LLM-Based Quantum Code Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.08570) • [📄 arXiv](https://arxiv.org/abs/2604.08570) • [📥 PDF](https://arxiv.org/pdf/2604.08570)

**💻 Code:** [⭐ Code](https://github.com/JawadKotaichh/quanbench-plus)

> QuanBench+ is a new benchmark for LLM-based quantum code generation across multiple frameworks. Our goal is to make evaluation more unified, reproducible, and meaningful with canonical solutions, pass@k analysis, and KL-based output checking. Woul...

</details>

<details>
<summary><b>2. The Past Is Not Past: Memory-Enhanced Dynamic Reward Shaping</b> ⭐ 90</summary>

<br/>

**👥 Authors:** Bo Wang, Weixin Zhang, Yufei Gao, Enxi Wang, Yang Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11297) • [📄 arXiv](https://arxiv.org/abs/2604.11297) • [📥 PDF](https://arxiv.org/pdf/2604.11297)

**💻 Code:** [⭐ Code](https://github.com/Linxi000/MEDS)

> We find that, in RL training, large language models often do not make mistakes at random. Instead, they tend to fall back into the same kinds of traps again and again. Even after long training, they can still return to familiar failure paths. A ke...

</details>

<details>
<summary><b>3. OmniShow: Unifying Multimodal Conditions for Human-Object Interaction Video Generation</b> ⭐ 70</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11804) • [📄 arXiv](https://arxiv.org/abs/2604.11804) • [📥 PDF](https://arxiv.org/pdf/2604.11804)

**💻 Code:** [⭐ Code](https://github.com/Correr-Zhou/OmniShow)

> 🔥 Introducing OmniShow , an all-in-one model for Human-Object Interaction Video Generation. Project page: https://correr-zhou.github.io/OmniShow Paper: https://arxiv.org/pdf/2604.11804 GitHub repo: https://github.com/Correr-Zhou/OmniShow HOIVG-Ben...

</details>

<details>
<summary><b>4. Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation</b> ⭐ 34</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10098) • [📄 arXiv](https://arxiv.org/abs/2604.10098) • [📥 PDF](https://arxiv.org/pdf/2604.10098)

**💻 Code:** [⭐ Code](https://github.com/ZunhaiSu/Awesome-Attention-Sink)

> Excited to share our first survey on Attention Sink — Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation 🚀 📌 We systematically reviewed 180+ papers and identified a clear evolutionary trajectory: 1️⃣ Fundamenta...

</details>

<details>
<summary><b>5. Strips as Tokens: Artist Mesh Generation with Native UV Segmentation</b> ⭐ 73</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.09132) • [📄 arXiv](https://arxiv.org/abs/2604.09132) • [📥 PDF](https://arxiv.org/pdf/2604.09132)

**💻 Code:** [⭐ Code](https://github.com/Xrvitd/SATO)

> Today we're releasing Strips as Tokens (SATO) , a new autoregressive framework for artist mesh generation with native UV segmentation . Most existing mesh generators use token orderings that do not match how artists actually build meshes. Coordina...

</details>

<details>
<summary><b>6. Uni-ViGU: Towards Unified Video Generation and Understanding via A Diffusion-Based Video Generator</b> ⭐ 16</summary>

<br/>

**👥 Authors:** Li Xu, Tianjiao Li, Jia Gong, joeqianqian, Fr0zencr4nE

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.08121) • [📄 arXiv](https://arxiv.org/abs/2604.08121) • [📥 PDF](https://arxiv.org/pdf/2604.08121)

**💻 Code:** [⭐ Code](https://github.com/Fr0zenCrane/Uni-ViGU)

> Here's an interesting observation that motivated this work: video generation is computationally much more expensive than video understanding. So why do most unified multimodal models start with understanding-focused architectures (like MLLMs) and ...

</details>

<details>
<summary><b>7. Pseudo-Unification: Entropy Probing Reveals Divergent Information Patterns in Unified Multimodal Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10949) • [📄 arXiv](https://arxiv.org/abs/2604.10949) • [📥 PDF](https://arxiv.org/pdf/2604.10949)

> Unified multimodal models (UMMs) were designed to combine the reasoning ability of large language models (LLMs) with the generation capability of vision models. In practice, however, this synergy remains elusive: UMMs fail to transfer LLM-like rea...

</details>

<details>
<summary><b>8. CocoaBench: Evaluating Unified Digital Agents in the Wild</b> ⭐ 23</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11201) • [📄 arXiv](https://arxiv.org/abs/2604.11201) • [📥 PDF](https://arxiv.org/pdf/2604.11201)

**💻 Code:** [⭐ Code](https://github.com/cocoabench/cocoa-agent)

> We present CocoaBench, a benchamark the requires unified digital agents to combine search, coding, and vision to solve. Project page: https://cocoabench.github.io/

</details>

<details>
<summary><b>9. CodeTracer: Towards Traceable Agent States</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11641) • [📄 arXiv](https://arxiv.org/abs/2604.11641) • [📥 PDF](https://arxiv.org/pdf/2604.11641)

**💻 Code:** [⭐ Code](https://github.com/NJU-LINK/CodeTracer)

> We present CodeTracer, a tracing architecture that parses heterogeneous run artifacts through evolving extractors, reconstructs the full state transition history as a hierarchical trace tree with persistent memory, and performs failure onset local...

</details>

<details>
<summary><b>10. Audio Flamingo Next: Next-Generation Open Audio-Language Models for Speech, Sound, and Music</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10905) • [📄 arXiv](https://arxiv.org/abs/2604.10905) • [📥 PDF](https://arxiv.org/pdf/2604.10905)

> AF-Next is a next-generation open large audio-language model for understanding and reasoning over speech, sounds, and music, with strong long-audio and time-grounded reasoning capabilities.

</details>

<details>
<summary><b>11. Introspective Diffusion Language Models</b> ⭐ 69</summary>

<br/>

**👥 Authors:** Donglin Zhuang, Zhongzhu Zhou, Junxiong Wang, Yuqing Jian, Yifan Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11035) • [📄 arXiv](https://arxiv.org/abs/2604.11035) • [📥 PDF](https://arxiv.org/pdf/2604.11035)

**💻 Code:** [⭐ Code](https://github.com/Introspective-Diffusion/I-DLM)

> No abstract available.

</details>

<details>
<summary><b>12. Tracing the Roots: A Multi-Agent Framework for Uncovering Data Lineage in Post-Training LLMs</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10480) • [📄 arXiv](https://arxiv.org/abs/2604.10480) • [📥 PDF](https://arxiv.org/pdf/2604.10480)

**💻 Code:** [⭐ Code](https://github.com/Leey21/data-lineage)

> Post-training data plays a pivotal role in shaping the capabilities of Large Language Models (LLMs), yet datasets are often treated as isolated artifacts, overlooking the systemic connections that underlie their evolution. To disentangle these com...

</details>

<details>
<summary><b>13. Solving Physics Olympiad via Reinforcement Learning on Physics Simulators</b> ⭐ 12</summary>

<br/>

**👥 Authors:** Nikash Bhardwaj, Zheyang Qin, Yangmin Li, Aryan Satpathy, Mihir Prabhudesai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11805) • [📄 arXiv](https://arxiv.org/abs/2604.11805) • [📥 PDF](https://arxiv.org/pdf/2604.11805)

**💻 Code:** [⭐ Code](https://github.com/Sim2Reason/Sim2Reason)

> This work seems promising for toy settings...My question to the authors would be: Would Frontier benefit from adopting the data generation process at scale?

</details>

<details>
<summary><b>14. Prompt Relay: Inference-Time Temporal Control for Multi-Event Video Generation</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10030) • [📄 arXiv](https://arxiv.org/abs/2604.10030) • [📥 PDF](https://arxiv.org/pdf/2604.10030)

**💻 Code:** [⭐ Code](https://github.com/GordonChen19/Prompt-Relay)

> Existing video generation models do not have mechanisms to support fine-grained temporal control in multi-event video generation. To this end, we propose Prompt Relay, an inference-time, training-free, plug-and-play method to support granular cont...

</details>

<details>
<summary><b>15. TRACE: Capability-Targeted Agentic Training</b> ⭐ 28</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.05336) • [📄 arXiv](https://arxiv.org/abs/2604.05336) • [📥 PDF](https://arxiv.org/pdf/2604.05336)

**💻 Code:** [⭐ Code](https://github.com/ScalingIntelligence/TRACE)

> Large Language Models (LLMs) deployed in agentic environments must exercise multiple capabilities across different task instances, where a capability is performing one or more actions in a trajectory that are necessary for successfully solving a s...

</details>

<details>
<summary><b>16. Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Danqi Chen, Xi Ye, Howard Yen, Yoonsang Lee

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11753) • [📄 arXiv](https://arxiv.org/abs/2604.11753) • [📥 PDF](https://arxiv.org/pdf/2604.11753)

> We study parallel test-time scaling for long-horizon agentic tasks such as agentic search and deep research, where multiple rollouts are generated in parallel and aggregated into a final response. While such scaling has proven effective for chain-...

</details>

<details>
<summary><b>17. Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yibo Shi, Shidong Pan, Dongliang Xu, Jungang Li, Zhixin Lin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11259) • [📄 arXiv](https://arxiv.org/abs/2604.11259) • [📥 PDF](https://arxiv.org/pdf/2604.11259)

> We introduce a new framework for personalized mobile GUI agents : modeling personalization as persona-consistent trajectory selection, building a privacy-preference dataset with variable-length and structurally diverse trajectory annotations, and ...

</details>

<details>
<summary><b>18. From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Chenchen Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.09459) • [📄 arXiv](https://arxiv.org/abs/2604.09459) • [📥 PDF](https://arxiv.org/pdf/2604.09459)

**💻 Code:** [⭐ Code](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)

> survey paper: From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models

</details>

<details>
<summary><b>19. Efficient RL Training for LLMs with Experience Replay</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.08706) • [📄 arXiv](https://arxiv.org/abs/2604.08706) • [📥 PDF](https://arxiv.org/pdf/2604.08706)

> Experience replay can cut LLM RL training compute by up to ~40% (without hurting final accuracy—and sometimes improving it). Experience replay (reusing past rollouts) is a staple of classical RL, but is still underexplored in LLM post-training—whe...

</details>

<details>
<summary><b>20. SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding</b> ⭐ 2.47k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.09557) • [📄 arXiv](https://arxiv.org/abs/2604.09557) • [📥 PDF](https://arxiv.org/pdf/2604.09557)

**💻 Code:** [⭐ Code](https://github.com/NVIDIA/Model-Optimizer)

> SPEED-Bench ( SPE culative E valuation D ataset) is a unified benchmark designed to evaluate speculative decoding (SD) across diverse semantic domains and realistic serving regimes, using production-grade inference engines. It measures both accept...

</details>

<details>
<summary><b>21. General365: Benchmarking General Reasoning in Large Language Models Across Diverse and Challenging Tasks</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11778) • [📄 arXiv](https://arxiv.org/abs/2604.11778) • [📥 PDF](https://arxiv.org/pdf/2604.11778)

**💻 Code:** [⭐ Code](https://github.com/meituan-longcat/General365)

> Github Repo: https://github.com/meituan-longcat/General365 Huggingface Dataset: https://huggingface.co/datasets/meituan-longcat/General365_Public Arxiv Paper: https://arxiv.org/abs/2604.11778 Project Page: https://general365.github.io/

</details>

<details>
<summary><b>22. Not All Denoising Steps Are Equal: Model Scheduling for Faster Masked Diffusion Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Valentin Malykh, Nikita Sorokin, Ivan Sedykh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.02340) • [📄 arXiv](https://arxiv.org/abs/2604.02340) • [📥 PDF](https://arxiv.org/pdf/2604.02340)

> We are excited to share our recent work on denoising step importance and model scheduling for Masked Diffusion Language Models (MDLMs).

</details>

<details>
<summary><b>23. Zero-shot World Models Are Developmentally Efficient Learners</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10333) • [📄 arXiv](https://arxiv.org/abs/2604.10333) • [📥 PDF](https://arxiv.org/pdf/2604.10333)

**💻 Code:** [⭐ Code](https://github.com/awwkl/ZWM)

> Today's best AI needs orders of magnitude more data than a human child to achieve visual competence. We introduce the Zero-shot World Model (ZWM), an approach that substantially narrows this gap. Even when trained on the first-person experience of...

</details>

<details>
<summary><b>24. Continuous Adversarial Flow Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11521) • [📄 arXiv](https://arxiv.org/abs/2604.11521) • [📥 PDF](https://arxiv.org/pdf/2604.11521)

> We propose continuous adversarial flow models, a type of continuous-time flow model trained with an adversarial objective. Unlike flow matching, which uses a fixed mean-squared-error criterion, our approach introduces a learned discriminator to gu...

</details>

<details>
<summary><b>25. SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adaptive Weighting</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaoliang Fu, Jingqing Ruan, Yiheng Liang, Xing Ma, Binbin Zheng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10688) • [📄 arXiv](https://arxiv.org/abs/2604.10688) • [📥 PDF](https://arxiv.org/pdf/2604.10688)

> No abstract available.

</details>

<details>
<summary><b>26. TorchUMM: A Unified Multimodal Model Codebase for Evaluation, Analysis, and Post-training</b> ⭐ 38</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10784) • [📄 arXiv](https://arxiv.org/abs/2604.10784) • [📥 PDF](https://arxiv.org/pdf/2604.10784)

**💻 Code:** [⭐ Code](https://github.com/AIFrontierLab/TorchUMM)

> The first unified codebase for unified multimodal models

</details>

<details>
<summary><b>27. Eliciting Medical Reasoning with Knowledge-enhanced Data Synthesis: A Semi-Supervised Reinforcement Learning Approach</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Ya Zhang, Jiangchao Yao, Ruipeng Zhang, Shuyang Jiang, tdlhl

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11547) • [📄 arXiv](https://arxiv.org/abs/2604.11547) • [📥 PDF](https://arxiv.org/pdf/2604.11547)

**💻 Code:** [⭐ Code](https://github.com/tdlhl/MedSSR)

> Accepted to ACL 2026 as a Findings paper

</details>

<details>
<summary><b>28. Advancing Polish Language Modeling through Tokenizer Optimization in the Bielik v3 7B and 11B Series</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10799) • [📄 arXiv](https://arxiv.org/abs/2604.10799) • [📥 PDF](https://arxiv.org/pdf/2604.10799)

> The development of the Bielik v3 PL series, encompassing both the 7B and 11B parameter variants, represents a significant milestone in the field of language-specific large language model (LLM) optimization. While general-purpose models often demon...

</details>

<details>
<summary><b>29. Playing Along: Learning a Double-Agent Defender for Belief Steering via Theory of Mind</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Elias Stengel-Eskin, Hyunji Lee, Zaid Khan, Vaidehi Patil, Hanqi Xiao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11666) • [📄 arXiv](https://arxiv.org/abs/2604.11666) • [📥 PDF](https://arxiv.org/pdf/2604.11666)

**💻 Code:** [⭐ Code](https://github.com/The-Inscrutable-X/AIDoubleAgentDefenders)

> We study a multi-turn adversarial dialogue setting where a defender must act as a double agent 🕵️ — not refusing, but proactively steering the attacker toward a plausible but false conclusion, without getting caught. This requires maintaining a th...

</details>

<details>
<summary><b>30. SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning Context</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11716) • [📄 arXiv](https://arxiv.org/abs/2604.11716) • [📥 PDF](https://arxiv.org/pdf/2604.11716)

**💻 Code:** [⭐ Code](https://github.com/KDEGroup/SWE-AGILE)

> We propose SWE-AGILE, a novel software agent framework designed to bridge the gap between reasoning depth, efficiency, and context constraints. SWE-AGILE introduces a Dynamic Reasoning Context strategy, maintaining a “sliding window” of detailed r...

</details>

<details>
<summary><b>31. Low-rank Optimization Trajectories Modeling for LLM RLVR Acceleration</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11446) • [📄 arXiv](https://arxiv.org/abs/2604.11446) • [📥 PDF](https://arxiv.org/pdf/2604.11446)

**💻 Code:** [⭐ Code](https://github.com/RUCAIBox/NExt)

> We investigate the evolution of LLMs during RLVR training, and propose the Nonlinear Extrapolation of low-rank trajectories (NExt), a novel framework that models and extrapolates low-rank parameter trajectories in a nonlinear manner.

</details>

<details>
<summary><b>32. Learning Long-term Motion Embeddings for Efficient Kinematics Generation</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11737) • [📄 arXiv](https://arxiv.org/abs/2604.11737) • [📥 PDF](https://arxiv.org/pdf/2604.11737)

**💻 Code:** [⭐ Code](https://github.com/CompVis/long-term-motion)

> Are you working with trajectories already to model motion more efficiently? Consider using our first stage to embed them!

</details>

<details>
<summary><b>33. BMdataset: A Musicologically Curated LilyPond Dataset</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10628) • [📄 arXiv](https://arxiv.org/abs/2604.10628) • [📥 PDF](https://arxiv.org/pdf/2604.10628)

**💻 Code:** [⭐ Code](https://github.com/CSCPadova/lilybert)

> We release lilybert a codebert based model specialized on lilypond.

</details>

<details>
<summary><b>34. DiningBench: A Hierarchical Multi-view Benchmark for Perception and Reasoning in the Dietary Domain</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10425) • [📄 arXiv](https://arxiv.org/abs/2604.10425) • [📥 PDF](https://arxiv.org/pdf/2604.10425)

**💻 Code:** [⭐ Code](https://github.com/meituan/DiningBench)

> Recent advancements in Vision-Language Models (VLMs) have revolutionized general visual understanding. However, their application in the food domain remains constrained by benchmarks that rely on coarse-grained categories, single-view imagery, and...

</details>

<details>
<summary><b>35. SciPredict: Can LLMs Predict the Outcomes of Scientific Experiments in Natural Sciences?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10718) • [📄 arXiv](https://arxiv.org/abs/2604.10718) • [📥 PDF](https://arxiv.org/pdf/2604.10718)

**💻 Code:** [⭐ Code](https://github.com/scaleapi/scipredict)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Machines acquire scientific taste from institutional traces (2026) PreScien...

</details>

<details>
<summary><b>36. TAIHRI: Task-Aware 3D Human Keypoints Localization for Close-Range Human-Robot Interaction</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.08921) • [📄 arXiv](https://arxiv.org/abs/2604.08921) • [📥 PDF](https://arxiv.org/pdf/2604.08921)

**💻 Code:** [⭐ Code](https://github.com/Tencent/TAIHRI)

> The project page is https://github.com/Tencent/TAIHRI

</details>

<details>
<summary><b>37. Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge Graphs and Agentic Memory</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11544) • [📄 arXiv](https://arxiv.org/abs/2604.11544) • [📥 PDF](https://arxiv.org/pdf/2604.11544)

> Structured memory representations such as knowledge graphs are central to autonomous agents and other long-lived systems. However, most existing approaches model time as discrete metadata, either sorting by recency (burying old-yet-permanent knowl...

</details>

<details>
<summary><b>38. Panoptic Pairwise Distortion Graph</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Bahador Rashidi, Abdul Wahab, Muhammad Kamran Janjua

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11004) • [📄 arXiv](https://arxiv.org/abs/2604.11004) • [📥 PDF](https://arxiv.org/pdf/2604.11004)

**💻 Code:** [⭐ Code](https://github.com/AISmartPerception/distortion-graphs)

> In this work, we introduce a new perspective on comparative image assessment by representing an image pair as a structured composition of its regions. In contrast, existing methods focus on whole image analysis, while implicitly relying on region-...

</details>

<details>
<summary><b>39. Polyglot Teachers: Evaluating Language Models for Multilingual Synthetic Data Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11290) • [📄 arXiv](https://arxiv.org/abs/2604.11290) • [📥 PDF](https://arxiv.org/pdf/2604.11290)

**💻 Code:** [⭐ Code](https://github.com/ljvmiranda921/polyglot-teachers)

> We systematically characterize what makes a good teacher model for multilingual synthetic data generation, generating over 1.4M SFT instances and training 100+ student models across six languages.

</details>

<details>
<summary><b>40. ADD for Multi-Bit Image Watermarking</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jie Ding, lainmn

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11491) • [📄 arXiv](https://arxiv.org/abs/2604.11491) • [📥 PDF](https://arxiv.org/pdf/2604.11491)

> Watermarking

</details>

<details>
<summary><b>41. Audio-Omni: Extending Multi-modal Understanding to Versatile Audio Generation and Editing</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10708) • [📄 arXiv](https://arxiv.org/abs/2604.10708) • [📥 PDF](https://arxiv.org/pdf/2604.10708)

**💻 Code:** [⭐ Code](https://github.com/ZeyueT/Audio-Omni)

> Audio-Omni is the first unified framework for multimodal audio understanding, generation, and editing across general sound, music, and speech.

</details>

<details>
<summary><b>42. Counting to Four is still a Chore for VLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10039) • [📄 arXiv](https://arxiv.org/abs/2604.10039) • [📥 PDF](https://arxiv.org/pdf/2604.10039)

**💻 Code:** [⭐ Code](https://github.com/leduy99/-CVPRW26-Modality-Attention-Share)

> Vision-language models are improving incredibly fast, and they are often celebrated for reaching near expert-level performance on many challenging tasks. But I think there is an important question we should keep asking: 𝘼𝙧𝙚 𝙩𝙝𝙚𝙮 𝙧𝙚𝙖𝙡𝙡𝙮 𝙨𝙩𝙧𝙤𝙣𝙜 𝙖𝙘𝙧𝙤...

</details>

<details>
<summary><b>43. SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.09212) • [📄 arXiv](https://arxiv.org/abs/2604.09212) • [📥 PDF](https://arxiv.org/pdf/2604.09212)

**💻 Code:** [⭐ Code](https://github.com/lhannnn/SPASM)

> No abstract available.

</details>

<details>
<summary><b>44. How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Gregory N. Frank

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.04385) • [📄 arXiv](https://arxiv.org/abs/2604.04385) • [📥 PDF](https://arxiv.org/pdf/2604.04385)

**💻 Code:** [⭐ Code](https://github.com/gregfrank/how-alignment-routes)

> This paper identifies the attention-level circuit responsible for refusal in aligned-trained language models. A 'gate' attention head at intermediate depth reads detected content and triggers downstream 'amplifier' heads that boost the output towa...

</details>

<details>
<summary><b>45. SHARE: Social-Humanities AI for Research and Education</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11152) • [📄 arXiv](https://arxiv.org/abs/2604.11152) • [📥 PDF](https://arxiv.org/pdf/2604.11152)

**💻 Code:** [⭐ Code](https://github.com/Joaoffg/SHARE)

> SHARE is a family of causal LLMs pretrained specifically for the socials sciences and humanities. Besides intermediate checkpoints of the models, we also release a new Cloze benchmark and a user interface. Any feedback is much appreciated, especia...

</details>

<details>
<summary><b>46. IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ke Li, Martin Ester, Qitong Wang, Yuzhen Mao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.10539) • [📄 arXiv](https://arxiv.org/abs/2604.10539) • [📥 PDF](https://arxiv.org/pdf/2604.10539)

**💻 Code:** [⭐ Code](https://github.com/yuzhenmao/IceCache)

> KV-cache Management (ICLR 2026)

</details>

<details>
<summary><b>47. ATANT: An Evaluation Framework for AI Continuity</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06710) • [📄 arXiv](https://arxiv.org/abs/2604.06710) • [📥 PDF](https://arxiv.org/pdf/2604.06710)

**💻 Code:** [⭐ Code](https://github.com/Kenotic-Labs/ATANT)

> ATANT defines continuity as a system property with 7 required properties and introduces the first LLM-free evaluation methodology for AI continuity systems. Includes a 250-story narrative corpus and 10-checkpoint evaluation protocol. Reference imp...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 47 |
| 📅 Today | [`2026-04-15.json`](data/daily/2026-04-15.json) | 47 |
| 📆 This Week | [`2026-W15.json`](data/weekly/2026-W15.json) | 56 |
| 🗓️ This Month | [`2026-04.json`](data/monthly/2026-04.json) | 325 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-04-15 | 47 | [View JSON](data/daily/2026-04-15.json) |
| 📄 2026-04-14 | 2 | [View JSON](data/daily/2026-04-14.json) |
| 📄 2026-04-13 | 7 | [View JSON](data/daily/2026-04-13.json) |
| 📄 2026-04-12 | 42 | [View JSON](data/daily/2026-04-12.json) |
| 📄 2026-04-11 | 42 | [View JSON](data/daily/2026-04-11.json) |
| 📄 2026-04-10 | 9 | [View JSON](data/daily/2026-04-10.json) |
| 📄 2026-04-09 | 30 | [View JSON](data/daily/2026-04-09.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W15 | 56 | [View JSON](data/weekly/2026-W15.json) |
| 📅 2026-W14 | 147 | [View JSON](data/weekly/2026-W14.json) |
| 📅 2026-W13 | 125 | [View JSON](data/weekly/2026-W13.json) |
| 📅 2026-W12 | 120 | [View JSON](data/weekly/2026-W12.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-04 | 325 | [View JSON](data/monthly/2026-04.json) |
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
