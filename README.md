<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-69-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8578+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">69</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">131</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">817</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8578+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 14, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18356) • [📄 arXiv](https://arxiv.org/abs/2610.18356) • [📥 PDF](https://arxiv.org/pdf/2610.18356)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AMAP-ML/Urbex)

> We introduce Urbex, an agentic vision-language framework for city-scale 3D grounding. Existing methods rank precomputed instance proposals. Urbex instead treats grounding as active spatial search: a VLM agent queries landmarks, zooms into local re...

</details>

<details>
<summary><b>2. Agent-Reflex: Teaching Language Agents to Act Reflectively</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17953) • [📄 arXiv](https://arxiv.org/abs/2610.17953) • [📥 PDF](https://arxiv.org/pdf/2610.17953)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RUC-NLPIR/Agent-Reflex)

> Excited to share our new work! 🥳 🪞 Agent-Reflex: Teaching Language Agents to Act Reflectively Real-world tool environments are noisy: services time out or return errors, and users interrupt to correct the agent. Agents trained in clean environment...

</details>

<details>
<summary><b>3. VideoJev: System One Model for Video Understanding and Interaction</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18615) • [📄 arXiv](https://arxiv.org/abs/2610.18615) • [📥 PDF](https://arxiv.org/pdf/2610.18615)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MCG-NJU/VideoJev)

> 🎬 Introducing VideoJev , a family of 4B and 35B-A3B System One models for video understanding and interaction . VideoJev directly scores temporal intervals and answer choices through a shared head, unifying temporal grounding and multiple-choice v...

</details>

<details>
<summary><b>4. Jeva: System One Models from First Principles</b> ⭐ 18</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18773) • [📄 arXiv](https://arxiv.org/abs/2610.18773) • [📥 PDF](https://arxiv.org/pdf/2610.18773)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LiQiiiii/Jeva)

> Introducing Jeva, a decision-native System One architecture unifying four properties by design: null awareness, permutation invariance, option scalability, and cacheability. Our 4B model supports Choice, Noul, and Score, handles 2,048 candidates, ...

</details>

<details>
<summary><b>5. Vela: User Behavior as Supervision Sparks LLM Intelligence</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14709) • [📄 arXiv](https://arxiv.org/abs/2610.14709) • [📥 PDF](https://arxiv.org/pdf/2610.14709)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AllSpark-Research/Vela)

> Hi HF community! I'm Yang Xiao , the first author of Vela. As LLMs are deployed across more real-world scenarios, they must be able to learn from long-term context, understand users' evolving preferences and intent, and make decisions grounded in ...

</details>

<details>
<summary><b>6. X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16811) • [📄 arXiv](https://arxiv.org/abs/2610.16811) • [📥 PDF](https://arxiv.org/pdf/2610.16811)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> X-Ragent is a post-training framework for chest X-ray reasoning that seeks auxiliary evidence only when needed and admits only valid quantitative measurements. Built on Qwen3-VL-8B, it is initialized with agentic supervised fine-tuning on the 7.7K...

</details>

<details>
<summary><b>7. LeWAM: End-to-End World and Action Modeling with JEPAs</b> ⭐ 228</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.12818) • [📄 arXiv](https://arxiv.org/abs/2610.12818) • [📥 PDF](https://arxiv.org/pdf/2610.12818)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MinghaoFu/lewam)

> JEPAs can 𝐧𝐨𝐰 jointly imagine what happens and what to do next! Meet 𝐋𝐞𝐖𝐀𝐌: A JEPA for the real world with 32.3× faster planning, 19 ms per plan Improves success 28.6% → 89.7% on contact-rich manipulations But also ... 🫶 a WAM for everyone with 17...

</details>

<details>
<summary><b>8. DoSA: Dots Sparse Attention</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13990) • [📄 arXiv](https://arxiv.org/abs/2610.13990) • [📥 PDF](https://arxiv.org/pdf/2610.13990)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/llm-sys/flash-indexer)

> DoSA skips unnecessary indexer scoring while preserving exact Top-K token selection. It uses score bounds to reject candidates early and fully scores only those still eligible. It achieves up to 2.74× Indexer speedup and 1.94× time-to-first-token ...

</details>

<details>
<summary><b>9. Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38847) • [📄 arXiv](https://arxiv.org/abs/2609.38847) • [📥 PDF](https://arxiv.org/pdf/2609.38847)

**💻 Code:** [⭐ Code](https://github.com/Estrellajer/ProRubric) • [⭐ Code](https://github.com/huggingface)

> Can an AI get a better score by giving a worse answer? Surprisingly, yes. Imagine asking whether to call 911—and getting 2,000+ characters of explanation before the model tells you to call. The answer checks plenty of boxes, but misses what matter...

</details>

<details>
<summary><b>10. TPPO: Tracking-Value PPO For Language Model Reasoning</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Zhi Wang, Yun Luo, Jianhao Yan, Chenxi Li, Futing Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16794) • [📄 arXiv](https://arxiv.org/abs/2610.16794) • [📥 PDF](https://arxiv.org/pdf/2610.16794)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LINs-lab/TPPO)

> Relative token-level credit is determined by how value evolves along the trajectory, yet PPO's critic never models it — so we analyze successive prefix values, find a Bayesian decomposition with additive updates in log-odds space, and build TPPO o...

</details>

<details>
<summary><b>11. AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards</b> ⭐ 42</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18860) • [📄 arXiv](https://arxiv.org/abs/2610.18860) • [📥 PDF](https://arxiv.org/pdf/2610.18860)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/microsoft/AesCode)

> Aesthetic code generation with decoupled cross-modal rewards: turning prompts into editable, verifiable HTML/CSS infographics, with image generators as aesthetic guidance.

</details>

<details>
<summary><b>12. Multics: Generative Multi-Player World Model with Hierarchical Communication</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17201) • [📄 arXiv](https://arxiv.org/abs/2610.17201) • [📥 PDF](https://arxiv.org/pdf/2610.17201)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TencentARC/Multics)

> Project page: https://karine-huang.github.io/Multics/ GitHub: https://github.com/TencentARC/Multics

</details>

<details>
<summary><b>13. ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15166) • [📄 arXiv](https://arxiv.org/abs/2610.15166) • [📥 PDF](https://arxiv.org/pdf/2610.15166)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We do not benchmark whether models can reproduce what a world looks like, but whether they can construct an executable world that works. Check our data here: 🤗Data

</details>

<details>
<summary><b>14. UltraBERT: Beyond the Limit of BERT Pre-Training</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jaewoo Kang, Taewhoo Lee, affjljoo3581

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15028) • [📄 arXiv](https://arxiv.org/abs/2610.15028) • [📥 PDF](https://arxiv.org/pdf/2610.15028)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Also please check out our blog ! Collection: dmis-lab/ultrabert UltraBERT-150M : pre-trained encoder, 32K context UltraBERT-380M : pre-trained encoder, 32K context UltraBERT-Embed-150M : ready-to-use embedding model

</details>

<details>
<summary><b>15. Harness^2: Recursive Agent Harnessing for an Open World</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14224) • [📄 arXiv](https://arxiv.org/abs/2610.14224) • [📥 PDF](https://arxiv.org/pdf/2610.14224)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/google-research/harness2)

> TLDR: Harness² brings recursive self-improvement to open-world agents, improving the current task’s execution harness and learning from those edits to improve future harnessing, without ground-truth feedback.

</details>

<details>
<summary><b>16. EviScene: Beyond "Is It AI?" for Agentic Image Factuality Assessment</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jialiang Shen, Yi Han, Zhengbo Zhang, Ruiqi Liu, ZiAnwang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14609) • [📄 arXiv](https://arxiv.org/abs/2610.14609) • [📥 PDF](https://arxiv.org/pdf/2610.14609)

**💻 Code:** [⭐ Code](https://github.com/wangzian828/EVISCENE) • [⭐ Code](https://github.com/huggingface)

> Hi Community! 🔍 We introduce EviScene: an approach where the model is given only an image, without pre-provided textual assertions to verify. The agent autonomously identifies issues and conducts investigations through visual inspection, web searc...

</details>

<details>
<summary><b>17. Learning How to Remember: Memory Modality Selection for GUI Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17928) • [📄 arXiv](https://arxiv.org/abs/2610.17928) • [📥 PDF](https://arxiv.org/pdf/2610.17928)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dmis-lab/SwitchMem)

> We explore a simple question: Should GUI agents always represent retrieved memories in the same modality? Our key finding is that memory modality preference varies across interaction steps. Building on this observation, we introduce SwitchMem, whi...

</details>

<details>
<summary><b>18. SALD: Self-Referenced Advantage Learning for Diffusion Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.01496) • [📄 arXiv](https://arxiv.org/abs/2610.01496) • [📥 PDF](https://arxiv.org/pdf/2610.01496)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The proposed Advantage-Guided Diffusion (AGD), Temporal Advantage Memory (TAM), and Spectral Advantage Decomposition (SAD) show strong potential to improve Diffusion Image generation. Code will be released soon....

</details>

<details>
<summary><b>19. VEDJE: Video-Efficient Discriminative Joint Encoder for Scalable Video-Text Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.11850) • [📄 arXiv](https://arxiv.org/abs/2610.11850) • [📥 PDF](https://arxiv.org/pdf/2610.11850)

**💻 Code:** [⭐ Code](https://github.com/GabrieleSerussi/vedje) • [⭐ Code](https://github.com/huggingface)

> 🚀 Can we get the accuracy of a 7.6B-parameter video-language model using a much smaller retrieval system? Introducing VEDJE : efficient video-text retrieval with compact, reusable video representations. Rather than repeatedly processing full video...

</details>

<details>
<summary><b>20. Self-Distillation with Verbal Regularization</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16354) • [📄 arXiv](https://arxiv.org/abs/2610.16354) • [📥 PDF](https://arxiv.org/pdf/2610.16354)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lijiazheng99/VRSD)

> On-policy self-distillation (OPSD) builds a teacher from the model itself by giving it privileged information (PI) the student can't see. We find PI often pushes the teacher toward shortcut answers, suppressing re-checking tokens like "Wait" and "...

</details>

<details>
<summary><b>21. DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17666) • [📄 arXiv](https://arxiv.org/abs/2610.17666) • [📥 PDF](https://arxiv.org/pdf/2610.17666)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Xuyan923r/DeltaTTG)

> Reinforcement learning with verifiable rewards (RLVR) for multi-turn agents relies on sparse terminal rewards that say little about individual steps. Within-group step comparisons depend on reliable state matching and sufficiently diverse sampled ...

</details>

<details>
<summary><b>22. GreenWAM: A World Foundation Model for Robotics</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18774) • [📄 arXiv](https://arxiv.org/abs/2610.18774) • [📥 PDF](https://arxiv.org/pdf/2610.18774)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/greenvla/GreenWAM)

> GreenWAM is a world foundation model for robotics: one model that serves as both an action-conditioned world model and a policy across 20 robot families, from bimanual arms to dexterous humanoids. Highlights: World model: top-tier trajectory, dept...

</details>

<details>
<summary><b>23. Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15782) • [📄 arXiv](https://arxiv.org/abs/2610.15782) • [📥 PDF](https://arxiv.org/pdf/2610.15782)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenGVLab/RSI-Nav)

> RSI-Nav is a recursive self-improvement framework for continuous vision-language navigation, built on Qwen3.5-9B. It improves instruction following and generation through iterative instruction generation, navigation verification, and joint trainin...

</details>

<details>
<summary><b>24. Open-o3-Video-v2: Seek, Ground, and Reason with Verifiable Spatio-Temporal Evidence</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17656) • [📄 arXiv](https://arxiv.org/abs/2610.17656) • [📥 PDF](https://arxiv.org/pdf/2610.17656)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Multimedia-Semantic-Analytics-Lab/Open-o3-Video-v2)

> Extension of Open-o3-Video (ICML26: https://marinero4972.github.io/projects/Open-o3-Video/ )

</details>

<details>
<summary><b>25. A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented Software Evolution</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15765) • [📄 arXiv](https://arxiv.org/abs/2610.15765) • [📥 PDF](https://arxiv.org/pdf/2610.15765)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/co-evolve-lab/ANIS)

> What if the bottleneck isn’t the agent—but the interface? In A Decade in a Day , we explore a complementary path to better software agents: redesigning the interfaces they use. We introduce ANIS , a framework that automatically synthesizes agent-f...

</details>

<details>
<summary><b>26. EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18872) • [📄 arXiv](https://arxiv.org/abs/2610.18872) • [📥 PDF](https://arxiv.org/pdf/2610.18872)

**💻 Code:** [⭐ Code](https://github.com/InternRobotics/EgoExplorer) • [⭐ Code](https://github.com/huggingface)

> EgoExplorer records human loco-manipulation in situ, where walking and manipulating are one behaviour, with a wearable rig (5 VIVE trackers + head-coupled GoPro + MANUS/Wuji gloves) that needs no instrumentation in the room. 🎥 Egocentric video · 🧍...

</details>

<details>
<summary><b>27. CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16577) • [📄 arXiv](https://arxiv.org/abs/2610.16577) • [📥 PDF](https://arxiv.org/pdf/2610.16577)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Unc1eW4ng/CineRecon)

> Hi everyone! We introduce CineRecon , a benchmark for evaluating how well coding agents reconstruct dynamic reference videos as editable Blender scenes. CineRecon contains 50 reference videos and 360 evaluation clips , spanning film, games, and re...

</details>

<details>
<summary><b>28. ClawLoop: Self-Improving Agents via Harness-Native Training Loop</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14118) • [📄 arXiv](https://arxiv.org/abs/2610.14118) • [📥 PDF](https://arxiv.org/pdf/2610.14118)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A self-improving agent running inside Claw-like harness for its own performance on general-purpose tasks

</details>

<details>
<summary><b>29. Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18871) • [📄 arXiv](https://arxiv.org/abs/2610.18871) • [📥 PDF](https://arxiv.org/pdf/2610.18871)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training mee...

</details>

<details>
<summary><b>30. FlashVSR+: Efficient Video Super-Resolution via Hybrid Attention and Reward-Yield Distribution Matching</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17552) • [📄 arXiv](https://arxiv.org/abs/2610.17552) • [📥 PDF](https://arxiv.org/pdf/2610.17552)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenImagingLab/FlashVSR_Plus)

> Hi, We are excited to release FlashVSR+, an efficient one-step diffusion framework for high-quality video super-resolution.

</details>

<details>
<summary><b>31. WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Ru Ying, Zhongshan Liu, Ke Wang, Anqiong Ji, KiyotakaWang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18568) • [📄 arXiv](https://arxiv.org/abs/2610.18568) • [📥 PDF](https://arxiv.org/pdf/2610.18568)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AutoLab-SAI-SJTU/WAVE-0)

> Project page: https://hmwang2002.github.io/release/wave0/ GitHub repo: https://github.com/AutoLab-SAI-SJTU/WAVE-0

</details>

<details>
<summary><b>32. ReTerm: Recovery Training for Self-Improving Terminal Agents</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Xiangyu Yue, Shiming Fu, Kaituo Feng, liuyong9975, twothsnd

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18484) • [📄 arXiv](https://arxiv.org/abs/2610.18484) • [📥 PDF](https://arxiv.org/pdf/2610.18484)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/twothsnd/ReTerm)

> Code: https://github.com/twothsnd/ReTerm Data: https://huggingface.co/datasets/twothsnd/ReTerm-10K

</details>

<details>
<summary><b>33. Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kai-Wei Chang, Nanyun Peng, Krishna Kumar Singh, Shraman Pramanick, Wenbo Hu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18868) • [📄 arXiv](https://arxiv.org/abs/2610.18868) • [📥 PDF](https://arxiv.org/pdf/2610.18868)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> How to scale long-horizon agentic RL envs? 🤔 🌍 We introduce Tev-Gym: 1,170 envs with dense progress rewards. Trained on it: 🔥 Tev-27B matches GPT-6 Astra & Claude Opus 5 on ALE-CM (Pass@5) 🚀 Tev-320B tops open models on Terminal-Bench 4.0-CM

</details>

<details>
<summary><b>34. GeoFix: Geometry Fixing for 4D Consistent Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sunghwan Hong, Jeongjae Lee, Dohun Lee, Hyojun Go, Yeobin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14293) • [📄 arXiv](https://arxiv.org/abs/2610.14293) • [📥 PDF](https://arxiv.org/pdf/2610.14293)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce GeoFix, a framework that aligns videos for geometric consistency and visual quality in 4D generation using a single depth consistency reward calibrated for camera overlap, both during training and inference-time alignment. Project pag...

</details>

<details>
<summary><b>35. WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18067) • [📄 arXiv](https://arxiv.org/abs/2610.18067) • [📥 PDF](https://arxiv.org/pdf/2610.18067)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce WorkRover, a framework for scaling long-horizon cowork-agent training through recursive environment evolution. • Jointly builds and validates aligned work contexts, executable tasks, and evidence-grounded verifiers. • Factorial Compat...

</details>

<details>
<summary><b>36. PhyProbe: Rethinking Physical Consistency Evaluation in Generated Videos</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38377) • [📄 arXiv](https://arxiv.org/abs/2609.38377) • [📥 PDF](https://arxiv.org/pdf/2609.38377)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/vinesmsuic/PhyProbe)

> pip install phyprobe PhyProbe scores how severely a generated video violates physical consistency. It extracts features with a frozen spatiotemporal encoder (PE-Core-G14-448) and maps them to a single score with a lightweight (~1M-parameter) head....

</details>

<details>
<summary><b>37. AReA: Adaptive Receptive-Field Attention for Efficient High-Resolution Diffusion Transformers</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17227) • [📄 arXiv](https://arxiv.org/abs/2610.17227) • [📥 PDF](https://arxiv.org/pdf/2610.17227)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/KooroshRH/AReA)

> TL;DR: AReA is a training-free attention method that lets existing Diffusion Transformers (FLUX.1, Qwen-Image, FLUX.2, Ideogram 4) generate images well above their training resolution, up to about 67 megapixels, while running faster than full atte...

</details>

<details>
<summary><b>38. WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18846) • [📄 arXiv](https://arxiv.org/abs/2610.18846) • [📥 PDF](https://arxiv.org/pdf/2610.18846)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kszpxxzmc/WorldRecon)

> 🌐 Project: https://kszpxxzmc.github.io/WorldRecon-website/ 📄 Paper: https://arxiv.org/abs/2610.18846 💻 Code: https://github.com/kszpxxzmc/WorldRecon

</details>

<details>
<summary><b>39. Fish Audio Drama 3 Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18010) • [📄 arXiv](https://arxiv.org/abs/2610.18010) • [📥 PDF](https://arxiv.org/pdf/2610.18010)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/fishaudio/fish-speech) • [⭐ Code](https://github.com/sgl-project/sglang-omni)

> We introduce Fish Audio Drama 3, an open-source speech generation model that turns text into directed performances, built on a 35B-parameter mixture-of-experts backbone that activates 3B parameters per token. It clones voices from multiple referen...

</details>

<details>
<summary><b>40. JevGPT: Thinking Fast and Slow in Autonomous Research</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Firas Laakom, Nanbo Li, Yimeng Chen, Yanning Dai, SlowWorker

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18272) • [📄 arXiv](https://arxiv.org/abs/2610.18272) • [📥 PDF](https://arxiv.org/pdf/2610.18272)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sunyasheng/JevGPT)

> No abstract available.

</details>

<details>
<summary><b>41. Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16118) • [📄 arXiv](https://arxiv.org/abs/2610.16118) • [📥 PDF](https://arxiv.org/pdf/2610.16118)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZelD0n/framepack-U)

> webpage: https://zeld0n.github.io/framepack-U/ code: https://github.com/ZelD0n/framepack-U huggingface: https://huggingface.co/datasets/ZelD0n/FramePack-U modelscope: https://www.modelscope.cn/datasets/ZelD0n/FramePack-U

</details>

<details>
<summary><b>42. AutoEnvScaling: Automating the Data Flywheel with Terminal Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14163) • [📄 arXiv](https://arxiv.org/abs/2610.14163) • [📥 PDF](https://arxiv.org/pdf/2610.14163)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MSR-Orchard/AutoEnvScaling)

> Recursive self-improvement needs agents that can build their own training environments. But researchers still sit in the loop, limiting it to scale. We introduce AutoEnvScaling, which turns env design into a terminal task: a proposer agent builds ...

</details>

<details>
<summary><b>43. PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Kartik Sharma, Chenda Duan, M. Efe Lorasdagi, Shreyas Rajesh, M. Yigit Turali

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15208) • [📄 arXiv](https://arxiv.org/abs/2610.15208) • [📥 PDF](https://arxiv.org/pdf/2610.15208)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Deep research requires connecting multiple steps of search, reasoning, and computation, with intermediate findings guiding what to investigate next. As investigations grow, agents must maintain research state across model calls and check findings ...

</details>

<details>
<summary><b>44. LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18092) • [📄 arXiv](https://arxiv.org/abs/2610.18092) • [📥 PDF](https://arxiv.org/pdf/2610.18092)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Technical Report

</details>

<details>
<summary><b>45. Latent World Action Model for GUI Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14228) • [📄 arXiv](https://arxiv.org/abs/2610.14228) • [📥 PDF](https://arxiv.org/pdf/2610.14228)

**💻 Code:** [⭐ Code](https://github.com/sjyu001/latent2world) • [⭐ Code](https://github.com/huggingface)

> TL;DR: Do GUI agents really need to reconstruct future screenshots to make better decisions? We introduce a Latent World Action Model that jointly learns action selection and action-conditioned future prediction directly in latent space, without e...

</details>

<details>
<summary><b>46. Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18766) • [📄 arXiv](https://arxiv.org/abs/2610.18766) • [📥 PDF](https://arxiv.org/pdf/2610.18766)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Rubric-based reward models (RMs) evaluate responses against explicit criteria. However, existing methods often derive criteria from observed response candidates, introducing response-induced bias that may limit rubric generalizability. Their judge...

</details>

<details>
<summary><b>47. Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16533) • [📄 arXiv](https://arxiv.org/abs/2610.16533) • [📥 PDF](https://arxiv.org/pdf/2610.16533)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We observe a fundamental difference between RLVR and SFT: RLVR gradients progressively concentrate in a low-dimensional subspace, revealing a unique optimization geometry. Building on this insight, we propose Ares, an adaptive-rank optimizer that ...

</details>

<details>
<summary><b>48. LongR: Unleashing Long-Context Reasoning via Reinforcement Learning with Dense Utility Rewards</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.05758) • [📄 arXiv](https://arxiv.org/abs/2602.05758) • [📥 PDF](https://arxiv.org/pdf/2602.05758)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🧠 Long context ≠ effective reasoning. We introduce LongR , an RL framework that teaches LLMs to “Think-and-Read” —interleaving reasoning with document consultation, guided by more than just final-answer correctness. Our key idea is a dense context...

</details>

<details>
<summary><b>49. HexaBee-4B: Six-Language Translation with Multilingual Answering and Bidirectional Supervision</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mohammad Badzohreh, Mohammadmostafa Rostamkhani, Iman998

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16361) • [📄 arXiv](https://arxiv.org/abs/2610.16361) • [📥 PDF](https://arxiv.org/pdf/2610.16361)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Iman998/HexaBee-4B)

> No abstract available.

</details>

<details>
<summary><b>50. Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15788) • [📄 arXiv](https://arxiv.org/abs/2610.15788) • [📥 PDF](https://arxiv.org/pdf/2610.15788)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lululu896/Agent-Sociodrama)

> .

</details>

<details>
<summary><b>51. RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15772) • [📄 arXiv](https://arxiv.org/abs/2610.15772) • [📥 PDF](https://arxiv.org/pdf/2610.15772)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zfkarl/RSIPO)

> RSIPO is a self-evolving agentic RL framework that enables skill-policy co-evolution and trust-calibrated self-distillation.

</details>

<details>
<summary><b>52. SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18206) • [📄 arXiv](https://arxiv.org/abs/2610.18206) • [📥 PDF](https://arxiv.org/pdf/2610.18206)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dxlong2000/SWE-Misbehavior)

> The paper finds that coding agents frequently violate task boundaries even when they appear to complete the requested task: they act without reading necessary dependencies, modify unrelated code or files, and make unnecessary system changes. These...

</details>

<details>
<summary><b>53. VIEWCRAFT: Evolving What Multimodal Agents See and How They Read It</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Weihua Du, Bocheng Zou, Ruichuan An, Binxiao Xu, hhua2

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15915) • [📄 arXiv](https://arxiv.org/abs/2610.15915) • [📥 PDF](https://arxiv.org/pdf/2610.15915)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Little-Fridge/ViewCraft)

> Reusable skills improve multimodal agents without updating model weights, but their effectiveness depends on both the evidence presented and the procedure used to read it. We introduce ViewCraft, which jointly evolves an executable evidence interf...

</details>

<details>
<summary><b>54. Diffusion Editing with Soft Mask: Pixel Level Redo of Image and Video with Adjustable Strength</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.00359) • [📄 arXiv](https://arxiv.org/abs/2610.00359) • [📥 PDF](https://arxiv.org/pdf/2610.00359)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🎨🎨🎨 Introduces a soft-mask guided diffusion editing framework that enables pixel-level, fine-grained control over the balance between content preservation and regeneration for image and video editing, without requiring retraining 🎨🎨🎨

</details>

<details>
<summary><b>55. UniForge3D: Joint 3D Reconstruction and Generation in a Shared Anchor-Guided Space</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15357) • [📄 arXiv](https://arxiv.org/abs/2610.15357) • [📥 PDF](https://arxiv.org/pdf/2610.15357)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/xibushu/UniForge3D)

> No abstract available.

</details>

<details>
<summary><b>56. PsyBer-Agent: A Psychology-Driven User Agent for Recommender Systems</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13989) • [📄 arXiv](https://arxiv.org/abs/2610.13989) • [📥 PDF](https://arxiv.org/pdf/2610.13989)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/franz-chang/PsyBer-Agent)

> Evaluating recommender systems before deployment requires simulators that remain realistic over long, closed-loop interaction cycles. Current LLM-based agents generally function as surface imitators that generate realistic short-term responses but...

</details>

<details>
<summary><b>57. DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Liang Chen, leoluo25933

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18862) • [📄 arXiv](https://arxiv.org/abs/2610.18862) • [📥 PDF](https://arxiv.org/pdf/2610.18862)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/leoluolol/DoubtLess)

> Reasoning models often reach the answer early and then repeat checks they have already made. DoubtLess shortens this at decoding time, with no training. A small reasoning model reads the CoT twice, once prompted to be brief and once prompted to be...

</details>

<details>
<summary><b>58. CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15327) • [📄 arXiv](https://arxiv.org/abs/2610.15327) • [📥 PDF](https://arxiv.org/pdf/2610.15327)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MENGZHEGENG/Audio-to-Video)

> Excellent work on audio-to-video generation

</details>

<details>
<summary><b>59. Controlled Acquisition and Abstention in Three-Channel Score Conflicts</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10808) • [📄 arXiv](https://arxiv.org/abs/2610.10808) • [📥 PDF](https://arxiv.org/pdf/2610.10808)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MENGZHEGENG/audio-video-text-conflicts)

> First paper deal with multimodal information conflict.

</details>

<details>
<summary><b>60. EventLens: Event-Structure Reinforcement Learning for Video Understanding</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaokun Liu, Ziheng Wang, Zihao Yue, Boshen Xu, Lostgreen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16172) • [📄 arXiv](https://arxiv.org/abs/2610.16172) • [📥 PDF](https://arxiv.org/pdf/2610.16172)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share EventLens (NeurIPS 2026) ! 🚀 Can video MLLMs truly understand how events unfold over time? We introduce Event-Structure Reinforcement Learning , a vision-centric framework that learns temporal structure through verifiable rewards ...

</details>

<details>
<summary><b>61. SHELDON: Reasoning through Dual Search over Hypothesis and Observation Spaces</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18025) • [📄 arXiv](https://arxiv.org/abs/2610.18025) • [📥 PDF](https://arxiv.org/pdf/2610.18025)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/stanford-oval/sheldon)

> Sheldon explores hypothesis and observation space jointly to find unknown observations that lead to new and novel hypotheses

</details>

<details>
<summary><b>62. LightVAE: Towards Compact and Efficient Video Autoencoders</b> ⭐ 15</summary>

<br/>

**👥 Authors:** Ruihao Gong, Fengjun Zhong, Yang Yong, Shiqiao Gu, mack-williams

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14726) • [📄 arXiv](https://arxiv.org/abs/2610.14726) • [📥 PDF](https://arxiv.org/pdf/2610.14726)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ModelTC/LightVAE)

> We present LightVAE, a compression framework for pretrained video VAEs. Our key observation is that spatial aggregation and temporal correction in causal 3D convolutions respond differently to compression. LightVAE keeps the spatial component dens...

</details>

<details>
<summary><b>63. Probable but Not Valid: A Psychometric Audit of Decision Models as Synthetic Survey Respondents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Viktorija Šarkauskaitė, Mantas Lukauskas

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14912) • [📄 arXiv](https://arxiv.org/abs/2610.14912) • [📥 PDF](https://arxiv.org/pdf/2610.14912)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can AI models really replace human survey respondents? We evaluated 47 generative LLMs and 14 decision models against real human survey data, looking beyond plausible answers to psychometric validity. A few interesting findings: Newer doesn't mean...

</details>

<details>
<summary><b>64. Web$hell: A Unified Interface for Agentic Web Access</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13416) • [📄 arXiv](https://arxiv.org/abs/2610.13416) • [📥 PDF](https://arxiv.org/pdf/2610.13416)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present Web$hell, an interface that unifies web access under a single access model.

</details>

<details>
<summary><b>65. CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04851) • [📄 arXiv](https://arxiv.org/abs/2610.04851) • [📥 PDF](https://arxiv.org/pdf/2610.04851)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ft2023/CURIO)

> CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery Test-time RL lets an LLM actually learn from its own attempts on a discovery problem, but reward-only updates tend to collapse onto early high-reward trajectories and kill off dir...

</details>

<details>
<summary><b>66. ShellElastic: Scalable Elastic Pretraining with Simultaneous Maximal Updates and Hyperparameter Transfer</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Mingze Xu, Chongjian Ge, Yifan Gong, Yan Kang, Can111

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15124) • [📄 arXiv](https://arxiv.org/abs/2610.15124) • [📥 PDF](https://arxiv.org/pdf/2610.15124)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jincan333/ShellElastic)

> Foundation models need to support diverse inference budgets, yet training a separate model for each budget duplicates pretraining effort. Elastic models train several nested sub-networks inside one weight-shared supernet, but existing recipes face...

</details>

<details>
<summary><b>67. Beyond Prompt Count: How Data Shapes Transfer in On-Policy Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37377) • [📄 arXiv](https://arxiv.org/abs/2609.37377) • [📥 PDF](https://arxiv.org/pdf/2609.37377)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/wyy-1112/dissecting-opd)

> We study how prompt count, source, and selection shape transfer in on-policy distillation (OPD). One motivating result: using “What is 1+1?” as the only training prompt raises Qwen3-4B’s math score from 15.47% to 47.93%, close to the teacher’s 48....

</details>

<details>
<summary><b>68. 4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17625) • [📄 arXiv](https://arxiv.org/abs/2610.17625) • [📥 PDF](https://arxiv.org/pdf/2610.17625)

**💻 Code:** [⭐ Code](https://github.com/ZGCA-HMI-Lab/4LC) • [⭐ Code](https://github.com/huggingface)

> 4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling Video world models repeatedly reuse past observations, but dynamic memories such as 4DGS re-render RGB and re-encode it into conditions for every request. 4LC encodes observ...

</details>

<details>
<summary><b>69. TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17540) • [📄 arXiv](https://arxiv.org/abs/2610.17540) • [📥 PDF](https://arxiv.org/pdf/2610.17540)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can a VLA get the benefit of reasoning without waiting for it? In TacitVLA, the action expert never attends to the reasoning it generates for the current call, so actions do not wait on autoregressive decoding. Across RoboMME, RMBench, LIBERO, and...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 69 |
| 📅 Today | [`2026-10-14.json`](data/daily/2026-10-14.json) | 69 |
| 📆 This Week | [`2026-W41.json`](data/weekly/2026-W41.json) | 131 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 817 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-14 | 69 | [View JSON](data/daily/2026-10-14.json) |
| 📄 2026-10-13 | 15 | [View JSON](data/daily/2026-10-13.json) |
| 📄 2026-10-12 | 47 | [View JSON](data/daily/2026-10-12.json) |
| 📄 2026-10-11 | 72 | [View JSON](data/daily/2026-10-11.json) |
| 📄 2026-10-10 | 72 | [View JSON](data/daily/2026-10-10.json) |
| 📄 2026-10-09 | 55 | [View JSON](data/daily/2026-10-09.json) |
| 📄 2026-10-08 | 52 | [View JSON](data/daily/2026-10-08.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W41 | 131 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 817 | [View JSON](data/monthly/2026-10.json) |
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
