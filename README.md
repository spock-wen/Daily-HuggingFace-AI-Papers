<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-55-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8987+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">55</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">109</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1226</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8987+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 20, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Learning from Fleet Experience: A Collective Learning Paradigm for Robots</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chao Yu, sundrops, chenrh, XuXin2003, AdamCYH

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25736) • [📄 arXiv](https://arxiv.org/abs/2610.25736) • [📥 PDF](https://arxiv.org/pdf/2610.25736)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Collective Experience Learning (CEL), a scalable paradigm in which deployed robots share their execution experience to improve a common policy. Its algorithm, FERT, uses failure contexts to retrieve relevant successful segments from t...

</details>

<details>
<summary><b>2. MemT-1.0: Towards Memory-Native Evolution</b> ⭐ 146</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26825) • [📄 arXiv](https://arxiv.org/abs/2610.26825) • [📥 PDF](https://arxiv.org/pdf/2610.26825)

**💻 Code:** [⭐ Code](https://github.com/MemTensor/MemT-1.0) • [⭐ Code](https://github.com/huggingface)

> Welcome, everyone! We’d love for you to try it out and share your feedback!

</details>

<details>
<summary><b>3. EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26625) • [📄 arXiv](https://arxiv.org/abs/2610.26625) • [📥 PDF](https://arxiv.org/pdf/2610.26625)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ropedia/EgoXperience)

> The SOTA mocap pipeline and model.

</details>

<details>
<summary><b>4. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory</b> ⭐ 18</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26860) • [📄 arXiv](https://arxiv.org/abs/2610.26860) • [📥 PDF](https://arxiv.org/pdf/2610.26860)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/uclanlp/OpenVLHarness)

> OpenVLHarness is a training-free harness that lets multimodal models combine perception, web search and Python computation, and keeps every piece of tool evidence readable and reusable across reasoning steps.

</details>

<details>
<summary><b>5. Holi-World: Building Holistic World Intelligence from Human-Ego Experience</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26549) • [📄 arXiv](https://arxiv.org/abs/2610.26549) • [📥 PDF](https://arxiv.org/pdf/2610.26549)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Ropedia/holi-world)

> HOLI-WORLD, an integrated ecosystem connecting experience capture, world representation, automated data construction, model learning, and independent evaluation.

</details>

<details>
<summary><b>6. Scaling Parameter-Efficient Fine-Tuning for Brain Encoding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26802) • [📄 arXiv](https://arxiv.org/abs/2610.26802) • [📥 PDF](https://arxiv.org/pdf/2610.26802)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has...

</details>

<details>
<summary><b>7. ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Jia Shi, Zhongrui Yu, Jiawei Wang, Yuanhong Yu, Yangyihui

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25690) • [📄 arXiv](https://arxiv.org/abs/2610.25690) • [📥 PDF](https://arxiv.org/pdf/2610.25690)

**💻 Code:** [⭐ Code](https://github.com/MachEmbodied/ScaleNav) • [⭐ Code](https://github.com/huggingface)

> We are excited to share ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation . ScaleNav uses scalable Internet video pretraining to learn navigation priors from action-free egocentric videos. A unified world-acti...

</details>

<details>
<summary><b>8. SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Xiao Zhou, Cong Li, Heng Cui, Songhao Wu, Zhongxin Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26824) • [📄 arXiv](https://arxiv.org/abs/2610.26824) • [📥 PDF](https://arxiv.org/pdf/2610.26824)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/CentreChen/Spec-MRL)

> We find that the ordered, orthogonal structure of a spectral basis naturally aligns with MRL’s nested prefix design, providing a better space for organizing information. SpecMRL reorganizes the embedding space using a learned, parameter-derived sp...

</details>

<details>
<summary><b>9. Self-Evolving Coding Agents via Harness-Policy Optimization</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22791) • [📄 arXiv](https://arxiv.org/abs/2610.22791) • [📥 PDF](https://arxiv.org/pdf/2610.22791)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MSR-Orchard/Self-HPO)

> 🤩 Introducing Self-HPO: let the coding agent improve its own harness, then train a stronger policy model with the optimized harness, and repeat the process for recursive improvement! 💪 Self-evolving: no external model required 🎯 Harness search tar...

</details>

<details>
<summary><b>10. OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24087) • [📄 arXiv](https://arxiv.org/abs/2610.24087) • [📥 PDF](https://arxiv.org/pdf/2610.24087)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/NineAbyss/OR-License)

> 🚀OR-License benchmarks LLM agents as real-world OR practitioners using industry-derived optimization problems from $3.68M in commissioned projects, evaluating end-to-end OR problem solving. We evaluated 11 frontier LLMs and analyzed their performa...

</details>

<details>
<summary><b>11. MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25404) • [📄 arXiv](https://arxiv.org/abs/2610.25404) • [📥 PDF](https://arxiv.org/pdf/2610.25404)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/houyuanchen111/MT-Forcing)

> Introducing MT Forcing : towards stable and consistent multi-turn image editing with autoregressive diffusion. Image editing models often produce good results in a single turn, yet accumulate artifacts and lose previously established details over ...

</details>

<details>
<summary><b>12. CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Chunyang Li, Baixuan Xu, Jiaxin Bai, Yiming Du, Zhongwei Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24960) • [📄 arXiv](https://arxiv.org/abs/2610.24960) • [📥 PDF](https://arxiv.org/pdf/2610.24960)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKUST-KnowComp/CoworkEnv)

> How can we build training environments for AI coworkers that need to use tools, handle multi-turn interactions, and operate in changing workspaces? We introduce CoworkEnv, a framework that synthesizes executable environments for training these age...

</details>

<details>
<summary><b>13. AnyGoal: On World Model Generalization Beyond Expert Rollouts</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26844) • [📄 arXiv](https://arxiv.org/abs/2610.26844) • [📥 PDF](https://arxiv.org/pdf/2610.26844)

**💻 Code:** [⭐ Code](https://github.com/galilai-group/AnyGoal) • [⭐ Code](https://github.com/huggingface)

> 💡A compositional generalization suite for world model research. pip install anygoal and see how much your world model knows about the world! Project Page: https://hazel-heejeong-nam.github.io/anygoal/ github: https://github.com/galilai-group/AnyGo...

</details>

<details>
<summary><b>14. RoAR-VAE: Improving Latent Diffusability through Robust Prediction</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26216) • [📄 arXiv](https://arxiv.org/abs/2610.26216) • [📥 PDF](https://arxiv.org/pdf/2610.26216)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LeapLabTHU/RoAR-VAE)

> This project aims to develop an open VAE training recipe with performance comparable to FLUX.2-VAE. Revisiting REPA-E, we identify robust prediction as an effective regularization principle: requiring useful information to remain recoverable from ...

</details>

<details>
<summary><b>15. InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26853) • [📄 arXiv](https://arxiv.org/abs/2610.26853) • [📥 PDF](https://arxiv.org/pdf/2610.26853)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yichuanH/InfiniDream)

> Procedural generation plays a key role in synthetic data creation and game development, offering greater controllability, editability, and diversity than static mesh representations. However, VLM-based code generation often produces relatively sim...

</details>

<details>
<summary><b>16. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.06830) • [📄 arXiv](https://arxiv.org/abs/2610.06830) • [📥 PDF](https://arxiv.org/pdf/2610.06830)

**💻 Code:** [⭐ Code](https://github.com/ViktorAxelsen/MemPilot) • [⭐ Code](https://github.com/huggingface)

> Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessi...

</details>

<details>
<summary><b>17. RoboValue: A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models</b> ⭐ 13</summary>

<br/>

**👥 Authors:** Honghao Su, Zhengye Du, xiaojy, wzlllong, Shengbang0209

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26663) • [📄 arXiv](https://arxiv.org/abs/2610.26663) • [📥 PDF](https://arxiv.org/pdf/2610.26663)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RoboValue-Benchmark/RoboValue)

> We introduce RoboValue , a fine-grained sim-and-real benchmark for unified evaluation of robotic value models. It evaluates four complementary capabilities: task-state understanding, temporal progress monitoring, failure and recovery reasoning, an...

</details>

<details>
<summary><b>18. Kronecker Delta Rule for Long Context Linear Attention</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26834) • [📄 arXiv](https://arxiv.org/abs/2610.26834) • [📥 PDF](https://arxiv.org/pdf/2610.26834)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ✨ Meet KronLSTM, our new linear attention architecture! 📦 The code is compatible with FLA, so you can plug it right in. 🛠️ We’re also cooking up faster kernels 🔥⚡ Stay tuned!

</details>

<details>
<summary><b>19. Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26848) • [📄 arXiv](https://arxiv.org/abs/2610.26848) • [📥 PDF](https://arxiv.org/pdf/2610.26848)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> https://physrsi-eval.github.io/

</details>

<details>
<summary><b>20. Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26851) • [📄 arXiv](https://arxiv.org/abs/2610.26851) • [📥 PDF](https://arxiv.org/pdf/2610.26851)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/annchenn/Manga2Animate)

> Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its characters and art style, or feed manga pages directly i...

</details>

<details>
<summary><b>21. AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25950) • [📄 arXiv](https://arxiv.org/abs/2610.25950) • [📥 PDF](https://arxiv.org/pdf/2610.25950)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKUST-KnowComp/AdaExploreBench)

> We introduce AdaExploreBench, a benchmark of LLM agents for proactive exploration and test-time adaptation in evolving environments.

</details>

<details>
<summary><b>22. AffordanceWAM: Affordance-Aware Joint World-Action Modeling for Robot Manipulation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.22332) • [📄 arXiv](https://arxiv.org/abs/2609.22332) • [📥 PDF](https://arxiv.org/pdf/2609.22332)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Skywalker-yqz/AffordanceWAM)

> 🤔 Have egocentric human videos, but aren’t sure how to use them to train robots without robot action labels? We introduce AffordanceWAM, which uses affordances to connect human video learning with robot action generation. The idea is to learn whic...

</details>

<details>
<summary><b>23. Think Visually Across Space and Time: Grounded Reasoning for Video Segmentation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xin Li, Ming-Hsuan Yang, Guangming Lu, Deshui Miao, Junwei Wen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25090) • [📄 arXiv](https://arxiv.org/abs/2610.25090) • [📥 PDF](https://arxiv.org/pdf/2610.25090)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A spatiotemporally grounded form of Video CoT that organizes query-relevant observations into a chronological reasoning chain.

</details>

<details>
<summary><b>24. DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26081) • [📄 arXiv](https://arxiv.org/abs/2610.26081) • [📥 PDF](https://arxiv.org/pdf/2610.26081)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A Benchmark and Source-Anchored Flow for Video Overlay Removal

</details>

<details>
<summary><b>25. Evidence-First Agentic Verification</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17724) • [📄 arXiv](https://arxiv.org/abs/2610.17724) • [📥 PDF](https://arxiv.org/pdf/2610.17724)

**💻 Code:** [⭐ Code](https://github.com/rsanayei/Sauron) • [⭐ Code](https://github.com/huggingface)

> When agent evaluations become post-training rewards, unreliable verdicts can reinforce failures. We introduce Sauron, an evidence-first agentic verifier that scales long-horizon evaluation through shared-evidence clustering, targeted trace/state q...

</details>

<details>
<summary><b>26. HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Honglin Lin, Yukuo Cen, ZhiYuan Feng, Zhuoshi Pan, Junrulu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26770) • [📄 arXiv](https://arxiv.org/abs/2610.26770) • [📥 PDF](https://arxiv.org/pdf/2610.26770)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/pzs19/HarnessPro)

> HarnessPro recursively improves agent harnesses to achieve better task performance at lower execution cost, offering multiple performance–cost trade-offs for different deployment budgets.

</details>

<details>
<summary><b>27. BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References</b> ⭐ 156</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23986) • [📄 arXiv](https://arxiv.org/abs/2610.23986) • [📥 PDF](https://arxiv.org/pdf/2610.23986)

**💻 Code:** [⭐ Code](https://github.com/QwenLM/BlenderWorld) • [⭐ Code](https://github.com/huggingface)

> 🎉 Excited to share our latest work from the Qwen team!  Visual agents can already build websites, design posters, and create slide decks. But how well can they handle 3D creation? This demands spatial reasoning, tool use, and iterative visual feed...

</details>

<details>
<summary><b>28. State World Models: Execute the Rules, Generate the Pixels</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26811) • [📄 arXiv](https://arxiv.org/abs/2610.26811) • [📥 PDF](https://arxiv.org/pdf/2610.26811)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Zhangyr2022/StateWorldModel)

> HF Dataset: https://huggingface.co/datasets/Louis0411/StateWorldModel Modelscope Dataset: https://modelscope.cn/datasets/Louis0411/StateWorldModel

</details>

<details>
<summary><b>29. Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Jian Zhang, Ruochong Zheng, Yu Yan, Yian Zhao, HongcanGuo04

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25666) • [📄 arXiv](https://arxiv.org/abs/2610.25666) • [📥 PDF](https://arxiv.org/pdf/2610.25666)

**💻 Code:** [⭐ Code](https://github.com/zhao-yian/Frechet_Forcing) • [⭐ Code](https://github.com/huggingface)

> Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips

</details>

<details>
<summary><b>30. Harnessing Textual Refusal Directions for Multimodal Safety</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.31876) • [📄 arXiv](https://arxiv.org/abs/2606.31876) • [📥 PDF](https://arxiv.org/pdf/2606.31876)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Moreno98/MARS)

> TLDR; MARS leverages textual refusal directions to selectively steer model activations towards refusal when the model’s internal representations indicate potential risk, regardless of modality. The approach is training-free, requires no multimodal...

</details>

<details>
<summary><b>31. Interlock: From Local Correctness to Task Completion in Long-Horizon Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19686) • [📄 arXiv](https://arxiv.org/abs/2610.19686) • [📥 PDF](https://arxiv.org/pdf/2610.19686)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Interlock: From Local Correctness to Task Completion in Long-Horizon Agents

</details>

<details>
<summary><b>32. Learning to Discriminate Scene Structures Makes Self-Supervised Depth Learning Scalable</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23600) • [📄 arXiv](https://arxiv.org/abs/2610.23600) • [📥 PDF](https://arxiv.org/pdf/2610.23600)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/mengtanZ/MaSS)

> Beyond achieving SoTA performance across diverse datasets with a unified model, MaSS is the first SSMDE method to effectively benefit from increased data diversity and exhibit remarkable generalizability to entirely out-of-distribution scenes. Cod...

</details>

<details>
<summary><b>33. Self-Evaluating Recursive Agents</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04902) • [📄 arXiv](https://arxiv.org/abs/2610.04902) • [📥 PDF](https://arxiv.org/pdf/2610.04902)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OliverLeeXZ/SERA)

> 🚀 Excited to share our latest work: Self-Evaluating Recursive Agents (SERA) ! As coding agents such as Claude Code and OpenAI Codex increasingly adopt task decomposition and subagent delegation, recursive agent architectures are emerging as a prom...

</details>

<details>
<summary><b>34. LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16782) • [📄 arXiv](https://arxiv.org/abs/2610.16782) • [📥 PDF](https://arxiv.org/pdf/2610.16782)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/IAIE-PhysicalAI/LIBERO-Industry)

> Are embodied AI models ready for the factory floor? Flexible manufacturing requires robots to adapt to changing products and production conditions. Yet today’s general-purpose embodied models still struggle when action failures and execution error...

</details>

<details>
<summary><b>35. HandsOn: A Large-Scale Simulation Benchmark for Generalizable Dexterous Manipulation</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Debin Ren, Ting Pan, Hongjin Wu, Yiming He, Tianwei Luo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26765) • [📄 arXiv](https://arxiv.org/abs/2610.26765) • [📥 PDF](https://arxiv.org/pdf/2610.26765)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TsinghuaC3I/HandsOn)

> Introducing HandsOn, a simulation platform and benchmark for generalizable dexterous manipulation. 66 human-verified tasks: Core-50 for demonstration-based learning and execution, plus Transfer-16 for asset and relation transfer, skill composition...

</details>

<details>
<summary><b>36. Factorization-Guided Training and Inference for Diffusion-Drafted Speculative Decoding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23935) • [📄 arXiv](https://arxiv.org/abs/2610.23935) • [📥 PDF](https://arxiv.org/pdf/2610.23935)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: More accepted tokens don’t always mean faster speculative decoding. We introduce DScout, which co-designs diffusion drafter training and inference: training aligns supervision with prefix acceptance, while inference configuration balances a...

</details>

<details>
<summary><b>37. ActionRoPE: action as coordinates for spatially consistent control in planar-camera game world models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yeying Jin, Yuzhe Wu, Zhiyang Deng, onepiece1999

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25861) • [📄 arXiv](https://arxiv.org/abs/2610.25861) • [📥 PDF](https://arxiv.org/pdf/2610.25861)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/TeaWhiteBro/ActionRoPE)

> 🎮 ActionRoPE: Actions as Coordinates for Game Worlds That Move Precisely and Stay Consistent In top-down and isometric games, the camera follows the player, so how far each action shifts the view is a fixed geometric quantity. Yet existing game wo...

</details>

<details>
<summary><b>38. UniAVC: Unified Audio-Video Creation via Progressive Training and Asymmetric Scheduling</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Yanghao Wang, Zhenqi He, Chong Hou Choi, Yuhao Liu, Kien T. Pham

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24791) • [📄 arXiv](https://arxiv.org/abs/2610.24791) • [📥 PDF](https://arxiv.org/pdf/2610.24791)

**💻 Code:** [⭐ Code](https://github.com/HKUST-LongGroup/UniAVC) • [⭐ Code](https://github.com/huggingface)

> UniAVC: Unified Audio-Video Creation via Progressive Training and Asymmetric Scheduling

</details>

<details>
<summary><b>39. HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24611) • [📄 arXiv](https://arxiv.org/abs/2610.24611) • [📥 PDF](https://arxiv.org/pdf/2610.24611)

**💻 Code:** [⭐ Code](https://github.com/wanyichen06/HSPR) • [⭐ Code](https://github.com/huggingface)

> Can we estimate a software agent’s full benchmark score by running only a small fraction of tasks? HSPR uses historical agent responses to build a hierarchical posterior over a new agent’s performance, then adaptively selects the most informative ...

</details>

<details>
<summary><b>40. RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21791) • [📄 arXiv](https://arxiv.org/abs/2610.21791) • [📥 PDF](https://arxiv.org/pdf/2610.21791)

**💻 Code:** [⭐ Code](https://github.com/1HUAN1/RSI-Flow) • [⭐ Code](https://github.com/huggingface)

> Large language model (LLM) agents have demonstrated strong capabilities in complex tasks, including code generation, tool use, and multi-hop question answering. Existing self-improvement methods enhance agent performance through model optimization...

</details>

<details>
<summary><b>41. World Model Interpretability: From Decoding Representations to Understanding Latent Worlds</b> ⭐ 95</summary>

<br/>

**👥 Authors:** Xinping Guan, Cailian Chen, Xinyi Le, Yongcheng Jing, Jize Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25296) • [📄 arXiv](https://arxiv.org/abs/2610.25296) • [📥 PDF](https://arxiv.org/pdf/2610.25296)

**💻 Code:** [⭐ Code](https://github.com/Jize-W/Awesome-World-Model-Interpretability) • [⭐ Code](https://github.com/huggingface)

> This Perspective aims to establish latent-world understanding as a central goal for interpreting predictive world models. We note that decodability is not understanding: accessible information does not reveal how it is organized, evolves, or causa...

</details>

<details>
<summary><b>42. FineSplat: Fine Patches, Local Groups, Detailed Splats</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Jungwoo Kim, Gyeongjin Kang, Joonhyuk Park, Hwasik Jeong, HyebinKim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25011) • [📄 arXiv](https://arxiv.org/abs/2610.25011) • [📥 PDF](https://arxiv.org/pdf/2610.25011)

**💻 Code:** [⭐ Code](https://github.com/hyebinny/FineSplat) • [⭐ Code](https://github.com/huggingface)

> Key Idea: A pose-free feed-forward 3DGS framework that leverages fine-grained features and dual-grouping attention for efficient cross-view interactions, enabling high-quality novel view synthesis with fewer Gaussians. Highlights: Fine-grained fea...

</details>

<details>
<summary><b>43. ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24766) • [📄 arXiv](https://arxiv.org/abs/2610.24766) • [📥 PDF](https://arxiv.org/pdf/2610.24766)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ernie-research/ECHO)

> ECHO — Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction A causal self-recursive Multi-Token Prediction (MTP) paradigm: Final-layer sharing : turns the indirect supervision of auxiliary MTP into direct multi-horizon supervisi...

</details>

<details>
<summary><b>44. Competing Learning in Hybrid Architectures</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26830) • [📄 arXiv](https://arxiv.org/abs/2610.26830) • [📥 PDF](https://arxiv.org/pdf/2610.26830)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/thunlp/competing-learning)

> Simple trick improves hybrid linear attention models (e.g., Kimi Delta Attention + Softmax Attention) for free!

</details>

<details>
<summary><b>45. Remembering Has a Price: Learning Memory Worth under Resource Constraints</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26453) • [📄 arXiv](https://arxiv.org/abs/2610.26453) • [📥 PDF](https://arxiv.org/pdf/2610.26453)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGNLAI/TokenWorth)

> We introduce TokenWorth , a lightweight online memory framework for lifelong agents operating under tight resource budgets. By learning query-dependent memory utility from execution feedback, TokenWorth improves memory retrieval and management, ac...

</details>

<details>
<summary><b>46. Co-Evolving Acting and Forecasting for Language Agents</b> ⭐ 12</summary>

<br/>

**👥 Authors:** Yuxiang Liu, Xuyan Ye, Yining Zhao, Yixing Chen, Haofei Yu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20597) • [📄 arXiv](https://arxiv.org/abs/2610.20597) • [📥 PDF](https://arxiv.org/pdf/2610.20597)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ulab-uiuc/CoPE)

> Agentic reinforcement learning learns only from a terminal scalar reward, so most of a long rollout goes unused. Per-step value targets all derive from that one scalar, and next-observation targets are long, noisy, and reach only one step ahead. C...

</details>

<details>
<summary><b>47. Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution</b> ⭐ 15</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17816) • [📄 arXiv](https://arxiv.org/abs/2610.17816) • [📥 PDF](https://arxiv.org/pdf/2610.17816)

**💻 Code:** [⭐ Code](https://github.com/OpenBMB/EC2-Bench) • [⭐ Code](https://github.com/huggingface)

> We systematically analyze edge-cloud collaboration strategies for LLM agents across 128 executable long-horizon tasks, measuring task performance, resource cost, and privacy exposure. Key finding: a 9B edge model with collaboration achieves ~73% o...

</details>

<details>
<summary><b>48. RealityBench: Simulated Environments to Evaluate a Vision Language Model's Ability to Document Human Physical Work</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14397) • [📄 arXiv](https://arxiv.org/abs/2610.14397) • [📥 PDF](https://arxiv.org/pdf/2610.14397)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We evaluate 26 VLMs in their ability to understand physical work, and release 11 Blender environments to evaluate them.

</details>

<details>
<summary><b>49. A Conditional No-Hair Theorem for Transformers: How Language Models Forget Their Prompt</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shuyang Xiang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.24133) • [📄 arXiv](https://arxiv.org/abs/2610.24133) • [📥 PDF](https://arxiv.org/pdf/2610.24133)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ShuyangenFrance/no-hair-transformers)

> We ask how much an autoregressive transformer retains of its prompt after generating t tokens. Consider two different prompts followed by the same continuation text, so that any difference in their hidden states comes from the prompt alone, and we...

</details>

<details>
<summary><b>50. Text-to-Image Generative Modeling Without Language Pretraining</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.26863) • [📄 arXiv](https://arxiv.org/abs/2610.26863) • [📥 PDF](https://arxiv.org/pdf/2610.26863)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We ask whether language pretraining is necessary for strong text-to-image generation. We introduce Halcyon, a family of early-fusion multimodal autoregressive models trained entirely from scratch on 100M image–text pairs. Halcyon outperforms stron...

</details>

<details>
<summary><b>51. Vision-Language-Delta-Action: Learning Compact Deltas as Actionable Transition Interfaces for Robotic Manipulation</b> ⭐ 695</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25874) • [📄 arXiv](https://arxiv.org/abs/2610.25874) • [📥 PDF](https://arxiv.org/pdf/2610.25874)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/baidu-baige/LoongForge)

> a Vision-Language-Delta-Action model trained with LoongForge: 98.5% on LIBERO, 84.5% zero-shot on LIBERO-Plus, and +17–18 points over π0.5 on real robots

</details>

<details>
<summary><b>52. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23470) • [📄 arXiv](https://arxiv.org/abs/2610.23470) • [📥 PDF](https://arxiv.org/pdf/2610.23470)

**💻 Code:** [⭐ Code](https://github.com/sakanaai/qd-rec) • [⭐ Code](https://github.com/huggingface)

> QD-Rec repeatedly selects an item, generates a hypothesis, and updates the archive through local novelty and quality comparisons: QD-Rec's archives during search in three domains (claude-sonnet-5 proposer). Each map cell shows the highest score am...

</details>

<details>
<summary><b>53. Policy Is Not Capability: Some Safety Benchmarks Measure Which Definition of "Unsafe" You Trained On</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jianbang Zhang, Adrian Chan, Yijin Wang, Jonathon Romero, Vahid Jebraeeli

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25060) • [📄 arXiv](https://arxiv.org/abs/2610.25060) • [📥 PDF](https://arxiv.org/pdf/2610.25060)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A guardrail's safety score depends on which definition of unsafe its training labels encode. Using ten guardrail classifiers trained on the same ~53k prompts labelled under two policies, we find that the training data already contained 88% of Jail...

</details>

<details>
<summary><b>54. Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Eunwoo Kim, Heayoun Choi, Jeongeun Park, taekyung-k, jiho-e

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09496) • [📄 arXiv](https://arxiv.org/abs/2610.09496) • [📥 PDF](https://arxiv.org/pdf/2610.09496)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: Can robots forget harmful behaviors without losing useful skills? SOUL (Sparse feature pOlicy UnLearnig) identifies interpretable sparse features associated with state hallucinations in VLAs and uses them to selectively unlearn harmful beha...

</details>

<details>
<summary><b>55. SPARC: Spoken Profile Authorship Recognition Corpus</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.25265) • [📄 arXiv](https://arxiv.org/abs/2610.25265) • [📥 PDF](https://arxiv.org/pdf/2610.25265)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bowenyi-pierre/SPARC)

> SPARC asks a simple question, once you strip the voice from speech, how much of the speaker is still in the words? Dataset and code: https://huggingface.co/datasets/timtsapras23/SPARC https://github.com/bowenyi-pierre/SPARC

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 55 |
| 📅 Today | [`2026-10-20.json`](data/daily/2026-10-20.json) | 55 |
| 📆 This Week | [`2026-W42.json`](data/weekly/2026-W42.json) | 109 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1226 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-20 | 55 | [View JSON](data/daily/2026-10-20.json) |
| 📄 2026-10-19 | 54 | [View JSON](data/daily/2026-10-19.json) |
| 📄 2026-10-18 | 84 | [View JSON](data/daily/2026-10-18.json) |
| 📄 2026-10-17 | 84 | [View JSON](data/daily/2026-10-17.json) |
| 📄 2026-10-16 | 69 | [View JSON](data/daily/2026-10-16.json) |
| 📄 2026-10-15 | 63 | [View JSON](data/daily/2026-10-15.json) |
| 📄 2026-10-14 | 69 | [View JSON](data/daily/2026-10-14.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W42 | 109 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1226 | [View JSON](data/monthly/2026-10.json) |
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
