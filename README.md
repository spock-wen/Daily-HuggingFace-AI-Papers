<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-35-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5142+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">35</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">97</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">320</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5142+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 10, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. ABot-Earth 0.5: Generative 3D Earth Model</b> ⭐ 83</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09967) • [📄 arXiv](https://arxiv.org/abs/2606.09967) • [📥 PDF](https://arxiv.org/pdf/2606.09967)

**💻 Code:** [⭐ Code](https://github.com/amap-cvlab/ABot-Earth-0.5) • [⭐ Code](https://github.com/huggingface)

> Tech report. ABot-Earth-0.5 is a generative 3D Earth model developed by the Amap CV Lab. The github repo is dedicated to our technical report and academic discourse. It does not contain implementation code. Media: https://www.youtube.com/watch?v=Q...

</details>

<details>
<summary><b>2. Kwai Keye-VL-2.0 Technical Report</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chongling Rao, Chengru Song, Changyi Liu, Bin Wen, Kwai Keye Team

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10651) • [📄 arXiv](https://arxiv.org/abs/2606.10651) • [📥 PDF](https://arxiv.org/pdf/2606.10651)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A good paper!

</details>

<details>
<summary><b>3. Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution</b> ⭐ 48</summary>

<br/>

**👥 Authors:** Pengkun Wang, Tongwen Huang, Shidong Yang, Ziyu Ma, Xucong Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10917) • [📄 arXiv](https://arxiv.org/abs/2606.10917) • [📥 PDF](https://arxiv.org/pdf/2606.10917)

**💻 Code:** [⭐ Code](https://github.com/AMAP-ML/roleagent) • [⭐ Code](https://github.com/huggingface)

> Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution Github: https://github.com/AMAP-ML/roleagent

</details>

<details>
<summary><b>4. SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research</b> ⭐ 28</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09730) • [📄 arXiv](https://arxiv.org/abs/2606.09730) • [📥 PDF](https://arxiv.org/pdf/2606.09730)

**💻 Code:** [⭐ Code](https://github.com/Search-Swarm/SearchSwarm) • [⭐ Code](https://github.com/huggingface)

> Real tasks can grow almost unbounded, yet a model's context is finite. We teach agentic LLMs delegation intelligence: to decompose a long-horizon task, delegate bounded subtasks to its own subagents, and integrate their condensed, evidence-grounde...

</details>

<details>
<summary><b>5. MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.07512) • [📄 arXiv](https://arxiv.org/abs/2606.07512) • [📥 PDF](https://arxiv.org/pdf/2606.07512)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> MemDreamer decouples perception and reasoning of long-video understanding via Hierachical Graph Memory and Agentic retrieval mechanism. This paradigm bypasses context limits and mitigates attention dilution, offering a promising scaling direction ...

</details>

<details>
<summary><b>6. Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05922) • [📄 arXiv](https://arxiv.org/abs/2606.05922) • [📥 PDF](https://arxiv.org/pdf/2606.05922)

**💻 Code:** [⭐ Code](https://github.com/wbopan/retro-harness) • [⭐ Code](https://github.com/huggingface)

> RHO (Retrospective Harness Optimization) improves an LLM agent's harness — its skills, tools, and workflows — using only the agent's own past trajectories, with no ground-truth validation set. It selects a difficulty-diverse coreset of past tasks ...

</details>

<details>
<summary><b>7. Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11025) • [📄 arXiv](https://arxiv.org/abs/2606.11025) • [📥 PDF](https://arxiv.org/pdf/2606.11025)

**💻 Code:** [⭐ Code](https://github.com/Tencent-Hunyuan/UniRL/tree/main/FlowDPPO) • [⭐ Code](https://github.com/huggingface)

> Recent work has demonstrated that online reinforcement learning (RL) can substantially improve the quality and alignment of flow matching models for image and video generation. Methods such as Flow-GRPO and CPS cast the denoising process as a Mark...

</details>

<details>
<summary><b>8. SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning</b> ⭐ 95</summary>

<br/>

**👥 Authors:** Jie Tang, Zhuoyi Yang, Fengjia Guo, Wenhao Yan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10804) • [📄 arXiv](https://arxiv.org/abs/2606.10804) • [📥 PDF](https://arxiv.org/pdf/2606.10804)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zai-org/SCAIL-2)

> SCAIL-2 provides an end-to-end framework for controlled character animation, eliminating reliance on intermediate pose skeletons and introducing the MotionPair-60K dataset for improved motion transfer performance.

</details>

<details>
<summary><b>9. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11176) • [📄 arXiv](https://arxiv.org/abs/2606.11176) • [📥 PDF](https://arxiv.org/pdf/2606.11176)

**💻 Code:** [⭐ Code](https://github.com/QinghongLin/data2story-skill) • [⭐ Code](https://github.com/huggingface)

> Can an AI agent act like an editor, turning raw data into readable, verifiable, multimodal stories? Data2Story brings data analysis, information retrieval, narrative writing, visual design, and fact-checking into one “virtual newsroom.” Every key ...

</details>

<details>
<summary><b>10. WorldOlympiad: Can Your World Model Survive a Triathlon?</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11129) • [📄 arXiv](https://arxiv.org/abs/2606.11129) • [📥 PDF](https://arxiv.org/pdf/2606.11129)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/WorldOlympiad) • [⭐ Code](https://github.com/huggingface)

> We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity. While existing benchmarks often focus on visual quality, semantic alignment, or short-te...

</details>

<details>
<summary><b>11. Rethinking the Divergence Regularization in LLM RL</b> ⭐ 324</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09821) • [📄 arXiv](https://arxiv.org/abs/2606.09821) • [📥 PDF](https://arxiv.org/pdf/2606.09821)

**💻 Code:** [⭐ Code](https://github.com/Tencent-Hunyuan/UniRL) • [⭐ Code](https://github.com/huggingface)

> Divergence Regularized Policy Optimization (DRPO) is our attempt to make mask-based trust regions smoother without losing what makes them effective. Our key insight is that trust-region geometry matters: DPPO-style trust-region geometry works well...

</details>

<details>
<summary><b>12. Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11180) • [📄 arXiv](https://arxiv.org/abs/2606.11180) • [📥 PDF](https://arxiv.org/pdf/2606.11180)

**💻 Code:** [⭐ Code](https://github.com/cvlab-kaist/LipForcing) • [⭐ Code](https://github.com/huggingface)

> https://cvlab-kaist.github.io/LipForcing/

</details>

<details>
<summary><b>13. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11182) • [📄 arXiv](https://arxiv.org/abs/2606.11182) • [📥 PDF](https://arxiv.org/pdf/2606.11182)

**💻 Code:** [⭐ Code](https://github.com/Princeton-AI2-Lab/EEVEE) • [⭐ Code](https://github.com/huggingface)

> EEVEE studies test-time prompt learning for LLM agents in more realistic settings, where tasks arrive as heterogeneous streams from multiple datasets and domains. Instead of optimizing a single prompt for a fixed benchmark, EEVEE introduces a rout...

</details>

<details>
<summary><b>14. One Token per Multimodal Evidence: Latent Memory for Resource-Constrained QA</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10572) • [📄 arXiv](https://arxiv.org/abs/2606.10572) • [📥 PDF](https://arxiv.org/pdf/2606.10572)

**💻 Code:** [⭐ Code](https://github.com/zz1358m/Latent-Memory-Master) • [⭐ Code](https://github.com/huggingface)

> Latent Memory is a novel method for efficient representation and QA generation. It shows that one token per multimodal evidence can lead to a good performance-efficiency trade-off.

</details>

<details>
<summary><b>15. Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic tasks in Real-World Professional Fields</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11042) • [📄 arXiv](https://arxiv.org/abs/2606.11042) • [📥 PDF](https://arxiv.org/pdf/2606.11042)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Recent years have witnessed the rapid evolution of AI agents toward handling increasingly complex, real-world tasks. However, existing benchmarks rarely evaluate whether agents can operate graphical user interfaces to complete long-horizon, high-v...

</details>

<details>
<summary><b>16. Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11052) • [📄 arXiv](https://arxiv.org/abs/2606.11052) • [📥 PDF](https://arxiv.org/pdf/2606.11052)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.04391) • [📄 arXiv](https://arxiv.org/abs/2606.04391) • [📥 PDF](https://arxiv.org/pdf/2606.04391)

**💻 Code:** [⭐ Code](https://github.com/plusnli/skill-dynamic-retrieval) • [⭐ Code](https://github.com/huggingface)

> This paper studies online skill learning for web agents, where agents continually induce reusable skills from previous task trajectories and reuse them for future web tasks. A key motivation is that most prior skill-based web agent methods retriev...

</details>

<details>
<summary><b>18. Interpreting and Steering a Text-to-Speech Language Model with Sparse Autoencoders</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10029) • [📄 arXiv](https://arxiv.org/abs/2606.10029) • [📥 PDF](https://arxiv.org/pdf/2606.10029)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Bringing SAEs to text-to-speech models! Currently, control over TTS models such as CosyVoice3 is limited to prompts or predefined tags. We found that model generations can be precisely edited by steering SAE features. We also analyze these feature...

</details>

<details>
<summary><b>19. How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10646) • [📄 arXiv](https://arxiv.org/abs/2606.10646) • [📥 PDF](https://arxiv.org/pdf/2606.10646)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What if we stopped rewarding every token equally and instead followed the actual "reasoning bloodstream" inside an LLM? FlowTracer tackles one of RL’s messiest blind spots—token-level credit assignment—by turning attention patterns into a directed...

</details>

<details>
<summary><b>20. Bridging the Agent-World Gap: Text World Models for LLM-based Agents</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09032) • [📄 arXiv](https://arxiv.org/abs/2606.09032) • [📥 PDF](https://arxiv.org/pdf/2606.09032)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sustech-nlp/awesome-text-world-models)

> We present a systematic overview of text world models for agent applications, providing insights into narrowing the agent–world gap.

</details>

<details>
<summary><b>21. UniPET: a universal network for high-quality PET image denoising across varied dose reduction factors</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Dan Zhao, Hui Zhang, Haowei Chen, Yang Zhou, Zhiwen Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11131) • [📄 arXiv](https://arxiv.org/abs/2606.11131) • [📥 PDF](https://arxiv.org/pdf/2606.11131)

**💻 Code:** [⭐ Code](https://github.com/Yaziwel/UniPET) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>22. U-TTT: Towards Generalizable PET Image Denoising via Test-Time Training</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Zihua Wang, Hui Zhang, Hao Lu, Jiayin Li, Zhiwen Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11032) • [📄 arXiv](https://arxiv.org/abs/2606.11032) • [📥 PDF](https://arxiv.org/pdf/2606.11032)

**💻 Code:** [⭐ Code](https://github.com/Yaziwel/U-TTT) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>23. MilliVid: Hierarchical Latents for Long-Range Consistency in Video Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vitor Guizilini, Sergey Zakharov, Basile Van Hoorick, David Charatan, Ishaan Preetam Chandratreya

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09056) • [📄 arXiv](https://arxiv.org/abs/2606.09056) • [📥 PDF](https://arxiv.org/pdf/2606.09056)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>24. Struct-Searcher: Agentic Structural Thinking Advances Multimodal Deep Information Seeking</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.07689) • [📄 arXiv](https://arxiv.org/abs/2606.07689) • [📥 PDF](https://arxiv.org/pdf/2606.07689)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Struct-Searcher is a training-free agentic workflow that advances multimodal deep research with structure-aware thinking mechanisms.

</details>

<details>
<summary><b>25. What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05304) • [📄 arXiv](https://arxiv.org/abs/2606.05304) • [📥 PDF](https://arxiv.org/pdf/2606.05304)

**💻 Code:** [⭐ Code](https://github.com/iNLP-Lab/PACT) • [⭐ Code](https://github.com/huggingface)

> Multi-agent systems (MAS) built on large language models are typically organized around roles, pipelines, and turn schedules, while the content that agents pass to one another is often left as unconstrained natural language. However, this free-for...

</details>

<details>
<summary><b>26. Dynamic Linear Attention</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10650) • [📄 arXiv](https://arxiv.org/abs/2606.10650) • [📥 PDF](https://arxiv.org/pdf/2606.10650)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DLA (Dynamic Linear Attention) is a framework for multi-state linear attention that uses information-aware dynamic state merging and capacity-bounded memory modeling to improve long-context LLM scalability.

</details>

<details>
<summary><b>27. BrainSurgery: Reproducible and Reliable Declarative Weight Manipulations for Model Editing and Upcycling</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09707) • [📄 arXiv](https://arxiv.org/abs/2606.09707) • [📥 PDF](https://arxiv.org/pdf/2606.09707)

**💻 Code:** [⭐ Code](https://github.com/schneiderkamplab/brainsurgery) • [⭐ Code](https://github.com/huggingface)

> BrainSurgery is a tool for reliably inspecting and modifying large neural network checkpoints without fragile one-off scripts. It uses declarative YAML plans to perform reproducible tensor transformations, such as reshaping, precision changes, lay...

</details>

<details>
<summary><b>28. PsychoSafe: Eliciting Psychologically-Informed Refusals in Large Language Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09697) • [📄 arXiv](https://arxiv.org/abs/2606.09697) • [📥 PDF](https://arxiv.org/pdf/2606.09697)

**💻 Code:** [⭐ Code](https://github.com/aisilab/psychological-safety) • [⭐ Code](https://github.com/huggingface)

> PsychoSafe is a psychologically informed framework for making LLM refusals more supportive in high-risk situations, such as crises, coercion, or escalating harmful intent. It improved refusal quality substantially over a generic baseline, especial...

</details>

<details>
<summary><b>29. Late-Layer Fusion is Enough: Dual-Path Vision Token Routing for Multimodal Large Language Models under Visual Saturation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jinyang Wu, Siyuan Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09131) • [📄 arXiv](https://arxiv.org/abs/2606.09131) • [📥 PDF](https://arxiv.org/pdf/2606.09131)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>30. Emergent Misalignment Can Be Induced by Sycophancy and Reversed via Alignment Gating</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.09068) • [📄 arXiv](https://arxiv.org/abs/2606.09068) • [📥 PDF](https://arxiv.org/pdf/2606.09068)

**💻 Code:** [⭐ Code](https://github.com/stay1to0/Sycophancy_Emergent_Misalignment_and_Gated_attention_FT) • [⭐ Code](https://github.com/huggingface)

> Prior work has shown that fine-tuning large language models on malicious or incorrect outputs in narrow domains can induce broad misalignment and harmful behavior, a phenomenon known as emergent misalignment. However, efficient methods for reversi...

</details>

<details>
<summary><b>31. ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Feng Li, Xuefeng Hu, Jiacheng Pan, Xiao Wang, Junke Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11188) • [📄 arXiv](https://arxiv.org/abs/2606.11188) • [📥 PDF](https://arxiv.org/pdf/2606.11188)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wdrink/ARM)

> Technical report: a discrete autoregressive model that unifies image generation, editing, and understanding.

</details>

<details>
<summary><b>32. IR3DE: A Linear Router for Large Language Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.06098) • [📄 arXiv](https://arxiv.org/abs/2606.06098) • [📥 PDF](https://arxiv.org/pdf/2606.06098)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/gensyn-ai/IR3DE)

> IR3DE is a lightweight, modular, linear router that accurately matches each prompt to the most appropriate LLM expert.

</details>

<details>
<summary><b>33. When the Chain of Thought Knows Better: Failure Modes in Multi-Turn Reasoning Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Samuele Poppi, Nils Lukas, Sai Kartheek Reddy Kasu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10740) • [📄 arXiv](https://arxiv.org/abs/2606.10740) • [📥 PDF](https://arxiv.org/pdf/2606.10740)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: Standard safety evaluations are missing a massive chunk of how reasoning models actually fail. In this paper, we moved beyond static, single-turn prompts to analyze multi-turn adversarial dialogues across distilled models like DeepSeek-R1-7...

</details>

<details>
<summary><b>34. Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Tobias Springenberg, Qiyang Li, Charles Xu, Andy Peng, Zhiyuan Zhou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.11087) • [📄 arXiv](https://arxiv.org/abs/2606.11087) • [📥 PDF](https://arxiv.org/pdf/2606.11087)

**💻 Code:** [⭐ Code](https://github.com/zhouzypaul/qgf) • [⭐ Code](https://github.com/huggingface)

> QGF (Q-Guided Flow) is a test-time reinforcement learning method that utilizes critic gradients to guide pre-trained flow-based policies toward higher-value actions, enhancing stability and scalability in continuous control.

</details>

<details>
<summary><b>35. BenSyc: Benchmarking Conversational Sycophancy and Human Alignment in LLMs for Bengali Contexts</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.10061) • [📄 arXiv](https://arxiv.org/abs/2606.10061) • [📥 PDF](https://arxiv.org/pdf/2606.10061)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large language models (LLMs) increasingly participate in emotionally sensitive social conversations, where responses may shift from balanced support toward excessive validation or escalatory alignment. Existing sycophancy research primarily focuse...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 35 |
| 📅 Today | [`2026-06-10.json`](data/daily/2026-06-10.json) | 35 |
| 📆 This Week | [`2026-W23.json`](data/weekly/2026-W23.json) | 97 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 320 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-10 | 35 | [View JSON](data/daily/2026-06-10.json) |
| 📄 2026-06-09 | 36 | [View JSON](data/daily/2026-06-09.json) |
| 📄 2026-06-08 | 26 | [View JSON](data/daily/2026-06-08.json) |
| 📄 2026-06-07 | 50 | [View JSON](data/daily/2026-06-07.json) |
| 📄 2026-06-06 | 0 | [View JSON](data/daily/2026-06-06.json) |
| 📄 2026-06-05 | 33 | [View JSON](data/daily/2026-06-05.json) |
| 📄 2026-06-04 | 32 | [View JSON](data/daily/2026-06-04.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W23 | 97 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |
| 📅 2026-W20 | 243 | [View JSON](data/weekly/2026-W20.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 320 | [View JSON](data/monthly/2026-06.json) |
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
