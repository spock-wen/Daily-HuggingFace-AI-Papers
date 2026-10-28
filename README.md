<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-40-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-9323+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">40</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">111</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1562</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">9323+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 28, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34283) • [📄 arXiv](https://arxiv.org/abs/2610.34283) • [📥 PDF](https://arxiv.org/pdf/2610.34283)

**💻 Code:** [⭐ Code](https://github.com/yihaohu0118/ChronoReplay) • [⭐ Code](https://github.com/huggingface)

> ChronoReplay is a training framework designed to improve the spatial reasoning capabilities of streaming vision-language models (VLMs). Existing spatial VLMs often specialize in specific answer formats, such as categorical spatial relations, metri...

</details>

<details>
<summary><b>2. The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36077) • [📄 arXiv](https://arxiv.org/abs/2610.36077) • [📥 PDF](https://arxiv.org/pdf/2610.36077)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The Trinity lets agents build their own training worlds around capabilities shared across tasks and recursively evolve reusable harnesses, gaining 26 points on average across 18 unseen benchmarks, including real-world robotics.

</details>

<details>
<summary><b>3. PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hanqing Wang, fairyang, zhoumo217, yilin-seu, zt0011

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37381) • [📄 arXiv](https://arxiv.org/abs/2610.37381) • [📥 PDF](https://arxiv.org/pdf/2610.37381)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>4. Hy-Nomas: Towards Free-form Interactive World Generation</b> ⭐ 274</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36729) • [📄 arXiv](https://arxiv.org/abs/2610.36729) • [📥 PDF](https://arxiv.org/pdf/2610.36729)

**💻 Code:** [⭐ Code](https://github.com/Tencent-Hunyuan/Hy-Nomas) • [⭐ Code](https://github.com/huggingface)

> We released the technical report of Hy-Nomas, a free-form interactive world generation model controlled by multi-turn text and camera inputs. Our model supports the exactly same features as Genie4, while Hy-Nomas is fully open-sourced model. Welco...

</details>

<details>
<summary><b>5. HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24520) • [📄 arXiv](https://arxiv.org/abs/2610.24520) • [📥 PDF](https://arxiv.org/pdf/2610.24520)

**💻 Code:** [⭐ Code](https://github.com/LUMIA-Group/habit-bench) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! I'm one of the authors of HABIT-Bench 👋 Can an agent learn your habits without being explicitly told—and know when not to apply them? Remembering a past choice is not enough. An agent needs to distinguish a recurring habit from a one-...

</details>

<details>
<summary><b>6. Memory Tax: Dissecting the Net Value of Agent Memory</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34073) • [📄 arXiv](https://arxiv.org/abs/2610.34073) • [📥 PDF](https://arxiv.org/pdf/2610.34073)

**💻 Code:** [⭐ Code](https://github.com/hexuan21/MemoryTax) • [⭐ Code](https://github.com/huggingface)

> Many agent memory systems can’t even beat a naive RAG? We conducted a comprehensive evaluation and find many underperform the naive RAG, even at higher cost. To better understand this, we introduce “Memory Tax”, see more in our paper.

</details>

<details>
<summary><b>7. Rollback: Experience Backtracking in World Models for Policy Improvement</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36068) • [📄 arXiv](https://arxiv.org/abs/2610.36068) • [📥 PDF](https://arxiv.org/pdf/2610.36068)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Rollback: Experience Backtracking in World Models for Policy Improvement

</details>

<details>
<summary><b>8. CodeCap-Bench: Can Code Serve as a Good Video Caption?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Junjie Zhao, Eric Tang, Yifan Xu, Jiafu Tang, DogNeverSleep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37341) • [📄 arXiv](https://arxiv.org/abs/2610.37341) • [📥 PDF](https://arxiv.org/pdf/2610.37341)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Video captioning aims to preserve visual information through compact descriptions, predominantly using natural language. However, precisely expressing fine-grained spatial structures and temporal dynamics in natural language often leads to lengthy...

</details>

<details>
<summary><b>9. Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37662) • [📄 arXiv](https://arxiv.org/abs/2610.37662) • [📥 PDF](https://arxiv.org/pdf/2610.37662)

**💻 Code:** [⭐ Code](https://github.com/hustvl/FVQ) • [⭐ Code](https://github.com/huggingface)

> This paper investigates whether discrete visual tokens can preserve semantic information as effectively as continuous representations. It shows that reconstruction error is an unreliable indicator of multimodal understanding and identifies effecti...

</details>

<details>
<summary><b>10. ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37666) • [📄 arXiv](https://arxiv.org/abs/2610.37666) • [📥 PDF](https://arxiv.org/pdf/2610.37666)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavi...

</details>

<details>
<summary><b>11. Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.32046) • [📄 arXiv](https://arxiv.org/abs/2610.32046) • [📥 PDF](https://arxiv.org/pdf/2610.32046)

**💻 Code:** [⭐ Code](https://github.com/yepengliu/TTME) • [⭐ Code](https://github.com/huggingface)

> Recent test-time training (TTT) frameworks have enabled open-weight large language models (LLMs) to outperform inference-only frameworks powered by frontier models on scientific discovery tasks. However, TTT introduces additional computational cos...

</details>

<details>
<summary><b>12. VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuzhe Chen, Xuyang Ma, Lele Yang, Wenbin Xu, Muxi Diao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35864) • [📄 arXiv](https://arxiv.org/abs/2610.35864) • [📥 PDF](https://arxiv.org/pdf/2610.35864)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🎬 VibeVideoBench: Can AI agents make a finished video, entirely with code? Agents writing code to make videos is a new way to generate video 💡: multimodal agents write code to render every frame and synthesize every sound, so formulas, charts and ...

</details>

<details>
<summary><b>13. LociArt: A Unified Paradigm for Free-Style Local Video Stylization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36456) • [📄 arXiv](https://arxiv.org/abs/2610.36456) • [📥 PDF](https://arxiv.org/pdf/2610.36456)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A very interesting work on controllable video stylization. LociArt unifies region selection and style specification through polar style-aware masks, while its geometry-aware conditioning helps preserve boundaries and non-target content. The abilit...

</details>

<details>
<summary><b>14. Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37037) • [📄 arXiv](https://arxiv.org/abs/2610.37037) • [📥 PDF](https://arxiv.org/pdf/2610.37037)

**💻 Code:** [⭐ Code](https://github.com/inclusionAI/Zooming-without-Zooming-v2) • [⭐ Code](https://github.com/huggingface)

> Recent multimodal models struggle with tasks that require connecting visual evidence across objects, images, and interactions, while collecting targeted supervision remains costly. We present Zooming-without-Zooming-v2 (ZwZ2) , a family of 4B/9B/2...

</details>

<details>
<summary><b>15. MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video Matting</b> ⭐ 54</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35724) • [📄 arXiv](https://arxiv.org/abs/2610.35724) • [📥 PDF](https://arxiv.org/pdf/2610.35724)

**💻 Code:** [⭐ Code](https://github.com/Shuyun-Wang/MatAnyone-E) • [⭐ Code](https://github.com/huggingface)

> Meet MatAnyone-E: high-quality video matting, much faster. ✂️ Compared with MatAnyone 2 at 4K: ⚡ ~7.4× faster inference 💾 Just 7.6% of the peak GPU memory ✨ Comparable matting quality Runs at 73 FPS at 1080p and 29 FPS at 4K on a single NVIDIA H20...

</details>

<details>
<summary><b>16. RSI Arena: Towards Recursive Self-Improvement with Human Feedback</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33624) • [📄 arXiv](https://arxiv.org/abs/2610.33624) • [📥 PDF](https://arxiv.org/pdf/2610.33624)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as train...

</details>

<details>
<summary><b>17. Channel Selection for Mixture-of-Experts Decoding Needs No Calibration Data</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37386) • [📄 arXiv](https://arxiv.org/abs/2610.37386) • [📥 PDF](https://arxiv.org/pdf/2610.37386)

**💻 Code:** [⭐ Code](https://github.com/AidenGeunGeun/calibration-free-moe) • [⭐ Code](https://github.com/huggingface)

> Activation pruning is a really big issue with slow-memory GPUs such as DGX Spark! Here is the GitHub: 😀 https://github.com/AidenGeunGeun/calibration-free-moe

</details>

<details>
<summary><b>18. Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35439) • [📄 arXiv](https://arxiv.org/abs/2610.35439v1) • [📥 PDF](https://arxiv.org/pdf/2610.35439)

**💻 Code:** [⭐ Code](https://github.com/YinsongYan/Omni-InteractScope) • [⭐ Code](https://github.com/huggingface)

> Introduce our latest work on interaction intelligence : Omni-InteractScope , a comprehensive benchmark for proactive and agentic interaction that connects omnimodal inputs , contextual triggers , and diverse response types . The code and data are ...

</details>

<details>
<summary><b>19. RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36791) • [📄 arXiv](https://arxiv.org/abs/2610.36791) • [📥 PDF](https://arxiv.org/pdf/2610.36791)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/RynnWorld-Latent) • [⭐ Code](https://github.com/huggingface)

> Our main contributions are as follows: We present RynnWorld-Latent, a text-free, latent-action-conditioned video world model, which uses frozen RynnLAM descriptors as a shared conditioning interface for learning visual dynamics from human interact...

</details>

<details>
<summary><b>20. Cross-modal Steering Vectors Exist Across Both Image and Text Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36269) • [📄 arXiv](https://arxiv.org/abs/2610.36269) • [📥 PDF](https://arxiv.org/pdf/2610.36269)

**💻 Code:** [⭐ Code](https://github.com/saintsauceee/cross-modal-steering) • [⭐ Code](https://github.com/huggingface)

> Cross-modal steering vectors transfer zero-shot in both directions 🖼️ ↔️ 📝 A steering vector extracted entirely from one modality can steer generation both within that modality and, without any adaptation, in the other This is exciting evidence fo...

</details>

<details>
<summary><b>21. What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents</b> ⭐ 34</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34491) • [📄 arXiv](https://arxiv.org/abs/2610.34491) • [📥 PDF](https://arxiv.org/pdf/2610.34491)

**💻 Code:** [⭐ Code](https://github.com/KaiserWhoLearns/ReasoningEffortLLM) • [⭐ Code](https://github.com/huggingface)

> Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will ...

</details>

<details>
<summary><b>22. The Lexical Imprint of Pre-training Data</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.10657) • [📄 arXiv](https://arxiv.org/abs/2602.10657) • [📥 PDF](https://arxiv.org/pdf/2602.10657)

**💻 Code:** [⭐ Code](https://github.com/penpaperkeycode/lexical-imprint) • [⭐ Code](https://github.com/huggingface)

> 🎯 What traces does pre-training data leave on a language model? We've just arXived our NeurIPS 2026 paper, The Lexical Imprint of Pre-training Data! In this work, we explore how pre-training data shapes zero-shot behavior through word-level unigra...

</details>

<details>
<summary><b>23. Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37255) • [📄 arXiv](https://arxiv.org/abs/2610.37255) • [📥 PDF](https://arxiv.org/pdf/2610.37255)

**💻 Code:** [⭐ Code](https://github.com/2020-qqtcg/HRP) • [⭐ Code](https://github.com/huggingface)

> A better agent setup can initially make a model perform worse. We show that models learn preferences tied to the prompts and tools they train with. Our framework separates a setup’s potential from how well the model uses it, helping predict when a...

</details>

<details>
<summary><b>24. Timestral</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37585) • [📄 arXiv](https://arxiv.org/abs/2610.37585) • [📥 PDF](https://arxiv.org/pdf/2610.37585)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>25. OvisOCR3 Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.33066) • [📄 arXiv](https://arxiv.org/abs/2610.33066) • [📥 PDF](https://arxiv.org/pdf/2610.33066)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce OvisOCR3, a compact 0.8B model unifying document parsing, general OCR, key information extraction, document figure captioning, and cross-page table reconstruction. Model weights and inference examples are publicly available, and we we...

</details>

<details>
<summary><b>26. Can LLMs Uncover Hidden Physical Laws through Free Exploration?</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Ying-Cong Chen, Xander Xu, Wen Wang, YZCS

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37649) • [📄 arXiv](https://arxiv.org/abs/2610.37649) • [📥 PDF](https://arxiv.org/pdf/2610.37649)

**💻 Code:** [⭐ Code](https://github.com/EnVision-Research/LongChang) • [⭐ Code](https://github.com/huggingface)

> LongChang explores whether LLMs can autonomously discover hidden physical laws. Visit our project page for all experimental results and interactive experiments. If you find LongChang interesting, we’d appreciate an upvote and a star on GitHub!

</details>

<details>
<summary><b>27. On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Chaim Baskin, Avi Mendelson, ElironRahimi, EliezerS

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22543) • [📄 arXiv](https://arxiv.org/abs/2610.22543) • [📥 PDF](https://arxiv.org/pdf/2610.22543)

**💻 Code:** [⭐ Code](https://github.com/Eliezer318/SPOT-dLLM) • [⭐ Code](https://github.com/huggingface)

> Diffusion LMs already know most of the next tokens. What they miss is the order. SPOT learns it. Exact decoding of a diffusion LM fills one masked position per pass. The model's predictions from the previous pass already give the right token at ov...

</details>

<details>
<summary><b>28. Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34674) • [📄 arXiv](https://arxiv.org/abs/2610.34674%7D) • [📥 PDF](https://arxiv.org/pdf/2610.34674)

**💻 Code:** [⭐ Code](https://github.com/OSMA-Bench/OSMA-Bench) • [⭐ Code](https://github.com/huggingface)

> Do household robots move more cautiously around riskier obstacles? OSMA-Bench evaluates whether VLM- and VLA-based policies adjust their clearance, speed, and smoothness according to an obstacle’s safety relevance. We find that recognizing risk do...

</details>

<details>
<summary><b>29. Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Yi Lin, Jingjia Huang, Sili Chen, Yanwei Li, Rui Yang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36022) • [📄 arXiv](https://arxiv.org/abs/2610.36022) • [📥 PDF](https://arxiv.org/pdf/2610.36022)

**💻 Code:** [⭐ Code](https://github.com/hku-sail/GeoUG) • [⭐ Code](https://github.com/huggingface)

> Image and video generators can produce spatially consistent visual content, but how to use this capability to improve spatial understanding remains underexplored. We study this problem from two perspectives: geometric supervision during training a...

</details>

<details>
<summary><b>30. Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.36466) • [📄 arXiv](https://arxiv.org/abs/2610.36466) • [📥 PDF](https://arxiv.org/pdf/2610.36466)

**💻 Code:** [⭐ Code](https://github.com/NVlabs/Nemotron-Labs-Diffusion-Uni) • [⭐ Code](https://github.com/huggingface)

> Unified Understanding and Generation DLLM with On Policy Distillation

</details>

<details>
<summary><b>31. Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Khalil El Khammar, Abderrahman Sghir, Imad Charradi, ImAnouar1

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37624) • [📄 arXiv](https://arxiv.org/abs/2610.37624) • [📥 PDF](https://arxiv.org/pdf/2610.37624)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Can remembering more information actually make an LLM group worse at making decisions? In our new preprint, Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions , we investigate a fundamental question in multi-agent AI: what infor...

</details>

<details>
<summary><b>32. Vision-Language-Action or World-Action? Just Action Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Toshihiko Yamasaki, Runyi Li, Lang Huang, y0urOy

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37219) • [📄 arXiv](https://arxiv.org/abs/2610.37219) • [📥 PDF](https://arxiv.org/pdf/2610.37219)

**💻 Code:** [⭐ Code](https://github.com/y0urOy/JAM) • [⭐ Code](https://github.com/huggingface)

> We introduce Just Action Models (JAM): action policies trained with a foresight loss on frozen features of recorded future observations, without image or video generation during training or inference. JAM supports generator, vision-language and se...

</details>

<details>
<summary><b>33. SearchHorizonBench: A Benchmark for Search Value in AI Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34714) • [📄 arXiv](https://arxiv.org/abs/2610.34714) • [📥 PDF](https://arxiv.org/pdf/2610.34714)

**💻 Code:** [⭐ Code](https://github.com/EthanNing/SearchHorizonBench) • [⭐ Code](https://github.com/huggingface)

> A Benchmark for Search Value in AI Agents

</details>

<details>
<summary><b>34. MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sherry Yang, Li Erran Li, Hejia Geng, Han Wang, Brian Ko

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.37175) • [📄 arXiv](https://arxiv.org/abs/2610.37175) • [📥 PDF](https://arxiv.org/pdf/2610.37175)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>35. Harness-Model Collaboration for Long-Horizon Continual Learning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haofei Zhang, Xueshu Chen, Yan Wang, Zhizhi Peng, bizhen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34724) • [📄 arXiv](https://arxiv.org/abs/2610.34724) • [📥 PDF](https://arxiv.org/pdf/2610.34724)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We propose HaMo, a Harness-Model collaborative framework for continual learning in long-horizon agents. Our method separates adaptation into two tightly coupled processes. At the harness level, each trajectory is distilled into a compact experienc...

</details>

<details>
<summary><b>36. Multiscale Policy Optimization for Long-Horizon LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35013) • [📄 arXiv](https://arxiv.org/abs/2610.35013) • [📥 PDF](https://arxiv.org/pdf/2610.35013)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share Multiscale Policy Optimization (MPO), a reinforcement learning framework designed for long-horizon LLM agents! We observe that critic values vary primarily across assistant turns, motivating turn-level optimization with fine-grain...

</details>

<details>
<summary><b>37. Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Weiyang Jin, Yue Su, Zihan Shao, Siyu Chen, xjxyys

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26030) • [📄 arXiv](https://arxiv.org/abs/2610.26030) • [📥 PDF](https://arxiv.org/pdf/2610.26030)

**💻 Code:** [⭐ Code](https://github.com/xjxyys/Truncate-or-Not) • [⭐ Code](https://github.com/huggingface)

> 🏠 Project page (with an interactive loop-setting explorer): https://xjxyys.github.io/truncate-or-not/ 💻 Code: https://github.com/xjxyys/Truncate-or-Not

</details>

<details>
<summary><b>38. h1: A Taste of the Bitter Lesson in Automated Theorem Proving</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.35962) • [📄 arXiv](https://arxiv.org/abs/2610.35962) • [📥 PDF](https://arxiv.org/pdf/2610.35962)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> While progress in informal mathematics has come largely from scaling the chain-of-thought and agentic reasoning of frontier language models, formal theorem proving has increasingly relied on human-designed workflows around these models, such as pl...

</details>

<details>
<summary><b>39. PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Xinran Liu, Minghong Cai, Chen Tang, Yilei Jiang, Jinyuan Hu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.34921) • [📄 arXiv](https://arxiv.org/abs/2610.34921) • [📥 PDF](https://arxiv.org/pdf/2610.34921)

**💻 Code:** [⭐ Code](https://github.com/yelonhu/PhysEvolve) • [⭐ Code](https://github.com/huggingface)

> Physical reasoning underpins how embodied systems understand and act in the physical world, yet vision-language models (VLMs) remain unreliable on questions about dynamics and physical causality. Progress is critically constrained by the scarcity ...

</details>

<details>
<summary><b>40. MoveBench: A Rubric-Based Benchmark for Evaluating Large Language Models in Sports and Health Coaching</b> ⭐ 17</summary>

<br/>

**👥 Authors:** Chengying Gu, Pan Ding, Jingling Wang, Jiang Bian, SatoSakula

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26185) • [📄 arXiv](https://arxiv.org/abs/2610.26185) • [📥 PDF](https://arxiv.org/pdf/2610.26185)

**💻 Code:** [⭐ Code](https://github.com/Keep-Tech/MoveBench) • [⭐ Code](https://github.com/huggingface)

> Nice to have benchamark with open source dataset

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 40 |
| 📅 Today | [`2026-10-28.json`](data/daily/2026-10-28.json) | 40 |
| 📆 This Week | [`2026-W43.json`](data/weekly/2026-W43.json) | 111 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1562 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-28 | 40 | [View JSON](data/daily/2026-10-28.json) |
| 📄 2026-10-27 | 43 | [View JSON](data/daily/2026-10-27.json) |
| 📄 2026-10-26 | 28 | [View JSON](data/daily/2026-10-26.json) |
| 📄 2026-10-25 | 49 | [View JSON](data/daily/2026-10-25.json) |
| 📄 2026-10-24 | 50 | [View JSON](data/daily/2026-10-24.json) |
| 📄 2026-10-23 | 36 | [View JSON](data/daily/2026-10-23.json) |
| 📄 2026-10-22 | 41 | [View JSON](data/daily/2026-10-22.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W43 | 111 | [View JSON](data/weekly/2026-W43.json) |
| 📅 2026-W42 | 334 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1562 | [View JSON](data/monthly/2026-10.json) |
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
