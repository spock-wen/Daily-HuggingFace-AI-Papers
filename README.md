<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-26-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9890+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">26</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">489</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9890+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** November 16, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Envisioning Agentic Robotics: A New Era of Robotic Systems</b> ⭐ 0</summary>

<br/>

**👥 Authors:** geekyutao, mwxely, visity, littlepure2333, wegg111

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18359) • [📄 arXiv](https://arxiv.org/abs/2611.18359) • [📥 PDF](https://arxiv.org/pdf/2611.18359)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>2. VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.15789) • [📄 arXiv](https://arxiv.org/abs/2611.15789) • [📥 PDF](https://arxiv.org/pdf/2611.15789)

**💻 Code:** [⭐ Code](https://github.com/vibeprevisbench/vibeprevisbench) • [⭐ Code](https://github.com/huggingface)

> awesome work～

</details>

<details>
<summary><b>3. Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent</b> ⭐ 124</summary>

<br/>

**👥 Authors:** Zhihao Yang, Yukun Chen, Qi Deng, Run Luo, iTheresaApocalypse

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18397) • [📄 arXiv](https://arxiv.org/abs/2611.18397) • [📥 PDF](https://arxiv.org/pdf/2611.18397)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RainBowLuoCS/Gamer)

> No abstract available.

</details>

<details>
<summary><b>4. MMFlash: Faster Speculative Decoding for Vision-Language Models</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18482) • [📄 arXiv](https://arxiv.org/abs/2611.18482) • [📥 PDF](https://arxiv.org/pdf/2611.18482)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/fscdc/MMFlash)

> Speculative decoding accelerates generation by letting a lightweight drafter propose tokens for parallel verification by a target model. Diffusion drafters such as DFlash propose an entire token block in a single forward pass, but mainly focus on ...

</details>

<details>
<summary><b>5. Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12901) • [📄 arXiv](https://arxiv.org/abs/2611.12901) • [📥 PDF](https://arxiv.org/pdf/2611.12901)

**💻 Code:** [⭐ Code](https://github.com/mdlm-steprefine/mdlm-steprefine) • [⭐ Code](https://github.com/huggingface)

> • We analyze the relationship between entropy spike steps and hallucinations in multimodal diffusion models from the perspective of uncertainty dynamics across denoising steps. • We propose StepRefine, a plug-and-play decoding approach that mitiga...

</details>

<details>
<summary><b>6. V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yong Suk Choi, Dongjun Kim, kkt94

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17831) • [📄 arXiv](https://arxiv.org/abs/2611.17831) • [📥 PDF](https://arxiv.org/pdf/2611.17831)

**💻 Code:** [⭐ Code](https://github.com/kkt94/Llama-V-JEPA-LM) • [⭐ Code](https://github.com/huggingface)

> We release Llama-V-JEPA-LM, open video-language models that join a frozen V-JEPA 2.1 world-model encoder to Qwen3 / Llama (1B–8B), trained in a single stage with counterfactual supervision: a clip and its transformed copy (reversed, mirrored, re-t...

</details>

<details>
<summary><b>7. MIRIX-2.0: Multi-Agent Memory System</b> ⭐ 3.47k</summary>

<br/>

**👥 Authors:** Yu Wang, Peng Xia, Jiayan Nan, Weizhi Zhang, Wei-Chieh Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.12068) • [📄 arXiv](https://arxiv.org/abs/2611.12068) • [📥 PDF](https://arxiv.org/pdf/2611.12068)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Mirix-AI/MIRIX)

> MIRIX-2.0 is out  🚀 🚀 🚀 one system for both factual and procedural memory. Complete records as the system of record, a provenance hypergraph citing answers back to raw rows, and AutoDream merging duplicates and distilling skills offline, outside t...

</details>

<details>
<summary><b>8. MEM-SQL: Memory-Empowered Text-to-SQL</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18338) • [📄 arXiv](https://arxiv.org/abs/2611.18338) • [📥 PDF](https://arxiv.org/pdf/2611.18338)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most Text-to-SQL benchmarks overlook a common scenario where a new request can reuse parts of an earlier query. For example, this month’s revenue report by region can use the same joins and revenue calculation as last month’s, with only the date r...

</details>

<details>
<summary><b>9. G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jin Zhang, Wenzheng Kong, Yuechun Yu, xiaofengmao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17814) • [📄 arXiv](https://arxiv.org/abs/2611.17814) • [📥 PDF](https://arxiv.org/pdf/2611.17814)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> G-CAST helps deployed agents adapt to evolving user needs, tools, and workflows through reward-guided training, validated reward updates, and cumulative regression checks. Deployed in Alibaba’s 1688 procurement agent, it improves adaptation while ...

</details>

<details>
<summary><b>10. JVT: Just Video Transformer makes pixel-space video diffusion simple</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Hua Geng, ghy0324, ZhouTimeMachine

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18549) • [📄 arXiv](https://arxiv.org/abs/2611.18549) • [📥 PDF](https://arxiv.org/pdf/2611.18549)

**💻 Code:** [⭐ Code](https://github.com/ZhouTimeMachine/JVT) • [⭐ Code](https://github.com/huggingface)

> Direct diffusion modeling of high-dimensional raw video data is challenging, and existing pixel-space methods often rely on specialized architectures. We introduce JVT (Just Video Transformer), a simple large-patch DiT-style Transformer for pixel-...

</details>

<details>
<summary><b>11. Loopback Transformer: Towards a Unified View of Residual Looped Transformers</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.07226) • [📄 arXiv](https://arxiv.org/abs/2611.07226) • [📥 PDF](https://arxiv.org/pdf/2611.07226)

**💻 Code:** [⭐ Code](https://github.com/yancyou/Loopback) • [⭐ Code](https://github.com/huggingface)

> In this paper, we study how residual connections should retain and reuse information when the same Transformer blocks run repeatedly. Inspired by recurrent memory, we develop a unified view of residual connections as memory operating along network...

</details>

<details>
<summary><b>12. Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** learner-subodh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16378) • [📄 arXiv](https://arxiv.org/abs/2611.16378) • [📥 PDF](https://arxiv.org/pdf/2611.16378)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What happens when an AI agent decides to improve itself? More importantly, how do we know whether those improvements are actually making it better? As agents begin modifying their own prompts, memories, tools, and workflows, one question becomes i...

</details>

<details>
<summary><b>13. Aligning AI Teams</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Erik Jones, Jascha Sohl-Dickstein, Morgan Jane Matthews, Siddarth Srinivasan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17820) • [📄 arXiv](https://arxiv.org/abs/2611.17820) • [📥 PDF](https://arxiv.org/pdf/2611.17820)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14504) • [📄 arXiv](https://arxiv.org/abs/2611.14504) • [📥 PDF](https://arxiv.org/pdf/2611.14504)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Bonbon is a vertical foundation model for biology that independently learned the hidden relationships governing molecular interactions, just as LLMs learned math without being explicitly trained on it. Accepted to the NeurIPS 2026 main track as an...

</details>

<details>
<summary><b>15. HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.16439) • [📄 arXiv](https://arxiv.org/abs/2611.16439) • [📥 PDF](https://arxiv.org/pdf/2611.16439)

**💻 Code:** [⭐ Code](https://github.com/robbyant-research/Lingbot-ALOHA) • [⭐ Code](https://github.com/huggingface)

> What if you could teach a mobile robot by walking with it and guiding its grippers by hand? HALO collects demonstrations up to 2.9× faster. The learned policies grasp and steer a chair precisely while staying in motion, pull apart tightly fitted L...

</details>

<details>
<summary><b>16. Mobile AI Factory: Building Specialized Language Models for Your Mobile Device</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.13509) • [📄 arXiv](https://arxiv.org/abs/2611.13509) • [📥 PDF](https://arxiv.org/pdf/2611.13509)

**💻 Code:** [⭐ Code](https://github.com/evanly-gh/SLM_Factory) • [⭐ Code](https://github.com/huggingface)

> In this paper, we ask whether a specialized language model can be built automatically for a given task and a given phone. Mobile AI Factory is an agentic system that fine-tunes and quantizes small language models, and uses real measurements of the...

</details>

<details>
<summary><b>17. eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18529) • [📄 arXiv](https://arxiv.org/abs/2611.18529) • [📥 PDF](https://arxiv.org/pdf/2611.18529)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We take the speaker embeddings from each slot (WeSpeaker ResNet34) and split them using Meta's recently released e-means. For streaming, each chunk reclusters only the most recent 90-second window and allows label corrections only within the last ...

</details>

<details>
<summary><b>18. CANTraj: Recovering Vehicle Trajectories from CAN Signals in Naturalistic Driving</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18442) • [📄 arXiv](https://arxiv.org/abs/2611.18442) • [📥 PDF](https://arxiv.org/pdf/2611.18442)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: Removing GPS from vehicle logs does not protect location privacy: we introduce CANTraj (3,940 naturalistic drives paired with GNSS trajectories) and CANTraj-Bench (1,380 hours, 85,919 km) to benchmark six re-implemented route-inference atta...

</details>

<details>
<summary><b>19. AI Reviews Are Biased Towards the Appendix</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17811) • [📄 arXiv](https://arxiv.org/abs/2611.17811) • [📥 PDF](https://arxiv.org/pdf/2611.17811)

**💻 Code:** [⭐ Code](https://github.com/cincynlp/review_appendix) • [⭐ Code](https://github.com/huggingface)

> Large language models (LLMs) are increasingly used by reviewers to highlight weaknesses during the reviewing process, and their outputs often shape the reviews that humans submit. Prior work studies how LLM reviews align with human ones, yet we kn...

</details>

<details>
<summary><b>20. GH-AWTrace: A Large-Scale Dataset of GitHub Agentic Workflow Execution Logs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.06866) • [📄 arXiv](https://arxiv.org/abs/2611.06866) • [📥 PDF](https://arxiv.org/pdf/2611.06866)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A dataset ( https://huggingface.co/datasets/jaykay9999/GHAWTrace ) containing agent trajectories from real-world agentic workflows in software projects. You can use the dataset to study: single-agent vs. multi-agent memory collaboration & communic...

</details>

<details>
<summary><b>21. Do Underwater Image Quality Metrics Agree with Human Perception? A Benchmark with Human Choices, Simple Edits and Generative Drift</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18429) • [📄 arXiv](https://arxiv.org/abs/2611.18429) • [📥 PDF](https://arxiv.org/pdf/2611.18429)

**💻 Code:** [⭐ Code](https://github.com/TrustUIQA/TrustUIQA) • [⭐ Code](https://github.com/huggingface)

> We test whether 73 no-reference image quality metrics agree with what people prefer on underwater photos. Using four opinion-score sets and our own paired-comparison study (20 raters, 1,920 choices), we find that agreement with human choices is lo...

</details>

<details>
<summary><b>22. JFinBench: A Continuously Refreshable Japanese Financial Benchmark from the Latest Certification Exams</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.18130) • [📄 arXiv](https://arxiv.org/abs/2611.18130) • [📥 PDF](https://arxiv.org/pdf/2611.18130)

**💻 Code:** [⭐ Code](https://github.com/SakanaAI/JFinBench) • [⭐ Code](https://github.com/huggingface)

> JFinBench is a Japanese financial benchmark comprising 321 examples from six certification exams held in 2026. Building benchmarks from public exam PDFs is challenging due to heterogeneous layouts, complex tables and figures, and diverse question ...

</details>

<details>
<summary><b>23. Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xuesong Li, Qingtao Yu, Masato Ishii, Akio Hayakawa, Zhengyang Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.02822) • [📄 arXiv](https://arxiv.org/abs/2611.02822) • [📥 PDF](https://arxiv.org/pdf/2611.02822)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The frame sink trick in autoregressive video diffusion models helps keep long-horizon rollouts consistent, but it also pulls motion toward low-dynamic modes. We find that long-range consistency is carried by a small subset of attention heads, whil...

</details>

<details>
<summary><b>24. WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17955) • [📄 arXiv](https://arxiv.org/abs/2611.17955) • [📥 PDF](https://arxiv.org/pdf/2611.17955)

**💻 Code:** [⭐ Code](https://github.com/McGill-NLP/webarena-pro) • [⭐ Code](https://github.com/huggingface)

> We're releasing WebArena-Pro, a benchmark for web agents covering 20 self-hosted applications across six domains, with 300 human-validated tasks spanning text, vision, audio, and video, and isolated task execution for reproducible, parallel evalua...

</details>

<details>
<summary><b>25. DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.17878) • [📄 arXiv](https://arxiv.org/abs/2611.17878) • [📥 PDF](https://arxiv.org/pdf/2611.17878)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kailaisun/DySENSE)

> Cities account for over two-thirds of the world’s energy and more than 70% of global carbon dioxide emissions. Urban Building Energy Modelling (UBEM) is essential for achieving the 2050 net-zero target and the UN’s Sustainable Development Goals 7 ...

</details>

<details>
<summary><b>26. Continual-ARC: Measuring Skill Acquisition over a Working Lifetime</b> ⭐ 37</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2611.14505) • [📄 arXiv](https://arxiv.org/abs/2611.14505) • [📥 PDF](https://arxiv.org/pdf/2611.14505)

**💻 Code:** [⭐ Code](https://github.com/unifyai/continual-arc) • [⭐ Code](https://github.com/huggingface)

> We built Continual-ARC to see whether agents get better with experience, scoring notes in a harness and updates to the weights on the same scale. ARC tasks recur through a stream of 200 instances, each time with a fresh input, and every demonstrat...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 26 |
| 📅 Today | [`2026-11-16.json`](data/daily/2026-11-16.json) | 26 |
| 📆 This Week | [`2026-W46.json`](data/weekly/2026-W46.json) | 26 |
| 🗓️ This Month | [`2026-11.json`](data/monthly/2026-11.json) | 489 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-11-16 | 26 | [View JSON](data/daily/2026-11-16.json) |
| 📄 2026-11-15 | 34 | [View JSON](data/daily/2026-11-15.json) |
| 📄 2026-11-14 | 34 | [View JSON](data/daily/2026-11-14.json) |
| 📄 2026-11-13 | 24 | [View JSON](data/daily/2026-11-13.json) |
| 📄 2026-11-12 | 18 | [View JSON](data/daily/2026-11-12.json) |
| 📄 2026-11-11 | 29 | [View JSON](data/daily/2026-11-11.json) |
| 📄 2026-11-10 | 26 | [View JSON](data/daily/2026-11-10.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W46 | 26 | [View JSON](data/weekly/2026-W46.json) |
| 📅 2026-W45 | 193 | [View JSON](data/weekly/2026-W45.json) |
| 📅 2026-W44 | 231 | [View JSON](data/weekly/2026-W44.json) |
| 📅 2026-W43 | 228 | [View JSON](data/weekly/2026-W43.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-11 | 489 | [View JSON](data/monthly/2026-11.json) |
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
