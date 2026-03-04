<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-41-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-2686+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">41</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">91</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">119</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">2686+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** March 04, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. From Scale to Speed: Adaptive Test-Time Scaling for Image Editing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00141) • [📄 arXiv](https://arxiv.org/abs/2603.00141) • [📥 PDF](https://arxiv.org/pdf/2603.00141)

> Adaptive Test-Time Scaling for Image Editing CVPR26

</details>

<details>
<summary><b>2. OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens</b> ⭐ 118</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.02138) • [📄 arXiv](https://arxiv.org/abs/2603.02138) • [📥 PDF](https://arxiv.org/pdf/2603.02138)

**💻 Code:** [⭐ Code](https://github.com/OpenVGLab/OmniLottie)

> OmniLottie is the first family of end-to-end multimodal Lottie generators that leverage pre-trained Vision-Language Models (VLMs), capable of generating complex and detailed Lottie animations from multi-modal instructions including texts, images, ...

</details>

<details>
<summary><b>3. SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.23866) • [📄 arXiv](https://arxiv.org/abs/2602.23866) • [📥 PDF](https://arxiv.org/pdf/2602.23866)

**💻 Code:** [⭐ Code](https://github.com/SWE-rebench/SWE-rebench-V2)

> SWE-rebench V2: https://huggingface.co/datasets/nebius/SWE-rebench-V2 SWE-rebench V2 PRs: https://huggingface.co/datasets/nebius/SWE-rebench-V2-PRs

</details>

<details>
<summary><b>4. RubricBench: Aligning Model-Generated Rubrics with Human Standards</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01562) • [📄 arXiv](https://arxiv.org/abs/2603.01562) • [📥 PDF](https://arxiv.org/pdf/2603.01562)

**💻 Code:** [⭐ Code](https://github.com/planepig/rubricbench)

> 🚀 Are LLM Judges actually evaluating what matters, or just being distracted by surface-level polish? As LLM alignment shifts from scalar Reward Models to Generative RMs (LLM-as-a-Judge), the community has increasingly relied on rubric-guided evalu...

</details>

<details>
<summary><b>5. OpenAutoNLU: Open Source AutoML Library for NLU</b> ⭐ 28</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01824) • [📄 arXiv](https://arxiv.org/abs/2603.01824) • [📥 PDF](https://arxiv.org/pdf/2603.01824)

**💻 Code:** [⭐ Code](https://github.com/mts-ai/OpenAutoNLU)

> OpenAutoNLU is an open-source automated machine learning library for natural  language understanding (NLU) tasks, covering both text classification and named entity recognition (NER). Unlike existing solutions, we introduce  data-aware training re...

</details>

<details>
<summary><b>6. MMR-Life: Piecing Together Real-life Scenes for Multimodal Multi-image Reasoning</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.02024) • [📄 arXiv](https://arxiv.org/abs/2603.02024) • [📥 PDF](https://arxiv.org/pdf/2603.02024)

**💻 Code:** [⭐ Code](https://github.com/BugMakerzzz/MMR-Life)

> Accepted by ICLR 2026 Homepage: https://mmr-life-bench.github.io/ Dataset: https://huggingface.co/datasets/Septzzz/MMR-Life Github: https://github.com/BugMakerzzz/MMR-Life

</details>

<details>
<summary><b>7. CHIMERA: Compact Synthetic Data for Generalizable LLM Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00889) • [📄 arXiv](https://arxiv.org/abs/2603.00889) • [📥 PDF](https://arxiv.org/pdf/2603.00889)

> We introduce CHIMERA , a compact but high-difficulty synthetic reasoning dataset with long Chain-of-Thought trajectories and broad multi-disciplinary coverage, designed for reasoning post-training of large language models. Dataset CHIMERA contains...

</details>

<details>
<summary><b>8. VGGT-Det: Mining VGGT Internal Priors for Sensor-Geometry-Free Multi-View Indoor 3D Object Detection</b> ⭐ 50</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00912) • [📄 arXiv](https://arxiv.org/abs/2603.00912) • [📥 PDF](https://arxiv.org/pdf/2603.00912)

**💻 Code:** [⭐ Code](https://github.com/yangcaoai/VGGT-Det-CVPR2026)

> Accepted by CVPR 2026. Code Page: https://github.com/yangcaoai/VGGT-Det-CVPR2026

</details>

<details>
<summary><b>9. CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Zichen Tian, Ziru Liu, Hanbo Li, Cheng Gong, Jinpeng Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01940) • [📄 arXiv](https://arxiv.org/abs/2603.01940) • [📥 PDF](https://arxiv.org/pdf/2603.01940)

> Developing multi-turn interactive tool-use agents is challenging because real-world user needs are often complex and ambiguous, yet agents must execute deterministic actions to satisfy them. To address this gap, we introduce CoVe (Constraint-Verif...

</details>

<details>
<summary><b>10. PhotoBench: Beyond Visual Matching Towards Personalized Intent-Driven Photo Retrieval</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Teng Wang, Junjie Wu, Warden-H, CyberDancer, SorrowTea

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01493) • [📄 arXiv](https://arxiv.org/abs/2603.01493) • [📥 PDF](https://arxiv.org/pdf/2603.01493)

**💻 Code:** [⭐ Code](https://github.com/LaVieEnRose365/PhotoBench)

> Paper link: https://arxiv.org/abs/2603.01493 Github Repo: https://github.com/LaVieEnRose365/PhotoBench Leaderboard: https://www.sorrowcloud.tech/leaderboard

</details>

<details>
<summary><b>11. LLaDA-o: An Effective and Length-Adaptive Omni Diffusion Model</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01068) • [📄 arXiv](https://arxiv.org/abs/2603.01068) • [📥 PDF](https://arxiv.org/pdf/2603.01068)

**💻 Code:** [⭐ Code](https://github.com/ML-GSAI/LLaDA-o)

> We present LLaDA-o, a length-adaptive MoD omni-diffusion model that unifies multimodal understanding and image generation, reaching 87.04 on DPG-Bench; we will open-source the model and code in https://github.com/ML-GSAI/LLaDA-o .

</details>

<details>
<summary><b>12. Spectral Condition for μP under Width-Depth Scaling</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00541) • [📄 arXiv](https://arxiv.org/abs/2603.00541) • [📥 PDF](https://arxiv.org/pdf/2603.00541)

**💻 Code:** [⭐ Code](https://github.com/ML-GSAI/Width-Depth-muP)

> Spectral Condition for muP under Width–Depth Scaling. scaling, maximal update parameterization, muP, feature learning, hyperparameter transfer, optimization.

</details>

<details>
<summary><b>13. WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories</b> ⭐ 31</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.02049) • [📄 arXiv](https://arxiv.org/abs/2603.02049) • [📥 PDF](https://arxiv.org/pdf/2603.02049)

**💻 Code:** [⭐ Code](https://github.com/FuchengSu/WorldStereo)

> Recent advances in foundational Video Diffusion Models (VDMs) have yielded significant progress. Yet, despite the remarkable visual quality of generated videos, reconstructing consistent 3D scenes from these outputs remains challenging, due to lim...

</details>

<details>
<summary><b>14. Efficient RLVR Training via Weighted Mutual Information Data Selection</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01907) • [📄 arXiv](https://arxiv.org/abs/2603.01907) • [📥 PDF](https://arxiv.org/pdf/2603.01907)

> No abstract available.

</details>

<details>
<summary><b>15. Learn Hard Problems During RL with Reference Guided Fine-tuning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01223) • [📄 arXiv](https://arxiv.org/abs/2603.01223) • [📥 PDF](https://arxiv.org/pdf/2603.01223)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API POPE: Learning to Reason on Hard Problems via Privileged On-Policy Explorat...

</details>

<details>
<summary><b>16. When Does RL Help Medical VLMs? Disentangling Vision, SFT, and RL Gains</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01301) • [📄 arXiv](https://arxiv.org/abs/2603.01301) • [📥 PDF](https://arxiv.org/pdf/2603.01301)

**💻 Code:** [⭐ Code](https://github.com/armenjeddi/medbridgerl)

> MedBridgeRL

</details>

<details>
<summary><b>17. CMI-RewardBench: Evaluating Music Reward Models with Compositional Multimodal Instruction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00610) • [📄 arXiv](https://arxiv.org/abs/2603.00610) • [📥 PDF](https://arxiv.org/pdf/2603.00610)

**💻 Code:** [⭐ Code](https://github.com/Haiwen-Xia/CMI-RewardBench)

> Arxiv paper https://arxiv.org/abs/2603.00610 Pre-training dataset https://huggingface.co/datasets/HaiwenXia/cmi-pref-pseudo finetuning dataset https://huggingface.co/datasets/HaiwenXia/cmi-pref benchmark code https://github.com/Haiwen-Xia/CMI-Rewa...

</details>

<details>
<summary><b>18. Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.21320) • [📄 arXiv](https://arxiv.org/abs/2602.21320) • [📥 PDF](https://arxiv.org/pdf/2602.21320)

**💻 Code:** [⭐ Code](https://github.com/emrecanacikgoz/Tool-R0)

> A self-play RL framework for training general-purpose tool-calling agents from scratch, without any human data.

</details>

<details>
<summary><b>19. Unified Vision-Language Modeling via Concept Space Alignment</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Holger Schwenk, Paul-Ambroise Duquenne, Yifu Qiu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01096) • [📄 arXiv](https://arxiv.org/abs/2603.01096) • [📥 PDF](https://arxiv.org/pdf/2603.01096)

> We introduce V-SONAR, a vision-language embedding space extended from the text-only embedding space SONAR (Omnilingual Embeddings Team et al., 2026), which supports 1500 text languages and 177 speech languages. To construct V-SONAR, we propose a p...

</details>

<details>
<summary><b>20. Half-Truths Break Similarity-Based Retrieval</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Seong Joon Oh, Bora Kargi, Gigglingface

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.23906) • [📄 arXiv](https://arxiv.org/abs/2602.23906) • [📥 PDF](https://arxiv.org/pdf/2602.23906)

**💻 Code:** [⭐ Code](https://github.com/kargibora/CS-CLIP)

> Code is available at https://github.com/kargibora/CS-CLIP

</details>

<details>
<summary><b>21. Agentic Code Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Satish Chandra, Shubham Ugare

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01896) • [📄 arXiv](https://arxiv.org/abs/2603.01896) • [📥 PDF](https://arxiv.org/pdf/2603.01896)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Agentic Rubrics as Contextual Verifiers for SWE Agents (2026) OmniCode: A B...

</details>

<details>
<summary><b>22. Recursive Think-Answer Process for LLMs and VLMs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yong Man Ro, Youngchae Chee, BK-Lee

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.02099) • [📄 arXiv](https://arxiv.org/abs/2603.02099) • [📥 PDF](https://arxiv.org/pdf/2603.02099)

> 🧠 Can models know when they are wrong—and try again? Think–Answer models such as DeepSeek-R1 and OpenAI o1 sometimes produce self-reflective cues like “Oops” or “Let me reconsider,” suggesting internal uncertainty. However, even when this uncertai...

</details>

<details>
<summary><b>23. Legal RAG Bench: an end-to-end benchmark for legal RAG</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01710) • [📄 arXiv](https://arxiv.org/abs/2603.01710) • [📥 PDF](https://arxiv.org/pdf/2603.01710)

**💻 Code:** [⭐ Code](https://github.com/isaacus-dev/legal-rag-bench)

> Hey Hugging Face, This is Legal RAG Bench, the first benchmark for legal RAG systems to simultaneously evaluate hallucinations, retrieval failures, and reasoning errors. The key takeaways of our benchmark are: Embedding models, not generative mode...

</details>

<details>
<summary><b>24. Spectral Attention Steering for Prompt Highlighting</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01281) • [📄 arXiv](https://arxiv.org/abs/2603.01281) • [📥 PDF](https://arxiv.org/pdf/2603.01281)

**💻 Code:** [⭐ Code](https://github.com/waylonli/SEKA)

> Attention steering is an important technique for controlling model focus, enabling capabilities such as prompt highlighting, where the model prioritises user-specified text. However, existing attention steering methods require explicit storage of ...

</details>

<details>
<summary><b>25. Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training</b> ⭐ 34</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.02208) • [📄 arXiv](https://arxiv.org/abs/2603.02208) • [📥 PDF](https://arxiv.org/pdf/2603.02208)

**💻 Code:** [⭐ Code](https://github.com/sileod/reasoning_core) • [⭐ Code](https://github.com/sileod/reasoning_core/)

> Training on verifiable symbolic data is a promising way to expand the reasoning frontier of language models beyond what standard pre-training corpora provide. Yet existing procedural generators often rely on fixed puzzles or templates and do not d...

</details>

<details>
<summary><b>26. Tool Verification for Test-Time Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yasaman Samadzadeh, Yuhui Zhang, Xiaohan Wang, Nikolai Röhrich, Ruotong Liao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.02203) • [📄 arXiv](https://arxiv.org/abs/2603.02203) • [📥 PDF](https://arxiv.org/pdf/2603.02203)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Distribution-Aware Reward Estimation for Test-Time Reinforcement Learning (...

</details>

<details>
<summary><b>27. CharacterFlywheel: Scaling Iterative Improvement of Engaging and Steerable LLMs in Production</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01973) • [📄 arXiv](https://arxiv.org/abs/2603.01973) • [📥 PDF](https://arxiv.org/pdf/2603.01973)

> We present CharacterFlywheel — an iterative process optimizing LLMs for real human engagement and character steerability, while maintaining rigorous safety protocols. Tested across Instagram, WhatsApp & Messenger with millions of users — where the...

</details>

<details>
<summary><b>28. LaSER: Internalizing Explicit Reasoning into Latent Space for Dense Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01425) • [📄 arXiv](https://arxiv.org/abs/2603.01425) • [📥 PDF](https://arxiv.org/pdf/2603.01425)

> Empowering dense retrievers with latent reasoning for high-performance, latency-free complex search. dense retrieval, latent reasoning, latent CoT, representation learning, efficiency.

</details>

<details>
<summary><b>29. ArtLLM: Generating Articulated Assets via 3D LLM</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01142) • [📄 arXiv](https://arxiv.org/abs/2603.01142) • [📥 PDF](https://arxiv.org/pdf/2603.01142)

> Accepted by CVPR 2026. Code will be released soon.

</details>

<details>
<summary><b>30. RAISE: Requirement-Adaptive Evolutionary Refinement for Training-Free Text-to-Image Alignment</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00483) • [📄 arXiv](https://arxiv.org/abs/2603.00483) • [📥 PDF](https://arxiv.org/pdf/2603.00483)

**💻 Code:** [⭐ Code](https://github.com/LiyaoJiang1998/RAISE)

> “RAISE: Requirement-Adaptive Self-Improving Evolution for Training-Free Text-to-Image Alignment” has been accepted to CVPR 2026! 🎉 📌 Question we address: Without training on massive carefully curated data or model scaling, can we simply achieve pr...

</details>

<details>
<summary><b>31. Classroom Final Exam: An Instructor-Tested Reasoning Benchmark</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19517) • [📄 arXiv](https://arxiv.org/abs/2602.19517) • [📥 PDF](https://arxiv.org/pdf/2602.19517)

**💻 Code:** [⭐ Code](https://github.com/Analogy-AI/CFE_Bench)

> CFE-Bench (Classroom Final Exam) is a text-only and multimodal reasoning benchmark built from authentic, repeatedly used university homework and exam problems sourced from instructor-maintained course materials and verified by professors. It conta...

</details>

<details>
<summary><b>32. CC-VQA: Conflict- and Correlation-Aware Method for Mitigating Knowledge Conflict in Knowledge-Based Visual Question Answering</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.23952) • [📄 arXiv](https://arxiv.org/abs/2602.23952) • [📥 PDF](https://arxiv.org/pdf/2602.23952)

**💻 Code:** [⭐ Code](https://github.com/cqu-student/CC-VQA)

> CVPR 2026

</details>

<details>
<summary><b>33. Synthetic Visual Genome 2: Extracting Large-scale Spatio-Temporal Scene Graphs from Videos</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.23543) • [📄 arXiv](https://arxiv.org/abs/2602.23543) • [📥 PDF](https://arxiv.org/pdf/2602.23543)

> Website: SVG2 Paper: arxiv Dataset: SVG2 Dataset Model: Traser

</details>

<details>
<summary><b>34. SeeThrough3D: Occlusion Aware 3D Control in Text-to-Image Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** R. Venkatesh Babu, Ravi Kiran Sarvadevabhatla, Pradhaan Bhat, Rishubh Parihar, Vaibhav Agrawal

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.23359) • [📄 arXiv](https://arxiv.org/abs/2602.23359) • [📥 PDF](https://arxiv.org/pdf/2602.23359)

> Current models for 3D aware control do not generate occlusions accurately, thus lead to unrealistic generations. This work proposes as simple yet effective mechanism to generate multi object scenes with complex occlusions, with 3D control over loc...

</details>

<details>
<summary><b>35. MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00585) • [📄 arXiv](https://arxiv.org/abs/2603.00585) • [📥 PDF](https://arxiv.org/pdf/2603.00585)

> In the current era of rapid advancements in video generation, while macroscopic simulation has reached unprecedented heights, the microscopic realm — the fundamental engine of life and science — remained a largely uncharted "black box" for AI. Mic...

</details>

<details>
<summary><b>36. ProtegoFed: Backdoor-Free Federated Instruction Tuning with Interspersed Poisoned Data</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00516) • [📄 arXiv](https://arxiv.org/abs/2603.00516) • [📥 PDF](https://arxiv.org/pdf/2603.00516)

**💻 Code:** [⭐ Code](https://github.com/dongdongzhaoUP/ProtegoFed)

> Federated Instruction Tuning (FIT) enables collaborative instruction tuning of large language models across multiple organizations (clients) in a cross-silo setting without requiring the sharing of private instructions. Recent findings on natural ...

</details>

<details>
<summary><b>37. FireRed-OCR Technical Report</b> ⭐ 90</summary>

<br/>

**👥 Authors:** Zhaojun Sun, Zuodong Zhong, Xinyue Li, Haoran Lou, Hao Wu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01840) • [📄 arXiv](https://arxiv.org/abs/2603.01840) • [📥 PDF](https://arxiv.org/pdf/2603.01840)

**💻 Code:** [⭐ Code](https://github.com/FireRedTeam/FireRed-OCR)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API PaddleOCR-VL-1.5: Towards a Multi-Task 0.9B VLM for Robust In-the-Wild Docu...

</details>

<details>
<summary><b>38. Cryo-Bench: Benchmarking Foundation Models for Cryosphere Applications</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Beth Tellman, Lalit Maurya, Saurabh Kaushik

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.01576) • [📄 arXiv](https://arxiv.org/abs/2603.01576) • [📥 PDF](https://arxiv.org/pdf/2603.01576)

**💻 Code:** [⭐ Code](https://github.com/Sk-2103/Cryo-Bench)

> Cryo‑Bench, the first comprehensive benchmark designed to evaluate how well Geospatial Foundation Models (GFMs) handle one of Earth’s most challenging and climate‑critical domains — the cryosphere. GFMs are rapidly transforming Earth observation r...

</details>

<details>
<summary><b>39. Using Songs to Improve Kazakh Automatic Speech Recognition</b> ⭐ 0</summary>

<br/>

**👥 Authors:** yeshpanovrustem

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2603.00961) • [📄 arXiv](https://arxiv.org/abs/2603.00961) • [📥 PDF](https://arxiv.org/pdf/2603.00961)

> Accepted to LREC 2026

</details>

<details>
<summary><b>40. Planning from Observation and Interaction</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.24121) • [📄 arXiv](https://arxiv.org/abs/2602.24121) • [📥 PDF](https://arxiv.org/pdf/2602.24121)

**💻 Code:** [⭐ Code](https://github.com/UWRobotLearning/mpail2)

> This work investigates real-world observational learning, or Inverse Reinforcement Learning from Observation (IRLfO), in which neither demonstration actions nor hand-designed rewards are assumed available. Previously too sample inefficient for rea...

</details>

<details>
<summary><b>41. Monocular Mesh Recovery and Body Measurement of Female Saanen Goats</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Tao Yu, Bin Zhang, Shichao Zhao, Bo Jin, luoxue-star

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.19896) • [📄 arXiv](https://arxiv.org/abs/2602.19896) • [📥 PDF](https://arxiv.org/pdf/2602.19896)

**💻 Code:** [⭐ Code](https://github.com/bojin-nwafu/Female-Saanen-Goats)

> Accepted to AAAI 2026

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 41 |
| 📅 Today | [`2026-03-04.json`](data/daily/2026-03-04.json) | 41 |
| 📆 This Week | [`2026-W09.json`](data/weekly/2026-W09.json) | 91 |
| 🗓️ This Month | [`2026-03.json`](data/monthly/2026-03.json) | 119 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-03-04 | 41 | [View JSON](data/daily/2026-03-04.json) |
| 📄 2026-03-03 | 22 | [View JSON](data/daily/2026-03-03.json) |
| 📄 2026-03-02 | 28 | [View JSON](data/daily/2026-03-02.json) |
| 📄 2026-03-01 | 28 | [View JSON](data/daily/2026-03-01.json) |
| 📄 2026-02-28 | 28 | [View JSON](data/daily/2026-02-28.json) |
| 📄 2026-02-27 | 30 | [View JSON](data/daily/2026-02-27.json) |
| 📄 2026-02-26 | 32 | [View JSON](data/daily/2026-02-26.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W09 | 91 | [View JSON](data/weekly/2026-W09.json) |
| 📅 2026-W08 | 184 | [View JSON](data/weekly/2026-W08.json) |
| 📅 2026-W07 | 197 | [View JSON](data/weekly/2026-W07.json) |
| 📅 2026-W06 | 293 | [View JSON](data/weekly/2026-W06.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-03 | 119 | [View JSON](data/monthly/2026-03.json) |
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
