<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-32-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-2509+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">98</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">990</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">2509+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** February 26, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. On Data Engineering for Scaling LLM Terminal Capabilities</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21193) • [📄 arXiv](https://arxiv.org/abs/2602.21193) • [📥 PDF](https://arxiv.org/pdf/2602.21193)

> Despite rapid recent progress in the terminal capabilities of large language models, the training data strategies behind state-of-the-art terminal agents remain largely undisclosed. We address this gap through a systematic study of data engineerin...

</details>

<details>
<summary><b>2. Query-focused and Memory-aware Reranker for Long Context Processing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12192) • [📄 arXiv](https://arxiv.org/abs/2602.12192) • [📥 PDF](https://arxiv.org/pdf/2602.12192)

> Our trained models can be downloaded from: https://huggingface.co/MindscapeRAG/QRRanker

</details>

<details>
<summary><b>3. PyVision-RL: Forging Open Agentic Vision Models via RL</b> ⭐ 43</summary>

<br/>

**👥 Authors:** Wenshuo Peng, Ming Li, Shaoheng Lin, haoquan03, stzhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20739) • [📄 arXiv](https://arxiv.org/abs/2602.20739) • [📥 PDF](https://arxiv.org/pdf/2602.20739)

**💻 Code:** [⭐ Code](https://github.com/agents-x-project/PyVision-RL)

> We introduce PyVision-RL, a reinforcement learning framework for open-weight multimodal models that stabilizes training and sustains interaction. Our approach combines an over sampling–filtering–ranking rollout strategy with an accumulative tool r...

</details>

<details>
<summary><b>4. Test-Time Training with KV Binding Is Secretly Linear Attention</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21204) • [📄 arXiv](https://arxiv.org/abs/2602.21204) • [📥 PDF](https://arxiv.org/pdf/2602.21204)

> Test-time training (TTT) with KV binding as sequence modeling layer is commonly interpreted as a form of online meta-learning that memorizes a key-value mapping at test time. However, our analysis reveals multiple phenomena that contradict this me...

</details>

<details>
<summary><b>5. From Perception to Action: An Interactive Benchmark for Vision Reasoning</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yihuai Lan, Maojia Song, henggg, Zhiqiang007, mozhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21015) • [📄 arXiv](https://arxiv.org/abs/2602.21015) • [📥 PDF](https://arxiv.org/pdf/2602.21015)

**💻 Code:** [⭐ Code](https://github.com/Social-AI-Studio/CHAIN)

> Introducing CHAIN, a new interactive benchmark that moves beyond static visual QA. It evaluates  Vision-Language Models (VLMs) on their ability to close the loop between perception, multi-step reasoning, and actionable execution in dynamic environ...

</details>

<details>
<summary><b>6. Multi-Vector Index Compression in Any Modality</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21202) • [📄 arXiv](https://arxiv.org/abs/2602.21202) • [📥 PDF](https://arxiv.org/pdf/2602.21202)

**💻 Code:** [⭐ Code](https://github.com/hanxiangqin/omni-col-press)

> Multimodal compression

</details>

<details>
<summary><b>7. See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jae-Gil Lee, Minkyu Kim, Minyoung Ahn, Jhyun17, Cabbalett

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20951) • [📄 arXiv](https://arxiv.org/abs/2602.20951) • [📥 PDF](https://arxiv.org/pdf/2602.20951)

**💻 Code:** [⭐ Code](https://github.com/krafton-ai/ArtiAgent)

> Accepted to CVPR’26.

</details>

<details>
<summary><b>8. DREAM: Deep Research Evaluation with Agentic Metrics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18940) • [📄 arXiv](https://arxiv.org/abs/2602.18940) • [📥 PDF](https://arxiv.org/pdf/2602.18940)

> Evaluating Deep Research Agents (DRAs) with static LLM judges often leads to the "Mirage of Synthesis," where fluent writing and accurate-looking citations mask underlying factual errors and flawed logic. The authors attribute this to a capability...

</details>

<details>
<summary><b>9. LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces</b> ⭐ 22</summary>

<br/>

**👥 Authors:** Chuanhao Li, Jiaxin Ai, Zelai Yang, Jianwen Sun, Yukang Feng

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14337) • [📄 arXiv](https://arxiv.org/abs/2602.14337) • [📥 PDF](https://arxiv.org/pdf/2602.14337)

**💻 Code:** [⭐ Code](https://github.com/finyorko/longcli-bench)

> Recent advances in AI-assisted programming have empowered agents to execute complex workflows via command-line interfaces, however, existing benchmarks are limited by short task horizons, data contamination from GitHub scraping, and a lack of fine...

</details>

<details>
<summary><b>10. QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xin Wang, Haokun Lin, Zhongwei Wang, Yunta Hsieh, Jingxuan Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20309) • [📄 arXiv](https://arxiv.org/abs/2602.20309) • [📥 PDF](https://arxiv.org/pdf/2602.20309)

> Published in CVPR2026.

</details>

<details>
<summary><b>11. Conv-FinRe: A Conversational and Longitudinal Benchmark for Utility-Grounded Financial Recommendation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16990) • [📄 arXiv](https://arxiv.org/abs/2602.16990) • [📥 PDF](https://arxiv.org/pdf/2602.16990)

**💻 Code:** [⭐ Code](https://github.com/The-FinAI/Conv-FinRe)

> Most recommendation benchmarks evaluate how well a model imitates user behavior. In financial advisory, however, observed actions can be noisy or short-sighted under market volatility and may conflict with a user's long-term goals. Treating what u...

</details>

<details>
<summary><b>12. PETS: A Principled Framework Towards Optimal Trajectory Allocation for Efficient Test-Time Self-Consistency</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16745) • [📄 arXiv](https://arxiv.org/abs/2602.16745) • [📥 PDF](https://arxiv.org/pdf/2602.16745)

**💻 Code:** [⭐ Code](https://github.com/ZDCSlab/PETS)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Agentic Test-Time Scaling for WebAgents (2026) HyPER: Bridging Exploration ...

</details>

<details>
<summary><b>13. Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiajun Wu, Li Fei-Fei, Manling Li, Huang Huang, Yining Hong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21198) • [📄 arXiv](https://arxiv.org/abs/2602.21198) • [📥 PDF](https://arxiv.org/pdf/2602.21198)

**💻 Code:** [⭐ Code](https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning)

> Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human...

</details>

<details>
<summary><b>14. The Art of Efficient Reasoning: Data, Reward, and Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20945) • [📄 arXiv](https://arxiv.org/abs/2602.20945) • [📥 PDF](https://arxiv.org/pdf/2602.20945)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Thickening-to-Thinning: Reward Shaping via Human-Inspired Learning Dynamics...

</details>

<details>
<summary><b>15. Communication-Inspired Tokenization for Structured Image Representations</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20731) • [📄 arXiv](https://arxiv.org/abs/2602.20731) • [📥 PDF](https://arxiv.org/pdf/2602.20731)

**💻 Code:** [⭐ Code](https://github.com/araachie/comit)

> A new way to represent images as discrete sequences of tokens by sequentially integrating information from image crops, yielding semantically meaningful structured representations.

</details>

<details>
<summary><b>16. TAPE: Tool-Guided Adaptive Planning and Constrained Execution in Language Model Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19633) • [📄 arXiv](https://arxiv.org/abs/2602.19633) • [📥 PDF](https://arxiv.org/pdf/2602.19633)

**💻 Code:** [⭐ Code](https://github.com/UW-Madison-Lee-Lab/TAPE)

> arxiv: https://arxiv.org/abs/2602.19633 code: https://github.com/UW-Madison-Lee-Lab/TAPE

</details>

<details>
<summary><b>17. Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21196) • [📄 arXiv](https://arxiv.org/abs/2602.21196) • [📥 PDF](https://arxiv.org/pdf/2602.21196)

**💻 Code:** [⭐ Code](https://github.com/togethercomputer/Untied-Ulysses)

> We present UPipe, a memory-efficient context parallelism technique that processes attention heads in chunks. Our approach reduces intermediate tensor memory usage in the attention layer by as much as 87.5% for 32B Transformers, while matching prev...

</details>

<details>
<summary><b>18. The Diffusion Duality, Chapter II: Ψ-Samplers and Efficient Curriculum</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Caglar Gulcehre, Justin Deschenaux, s-sahoo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21185) • [📄 arXiv](https://arxiv.org/abs/2602.21185) • [📥 PDF](https://arxiv.org/pdf/2602.21185)

> Introduces Predictor-Corrector samplers for discrete diffusion that beat ancestral sampling and enable efficient, improving sampling with more steps, plus a memory-efficient Gaussian-relaxation curriculum.

</details>

<details>
<summary><b>19. Implicit Intelligence -- Evaluating Agents on What Users Don't Say</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Marc Wetter, Ved Sirdeshmukh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20424) • [📄 arXiv](https://arxiv.org/abs/2602.20424) • [📥 PDF](https://arxiv.org/pdf/2602.20424)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents und...

</details>

<details>
<summary><b>20. Benchmark Test-Time Scaling of General LLM Agents</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18998) • [📄 arXiv](https://arxiv.org/abs/2602.18998) • [📥 PDF](https://arxiv.org/pdf/2602.18998)

**💻 Code:** [⭐ Code](https://github.com/cxcscmu/General-AgentBench)

> LLM agents are increasingly expected to function as general-purpose systems capable of resolving open-ended user requests. While existing benchmarks focus on domain-aware environments for developing specialized agents, evaluating general-purpose a...

</details>

<details>
<summary><b>21. RankEvolve: Automating the Discovery of Retrieval Algorithms via LLM-Driven Evolution</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16932) • [📄 arXiv](https://arxiv.org/abs/2602.16932) • [📥 PDF](https://arxiv.org/pdf/2602.16932)

**💻 Code:** [⭐ Code](https://github.com/fangchenli/ranking-evolved)

> No abstract available.

</details>

<details>
<summary><b>22. One-step Language Modeling via Continuous Denoising</b> ⭐ 43</summary>

<br/>

**👥 Authors:** Jerry Huang, Sheel Shah, Manan Agarwal, Jaehoon Yoo, Chanhyuk Lee

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16813) • [📄 arXiv](https://arxiv.org/abs/2602.16813) • [📥 PDF](https://arxiv.org/pdf/2602.16813)

**💻 Code:** [⭐ Code](https://github.com/david3684/flm)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API T3D: Few-Step Diffusion Language Models via Trajectory Self-Distillation wi...

</details>

<details>
<summary><b>23. Aletheia tackles FirstProof autonomously</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21201) • [📄 arXiv](https://arxiv.org/abs/2602.21201) • [📥 PDF](https://arxiv.org/pdf/2602.21201)

**💻 Code:** [⭐ Code](https://github.com/google-deepmind/superhuman/tree/main/aletheia)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Towards Autonomous Mathematics Research (2026) Semi-Autonomous Mathematics ...

</details>

<details>
<summary><b>24. SIMSPINE: A Biomechanics-Aware Simulation Framework for 3D Spine Motion Annotation and Benchmarking</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20792) • [📄 arXiv](https://arxiv.org/abs/2602.20792) • [📥 PDF](https://arxiv.org/pdf/2602.20792)

**💻 Code:** [⭐ Code](https://github.com/dfki-av/simspine)

> This paper was accepted for publication at CVPR 2026! In the following image, you can see the improvement over previous SOTA in spine keypoint regression task:

</details>

<details>
<summary><b>25. OCR-Agent: Agentic OCR with Capability and Memory Reflection</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21053) • [📄 arXiv](https://arxiv.org/abs/2602.21053) • [📥 PDF](https://arxiv.org/pdf/2602.21053)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/OCR-Agent)

> Code: https://github.com/AIGeeksGroup/OCR-Agent

</details>

<details>
<summary><b>26. OmniOCR: Generalist OCR for Ethnic Minority Languages</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21042) • [📄 arXiv](https://arxiv.org/abs/2602.21042) • [📥 PDF](https://arxiv.org/pdf/2602.21042)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/OmniOCR)

> Code: https://github.com/AIGeeksGroup/OmniOCR

</details>

<details>
<summary><b>27. Adaptive Text Anonymization: Learning Privacy-Utility Trade-offs via Prompt Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20743) • [📄 arXiv](https://arxiv.org/abs/2602.20743) • [📥 PDF](https://arxiv.org/pdf/2602.20743)

> We introduce adaptive text anonymization, a new approach that automatically tailors anonymization strategies to specific privacy and utility requirements instead of relying on fixed, manually designed methods. It uses prompt optimization to genera...

</details>

<details>
<summary><b>28. Learning to Detect Language Model Training Data via Active Reconstruction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19020) • [📄 arXiv](https://arxiv.org/abs/2602.19020) • [📥 PDF](https://arxiv.org/pdf/2602.19020)

**💻 Code:** [⭐ Code](https://github.com/oseyosey/MIA-RL)

> Many people are using RL to make models smarter. We used RL to pull training data out of the models themselves. Our results show that models know a lot more about their training data than most people think. We develop Active Data Reconstruction At...

</details>

<details>
<summary><b>29. LaS-Comp: Zero-shot 3D Completion with Latent-Spatial Consistency</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.18735) • [📄 arXiv](https://arxiv.org/abs/2602.18735) • [📥 PDF](https://arxiv.org/pdf/2602.18735)

**💻 Code:** [⭐ Code](https://github.com/DavidYan2001/LaS-Comp)

> null

</details>

<details>
<summary><b>30. FlowPrefill: Decoupling Preemption from Prefill Scheduling Granularity to Mitigate Head-of-Line Blocking in LLM Serving</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Jidong Zhai, Jianjiang Li, Xinyang Chen, Zan Zong, hsiehchiachi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.16603) • [📄 arXiv](https://arxiv.org/abs/2602.16603) • [📥 PDF](https://arxiv.org/pdf/2602.16603)

**💻 Code:** [⭐ Code](https://github.com/HSIEHCHIACHI/FlowPrefill)

> Say goodbye to LLM prefill delays! 🚀 Excited to share our new paper FlowPrefill. We tackle head-of-line blocking in LLM serving with operator-level preemption & event-driven scheduling, boosting goodput by up to 5.6×. Paper: https://arxiv.org/abs/...

</details>

<details>
<summary><b>31. TextPecker: Rewarding Structural Anomaly Quantification for Enhancing Visual Text Rendering</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Hao Feng, An-Lan Wang, Xuecheng Wu, Yuliang Liu, CIawevy

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20903) • [📄 arXiv](https://arxiv.org/abs/2602.20903) • [📥 PDF](https://arxiv.org/pdf/2602.20903)

**💻 Code:** [⭐ Code](https://github.com/CIawevy/TextPecker)

> [CVPR2026] TextPecker: Rewarding Structural Anomaly Quantification for Enhancing Visual Text Rendering

</details>

<details>
<summary><b>32. Generative AI and Machine Learning Collaboration for Container Dwell Time Prediction via Data Standardization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.20540) • [📄 arXiv](https://arxiv.org/abs/2602.20540) • [📥 PDF](https://arxiv.org/pdf/2602.20540)

> The proposed framework employs Gen AI to standardize unstructured information into standard international codes, with dynamic re-prediction triggered by electronic data interchange state updates, enabling the machine learning model to predict ICDT...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 32 |
| 📅 Today | [`2026-02-26.json`](data/daily/2026-02-26.json) | 32 |
| 📆 This Week | [`2026-W08.json`](data/weekly/2026-W08.json) | 98 |
| 🗓️ This Month | [`2026-02.json`](data/monthly/2026-02.json) | 990 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-02-26 | 32 | [View JSON](data/daily/2026-02-26.json) |
| 📄 2026-02-25 | 25 | [View JSON](data/daily/2026-02-25.json) |
| 📄 2026-02-24 | 18 | [View JSON](data/daily/2026-02-24.json) |
| 📄 2026-02-23 | 23 | [View JSON](data/daily/2026-02-23.json) |
| 📄 2026-02-22 | 23 | [View JSON](data/daily/2026-02-22.json) |
| 📄 2026-02-21 | 23 | [View JSON](data/daily/2026-02-21.json) |
| 📄 2026-02-20 | 18 | [View JSON](data/daily/2026-02-20.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W08 | 98 | [View JSON](data/weekly/2026-W08.json) |
| 📅 2026-W07 | 197 | [View JSON](data/weekly/2026-W07.json) |
| 📅 2026-W06 | 293 | [View JSON](data/weekly/2026-W06.json) |
| 📅 2026-W05 | 357 | [View JSON](data/weekly/2026-W05.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-02 | 990 | [View JSON](data/monthly/2026-02.json) |
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
