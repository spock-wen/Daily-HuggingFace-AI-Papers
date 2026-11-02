<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-30-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9470+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">30</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">30</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">69</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9470+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 02, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22740) • [📄 arXiv](https://arxiv.org/abs/2610.22740) • [📥 PDF](https://arxiv.org/pdf/2610.22740)

**💻 Code:** [⭐ Code](https://github.com/beita6969/R2Orch) • [⭐ Code](https://github.com/huggingface)

> R²Orch (Recursive Self-Play Orchestration) trains an agent orchestrator without a hand-designed curriculum: an inner self-play loop improves the orchestrator on tasks a Proposer picks, and an outer loop improves how that inner loop learns. The Pro...

</details>

<details>
<summary><b>2. Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39497) • [📄 arXiv](https://arxiv.org/abs/2610.39497) • [📥 PDF](https://arxiv.org/pdf/2610.39497)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come i...

</details>

<details>
<summary><b>3. FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36545) • [📄 arXiv](https://arxiv.org/abs/2610.36545) • [📥 PDF](https://arxiv.org/pdf/2610.36545)

**💻 Code:** [⭐ Code](https://github.com/Lyne1/FrameForge) • [⭐ Code](https://github.com/huggingface)

> Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual tr...

</details>

<details>
<summary><b>4. Wizard: Manipulate Any World in Real Time via Agentic Control</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40339) • [📄 arXiv](https://arxiv.org/abs/2610.40339) • [📥 PDF](https://arxiv.org/pdf/2610.40339)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🪄 Wizard: Manipulate Any World in Real Time via Agentic Control! Existing game world models produce realistic visuals but remain constrained by familiar environments and predefined motions. Control largely focuses on locomotion, with limited suppo...

</details>

<details>
<summary><b>5. Latent Reasoning in Continuous Space for Unified Multimodal Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42149) • [📄 arXiv](https://arxiv.org/abs/2610.42149) • [📥 PDF](https://arxiv.org/pdf/2610.42149)

**💻 Code:** [⭐ Code](https://github.com/rootyJeon/LARC) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>6. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fan Zhang, Xudong Wang, Kehong Wu, Hongyu Qu, Jack-sherry

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40373) • [📄 arXiv](https://arxiv.org/abs/2610.40373) • [📥 PDF](https://arxiv.org/pdf/2610.40373)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to en...

</details>

<details>
<summary><b>7. CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent Systems</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Hyunwoo J. Kim, Jinsung Yoon, Jonathan Minho Chung, happy8825, jonghakim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34722) • [📄 arXiv](https://arxiv.org/abs/2610.34722) • [📥 PDF](https://arxiv.org/pdf/2610.34722)

**💻 Code:** [⭐ Code](https://github.com/mlvlab/CEPO) • [⭐ Code](https://github.com/huggingface)

> Multi-agent systems (MAS) require both effective coordination and specialized task execution. Existing prompt optimization approaches typically couple these functions within agent-specific prompts. We introduce Coordinator-Executor Prompt Optimiza...

</details>

<details>
<summary><b>8. CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents</b> ⭐ 32</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40799) • [📄 arXiv](https://arxiv.org/abs/2610.40799) • [📥 PDF](https://arxiv.org/pdf/2610.40799)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/waltstephen/CaPtain)

> Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-aspolicy (CaP) puts r...

</details>

<details>
<summary><b>9. Apriel Voice 27B Preview: An Open Model for Speech, Reasoning, and Tool Use</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40738) • [📄 arXiv](https://arxiv.org/abs/2610.40738) • [📥 PDF](https://arxiv.org/pdf/2610.40738)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Apriel Voice 27B Preview is an open speech-language model that integrates speech understanding, reasoning, and tool use within a shared backbone, achieving strong results on audio benchmarks through a two-stage training procedure with online disti...

</details>

<details>
<summary><b>10. ReLift: Dense 3D Tracking as Lifted Trajectory Repair</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42136) • [📄 arXiv](https://arxiv.org/abs/2610.42136) • [📥 PDF](https://arxiv.org/pdf/2610.42136)

**💻 Code:** [⭐ Code](https://github.com/ReLift3D/ReLift) • [⭐ Code](https://github.com/huggingface)

> ReLift: dense 3D tracking from monocular video. We combine off-the-shelf 2D trackers and 3D geometry models with a small trajectory corrector that repairs lifting errors and recovers occluded motion. Trained once on simulated lifting errors, the c...

</details>

<details>
<summary><b>11. Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37918) • [📄 arXiv](https://arxiv.org/abs/2610.37918) • [📥 PDF](https://arxiv.org/pdf/2610.37918)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/DefakerOne2) • [⭐ Code](https://github.com/huggingface)

> Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage

</details>

<details>
<summary><b>12. Probing Spatial State Representations in Visual Foundation Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40636) • [📄 arXiv](https://arxiv.org/abs/2610.40636) • [📥 PDF](https://arxiv.org/pdf/2610.40636)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>13. WorldBridge: Bridging Video and Action for Task Generalization in World Action Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yaoxu Lyu, Liangkai Li, Hao Li, Yubo Guo, Jun Cen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40748) • [📄 arXiv](https://arxiv.org/abs/2610.40748) • [📥 PDF](https://arxiv.org/pdf/2610.40748)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project Page: https://worldbridge-jd.github.io/

</details>

<details>
<summary><b>14. REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zhenglin Wan, Haoyuan Chen, Zhengfeiyang Zhang, Yixing Ma, Pengfei Zhou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42053) • [📄 arXiv](https://arxiv.org/abs/2610.42053) • [📥 PDF](https://arxiv.org/pdf/2610.42053)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> REA offers a practical way to coordinate slow reasoning of the embodied agent with fast robot policies, improving reliability through routing and recovery while keeping ongoing execution independent of the brain’s latency.

</details>

<details>
<summary><b>15. GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31222) • [📄 arXiv](https://arxiv.org/abs/2610.31222) • [📥 PDF](https://arxiv.org/pdf/2610.31222)

**💻 Code:** [⭐ Code](https://github.com/arm-research/AAIR-GLOW-FM) • [⭐ Code](https://github.com/huggingface)

> GLOW-FM:  Generative low-light image enhancement using Flow Matching. GLOW-FM combines a lightweight Tiny-VAE encoder with an Hourglass Diffusion Transformer (HDiT) architecture to perform efficient enhancement in a compact latent space. Trained w...

</details>

<details>
<summary><b>16. HALO: Human-Grounded Granular Evaluation of Proactive Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39086) • [📄 arXiv](https://arxiv.org/abs/2610.39086) • [📥 PDF](https://arxiv.org/pdf/2610.39086)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/CedricPei/HALO)

> Proactive agents must decide whether, when, and how far to assist without an explicit request. Existing evaluations often rely on automated scores or binary verdicts, offering limited human diagnosis of evidence use and intervention quality. To ad...

</details>

<details>
<summary><b>17. WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16927) • [📄 arXiv](https://arxiv.org/abs/2610.16927v2) • [📥 PDF](https://arxiv.org/pdf/2610.16927)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Personalization should clarify user intent, not overwrite it. How can we build a compact query rewriter that understands users' personalized intent while avoiding intent drift? We introduce WeFair , a fidelity-aware alignment framework for persona...

</details>

<details>
<summary><b>18. On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40945) • [📄 arXiv](https://arxiv.org/abs/2610.40945) • [📥 PDF](https://arxiv.org/pdf/2610.40945)

**💻 Code:** [⭐ Code](https://github.com/Skylanding/Training-Inference-Mismatch) • [⭐ Code](https://github.com/huggingface)

> We split the training-inference mismatch in LLM RL into a numerical discrepancy, which stays nearly constant, and a policy lag, which compounds through the trainer's own updates. From this split we derive the discrepancy-lag correction (DLC), whic...

</details>

<details>
<summary><b>19. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hao Zhu, Ria Doshi, Cherie Ho, Suning Huang, danielwusg

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42141) • [📄 arXiv](https://arxiv.org/abs/2610.42141) • [📥 PDF](https://arxiv.org/pdf/2610.42141)

**💻 Code:** [⭐ Code](https://github.com/roboarchitect-ai/RoboArchitect) • [⭐ Code](https://github.com/huggingface)

> RoboArchitect automatically designs and continually improves a robotic agent around a frozen robot policy, without updating any weights. These agents develop their own control routines. Most converge on a dynamic split between the VLA policy and c...

</details>

<details>
<summary><b>20. When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40256) • [📄 arXiv](https://arxiv.org/abs/2610.40256) • [📥 PDF](https://arxiv.org/pdf/2610.40256)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> CodeSpecWeave synthesizes long-horizon coding tasks with interdependent specifications and reliable tests, grounded in real developer requirements. RL on these tasks substantially improves MiMo models on DeepSWE-v1.1, and CodeSpecWeave-Bench revea...

</details>

<details>
<summary><b>21. Supervising the Visible State: Separating Representation from View Selection in Streaming Video</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34926) • [📄 arXiv](https://arxiv.org/abs/2610.34926) • [📥 PDF](https://arxiv.org/pdf/2610.34926)

**💻 Code:** [⭐ Code](https://github.com/yihaohu0118/ViSS) • [⭐ Code](https://github.com/huggingface)

> An action seen once and the same action seen three times receive the same action-recognition label, so that supervision does not require a model to count. Answers shared across histories that differ in event order, accumulation, or relations leave...

</details>

<details>
<summary><b>22. MemSteer: Turning User Histories into Supervision for Agent Memory Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39276) • [📄 arXiv](https://arxiv.org/abs/2610.39276) • [📥 PDF](https://arxiv.org/pdf/2610.39276)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🧠 You set a deadline by email, then moved it in chat. Which date will your AI assistant remember? We built MemSteer at Peking University and Microsoft Research Asia to turn a user’s own history into tests for agent memory. It connects facts across...

</details>

<details>
<summary><b>23. No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dongyoon Han, Jong-Seok Lee, Jaehui Hwang, Jaemyung Yu, tunatone

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40914) • [📄 arXiv](https://arxiv.org/abs/2610.40914) • [📥 PDF](https://arxiv.org/pdf/2610.40914)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We find that REPA and dispersive regularization substantially reorganize AdaLN-Zero residual gates in diffusion transformers, suggesting that training acceleration arises partly from reshaping the residual gating pathway. Broader gate participatio...

</details>

<details>
<summary><b>24. CausalWAM: Learning the Causes of Actions in World Action Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42096) • [📄 arXiv](https://arxiv.org/abs/2610.42096) • [📥 PDF](https://arxiv.org/pdf/2610.42096)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing CWAM (Causal WAM), a world action model that provably learns the true causes of actions.

</details>

<details>
<summary><b>25. Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37393) • [📄 arXiv](https://arxiv.org/abs/2610.37393) • [📥 PDF](https://arxiv.org/pdf/2610.37393)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! Excited to share our new preprint, QCP: Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling "Success is only the beginning. How a robot performs a task matters too." Carrying a drink calls for stability. C...

</details>

<details>
<summary><b>26. VoxLock: Target-Speaker Extraction for Voice Agents Without an Enrollment Step</b> ⭐ 85</summary>

<br/>

**👥 Authors:** arbazsiddiqui

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40727) • [📄 arXiv](https://arxiv.org/abs/2610.40727) • [📥 PDF](https://arxiv.org/pdf/2610.40727)

**💻 Code:** [⭐ Code](https://github.com/arbazsiddiqui/voxlock) • [⭐ Code](https://github.com/huggingface)

> Author here. VoxLock is a 27M-parameter streaming voice isolator for voice agents that needs no enrollment step: it takes the caller's voice from the first seconds of the call by itself. On the Krisp Voice Isolation Benchmark (265 real recordings)...

</details>

<details>
<summary><b>27. SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Mingxiao Li, Xue Liu, Bowei He, Yusheng Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37919) • [📄 arXiv](https://arxiv.org/abs/2610.37919) • [📥 PDF](https://arxiv.org/pdf/2610.37919)

**💻 Code:** [⭐ Code](https://github.com/yushengzh/scigame) • [⭐ Code](https://github.com/huggingface)

> SciGame separates scientific law discovery from memorization. Every relation becomes a "scientific card" generating two worlds behind one interface: an Original environment following the published law, and a Counterfactual twin with a mutated but ...

</details>

<details>
<summary><b>28. TernScope: Model-Hardware Co-Design for Efficient Ternary Endoscopic Segmentation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.29617) • [📄 arXiv](https://arxiv.org/abs/2610.29617) • [📥 PDF](https://arxiv.org/pdf/2610.29617)

**💻 Code:** [⭐ Code](https://github.com/ReaganWu/TernScope) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! I'm the first author of TernScope. Can a tiny segmentation network use ternary weights throughout—including the input and prediction layers—and translate that into smaller hardware? We co-design an endoscopic segmentation model and a ...

</details>

<details>
<summary><b>29. SketchDirector: Complex Scene Sketching via Agentic Layout Reasoning and Detail Refinement</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41260) • [📄 arXiv](https://arxiv.org/abs/2610.41260) • [📥 PDF](https://arxiv.org/pdf/2610.41260)

**💻 Code:** [⭐ Code](https://github.com/GVCLab/SketchDirector) • [⭐ Code](https://github.com/huggingface)

> Existing sketch generation methods often rely on image guidance and are largely limited to individual objects or simplified scenes, leaving text-guided complex scene sketching underexplored. We present SketchDirector, an agentic framework that mim...

</details>

<details>
<summary><b>30. TurnTurk-GPT: Text-Based Turn-Taking Prediction for Turkish</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mustafa Sertaç Türkel, Nur Yağmur Tuncer, Fatma Nur Korkmaz, Ahmet Tuğrul Bayrak

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42010) • [📄 arXiv](https://arxiv.org/abs/2610.42010) • [📥 PDF](https://arxiv.org/pdf/2610.42010)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper presents TurnTurk-GPT, a text-based turn-taking predictor for Turkish obtained by fine-tuning a Turkish GPT-2 model with the TurnGPT objective on synthetic and real dialogue, and evaluates it on real Turkish conversation against rule ba...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 30 |
| 📅 Today | [`2026-11-02.json`](data/daily/2026-11-02.json) | 30 |
| 📆 This Week | [`2026-W44.json`](data/weekly/2026-W44.json) | 30 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 69 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-02 | 30 | [View JSON](data/daily/2026-11-02.json) |
| 📄 2026-11-01 | 39 | [View JSON](data/daily/2026-11-01.json) |
| 📄 2026-10-31 | 39 | [View JSON](data/daily/2026-10-31.json) |
| 📄 2026-10-30 | 30 | [View JSON](data/daily/2026-10-30.json) |
| 📄 2026-10-29 | 9 | [View JSON](data/daily/2026-10-29.json) |
| 📄 2026-10-28 | 40 | [View JSON](data/daily/2026-10-28.json) |
| 📄 2026-10-27 | 43 | [View JSON](data/daily/2026-10-27.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W44 | 30 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 69 | [View JSON](data/monthly/2026-11.json) |
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
