<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-61-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7822+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">61</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">240</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">61</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7822+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 01, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation Residuals in On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** vaynetian, Donghanark, renweijie, chenmeijia30, LH2101

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36484) • [📄 arXiv](https://arxiv.org/abs/2609.36484) • [📥 PDF](https://arxiv.org/pdf/2609.36484)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/xixixixixxxx/RIDE)

> We introduce RIDE (RL-Induced Direction Extrapolation), an on-policy distillation method that treats an RL-trained teacher as a direction for learning. On student-generated trajectories, RIDE computes the layerwise hidden-state residual between th...

</details>

<details>
<summary><b>2. UniEvo-VL: An On-policy Self-Distillation Training Recipe for Multimodal Model Self-improvement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38721) • [📄 arXiv](https://arxiv.org/abs/2609.38721) • [📥 PDF](https://arxiv.org/pdf/2609.38721)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone, first author here! 👋 Can multimodal models improve image generation by learning from their own feedback? We introduce UniEvo-VL , an on-policy self-distillation training recipe for multimodal model self-improvement. Building on Qwen-i...

</details>

<details>
<summary><b>3. False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39102) • [📄 arXiv](https://arxiv.org/abs/2609.39102) • [📥 PDF](https://arxiv.org/pdf/2609.39102)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: In self-evolving search agents (a proposer writes questions + pseudo-labels from source documents, a solver answers them, and their agreement is the training reward), the proposer and solver can converge on shared errors: internal reward ke...

</details>

<details>
<summary><b>4. WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40325) • [📄 arXiv](https://arxiv.org/abs/2609.40325) • [📥 PDF](https://arxiv.org/pdf/2609.40325)

**💻 Code:** [⭐ Code](https://github.com/UCSB-NLP-Chang/WorldAuditBench) • [⭐ Code](https://github.com/huggingface)

> We introduce WorldAuditBench, a benchmark with 213 tasks across 13 interactive 3D environments that tests whether multimodal agents can explore, investigate, and identify world anomalies.

</details>

<details>
<summary><b>5. Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39982) • [📄 arXiv](https://arxiv.org/abs/2609.39982) • [📥 PDF](https://arxiv.org/pdf/2609.39982)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Mid-Harness, which scales test-time compute for terminal agents by sampling and verifying candidate actions before executing one, while keeping the action generator and execution harness unchanged. Our key finding is that verification...

</details>

<details>
<summary><b>6. AREX-2: Advancing Self-Improving Agents through Long-Horizon Reflective Tasks</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38288) • [📄 arXiv](https://arxiv.org/abs/2609.38288) • [📥 PDF](https://arxiv.org/pdf/2609.38288)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VectorSpaceLab/AREX-2)

> Homepage: https://github.com/VectorSpaceLab/AREX-2 Models: https://huggingface.co/collections/BAAI/arex-2

</details>

<details>
<summary><b>7. EvoDuet: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific Discovery</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40340) • [📄 arXiv](https://arxiv.org/abs/2609.40340) • [📥 PDF](https://arxiv.org/pdf/2609.40340)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Open-Galapagos/EvoDuet)

> Excited to introduce  🎶 EvoDuet: co-evolving web search and task solutions to push the state of the art across 8 scientific optimization tasks.

</details>

<details>
<summary><b>8. Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38143) • [📄 arXiv](https://arxiv.org/abs/2609.38143) • [📥 PDF](https://arxiv.org/pdf/2609.38143)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/qiancheng-apodex/MetaSkill-AI4AI)

> ArXiv: https://arxiv.org/pdf/2609.38143 Code: https://github.com/qiancheng-apodex/MetaSkill-AI4AI

</details>

<details>
<summary><b>9. EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38334) • [📄 arXiv](https://arxiv.org/abs/2609.38334) • [📥 PDF](https://arxiv.org/pdf/2609.38334)

**💻 Code:** [⭐ Code](https://github.com/Gnonymous/EVOKE#-results) • [⭐ Code](https://github.com/Gnonymous/EVOKE#-from-prediction-to-preference) • [⭐ Code](https://github.com/Gnonymous/EVOKE)

> EVOKE : E liciting W W o rld K nowledg e in Agents for Transferable Decision-Making 🌐 Project Page · 📑 Paper · 💡 Idea · 📊 Results · 📝 Citation EVOKE is a post-training method that elicits the world knowledge already inside pretrained LLM agents, s...

</details>

<details>
<summary><b>10. RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39045) • [📄 arXiv](https://arxiv.org/abs/2609.39045) • [📥 PDF](https://arxiv.org/pdf/2609.39045)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/WenyiWU0111/RSIGame)

> 🎮 From game generation to autonomous game improvement. Recent advances in large language models have made automatic game generation increasingly feasible, yet reliably improving generated games beyond a playable version remains challenging. We int...

</details>

<details>
<summary><b>11. More Choices, Fewer Decisions: Ordinal-Scale Bias in JEV-like Direct-Decision Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38827) • [📄 arXiv](https://arxiv.org/abs/2609.38827) • [📥 PDF](https://arxiv.org/pdf/2609.38827)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Direct-decision models turn text into low-latency structured labels and scores, making them attractive for classification and automatic evaluation. Yet reliability requires more than accuracy: a model must also use the ordinal decision scale suppl...

</details>

<details>
<summary><b>12. Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering</b> ⭐ 16</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38177) • [📄 arXiv](https://arxiv.org/abs/2609.38177) • [📥 PDF](https://arxiv.org/pdf/2609.38177)

**💻 Code:** [⭐ Code](https://github.com/cvlab-kaist/Imagine3D-LLM) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>13. Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40111) • [📄 arXiv](https://arxiv.org/abs/2609.40111) • [📥 PDF](https://arxiv.org/pdf/2609.40111)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> An unsuccessful LLM agent rollout contains more information than its final reward: the observations available to the agent, the actions it chose, and the environment’s responses. Reusing this experience for learning requires identifying a decision...

</details>

<details>
<summary><b>14. LANTERN: Illuminating Hidden Mathematical Knowledge in Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mikhail Seleznyov, Dmitry I. Ignatov, Ivan Oseledets, Elena Tutubalina, pashocles

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32264) • [📄 arXiv](https://arxiv.org/abs/2609.32264) • [📥 PDF](https://arxiv.org/pdf/2609.32264)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What if the next mathematical discovery is hiding between two objects nobody thought to connect? In under 8 hours, LANTERN scanned 50M OEIS pairs, verified 62 previously unlinked relations, and found four absent from both OEIS and the targeted lit...

</details>

<details>
<summary><b>15. Unmask the State: When Does State Adaptation Matter for Masked Diffusion Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33355) • [📄 arXiv](https://arxiv.org/abs/2609.33355) • [📥 PDF](https://arxiv.org/pdf/2609.33355)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Masked diffusion language models (MDMs) admit flexible generation orders, making the unmasking strategy an inference decision. Existing methods vary in how they prioritize positions, control parallelism, restrict selection regions, revise predicti...

</details>

<details>
<summary><b>16. It's Not What the Image Shows: Irrelevant Context Destabilises VLM Judges Without Informing Them</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37863) • [📄 arXiv](https://arxiv.org/abs/2609.37863) • [📥 PDF](https://arxiv.org/pdf/2609.37863)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38660) • [📄 arXiv](https://arxiv.org/abs/2609.38660) • [📥 PDF](https://arxiv.org/pdf/2609.38660)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Long-form subtitle translation requires more than sentence-level translation: terminology, character references, style, and context must remain consistent across entire episodes and series. We introduce SMART, a self-evolving multi-agent system th...

</details>

<details>
<summary><b>18. Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies</b> ⭐ 560</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38537) • [📄 arXiv](https://arxiv.org/abs/2609.38537) • [📥 PDF](https://arxiv.org/pdf/2609.38537)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/anonymous-report-421/GPT-as-Policy)

> Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies

</details>

<details>
<summary><b>19. AIM: Agentic Idea Management for Automated Research</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38445) • [📄 arXiv](https://arxiv.org/abs/2609.38445) • [📥 PDF](https://arxiv.org/pdf/2609.38445)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Implementing and evaluating research ideas is expensive. As agents generate more candidates, choosing what to explore and learning from previous experiments becomes increasingly important. Numerous approaches have been proposed for automated resea...

</details>

<details>
<summary><b>20. DC-SAE: Deep Compression Semantic Autoencoder for Faster Diffusion Convergence</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39222)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>21. DyRAD: Radar Novel View Synthesis for Dynamic Driving Scenes</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39841)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>22. ThinkV2V: Unleashing the Reasoning Capability of MLLMs for Instruction-Guided Video Editing</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Guisheng Liu, Hao Yang, Fan Zhang, Haoyang He, donghao-zhou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38541)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>23. I Have a Stream: Making Self-Supervised Learning Work on Continuous Video</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40333)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>24. Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39578)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>25. RoboCoach: World Models as Active Coaches for Compositional Robot Skills</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39685)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>26. Synthetic Pre-pretraining Survives Scale, but Not as a Grammatical Prior</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39827)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>27. LoopVL: Recurrent Visual Intelligence</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38426)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>28. Scaling Laws for Looped Mixture of Experts</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40316)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>29. Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40358)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>30. Decompose Radicals, Then Reward: Fine-Grained Inspection for Accurate Chinese Text Rendering</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37569)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>31. The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yue Wu, Yao Liu, Yanbo Li, Jingyi Shen, tzt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39661)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>32. OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39903)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>33. PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40285) • [📄 arXiv](https://arxiv.org/abs/2609.40285) • [📥 PDF](https://arxiv.org/pdf/2609.40285)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: Multi-turn agents don't fail everywhere. Most failed rollouts hinge on one early pivotal mistake , the mistake is usually recoverable, and standard on-policy distillation can't repair it because the student never samples the recovery action...

</details>

<details>
<summary><b>34. DuoOPD: Learning from Joint Teacher-Student Outcomes for Multi-Task On-Policy Distillation</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Rui Li, Linan Yue, Heng Zhou, Weibo Gao, Ao Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33711)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>35. A2Z GameSpec-Bench: How Faithfully Can Coding Agents Generate Games from Game Design Specifications?</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39564)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>36. Game-Guided Skill Discovery through Self-Play for Playable Agent Control</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sehoon Ha, Xue Bin Peng, Jeonghwan Kim, Seungeun Rho

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40137)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>37. WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38121)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>38. The Low-Rank Structure of VLA Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34599)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>39. CoEvoWhen: Policy-Tool Coevolution for Ultra-Long Video Temporal Grounding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40048)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>40. CUA-SWE: When Computer-Use Agents Meet Visual Software Engineering</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32600)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>41. The Endless Exam: Mathematical Constructions from Today's Models toward Superintelligence</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Muhansp

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.24555)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>42. Safety of Latent Communication in Multi-Agent Systems</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39788)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>43. ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Lu Cheng, Yupu Yao, Ke Fang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36333)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>44. Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37915)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>45. The Geometry of Inference in Transformer Residual Streams</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Radu State, Mikhail Burtsev, Timur Mudarisov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37824)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>46. SlideDP: Scaling Host-Resident LLM Fine-Tuning Across Multiple GPUs</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Yingli Zhao, Zhiyu Li, Yulong Ao, Shiyuan Lin, Regiayoung

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34162)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>47. Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Katharina von der Wense, Manuel Mager, Minh Duc Bui, mario-sanz

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36931)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>48. Working Around the Compute Ceiling: Byte-Exact Memory in Galahad Makes LLM Reading a One-Time Cost LLM Reading a One-Time Cost</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39358)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>49. Decision-Oriented Recommendation Reranking: An Empirical Study of Jev</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40241)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>50. SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38822)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>51. EviRover: Reinforcing Agentic Perception Beyond a Glance</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Manyuan Zhang, Yilei Jiang, Tianshuo Peng, Kaituo Feng, Kaixuan Fan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.40230)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>52. Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.29142)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>53. See it, Say it, Sorted: Mechanistic Diagnosis and Parameter-Space Mitigation of Emergent Misalignment in LLMs</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34970)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>54. Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.39166)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>55. Evaluating Bounded Autonomy in Regulated Agentic AI: A Diagnostic Harness with Constitutional Rewards, Escalation Labels, and Runtime Governance</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dipankar Sarkar

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37501)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>56. Retrieval Capacity of Self-Attention Under Competition</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Radu State, Mikhail Burtsev, Timur Mudarisov

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37879)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>57. CheatBench: Measuring Reward Gaming in AI Agents</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36308)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>58. AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38142)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>59. PatchHolmes: Agentic Patch Retrieval via Listwise Selection</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38807)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>60. Understanding Multimodality in Generative Behavioral Cloning</b> ⭐ 18</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.22493)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>61. Almost Human, Except When It Matters: VoxParity and the Decisions a Voice Should Change</b> ⭐ 0</summary>

<br/>

**👥 Authors:** bhavikmangla

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35922)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 61 |
| 📅 Today | [`2026-10-01.json`](data/daily/2026-10-01.json) | 61 |
| 📆 This Week | [`2026-W39.json`](data/weekly/2026-W39.json) | 240 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 61 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-01 | 61 | [View JSON](data/daily/2026-10-01.json) |
| 📄 2026-09-30 | 72 | [View JSON](data/daily/2026-09-30.json) |
| 📄 2026-09-29 | 83 | [View JSON](data/daily/2026-09-29.json) |
| 📄 2026-09-28 | 24 | [View JSON](data/daily/2026-09-28.json) |
| 📄 2026-09-27 | 22 | [View JSON](data/daily/2026-09-27.json) |
| 📄 2026-09-26 | 22 | [View JSON](data/daily/2026-09-26.json) |
| 📄 2026-09-25 | 18 | [View JSON](data/daily/2026-09-25.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W39 | 240 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 61 | [View JSON](data/monthly/2026-10.json) |
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
