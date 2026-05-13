<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-42-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4114+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">42</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">128</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">350</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4114+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** May 13, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture</b> ⭐ 1.58k</summary>

<br/>

**👥 Authors:** yl-1993, gaclove, muyiyunzi, caizhongang, TokenWang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12500) • [📄 arXiv](https://arxiv.org/abs/2605.12500) • [📥 PDF](https://arxiv.org/pdf/2605.12500)

**💻 Code:** [⭐ Code](https://github.com/OpenSenseNova/SenseNova-U1)

> 🚀 SenseNova U1 is a new series of native multimodal models that unifies multimodal understanding, reasoning, and generation within a monolithic architecture. It marks a fundamental paradigm shift in multimodal AI: from modality integration to true...

</details>

<details>
<summary><b>2. MemPrivacy: Privacy-Preserving Personalized Memory Management for Edge-Cloud Agents</b> ⭐ 31</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09530) • [📄 arXiv](https://arxiv.org/abs/2605.09530) • [📥 PDF](https://arxiv.org/pdf/2605.09530)

**💻 Code:** [⭐ Code](https://github.com/MemTensor/MemPrivacy)

> MemPrivacy: Privacy-Preserving Personalized Memory for Edge-Cloud Agents Authors: Yining Chen, Jihao Zhao, Bo Tang, Haofen Wang, Yue Zhang, Fei Huang, Feiyu Xiong, Zhiyu Li ArXiv: 2605.09530 GitHub: MemTensor/MemPrivacy Hugging Face Models: IAAR-S...

</details>

<details>
<summary><b>3. δ-mem: Efficient Online Memory for Large Language Models</b> ⭐ 26</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12357) • [📄 arXiv](https://arxiv.org/abs/2605.12357) • [📥 PDF](https://arxiv.org/pdf/2605.12357)

**💻 Code:** [⭐ Code](https://github.com/declare-lab/delta-Mem)

> https://github.com/declare-lab/delta-Mem

</details>

<details>
<summary><b>4. RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10899) • [📄 arXiv](https://arxiv.org/abs/2605.10899) • [📥 PDF](https://arxiv.org/pdf/2605.10899)

> TLDR: RubricEM introduces a rubric-guided reinforcement learning framework for training long-form deep research agents, enabling finer-grained stagewise credit assignment and reflection meta-policy training beyond verifiable rewards.

</details>

<details>
<summary><b>5. World Action Models: The Next Frontier in Embodied AI</b> ⭐ 36</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12090) • [📄 arXiv](https://arxiv.org/abs/2605.12090) • [📥 PDF](https://arxiv.org/pdf/2605.12090)

**💻 Code:** [⭐ Code](https://github.com/OpenMOSS/Awesome-WAM)

> World Action Models: The Next Frontier in Embodied AI

</details>

<details>
<summary><b>6. ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12481) • [📄 arXiv](https://arxiv.org/abs/2605.12481) • [📥 PDF](https://arxiv.org/pdf/2605.12481)

**💻 Code:** [⭐ Code](https://github.com/X-PLUG/ToolCUA)

> We introduce ToolCUA, an end-to-end agent for optimal GUI-Tool path orchestration, by leveraging an automated interleaved trajectory scaling pipeline and two-staged training paradigm with Reinforcement finetuning and online agentic RL in sandbox. ...

</details>

<details>
<summary><b>7. Beyond the Last Layer: Multi-Layer Representation Fusion for Visual Tokenization</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Yuanxing Zhang, Yihang Lou, Yan Bai, DogNeverSleep, zzzhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10780) • [📄 arXiv](https://arxiv.org/abs/2605.10780) • [📥 PDF](https://arxiv.org/pdf/2605.10780)

**💻 Code:** [⭐ Code](https://github.com/zhuzil/DRoRAE)

> Representation autoencoders that reuse frozen pretrained vision encoders as visual tokenizers have achieved strong reconstruction and generation quality. However, existing methods universally extract features from only the last encoder layer, disc...

</details>

<details>
<summary><b>8. L2P: Unlocking Latent Potential for Pixel Generation</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Jiangning Zhang, Xu Chen, Junwei Zhu, Zhennan Chen, yingtai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12013) • [📄 arXiv](https://arxiv.org/abs/2605.12013) • [📥 PDF](https://arxiv.org/pdf/2605.12013)

**💻 Code:** [⭐ Code](https://github.com/NJU-PCALab/L2P)

> An efficient transfer paradigm enabling high-quality, end-to-end pixel-space diffusion with minimal computational overhead (even on consumer GPUs) and data requirements. project page: https://nju-pcalab.github.io/projects/L2P/

</details>

<details>
<summary><b>9. AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Hengshuang Zhao, Zhe Liu, Rui Yang, Jie Wu, Runhui Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12495) • [📄 arXiv](https://arxiv.org/abs/2605.12495) • [📥 PDF](https://arxiv.org/pdf/2605.12495)

**💻 Code:** [⭐ Code](https://github.com/huangrh99/AlphaGRPO)

> AlphaGRPO enables multimodal generation RL training across text and image generation for AR-Diffusion-native unified multimodal models, such as BAGEL. It supports training on reasoning text-to-image generation and self-reflective refinement.

</details>

<details>
<summary><b>10. CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12496) • [📄 arXiv](https://arxiv.org/abs/2605.12496) • [📥 PDF](https://arxiv.org/pdf/2605.12496)

> Project page: https://yihao-meng.github.io/CausalCine/

</details>

<details>
<summary><b>11. Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12178) • [📄 arXiv](https://arxiv.org/abs/2605.12178) • [📥 PDF](https://arxiv.org/pdf/2605.12178)

> We study the question of enterprise models in enterprise software, where many transition rules are not hidden in the environment but stored explicitly as workflows, business rules, SLAs, schemas, and configuration records. We compare trained world...

</details>

<details>
<summary><b>12. Teaching Language Models to Think in Code</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.07237) • [📄 arXiv](https://arxiv.org/abs/2605.07237) • [📥 PDF](https://arxiv.org/pdf/2605.07237)

> arxiv: https://arxiv.org/abs/2605.07237 Code and models will be released soon.

</details>

<details>
<summary><b>13. On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Xinchao Wang, Qi Li, YINBO0927

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11882) • [📄 arXiv](https://arxiv.org/abs/2605.11882) • [📥 PDF](https://arxiv.org/pdf/2605.11882)

**💻 Code:** [⭐ Code](https://github.com/YinBo0927/FATE)

> No abstract available.

</details>

<details>
<summary><b>14. Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10832) • [📄 arXiv](https://arxiv.org/abs/2605.10832) • [📥 PDF](https://arxiv.org/pdf/2605.10832)

**💻 Code:** [⭐ Code](https://github.com/JoeYing1019/ODE)

> This work introduces On-policy Data Evolution (ODE) for visual-native multimodal deep search agents. It combines an image-bank reference protocol, which allows tool-generated images to be reused across later tool calls, with a closed-loop data evo...

</details>

<details>
<summary><b>15. SeePhys Pro: Diagnosing Modality Transfer and Blind-Training Effects in Multimodal RLVR for Physics Reasoning</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Yueling Tang, Bokai Zhou, Zirong Liu, Terry Jingchen Zhang, Kun Xiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09266) • [📄 arXiv](https://arxiv.org/abs/2605.09266) • [📥 PDF](https://arxiv.org/pdf/2605.09266)

**💻 Code:** [⭐ Code](https://github.com/AI4Phys/SeePhy-Pro)

> This paper introduces a fine-grained benchmark for studying modality transfer in multimodal physics reasoning. By progressively moving key information from text to images, the paper shows that current MLLMs struggle to maintain consistent reasonin...

</details>

<details>
<summary><b>16. MCP-Cosmos: World Model-Augmented Agents for Complex Task Execution in MCP Environments</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09131) • [📄 arXiv](https://arxiv.org/abs/2605.09131) • [📥 PDF](https://arxiv.org/pdf/2605.09131)

> World Model 4 MCP

</details>

<details>
<summary><b>17. Missing Old Logits in Asynchronous Agentic RL: Semantic Mismatch and Repair Methods for Off-Policy Correction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12070) • [📄 arXiv](https://arxiv.org/abs/2605.12070) • [📥 PDF](https://arxiv.org/pdf/2605.12070)

**💻 Code:** [⭐ Code](https://github.com/millioniron/ROLL)

> Asynchronous reinforcement learning improves rollout throughput for large language model agents by decoupling sample generation from policy optimization, but it also introduces a critical failure mode for PPO-style off-policy correction. In hetero...

</details>

<details>
<summary><b>18. From Web to Pixels: Bringing Agentic Search into Visual Perception</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dongming Wu, Xingping Dong, Kaituo Feng, Xinyi Sun, Bokang Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12497) • [📄 arXiv](https://arxiv.org/abs/2605.12497) • [📥 PDF](https://arxiv.org/pdf/2605.12497)

**💻 Code:** [⭐ Code](https://github.com/yangbokang/pixel-searcher)

> Project page: https://pixel-searcher.github.io/ Code: https://github.com/yangbokang/pixel-searcher

</details>

<details>
<summary><b>19. World Model for Robot Learning: A Comprehensive Survey</b> ⭐ 289</summary>

<br/>

**👥 Authors:** Xinying Guo, Tuo An, Jindou Jia, Gen Li, Bohan Hou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.00080) • [📄 arXiv](https://arxiv.org/abs/2605.00080) • [📥 PDF](https://arxiv.org/pdf/2605.00080)

**💻 Code:** [⭐ Code](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy)

> A policy-centric survey of predictive world models for robot policy learning, planning, simulation, evaluation, data generation, and robotic video generation.

</details>

<details>
<summary><b>20. LoopUS: Recasting Pretrained LLMs into Looped Latent Refinement Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11011) • [📄 arXiv](https://arxiv.org/abs/2605.11011) • [📥 PDF](https://arxiv.org/pdf/2605.11011)

**💻 Code:** [⭐ Code](https://github.com/Thrillcrazyer/LoopUS)

> project page: https://thrillcrazyer.github.io/LoopUS

</details>

<details>
<summary><b>21. PASA: A Principled Embedding-Space Watermarking Approach for LLM-Generated Text under Semantic-Invariant Attacks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10977) • [📄 arXiv](https://arxiv.org/abs/2605.10977) • [📥 PDF](https://arxiv.org/pdf/2605.10977)

**💻 Code:** [⭐ Code](https://github.com/ai-kunkun/PASA)

> Welcome

</details>

<details>
<summary><b>22. MEME: Multi-entity & Evolving Memory Evaluation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12477) • [📄 arXiv](https://arxiv.org/abs/2605.12477) • [📥 PDF](https://arxiv.org/pdf/2605.12477)

**💻 Code:** [⭐ Code](https://github.com/SeokwonJung-Jay/MEME-public)

> Project page: https://seokwonjung-jay.github.io/meme-eval/ Code: https://github.com/SeokwonJung-Jay/MEME-public

</details>

<details>
<summary><b>23. Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12483) • [📄 arXiv](https://arxiv.org/abs/2605.12483) • [📥 PDF](https://arxiv.org/pdf/2605.12483)

> No abstract available.

</details>

<details>
<summary><b>24. Continual Harness: Online Adaptation for Self-Improving Foundation Agents</b> ⭐ 88</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09998) • [📄 arXiv](https://arxiv.org/abs/2605.09998) • [📥 PDF](https://arxiv.org/pdf/2605.09998)

**💻 Code:** [⭐ Code](https://github.com/sethkarten/continual-harness)

> Continual Harness: Online Adaptation for Self-Improving Foundation Agents

</details>

<details>
<summary><b>25. Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10365) • [📄 arXiv](https://arxiv.org/abs/2605.10365) • [📥 PDF](https://arxiv.org/pdf/2605.10365)

**💻 Code:** [⭐ Code](https://github.com/ValueByte-AI/Agent-ValueBench)

> Autonomous agents have rapidly matured as task executors and seen widespread deployment via harnesses such as OpenClaw. Safety concerns have rightly drawn growing research attention, and beneath them lie the values silently steering agent behavior...

</details>

<details>
<summary><b>26. The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11182) • [📄 arXiv](https://arxiv.org/abs/2605.11182) • [📥 PDF](https://arxiv.org/pdf/2605.11182)

**💻 Code:** [⭐ Code](https://github.com/ulab-uiuc/Open-On-Policy-Distillation)

> Excited to share our paper on On-Policy Distillation!

</details>

<details>
<summary><b>27. LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12493) • [📄 arXiv](https://arxiv.org/abs/2605.12493) • [📥 PDF](https://arxiv.org/pdf/2605.12493)

**💻 Code:** [⭐ Code](https://github.com/xiaowu0162/LongMemEval-V2)

> Is your memory system ready to make your agent an experienced colleague after consuming 500 sessions/115M tokens? LME-V2 stress tests the required memory abilities. Check out the paper, data, and code here: https://xiaowu0162.github.io/longmemeval...

</details>

<details>
<summary><b>28. LychSim: A Controllable and Interactive Simulation Framework for Vision Research</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12449) • [📄 arXiv](https://arxiv.org/abs/2605.12449) • [📥 PDF](https://arxiv.org/pdf/2605.12449)

**💻 Code:** [⭐ Code](https://github.com/wufeim/LychSim)

> LychSim is a highly controllable, interactive simulation framework built on Unreal Engine 5, designed to lower the technical barrier of using a modern game engine for computer vision research.

</details>

<details>
<summary><b>29. VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kanle Shi, Zian Huang, Junsheng Zhou, Wenyuan Zhang, Jimin Tang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11424) • [📄 arXiv](https://arxiv.org/abs/2605.11424) • [📥 PDF](https://arxiv.org/pdf/2605.11424)

> No abstract available.

</details>

<details>
<summary><b>30. Images in Sentences: Scaling Interleaved Instructions for Unified Visual Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xun Wang, Xinyu Huang, Dewei Zhou, Kunchang Li, Yabo Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12305) • [📄 arXiv](https://arxiv.org/abs/2605.12305) • [📥 PDF](https://arxiv.org/pdf/2605.12305)

> No abstract available.

</details>

<details>
<summary><b>31. AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11518) • [📄 arXiv](https://arxiv.org/abs/2605.11518) • [📥 PDF](https://arxiv.org/pdf/2605.11518)

**💻 Code:** [⭐ Code](https://github.com/taichengguo/AutoLLMResearch)

> No abstract available.

</details>

<details>
<summary><b>32. MoCam: Unified Novel View Synthesis via Structured Denoising Dynamics</b> ⭐ 18</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12119) • [📄 arXiv](https://arxiv.org/abs/2605.12119) • [📥 PDF](https://arxiv.org/pdf/2605.12119)

**💻 Code:** [⭐ Code](https://github.com/Orange-3DV-Team/MoCam)

> This paper introduces MoCam, a unified framework for novel view synthesis that addresses the fundamental conflict between geometric and appearance priors in diffusion-based generation.

</details>

<details>
<summary><b>33. AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jian-Feng Cai, Fengmiao Bian, Ziyun Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08734) • [📄 arXiv](https://arxiv.org/abs/2605.08734) • [📥 PDF](https://arxiv.org/pdf/2605.08734)

> AdaPreLoRA: Adafactor Preconditioned Low-Rank Adaptation

</details>

<details>
<summary><b>34. One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.05630) • [📄 arXiv](https://arxiv.org/abs/2605.05630) • [📥 PDF](https://arxiv.org/pdf/2605.05630)

**💻 Code:** [⭐ Code](https://github.com/Graph-COM/TurnGate)

> Codes & Datasets: https://github.com/Graph-COM/TurnGate Project Website: https://turn-gate.github.io/ Arxiv: https://arxiv.org/abs/2605.05630 TurnGate is a response-aware defense mechanism designed to detect and mitigate hidden malicious intent in...

</details>

<details>
<summary><b>35. Lite3R: A Model-Agnostic Framework for Efficient Feed-Forward 3D Reconstruction</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.11354) • [📄 arXiv](https://arxiv.org/abs/2605.11354) • [📥 PDF](https://arxiv.org/pdf/2605.11354)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/Lite3R)

> The code has been open-sourced.

</details>

<details>
<summary><b>36. Reward Hacking in Rubric-Based Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Bing Liu, Anisha Gunjal, Zihao Wang, MohammadHossein Rezaei, Anas Mahmoud

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12474) • [📄 arXiv](https://arxiv.org/abs/2605.12474) • [📥 PDF](https://arxiv.org/pdf/2605.12474)

> No abstract available.

</details>

<details>
<summary><b>37. FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mingxuan Yuan, Sinno Jialin Pan, Xianzhi Yu, Hui-Ling Zhen, Zehua Pei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.09932) • [📄 arXiv](https://arxiv.org/abs/2605.09932) • [📥 PDF](https://arxiv.org/pdf/2605.09932)

> Large language models can now process increasingly long inputs, yet their ability to effectively use information spread across long contexts remains limited. We trace this gap to how attention budget is spent during supervised fine-tuning (SFT) on...

</details>

<details>
<summary><b>38. GLiNER-Relex: A Unified Framework for Joint Named Entity Recognition and Relation Extraction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vivek Kalyanarangan, Mykhailo Shtopko, Oleksandr Lukashov, Ihor Stepanov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.10108) • [📄 arXiv](https://arxiv.org/abs/2605.10108) • [📥 PDF](https://arxiv.org/pdf/2605.10108)

> 👏

</details>

<details>
<summary><b>39. Geometric Factual Recall in Transformers</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Alberto Bietti, Joan Bruna, Gilad Yehudai, Shauli Ravfogel

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.12426) • [📄 arXiv](https://arxiv.org/abs/2605.12426) • [📥 PDF](https://arxiv.org/pdf/2605.12426)

> We show that transformers memorize facts geometrically: subject embeddings encode superpositions of their attributes, and the MLP acts as a generic relation-conditioned selector.

</details>

<details>
<summary><b>40. PAAC: Privacy-Aware Agentic Device-Cloud Collaboration</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Christopher G. Brinton, Shiqiang Wang, Wenzhi Fang, liangqiy

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.08646) • [📄 arXiv](https://arxiv.org/abs/2605.08646) • [📥 PDF](https://arxiv.org/pdf/2605.08646)

> 🔑 TL;DR PAAC reframes the device-cloud split as a trust boundary rather than a compute split, with two contributions working in tandem: a decoupled agentic architecture and an LLM-driven privacy sanitizer. 🤝 Decoupled Architecture Cloud-reason-and...

</details>

<details>
<summary><b>41. Implicit Preference Alignment for Human Image Animation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.07545) • [📄 arXiv](https://arxiv.org/abs/2605.07545) • [📥 PDF](https://arxiv.org/pdf/2605.07545)

**💻 Code:** [⭐ Code](https://github.com/mdswyz/IPA)

> Implicit Preference Alignment that removes the need for bad samples for preference optimization.

</details>

<details>
<summary><b>42. FaithfulFaces: Pose-Faithful Facial Identity Preservation for Text-to-Video Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.04702) • [📄 arXiv](https://arxiv.org/abs/2605.04702) • [📥 PDF](https://arxiv.org/pdf/2605.04702)

> Pose-Faithful Facial Identity Preservation for Text-to-Video Generation

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 42 |
| 📅 Today | [`2026-05-13.json`](data/daily/2026-05-13.json) | 42 |
| 📆 This Week | [`2026-W19.json`](data/weekly/2026-W19.json) | 128 |
| 🗓️ This Month | [`2026-05.json`](data/monthly/2026-05.json) | 350 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-05-13 | 42 | [View JSON](data/daily/2026-05-13.json) |
| 📄 2026-05-12 | 48 | [View JSON](data/daily/2026-05-12.json) |
| 📄 2026-05-11 | 38 | [View JSON](data/daily/2026-05-11.json) |
| 📄 2026-05-10 | 38 | [View JSON](data/daily/2026-05-10.json) |
| 📄 2026-05-09 | 38 | [View JSON](data/daily/2026-05-09.json) |
| 📄 2026-05-08 | 25 | [View JSON](data/daily/2026-05-08.json) |
| 📄 2026-05-07 | 15 | [View JSON](data/daily/2026-05-07.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W19 | 128 | [View JSON](data/weekly/2026-W19.json) |
| 📅 2026-W18 | 158 | [View JSON](data/weekly/2026-W18.json) |
| 📅 2026-W17 | 120 | [View JSON](data/weekly/2026-W17.json) |
| 📅 2026-W16 | 156 | [View JSON](data/weekly/2026-W16.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-05 | 350 | [View JSON](data/monthly/2026-05.json) |
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
