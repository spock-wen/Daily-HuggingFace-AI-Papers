<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-37-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3089+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">37</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">41</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">522</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3089+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** March 24, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.17024) • [📄 arXiv](https://arxiv.org/abs/2603.17024) • [📥 PDF](https://arxiv.org/pdf/2603.17024)

> When training Qwen3.5, we kept asking ourselves: 🧐What kind of multimodal RLVR data actually leads to generalizable gains? 💡We believe the answer may not lie only in data tightly tailored to specific benchmarks, but also in OOD proxy tasks that tr...

</details>

<details>
<summary><b>2. Astrolabe: Steering Forward-Process Reinforcement Learning for Distilled Autoregressive Video Models</b> ⭐ 54</summary>

<br/>

**👥 Authors:** Jie Huang, Siming Fu, Zeyue Xue, Songchun Zhang, refkxh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.17051) • [📄 arXiv](https://arxiv.org/abs/2603.17051) • [📥 PDF](https://arxiv.org/pdf/2603.17051)

**💻 Code:** [⭐ Code](https://github.com/franklinz233/Astrolabe)

> Astrolabe is an efficient online Reinforcement Learning (RL) framework designed to align distilled autoregressive (AR) streaming video models with human visual preferences. Without sacrificing real-time inference speed, Astrolabe consistently and ...

</details>

<details>
<summary><b>3. TerraScope: Pixel-Grounded Visual Reasoning for Earth Observation</b> ⭐ 110</summary>

<br/>

**👥 Authors:** Begüm Demir, Xiao Xiang Zhu, Bin Ren, Yan Shu, earthflow

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19039) • [📄 arXiv](https://arxiv.org/abs/2603.19039) • [📥 PDF](https://arxiv.org/pdf/2603.19039)

**💻 Code:** [⭐ Code](https://github.com/shuyansy/Earth-Observation-VLMs)

> CVPR2026-Pixel-Grounded reasoning for Earth Observation.

</details>

<details>
<summary><b>4. ProactiveBench: Benchmarking Proactiveness in Multimodal Large Language Models</b> ⭐ 18</summary>

<br/>

**👥 Authors:** Massimiliano Mancini, Elisa Ricci, Stéphane Lathuilière, Subhankar Roy, Thomas De Min

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19466) • [📄 arXiv](https://arxiv.org/abs/2603.19466) • [📥 PDF](https://arxiv.org/pdf/2603.19466)

**💻 Code:** [⭐ Code](https://github.com/tdemin16/proactivebench)

> We introduce ProactiveBench, a benchmark to evaluate whether MLLMs can ask for help when faced with unanswerable visual queries, e.g., suggesting to move an occluding object rather than hallucinating or abstaining. We repurpose 7 datasets into 7 d...

</details>

<details>
<summary><b>5. FlowScene: Style-Consistent Indoor Scene Generation with Multimodal Graph Rectified Flow</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chao Zhang, YuYang Yin, Keyang Lu, Guangyao Zhai, yangzhifei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19598) • [📄 arXiv](https://arxiv.org/abs/2603.19598) • [📥 PDF](https://arxiv.org/pdf/2603.19598)

> scene generation

</details>

<details>
<summary><b>6. The Y-Combinator for LLMs: Solving Long-Context Rot with λ-Calculus</b> ⭐ 46</summary>

<br/>

**👥 Authors:** Haitham Bou-Ammar, Matthieu Zimmer, Xiaotong Ji, Rasul Tutunov, Amartya Roy

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.20105) • [📄 arXiv](https://arxiv.org/abs/2603.20105) • [📥 PDF](https://arxiv.org/pdf/2603.20105)

**💻 Code:** [⭐ Code](https://github.com/lambda-calculus-LLM/lambda-RLM)

> 🎰 Why your 405B model is losing to an 8B model (and how 1930s math fixed it). The AI industry has a "Context Rot" problem. 🥕 As prompts get longer, we usually try to fix them with more RAM or massive parameter counts. But "stochastic control", i.e...

</details>

<details>
<summary><b>7. LumosX: Relate Any Identities with Their Attributes for Personalized Video Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.20192) • [📄 arXiv](https://arxiv.org/abs/2603.20192) • [📥 PDF](https://arxiv.org/pdf/2603.20192)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/Lumos-Custom)

> Code and models: https://jiazheng-xing.github.io/lumosx-home/ https://github.com/alibaba-damo-academy/Lumos-Custom

</details>

<details>
<summary><b>8. Hyperagents</b> ⭐ 109</summary>

<br/>

**👥 Authors:** Jeff Clune, Jakob Foerster, Wannan Yang, Bingchen Zhao, Jenny Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19461) • [📄 arXiv](https://arxiv.org/abs/2603.19461) • [📥 PDF](https://arxiv.org/pdf/2603.19461)

**💻 Code:** [⭐ Code](https://github.com/facebookresearch/Hyperagents)

> Introduces hyperagents, self-referential systems where task and meta agents co-modify themselves, enabling metacognitive self-improvement and cross-domain performance gains beyond coding tasks.

</details>

<details>
<summary><b>9. A Subgoal-driven Framework for Improving Long-Horizon LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19685) • [📄 arXiv](https://arxiv.org/abs/2603.19685) • [📥 PDF](https://arxiv.org/pdf/2603.19685)

> This paper seems outdated. Why are GPT-4 Turbo and GPT-4o still being presented as SOTA?

</details>

<details>
<summary><b>10. Reasoning as Compression: Unifying Budget Forcing via the Conditional Information Bottleneck</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.08462) • [📄 arXiv](https://arxiv.org/abs/2603.08462) • [📥 PDF](https://arxiv.org/pdf/2603.08462)

> Chain-of-Thought (CoT) prompting improves LLM accuracy on complex tasks but often increases token usage and inference cost. Existing "Budget Forcing" methods reducing cost via fine-tuning with heuristic length penalties, suppress both essential re...

</details>

<details>
<summary><b>11. Versatile Editing of Video Content, Actions, and Dynamics without Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.17989) • [📄 arXiv](https://arxiv.org/abs/2603.17989) • [📥 PDF](https://arxiv.org/pdf/2603.17989)

> Current inversion-free approaches struggle to perform general non-structure-preserving edits. In particular, when tuning their hyperparameters to allow significant modifications, they generate videos whose low frequencies are unnecessarily misalig...

</details>

<details>
<summary><b>12. Deep Tabular Research via Continual Experience-Driven Execution</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.09151) • [📄 arXiv](https://arxiv.org/abs/2603.09151) • [📥 PDF](https://arxiv.org/pdf/2603.09151)

> A novel agentic deep research framework that treats tabular reasoning as a closed-loop decision-making process. Specifically, (i) DTR first constructs a hierarchical meta graph to capture bidirectional semantics, mapping natural language queries i...

</details>

<details>
<summary><b>13. WorldAgents: Can Foundation Image Models be Agents for 3D World Models?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Matthias Nießner, Angela Dai, Ziya Erkoç

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19708) • [📄 arXiv](https://arxiv.org/abs/2603.19708) • [📥 PDF](https://arxiv.org/pdf/2603.19708)

> Shows that 2D foundation image models encode 3D world understanding, enabling a multi-agent Director-Generator-Verifier system to synthesize coherent, 3D-consistent scenes and novel-view reconstructions.

</details>

<details>
<summary><b>14. BEAVER: A Training-Free Hierarchical Prompt Compression Method via Structure-Aware Page Selection</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19635) • [📄 arXiv](https://arxiv.org/abs/2603.19635) • [📥 PDF](https://arxiv.org/pdf/2603.19635)

**💻 Code:** [⭐ Code](https://github.com/JusperLee/BEAVER)

> This paper introduces BEAVER (a training-free hierarchical prompt compression method), which addresses the computational challenges of processing long documents with LLMs. Method BEAVER shifts from linear token removal to structure-aware hierarchi...

</details>

<details>
<summary><b>15. How Well Does Generative Recommendation Generalize?</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19809) • [📄 arXiv](https://arxiv.org/abs/2603.19809) • [📥 PDF](https://arxiv.org/pdf/2603.19809)

**💻 Code:** [⭐ Code](https://github.com/Jamesding000/MemGen-GR)

> Shows that semantic ID-based generative recommendation models perform better on instances that require generalization, whereas conventional item ID-based models perform better when memorization is more important.

</details>

<details>
<summary><b>16. HiMu: Hierarchical Multimodal Frame Selection for Long Video Question Answering</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.18558) • [📄 arXiv](https://arxiv.org/abs/2603.18558) • [📥 PDF](https://arxiv.org/pdf/2603.18558)

**💻 Code:** [⭐ Code](https://github.com/DanBenAmi/HiMu)

> TL;DR: HiMu is a training-free frame selector for long video QA that gets the best of both worlds — structured reasoning without expensive LVLM calls. The problem: When answering questions about long videos, you need to pick the right frames. Fast...

</details>

<details>
<summary><b>17. Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19987) • [📄 arXiv](https://arxiv.org/abs/2603.19987) • [📥 PDF](https://arxiv.org/pdf/2603.19987)

> We found that RL post-training for LLMs hits a persistent capability ceiling because models condition on ever-growing action histories instead of compact Markov states — we proposed reintroducing explicit Markov state estimation into the training ...

</details>

<details>
<summary><b>18. LoopRPT: Reinforcement Pre-Training for Looped Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuhan Li, Nuo Chen, hchang95, ThreeGold116, JENLISA4EVER

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19714) • [📄 arXiv](https://arxiv.org/abs/2603.19714) • [📥 PDF](https://arxiv.org/pdf/2603.19714)

> This paper proposes LoopRPT, a reinforcement pre-training framework that directly optimizes latent reasoning in looped language models. By shifting RL from sparse output supervision to step-wise rewards over intermediate reasoning, and focusing on...

</details>

<details>
<summary><b>19. EgoForge: Goal-Directed Egocentric World Simulator</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.20169) • [📄 arXiv](https://arxiv.org/abs/2603.20169) • [📥 PDF](https://arxiv.org/pdf/2603.20169)

> Given a single smart-glasses egocentric image, a high-level goal instruction, and an auxiliary exocentric view, EgoForge generates egocentric rollouts that follow user intent and preserve scene structure, without requiring dense supervision such a...

</details>

<details>
<summary><b>20. Beyond Single Tokens: Distilling Discrete Diffusion Models via Discrete MMD</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.20155) • [📄 arXiv](https://arxiv.org/abs/2603.20155) • [📥 PDF](https://arxiv.org/pdf/2603.20155)

> Discrete Moment Matching Distillation preserves quality and diversity when distilling discrete diffusion models, enabling efficient sampling for text and image tasks and sometimes surpassing teacher models.

</details>

<details>
<summary><b>21. Cooperation and Exploitation in LLM Policy Synthesis for Sequential Social Dilemmas</b> ⭐ 2</summary>

<br/>

**👥 Authors:** vicgalle

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19453) • [📄 arXiv](https://arxiv.org/abs/2603.19453) • [📥 PDF](https://arxiv.org/pdf/2603.19453)

**💻 Code:** [⭐ Code](https://github.com/vicgalle/llm-policies-social-dilemmas)

> @ librarian-bot recommend

</details>

<details>
<summary><b>22. DROID-SLAM in the Wild</b> ⭐ 148</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19076) • [📄 arXiv](https://arxiv.org/abs/2603.19076) • [📥 PDF](https://arxiv.org/pdf/2603.19076)

**💻 Code:** [⭐ Code](https://github.com/MoyangLi00/DROID-W)

> Our approach delivers high-quality dynamic point cloud reconstruction, accurate camera pose estimation, and dynamic uncertainty estimation. It robustly handles any real-world videos, including challenging film clips, and also supports static Gauss...

</details>

<details>
<summary><b>23. AgentDS Technical Report: Benchmarking the Future of Human-AI Collaboration in Domain-Specific Data Science</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fangqiao Tian, Robert Specht, Xun Xian, Jin Du, An Luo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19005) • [📄 arXiv](https://arxiv.org/abs/2603.19005) • [📥 PDF](https://arxiv.org/pdf/2603.19005)

> Our AgentDS technical report is now live on arXiv.

</details>

<details>
<summary><b>24. Teaching an Agent to Sketch One Part at a Time</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Greg Shakhnarovich, Yael Vinker, David Yunis, Ruize Xu, Xiaodan Du

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19500) • [📄 arXiv](https://arxiv.org/abs/2603.19500) • [📥 PDF](https://arxiv.org/pdf/2603.19500)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API IntroSVG: Learning from Rendering Feedback for Text-to-SVG Generation via a...

</details>

<details>
<summary><b>25. Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encoders</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Paola Cascante-Bonilla, Shang-Jui Ray Kuo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19209) • [📄 arXiv](https://arxiv.org/abs/2603.19209) • [📥 PDF](https://arxiv.org/pdf/2603.19209)

**💻 Code:** [⭐ Code](https://github.com/raykuo18/vlm-ssm-vision-encoders)

> Tweet: https://x.com/ai_bites/status/2035311212917923928?s=46

</details>

<details>
<summary><b>26. Language on Demand, Knowledge at Core: Composing LLMs with Encoder-Decoder Translation Models for Extensible Multilinguality</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yang Feng, Mengyu Bu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.17512) • [📄 arXiv](https://arxiv.org/abs/2603.17512) • [📥 PDF](https://arxiv.org/pdf/2603.17512)

**💻 Code:** [⭐ Code](https://github.com/ictnlp/XBridge)

> Our XBridge proposes a new paradigm for multilingual extension, beyond large-scale multilingual training or massive parameter expansion (e.g., MoE). With minimal additional parameters, limited training data, and parameter-efficient training, XBrid...

</details>

<details>
<summary><b>27. CurveStream: Boosting Streaming Video Understanding in MLLMs via Curvature-Aware Hierarchical Visual Memory Management</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tao Chen, Kangcong Li, Jianjian Cao, Xudong Tan, wangchao668

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19571) • [📄 arXiv](https://arxiv.org/abs/2603.19571) • [📥 PDF](https://arxiv.org/pdf/2603.19571)

**💻 Code:** [⭐ Code](https://github.com/streamingvideos/CurveStream)

> Streaming Video Understanding

</details>

<details>
<summary><b>28. TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Longwen Zhang, Qixuan Zhang, Kaixin Yao, Haoran Jiang, ZERONE182

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.17735) • [📄 arXiv](https://arxiv.org/abs/2603.17735) • [📥 PDF](https://arxiv.org/pdf/2603.17735)

> Submit.

</details>

<details>
<summary><b>29. Probing Cultural Signals in Large Language Models through Author Profiling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.16749) • [📄 arXiv](https://arxiv.org/abs/2603.16749) • [📥 PDF](https://arxiv.org/pdf/2603.16749)

**💻 Code:** [⭐ Code](https://github.com/ValentinLafargue/CulturalProbingLLM)

> When unsure, LLMs don’t stay neutral: they default. This paper shows how cultural bias emerges not only from errors, but from what models assume in the absence of strong signals.

</details>

<details>
<summary><b>30. Human-AI Synergy in Agentic Code Review</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.15911) • [📄 arXiv](https://arxiv.org/abs/2603.15911) • [📥 PDF](https://arxiv.org/pdf/2603.15911)

**💻 Code:** [⭐ Code](https://github.com/Software-Evolution-Analytics-Lab-SEAL/AI_Vs_Human_Codereview)

> No abstract available.

</details>

<details>
<summary><b>31. From Masks to Pixels and Meaning: A New Taxonomy, Benchmark, and Metrics for VLM Image Tampering</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.20193) • [📄 arXiv](https://arxiv.org/abs/2603.20193) • [📥 PDF](https://arxiv.org/pdf/2603.20193)

**💻 Code:** [⭐ Code](https://github.com/VILA-Lab/PIXAR)

> This paper reformulates VLM image tampering from coarse region labels to a pixel-grounded, meaning and language-aware task.

</details>

<details>
<summary><b>32. ReLi3D: Relightable Multi-view 3D Reconstruction with Disentangled Illumination</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19753) • [📄 arXiv](https://arxiv.org/abs/2603.19753) • [📥 PDF](https://arxiv.org/pdf/2603.19753)

**💻 Code:** [⭐ Code](https://github.com/Stability-AI/ReLi3D)

> Relightable 3D assets with physically based, spatially varying materials are still hard to obtain from images. Most approaches either separate geometry/materials/lighting into different stages, or they struggle with the fundamental ambiguity of si...

</details>

<details>
<summary><b>33. Adaptive Layerwise Perturbation: Unifying Off-Policy Corrections for LLM RL</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ziji Zhang, Zhou Yu, Yifan Hao, Xuanchang Zhang, Chenlu Ye

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.19470) • [📄 arXiv](https://arxiv.org/abs/2603.19470) • [📥 PDF](https://arxiv.org/pdf/2603.19470)

> Adaptive Layerwise Perturbation: Unifying Off-Policy Corrections for LLM RL

</details>

<details>
<summary><b>34. Automatic detection of Gen-AI texts: A comparative framework of neural models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.18750) • [📄 arXiv](https://arxiv.org/abs/2603.18750) • [📥 PDF](https://arxiv.org/pdf/2603.18750)

**💻 Code:** [⭐ Code](https://github.com/cristian03git/DETECTION_GENAI)

> How well can we detect AI-generated text? This paper presents a comparative framework evaluating multiple neural architectures — including CNNs, MLPs, MobileNet-based models, and Transformers — for AI text detection. We analyze performance across ...

</details>

<details>
<summary><b>35. Multiscale Switch for Semi-Supervised and Contrastive Learning in Medical Ultrasound Image Segmentation</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.18655) • [📄 arXiv](https://arxiv.org/abs/2603.18655) • [📥 PDF](https://arxiv.org/pdf/2603.18655)

**💻 Code:** [⭐ Code](https://github.com/jinggqu/Switch)

> No abstract available.

</details>

<details>
<summary><b>36. ReLMXEL: Adaptive RL-Based Memory Controller with Explainable Energy and Latency Optimization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Naveen M, Venkata Kalyan Tavva, R. Raghunatha Sarma, Gandholi Sarat, Chirag9132

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.17309) • [📄 arXiv](https://arxiv.org/abs/2603.17309) • [📥 PDF](https://arxiv.org/pdf/2603.17309)

**💻 Code:** [⭐ Code](https://github.com/Chirag-Sai-Panuganti/ReLMXEL)

> Explainable multi-agent reinforcement learning (RL) framework designed to optimize memory controller parameters, reducing latency and energy consumption while improving memory bandwidth utilization.

</details>

<details>
<summary><b>37. s2n-bignum-bench: A practical benchmark for evaluating low-level code reasoning of LLMs</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Carlo Lipizzi, Juneyoung Lee, Soonho Kong, John Harrison, kings-crown

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.14628) • [📄 arXiv](https://arxiv.org/abs/2603.14628) • [📥 PDF](https://arxiv.org/pdf/2603.14628)

**💻 Code:** [⭐ Code](https://github.com/kings-crown/s2n-bignum-bench)

> We propose a new benchmark evaluating large language models on formal proof synthesis for industrial cryptographic assembly routines verified in HOL Light, addressing the gap between competition mathematics and real-world implementation verification.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 37 |
| 📅 Today | [`2026-03-24.json`](data/daily/2026-03-24.json) | 37 |
| 📆 This Week | [`2026-W12.json`](data/weekly/2026-W12.json) | 41 |
| 🗓️ This Month | [`2026-03.json`](data/monthly/2026-03.json) | 522 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-03-24 | 37 | [View JSON](data/daily/2026-03-24.json) |
| 📄 2026-03-23 | 4 | [View JSON](data/daily/2026-03-23.json) |
| 📄 2026-03-22 | 32 | [View JSON](data/daily/2026-03-22.json) |
| 📄 2026-03-21 | 32 | [View JSON](data/daily/2026-03-21.json) |
| 📄 2026-03-20 | 2 | [View JSON](data/daily/2026-03-20.json) |
| 📄 2026-03-19 | 52 | [View JSON](data/daily/2026-03-19.json) |
| 📄 2026-03-18 | 8 | [View JSON](data/daily/2026-03-18.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W12 | 41 | [View JSON](data/weekly/2026-W12.json) |
| 📅 2026-W11 | 133 | [View JSON](data/weekly/2026-W11.json) |
| 📅 2026-W10 | 119 | [View JSON](data/weekly/2026-W10.json) |
| 📅 2026-W09 | 201 | [View JSON](data/weekly/2026-W09.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-03 | 522 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |
| 🗓️ 2025-12 | 787 | [View JSON](data/monthly/2025-12.json) |

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
