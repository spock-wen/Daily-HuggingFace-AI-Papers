<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-44-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4909+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">44</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">87</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">87</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4909+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 02, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Crafter: A Multi-Agent Harness for Editable Scientific Figure Generation from Diverse Inputs</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Liang Chen, Zheng Wang, Zhenhailong Wang, Shuzheng Si, Haozhe Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.30611) • [📄 arXiv](https://arxiv.org/abs/2605.30611) • [📥 PDF](https://arxiv.org/pdf/2605.30611)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HaozheZhao/Crafter)

> Crafter is a multi-agent system for generating publication-quality scientific figures across diverse types and conditions, with CraftEditor turning raster outputs into editable SVGs and CraftBench for evaluation.

</details>

<details>
<summary><b>2. On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02437) • [📄 arXiv](https://arxiv.org/abs/2606.02437) • [📥 PDF](https://arxiv.org/pdf/2606.02437)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters

</details>

<details>
<summary><b>3. A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28556) • [📄 arXiv](https://arxiv.org/abs/2605.28556) • [📥 PDF](https://arxiv.org/pdf/2605.28556)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tomerkeren42/TASTE-task-synthesis-from-tool-sequence-evolution)

> TASTE is a new way to automatically create diverse, harder, and verified benchmarks for tool-using AI agents. Instead of writing tasks first, we start from the tool sequences agents need to execute, then synthesize realistic tasks around them. The...

</details>

<details>
<summary><b>4. K-BrowseComp: A Web Browsing Agent Benchmark Grounded in Korean Contexts</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02404) • [📄 arXiv](https://arxiv.org/abs/2606.02404) • [📥 PDF](https://arxiv.org/pdf/2606.02404)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/prometheus-eval/K-BrowseComp)

> Frontier model evaluations are shifting from foundational capabilities (e.g., instruction following and reasoning) toward compositional, agentic ones, but Korean agentic benchmarks remain scarce. We introduce K-BrowseComp, a web-browsing agent ben...

</details>

<details>
<summary><b>5. Draft-OPD: On-Policy Distillation for Speculative Draft Models</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Qianjia Cheng, Shunkai Zhang, Haoran Zhang, Yafy Li, bingyang-lei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.29343) • [📄 arXiv](https://arxiv.org/abs/2605.29343) • [📥 PDF](https://arxiv.org/pdf/2605.29343)

**💻 Code:** [⭐ Code](https://github.com/bingyang-lei/Draft-OPD) • [⭐ Code](https://github.com/huggingface)

> Our model is also aviliable at https://huggingface.co/collections/bingyang-lei/draft-opd

</details>

<details>
<summary><b>6. VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02564) • [📄 arXiv](https://arxiv.org/abs/2606.02564) • [📥 PDF](https://arxiv.org/pdf/2606.02564)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Video Generation Models can produce temporally coherent visual trajectories, yet often fail to follow task-specific rules. We introduce a VLM-as-Teacher framework that synthesizes task-specific reward queries and guides a VGM Reasoner through onli...

</details>

<details>
<summary><b>7. VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.30351) • [📄 arXiv](https://arxiv.org/abs/2605.30351) • [📥 PDF](https://arxiv.org/pdf/2605.30351)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yesiltepe-hidir/VideoMLA)

> VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion

</details>

<details>
<summary><b>8. X-Stream: Exploring MLLMs as Multiplexers for Multi-Stream Understanding</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Dongming Wu, Yang Bo, Huadai Liu, Xudong Lu, Peiwen Sun

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02482) • [📄 arXiv](https://arxiv.org/abs/2606.02482) • [📥 PDF](https://arxiv.org/pdf/2606.02482)

**💻 Code:** [⭐ Code](https://github.com/PeiwenSun2000/X-Stream) • [⭐ Code](https://github.com/huggingface)

> Paper: https://arxiv.org/abs/2606.02482 Code: https://github.com/PeiwenSun2000/X-Stream Data: https://huggingface.co/datasets/spw2000/X-stream

</details>

<details>
<summary><b>9. SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01311) • [📄 arXiv](https://arxiv.org/abs/2606.01311) • [📥 PDF](https://arxiv.org/pdf/2606.01311)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zjunlp/SkillAdaptor)

> Large language model (LLM) agents increasingly rely on reusable external skills to solve long-horizon interactive tasks. Existing training-free skill adaptation pipelines usually update skills from full trajectories or session-level feedback, whic...

</details>

<details>
<summary><b>10. Which Pretraining Paradigm Better Serves Spatial Intelligence? An Empirical Comparison of Vision-Language and Video Generation Models</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28132) • [📄 arXiv](https://arxiv.org/abs/2605.28132) • [📥 PDF](https://arxiv.org/pdf/2605.28132)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/om-ai-lab/Probing-VLM-VGM)

> As we push toward Vision-First architectures for robotics, a critical question remains: Which pre-training scheme provides the best substrate for Spatial Intelligence? VLM or VGM? To find out, we built a lightweight, frozen-feature probing framewo...

</details>

<details>
<summary><b>11. NITP: Next Implicit Token Prediction for LLM Pre-training</b> ⭐ 21</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.24956) • [📄 arXiv](https://arxiv.org/abs/2605.24956) • [📥 PDF](https://arxiv.org/pdf/2605.24956)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aHapBean/NITP)

> Accepted to ICML 2026.

</details>

<details>
<summary><b>12. Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration?</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01247) • [📄 arXiv](https://arxiv.org/abs/2606.01247) • [📥 PDF](https://arxiv.org/pdf/2606.01247)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aim-uofa/TVRBench)

> Interesting benchmark for testing whether foundation models can actively navigate to a target viewpoint, rather than just passively understand images. The low zero-shot success rates make TVRBench a nice stress test for embodied spatial intelligen...

</details>

<details>
<summary><b>13. LVSA: Training-Free Sparse Attention for Long Video Diffusion</b> ⭐ 12</summary>

<br/>

**👥 Authors:** Hongsheng Liu, Yujie Yuan, Ioannis Lamprou, zzhang-fr, gglorian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.31057) • [📄 arXiv](https://arxiv.org/abs/2605.31057) • [📥 PDF](https://arxiv.org/pdf/2605.31057)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/JiusiServe/LongVideoSparseAttention)

> Dense self-attention is the compute and quality bottleneck of long-video diffusion inference: cost grows quadratically with the sequence length, and beyond the training horizon the model converges to near-static output, that is, "frozen" repetitiv...

</details>

<details>
<summary><b>14. ESPO: Early-Stopping Proximal Policy Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.29860) • [📄 arXiv](https://arxiv.org/abs/2605.29860) • [📥 PDF](https://arxiv.org/pdf/2605.29860)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ESPO (Early-Stopping Proximal Policy Optimization) tackles a key waste in RL training of reasoning LLMs: when a model errs early in a trajectory, standard algorithms keep generating to the maximum length, burning compute on never-rewarded tokens a...

</details>

<details>
<summary><b>15. When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.24202) • [📄 arXiv](https://arxiv.org/abs/2605.24202) • [📥 PDF](https://arxiv.org/pdf/2605.24202)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XHMY/marl-llm-workflows)

> 🤔 When does training a multi-agent LLM workflow end-to-end with RL actually help, and when does it quietly break? We run a controlled study across three workflows (Eval-Opt, Voting, Orch-Workers), two tasks (math + code), and three scales (Qwen3 0...

</details>

<details>
<summary><b>16. MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Jingxing Wang, Xiyuan Yang, Gongyi Zou, Peizhi Niu, Wenhao Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02470) • [📄 arXiv](https://arxiv.org/abs/2606.02470) • [📥 PDF](https://arxiv.org/pdf/2606.02470)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wwh0411/MCP-Persona)

> ICML 2026

</details>

<details>
<summary><b>17. Brain-IT-VQA: From Brain Signals to Answers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.29588) • [📄 arXiv](https://arxiv.org/abs/2605.29588) • [📥 PDF](https://arxiv.org/pdf/2605.29588)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A step toward connecting brain signals and large language models.

</details>

<details>
<summary><b>18. StreamChar: Long-Horizon Streaming Character Audio-Video Generation with Decoupled Orchestration</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.25659) • [📄 arXiv](https://arxiv.org/abs/2605.25659) • [📥 PDF](https://arxiv.org/pdf/2605.25659)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Audio-video multimodal generation with real-time interactive experience on a single GPU.

</details>

<details>
<summary><b>19. OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02031) • [📄 arXiv](https://arxiv.org/abs/2606.02031) • [📥 PDF](https://arxiv.org/pdf/2606.02031)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenWebRL/OpenWebRL)

> OpenWebRL presents a fully open framework for training visual web agents with online multi-turn reinforcement learning on real websites. It covers the full pipeline from live-browser infrastructure and supervised initialization to context manageme...

</details>

<details>
<summary><b>20. LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02553) • [📄 arXiv](https://arxiv.org/abs/2606.02553) • [📥 PDF](https://arxiv.org/pdf/2606.02553)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/qixinhu11/LongLive-RAG)

> Autoregressive (AR) video diffusion enables variable-length synthesis, but long-horizon generation often suffers from accumulated errors and identity drift. For efficiency, existing methods commonly adopt sliding-window attention during generation...

</details>

<details>
<summary><b>21. Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zichen Ding, Qier Cui, Bochen Lin, Jiapeng Zhu, Jianxiang Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.30723) • [📄 arXiv](https://arxiv.org/abs/2605.30723) • [📥 PDF](https://arxiv.org/pdf/2605.30723)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Key idea: Skills are not universally effective across LLM backbones. This paper introduces MASA, a model-aware skill alignment framework that rewrites and adapts skills based on a model’s capability profile. Results across multiple agent environme...

</details>

<details>
<summary><b>22. Speculative Pipeline Decoding: Higher-Accruacy and Zero-Bubble Speculation via Pipeline Parallelism</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.30852) • [📄 arXiv](https://arxiv.org/abs/2605.30852) • [📥 PDF](https://arxiv.org/pdf/2605.30852)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yuyijiong/speculative_pipeline_decoding)

> This is a novel speculative decoding paradigm, expected to address the issues of increasing difficulty and latency bubbles in traditional SD. Compatible with Qwen3, Qwen3.5, Llama3.1, etc. The target model runs in a multi-stage pipeline while a li...

</details>

<details>
<summary><b>23. RoboStressBench: Benchmarking VLM Robustness to Physical Visual Stress in Embodied Scenes</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00828) • [📄 arXiv](https://arxiv.org/abs/2606.00828) • [📥 PDF](https://arxiv.org/pdf/2606.00828)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YUEVII/RoboStressBench)

> Vision-Language Models (VLMs) have shown strong visual understanding and are increasingly deployed in embodied AI systems, where reliable perception under real conditions is essential. However, existing benchmarks assess VLMs using clean images or...

</details>

<details>
<summary><b>24. Masking Stale Observations Helps Search Agents -- Until It Doesn't: A Regime Map and Its Mechanism</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00408) • [📄 arXiv](https://arxiv.org/abs/2606.00408) • [📥 PDF](https://arxiv.org/pdf/2606.00408)

**💻 Code:** [⭐ Code](https://github.com/i-DeepSearch/observation-masking) • [⭐ Code](https://github.com/huggingface)

> We present a systematic study on observation masking—a lightweight context management (CM) technique for long-horizon search agents. By evaluation over diverse backbones (4B–284B) and retrievers, we establish a quantitative regime map revealing th...

</details>

<details>
<summary><b>25. Joint Agent Memory and Exploration Learning via Novelty Signals</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Guohong Liu, Yuxuan Chen, Rui Kong, Xiaohong Weng, Shizuo Tian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01528) • [📄 arXiv](https://arxiv.org/abs/2606.01528) • [📥 PDF](https://arxiv.org/pdf/2606.01528)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MobileLLM/JAMEL)

> Joint Agent Memory and Exploration Learning (JAMEL) framework trains memory and exploration policies together through novelty-driven interaction, enabling effective exploration in open-ended environments with reduced computational costs.

</details>

<details>
<summary><b>26. RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02277) • [📄 arXiv](https://arxiv.org/abs/2606.02277) • [📥 PDF](https://arxiv.org/pdf/2606.02277)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZGC-EmbodyAI/RoboSemanticBench)

> No abstract available.

</details>

<details>
<summary><b>27. Multi-Agent Computer Use</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Daniel Fried, Ruslan Salakhutdinov, Jing Yu Koh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01533) • [📄 arXiv](https://arxiv.org/abs/2606.01533) • [📥 PDF](https://arxiv.org/pdf/2606.01533)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A multi-agent framework for computer use that utilizes a manager model to decompose tasks into directed acyclic graphs, enabling parallel execution and improved performance on long-horizon navigation tasks.

</details>

<details>
<summary><b>28. 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01057) • [📄 arXiv](https://arxiv.org/abs/2606.01057) • [📥 PDF](https://arxiv.org/pdf/2606.01057)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 3DCodeBench is a systematic benchmark and human evaluation platform for assessing vision-language model agents in generating procedural 3D assets via code in 3D modeling software.

</details>

<details>
<summary><b>29. HakushoBench: A Japanese Chart and Table VQA Benchmark from Governmental White Papers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01132) • [📄 arXiv](https://arxiv.org/abs/2606.01132) • [📥 PDF](https://arxiv.org/pdf/2606.01132)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce HakushoBench , a challenging Japanese chart and table visual question answering (VQA) benchmark for evaluating vision-language models (VLMs). To construct HakushoBench, we leverage Japanese government white papers, which contain a lar...

</details>

<details>
<summary><b>30. Off-the-Shelf LLMs as Process Scorers: Training-Free Alternative to PRMs for Mathematical Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01682) • [📄 arXiv](https://arxiv.org/abs/2606.01682) • [📥 PDF](https://arxiv.org/pdf/2606.01682)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>31. LongAttnComp: Cross-Family Context Compression for Long-Context Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01336) • [📄 arXiv](https://arxiv.org/abs/2606.01336) • [📥 PDF](https://arxiv.org/pdf/2606.01336)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper presents a fine-tuning-based long-context compressor with a two-stage training recipe , which achieves strong long-context reasoning performance. A shorter version was accepted at the AdaptFM Workshop at ICML 2026.

</details>

<details>
<summary><b>32. FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification for Agentic Search</b> ⭐ 2</summary>

<br/>

**👥 Authors:** See-Kiong Ng, Bryan Hooi, Hui Chen, James Xu Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00660) • [📄 arXiv](https://arxiv.org/abs/2606.00660) • [📥 PDF](https://arxiv.org/pdf/2606.00660)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XuZhao0/fineverify)

> Code and data are available at: https://github.com/XuZhao0/fineverify

</details>

<details>
<summary><b>33. Adapting Multilingual Embedding Models to Turkish via Cross-Lingual Tokenizer Surgery and Offline Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.29992) • [📄 arXiv](https://arxiv.org/abs/2605.29992) • [📥 PDF](https://arxiv.org/pdf/2605.29992)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/malibayram/embedding-trainer)

> This paper presents embeddingmagibu-200m, a Turkish-focused sentence embedding model built through cross-lingual tokenizer surgery and offline embedding distillation. Instead of expensive full pretraining, we adapt a multilingual embedding model b...

</details>

<details>
<summary><b>34. Compositional Text-to-Image Generation Via Region-aware Bimodal Direct Preference Optimization</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Zuxuan Wu, Yitong Chen, Wujian Peng, anzeameol

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28615) • [📄 arXiv](https://arxiv.org/abs/2605.28615) • [📥 PDF](https://arxiv.org/pdf/2605.28615)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/anzeameol/BiDPO)

> T2I models still struggle with complex prompts—like getting attribute binding, spatial relations, or counting wrong. To bridge this gap, we proposed BiDPO. We curate a high-quality preference dataset (BiComp), extend Diffusion DPO to jointly optim...

</details>

<details>
<summary><b>35. Not only where, But when: Temporal Scheduling for RLVR</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiaqi Wang, Feng Zhao, Ruilin Li, Jinghao Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.25381) • [📄 arXiv](https://arxiv.org/abs/2605.25381) • [📥 PDF](https://arxiv.org/pdf/2605.25381)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Jinghaoleven/RLVR-Schedule)

> What if credit allocation in RLVR should evolve over training rather than remain fixed? We propose Temporal Scheduling, which gradually shifts optimization focus across trajectory and enables more stable policy evolution. The result is consistent ...

</details>

<details>
<summary><b>36. Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00090) • [📄 arXiv](https://arxiv.org/abs/2606.00090) • [📥 PDF](https://arxiv.org/pdf/2606.00090)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems

</details>

<details>
<summary><b>37. Can Predicted Dynamics Exist in the Physical World?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00089) • [📄 arXiv](https://arxiv.org/abs/2606.00089) • [📥 PDF](https://arxiv.org/pdf/2606.00089)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Predictive Physical AI systems output state rollouts, action chunks, and latent plans, yet a low root-mean-square error (RMSE) does not imply that a particular proposal is physically executable. We formulate physical admissibility as a prediction-...

</details>

<details>
<summary><b>38. EVA01: Unified Native 3D Understanding and Generation via Mixture-of-Transformers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.16745) • [📄 arXiv](https://arxiv.org/abs/2605.16745) • [📥 PDF](https://arxiv.org/pdf/2605.16745)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> EVA01 is a unified framework that extends the modality boundary of MLLMs to natively incorporate 3D mesh understanding, generation, and context-aware editing.

</details>

<details>
<summary><b>39. Thinking in Blender: Staged Executable Inverse Graphics with Vision-Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hadar Averbuch-Elor, Wei-Chiu Ma, Rundong Luo, Guangzhao He

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02580) • [📄 arXiv](https://arxiv.org/abs/2606.02580) • [📥 PDF](https://arxiv.org/pdf/2606.02580)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> SEIG is an agentic framework that reconstructs 3D scenes from single images by progressively generating executable Blender code, enabling novel-view synthesis, scene editing, and relighting.

</details>

<details>
<summary><b>40. ChartArena: Benchmarking Chart Parsing across Languages, Scenarios, and Formats</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hao Feng, Chengquan Zhang, Xingyu Wan, Gengluo Li, Shangpin Peng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01348) • [📄 arXiv](https://arxiv.org/abs/2606.01348) • [📥 PDF](https://arxiv.org/pdf/2606.01348)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/pspdada/ChartArena)

> ChartArena is a comprehensive bilingual benchmark for evaluating the chart parsing capabilities of vision-language models, spanning the full difficulty spectrum of charts encountered in practice. It covers eight chart families: both numeric charts...

</details>

<details>
<summary><b>41. Confidence-Adaptive SwiGLU for Mixture-of-Experts</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Liangli Zhen, Yuhang Wu, Xiaobing Sun, Xiuchao Sui, Shaohua Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00761) • [📄 arXiv](https://arxiv.org/abs/2606.00761) • [📥 PDF](https://arxiv.org/pdf/2606.00761)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/askerlee/kappa-swiglu)

> κ-SwiGLU is a confidence-aware SwiGLU variant for MoE models that uses router logits to adapt expert gate sharpness, improving pretraining performance with negligible additional parameters and small computational overhead.

</details>

<details>
<summary><b>42. StressDream: Steering Video World Models for Robust Policy Evaluation and Improvement</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Apoorva Sharma, Wenhao Ding, Ran Tian, Sushant Veer, Junwon Seo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00267) • [📄 arXiv](https://arxiv.org/abs/2606.00267) • [📥 PDF](https://arxiv.org/pdf/2606.00267)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/CMU-IntentLab/StressDream)

> StressDream steers video world model imaginations toward high-impact, plausible outcomes using VLM-guided noise optimization to enable robust policy evaluation for robotics and autonomous driving.

</details>

<details>
<summary><b>43. Geometric Latent Reasoning Induces Shorter Generations in LLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02248) • [📄 arXiv](https://arxiv.org/abs/2606.02248) • [📥 PDF](https://arxiv.org/pdf/2606.02248)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large language models solve complex problems by generating lengthy chains of explicit reasoning tokens. While effective, this makes reasoning expensive, length-sensitive, and constrained to (discrete) natural language. While latent reasoning offer...

</details>

<details>
<summary><b>44. The Hamilton-Jacobi Theory of Deep Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.28983) • [📄 arXiv](https://arxiv.org/abs/2605.28983) • [📥 PDF](https://arxiv.org/pdf/2605.28983)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 44 |
| 📅 Today | [`2026-06-02.json`](data/daily/2026-06-02.json) | 44 |
| 📆 This Week | [`2026-W22.json`](data/weekly/2026-W22.json) | 87 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 87 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-02 | 44 | [View JSON](data/daily/2026-06-02.json) |
| 📄 2026-06-01 | 43 | [View JSON](data/daily/2026-06-01.json) |
| 📄 2026-05-31 | 59 | [View JSON](data/daily/2026-05-31.json) |
| 📄 2026-05-30 | 59 | [View JSON](data/daily/2026-05-30.json) |
| 📄 2026-05-29 | 43 | [View JSON](data/daily/2026-05-29.json) |
| 📄 2026-05-28 | 39 | [View JSON](data/daily/2026-05-28.json) |
| 📄 2026-05-27 | 28 | [View JSON](data/daily/2026-05-27.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W22 | 87 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |
| 📅 2026-W20 | 243 | [View JSON](data/weekly/2026-W20.json) |
| 📅 2026-W19 | 310 | [View JSON](data/weekly/2026-W19.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 87 | [View JSON](data/monthly/2026-06.json) |
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
