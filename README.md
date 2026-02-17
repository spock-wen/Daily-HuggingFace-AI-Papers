<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-32-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-2287+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">32</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">73</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">768</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">2287+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** February 17, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Less is Enough: Synthesizing Diverse Data in Feature Space of LLMs</b> ⭐ 52</summary>

<br/>

**👥 Authors:** Ninghao Liu, Lijie Hu, Yijiang Li, Xuansheng Wu, Zhongzhi1228

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.10388) • [📄 arXiv](https://arxiv.org/abs/2602.10388) • [📥 PDF](https://arxiv.org/pdf/2602.10388)

**💻 Code:** [⭐ Code](https://github.com/Zhongzhi660/FAC-Synthesis)

> Less is Enough shows that better data matters more than more data . Instead of generating massive amounts of synthetic sample, we look inside the model’s hidden features to find what is truly missing. We introduce Feature Activation Coverage (FAC)...

</details>

<details>
<summary><b>2. SQuTR: A Robustness Benchmark for Spoken Query to Text Retrieval under Acoustic Noise</b> ⭐ 96</summary>

<br/>

**👥 Authors:** Jianhao Nie, Yueying Hua, Ke Yang, Yuejie Li, berlin8587

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12783) • [📄 arXiv](https://arxiv.org/abs/2602.12783) • [📥 PDF](https://arxiv.org/pdf/2602.12783)

**💻 Code:** [⭐ Code](https://github.com/ttoyekk1a/SQuTR-Spoken-Query-to-Text-Retrieval)

> SQuTR (Spoken Query-to-Text Retrieval) is a large-scale bilingual benchmark designed to evaluate the robustness of information retrieval (IR) systems under realistic and complex acoustic perturbations. While speech has become a primary interface f...

</details>

<details>
<summary><b>3. MedXIAOHE: A Comprehensive Recipe for Building Medical MLLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12705) • [📄 arXiv](https://arxiv.org/abs/2602.12705) • [📥 PDF](https://arxiv.org/pdf/2602.12705)

> We present MedXIAOHE, a medical vision-language foundation model designed to advance general-purpose medical understanding and reasoning in real-world clinical applications. MedXIAOHE achieves state-of-the-art performance across diverse medical be...

</details>

<details>
<summary><b>4. Zooming without Zooming: Region-to-Image Distillation for Fine-Grained Multimodal Perception</b> ⭐ 55</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11858) • [📄 arXiv](https://arxiv.org/abs/2602.11858) • [📥 PDF](https://arxiv.org/pdf/2602.11858)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/Zooming-without-Zooming)

> Recent "Thinking-with-Images" methods improve fine-grained perception by iteratively zooming into regions of interest during inference, but incur high latency due to repeated tool calls and visual re-encoding. In this work, we present ZwZ models (...

</details>

<details>
<summary><b>5. OneVision-Encoder: Codec-Aligned Sparsity as a Foundational Principle for Multimodal Intelligence</b> ⭐ 225</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.08683) • [📄 arXiv](https://arxiv.org/abs/2602.08683) • [📥 PDF](https://arxiv.org/pdf/2602.08683)

**💻 Code:** [⭐ Code](https://github.com/EvolvingLMMs-Lab/OneVision-Encoder) • [⭐ Code](https://github.com/EvolvingLMMs-Lab/OneVision-Encoder/blob/main/docs/data_card.md)

> Code: https://github.com/EvolvingLMMs-Lab/OneVision-Encoder Data: https://github.com/EvolvingLMMs-Lab/OneVision-Encoder/blob/main/docs/data_card.md Model: https://huggingface.co/collections/lmms-lab-encoder/onevision-encoder

</details>

<details>
<summary><b>6. CoPE-VideoLM: Codec Primitives For Efficient Video Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13191) • [📄 arXiv](https://arxiv.org/abs/2602.13191) • [📥 PDF](https://arxiv.org/pdf/2602.13191)

> TL;DR: Replace dense per-frame image embeddings, use video codec primitives to reduce TTFT by up to 86% and token usage by up to 93% while maintaining video understanding performance. 🚀 Project Page: https://sayands.github.io/cope/

</details>

<details>
<summary><b>7. GeoAgent: Learning to Geolocate Everywhere with Reinforced Geographic Characteristics</b> ⭐ 15</summary>

<br/>

**👥 Authors:** MingMing Cheng, Dingwen Zhang, Boyuan Sun, Yiming Zhang, ghost233lism

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12617) • [📄 arXiv](https://arxiv.org/abs/2602.12617) • [📥 PDF](https://arxiv.org/pdf/2602.12617)

**💻 Code:** [⭐ Code](https://github.com/HVision-NKU/GeoAgent)

> GeoAgent is a model capable of reasoning closely with humans and deriving fine-grained address conclusions. For more details, please refer to our project and github repo

</details>

<details>
<summary><b>8. SemanticMoments: Training-Free Motion Similarity via Third Moment Features</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.09146) • [📄 arXiv](https://arxiv.org/abs/2602.09146) • [📥 PDF](https://arxiv.org/pdf/2602.09146)

> Modern video representations like VideoMAE and V-JEPA2 are biased toward appearance rather than motion. We introduce SemanticMoments, a training-free representation for semantic motion similarity.

</details>

<details>
<summary><b>9. What does RL improve for Visual Reasoning? A Frankenstein-Style Analysis</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12395) • [📄 arXiv](https://arxiv.org/abs/2602.12395) • [📥 PDF](https://arxiv.org/pdf/2602.12395)

**💻 Code:** [⭐ Code](https://github.com/tianyi-lab/Frankenstein)

> Reinforcement learning (RL) has become a common post-training stage for improving visual reasoning in multimodal models, but what exactly does RL improve internally? This paper introduces a Frankenstein-style causal analysis framework to dissect t...

</details>

<details>
<summary><b>10. Intelligent AI Delegation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11865) • [📄 arXiv](https://arxiv.org/abs/2602.11865) • [📥 PDF](https://arxiv.org/pdf/2602.11865)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Syst...

</details>

<details>
<summary><b>11. RLinf-Co: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12628) • [📄 arXiv](https://arxiv.org/abs/2602.12628) • [📥 PDF](https://arxiv.org/pdf/2602.12628)

> In this paper, we propose an RL-based sim-real Co-training (RL-Co) framework that leverages interactive simulation while preserving real-world capabilities.

</details>

<details>
<summary><b>12. ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning</b> ⭐ 157</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11236) • [📄 arXiv](https://arxiv.org/abs/2602.11236) • [📥 PDF](https://arxiv.org/pdf/2602.11236)

**💻 Code:** [⭐ Code](https://github.com/amap-cvlab/ABot-Manipulation)

> 🌟** ABot-M0** is a general-purpose robotics model with the following core highlights: Massive & Unified Data: It integrates over 6 million open-source trajectories to form the largest unified dataset for robotic manipulation, providing a strong fo...

</details>

<details>
<summary><b>13. Towards Universal Video MLLMs with Attribute-Structured and Quality-Verified Instructions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13013) • [📄 arXiv](https://arxiv.org/abs/2602.13013) • [📥 PDF](https://arxiv.org/pdf/2602.13013)

**💻 Code:** [⭐ Code](https://github.com/ASID-Caption/ASID-Caption)

> ASID-Caption introduces a data-and-model suite for fine-grained audiovisual video understanding. We present: • ASID-1M, a large-scale collection of attribute-structured and quality-verified audiovisual instruction annotations; • ASID-Verify, a sca...

</details>

<details>
<summary><b>14. BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid for Large Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.04163) • [📄 arXiv](https://arxiv.org/abs/2602.04163) • [📥 PDF](https://arxiv.org/pdf/2602.04163)

> we propose Bit-Plane Decomposition Quantization (BPDQ) , which constructs a variable quantization grid via bit-planes and scalar coefficients, and iteratively refines them using approximate second-order information while progressively compensating...

</details>

<details>
<summary><b>15. DICE: Diffusion Large Language Models Excel at Generating CUDA Kernels</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Zhiqiang Tao, Jianmian Wang, Xueyi Chen, Lingcheng Kong, DeadlyKitt3n

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11715) • [📄 arXiv](https://arxiv.org/abs/2602.11715) • [📥 PDF](https://arxiv.org/pdf/2602.11715)

**💻 Code:** [⭐ Code](https://github.com/deadlykitten4/DICE)

> DICE series are the first diffusion large language models (dLLMs) tailored for CUDA kernel generation. Welcome discussion and collaboration!

</details>

<details>
<summary><b>16. SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Huayu Sha, Binze Hu, Zhiheng Xi, Yajie Yang, Yujiong Shen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12984) • [📄 arXiv](https://arxiv.org/abs/2602.12984) • [📥 PDF](https://arxiv.org/pdf/2602.12984)

**💻 Code:** [⭐ Code](https://github.com/CMarsRover/SciAgentGYM)

> Proposes SciAgentGym and SciAgentBench to benchmark and improve multi-step scientific tool-use in LLM agents via SciForge data synthesis and fine-tuning, enabling cross-domain transfer.

</details>

<details>
<summary><b>17. FLAC: Maximum Entropy RL via Kinetic Energy Regularized Bridge Matching</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiao Ma, Fuchun Sun, Yu Luo, Yunfei Li, Lei Lv

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12829) • [📄 arXiv](https://arxiv.org/abs/2602.12829) • [📥 PDF](https://arxiv.org/pdf/2602.12829)

> FLAC is a likelihood-free RL method using kinetic energy regularization and a generalized Schrödinger bridge to stay near a high-entropy reference while optimizing return, avoiding explicit density estimation.

</details>

<details>
<summary><b>18. Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution</b> ⭐ 229</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12684) • [📄 arXiv](https://arxiv.org/abs/2602.12684) • [📥 PDF](https://arxiv.org/pdf/2602.12684)

**💻 Code:** [⭐ Code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0)

> Open-source Xiaomi-Robotics-0 delivers a vision-language-action model enabling real-time robotic action with cross-embodiment data and VLMs, plus asynchronous inference and smooth real-time rollouts.

</details>

<details>
<summary><b>19. On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12506) • [📄 arXiv](https://arxiv.org/abs/2602.12506) • [📥 PDF](https://arxiv.org/pdf/2602.12506)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Towards Faithful Reasoning in Comics for Small MLLMs (2026) Analyzing Reaso...

</details>

<details>
<summary><b>20. Code2Worlds: Empowering Coding LLMs for 4D World Generation</b> ⭐ 23</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11757) • [📄 arXiv](https://arxiv.org/abs/2602.11757) • [📥 PDF](https://arxiv.org/pdf/2602.11757)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/Code2Worlds)

> https://aigeeksgroup.github.io/Code2Worlds

</details>

<details>
<summary><b>21. Self-EvolveRec: Self-Evolving Recommender Systems with LLM-based Directional Feedback</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jimin Seo, Wonjoong Kim, Hongseok Kang, Sangwu Park, Sein-Kim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12612) • [📄 arXiv](https://arxiv.org/abs/2602.12612) • [📥 PDF](https://arxiv.org/pdf/2602.12612)

**💻 Code:** [⭐ Code](https://github.com/Sein-Kim/self_evolverec)

> We introduce Self-EvolveRec, a novel framework that enables recommender systems to autonomously evolve by transcending the limitations of simple scalar feedback. By implementing an LLM-based Directional Feedback Loop, we integrate qualitative crit...

</details>

<details>
<summary><b>22. Best of Both Worlds: Multimodal Reasoning and Generation via Unified Discrete Flow Matching</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12221) • [📄 arXiv](https://arxiv.org/abs/2602.12221) • [📥 PDF](https://arxiv.org/pdf/2602.12221)

> No abstract available.

</details>

<details>
<summary><b>23. TADA! Tuning Audio Diffusion Models through Activation Steering</b> ⭐ 9</summary>

<br/>

**👥 Authors:** Kamil Deja, Mateusz Modrzejewski, Katarzyna Zaleska, Łukasz Staniszewski

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11910) • [📄 arXiv](https://arxiv.org/abs/2602.11910) • [📥 PDF](https://arxiv.org/pdf/2602.11910)

**💻 Code:** [⭐ Code](https://github.com/luk-st/steer-audio)

> About In this work, we investigate the internal mechanisms 🔬 of text-to-audio 🎶 diffusion models, showing that various musical concepts (instruments 🎸, vocal 🎤, tempo 🏃, mood 🤗) are controlled by a small, shared subset of attention layers. By comb...

</details>

<details>
<summary><b>24. Light4D: Training-Free Extreme Viewpoint 4D Video Relighting</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11769) • [📄 arXiv](https://arxiv.org/abs/2602.11769) • [📥 PDF](https://arxiv.org/pdf/2602.11769)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/Light4D)

> https://aigeeksgroup.github.io/Light4D

</details>

<details>
<summary><b>25. Learning Image-based Tree Crown Segmentation from Enhanced Lidar-based Pseudo-labels</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xiaowei Yu, Niko Koivumäki, Josef Taher, Stefan Rua, Julppe1

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13022) • [📄 arXiv](https://arxiv.org/abs/2602.13022) • [📥 PDF](https://arxiv.org/pdf/2602.13022)

> We present a lidar-based pseudo-supervision method for training tree crown instance segmentation models without manual annotation.

</details>

<details>
<summary><b>26. Favia: Forensic Agent for Vulnerability-fix Identification and Analysis</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jingyue Li, Jiamou Sun, andstor

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12500) • [📄 arXiv](https://arxiv.org/abs/2602.12500) • [📥 PDF](https://arxiv.org/pdf/2602.12500)

**💻 Code:** [⭐ Code](https://github.com/andstor/agentic-security-patch-classification-replication-package)

> Favia is a forensic, agent-based framework that identifies vulnerability-fixing commits for disclosed CVEs by combining scalable candidate ranking with iterative, evidence-driven LLM reasoning.

</details>

<details>
<summary><b>27. scPilot: Large Language Model Reasoning Toward Automated Single-Cell Analysis and Discovery</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11609) • [📄 arXiv](https://arxiv.org/abs/2602.11609) • [📥 PDF](https://arxiv.org/pdf/2602.11609)

**💻 Code:** [⭐ Code](https://github.com/maitrix-org/scPilot)

> scPilot: Large Language Model Reasoning Toward Automated Single-Cell Analysis and Discovery

</details>

<details>
<summary><b>28. Steer2Edit: From Activation Steering to Component-Level Editing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.09870) • [📄 arXiv](https://arxiv.org/abs/2602.09870) • [📥 PDF](https://arxiv.org/pdf/2602.09870)

> Can steering vectors be turned into permanent, interpretable weight edits? STEER2EDIT converts steering signals into closed-form, component-level rank-1 updates on attention heads and MLP neurons — no fine-tuning required. Instead of globally shif...

</details>

<details>
<summary><b>29. GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.04315) • [📄 arXiv](https://arxiv.org/abs/2602.04315) • [📥 PDF](https://arxiv.org/pdf/2602.04315)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/GeneralVLA)

> https://aigeeksgroup.github.io/GeneralVLA

</details>

<details>
<summary><b>30. Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Xin Qiu, Risto Miikkulainen, Dibbla

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.03120) • [📄 arXiv](https://arxiv.org/abs/2602.03120) • [📥 PDF](https://arxiv.org/pdf/2602.03120)

**💻 Code:** [⭐ Code](https://github.com/dibbla/Quantized-Evolution-Strategies)

> We study an interesting question of whether it is possible to perform full-parameter fine-tuning on Large Language Models (LLMs) directly within the quantized space, effectively bypassing the need for high-precision weights and standard backpropag...

</details>

<details>
<summary><b>31. OpenLID-v3: Improving the Precision of Closely Related Language Identification -- An Experience Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13139) • [📄 arXiv](https://arxiv.org/abs/2602.13139) • [📥 PDF](https://arxiv.org/pdf/2602.13139)

**💻 Code:** [⭐ Code](https://github.com/hplt-project/openlid)

> Language identification model Supports 194 languages High performance (FastText-based) Fast and easy to use Fully transparent: training data and per-language performance openly available Used by HPLT

</details>

<details>
<summary><b>32. Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.07298) • [📄 arXiv](https://arxiv.org/abs/2602.07298) • [📥 PDF](https://arxiv.org/pdf/2602.07298)

> We present the first empirically validated scaling laws for LLMs in recommendation, enabled by a principled layered synthetic data framework that transforms noisy, biased user interaction logs into a high-quality pedagogical curriculum—demonstrati...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 32 |
| 📅 Today | [`2026-02-17.json`](data/daily/2026-02-17.json) | 32 |
| 📆 This Week | [`2026-W07.json`](data/weekly/2026-W07.json) | 73 |
| 🗓️ This Month | [`2026-02.json`](data/monthly/2026-02.json) | 768 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-02-17 | 32 | [View JSON](data/daily/2026-02-17.json) |
| 📄 2026-02-16 | 41 | [View JSON](data/daily/2026-02-16.json) |
| 📄 2026-02-15 | 41 | [View JSON](data/daily/2026-02-15.json) |
| 📄 2026-02-14 | 41 | [View JSON](data/daily/2026-02-14.json) |
| 📄 2026-02-13 | 47 | [View JSON](data/daily/2026-02-13.json) |
| 📄 2026-02-12 | 57 | [View JSON](data/daily/2026-02-12.json) |
| 📄 2026-02-11 | 58 | [View JSON](data/daily/2026-02-11.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W07 | 73 | [View JSON](data/weekly/2026-W07.json) |
| 📅 2026-W06 | 293 | [View JSON](data/weekly/2026-W06.json) |
| 📅 2026-W05 | 357 | [View JSON](data/weekly/2026-W05.json) |
| 📅 2026-W04 | 214 | [View JSON](data/weekly/2026-W04.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-02 | 768 | [View JSON](data/monthly/2026-02.json) |
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
