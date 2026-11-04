<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-43-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9551+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">43</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">111</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">150</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9551+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 04, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Zhenglin Wan, Weidong Tang, Hexin Wang, Yixing Ma, Pengfei Zhou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05275) • [📄 arXiv](https://arxiv.org/abs/2611.05275) • [📥 PDF](https://arxiv.org/pdf/2611.05275)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InfRec-Cardinal/route-anything)

> A potential path to AGI could be a router: Route Anything brings routing to text, images, video, speech, code, and robots, delivering 8.82× average relative efficiency across four settings and exceeding the performance of the best fixed model in d...

</details>

<details>
<summary><b>2. Think Less, Locally: Local Preference Learning for Reasoning Compression</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04814) • [📄 arXiv](https://arxiv.org/abs/2611.04814) • [📥 PDF](https://arxiv.org/pdf/2611.04814)

**💻 Code:** [⭐ Code](https://github.com/MuyaoYuan/LoCo) • [⭐ Code](https://github.com/huggingface)

> Model is released at: https://huggingface.co/MuyaoYuan/LoCo-7B

</details>

<details>
<summary><b>3. Words Caught in the Heart: Simulating Person-Specific Expression for Self-Opaque Clients in Psychotherapy</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.00617) • [📄 arXiv](https://arxiv.org/abs/2611.00617) • [📥 PDF](https://arxiv.org/pdf/2611.00617)

**💻 Code:** [⭐ Code](https://github.com/whunextgen/Pandora) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>4. MoviEdit: Long-form Multi-Shot Video Editing Made Easy</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02737) • [📄 arXiv](https://arxiv.org/abs/2611.02737) • [📥 PDF](https://arxiv.org/pdf/2611.02737)

**💻 Code:** [⭐ Code](https://github.com/adobe-research/MoviEdit-Bench) • [⭐ Code](https://github.com/huggingface)

> Long-form multi-shot video editing requires an intended edit to remain coherent across abrupt changes in scene, viewpoint, and subject appearance, while processing substantially longer visual context than conventional single-shot editors. We intro...

</details>

<details>
<summary><b>5. Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04916) • [📄 arXiv](https://arxiv.org/abs/2611.04916) • [📥 PDF](https://arxiv.org/pdf/2611.04916)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This technical report shares practical lessons from the evolution of Kling’s video-generation systems. It argues that the next bottleneck is no longer visual rendering, but semantic control—the ability to understand what to generate, preserve, org...

</details>

<details>
<summary><b>6. DreamX: Video Diffusion Model is a Universal Latent Action Learner</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05377) • [📄 arXiv](https://arxiv.org/abs/2611.05377) • [📥 PDF](https://arxiv.org/pdf/2611.05377)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DreamX turns a pretrained video diffusion model into a latent action learner. Its encoder reads compact latent actions out of human and robot videos while the video prior takes care of appearance, so the latents capture motion alone. The same late...

</details>

<details>
<summary><b>7. Axion 1.0: Open Agent Foundation Models, Simplified</b> ⭐ 19</summary>

<br/>

**👥 Authors:** Jingchen Sun, Yijun Liang, Jiayu Zheng, Yunjie Tian, Yuqi Jia

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03233) • [📄 arXiv](https://arxiv.org/abs/2611.03233) • [📥 PDF](https://arxiv.org/pdf/2611.03233)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bytedance/axion1_0)

> Introducing Axion 1.0: Open Agent Foundation Models, Simplified. Strong scientific reasoning and tool use with a simple post-training recipe: two lightweight supervised fine-tuning stages followed by reinforcement learning. Learn to reason: model-...

</details>

<details>
<summary><b>8. RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02497) • [📄 arXiv](https://arxiv.org/abs/2611.02497) • [📥 PDF](https://arxiv.org/pdf/2611.02497)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RoboColosseum/robocolosseum-client)

> General-purpose robot policies must work across robots, tasks, and environments, yet the variation that makes physical trials informative also makes them difficult to reproduce. We introduce RoboColosseum, a distributed evaluation framework that c...

</details>

<details>
<summary><b>9. Factorized MLLM Embeddings for Composed Image Retrieval</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05193) • [📄 arXiv](https://arxiv.org/abs/2611.05193) • [📥 PDF](https://arxiv.org/pdf/2611.05193)

**💻 Code:** [⭐ Code](https://github.com/cvlab-kaist/FactEmbed) • [⭐ Code](https://github.com/huggingface)

> FactEmbed lets users find images by combining a reference image with a text modification, a query that neither modality can express easily on its own. TL;DR: Before embedding a composed query, let the MLLM imagine the target through factorized lat...

</details>

<details>
<summary><b>10. ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05036) • [📄 arXiv](https://arxiv.org/abs/2611.05036) • [📥 PDF](https://arxiv.org/pdf/2611.05036)

**💻 Code:** [⭐ Code](https://github.com/dongguanting/ToolSpace) • [⭐ Code](https://github.com/huggingface)

> Happy to share our latest work on agent environment synthesis: 🌟 ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents Most existing environment synthesis methods are data-centric: they first build the underlying database, ...

</details>

<details>
<summary><b>11. YANAMI: A Large-Scale Multimodal Dataset and Benchmark for Multiturn Stateful Interaction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Siyu Li, Junming Liu, Tengyue Nong, Shengyu Wang, HarrisonPENG

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05280) • [📄 arXiv](https://arxiv.org/abs/2611.05280) • [📥 PDF](https://arxiv.org/pdf/2611.05280)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing YANAMI 🌍 A dataset & benchmark for stateful multimodal interaction: • 400K dialogues, 2M+ images • Track constraints & incorporate corrections • Evaluate understanding + visual realization Fine-tuning BAGEL: +13.23 benchmark points; +1...

</details>

<details>
<summary><b>12. EvoTeam: Multi-Agent Collaboration via Evolving Teams</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39813) • [📄 arXiv](https://arxiv.org/abs/2610.39813) • [📥 PDF](https://arxiv.org/pdf/2610.39813)

**💻 Code:** [⭐ Code](https://github.com/DEEP-JLU/EvoTeam) • [⭐ Code](https://github.com/huggingface)

> LLM-based multi-agent systems (MAS) rely on collaboration among specialized agents to solve complex tasks. Existing methods improve MAS by refining the prompts, skills, and execution strategies of individual agents based on task feedback. However,...

</details>

<details>
<summary><b>13. VidUEU-Agent: A Data-Curation Agent for Multimodal Understanding, Editing, and Unified Tasks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haoran Li, Lingyi Meng, Zecong Tang, Weitong Lian, Tengju Ru

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04418) • [📄 arXiv](https://arxiv.org/abs/2611.04418) • [📥 PDF](https://arxiv.org/pdf/2611.04418)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LRuca/VidUEU-Agent)

> 🚀 We are excited to share our latest work: “VidUEU-Agent: A Data-Curation Agent for Multimodal Understanding, Editing, and Unified Tasks”! The scarcity and high annotation cost of high-quality multimodal instruction data remain major bottlenecks f...

</details>

<details>
<summary><b>14. ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02079) • [📄 arXiv](https://arxiv.org/abs/2611.02079) • [📥 PDF](https://arxiv.org/pdf/2611.02079)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/microsoft/AutoSaddler/tree/feat/paretosaddler)

> The code is available at: https://github.com/microsoft/AutoSaddler/tree/feat/paretosaddler . We welcome your comments and feedback!

</details>

<details>
<summary><b>15. WebHarbor: Docking Real Websites for Evolving GUI Agent Environments</b> ⭐ 44</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03634) • [📄 arXiv](https://arxiv.org/abs/2611.03634) • [📥 PDF](https://arxiv.org/pdf/2611.03634)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aiming-lab/WebHarbor)

> We introduce WebHarbor, a suite of 153 executable, dockerized website environments that reconstruct the visual interfaces, content, and workflows of real-world web services, plus 3,518 tasks for evaluating and training GUI web agents. Why: live-we...

</details>

<details>
<summary><b>16. SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding</b> ⭐ 29</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02501) • [📄 arXiv](https://arxiv.org/abs/2611.02501) • [📥 PDF](https://arxiv.org/pdf/2611.02501)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/StargazerX0/SpecPilot)

> SpecPilot is an agentic loop that discovers lossless speculative decoding optimizations for each deployment, raising the speedup over AR from 4.46× to 10.87×. Paper: https://arxiv.org/pdf/2611.02501 Code: https://github.com/StargazerX0/SpecPilot P...

</details>

<details>
<summary><b>17. "Shall We Approve?" Consequence-Aware Approval for Autonomous Coding Agents</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40753) • [📄 arXiv](https://arxiv.org/abs/2610.40753) • [📥 PDF](https://arxiv.org/pdf/2610.40753)

**💻 Code:** [⭐ Code](https://github.com/wudaoz/Caper) • [⭐ Code](https://github.com/huggingface)

> Does a coding agent really know what its next command will do? Approving every command by hand does not scale: Claude Code users approve 93% of permission prompts anyway. So agents now rely on automated approvers, such as Claude Code's Auto Mode, ...

</details>

<details>
<summary><b>18. MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Brian Shim, Yu Zhang, Mingze Yuan, Xiwei Cheng, Yikun Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39714) • [📄 arXiv](https://arxiv.org/abs/2610.39714) • [📥 PDF](https://arxiv.org/pdf/2610.39714)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>19. FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04303) • [📄 arXiv](https://arxiv.org/abs/2611.04303) • [📥 PDF](https://arxiv.org/pdf/2611.04303)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> FlowTranslator establishes flow-based editing as a strong, fully training-free baseline for IIMT.

</details>

<details>
<summary><b>20. PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaowen Chang, Tengfei Ma, Lihao Guo, Wentao Ma, Travis Davies

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04870) • [📄 arXiv](https://arxiv.org/abs/2611.04870) • [📥 PDF](https://arxiv.org/pdf/2611.04870)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> PrimeSim is an action-conditioned, multiview world model that runs as a robot simulator. It starts from a pretrained video generator, midtrains on 30,110 hours across 22 platforms, then posttrains into a causal few-step generator. Posttraining com...

</details>

<details>
<summary><b>21. Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40747) • [📄 arXiv](https://arxiv.org/abs/2610.40747) • [📥 PDF](https://arxiv.org/pdf/2610.40747)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Mage-VL-Cowork presents a complete recipe for training a hybrid computer-use model—from multimodal alignment for enhanced GUI perception and office-oriented coding to agentic capabilities and hybrid policy execution for completing everyday office ...

</details>

<details>
<summary><b>22. Recursa: Toward Recursively Self-Improving Foundation Model Systems</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04035) • [📄 arXiv](https://arxiv.org/abs/2611.04035) • [📥 PDF](https://arxiv.org/pdf/2611.04035)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> When a foundation model moves into a new domain, there's usually little expert-written data or reliable supervision to train on. Recursa adapts to the domain by learning from its own experience, without human experts or a stronger teacher model. A...

</details>

<details>
<summary><b>23. Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.40574) • [📄 arXiv](https://arxiv.org/abs/2610.40574) • [📥 PDF](https://arxiv.org/pdf/2610.40574)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/xingzhejun/MTA-OPSD)

> On-policy Self-distillation (OPSD) has proven effective for post-training large language models by constructing a teacher conditioned on privileged references. However, existing approaches keep the teacher fixed either throughout training by consi...

</details>

<details>
<summary><b>24. Near-Zero Token Embeddings Silently Stall Training in Gated Sequence Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mingjian Zhao, Haoran Song, Yuxin Wang, Xin Liu, BBBBCHAN

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04449) • [📄 arXiv](https://arxiv.org/abs/2611.04449) • [📥 PDF](https://arxiv.org/pdf/2611.04449)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Near-zero input tokens trigger gradient blowup in gated models, not mid-sequence Transformers.

</details>

<details>
<summary><b>25. Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished Tasks?</b> ⭐ 26</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02017) • [📄 arXiv](https://arxiv.org/abs/2611.02017) • [📥 PDF](https://arxiv.org/pdf/2611.02017)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Miraclecsc/Switch-SWE)

> Switch-SWE is a repository-level benchmark for evaluating whether coding agents can resume a focus task after working on other unfinished tasks in the same repository. Each task is evaluated in matched uninterrupted and switched sessions, requirin...

</details>

<details>
<summary><b>26. Can AI Reviewers See Your Efforts to Improve Your Paper? A Large-Scale Study of Paper Revision Trajectories</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02244) • [📄 arXiv](https://arxiv.org/abs/2611.02244) • [📥 PDF](https://arxiv.org/pdf/2611.02244)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/c-steve-wang/PaperTrace)

> Do AI reviewers recognize the improvements authors make through revision? We introduce PaperTrajectory-2026, covering 6,959 paper trajectories across five AI conferences, with automatic annotations along 14 revision dimensions. Evaluating eight AI...

</details>

<details>
<summary><b>27. LOLPlay: Benchmarking Real-Time Visual Agents in League of Legends</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Zhaojian Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03685) • [📄 arXiv](https://arxiv.org/abs/2611.03685) • [📥 PDF](https://arxiv.org/pdf/2611.03685)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/answers111/LOLPlay)

> Benchmarking visual agents in real-world LOL game.

</details>

<details>
<summary><b>28. RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05163) • [📄 arXiv](https://arxiv.org/abs/2611.05163) • [📥 PDF](https://arxiv.org/pdf/2611.05163)

**💻 Code:** [⭐ Code](https://github.com/ryan-seungyong-lee/RoboTryOn) • [⭐ Code](https://github.com/huggingface)

> RoboTryOn keeps the demonstrated motion and swaps the human for the robot (like Virtual Try-On!). From an egocentric human video alone, it synthesizes a robot demonstration (video and joint actions) that teaches a policy tasks it has never been te...

</details>

<details>
<summary><b>29. You don't need long context</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05306) • [📄 arXiv](https://arxiv.org/abs/2611.05306) • [📥 PDF](https://arxiv.org/pdf/2611.05306)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Later tokens are costlier to generate than earlier tokens. On frontier open weight models, the disparity in cost may rise to as much as 7x. Through frequent compaction, we show across a broad range of long-horizon and long-input tasks that frontie...

</details>

<details>
<summary><b>30. Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with the Embodied Agent Arena</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Yangkai Wei, Yehang Zhang, Zexi Li, Pukun Zhao, Haojian Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.00854) • [📄 arXiv](https://arxiv.org/abs/2610.00854) • [📥 PDF](https://arxiv.org/pdf/2610.00854)

**💻 Code:** [⭐ Code](https://github.com/embodied-agent-arena/embodied-agent-arena) • [⭐ Code](https://github.com/huggingface)

> Embodied Agent Arena evaluates ten frontier VLM agents on 1,000 cases across Geometry, Spatial Reasoning, Affordance, Task Planning, and Manipulation. It combines 32 established sources with GeoProbe, a new 168-case benchmark for camera, motion, d...

</details>

<details>
<summary><b>31. Every Pixel Is an Option: A System One Model for Medical Ultrasound Biometry</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03360) • [📄 arXiv](https://arxiv.org/abs/2611.03360) • [📥 PDF](https://arxiv.org/pdf/2611.03360)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>32. Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Tanya Sah, Mehak Kapoor, Harshul Jain, Parv17k

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36915) • [📄 arXiv](https://arxiv.org/abs/2610.36915) • [📥 PDF](https://arxiv.org/pdf/2610.36915)

**💻 Code:** [⭐ Code](https://github.com/Parv17k/decision-models-conflict-typing) • [⭐ Code](https://github.com/huggingface)

> Github code : https://github.com/Parv17k/decision-models-conflict-typing .

</details>

<details>
<summary><b>33. Is Your Long-Horizon Benchmark Really Deep? Measuring and Synthesizing Depth in Terminal Tasks</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Zixuan Weng, Yuyang Wu, Hang Hua, Yue Huang, AlanRosston520

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.01927) • [📄 arXiv](https://arxiv.org/abs/2611.01927) • [📥 PDF](https://arxiv.org/pdf/2611.01927)

**💻 Code:** [⭐ Code](https://github.com/AlanRosston/Depth) • [⭐ Code](https://github.com/huggingface)

> Long-horizon terminal tasks are used to evaluate and train agents. Human-curated datasets are scarce, so many synthesis methods have emerged. They usually measure the length of a task by the turns a model needs to pass it, and its difficulty by la...

</details>

<details>
<summary><b>34. What We Keep of What We Forget: Replacement Operators and Routing Semantics in Training-Free MoE Expert Pruning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Faisal Shafait, Momina Moetesum, Sehrish Bibi, drezzaali

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.41366) • [📄 arXiv](https://arxiv.org/abs/2610.41366) • [📥 PDF](https://arxiv.org/pdf/2610.41366)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The paper provides a controlled fixed-pruning-mask comparison of replacement/rerouting strategies and shows that post-pruning gate scale is part of the pruning algorithm, proposing the trained-scale rule: preserving the router’s training-time norm...

</details>

<details>
<summary><b>35. Is Forgetting Unified? Exploring Concept Unlearning in Unified Multimodal Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04467) • [📄 arXiv](https://arxiv.org/abs/2611.04467) • [📥 PDF](https://arxiv.org/pdf/2611.04467)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Long-horizon embodied tasks require agents to learn, reason, and generalize robustly across complex real-world environments. However, existing approaches often struggle with partial observability, fragmented spatial reasoning, and inefficient inte...

</details>

<details>
<summary><b>36. Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yue Wang, Steven Hoi, Panrong Tong, Quyu Kong, Yuxiang Chai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.39251) • [📄 arXiv](https://arxiv.org/abs/2610.39251) • [📥 PDF](https://arxiv.org/pdf/2610.39251)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Trajectory-level GRPO is a common approach for training multi-step GUI agents, but repeatedly rolling out complete trajectories from the task root can be inefficient: task-level rewards provide coarse supervision over which intermediate decisions ...

</details>

<details>
<summary><b>37. SeMo3D: Unifying 3D Generation, Editing, and Completion via Selective Modeling</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02568) • [📄 arXiv](https://arxiv.org/abs/2611.02568) • [📥 PDF](https://arxiv.org/pdf/2611.02568)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XiaokunSun/SeMo3D)

> 3D generation, editing, and completion are typically treated as regenerating the complete 3D asset under task-specific constraints, even when only a local region needs modification. This leads to task isolation, inconsistency in content that shoul...

</details>

<details>
<summary><b>38. Muon Makes the First Mixture-of-Experts Layer Harder to Balance</b> ⭐ 0</summary>

<br/>

**👥 Authors:** marcoshernanz

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37914) • [📄 arXiv](https://arxiv.org/abs/2610.37914) • [📥 PDF](https://arxiv.org/pdf/2610.37914)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/marcoshernanz/muon-moe-routing)

> Open MoE recipes disagree on whether Muon should train the router. DeepSeek trains it with Muon, Qwen keeps it on AdamW. We found the router's optimizer isn't the problem. With Muon on the rest of the network, the inputs to the router of the first...

</details>

<details>
<summary><b>39. Going Deeper With Memories</b> ⭐ 0</summary>

<br/>

**👥 Authors:** akhadangi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05255) • [📄 arXiv](https://arxiv.org/abs/2611.05255) • [📥 PDF](https://arxiv.org/pdf/2611.05255)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/akhadangi/deepmem)

> DeepMem

</details>

<details>
<summary><b>40. Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Lenh Cong Phan Pham, Nhan Huu Tran, Nhu Huynh Thi Le, Thu Anh Ngoc Le, Huan Phong Thai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03747) • [📄 arXiv](https://arxiv.org/abs/2611.03747) • [📥 PDF](https://arxiv.org/pdf/2611.03747)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/nhunguet/SearchEngine)

> Demo

</details>

<details>
<summary><b>41. Kierston & KierstonBench: Simulation of Allentown, PA and Evaluation of Language Models in Crime Investigation and Surveillance Tasks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Svyatoslav Dorofeev, Andrew Semenov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.04785) • [📄 arXiv](https://arxiv.org/abs/2611.04785) • [📥 PDF](https://arxiv.org/pdf/2611.04785)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Kiz8-Team/kierston-oss)

> .

</details>

<details>
<summary><b>42. GigaSpeech 3: Scaling Multi-Dialect Arabic Speech Recognition with Weakly Labeled Data</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02476) • [📄 arXiv](https://arxiv.org/abs/2611.02476) • [📥 PDF](https://arxiv.org/pdf/2611.02476)

**💻 Code:** [⭐ Code](https://github.com/SpeechColab/GigaSpeechBench) • [⭐ Code](https://github.com/Antares-97/GigaSpeech3) • [⭐ Code](https://github.com/huggingface)

> 🎙️ GigaSpeech 3 Scaling Multi-Dialect Arabic Speech Recognition with Weakly Labeled Data GigaSpeech 3 is a large-scale, weakly labeled Arabic speech corpus containing approximately 10 million speech segments across Algerian (DZA), Egyptian (EGY), ...

</details>

<details>
<summary><b>43. Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.03183) • [📄 arXiv](https://arxiv.org/abs/2611.03183) • [📥 PDF](https://arxiv.org/pdf/2611.03183)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can an autonomous research agent improve AlphaFold 3 without modifying its model weights? We introduce an agent that treats AlphaFold 3 as a black-box experimental instrument, autonomously analyzing and reorganizing MSAs through biological reasoni...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 43 |
| 📅 Today | [`2026-11-04.json`](data/daily/2026-11-04.json) | 43 |
| 📆 This Week | [`2026-W44.json`](data/weekly/2026-W44.json) | 111 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 150 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-04 | 43 | [View JSON](data/daily/2026-11-04.json) |
| 📄 2026-11-03 | 38 | [View JSON](data/daily/2026-11-03.json) |
| 📄 2026-11-02 | 30 | [View JSON](data/daily/2026-11-02.json) |
| 📄 2026-11-01 | 39 | [View JSON](data/daily/2026-11-01.json) |
| 📄 2026-10-31 | 39 | [View JSON](data/daily/2026-10-31.json) |
| 📄 2026-10-30 | 30 | [View JSON](data/daily/2026-10-30.json) |
| 📄 2026-10-29 | 9 | [View JSON](data/daily/2026-10-29.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W44 | 111 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 150 | [View JSON](data/monthly/2026-11.json) |
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
