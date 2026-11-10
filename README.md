<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-26-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9725+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">26</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">54</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">324</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9725+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 10, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Learning Heterogeneous Tactile Representation for General Dexterous Manipulation</b> ⭐ 66</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12806) • [📄 arXiv](https://arxiv.org/abs/2611.12806) • [📥 PDF](https://arxiv.org/pdf/2611.12806)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Robbyant/lingbot-touch)

> LingBot-Touch: A Foundation Model for Heterogeneous Tactile Representation Learning

</details>

<details>
<summary><b>2. WorldFoundry: Towards Unified Infrastructure for World Intelligence</b> ⭐ 322</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10771) • [📄 arXiv](https://arxiv.org/abs/2611.10771) • [📥 PDF](https://arxiv.org/pdf/2611.10771)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenEnvision/WorldFoundry)

> Visual generative models increasingly blur the line between synthesizing observations and simulating environments. Yet visual plausibility alone does not constitute successful world modeling: compelling outputs may lack persistent state, physical ...

</details>

<details>
<summary><b>3. Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12762) • [📄 arXiv](https://arxiv.org/abs/2611.12762) • [📥 PDF](https://arxiv.org/pdf/2611.12762)

**💻 Code:** [⭐ Code](https://github.com/Alpha-Innovator/Sage-Taiyi) • [⭐ Code](https://github.com/huggingface)

> We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understandin...

</details>

<details>
<summary><b>4. Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12886) • [📄 arXiv](https://arxiv.org/abs/2611.12886) • [📥 PDF](https://arxiv.org/pdf/2611.12886)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EliYuan30/Reframe)

> Reframe learns to acquire useful visual evidence, then use it. Built on Qwen3.5-9B, with no SFT cold start. GD-GRPO makes the observation necessary : grounding rewards on tool actions, plus stochastic removal of the original visual input, so the m...

</details>

<details>
<summary><b>5. Flide: Accelerating Decision Inference with Exact State Forking</b> ⭐ 291</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.42148) • [📄 arXiv](https://arxiv.org/abs/2610.42148) • [📥 PDF](https://arxiv.org/pdf/2610.42148)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OmniJev/Flide)

> Hi everyone! I'm one of the authors of Flide. We built Flide from scratch, an open-source inference engine for Jev-like decision models. The key idea is exact state forking, which allows multiple questions to share computation while preserving exa...

</details>

<details>
<summary><b>6. ReproBridge: Building Reproducibility into ML Research Artifacts</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08452) • [📄 arXiv](https://arxiv.org/abs/2611.08452) • [📥 PDF](https://arxiv.org/pdf/2611.08452)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ReproBridge starts from a simple question: when a coding agent reproduces a paper, how much of its success comes from the released artifacts, and how much from the agent filling in what the paper and code leave implicit? What we built Refined repr...

</details>

<details>
<summary><b>7. SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10329) • [📄 arXiv](https://arxiv.org/abs/2611.10329) • [📥 PDF](https://arxiv.org/pdf/2611.10329)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Siris to test whether LLMs can tell these cases apart, judging from their systems understanding when a limitation invalidates the simulator's recommendation.

</details>

<details>
<summary><b>8. How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Chengliang Chai, Sitong Zhang, Songlin Jiang, Ziting Wang, Benyucong

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.11450) • [📄 arXiv](https://arxiv.org/abs/2611.11450) • [📥 PDF](https://arxiv.org/pdf/2611.11450)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/benyucong/train-inference-mismatch-opd)

> Cheaper rollouts (quantized inference, asynchronous rollouts from older weights) make the rollout engine differ from the model being trained. We measure how much of this training–inference mismatch on-policy distillation (OPD) can absorb, and how ...

</details>

<details>
<summary><b>9. TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02810) • [📄 arXiv](https://arxiv.org/abs/2611.02810) • [📥 PDF](https://arxiv.org/pdf/2611.02810)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yingtaoren/TRIO)

> Can three specialized agents make RAG more accurate than a single powerful reasoning model? 🚀 Introducing TRIO , a multi-agent RAG framework that improves retrieval-augmented reasoning through specialized agent optimization. TRIO jointly coordinat...

</details>

<details>
<summary><b>10. FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08240) • [📄 arXiv](https://arxiv.org/abs/2611.08240) • [📥 PDF](https://arxiv.org/pdf/2611.08240)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EDAPINENUT/fewsteprl-sd35)

> No abstract available.

</details>

<details>
<summary><b>11. AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sinuo Wang, Rui Sun, Beidi Luan, Yikun Li, Qiming Shi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36980) • [📄 arXiv](https://arxiv.org/abs/2610.36980) • [📥 PDF](https://arxiv.org/pdf/2610.36980)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🤖 Can an LLM agent run a vending business for 180 days? Many commercial tasks end when a transaction is completed. Running a business is different: today’s decisions determine tomorrow’s stock availability, costs, and cash position. We introduce A...

</details>

<details>
<summary><b>12. JoVox: Joint Hierarchical Flow Matching for Lightweight Voxel Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10690) • [📄 arXiv](https://arxiv.org/abs/2611.10690) • [📥 PDF](https://arxiv.org/pdf/2611.10690)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yuyujunjun/JoVox)

> JoVox generates voxel structures with one discrete flow matching model that learns all hierarchy levels jointly (4³ → 16³ → 64³), instead of one level at a time. Compared with TRELLIS.2 using the same backbone: 8× training throughput, 1/15 FLOPs p...

</details>

<details>
<summary><b>13. SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08935) • [📄 arXiv](https://arxiv.org/abs/2611.08935) • [📥 PDF](https://arxiv.org/pdf/2611.08935)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Reliable dermatology AI requires access to verifiable evidence distributed across heterogeneous textual and visual sources. However, conventional retrieval-augmented generation (RAG) typically relies on one-shot retrieval from flat corpora, limiti...

</details>

<details>
<summary><b>14. Training Vision Transformers to Focus: Emergence of Spatial Attention Head Specialization</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Youyang Ng, Yu-Chieh Lin, Yuji Nozawa

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.11890) • [📄 arXiv](https://arxiv.org/abs/2611.11890) • [📥 PDF](https://arxiv.org/pdf/2611.11890)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yuji-nozawa/ReFoCo)

> Vision Transformers are powerful AI models for recognizing images. They process images as if they had many "eyes", each capable of looking at different aspects of an image. However, the ways these eyes see an image can be ambiguous or overly simil...

</details>

<details>
<summary><b>15. InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.11558) • [📄 arXiv](https://arxiv.org/abs/2611.11558) • [📥 PDF](https://arxiv.org/pdf/2611.11558)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> In this paper, we propose InfraRSI, a harness for hardware optimization.

</details>

<details>
<summary><b>16. InstantHMR : Real-Time Human Mesh Recovery on Your Phone</b> ⭐ 349</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09195) • [📄 arXiv](https://arxiv.org/abs/2611.09195) • [📥 PDF](https://arxiv.org/pdf/2611.09195)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Naturalpad-studio/InstantHMR)

> Code: https://github.com/Naturalpad-studio/InstantHMR

</details>

<details>
<summary><b>17. Stochastic Deep Supervision for Gallery-Consistent Early-Exit Face Recognition</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.09987) • [📄 arXiv](https://arxiv.org/abs/2611.09987) • [📥 PDF](https://arxiv.org/pdf/2611.09987)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/gurayozgur/SD-ViT)

> No abstract available.

</details>

<details>
<summary><b>18. All Quiet on the Neural Front: Language Models Do Not Report Injected Pain States</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Emilio Ferrara

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10123) • [📄 arXiv](https://arxiv.org/abs/2611.10123) • [📥 PDF](https://arxiv.org/pdf/2611.10123)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can a language model report the pain state it represents? We inject the "pain direction" from The Pain Axis into Llama-3.1-8B, Qwen2.5-7B and Qwen2.5-32B and ask them, in a fresh turn, what changed. They do not name it (Qwen2.5-32B: 0 of 2,880 ste...

</details>

<details>
<summary><b>19. How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12324) • [📄 arXiv](https://arxiv.org/abs/2611.12324) • [📥 PDF](https://arxiv.org/pdf/2611.12324)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/third-intelligence/WARC)

> MechEval measures how fast a world model learns the mechanics of an unseen game, and WARC is a world model that learns them at test time.

</details>

<details>
<summary><b>20. FlyHash for LLM Agent Memory: An Empirical Validation and a New Application</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Chrisogonas O. Odhiambo, pranamhan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.05791) • [📄 arXiv](https://arxiv.org/abs/2611.05791) • [📥 PDF](https://arxiv.org/pdf/2611.05791)

**💻 Code:** [⭐ Code](https://github.com/mohanji/flyhash-agent-memory) • [⭐ Code](https://github.com/huggingface)

> Hi everyone, I'm one of the authors. We tested FlyHash, a fruit-fly-inspired sparse hash, against SimHash for retrieving memories in LLM agents, using matched bit budgets and a labeled benchmark we released (6,000 memories, 150 queries). Main resu...

</details>

<details>
<summary><b>21. PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals</b> ⭐ 215</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.08969) • [📄 arXiv](https://arxiv.org/abs/2611.08969) • [📥 PDF](https://arxiv.org/pdf/2611.08969)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ForeverBlue816/PhysioWave)

> We introduce PhysioWave-T, an efficient biosignal foundation model for EEG, ECG, and surface EMG. Scaling across these signals requires handling diverse recording setups and varying signal quality. Our Dynamic Scale Folding adapts to heterogeneous...

</details>

<details>
<summary><b>22. Longtail-SWE: High-Quality SWE Tasks for Underrepresented Languages</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10304) • [📄 arXiv](https://arxiv.org/abs/2611.10304) • [📥 PDF](https://arxiv.org/pdf/2611.10304)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SWE-rebench/LongTail-SWE)

> LongTail-SWE evaluates coding agents on 202 real-world software engineering tasks across 13 underrepresented programming languages. Each task comes from a GitHub issue and a corresponding pull request, with an executable environment and tests. We ...

</details>

<details>
<summary><b>23. Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.11344) • [📄 arXiv](https://arxiv.org/abs/2611.11344) • [📥 PDF](https://arxiv.org/pdf/2611.11344)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/tmlr-group/Spatial-Harness)

> We introduce Spatial Harness (NeurIPS 2026), which grounds VLM spatial reasoning in executable world states . Given images and a question, a Perceiver combines visual estimates with language constraints to place objects and cameras in a shared coo...

</details>

<details>
<summary><b>24. Horizon-Scalable Q-Learning</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.10987) • [📄 arXiv](https://arxiv.org/abs/2611.10987) • [📥 PDF](https://arxiv.org/pdf/2611.10987)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ryanxhr/hql)

> Learning accurate off-policy state-action value functions (Q-functions) from offline datasets becomes harder as the task horizon grows. One-step temporal-difference (TD) learning bootstraps after every transition, so small per-step errors accumula...

</details>

<details>
<summary><b>25. Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching</b> ⭐ 20</summary>

<br/>

**👥 Authors:** Bálint Molnár, Arijit Khan, Sriom Chakrabarti, dylan-ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2501.08686) • [📄 arXiv](https://arxiv.org/abs/2501.08686) • [📥 PDF](https://arxiv.org/pdf/2501.08686)

**💻 Code:** [⭐ Code](https://github.com/machuangtao/KG-RAG4SM) • [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/machuangtao/kg-rag4sm)

> KG-RAG4SM mitigates hallucinations in LLMs for schema matching by grounding LLMs with retrieved subgraphs from large external KGs with vector-based, graph traversal-based subgraph retrieval, ranking-based subgraph refinement, and a hybrid approach...

</details>

<details>
<summary><b>26. Energy-Tweedie: Score meets Score, Energy meets Energy</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2512.23818) • [📄 arXiv](https://arxiv.org/abs/2512.23818) • [📥 PDF](https://arxiv.org/pdf/2512.23818)

**💻 Code:** [⭐ Code](https://github.com/andleb/et) • [⭐ Code](https://github.com/huggingface)

> We derive the Energy–Tweedie identity: for Gibbs corruption, the score is recovered from the path derivative of a matched kernel scoring rule induced by the noise and evaluated at the denoising posterior, generalizing Tweedie’s formula.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 26 |
| 📅 Today | [`2026-11-10.json`](data/daily/2026-11-10.json) | 26 |
| 📆 This Week | [`2026-W45.json`](data/weekly/2026-W45.json) | 54 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 324 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-10 | 26 | [View JSON](data/daily/2026-11-10.json) |
| 📄 2026-11-09 | 28 | [View JSON](data/daily/2026-11-09.json) |
| 📄 2026-11-08 | 32 | [View JSON](data/daily/2026-11-08.json) |
| 📄 2026-11-07 | 32 | [View JSON](data/daily/2026-11-07.json) |
| 📄 2026-11-06 | 24 | [View JSON](data/daily/2026-11-06.json) |
| 📄 2026-11-05 | 32 | [View JSON](data/daily/2026-11-05.json) |
| 📄 2026-11-04 | 43 | [View JSON](data/daily/2026-11-04.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W45 | 54 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 324 | [View JSON](data/monthly/2026-11.json) |
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
