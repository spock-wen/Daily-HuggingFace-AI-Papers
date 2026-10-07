<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-51-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8196+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">51</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">140</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">435</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8196+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 07, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenfeng Feng, Weiqing Li, Guofeng Quan, Bingxi Hou, Nothing2Say

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08448) • [📄 arXiv](https://arxiv.org/abs/2610.08448) • [📥 PDF](https://arxiv.org/pdf/2610.08448)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> In this paper, we examine whether expanding this alignment coverage improves learning. Across three heterogeneous teacher--student pairs on mathematical reasoning and code generation, strict 1:1 groups already cover most student-generated tokens d...

</details>

<details>
<summary><b>2. DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation</b> ⭐ 23</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03543) • [📄 arXiv](https://arxiv.org/abs/2610.03543) • [📥 PDF](https://arxiv.org/pdf/2610.03543)

**💻 Code:** [⭐ Code](https://github.com/JohnZhan2023/DuoMatching) • [⭐ Code](https://github.com/huggingface)

> Hi HF community! I’m one of the authors of DuoMatching, our work on high-quality, real-time video generation with image priors. DuoMatching combines joint distribution matching from a video teacher with direct frame-level supervision from an image...

</details>

<details>
<summary><b>3. TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07767) • [📄 arXiv](https://arxiv.org/abs/2610.07767) • [📥 PDF](https://arxiv.org/pdf/2610.07767)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL meth...

</details>

<details>
<summary><b>4. EVISKILL: Grounding Skill Evolution in Replayable Evidence</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05030) • [📄 arXiv](https://arxiv.org/abs/2610.05030) • [📥 PDF](https://arxiv.org/pdf/2610.05030)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Zhouyaner/Eviskill)

> Continual skill evolution enables LLM agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. Its effectiveness depends on determining not only what to change, but also why a cha...

</details>

<details>
<summary><b>5. From Evidence to Action: How Tool-Using Agents Fail</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07753) • [📄 arXiv](https://arxiv.org/abs/2610.07753) • [📥 PDF](https://arxiv.org/pdf/2610.07753)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/caoshidong66/safeact)

> Tool-using agents can reach the right end state without having established the evidence that justified their actions. We introduce SafeActBench (656 cases, 6 operational domains, 5 protocols from static action judgment to dependency-constrained mu...

</details>

<details>
<summary><b>6. AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05140) • [📄 arXiv](https://arxiv.org/abs/2610.05140) • [📥 PDF](https://arxiv.org/pdf/2610.05140)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Scientific agents usually take the tests. With AutoSciBench, they also help build them. The framework constructs questions, scientific data, and ground-truth answers, then uses solver feedback to revise task designs. Lessons from earlier runs info...

</details>

<details>
<summary><b>7. Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37334) • [📄 arXiv](https://arxiv.org/abs/2609.37334) • [📥 PDF](https://arxiv.org/pdf/2609.37334)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🤖 Robots don’t always move as commanded. We introduce Self Compensating VLA, which learns from this gap during deployment. 🧠 The policy adapts online using the difference between commanded and executed motion. We update small LoRA adapters using p...

</details>

<details>
<summary><b>8. HuatuoGPT-3: RL-Only Domain Adaptation from Base Models</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05966) • [📄 arXiv](https://arxiv.org/abs/2610.05966) • [📥 PDF](https://arxiv.org/pdf/2610.05966)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/FreedomIntelligence/HuatuoGPT-3)

> HuatuoGPT-3 advances the HuatuoGPT line from medical data adaptation to training-paradigm innovation. Instead of following the conventional SFT-then-RL pipeline, it explores RL-only domain adaptation from base models through OnePO, using teacher o...

</details>

<details>
<summary><b>9. World Action Learning via Interaction-Centric Spectral Latent Guidance</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.03607) • [📄 arXiv](https://arxiv.org/abs/2610.03607) • [📥 PDF](https://arxiv.org/pdf/2610.03607)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> How can egocentric human videos effectively benefit robot learning despite camera motion and human–robot execution differences? WING learns interaction-centric latent actions from ego videos and transfers them to robot policies through low-frequen...

</details>

<details>
<summary><b>10. Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.01892) • [📄 arXiv](https://arxiv.org/abs/2610.01892) • [📥 PDF](https://arxiv.org/pdf/2610.01892)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zfy0314/ssr-unofficial)

> Multimodal agents commonly generate free-form reasoning before each action. For small models, limited model capacity can result in lengthy reasoning that provides little useful guidance for action generation while incurring substantial inference c...

</details>

<details>
<summary><b>11. UNREAL: Unifying Retrieval and Long-Context with a Single Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08463) • [📄 arXiv](https://arxiv.org/abs/2610.08463) • [📥 PDF](https://arxiv.org/pdf/2610.08463)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce UNREAL, which uses a single frozen LLM to retrieve evidence and generate answers. It adds fewer than 500K trainable parameters and uses the model’s internal representations to select relevant chunks from long prompts or entire corpora...

</details>

<details>
<summary><b>12. AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Alessandro Rastelli, Giuseppe Santoro, Salvatore Rionero, Giulio Zeloni, enrico-protom

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.01218) • [📄 arXiv](https://arxiv.org/abs/2610.01218) • [📥 PDF](https://arxiv.org/pdf/2610.01218)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most RAG evaluation tools stop at a score. In enterprise engagements we needed a release decision we could defend: promote, manual review, block, or "not evaluable" when the evidence is missing. AGO AI Quality Gate is the evidence-first gate we bu...

</details>

<details>
<summary><b>13. EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenxuan Song, Mingjian Liang, Yifei Deng, Yikai Qin, Jay9999999

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07969) • [📄 arXiv](https://arxiv.org/abs/2610.07969) • [📥 PDF](https://arxiv.org/pdf/2610.07969)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38972) • [📄 arXiv](https://arxiv.org/abs/2609.38972) • [📥 PDF](https://arxiv.org/pdf/2609.38972)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yihuaihong/CIA-minimal-repro)

> Do LLMs actually reason the way their chain-of-thought says they do? We introduce CoT-Interpretability Alignment (CIA), a metric that checks whether the reasoning written in a model's CoT matches the internal strategy detected by interpretability ...

</details>

<details>
<summary><b>15. MiniCorp: The Last Mile of the AI Agent Firm</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05912) • [📄 arXiv](https://arxiv.org/abs/2610.05912) • [📥 PDF](https://arxiv.org/pdf/2610.05912)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The last mile toward enterprise AGI is a company that runs itself. Training and adapting such agents require longitudinal enterprise data, which remain scarce, costly to acquire, and often restricted by privacy constraints. Historical archives are...

</details>

<details>
<summary><b>16. GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.00948) • [📄 arXiv](https://arxiv.org/abs/2610.00948) • [📥 PDF](https://arxiv.org/pdf/2610.00948)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/GaryYang12345/GUI-HARVEST)

> 👋 We’re excited to share GUI-HARVEST , which enables GUI agents to improve automatically by evolving their execution harness while keeping model weights frozen. The idea: learn from what actually happens on screen. GUI-HARVEST compares screenshots...

</details>

<details>
<summary><b>17. NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale</b> ⭐ 2.05k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08430) • [📄 arXiv](https://arxiv.org/abs/2610.08430) • [📥 PDF](https://arxiv.org/pdf/2610.08430)

**💻 Code:** [⭐ Code](https://github.com/NVIDIA-NeMo/RL) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NVIDIA-NeMo/RL/pull/2444)

> I'm excited to share NeMo-DCR, a project I contributed to during my internship at NVIDIA this summer! 📑 Paper: https://arxiv.org/abs/2610.08430 🔄 The Problem: In mega-scale Agentic RL, each policy update on the training cluster must reach the roll...

</details>

<details>
<summary><b>18. SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Baeseong Park, Byeongjun Shin, Juntaek Oh, Kyoungho Jeun, gunho1123

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34117) • [📄 arXiv](https://arxiv.org/abs/2609.34117) • [📥 PDF](https://arxiv.org/pdf/2609.34117)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi HF community! I'm one of the authors of SlimWise, which speeds up MoE serving by pruning experts only during decode. SlimWise runs prefill with the full model and decode with a pruned model that reuses the full-model KV cache. This training-fre...

</details>

<details>
<summary><b>19. Adaptive Latent Capacity for World Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32921) • [📄 arXiv](https://arxiv.org/abs/2609.32921) • [📥 PDF](https://arxiv.org/pdf/2609.32921)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. DiVeR: Decision-Critical Verifier Learning for VLA Test-Time Scaling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04933) • [📄 arXiv](https://arxiv.org/abs/2610.04933) • [📥 PDF](https://arxiv.org/pdf/2610.04933)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DiVeR improves VLA test-time scaling by identifying sparse decision-critical states from action-representation dispersion and focusing verifier learning where action selection matters most.

</details>

<details>
<summary><b>21. Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07510) • [📄 arXiv](https://arxiv.org/abs/2610.07510) • [📥 PDF](https://arxiv.org/pdf/2610.07510)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/uiuc-kang-lab/PersistBD)

> Can benign post-training remove inherited backdoors in LLM agents? We find that supervised fine-tuning weakens backdoors, but subsequent RL often preserves—and sometimes amplifies—the remaining malicious behavior. Our method, PersistBD, increases ...

</details>

<details>
<summary><b>22. Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07641) • [📄 arXiv](https://arxiv.org/abs/2610.07641) • [📥 PDF](https://arxiv.org/pdf/2610.07641)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Tool-augmented speech assistants typically serialize automatic speech recognition, large language model inference, and external tool execution. As a result, tool latency is incurred only after the user has finished speaking and the LLM has identif...

</details>

<details>
<summary><b>23. Accent Analogy Guidance: More Speaker Similarity at Equal Accent in Cross-Lingual Voice Cloning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.29123) • [📄 arXiv](https://arxiv.org/abs/2609.29123) • [📥 PDF](https://arxiv.org/pdf/2609.29123)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yoomee-cho/accent-analogy-guidance)

> In cross-lingual zero-shot TTS, the accent of the reference speaker leaks into the target language. Accent Analogy Guidance (AAG) is a training-free sampler term: it subtracts an accent direction estimated from the model's own predictions for one ...

</details>

<details>
<summary><b>24. Harness-Aware Distillation for Small Language Model Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02858) • [📄 arXiv](https://arxiv.org/abs/2610.02858) • [📥 PDF](https://arxiv.org/pdf/2610.02858)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/moon4sake/harness-aware-distillation)

> Harness-Aware Distillation (HAD) helps small language model agents make better use of their deployment harness. It augments on-policy distillation with action preferences derived by contrasting the same teacher’s actions with and without harness i...

</details>

<details>
<summary><b>25. DistScene: Object-to-Scene Distillation for 3D Scene Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tianyu Liu, Chengcheng Zhou, Ken Deng, Hongyu Yan, Kunming Luo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06960) • [📄 arXiv](https://arxiv.org/abs/2610.06960) • [📥 PDF](https://arxiv.org/pdf/2610.06960)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>26. DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04596) • [📄 arXiv](https://arxiv.org/abs/2610.04596) • [📥 PDF](https://arxiv.org/pdf/2610.04596)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation

</details>

<details>
<summary><b>27. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08773) • [📄 arXiv](https://arxiv.org/abs/2610.08773) • [📥 PDF](https://arxiv.org/pdf/2610.08773)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Sarim-MBZUAI/advsim2real)

> The paper introduces AdvSim2Real, a training framework that makes web agents more capable and resistant to prompt injection by having three components co-evolve in a simulated web environment: a curriculum generates tasks the agent solves about ha...

</details>

<details>
<summary><b>28. Personal-Agent Mediated Recommendation with Cross-Platform User History</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07588) • [📄 arXiv](https://arxiv.org/abs/2610.07588) • [📥 PDF](https://arxiv.org/pdf/2610.07588)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We study how a personal agent can selectively revise a strong platform ranking using cross-platform user history. Personal-Agent Mediated Recommendation: We formalize this new recommendation setting. MediateRec: We introduce a benchmark spanning c...

</details>

<details>
<summary><b>29. ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08779) • [📄 arXiv](https://arxiv.org/abs/2610.08779) • [📥 PDF](https://arxiv.org/pdf/2610.08779)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhouzhenghong-gt/ALIVE-code)

> Make inserted objects “alive”: not merely visible, but part of the video’s world, responding to surrounding actions.

</details>

<details>
<summary><b>30. HiPLEX: Hierarchical Policy Factorization for Full Duplex Speech Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07727) • [📄 arXiv](https://arxiv.org/abs/2610.07727) • [📥 PDF](https://arxiv.org/pdf/2610.07727)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Our method, HiPLEX (Hierarchical policy factorization for full-duPLEX SLMs), factorizes the policy into when to talk and what to talk. Plus, our credit assignment method causally attributes rewards to the correct or incorrect timing and semantic d...

</details>

<details>
<summary><b>31. Learning Discriminative Geometry for Drifting Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04703) • [📄 arXiv](https://arxiv.org/abs/2610.04703) • [📥 PDF](https://arxiv.org/pdf/2610.04703)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/aalto-icl/DiscriminativeGeometryforDrifting)

> We investigate why Drifting Models perform poorly in pixel space but improve substantially with pretrained features. We show that the key lies in the discriminative geometry of the representation, which determines sample weighting in KDE and the r...

</details>

<details>
<summary><b>32. HLA: Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05842) • [📄 arXiv](https://arxiv.org/abs/2610.05842) • [📥 PDF](https://arxiv.org/pdf/2610.05842)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing

</details>

<details>
<summary><b>33. Towards In-Parameter Memory Augmentation for Large Language Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08630) • [📄 arXiv](https://arxiv.org/abs/2610.08630) • [📥 PDF](https://arxiv.org/pdf/2610.08630)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKUST-KnowComp/Awesome-In-Parameter-Memory)

> Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based ...

</details>

<details>
<summary><b>34. Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07785) • [📄 arXiv](https://arxiv.org/abs/2610.07785) • [📥 PDF](https://arxiv.org/pdf/2610.07785)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/attacca-project/attacca)

> .

</details>

<details>
<summary><b>35. Judged Useless, Queried Anyway: Tool-Using Agents Rarely Turn Their Own Evidence Judgments into Stopping Decisions</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06191) • [📄 arXiv](https://arxiv.org/abs/2610.06191) • [📥 PDF](https://arxiv.org/pdf/2610.06191)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bennidict23/judged-useless-queried-anyway)

> We study whether tool-using agents actually act on their own judgments that retrieved evidence is useless. Across seven agents, they recognize failing-source results as useless 97–100% of the time, yet rarely stop querying. An enforced integration...

</details>

<details>
<summary><b>36. Building Rome from a Single Image</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Quentin Herau, Depu Meng, Tianshuo Xu, Fang Li, Jiraphon Yenphraphai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08790) • [📄 arXiv](https://arxiv.org/abs/2610.08790) • [📥 PDF](https://arxiv.org/pdf/2610.08790)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>37. Harness Engineering for Software Engineering via Modular Executable Dev-Primitives</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haohan Wang, Peng Kuang, Xinjie Li, Haibo Jin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07832) • [📄 arXiv](https://arxiv.org/abs/2610.07832) • [📥 PDF](https://arxiv.org/pdf/2610.07832)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> HERMES turns repository components into agent-native Dev-Primitives, enabling localized reasoning, natural-language inter-component communication, and diagnosis-driven revision for long-horizon software engineering.

</details>

<details>
<summary><b>38. Learning to Read the Contextual Tokens in Diffusion Transformers</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06844) • [📄 arXiv](https://arxiv.org/abs/2610.06844) • [📥 PDF](https://arxiv.org/pdf/2610.06844)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is ...

</details>

<details>
<summary><b>39. JLD: Perceptual Distance Through A Jacobian Lens</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Alan C. Bovik, Balu Adsumilli, Shreshth Saini

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05967) • [📄 arXiv](https://arxiv.org/abs/2610.05967) • [📥 PDF](https://arxiv.org/pdf/2610.05967)

**💻 Code:** [⭐ Code](https://github.com/shreshthsaini/jld) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>40. MEND: RL For Flow Models via Proximal Velocity Matching</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05954) • [📄 arXiv](https://arxiv.org/abs/2610.05954) • [📥 PDF](https://arxiv.org/pdf/2610.05954)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/shreshthsaini/MEND-RL)

> New RL approach for better training Diffusion Models

</details>

<details>
<summary><b>41. VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08761) • [📄 arXiv](https://arxiv.org/abs/2610.08761) • [📥 PDF](https://arxiv.org/pdf/2610.08761)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>42. World Models' Last Exam in Physics</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ziming Qin, Xinjie Lin, Yuzhao Peng, Qingle Liu, Mingju Gao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08791) • [📄 arXiv](https://arxiv.org/abs/2610.08791) • [📥 PDF](https://arxiv.org/pdf/2610.08791)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>43. Conditional Trajectory Peaks: Single-Pass Multimodal Policies over Action Chunks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ping Liu, Rongtian Shen, Di Wu, KevinZhangZJU, XuhuaX

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06104) • [📄 arXiv](https://arxiv.org/abs/2610.06104) • [📥 PDF](https://arxiv.org/pdf/2610.06104)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multimodal imitation learning requires diverse executable futures under the same observation and consistent behavior across replanning cycles. We present Conditional Trajectory Peaks (CTP), a single-pass policy framework that jointly predicts comp...

</details>

<details>
<summary><b>44. Execution-Aligned Progressive Noise for Consistent Asynchronous Replanning in Generative Robot Policies</b> ⭐ 0</summary>

<br/>

**👥 Authors:** He Zheng, Ping Liu, Di Wu, KevinZhangZJU, XuhuaX

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06090) • [📄 arXiv](https://arxiv.org/abs/2610.06090) • [📥 PDF](https://arxiv.org/pdf/2610.06090)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Continuous asynchronous replanning is essential for real-time generative robot policies, but independent stochastic initialization can cause mode switching and inconsistent continuation across action chunks. We propose Execution-Aligned Progressiv...

</details>

<details>
<summary><b>45. Toward Real-Time VLAs: Stage-Aware Two-Step Flow Denoising and System-Level Evaluation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Ping Liu, Rongtian Shen, Di Wu, KevinZhangZJU, XuhuaX

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39822) • [📄 arXiv](https://arxiv.org/abs/2609.39822) • [📥 PDF](https://arxiv.org/pdf/2609.39822)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MagiclabRobotics/Inference)

> Vision-language-action (VLA) models face a timing gap between low-rate inference and high-rate robot execution. We characterize this gap through end-to-end latency measurements of model inference and the robot execution chain. Repeated Flow Matchi...

</details>

<details>
<summary><b>46. Magic-W0: A Structured World-Action Foundation Model for Physical Intelligence</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Lingfeng Zhang, Yuan Zhang, Zhenhan Yin, KevinZhangZJU, XuhuaX

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39870) • [📄 arXiv](https://arxiv.org/abs/2609.39870) • [📥 PDF](https://arxiv.org/pdf/2609.39870)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MagiclabRobotics/Magic-W0)

> World-action models (WAMs) augment robot policies with action-conditioned environment dynamics, yet existing approaches largely rely on future observation reconstruction or generic latent prediction and lack structured, control-oriented world repr...

</details>

<details>
<summary><b>47. WildMatch: Weakly Supervised Image Matcher Adaptation for Wildlife Re-Identification</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Bartosz Zieliński, Izabela Wierzbowska, Ekaterina Rostovskaya, Piotr Kubaty, Turhan Can Kargin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07384) • [📄 arXiv](https://arxiv.org/abs/2610.07384) • [📥 PDF](https://arxiv.org/pdf/2610.07384)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/turhancan97/WildMatch)

> Wildlife re-identification depends on matching distinctive local markings, but global-embedding methods can overlook that evidence, while general-purpose image matchers are not adapted to wildlife. The paper asks whether these matchers can be spec...

</details>

<details>
<summary><b>48. DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08048) • [📄 arXiv](https://arxiv.org/abs/2610.08048) • [📥 PDF](https://arxiv.org/pdf/2610.08048)

**💻 Code:** [⭐ Code](https://github.com/illuin-tech/daedalus) • [⭐ Code](https://github.com/huggingface)

> Go read the 🏛️ blog post !

</details>

<details>
<summary><b>49. Source Identification Is Not Fitness Testing: Measuring the Limits of Synthetic-Data Attribution</b> ⭐ 0</summary>

<br/>

**👥 Authors:** jarmstrong001

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.00417) • [📄 arXiv](https://arxiv.org/abs/2610.00417) • [📥 PDF](https://arxiv.org/pdf/2610.00417)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Repeated training on model-generated data can degrade later models, and one response is to use provenance when choosing which generated examples to reuse. This paper tests both halves of that idea on financial-risk text. Generator attribution is 9...

</details>

<details>
<summary><b>50. CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xinyu Zhang, Yun Sing Koh, Hong Jia, Dong Gong, wrecka

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.08777) • [📄 arXiv](https://arxiv.org/abs/2610.08777) • [📥 PDF](https://arxiv.org/pdf/2610.08777)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wrecklong/CtrlCache)

> Hi everyone! We present CtrlCache, a training-free caching method for interactive video world models. Key idea: in interactive generation, the user's controls for a chunk are known before the chunk is denoised. CtrlCache uses them to decide when c...

</details>

<details>
<summary><b>51. ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Noam Koenigstein, Ziv Weiss Haddad, Oren Barkan, Yehonatan Elisha

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04605) • [📄 arXiv](https://arxiv.org/abs/2610.04605) • [📥 PDF](https://arxiv.org/pdf/2610.04605)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 51 |
| 📅 Today | [`2026-10-07.json`](data/daily/2026-10-07.json) | 51 |
| 📆 This Week | [`2026-W40.json`](data/weekly/2026-W40.json) | 140 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 435 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-07 | 51 | [View JSON](data/daily/2026-10-07.json) |
| 📄 2026-10-06 | 48 | [View JSON](data/daily/2026-10-06.json) |
| 📄 2026-10-05 | 41 | [View JSON](data/daily/2026-10-05.json) |
| 📄 2026-10-04 | 84 | [View JSON](data/daily/2026-10-04.json) |
| 📄 2026-10-03 | 84 | [View JSON](data/daily/2026-10-03.json) |
| 📄 2026-10-02 | 66 | [View JSON](data/daily/2026-10-02.json) |
| 📄 2026-10-01 | 61 | [View JSON](data/daily/2026-10-01.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W40 | 140 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 435 | [View JSON](data/monthly/2026-10.json) |
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
