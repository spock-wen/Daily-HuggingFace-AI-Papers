<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-24-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6211+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">24</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">38</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">523</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6211+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 28, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Kimi K3: Open Frontier Intelligence</b> ⭐ 2.58k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24653) • [📄 arXiv](https://arxiv.org/abs/2607.24653) • [📥 PDF](https://arxiv.org/pdf/2607.24653)

**💻 Code:** [⭐ Code](https://github.com/MoonshotAI/Kimi-K3) • [⭐ Code](https://github.com/huggingface)

> great one

</details>

<details>
<summary><b>2. JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents</b> ⭐ 20</summary>

<br/>

**👥 Authors:** Chenxin Li, Biqiang Li, Zhaohu Xing, Zixu Lin, Yunlong Lin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23588) • [📄 arXiv](https://arxiv.org/abs/2607.23588) • [📥 PDF](https://arxiv.org/pdf/2607.23588)

**💻 Code:** [⭐ Code](https://github.com/LYL1015/JarvisHub) • [⭐ Code](https://github.com/huggingface)

> Our new project, JarvisHub, is now live and open source! 🥳 Unlike one-shot prompt-based generation tools, linear chatbot agents, or node-based workflows that require manual setup, JarvisHub is a Canvas-Native Agent Harness for long-horizon multimo...

</details>

<details>
<summary><b>3. Progress Reward Modeling for Robotic Learning: A Comprehensive Survey</b> ⭐ 35</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.21655) • [📄 arXiv](https://arxiv.org/abs/2607.21655) • [📥 PDF](https://arxiv.org/pdf/2607.21655)

**💻 Code:** [⭐ Code](https://github.com/sterzhang/Awesome-Progress-Models) • [⭐ Code](https://github.com/huggingface)

> Welcome any update of this direction! Welcome PR and discussion! Our repo: https://github.com/sterzhang/Awesome-Progress-Models

</details>

<details>
<summary><b>4. From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chunji Lv, Shuaiyu Zhou, Zixin Song, Jiangwang Chen, Junlin Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24280) • [📄 arXiv](https://arxiv.org/abs/2607.24280) • [📥 PDF](https://arxiv.org/pdf/2607.24280)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Agentic search enables large language models to solve knowledge-intensive tasks by interleaving multi-step reasoning with retrieval, yet optimizing this with outcome-based reinforcement learning (RL) provides only sparse supervision. Knowledge dis...

</details>

<details>
<summary><b>5. StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.22798) • [📄 arXiv](https://arxiv.org/abs/2607.22798) • [📥 PDF](https://arxiv.org/pdf/2607.22798)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚨 We just set a new SOTA on OSWorld 2.0! ⭐️ And we did it by making our computer-use agent look less, not more. Everyone's racing the same way: better vision, sharper screen-reading, more pixels. We went the opposite direction. StateAct barely loo...

</details>

<details>
<summary><b>6. Data Pyramid for Embodied Manipulation</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24744) • [📄 arXiv](https://arxiv.org/abs/2607.24744) • [📥 PDF](https://arxiv.org/pdf/2607.24744)

**💻 Code:** [⭐ Code](https://github.com/worldbench/awesome-embodied-data-pyramid) • [⭐ Code](https://github.com/huggingface)

> Multimodal foundation models learned to see and reason from Internet-scale image-text data. Embodied AI, however, requires a fundamentally different ingredient: interaction data that couples perception, physical states, and actions. But today’s em...

</details>

<details>
<summary><b>7. Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haozhe Liu, Tian Ye, Junsong Chen, Yitong Li, Haopeng Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24027) • [📄 arXiv](https://arxiv.org/abs/2607.24027) • [📥 PDF](https://arxiv.org/pdf/2607.24027)

**💻 Code:** [⭐ Code](https://github.com/NVlabs/Sana/tree/sol-engine) • [⭐ Code](https://github.com/huggingface)

> 🚀 Sol-Attn is a training-free sparse attention method that accelerates video generation while better preserving quality. Sol-Attn unifies dynamic routing, sparse computation, and approximate correction in a single online-softmax pass: • On-the-fly...

</details>

<details>
<summary><b>8. Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jinpeng Yu, Fangtai Wu, Haozhong Xiong, Haozhe Wang, Bingnan Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24731) • [📄 arXiv](https://arxiv.org/abs/2607.24731) • [📥 PDF](https://arxiv.org/pdf/2607.24731)

**💻 Code:** [⭐ Code](https://github.com/rethinking-cfg-opd/Rethinking-CFG-OPD) • [⭐ Code](https://github.com/huggingface)

> What happens when on-policy diffusion distillation meets classifier-free guidance? A natural approach is to match the teacher’s and student’s guided predictions. But this seemingly reasonable objective hides a subtle ambiguity: errors from the pos...

</details>

<details>
<summary><b>9. OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for Joint Generation</b> ⭐ 31</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23855) • [📄 arXiv](https://arxiv.org/abs/2607.23855) • [📥 PDF](https://arxiv.org/pdf/2607.23855)

**💻 Code:** [⭐ Code](https://github.com/OpenMOSS/OmniVAE) • [⭐ Code](https://github.com/huggingface)

> Why do we need joint audio-video representations? The same real-world event is often expressed through both sound and vision, but each modality also contains unique information. Ideally, a multimodal latent space should capture both shared event s...

</details>

<details>
<summary><b>10. The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24720) • [📄 arXiv](https://arxiv.org/abs/2607.24720) • [📥 PDF](https://arxiv.org/pdf/2607.24720)

**💻 Code:** [⭐ Code](https://github.com/Quester-one/PlanPhysCode) • [⭐ Code](https://github.com/huggingface)

> Homepage: https://quester-one.github.io/PlanPhysWebsite/ GitHub: https://github.com/Quester-one/PlanPhysCode Hugging Face Model: https://huggingface.co/MultimodalAgent/TianyiMen_PlanPhys_Models Hugging Face Dataset: https://huggingface.co/datasets...

</details>

<details>
<summary><b>11. Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23518) • [📄 arXiv](https://arxiv.org/abs/2607.23518) • [📥 PDF](https://arxiv.org/pdf/2607.23518)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/caohengyuan/Chamaileon)

> Most protein binder design methods assume a single target in a single structural state, while many real-world applications require one sequence to function across multiple conformations or targets. We introduce Chamaileon, a unified framework for ...

</details>

<details>
<summary><b>12. Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.21694) • [📄 arXiv](https://arxiv.org/abs/2607.21694) • [📥 PDF](https://arxiv.org/pdf/2607.21694)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🔍 Overview Oxygen-TryOn is a unified, open-source foundation model for any-item virtual try-on . Given one or more reference items — provided either as clean product shots or as in-the-wild photos of someone already wearing them — together with a ...

</details>

<details>
<summary><b>13. DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dongling Xiao, Ruiqi Lu, Qianle Wang, Zhongbin Guo, Jiahao Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24516) • [📄 arXiv](https://arxiv.org/abs/2607.24516) • [📥 PDF](https://arxiv.org/pdf/2607.24516)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Welcome everyone to exchange and discuss!

</details>

<details>
<summary><b>14. dRAE: Representation Autoencoder with Hyper-Spherical Codes</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.22148) • [📄 arXiv](https://arxiv.org/abs/2607.22148) • [📥 PDF](https://arxiv.org/pdf/2607.22148)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/martian422/dRAE)

> We propose dRAE, a visual tokenizer built on Hyper-Spherical Quantization (HSQ). By assigning codes via cosine similarity and updating embeddings in tangent space, HSQ aligns the quantization objective with the intrinsic geometry of pre-trained vi...

</details>

<details>
<summary><b>15. ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24743) • [📄 arXiv](https://arxiv.org/abs/2607.24743) • [📥 PDF](https://arxiv.org/pdf/2607.24743)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/ClinFusion) • [⭐ Code](https://github.com/huggingface)

> Code: https://github.com/alibaba-damo-academy/ClinFusion Models: https://huggingface.co/collections/Alibaba-DAMO-Academy/clinfusion

</details>

<details>
<summary><b>16. GNM Head: A Generative aNthropometric Model of the human head</b> ⭐ 1.22k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23687) • [📄 arXiv](https://arxiv.org/abs/2607.23687) • [📥 PDF](https://arxiv.org/pdf/2607.23687)

**💻 Code:** [⭐ Code](https://github.com/google/GNM) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. FilmBench: A Film-Grade Benchmark for Cinematic Video Generation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Fei Ding, Hong Qi, Guangzheng Hu, Niantong Li, Shengyi Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24241) • [📄 arXiv](https://arxiv.org/abs/2607.24241) • [📥 PDF](https://arxiv.org/pdf/2607.24241)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Neo-yk/FilmOps)

> No abstract available.

</details>

<details>
<summary><b>18. A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens, Bit-Exact, Forever</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23806) • [📄 arXiv](https://arxiv.org/abs/2607.23806) • [📥 PDF](https://arxiv.org/pdf/2607.23806)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> More information? Just ask

</details>

<details>
<summary><b>19. Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.22098) • [📄 arXiv](https://arxiv.org/abs/2607.22098) • [📥 PDF](https://arxiv.org/pdf/2607.22098)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 👋 Hi Hugging Face community! We’re excited to share our new paper: 🧠 Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models Large reasoning models generate long chains of thought, but are all reasoning...

</details>

<details>
<summary><b>20. Codifying the Judge: Scalable Evaluation via Program Distillation</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.22561) • [📄 arXiv](https://arxiv.org/abs/2607.22561) • [📥 PDF](https://arxiv.org/pdf/2607.22561)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SprocketLab/PAJAMA)

> LLM-as-a-judge is now everywhere for automated evaluation. But it can be slow, expensive, and opaque. What if we ask the judge for its rubric once, and execute that logic as a program? Introducing PAJAMA—a new hybrid evaluation system that pushes ...

</details>

<details>
<summary><b>21. Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yu Xiao, Yao Zhang, Zhuchenyang Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.24651) • [📄 arXiv](https://arxiv.org/abs/2607.24651) • [📥 PDF](https://arxiv.org/pdf/2607.24651)

**💻 Code:** [⭐ Code](https://github.com/Ryenhails/quote-and-retrieve) • [⭐ Code](https://github.com/huggingface)

> 📌 What is this? We introduce a Language Interface for Visual Evidence Attribution—an alternative to coordinate-based bounding box prediction in multi-page visual document understanding. Instead of outputting coordinates, our model generates verbat...

</details>

<details>
<summary><b>22. IndicTalk: A Large-Scale Persona-Based Multilingual Conversational Corpus for Indic Languages</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23242) • [📄 arXiv](https://arxiv.org/abs/2607.23242) • [📥 PDF](https://arxiv.org/pdf/2607.23242)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large Language Models (LLMs) have transformed conversational AI, yet high-quality multilingual code-mixed dialogue resources remain scarce, particularly for Indic languages where speakers naturally alternate between English and their native langua...

</details>

<details>
<summary><b>23. Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.21936) • [📄 arXiv](https://arxiv.org/abs/2607.21936) • [📥 PDF](https://arxiv.org/pdf/2607.21936)

**💻 Code:** [⭐ Code](https://github.com/EvelynKimm/ARI) • [⭐ Code](https://github.com/huggingface)

> Historical documents act as invaluable knowledge archives but often suffer from illegibility due to physical deterioration and damage. While existing restoration methods based on masked language modeling effectively utilize local context, they str...

</details>

<details>
<summary><b>24. DriveDNA: A Large-Scale Multimodal Naturalistic Driving Dataset and Benchmark for Driving Style Identification</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.23822) • [📄 arXiv](https://arxiv.org/abs/2607.23822) • [📥 PDF](https://arxiv.org/pdf/2607.23822)

**💻 Code:** [⭐ Code](https://github.com/WangYuHang-cmd/DriveDNA) • [⭐ Code](https://github.com/huggingface)

> Hi, author here 👋 TL;DR: Recognizing a driver is not the same as capturing driving style. DriveDNA is a large-scale naturalistic driving benchmark (465 drivers, 115 vehicle models, 975 h of human-controlled driving with CAN + forward video) built ...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 24 |
| 📅 Today | [`2026-07-28.json`](data/daily/2026-07-28.json) | 24 |
| 📆 This Week | [`2026-W30.json`](data/weekly/2026-W30.json) | 38 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 523 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-28 | 24 | [View JSON](data/daily/2026-07-28.json) |
| 📄 2026-07-27 | 14 | [View JSON](data/daily/2026-07-27.json) |
| 📄 2026-07-26 | 22 | [View JSON](data/daily/2026-07-26.json) |
| 📄 2026-07-25 | 22 | [View JSON](data/daily/2026-07-25.json) |
| 📄 2026-07-24 | 16 | [View JSON](data/daily/2026-07-24.json) |
| 📄 2026-07-23 | 14 | [View JSON](data/daily/2026-07-23.json) |
| 📄 2026-07-22 | 19 | [View JSON](data/daily/2026-07-22.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W30 | 38 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |
| 📅 2026-W27 | 133 | [View JSON](data/weekly/2026-W27.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 523 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |

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
