<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-72-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7761+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">72</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">179</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">781</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7761+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 30, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Raven: The Harness of Harnesses for Composable Agentic Intelligence</b> ⭐ 4.83k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33439) • [📄 arXiv](https://arxiv.org/abs/2609.33439) • [📥 PDF](https://arxiv.org/pdf/2609.33439)

**💻 Code:** [⭐ Code](https://github.com/EverMind-AI/Raven) • [⭐ Code](https://github.com/huggingface)

> As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale...

</details>

<details>
<summary><b>2. MaLiang-Harness: A Programmable Path to Image and Video Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34309) • [📄 arXiv](https://arxiv.org/abs/2609.34309) • [📥 PDF](https://arxiv.org/pdf/2609.34309)

**💻 Code:** [⭐ Code](https://github.com/gulucaptain/MaLiang-Harness) • [⭐ Code](https://github.com/huggingface)

> Executable programs offer explicit control over how images and videos are constructed, but generating runnable code is only the beginning of visual creation. A program can execute correctly while violating the requested composition, appearance, or...

</details>

<details>
<summary><b>3. In-Context Learning for Robots: Methods and Applications</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36012) • [📄 arXiv](https://arxiv.org/abs/2609.36012) • [📥 PDF](https://arxiv.org/pdf/2609.36012)

**💻 Code:** [⭐ Code](https://github.com/JethroJames/awesome-robots-icl) • [⭐ Code](https://github.com/huggingface)

> Co-author note: I contributed to this survey. A robot can finish a task and still miss what the demonstration taught. This survey follows context all the way to execution: through action distributions, motion references, predicted futures, and ski...

</details>

<details>
<summary><b>4. PanoVLN: Towards Effective Panoramic Vision-and-Language Navigation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34759) • [📄 arXiv](https://arxiv.org/abs/2609.34759) • [📥 PDF](https://arxiv.org/pdf/2609.34759)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> https://wangzhen-w.github.io/PanoVLN/

</details>

<details>
<summary><b>5. Omni-IO Skills: Harnessing Your Agent Omni-Native</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31847) • [📄 arXiv](https://arxiv.org/abs/2609.31847) • [📥 PDF](https://arxiv.org/pdf/2609.31847)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/any2any-mllm/Omni-IO-Skill)

> Hi everyone! Sharing our new work: Omni-IO Skills: Harnessing Your Agent Omni-Native 🚀 Your agent is only one harness away from being omni-native ! General-purpose agents like Claude and Codex are strong at reasoning and planning, but audio, video...

</details>

<details>
<summary><b>6. VoxMem: Benchmarking Multimodal Memory in Large Audio Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32607) • [📄 arXiv](https://arxiv.org/abs/2609.32607) • [📥 PDF](https://arxiv.org/pdf/2609.32607)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/swagshaw/voxmem)

> Can your voice assistant remember who told it something, not just what was said? Mostly, no. We built VoxMem, a benchmark where the answer to a question hides in a multi-session spoken history. Sometimes it's in the words, but often it's in the sp...

</details>

<details>
<summary><b>7. What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34981) • [📄 arXiv](https://arxiv.org/abs/2609.34981) • [📥 PDF](https://arxiv.org/pdf/2609.34981)

**💻 Code:** [⭐ Code](https://github.com/LeapLabTHU/Simple-WAM) • [⭐ Code](https://github.com/huggingface)

> Links 📄 paper: https://arxiv.org/abs/2609.34981 🏠 project page: https://zrporz.github.io/Simple-WAM-Web/ 💻 code: https://github.com/LeapLabTHU/Simple-WAM 🤗 model: https://huggingface.co/rpzhou/Simple-WAM

</details>

<details>
<summary><b>8. SAKI: Maximal-Coupling-Routed Teacher Supervision for On-Policy Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36601) • [📄 arXiv](https://arxiv.org/abs/2609.36601) • [📥 PDF](https://arxiv.org/pdf/2609.36601)

**💻 Code:** [⭐ Code](https://github.com/Miteto-sudo/SAKI) • [⭐ Code](https://github.com/huggingface)

> On-policy distillation (OPD) reduces train-test state mismatch by training a student on its own generated trajectories, but weak students may visit teacher-misaligned prefixes where supervision is less representative. We introduce SAKI (Supervisio...

</details>

<details>
<summary><b>9. Think Before You Score: Thinking Reward Model for Visual Generation</b> ⭐ 16</summary>

<br/>

**👥 Authors:** Tengfei Liu, Dianyi Wang, Zhenchen Tang, Xuehai Bai, DogNeverSleep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37372) • [📄 arXiv](https://arxiv.org/abs/2609.37372) • [📥 PDF](https://arxiv.org/pdf/2609.37372)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/bxhsort/Thinking_Reward_Model)

> Visual reward models are essential for evaluating and improving visual generation models, yet existing approaches typically map task conditions and candidate outputs directly to scalar rewards, leaving implicit what should be evaluated for each in...

</details>

<details>
<summary><b>10. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38155) • [📄 arXiv](https://arxiv.org/abs/2609.38155) • [📥 PDF](https://arxiv.org/pdf/2609.38155)

**💻 Code:** [⭐ Code](https://github.com/rhfeiyang/GEB) • [⭐ Code](https://github.com/huggingface)

> We introduce Grounded Entity Biographies (GEB), which links observations of the same physical entity across long videos into retrievable biographies, improving long-horizon video understanding.

</details>

<details>
<summary><b>11. Follow the Entities: A Corpus Map for Agentic Search</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37226) • [📄 arXiv](https://arxiv.org/abs/2609.37226) • [📥 PDF](https://arxiv.org/pdf/2609.37226)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> What if your agent had a map of the corpus, instead of rediscovering how documents connect for every query? 🗺️ CorpusMap builds that map once, offline: each recurring entity (a project, a person, an incident) gets an Entity Page with source-attrib...

</details>

<details>
<summary><b>12. EngiWorld: What Can Frontier Agents Deliver in Professional Engineering Environments?</b> ⭐ 17</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37686) • [📄 arXiv](https://arxiv.org/abs/2609.37686) • [📥 PDF](https://arxiv.org/pdf/2609.37686)

**💻 Code:** [⭐ Code](https://github.com/Hongcheng-Gao/EngiWorld) • [⭐ Code](https://github.com/huggingface)

> EngiWorld is the first benchmark covering the complete engineering design loop, with 1,301 expert-curated tasks across 6 domains (CAD, CAE, CAM, BIM, EDA, 3D visualization) and 26 professional software platforms. Its artifact-centric evaluation pr...

</details>

<details>
<summary><b>13. LongCat-DeepResearch Technical Report</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haolin Ren, Wanli Wu, He Zhu, Meituan LongCat Team, LeonardYue

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36071) • [📄 arXiv](https://arxiv.org/abs/2609.36071) • [📥 PDF](https://arxiv.org/pdf/2609.36071)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. OmniTaskonomy: When Does Visual Generation Improve Visual Understanding?</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38079) • [📄 arXiv](https://arxiv.org/abs/2609.38079) • [📥 PDF](https://arxiv.org/pdf/2609.38079)

**💻 Code:** [⭐ Code](https://github.com/para-lost/OmniTaskonomy) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>15. Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37868) • [📄 arXiv](https://arxiv.org/abs/2609.37868) • [📥 PDF](https://arxiv.org/pdf/2609.37868)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We explore a simple question: can heterogeneous reasoning models learn from successes that their peers discover but they fail to sample? GRAFT exchanges complementary peer trajectories during RLVR while explicitly controlling off-policy mismatch. ...

</details>

<details>
<summary><b>16. LLMs are General Asynchronous Agents</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35427) • [📄 arXiv](https://arxiv.org/abs/2609.35427) • [📥 PDF](https://arxiv.org/pdf/2609.35427)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/dvmazur/async_llm)

> We’re releasing AsyncLLM, an open-source framework that lets pretrained LLMs observe, reason and act concurrently without additional training. The key idea: concurrency lives inside inference, and not around API calls. Inspired by asyncio an agent...

</details>

<details>
<summary><b>17. Anisotropic Representations Improve Planning in JEPA World Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37441) • [📄 arXiv](https://arxiv.org/abs/2609.37441) • [📥 PDF](https://arxiv.org/pdf/2609.37441)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>18. LEGO-Anything: Coding Agents for 3D Scene Reconstruction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36380) • [📄 arXiv](https://arxiv.org/abs/2609.36380) • [📥 PDF](https://arxiv.org/pdf/2609.36380)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> LEGO-Anything uses coding agents to reconstruct a single image as an editable, executable 3D scene through iterative Blender programming. The work introduces LEGO-Bench, comprising 208 images from 104 indoor and outdoor scenes, to evaluate artifac...

</details>

<details>
<summary><b>19. Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Linjun Li, Dongjie Fu, Zihan Zhang, Xize Cheng, Wenxu Jia

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32522) • [📄 arXiv](https://arxiv.org/abs/2609.32522) • [📥 PDF](https://arxiv.org/pdf/2609.32522)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce VoxPolyMem , an interaction-aware hierarchical memory framework designed for complex multi-party speech and multimodal settings, effectively resolving memory attribution challenges through structured layers and an LLM-based agentic re...

</details>

<details>
<summary><b>20. SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Junsong Chen, Yitong Li, Shuchen Xue, Tian Ye, Haozhe Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37969) • [📄 arXiv](http://arxiv.org/abs/2609.37969) • [📥 PDF](https://arxiv.org/pdf/2609.37969)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 SoL-Refiner: 2K video in one step. Give it a low-resolution video from any generator, and SoL-Refiner turns it into sharp, detailed 2K/4K video with a single denoising step. ✨ Crisp textures and fine detail at 4K ⚡ One step, 8.91× faster end to ...

</details>

<details>
<summary><b>21. EVO-WAM: Evolving World Action Models through Video-Action Verification</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38057) • [📄 arXiv](https://arxiv.org/abs/2609.38057) • [📥 PDF](https://arxiv.org/pdf/2609.38057)

**💻 Code:** [⭐ Code](https://github.com/Clausy9/EVO-WAM) • [⭐ Code](https://github.com/huggingface)

> Really cool idea! 🤖 EVO-WAM shows that a World Action Model can actually learn from its own imagination! Instead of collecting more expert demonstrations, it generates video-action rollouts, uses a VLM to check whether the task is completed, and a...

</details>

<details>
<summary><b>22. ROSS: Relearning from Self-Generated Rollouts through Selective Supervision</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35954) • [📄 arXiv](https://arxiv.org/abs/2609.35954) • [📥 PDF](https://arxiv.org/pdf/2609.35954)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large language model post-training generates self-generated rollouts through reinforcement learning and on-policy distillation, yet this experience is often treated as stale once the policy advances. Historical rollouts can remain compatible with ...

</details>

<details>
<summary><b>23. HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Fei Tang, Niu Lian, Zhengxi Lu, Junbo Niu, Tongbo Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38008) • [📄 arXiv](https://arxiv.org/abs/2609.38008) • [📥 PDF](https://arxiv.org/pdf/2609.38008)

**💻 Code:** [⭐ Code](https://github.com/ZJU-REAL/HybridCUA) • [⭐ Code](https://github.com/huggingface)

> We develop a data construction pipeline that produces interleaved GUI and CLI trajectories. This pipeline results in HybridCUA-8K, containing 5K hybrid trajectories and 3K verified RLVR tasks. Building on these data, we propose a training framewor...

</details>

<details>
<summary><b>24. LongLive-Plug: Once-for-All Distillation for Video Generation</b> ⭐ 2.64k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38154) • [📄 arXiv](https://arxiv.org/abs/2609.38154) • [📥 PDF](https://arxiv.org/pdf/2609.38154)

**💻 Code:** [⭐ Code](https://github.com/NVlabs/LongLive) • [⭐ Code](https://github.com/huggingface)

> We introduce LongLive-Plug, a once-for-all distillation framework that learns reusable capabilities as LoRAs for training-free, plug-and-play deployment to compatible downstream video models. We validate deployment on 54 downstream models across M...

</details>

<details>
<summary><b>25. APM-Bench: Benchmarking Cross-session Persistent Memory for Egocentric Streaming Video Assistants</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Jianhang Li, Liang Xu, Qiyao Wang, Jinming Liu, Jianguo Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37559) • [📄 arXiv](https://arxiv.org/abs/2609.37559) • [📥 PDF](https://arxiv.org/pdf/2609.37559)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Jianguo-Huang11/APM-Bench)

> Streaming video models increasingly support continuous perception, real-time interaction, and proactive assistance, showing their potential as personal assistants; memory is key to making such assistants truly personal by retaining and reusing use...

</details>

<details>
<summary><b>26. Marathoner: Ultra-Long-Horizon Autonomous Intelligence</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34378) • [📄 arXiv](https://arxiv.org/abs/2609.34378) • [📥 PDF](https://arxiv.org/pdf/2609.34378)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Humans naturally possess the ability to work persistently toward long-term goals. Given a challenging task, humans can continuously work for months or even years to accomplish a specific objective. Following this spirit, strong proprietary models ...

</details>

<details>
<summary><b>27. WorldAttention: An Efficient Attention Architecture for Interactive Video World Models</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34606) • [📄 arXiv](https://arxiv.org/abs/2609.34606) • [📥 PDF](https://arxiv.org/pdf/2609.34606)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/WorldAttention) • [⭐ Code](https://github.com/huggingface)

> 🌍 We propose WorldAttention, an efficient attention architecture that lets interactive video world models draw on long-range history while generating at 22 FPS on a single NVIDIA H100. ⚡ Its Hybrid Sparse Attention and Hierarchical KV Cache delive...

</details>

<details>
<summary><b>28. WorldLine: Action-Driven Visual Simulation for Robotic Manipulation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38059) • [📄 arXiv](https://arxiv.org/abs/2609.38059) • [📥 PDF](https://arxiv.org/pdf/2609.38059)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Zhengsh123/WorldLine)

> A visual simulator that predicts how robot actions change the scene. WorldLine separates learning robot–object dynamics from learning how each robot’s controls should steer them.

</details>

<details>
<summary><b>29. CrossBFM: Distilling a Shared Latent Behavior Space Across Humanoid Embodiments</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Siwei Ju, Cuc T. Trinh, Nico Bohlinger, Tuan Dat Phuong, Tan-Dzung Do

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38087) • [📄 arXiv](https://arxiv.org/abs/2609.38087) • [📥 PDF](https://arxiv.org/pdf/2609.38087)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project Page: https://dotandung.github.io/crossbfm/

</details>

<details>
<summary><b>30. Asking for What Was Never Requested: Horizontal and Vertical Proactivity in Agents</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37236) • [📄 arXiv](https://arxiv.org/abs/2609.37236) • [📥 PDF](https://arxiv.org/pdf/2609.37236)

**💻 Code:** [⭐ Code](https://github.com/dolev31/ProactiveInquirer) • [⭐ Code](https://github.com/huggingface)

> What should an LLM agent pursue that the user never asked for? We define horizontal proactivity (a need the current state already names) and vertical proactivity (a need only newly found evidence names), measure both against need graphs with no LL...

</details>

<details>
<summary><b>31. EasyPPO: Stabilizing the Critic Is Key</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenhao Chai, Dacheng Li, Huanzhi Mao, Qiuyang Mang, Xuanyi Zhou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36802) • [📄 arXiv](https://arxiv.org/abs/2609.36802) • [📥 PDF](https://arxiv.org/pdf/2609.36802)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 来看

</details>

<details>
<summary><b>32. HiRAE: Hierarchical Representation Autoencoding with Residual Budgets</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuanxing Zhang, Yihang Lou, Yan Bai, Xuanyu Zhu, DogNeverSleep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37775) • [📄 arXiv](https://arxiv.org/abs/2609.37775) • [📥 PDF](https://arxiv.org/pdf/2609.37775)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Pretrained visual representations support image generation, but may not fully preserve the fine-grained details needed for faithful reconstruction. Meanwhile, intermediate encoder layers contain complementary visual details, but learning to fuse t...

</details>

<details>
<summary><b>33. ANTMAN: Adaptive Need Tracking for Multi-Agent Navigation in Large Information Spaces</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33326) • [📄 arXiv](https://arxiv.org/abs/2609.33326) • [📥 PDF](https://arxiv.org/pdf/2609.33326)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce ANTMAN, an adaptive coordination framework for information-seeking agents operating over large-scale information spaces. Instead of relying on static decomposition, ANTMAN tracks evolving unresolved information needs and scales coordi...

</details>

<details>
<summary><b>34. Reasoning with Image Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.16409) • [📄 arXiv](https://arxiv.org/abs/2609.16409) • [📥 PDF](https://arxiv.org/pdf/2609.16409)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Chain-of-thought reasoning has revolutionized natural language processing by enabling large language models (LLMs) to decompose problems into intermediate steps before answering. Yet confining reasoning to the textual domain presents limitations f...

</details>

<details>
<summary><b>35. Context Language Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37725) • [📄 arXiv](https://arxiv.org/abs/2609.37725) • [📥 PDF](https://arxiv.org/pdf/2609.37725)

**💻 Code:** [⭐ Code](https://github.com/facebookresearch/context-language-models) • [⭐ Code](https://github.com/huggingface)

> The Bitter Lesson for context management : Giving LMs unrestricted access to their own context beats human-designed SOTA! Introducing 🩵 Context Language Models (CLMs) 🩵 Natively manage their own context Treat context as a file Learn policies in CL...

</details>

<details>
<summary><b>36. Selecting The Most Informative Tokens in Natural Language Autoencoders</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37040) • [📄 arXiv](https://arxiv.org/abs/2609.37040) • [📥 PDF](https://arxiv.org/pdf/2609.37040)

**💻 Code:** [⭐ Code](https://github.com/federicotorrielli/nla-token-selector) • [⭐ Code](https://github.com/huggingface)

> We ask a practical question about Natural Language Autoencoders (NLAs): if generating an explanation for every token is prohibitively expensive, which token positions should I inspect? We test this at scale, generating about 4.7 million explanatio...

</details>

<details>
<summary><b>37. Omni-Decision: Evidence-Ledger Planning for Omni-Modal Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuhao Wang, Feida Zhu, Yiran Zhong, Yi Zhu, Ming Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.11433) • [📄 arXiv](https://arxiv.org/abs/2607.11433) • [📥 PDF](https://arxiv.org/pdf/2607.11433)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone! We introduce Omni-Decision, an agent for tasks spanning video, audio, web search, and computation. Our controlled experiments show that replacing the planner has a much larger impact on performance than replacing the perception backen...

</details>

<details>
<summary><b>38. When Does Dense Retrieval Need Asymmetric Geometry? A Bias-Variance Theory of Shared and Dual Projections</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32488) • [📄 arXiv](https://arxiv.org/abs/2609.32488) • [📥 PDF](https://arxiv.org/pdf/2609.32488)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> When should dense retrieval use separate query and document projections instead of a shared one? We study this choice through a bias–variance lens, derive a boundary for when the added flexibility is worthwhile, and propose CARS to help select bet...

</details>

<details>
<summary><b>39. EmoRES-TTS: Residual-Enhanced Vector Steering for Emotional Speech Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38157) • [📄 arXiv](https://arxiv.org/abs/2609.38157) • [📥 PDF](https://arxiv.org/pdf/2609.38157)

**💻 Code:** [⭐ Code](https://github.com/facebookresearch/EmoRES-TTS) • [⭐ Code](https://github.com/huggingface)

> EmoRES improves emotional speech generation without retraining by decomposing emotion steering vectors into shared and emotion-specific components and selectively strengthening the latter, improving emotion control across different TTS backbones. ...

</details>

<details>
<summary><b>40. Chinese-Jev: Bringing System One Model to Chinese-Language Tasks</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36965) • [📄 arXiv](https://arxiv.org/abs/2609.36965) • [📥 PDF](https://arxiv.org/pdf/2609.36965)

**💻 Code:** [⭐ Code](https://github.com/gulucaptain/Chinese-Jev) • [⭐ Code](https://github.com/huggingface)

> System One models such as Jev offer an efficient alternative to generative language models for tasks that require decisions rather than open-ended responses. In this paper, we introduce Chinese-Jev, a System One model that addresses the Chinese-QA...

</details>

<details>
<summary><b>41. TabFM: A Zero-Shot Foundation Model for Tabular Data</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37959) • [📄 arXiv](https://arxiv.org/abs/2609.37959) • [📥 PDF](https://arxiv.org/pdf/2609.37959)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TabFM, a tabular foundation model from Google Research

</details>

<details>
<summary><b>42. VideoLoop: Looped Working Memory Against Semantic Thrashing in Long-Form Video Agents</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Jiebo Luo, Zhengyuan Yang, Jingyang Lin, Jianming Xu, Jinfa Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38119) • [📄 arXiv](https://arxiv.org/abs/2609.38119) • [📥 PDF](https://arxiv.org/pdf/2609.38119)

**💻 Code:** [⭐ Code](https://github.com/philipxjm/videoloop) • [⭐ Code](https://github.com/huggingface)

> VideoLoop addresses semantic thrashing in long-form video agents with two coupled loops: an outer loop that reasons over video and an inner loop that retrieves past artifacts and rewrites a bounded working memory. It improves four LVLM backbones b...

</details>

<details>
<summary><b>43. Adversarial Training for Pixel Diffusion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38170) • [📄 arXiv](https://arxiv.org/abs/2609.38170) • [📥 PDF](https://arxiv.org/pdf/2609.38170)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Pixel diffusion models can generate semantically strong images, yet often miss fine-scale natural image statistics. We find that adversarial post-training consistently restores this missing high-frequency detail, improving fidelity, coverage, prom...

</details>

<details>
<summary><b>44. TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33589) • [📄 arXiv](https://arxiv.org/abs/2609.33589) • [📥 PDF](https://arxiv.org/pdf/2609.33589)

**💻 Code:** [⭐ Code](https://github.com/1229095296/TGRL) • [⭐ Code](https://github.com/huggingface)

> Accepted by NeurIPS2026. Efficient exploration often remains a central bottleneck in reinforcement learning with verifiable rewards (RLVR). Although temperature control and test-time scaling strategies can increase rollout diversity of large langu...

</details>

<details>
<summary><b>45. EpiCon: Collective Agent Learning through Co-Evolving Multimodal Memory</b> ⭐ 0</summary>

<br/>

**👥 Authors:** William T. Freeman, Rogerio Feris, Shaden Alshammari, hhua2, zengziyun

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37923) • [📄 arXiv](https://arxiv.org/abs/2609.37923) • [📥 PDF](https://arxiv.org/pdf/2609.37923)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> EpiCon is a shared multimodal memory framework that enables agents to co-evolve memory from their own executions and transfer accumulated experience across agents without updating the host model. It couples question-level memory refinement with a ...

</details>

<details>
<summary><b>46. Language Models Are "Insecure" Reporters</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36139) • [📄 arXiv](https://arxiv.org/abs/2609.36139) • [📥 PDF](https://arxiv.org/pdf/2609.36139)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>47. TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37989) • [📄 arXiv](https://arxiv.org/abs/2609.37989) • [📥 PDF](https://arxiv.org/pdf/2609.37989)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TabFM-Auto: an LLM agent search feature engineering around a frozen TabFM — the Tabular Foundation Model by Google Research — to achieve over 2000 Elo on TabArena.

</details>

<details>
<summary><b>48. Beyond Selection: Token Parameterization for Extreme Visual Token Compression</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Cheng Zhuo, Zheyu Yan, Yu Li, zrrraa

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35232) • [📄 arXiv](https://arxiv.org/abs/2609.35232) • [📥 PDF](https://arxiv.org/pdf/2609.35232)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zrrraa/Braco)

> TL;DR: Don’t just decide which visual tokens to keep—change how they are represented. We revisit compression through a token parameterization lens, separating (i) basis transformation and structured truncation (retained subspace/compressibility) f...

</details>

<details>
<summary><b>49. Real2Gym: Building Gyms from Videos, Bringing Skills to Robots</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37089) • [📄 arXiv](https://arxiv.org/abs/2609.37089) • [📥 PDF](https://arxiv.org/pdf/2609.37089)

**💻 Code:** [⭐ Code](https://github.com/real2gym/Real2Gym) • [⭐ Code](https://github.com/huggingface)

> Real-world videos provide rich demonstrations of manipulation, but turning them into reusable robot skills requires visually aligned environments, executable physical interactions, and mechanisms for learning from experience. We introduce Real2Gym...

</details>

<details>
<summary><b>50. Where the Model Changes Its Mind: Hindsight-Divergence Localization for Efficient Reinforcement Learning with Verifiable Rewards</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36864) • [📄 arXiv](https://arxiv.org/abs/2609.36864) • [📥 PDF](https://arxiv.org/pdf/2609.36864)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Where the Model Changes Its Mind: Hindsight-Divergence Localization for Efficient Reinforcement Learning with Verifiable Rewards

</details>

<details>
<summary><b>51. AnyStep-WAM: Budget-Aligned Distillation and Adaptive Inference for World Action Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Canyang Chen, Yibo Li, Donglin Yang, Xiangyu Wang, Rui Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33748) • [📄 arXiv](https://arxiv.org/abs/2609.33748) • [📥 PDF](https://arxiv.org/pdf/2609.33748)

**💻 Code:** [⭐ Code](https://github.com/RuiWang724/AnyStep-WAM) • [⭐ Code](https://github.com/huggingface)

> World-action models (WAMs) typically use fixed-step denoising, despite varying precision requirements across manipulation stages. We introduce AnyStep WAM, a framework for cross-budget prediction and scene-dependent computation allocation. Budget-...

</details>

<details>
<summary><b>52. Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.38140) • [📄 arXiv](https://arxiv.org/abs/2609.38140) • [📥 PDF](https://arxiv.org/pdf/2609.38140)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Accepted as a Spotlight paper at NeurIPS 2026. Project page: https://yuci-gpt.github.io/SplitMoE/

</details>

<details>
<summary><b>53. PlaylistEval: Can Video-Language Judges Be Trusted at Day Scale and Beyond?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hwanjun Song, shayekh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34314) • [📄 arXiv](https://arxiv.org/abs/2609.34314) • [📥 PDF](https://arxiv.org/pdf/2609.34314)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We benchmark 17 video-language judges from eight model families on PlaylistEval, covering 630 preference pairs across seven domains, with roughly 100 hours of video per domain. Several findings stood out: The strongest judge reaches only 75.4% acc...

</details>

<details>
<summary><b>54. AutoDataBench: Can Agents Write the Data That Feeds the Self-Improvement Loop?</b> ⭐ 18</summary>

<br/>

**👥 Authors:** Yibo Wang, Huanjin Yao, Zeyu Qin, Haoyu Wang, Haotian Luo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35025) • [📄 arXiv](https://arxiv.org/abs/2609.35025) • [📥 PDF](https://arxiv.org/pdf/2609.35025)

**💻 Code:** [⭐ Code](https://github.com/StarDewXXX/AutoDataBench) • [⭐ Code](https://github.com/huggingface)

> Recent gains in language model capability have come more from data than from architecture. Frontier labs and data companies produce verifiable agentic tasks, which supervised finetuning and reinforcement learning then turn into capability. This pr...

</details>

<details>
<summary><b>55. WISE-ATTA: When to Ask for Labels in Budgeted Active Test-Time Adaptation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.37687) • [📄 arXiv](https://arxiv.org/abs/2609.37687) • [📥 PDF](https://arxiv.org/pdf/2609.37687)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Muhammad-Huzaifaa/WISE-ATTA)

> Most active test-time adaptation methods assume you can request supervision (labels) for every test batch, which becomes expensive over long streams. We look at the problem from a budgeted setting where only a fraction of batches can be labeled, s...

</details>

<details>
<summary><b>56. Persistence Forcing: Exploiting Feature Specialization in Pixel-Space Diffusion</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36014) • [📄 arXiv](https://arxiv.org/abs/2609.36014) • [📥 PDF](https://arxiv.org/pdf/2609.36014)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ChongWang1024/PerF)

> Persistence Forcing: Exploiting Feature Specialization in Pixel-Space Diffusion Paper · Project Page · Code · Pretrained Models PerF introduces heterogeneous refinement in pixel-space diffusion Transformers, revealing persistent and active feature...

</details>

<details>
<summary><b>57. SEAD: A State-Based Perspective on Attack and Defense in Tool-Using Agents</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Pan Li, Rongzhe Wei, Junran Wang, Xinjie Shen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34518) • [📄 arXiv](https://arxiv.org/abs/2609.34518) • [📥 PDF](https://arxiv.org/pdf/2609.34518)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/EverywhereSafety/SEAD)

> SEAD studies agent safety through the state changes caused by tool use. An action that appears harmless in isolation can become harmful after earlier steps change the environment, while the visible conversation may not reveal that state. We formul...

</details>

<details>
<summary><b>58. StoryEngine: A State-Grounded Agentic Framework for Video Storytelling</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33627) • [📄 arXiv](https://arxiv.org/abs/2609.33627) • [📥 PDF](https://arxiv.org/pdf/2609.33627)

**💻 Code:** [⭐ Code](https://github.com/wwwTaylor/StoryEngine) • [⭐ Code](https://github.com/huggingface)

> 🎬 StoryEngine: A State-Driven Agentic Framework for Multi-Shot Video Storytelling AI can generate beautiful short videos. But keeping a story coherent across multiple shots remains a challenge: characters drift, objects become inconsistent, and er...

</details>

<details>
<summary><b>59. StructRL: Online Structured Reinforcement Learning for Long-Horizon Vision-Language-Action Tasks</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36352) • [📄 arXiv](https://arxiv.org/abs/2609.36352) • [📥 PDF](https://arxiv.org/pdf/2609.36352)

**💻 Code:** [⭐ Code](https://github.com/amazon-science/StructRL) • [⭐ Code](https://github.com/huggingface)

> StructRL is an online RL framework for long-horizon VLA tasks. Instead of rewarding only final task success, it rewards verifiable progress: an LLM decomposes each task into subtasks with simulator-checkable completion criteria and a prerequisite ...

</details>

<details>
<summary><b>60. Same Bytes, Different Authority: Reserved-Token Representations in Chat-Template Prompt Injection</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35932) • [📄 arXiv](https://arxiv.org/abs/2609.35932) • [📥 PDF](https://arxiv.org/pdf/2609.35932)

**💻 Code:** [⭐ Code](https://github.com/Byte-Authority/Byte-Authority) • [⭐ Code](https://github.com/huggingface)

> Prompt-injection defenses often treat a chat-template marker as ordinary text. This paper shows that the same visible bytes can carry very different authority depending on whether the tokenizer emits a reserved control token or ordinary subwords. ...

</details>

<details>
<summary><b>61. Pretraining Transformers with Quantized Softmax in Attention</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.33591) • [📄 arXiv](https://arxiv.org/abs/2609.33586) • [📥 PDF](https://arxiv.org/pdf/2609.33591)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> When you approximate softmax during pretraining , the approximation defines the learning rule. We study which backward choices make a quantized softmax trainable from scratch. Key findings (GPT-2-style 124M/1B, up to 2.5B tokens, 5-seed replicatio...

</details>

<details>
<summary><b>62. One Proposal for Every Margin: Zero-Shot Amortized Sequential Importance Sampling for Binary Matrices</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35514) • [📄 arXiv](https://arxiv.org/abs/2609.35514) • [📥 PDF](https://arxiv.org/pdf/2609.35514)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi everyone, first author here! 👋 Excited to share MarginFlow: one learned proposal for thousands of counting and sampling problems. 🚀 We tackle a classic challenge: counting and sampling binary matrices with prescribed row and column sums—a found...

</details>

<details>
<summary><b>63. Preference-Guided Adaptation for Open-Vocabulary Semantic Segmentation via Prompt Disagreement</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.34528) • [📄 arXiv](https://arxiv.org/abs/2609.34528) • [📥 PDF](https://arxiv.org/pdf/2609.34528)

**💻 Code:** [⭐ Code](https://github.com/blue-531/pref-ovss) • [⭐ Code](https://github.com/huggingface)

> Open-vocabulary semantic segmentation (OVSS) enables pixel-level prediction over arbitrary text-specified vocabularies and has shown strong generalization on common benchmarks. However, OVSS performance often degrades in specialized domains such a...

</details>

<details>
<summary><b>64. PrismQuant: Optimal Null-Space Rotations for Grouped Quantizers</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.32429) • [📄 arXiv](https://arxiv.org/abs/2609.32429) • [📥 PDF](https://arxiv.org/pdf/2609.32429)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ForeverBlue816/PrismQuant)

> No abstract available.

</details>

<details>
<summary><b>65. Principled Thoughts for Latent Recursive LLM Systems</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36159) • [📄 arXiv](https://arxiv.org/abs/2609.36159) • [📥 PDF](https://arxiv.org/pdf/2609.36159)

**💻 Code:** [⭐ Code](https://github.com/FARD-Lab/REST) • [⭐ Code](https://github.com/huggingface)

> Large language models can reason in continuous space instead of decoded text, by recurring on their own hidden states or by passing those states between agents, while training supervises only the Cross-Entropy (CE) of the final decoded answer and ...

</details>

<details>
<summary><b>66. Act First, Reason Later: Accelerating On-Policy Distillation for Multi-Turn Agents via Reference-Conditioned Inverse Dynamics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.36608) • [📄 arXiv](https://arxiv.org/abs/2609.36608) • [📥 PDF](https://arxiv.org/pdf/2609.36608)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> ActFirst-OPD accelerates multi-turn agent on-policy distillation by combining reference-conditioned inverse dynamics for fast actions with asynchronous full-response generation.

</details>

<details>
<summary><b>67. FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Alan Yuille, Soumava Paul, Srinjay Sarkar, toshi2k2

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35770) • [📄 arXiv](https://arxiv.org/abs/2609.35770) • [📥 PDF](https://arxiv.org/pdf/2609.35770)

**💻 Code:** [⭐ Code](https://github.com/toshi2k2/fure) • [⭐ Code](https://github.com/huggingface)

> Efficient SOTA for 3D animal fur reconstruction.

</details>

<details>
<summary><b>68. Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.19669) • [📄 arXiv](https://arxiv.org/abs/2608.19669) • [📥 PDF](https://arxiv.org/pdf/2608.19669)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Submitting because I found interesting... Description from the author: https://x.com/haoqik322/status/2099280837208653984

</details>

<details>
<summary><b>69. Jev thinks "I don't know'', but doesn't say it: Introducing Sys1Cal-v1 Dataset for Probability Calibration</b> ⭐ 0</summary>

<br/>

**👥 Authors:** RPorcedda

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35342) • [📄 arXiv](https://arxiv.org/abs/2609.35342) • [📥 PDF](https://arxiv.org/pdf/2609.35342)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/little-g-ai/Sys1Cal-v1)

> Sys1Cal-v1 asks a simple question: when a System One Model returns a probability, does that probability actually have the numerical meaning we assume it has? We introduce a benchmark in which the exact probability of every proposition is known by ...

</details>

<details>
<summary><b>70. Understanding On-Policy Distillation: A Mechanistic Interpretability Perspective via Sparse Crosscoders</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35210) • [📄 arXiv](https://arxiv.org/abs/2609.35210) • [📥 PDF](https://arxiv.org/pdf/2609.35210)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This work reveals that on-policy distillation improves reasoning primarily by reshaping how students use existing representations, offering a mechanistic account of what stronger teachers actually teach.

</details>

<details>
<summary><b>71. Hyperspherical Semantic Trajectory Analysis: Mapping Technological Diffusion across Academic Preprints, Patent Signals, and Compute Scaling</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Muhammad Sukri Bin Ramli

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.35845) • [📄 arXiv](https://arxiv.org/abs/2609.35845) • [📥 PDF](https://arxiv.org/pdf/2609.35845)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hyperspherical Semantic Trajectory Analysis: Mapping Technological Diffusion across Academic Preprints, Patent Signals, and Compute Scaling Muhammad Sukri Bin Ramli Macroeconomic productivity metrics, such as Total Factor Productivity, register te...

</details>

<details>
<summary><b>72. CaptchaArena: A Large-Scale, Fine-Grained Dataset for Training Computer-Use Agents on Interactive CAPTCHAs</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.31957) • [📄 arXiv](https://arxiv.org/abs/2609.31957) • [📥 PDF](https://arxiv.org/pdf/2609.31957)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/X0X0X00/CaptchaArena)

> We introduce CaptchaArena, a large-scale, fine-grained dataset for interactive CAPTCHA solving, with 50K puzzles across 20 types and 5 interaction modes, including 46K screenshot-action trajectories with step-by-step reasoning. Using CaptchaArena,...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 72 |
| 📅 Today | [`2026-09-30.json`](data/daily/2026-09-30.json) | 72 |
| 📆 This Week | [`2026-W39.json`](data/weekly/2026-W39.json) | 179 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 781 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-30 | 72 | [View JSON](data/daily/2026-09-30.json) |
| 📄 2026-09-29 | 83 | [View JSON](data/daily/2026-09-29.json) |
| 📄 2026-09-28 | 24 | [View JSON](data/daily/2026-09-28.json) |
| 📄 2026-09-27 | 22 | [View JSON](data/daily/2026-09-27.json) |
| 📄 2026-09-26 | 22 | [View JSON](data/daily/2026-09-26.json) |
| 📄 2026-09-25 | 18 | [View JSON](data/daily/2026-09-25.json) |
| 📄 2026-09-24 | 24 | [View JSON](data/daily/2026-09-24.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W39 | 179 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |
| 📅 2026-W37 | 138 | [View JSON](data/weekly/2026-W37.json) |
| 📅 2026-W36 | 151 | [View JSON](data/weekly/2026-W36.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 781 | [View JSON](data/monthly/2026-09.json) |
| 🗓️ 2026-08 | 709 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |

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
