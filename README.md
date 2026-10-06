<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-48-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8145+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">48</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">89</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">384</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8145+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 06, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05608) • [📄 arXiv](https://arxiv.org/abs/2610.05608) • [📥 PDF](https://arxiv.org/pdf/2610.05608)

**💻 Code:** [⭐ Code](https://github.com/kandinskylab/kandinsky-6) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kandinskylab/kandinsky-6-sr)

> 🎬 Kandinsky 6.0 Video — 3B Lite / 29B Pro for synchronized text/image-to-audio-video , with 44 kHz audio, lip-sync and Full-HD super-resolution. 🧠 Uses a dual-stream CrossDiT with bidirectional audio↔video attention, followed by SFT, RL and 10-ste...

</details>

<details>
<summary><b>2. ALoDLM: Adaptively Looped Diffusion Language Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04198) • [📄 arXiv](https://arxiv.org/abs/2610.04198) • [📥 PDF](https://arxiv.org/pdf/2610.04198)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/amazon-science/ALoDLM)

> Diffusion language models (DLMs) enable fast generation by predicting multiple tokens in parallel, but their practical adoption remains limited by a persistent quality gap relative to comparably sized autoregressive (AR) models. We attribute this ...

</details>

<details>
<summary><b>3. Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Jinsong Su, Zerui Chen, Zhishang Xiang, Haibo Meng, Ruqing Ning

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05162) • [📄 arXiv](https://arxiv.org/abs/2610.05162) • [📥 PDF](https://arxiv.org/pdf/2610.05162)

**💻 Code:** [⭐ Code](https://github.com/DEEP-JLU/MemAdapter) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/DEEP-JLU/MemAdapter.git)

> Long-term memory enables LLM-based agents to retain and reuse information across tasks and sessions, supporting personalization and long-horizon interactions. However, persistent memories can also induce sycophancy, causing agents to over-align wi...

</details>

<details>
<summary><b>4. Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37267) • [📄 arXiv](https://arxiv.org/abs/2609.37267) • [📥 PDF](https://arxiv.org/pdf/2609.37267)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym

</details>

<details>
<summary><b>5. CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.00923) • [📄 arXiv](https://arxiv.org/abs/2610.00923) • [📥 PDF](https://arxiv.org/pdf/2610.00923)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multimodal RAG decides which items to retrieve, but not how much of each item the reader actually needs. We introduce CANOPY, which represents each retrieved text, table, or video as a hierarchy of original regions and uses a fine-tuned node encod...

</details>

<details>
<summary><b>6. In-Distribution Forcing for Long Video Generation at Test Time</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03120) • [📄 arXiv](https://arxiv.org/abs/2610.03120) • [📥 PDF](https://arxiv.org/pdf/2610.03120)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/In-Distribution-Forcing/ID-Forcing)

> Modern autoregressive (AR) video diffusion models excel at short-horizon video generation, yet generating long videos remains challenging due to drifting, where colors and textures shift, and motion dynamics decay. Existing works primarily rely on...

</details>

<details>
<summary><b>7. ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience</b> ⭐ 0</summary>

<br/>

**👥 Authors:** dginf, jeff024

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05303) • [📄 arXiv](https://arxiv.org/abs/2610.05303) • [📥 PDF](https://arxiv.org/pdf/2610.05303)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ASCENT lets an LLM agent keep learning while it is deployed. In Online Agentic Test-Time Training (OaTTT), the agent executes each task once in one pass over its task stream, and that single attempt with its verification result is the only learnin...

</details>

<details>
<summary><b>8. OSWorld-Pro: Process-based Evaluation for Computer Use Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24890) • [📄 arXiv](https://arxiv.org/abs/2609.24890) • [📥 PDF](https://arxiv.org/pdf/2609.24890)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> OSWorld-Pro: Process-based Evaluation for Computer Use Agents

</details>

<details>
<summary><b>9. Optimizing the Optimizer: Language Models Discover Faster Molecular Relaxation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Maxim Radchenko, Denis Potapov, Kuzma Khrabrov, Vladimir Deshchenya, Artem Tsypin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06577) • [📄 arXiv](https://arxiv.org/abs/2610.06577) • [📥 PDF](https://arxiv.org/pdf/2610.06577)

**💻 Code:** [⭐ Code](https://github.com/vdeshchenya/autosella) • [⭐ Code](https://github.com/huggingface)

> Hi everyone, I’m one of the authors of AutoSella. We let language-model agents rewrite Sella, the fastest open-source molecular geometry optimizer, to reduce the number of force evaluations. The search uses inexpensive GFN2-xTB calculations, with ...

</details>

<details>
<summary><b>10. RobotUse: Allocating Computation, Context, and Decisions</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04929) • [📄 arXiv](https://arxiv.org/abs/2610.04929) • [📥 PDF](https://arxiv.org/pdf/2610.04929)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/robotuse-team/RobotUse)

> RobotUse is a robot agent harness that connects language-level goals to visual decisions and physical execution. Robot tasks require agents to plan toward an overall goal while selecting targets, choosing gripper poses, and revising actions based ...

</details>

<details>
<summary><b>11. Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05076) • [📄 arXiv](https://arxiv.org/abs/2610.05076) • [📥 PDF](https://arxiv.org/pdf/2610.05076)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lingjivoo/ttt-ouroboros)

> Hi everyone! Author here 👋 What happens when a model keeps learning from its own outputs during inference? We study this feedback loop over 128K-token streams with TTT-E2E models from 125M to 3B and Adam-based adaptation of Qwen3-4B. Our key findi...

</details>

<details>
<summary><b>12. SearchJev: A Fast and Calibrated System-1 Model for Search Agents</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Songwei Xu, Qiwei Xu, Konstantinos Papakostas, Lipeng Zuo, Congfeng Cao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05107) • [📄 arXiv](https://arxiv.org/abs/2610.05107) • [📥 PDF](https://arxiv.org/pdf/2610.05107)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EvoScientist/SearchJev)

> SearchJev, a fast and calibrated System-1 model for search agents. Search agents repeatedly make small but important decisions: Is this passage relevant? Is the evidence sufficient? Which link should I open next? Asking a large LLM to generate an ...

</details>

<details>
<summary><b>13. Towards Looped Models Done Right, Part II: Rethinking at Fixed Points</b> ⭐ 29</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06833) • [📄 arXiv](https://arxiv.org/abs/2610.06833) • [📥 PDF](https://arxiv.org/pdf/2610.06833)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ifm-ai/xllm-loop) • [⭐ Code](github.com/ifm-ai/xllm-loop)

> Scaling up a model has meant paying twice, in compute and in memory.We show that looped models can pay in compute alone, using the loop's fixed point as a shortcut. A 1.6B looped model runs twelve blocks deep on four blocks of memory. On the same ...

</details>

<details>
<summary><b>14. OmniReasoning: Pushing the Limits of Audio-Visual Joint Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39490) • [📄 arXiv](https://arxiv.org/abs/2609.39490) • [📥 PDF](https://arxiv.org/pdf/2609.39490)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PKU-VaLuE-Lab/OmniReasoning)

> Recent advances have enabled unified omni-modal models in understanding audio, vision, and language. However, existing benchmarks, training data, and learning methods largely treat the modalities independently, leaving the capability of audio-visu...

</details>

<details>
<summary><b>15. Data Unlearning via Inverse Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Iaroslav Koshelev, Evgeny Burnaev, Zhenhe Zhang, Nikita Kornilov, Aleksei Leonov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36099) • [📄 arXiv](https://arxiv.org/abs/2609.36099) • [📥 PDF](https://arxiv.org/pdf/2609.36099)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Data Unlearning via Inverse Distillation (IDU) — a framework that combines selective data forgetting with one-step generation. Starting from a diffusion or flow teacher trained on the full dataset, IDU trains a one-step student to sup...

</details>

<details>
<summary><b>16. Noise Out, Bias In: Targeted Bias Injection in Diffusion Language Models via Closed-Loop Activation Steering</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05894) • [📄 arXiv](https://arxiv.org/abs/2610.05894) • [📥 PDF](https://arxiv.org/pdf/2610.05894)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Sarim-MBZUAI/dlm_bias)

> Diffusion language models repeatedly revise tokens before committing to an answer, giving attackers repeated opportunities to influence generation. We study targeted bias injection through closed-loop activation steering: an attacker with access t...

</details>

<details>
<summary><b>17. Certification of Real Images through Calibrated Content Authentication</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05870) • [📄 arXiv](https://arxiv.org/abs/2610.05870) • [📥 PDF](https://arxiv.org/pdf/2610.05870)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Sarim-MBZUAI/content-authentication)

> Deepfake detectors struggle with newer generators, and adversarial attacks push all 20 tested detectors below 2% accuracy. We propose calibrated resynthesis: certify an image as authentic relative to tested generators only when none can faithfully...

</details>

<details>
<summary><b>18. When to Switch: Reliable Action-Chunk Extension for Vision-Language-Action Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05719) • [📄 arXiv](https://arxiv.org/abs/2610.05719) • [📥 PDF](https://arxiv.org/pdf/2610.05719)

**💻 Code:** [⭐ Code](https://github.com/Seonghoon-Yu/RACE-VLA) • [⭐ Code](https://github.com/huggingface)

> Real-robot demo Why do longer action chunks become unreliable in VLAs? We find that action errors are not evenly distributed—they spike around transitions between manipulation subskills, and these spikes grow as the chunk gets longer. RACE explici...

</details>

<details>
<summary><b>19. RealtimeWAM: One-Step Asynchronous World Action Models</b> ⭐ 2.88k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06617) • [📄 arXiv](https://arxiv.org/abs/2610.06617) • [📥 PDF](https://arxiv.org/pdf/2610.06617)

**💻 Code:** [⭐ Code](https://github.com/ModelTC/LightX2V) • [⭐ Code](https://github.com/huggingface)

> An extremely efficient one-step asynchronous WAM for real-time world modeling. Achieves up to 25× speedup over existing WAMs with less than 1% accuracy degradation .

</details>

<details>
<summary><b>20. Rethinking Long-Video Efficiency: A Joint Allocation Perspective on Frames, Pixels, and Front-End Latency</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04318) • [📄 arXiv](https://arxiv.org/abs/2610.04318) • [📥 PDF](https://arxiv.org/pdf/2610.04318)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🎬 LoHi (NeurIPS 2026) : Rethinking long-video efficiency. 💡 Three lessons 🎞️ More frames, not more pixels : at the same token budget, dense low-resolution frames beat sparse native-resolution frames. 🔍 Resolution is task-dependent : most questions...

</details>

<details>
<summary><b>21. Base Models Can Reason By Taking a Cue From Training Data</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06851) • [📄 arXiv](https://arxiv.org/abs/2610.06851) • [📥 PDF](https://arxiv.org/pdf/2610.06851)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sophicle/cues)

> Two opening tokens can bring a base model’s reasoning performance close to that of its RL-trained counterpart. These token cues come from associations learned during training, and RL makes effective cues more likely. Changing those associations ca...

</details>

<details>
<summary><b>22. QuantCode Model: Specializing Language Models for Executable Algorithmic Trading Code</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dmitry Zmitrovich, Orkhan Ekhtibarov, alexeychernysh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39420) • [📄 arXiv](https://arxiv.org/abs/2609.39420) • [📥 PDF](https://arxiv.org/pdf/2609.39420)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present QuantCode Model, a study of how to specialize LLMs for executable algorithmic trading code. On QuantCode-Bench (400 Backtrader tasks), continued pretraining on trading-framework code raises single-turn Judge Pass of Qwen3.6-35B-A3B from...

</details>

<details>
<summary><b>23. UndoBench: Separating Task Competence from Recovery Capability in Tool-Using AI Agents</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Tanya Sah, Harshul Jain, Tanmay Sah, Dolly Sah

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05622) • [📄 arXiv](https://arxiv.org/abs/2610.05622) • [📥 PDF](https://arxiv.org/pdf/2610.05622)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tradertanmay/undobench)

> Tool-using AI agents are increasingly deployed across enterprise software systems, yet widely used benchmarks primarily evaluate nominal task completion, conflating baseline planning competence with operational fault recovery. We introduce UndoBen...

</details>

<details>
<summary><b>24. Dynamic Harness Search: Building Multi-Agent Systems Per-Query via Prediction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04137) • [📄 arXiv](https://arxiv.org/abs/2610.04137) • [📥 PDF](https://arxiv.org/pdf/2610.04137)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>25. Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05416) • [📄 arXiv](https://arxiv.org/abs/2610.05416) • [📥 PDF](https://arxiv.org/pdf/2610.05416)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent-Hunyuan/Prism)

> Natively training joint video-audio generation models at higher resolutions empowers them to learn richer visual details and sharper motion dynamics. However, full attention incurs quadratic cost and, as resolution increases, spreads attention ove...

</details>

<details>
<summary><b>26. What Gradients Add to Text Leakage in Split Language Models, Counted per Token and per Document</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04128) • [📄 arXiv](https://arxiv.org/abs/2610.04128) • [📥 PDF](https://arxiv.org/pdf/2610.04128)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Adding gradients to a text-reconstruction attack raises token recovery from 94.20% to 97.38% in a controlled GPT-2 split-training experiment. Yet exact recovery of entire 32-token documents jumps from 13.71% to 37.77%—almost 2.8×. The metric also ...

</details>

<details>
<summary><b>27. Representation-Space MMD for Diffusion Language Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06648) • [📄 arXiv](https://arxiv.org/abs/2610.06648) • [📥 PDF](https://arxiv.org/pdf/2610.06648)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yandex-research/dlm-mmd)

> No abstract available.

</details>

<details>
<summary><b>28. PerturBot: Breaking Shortcut Priors in Vision-Language-Action Models with Perturbative Training</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Cong Chen, Hanqing Wang, Tianjian Feng, Chonghao Sima, Mingyu Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04616) • [📄 arXiv](https://arxiv.org/abs/2610.04616) • [📥 PDF](https://arxiv.org/pdf/2610.04616)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aim-uofa/PerturBot)

> A vision--language--action (VLA) policy can complete complex tasks while ignoring the evidence that should determine its actions. An object held near the wrist camera can displace the instructed target. Language and action show the same pattern: a...

</details>

<details>
<summary><b>29. From Knowledge Access to Source Learning: Developing Source-Specific Competence</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02150) • [📄 arXiv](https://arxiv.org/abs/2610.02150) • [📥 PDF](https://arxiv.org/pdf/2610.02150)

**💻 Code:** [⭐ Code](https://github.com/luchengfu6/SourceLearn) • [⭐ Code](https://github.com/huggingface)

> If an AI agent keeps working with the same codebase or documentation, shouldn’t it get better at using it over time? 🧠 Our new paper, “From Knowledge Access to Source Learning: Developing Source-Specific Competence,” introduces SourceLearn — a fra...

</details>

<details>
<summary><b>30. Code2Games: Enabling Coding Agents for Gaming World Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05033) • [📄 arXiv](https://arxiv.org/abs/2610.05033) • [📥 PDF](https://arxiv.org/pdf/2610.05033)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/Code2Games) • [⭐ Code](https://github.com/huggingface)

> Open source code: https://github.com/AIGeeksGroup/Code2Games

</details>

<details>
<summary><b>31. Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wotao Yin, PeterLauLukCh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03872) • [📄 arXiv](https://arxiv.org/abs/2610.03872) • [📥 PDF](https://arxiv.org/pdf/2610.03872)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AI agents are becoming increasingly capable of generating scientific code, but generating code is not the same as improving the algorithms behind it. For numerical solvers, execution feedback can expose poor performance, but rarely reveals its und...

</details>

<details>
<summary><b>32. PaLoRA: Paced Low-Rank Adaptation for Continual Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hao Tang, Fanhu Zeng, Yuxuan Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04226) • [📄 arXiv](https://arxiv.org/abs/2610.04226) • [📥 PDF](https://arxiv.org/pdf/2610.04226)

**💻 Code:** [⭐ Code](https://github.com/liyuxuan-github/PaLoRA) • [⭐ Code](https://github.com/huggingface)

> PaLoRA introduces rank-aware pacing for parameter-efficient continual learning, adaptively controlling low-rank updates according to the effective rank of accumulated knowledge. Combined with adaptive SVD truncation and null-space gradient project...

</details>

<details>
<summary><b>33. PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yueqing Sun, Jiayuan Zhang, Yuxin Chen, Yuchun Miao, Yaorui Shi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32423) • [📄 arXiv](https://arxiv.org/abs/2609.32423) • [📥 PDF](https://arxiv.org/pdf/2609.32423)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The harness surrounding a language model is a central determinant of agent performance. Recent methods optimize harnesses by searching over complete programs, where individual mechanisms are difficult to isolate and reuse. We introduce PluginRSI, ...

</details>

<details>
<summary><b>34. What Matters for Latent Reasoning with Flow Matching</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06666) • [📄 arXiv](https://arxiv.org/abs/2610.06666) • [📥 PDF](https://arxiv.org/pdf/2610.06666)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Abstract: Latent reasoning lets a large language model (LLM) think in a continuous space and verbalize only the answer. We argue that an effective latent thought must meet five requirements: it should be useful, helping produce the correct answer ...

</details>

<details>
<summary><b>35. TextReg: Mitigating Prompt Distributional Overfitting via Regularized Text-Space Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.21318) • [📄 arXiv](https://arxiv.org/abs/2605.21318) • [📥 PDF](https://arxiv.org/pdf/2605.21318)

**💻 Code:** [⭐ Code](https://github.com/luchengfu6/TextReg) • [⭐ Code](https://github.com/huggingface)

> Can prompts overfit just like machine learning models do? Prompt optimization has emerged as a powerful paradigm for improving LLM performance. However, we observed a recurring phenomenon: as optimization progresses, prompts often become longer, a...

</details>

<details>
<summary><b>36. The Missing Primitive: Diagnosing and Repairing Mathematical Reasoning in Large Language Models</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02191) • [📄 arXiv](https://arxiv.org/abs/2610.02191) • [📥 PDF](https://arxiv.org/pdf/2610.02191)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/taco-group/Math-Primitive)

> While Large Language Models (LLMs) have demonstrated striking capabilities on frontier mathematical problems, it remains unclear whether they possess the structural mathematical understanding underlying their solutions. In this paper, we take a fi...

</details>

<details>
<summary><b>37. How to Loop MoE: Flatten the Experts, Untie the Attention</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Wang Yang, Debargha Ganguly, Mohsen Hariri, Chuang Ma, Shouren Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35751) • [📄 arXiv](https://arxiv.org/abs/2609.35751) • [📥 PDF](https://arxiv.org/pdf/2609.35751)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SR-A-W/how-to-loop-moe)

> Looped Transformers reuse the same block across multiple passes, while sparse Mixture-of-Experts models store many experts but activate only a few for each token. These two ideas are naturally complementary: every new pass gives a token another ro...

</details>

<details>
<summary><b>38. CurveCodec 2: Skeleton-agnostic animation compression with a learned entropy model</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04211) • [📄 arXiv](https://arxiv.org/abs/2610.04211) • [📥 PDF](https://arxiv.org/pdf/2610.04211)

**💻 Code:** [⭐ Code](https://github.com/rubbly/CurveCodec) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGAnimation/AnimationCodec)

> CurveCodec v0.2.0 Skeleton-agnostic animation compression with a learned entropy model SIGGRAPH Asia 2026 [ arXiv ] [ homepage ] [ code ] [ demo ] Mingyi Shi 1 · Huancheng Lin 1 · Xuelin Chen 2,* · Taku Komura 1,* 1 The University of Hong Kong · 2...

</details>

<details>
<summary><b>39. OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Mark Harman, Peter O&#39;Hearn, Claire Le Goues, Earl T. Barr, Zhaoyang Chu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02459) • [📄 arXiv](https://arxiv.org/abs/2610.02459) • [📥 PDF](https://arxiv.org/pdf/2610.02459)

**💻 Code:** [⭐ Code](https://github.com/user-attachments/assets/3b134c51-a949-44dd-9474-5249c3879aa0) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/terminalworld/OpenRUA)

> 🤖 OpenRUA : Off-the-shelf coding agents (Claude Code, Codex) directly control robots via native ROS 2 as zero-shot visuomotor policies , with no VLA models and no hand-crafted primitives. 🚫 Zero-Abstraction : Cuts through over-engineered harness s...

</details>

<details>
<summary><b>40. Periscope: Extending Frozen Language Models Beyond Their Context Window</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04047) • [📄 arXiv](https://arxiv.org/abs/2610.04047) • [📥 PDF](https://arxiv.org/pdf/2610.04047)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mohammad2012191/Periscope)

> a training-free method that reads texts past the context window, giving an evidence map at lower memory cost.

</details>

<details>
<summary><b>41. Arm-wise Compositional Generalization in Dual-Arm Vision-Language-Action Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yifan Wang, Zhongbo Zhang, Yuhan Wu, Binghao Ran, Zaibin Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06184) • [📄 arXiv](https://arxiv.org/abs/2610.06184) • [📥 PDF](https://arxiv.org/pdf/2610.06184)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhangzaibin/future-robots)

> We introduce arm-wise compositional generalization, together with a benchmark and a study of architectural design choices. This capability enables familiar skills to be recombined across arms to perform new collaborative tasks—for example, general...

</details>

<details>
<summary><b>42. OmniConfess: Eliciting Token Confessions to Mitigate Omni-Modal Hallucination</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Kaiwen Xue, Zhonghong Ou, Hui Feng, Haoran Luo, Huiqiang Rong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02999) • [📄 arXiv](https://arxiv.org/abs/2610.02999) • [📥 PDF](https://arxiv.org/pdf/2610.02999)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RongHuiQiang/OmniConfess)

> Hi everyone! We introduce OmniConfess, a training-free method for mitigating omni-modal hallucinations. It anchors a candidate response, examines each token’s dependence on individual evidence channels, and uses the resulting confession to guide c...

</details>

<details>
<summary><b>43. SoK: Semantic Decision Engines in Network Control Loops</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Rui Lang, Haochen Gong, Xu Wang, Chen Li, Delong Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06425) • [📄 arXiv](https://arxiv.org/abs/2610.06425) • [📥 PDF](https://arxiv.org/pdf/2610.06425)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OniReimu/SoK-JEV)

> When can a semantic decision engine sit inside a network control loop? We systematize 139 paper families by decision interface, execution path and check ownership. Fifty families claim their engine fits a control loop or time budget, but only four...

</details>

<details>
<summary><b>44. Intent Interpretation at RIC Timescales: Jev Decision Models versus Large Language Models in 6G Open RAN</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Guangsheng Yu, Rui Lang, Haochen Gong, Xu Wang, Delong Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.23136) • [📄 arXiv](https://arxiv.org/abs/2609.23136) • [📥 PDF](https://arxiv.org/pdf/2609.23136)

**💻 Code:** [⭐ Code](https://github.com/OniReimu/6G-JEV) • [⭐ Code](https://github.com/huggingface)

> Which O-RAN control loop can host an intent interpreter? We compare Jev and two other typed decision models with hosted LLMs on RANIntent v1, in closed-loop ns-3 5G-LENA simulation, and on a real A1/E2 path (srsRAN gNB + O-RAN SC near-RT RIC). Int...

</details>

<details>
<summary><b>45. DEPICT: Scoring Text-to-Image Alignment by Answer Agreement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03617) • [📄 arXiv](https://arxiv.org/abs/2610.03617) • [📥 PDF](https://arxiv.org/pdf/2610.03617)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A training free T2I alignment metric that uses the agreement of both modalities for better correlation with humans.

</details>

<details>
<summary><b>46. Learning Steadily: Accumulating Relative Point Margin Scores for Face Image Quality Assessment</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31662) • [📄 arXiv](https://arxiv.org/abs/2609.31662) • [📥 PDF](https://arxiv.org/pdf/2609.31662)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>47. Learning to Learn a Language</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Holger Fröhlich, lennartcb

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05879) • [📄 arXiv](https://arxiv.org/abs/2610.05879) • [📥 PDF](https://arxiv.org/pdf/2610.05879)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/cbl/prior-fitted-language-model)

> PFLM is a 300M-parameter byte-level model trained without any natural language. Every training sequence comes from a freshly sampled recurrent causal model, so each one is a new "language" and the only way to predict it is to infer its rules from ...

</details>

<details>
<summary><b>48. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Anatulya Nandi, Liuyu Bian, Jinhong Li, Sirui Xu, Yucheng Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06850) • [📄 arXiv](https://arxiv.org/abs/2610.06850) • [📥 PDF](https://arxiv.org/pdf/2610.06850)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 48 |
| 📅 Today | [`2026-10-06.json`](data/daily/2026-10-06.json) | 48 |
| 📆 This Week | [`2026-W40.json`](data/weekly/2026-W40.json) | 89 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 384 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-06 | 48 | [View JSON](data/daily/2026-10-06.json) |
| 📄 2026-10-05 | 41 | [View JSON](data/daily/2026-10-05.json) |
| 📄 2026-10-04 | 84 | [View JSON](data/daily/2026-10-04.json) |
| 📄 2026-10-03 | 84 | [View JSON](data/daily/2026-10-03.json) |
| 📄 2026-10-02 | 66 | [View JSON](data/daily/2026-10-02.json) |
| 📄 2026-10-01 | 61 | [View JSON](data/daily/2026-10-01.json) |
| 📄 2026-09-30 | 72 | [View JSON](data/daily/2026-09-30.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W40 | 89 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 384 | [View JSON](data/monthly/2026-10.json) |
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
