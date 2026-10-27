<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-43-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9283+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">71</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1522</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9283+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 27, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33568) • [📄 arXiv](https://arxiv.org/abs/2610.33568) • [📥 PDF](https://arxiv.org/pdf/2610.33568)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yihaohu0118/Trajectory2Gym)

> Trajectory2Gym is a framework for scaling tool-use agents through compositional coverage and decision-grounded supervision. It constructs executable interactions that capture multi-step dependencies and trains agents on decisions supported by thei...

</details>

<details>
<summary><b>2. StreamVibe: Proactive Video Agents for Evolving User Intent</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34662) • [📄 arXiv](https://arxiv.org/abs/2610.34662) • [📥 PDF](https://arxiv.org/pdf/2610.34662)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Vision-language models are shifting from offline passive understanding toward online proactive interaction. However, prevailing methods largely rely on explicit requests while overlooking implicit user intents (e.g., “where should I click next?” w...

</details>

<details>
<summary><b>3. DynaFlow: Learning Free-Form Multi-Agent Orchestration</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34467) • [📄 arXiv](https://arxiv.org/abs/2610.34467) • [📥 PDF](https://arxiv.org/pdf/2610.34467)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/amiya-special/Dynaflow)

> GitHub: https://github.com/amiya-special/Dynaflow Arxiv: https://arxiv.org/abs/2610.34467 Project Page: https://amiya-special.github.io/DynaFlow-website

</details>

<details>
<summary><b>4. Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32285) • [📄 arXiv](https://arxiv.org/abs/2610.32285) • [📥 PDF](https://arxiv.org/pdf/2610.32285)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TraceLite-AI/TraceTrial-Bench)

> Task success does not always mean the agent harness worked reliably. We introduce TraceTrial-Bench, a benchmark that evaluates agent task performance and harness reliability separately, using 95 mechanism-oriented tasks across seven components: co...

</details>

<details>
<summary><b>5. InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33966) • [📄 arXiv](https://arxiv.org/abs/2610.33966) • [📥 PDF](https://arxiv.org/pdf/2610.33966)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/facebookresearch/InteractiveWorld)

> InteractiveWorld is the first environment that realistically simulates a human and a wearable AI assistant interacting in the physical world: the assistant sees through the human’s eyes and talks, the human decides and acts, and the world responds.

</details>

<details>
<summary><b>6. Work Agents: Systems, Capabilities, and Optimization</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35845) • [📄 arXiv](https://arxiv.org/abs/2610.35845) • [📥 PDF](https://arxiv.org/pdf/2610.35845)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EnjunDu/awesome-working-agent)

> As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how...

</details>

<details>
<summary><b>7. WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Fei Wang, Peng Zhang, Wenhua Liao, Yu Liu, sary11

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33135) • [📄 arXiv](https://arxiv.org/abs/2610.33135) • [📥 PDF](https://arxiv.org/pdf/2610.33135)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PixCtrol/WorldCast)

> No abstract available.

</details>

<details>
<summary><b>8. Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34415) • [📄 arXiv](https://arxiv.org/abs/2610.34415) • [📥 PDF](https://arxiv.org/pdf/2610.34415)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/WJM-George/AMBIT)

> AMBIT is a unified First-Order Ambisonics framework that turns language into executable ScenePlans of source content, activity, and 3D trajectories, and renders them with a shared Transfusion model for both native generation and instruction-guided...

</details>

<details>
<summary><b>9. Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based RL</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33512) • [📄 arXiv](https://arxiv.org/abs/2610.33512) • [📥 PDF](https://arxiv.org/pdf/2610.33512)

**💻 Code:** [⭐ Code](https://github.com/JHKim631/FORK) • [⭐ Code](https://github.com/huggingface)

> Rubric-based rewards enable effective reinforcement learning on non-verifiable tasks. However, because these rewards are typically defined as a weighted measure of rubric coverage, models are trained primarily to maximize a recall objective. As a ...

</details>

<details>
<summary><b>10. Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32195) • [📄 arXiv](https://arxiv.org/abs/2610.32195) • [📥 PDF](https://arxiv.org/pdf/2610.32195)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce PRINCIPIA, an automatic framework for scientific knowledge construction at test time. By observing and interpreting experimental outcomes, PRINCIPIA forms hypotheses, generalizes them into  empirical principles, and revises hypotheses...

</details>

<details>
<summary><b>11. World-in-Context: Interactive Video World Modeling with In-Context Conditioning</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33169) • [📄 arXiv](https://arxiv.org/abs/2610.33169) • [📥 PDF](https://arxiv.org/pdf/2610.33169)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aigc3d/World-in-Context)

> World-in-Context: Interactive Video World Modeling with In-Context Conditioning

</details>

<details>
<summary><b>12. Qwen-Image-PE: Learning Visual Design for Text-to-Image Prompt Enhancement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33472) • [📄 arXiv](https://arxiv.org/abs/2610.33472) • [📥 PDF](https://arxiv.org/pdf/2610.33472)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We train a T2I prompt enhancer for visual design.

</details>

<details>
<summary><b>13. Trustworthy Recursive Self-Improvement in the Era of Large Models: Foundation, Risks, Evaluation and Open Challenges</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tongyu Wen, Qipeng Wang, Jinyi Bai, Ang Gao, Jiayue Pu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35193) • [📄 arXiv](https://arxiv.org/abs/2610.35193) • [📥 PDF](https://arxiv.org/pdf/2610.35193)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AI systems built around large models increasingly use experience and feedback to make persistent changes to models, prompts, memories, tools, and workflows. Recursive self-improvement (RSI) extends this process to inductive biases and to the mecha...

</details>

<details>
<summary><b>14. Δτ-Bench: Pushing Agents Toward a Moving Capability</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34238) • [📄 arXiv](https://arxiv.org/abs/2610.34238) • [📥 PDF](https://arxiv.org/pdf/2610.34238)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zjunlp/delta-tau-bench)

> In this paper, we introduce △τ-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems.

</details>

<details>
<summary><b>15. Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33956) • [📄 arXiv](https://arxiv.org/abs/2610.33956) • [📥 PDF](https://arxiv.org/pdf/2610.33956)

**💻 Code:** [⭐ Code](https://github.com/haoyu-zhao/Continual-Learning-Exam) • [⭐ Code](https://github.com/huggingface)

> 🚀 Introducing Continual Learning Exam (CLE): Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents! 🧠 Can LLM agents truly learn from experience and continuously improve over time? Most existing agent benchmarks focus on whether ag...

</details>

<details>
<summary><b>16. AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33413) • [📄 arXiv](https://arxiv.org/abs/2610.33413) • [📥 PDF](https://arxiv.org/pdf/2610.33413)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AV-FABLE localizes sparse audio and visual manipulations on separate timelines in long-form video; NFSR reads frozen AV-LLM features with separate decoders and leads in-domain and on three OOD settings.

</details>

<details>
<summary><b>17. S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning</b> ⭐ 5.22k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35518) • [📄 arXiv](https://arxiv.org/abs/2610.35518) • [📥 PDF](https://arxiv.org/pdf/2610.35518)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/InternLM/xtuner)

> Critic-free methods are widely used in reinforcement learning with verifiable rewards (RLVR) for long chain-of-thought (CoT) reasoning, avoiding difficult and costly critic training. Common alternatives lack token-level credit assignment and typic...

</details>

<details>
<summary><b>18. EmbodiedLab: Benchmarking Embodied Agents That Act to Know</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35385) • [📄 arXiv](https://arxiv.org/abs/2610.35385) • [📥 PDF](https://arxiv.org/pdf/2610.35385)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HexaFuture/EmbodiedLab)

> Manipulation benchmarks test acting to change; EmbodiedLab tests acting to know. Given only an objective and the apparatus, a robot runs its own experiment in a physics-based lab to find out a result it cannot know in advance. 30 science experimen...

</details>

<details>
<summary><b>19. RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34356) • [📄 arXiv](https://arxiv.org/abs/2610.34356) • [📥 PDF](https://arxiv.org/pdf/2610.34356)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/RynnVLA-Latent) • [⭐ Code](https://github.com/huggingface)

> Our contributions are as follows: 3D-grounded latent-action supervision. We introduce RynnLAM, which combines residual feature prediction, camera-compensated 3D-flow supervision, and camera-motion decoupling to construct continuous transition repr...

</details>

<details>
<summary><b>20. ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18683) • [📄 arXiv](https://arxiv.org/abs/2610.18683) • [📥 PDF](https://arxiv.org/pdf/2610.18683)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LINs-lab/ProAS)

> We argue against the limitations of the traditional GRPO-type credit assignment, such as (1) the unreasonable reinforcement of unreasonable actions within the positively advantaged trajectory,  and (2) the fact that actions within the negatively a...

</details>

<details>
<summary><b>21. miniTE: Diagnosing and Bridging the Execution Gap in Native NVFP4 Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23928) • [📄 arXiv](https://arxiv.org/abs/2610.23928) • [📥 PDF](https://arxiv.org/pdf/2610.23928)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 Can we really train LLMs with native FP4 reinforcement learning — without sacrificing stability? Excited to share miniTE , our open-source framework for stable and efficient native NVFP4 (W4A4) RL! One surprising finding: Same weights + same pre...

</details>

<details>
<summary><b>22. More Memory, Better Videos? A Controlled Study of Visual Memory in Long-Video Generation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Yucheng Wang, Yulong Xu, Xinyu Wang, Huafeng Shi, Yuzhuo Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35001) • [📄 arXiv](https://arxiv.org/abs/2610.35001) • [📥 PDF](https://arxiv.org/pdf/2610.35001)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Suchenl/VMem-Bench)

> Does visual memory always improve generated video? VMem-Bench separates reference selection from generator outcomes. Across real-film and causal-story tracks, retrieval improves entity recall but can reduce precision and forbidden-entity avoidance...

</details>

<details>
<summary><b>23. Rethinking Video Storage for AI Training: Breaking Cross-Frame Dependencies for Efficient Random Access</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33079) • [📄 arXiv](https://arxiv.org/abs/2610.33079) • [📥 PDF](https://arxiv.org/pdf/2610.33079)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kaname-madoka18/codec4AI)

> 🛑 Stop using LeRobot’s default video storage. 🚀 Upgrade your training-data infra with codec4AI! 🏛️ From Academician Wen Gao’s team at Peking University. Video training needs fast random frame access. codec4AI brings sparse decoding and dependency-...

</details>

<details>
<summary><b>24. Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players</b> ⭐ 31</summary>

<br/>

**👥 Authors:** Limin Wang, Rizling

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33845) • [📄 arXiv](https://arxiv.org/abs/2610.33845) • [📥 PDF](https://arxiv.org/pdf/2610.33845)

**💻 Code:** [⭐ Code](https://github.com/MCG-NJU/AutoTavern) • [⭐ Code](https://github.com/huggingface)

> Excited to share our work, Build, Don't Play ! Can LLM agents build better game-playing AI systems than they can directly play? We introduce AutoTavern , a self-improving research system where LLM agents verify game mechanics, build a faithful Hea...

</details>

<details>
<summary><b>25. Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33024) • [📄 arXiv](https://arxiv.org/abs/2610.33024) • [📥 PDF](https://arxiv.org/pdf/2610.33024)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhihaoyang30/skill-adaptation-code)

> No abstract available.

</details>

<details>
<summary><b>26. Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Xinyi Shang, Peng Sun, Xiaohan Zhao, Yaxin Luo, Jiacheng Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31309) • [📄 arXiv](https://arxiv.org/abs/2610.31309) • [📥 PDF](https://arxiv.org/pdf/2610.31309)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VILA-Lab/optic)

> Recent work shows that increasing embedding capacity can improve language models, making it a promising direction for scaling. As more capacity goes into embedding tables, extreme compression becomes increasingly important: we want to keep the ben...

</details>

<details>
<summary><b>27. HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction</b> ⭐ 361</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31635) • [📄 arXiv](https://arxiv.org/abs/2610.31635) • [📥 PDF](https://arxiv.org/pdf/2610.31635)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HiP3Rs/HiP3R)

> Turn long videos into coherent 3D worlds. HiP3R aligns overlapping reconstructions at the chunk level, then refines one shared camera pose per frame. Delivers 3D scenes across thousands of frames.

</details>

<details>
<summary><b>28. Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33503) • [📄 arXiv](https://arxiv.org/abs/2610.33503) • [📥 PDF](https://arxiv.org/pdf/2610.33503)

**💻 Code:** [⭐ Code](https://github.com/AIforIP/PatEx-Gym) • [⭐ Code](https://github.com/huggingface)

> PatEx-Gym introduces the first long-horizon agentic task in the patent domain, requiring agents to autonomously search for prior art, inspect technical evidence, iteratively refine their search strategies, and produce evidence-grounded Office Acti...

</details>

<details>
<summary><b>29. AgentProofBench: Benchmarking Reusable Verifiers for Web Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34634) • [📄 arXiv](https://arxiv.org/abs/2610.34634) • [📥 PDF](https://arxiv.org/pdf/2610.34634)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EthanNing/AgentProofBench)

> Benchmarking Reusable Verifiers for Web Agents

</details>

<details>
<summary><b>30. CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yixin Chen, Ruolin Zuo, Shuwei Jiang, Yintianrun Zhang, j-zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.29915) • [📄 arXiv](https://arxiv.org/abs/2610.29915) • [📥 PDF](https://arxiv.org/pdf/2610.29915)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PKU-VaLuE-Lab/CausalAlign)

> Diffusion-based video generation models (VGMs) can synthesize visually compelling content, but maintaining geometrically consistent camera ego-motion across frames remains an open problem. Camera ego-motion describes these cross-frame viewpoint ch...

</details>

<details>
<summary><b>31. Joint or Per-Option? Compact Encoders for Closed-Set Decisions from 17 Million to 1 Billion Parameters</b> ⭐ 0</summary>

<br/>

**👥 Authors:** tardellirs

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.30970) • [📄 arXiv](https://arxiv.org/abs/2610.30970) • [📥 PDF](https://arxiv.org/pdf/2610.30970)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tardellirs/crivo-decision-encoders)

> Author here. Many LM pipelines end in a closed-set decision: pick a tool, a label, a route. We asked two things: how small an encoder for this can be, and whether it should read the options jointly or one at a time. Per-option vs joint: in a three...

</details>

<details>
<summary><b>32. Mycelium: A Meta-Study of Hallucination Detection Across Provenance, Typology, and Granularities</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Julia Belikova, lmeribal

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33608) • [📄 arXiv](https://arxiv.org/abs/2610.33608) • [📥 PDF](https://arxiv.org/pdf/2610.33608)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lmeribal/mycelium)

> We share our study of hallucination detection benchmarks and evaluation practices. 🍄 Feedback and discussion are very welcome!

</details>

<details>
<summary><b>33. Skill^{infty}: Recursive Self-Improvement for Agent Skill Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35434) • [📄 arXiv](https://arxiv.org/abs/2610.35434) • [📥 PDF](https://arxiv.org/pdf/2610.35434)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> In Skill∞, a meta agent follows a meta-skill to optimize task skills and optimizes the meta-skill itself with the same procedure, so skill optimization becomes recursively self-improving.

</details>

<details>
<summary><b>34. Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yun Zhou, Yawei Wang, Youzhi Luo, Han Ding, Jiongxiao Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.29139) • [📄 arXiv](https://arxiv.org/abs/2610.29139) • [📥 PDF](https://arxiv.org/pdf/2610.29139)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Exploring selective world-model guidance in the agent loop for anticipating and avoiding future failures.

</details>

<details>
<summary><b>35. Constrained Decoding: Harmful or Beneficial? Revisiting Its Impact on LLM Performance</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35328) • [📄 arXiv](https://arxiv.org/abs/2610.35328) • [📥 PDF](https://arxiv.org/pdf/2610.35328)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>36. RoboHarness: A Simple Harness Outperforms VLA and World Action Models</b> ⭐ 265</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14018) • [📄 arXiv](https://arxiv.org/abs/2610.14018) • [📥 PDF](https://arxiv.org/pdf/2610.14018)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/BinceQu/RoboHarness)

> We've open-sourced RoboHarness! Try it with your own coding agent and model, and let us know what you build. On BEHAVIOR Challenge 2025 tasks, RoboHarness + Qwen3.8-Flash-Next outperforms state-of-the-art VLA models. 💻 https://github.com/BinceQu/R...

</details>

<details>
<summary><b>37. Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34654) • [📄 arXiv](https://arxiv.org/abs/2610.34654) • [📥 PDF](https://arxiv.org/pdf/2610.34654)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Language model agents often abandon correct work when a user challenges it, yet simply telling them to stand firm makes them ignore real mistakes. Once an agent reads a complaint, it tends to discount its own earlier checks in order to agree with ...

</details>

<details>
<summary><b>38. Nested Sparsity for Scalable Pretraining and Continual Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.31818) • [📄 arXiv](https://arxiv.org/abs/2610.31818) • [📥 PDF](https://arxiv.org/pdf/2610.31818)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ma-Lab-Berkeley/Nestor)

> Upload the paper.

</details>

<details>
<summary><b>39. Humans in Space: Can MLLMs Construct Human-Centric Spatial Understanding via Active Exocentric Exploration?</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Xin Yu, Ling Chen, Chen Liu, Tengyue Zhang, gtc-hf

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34149) • [📄 arXiv](https://arxiv.org/abs/2610.34149) • [📥 PDF](https://arxiv.org/pdf/2610.34149)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/gtc-gh/SATE-Bench)

> SATE-Bench is an interactive benchmark that evaluates whether MLLMs know when to explore and when they have seen enough: an occluded initial view leaves the model "hungry" for information, and it has to explore the scene to fully "sate" that need.

</details>

<details>
<summary><b>40. DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21561) • [📄 arXiv](https://arxiv.org/abs/2610.21561) • [📥 PDF](https://arxiv.org/pdf/2610.21561)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/idiap/dialfork)

> Ask an LLM agent to check the weather. It's polite, fluent and never says anything false... and twenty turns later you still don't have your forecast. 🌦️ That's procedural hallucination : the agent stops following the procedure it was given. Every...

</details>

<details>
<summary><b>41. Trust Mechanisms for Offline Generative AI at the Edge: A Connectivity-Regime Framework and an Empirical Study on a Raspberry Pi 5</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33732) • [📄 arXiv](https://arxiv.org/abs/2610.33732) • [📥 PDF](https://arxiv.org/pdf/2610.33732)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/securagenai/edge-rag-trust-mechanisms)

> We study what trust mechanisms do, and cost, for a fully local RAG assistant on a Raspberry Pi 5 running under network isolation (Qwen2.5 1.5B/3B/7B, 300 SQuAD 2.0 questions). Key findings: A calibrated retrieval-score gate detects out-of-corpus q...

</details>

<details>
<summary><b>42. Assessing the CAD Capabilities of General-Purpose AI Models: A Case Study of GPT-6 Astra</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24451) • [📄 arXiv](https://arxiv.org/abs/2610.24451) • [📥 PDF](https://arxiv.org/pdf/2610.24451)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can frontier AI models generate CAD models that are actually usable in engineering? Unlike evaluations centered on simplified or toy examples, our study assesses GPT-6 Astra using realistic engineering CAD models with nontrivial complexity. More i...

</details>

<details>
<summary><b>43. Beyond Benchmarks: Can Small Open-Weight Models Get Real Coding Work Done?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** jainofficials

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34241) • [📄 arXiv](https://arxiv.org/abs/2610.34241) • [📥 PDF](https://arxiv.org/pdf/2610.34241)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most coding benchmarks measure whether a model can solve a problem. But what happens when we ask smaller open-weight models to complete real software engineering tasks? In Beyond Benchmarks , I investigate this gap through practical coding workflo...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 43 |
| 📅 Today | [`2026-10-27.json`](data/daily/2026-10-27.json) | 43 |
| 📆 This Week | [`2026-W43.json`](data/weekly/2026-W43.json) | 71 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1522 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-27 | 43 | [View JSON](data/daily/2026-10-27.json) |
| 📄 2026-10-26 | 28 | [View JSON](data/daily/2026-10-26.json) |
| 📄 2026-10-25 | 49 | [View JSON](data/daily/2026-10-25.json) |
| 📄 2026-10-24 | 50 | [View JSON](data/daily/2026-10-24.json) |
| 📄 2026-10-23 | 36 | [View JSON](data/daily/2026-10-23.json) |
| 📄 2026-10-22 | 41 | [View JSON](data/daily/2026-10-22.json) |
| 📄 2026-10-21 | 49 | [View JSON](data/daily/2026-10-21.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W43 | 71 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1522 | [View JSON](data/monthly/2026-10.json) |
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
