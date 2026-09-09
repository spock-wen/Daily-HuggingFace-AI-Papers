<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-37-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7209+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">62</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">229</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7209+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 09, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness</b> ⭐ 33</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08183) • [📄 arXiv](https://arxiv.org/abs/2609.08183) • [📥 PDF](https://arxiv.org/pdf/2609.08183)

**💻 Code:** [⭐ Code](https://github.com/TokenRhythm/NeoHorse) • [⭐ Code](https://github.com/huggingface)

> Huggingface: https://huggingface.co/collections/TokenRhythm/neohorse-1 ; Github: https://github.com/TokenRhythm/NeoHorse

</details>

<details>
<summary><b>2. AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing</b> ⭐ 27</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08936) • [📄 arXiv](https://arxiv.org/abs/2609.08936) • [📥 PDF](https://arxiv.org/pdf/2609.08936)

**💻 Code:** [⭐ Code](https://github.com/Tencent-Hunyuan/AuK) • [⭐ Code](https://github.com/huggingface)

> We introduce AuK, an open-source foundational model that unifies speech generation and editing through a common interface of natural-language instructions and audio context.

</details>

<details>
<summary><b>3. Omni Interaction Agent Technical Report</b> ⭐ 18</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08977) • [📄 arXiv](https://arxiv.org/abs/2609.08977) • [📥 PDF](https://arxiv.org/pdf/2609.08977)

**💻 Code:** [⭐ Code](https://github.com/Omni-Interaction-Gander/Omni-Interaction-Agent) • [⭐ Code](https://github.com/huggingface)

> Demo: https://omni-interaction-gander.github.io/Omni-Interaction-Agent/

</details>

<details>
<summary><b>4. Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08798) • [📄 arXiv](https://arxiv.org/abs/2609.08798) • [📥 PDF](https://arxiv.org/pdf/2609.08798)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/raymin0223/on_policy_reverse_distillation)

> Contributions Our key contributions are as follows: Weak-to-Strong Generalization. We study how post-training gains from weaker models can be transferred to stronger students in two practical scenarios: successive model transfer and multi-domain c...

</details>

<details>
<summary><b>5. DriveZero: End-to-End Driving Beyond Human Demonstrations</b> ⭐ 42</summary>

<br/>

**👥 Authors:** Zirun Su, Chengcheng Hu, Hao He, StarBurger, zhangheng1123

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06055) • [📄 arXiv](https://arxiv.org/abs/2609.06055) • [📥 PDF](https://arxiv.org/pdf/2609.06055)

**💻 Code:** [⭐ Code](https://github.com/XiaomiAutoL3/DriveZero) • [⭐ Code](https://github.com/huggingface)

> DriveZero decomposes driving into an action model and a perception model, pretrains each in the regime best suited to it, and unifies them by distillation. DriveRL , the action model, learns to drive from scratch with closed-loop RL. It converts r...

</details>

<details>
<summary><b>6. GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05588) • [📄 arXiv](https://arxiv.org/abs/2609.05588) • [📥 PDF](https://arxiv.org/pdf/2609.05588)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation

</details>

<details>
<summary><b>7. OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining</b> ⭐ 344</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07398) • [📄 arXiv](https://arxiv.org/abs/2609.07398) • [📥 PDF](https://arxiv.org/pdf/2609.07398)

**💻 Code:** [⭐ Code](https://github.com/OpenWAM-Official/OpenWAM) • [⭐ Code](https://github.com/huggingface)

> We introduce OpenWAM , an open, modular exploration towards systematic world-action model pretraining. OpenWAM includes three parts: 🧱 OpenWAM-Infra : We factorizes the WAM design space into composable modules, with unified training, inference, de...

</details>

<details>
<summary><b>8. Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Tongtong Liang, Shengju Qian, Enderfga, refkxh, Alicezrzhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09123) • [📄 arXiv](https://arxiv.org/abs/2609.09123) • [📥 PDF](https://arxiv.org/pdf/2609.09123)

**💻 Code:** [⭐ Code](https://github.com/delaprada/Mask-Forcing) • [⭐ Code](https://github.com/huggingface)

> We introduce Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout. Autoregressive (AR) video diffusion models have shown great potential in real-time video generation. Recent methods distill pretrained...

</details>

<details>
<summary><b>9. SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid Agentic Layout Evolution</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05594) • [📄 arXiv](https://arxiv.org/abs/2609.05594) • [📥 PDF](https://arxiv.org/pdf/2609.05594)

**💻 Code:** [⭐ Code](https://github.com/rxjfighting/SceneMosaic) • [⭐ Code](https://github.com/huggingface)

> SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid Agentic Layout Evolution Existing agent-based scene generation yields high-quality layouts through iterative refinement, but is slow. Conversely, Image-to-3D methods a...

</details>

<details>
<summary><b>10. Miles v0.1: Production-Level Post-Training</b> ⭐ 2.68k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08368) • [📄 arXiv](https://arxiv.org/abs/2609.08368) • [📥 PDF](https://arxiv.org/pdf/2609.08368)

**💻 Code:** [⭐ Code](https://github.com/radixark/miles) • [⭐ Code](https://github.com/huggingface)

> Miles is open-sourced at https://github.com/radixark/miles , with the project website at https://miles.radixark.com/

</details>

<details>
<summary><b>11. Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation</b> ⭐ 79</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08084) • [📄 arXiv](https://arxiv.org/abs/2609.08084) • [📥 PDF](https://arxiv.org/pdf/2609.08084)

**💻 Code:** [⭐ Code](https://github.com/huawei-bayerlab/marigold-v2) • [⭐ Code](https://github.com/huggingface)

> Marigold V2 is out! (to appear at SIGGRAPH Asia 2026). If you missed V1: Marigold post-trains an image generator into a depth estimator on one GPU -- the accessible research game. V2 upgrades to a diffusion transformer: single step, very sharp edg...

</details>

<details>
<summary><b>12. BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jungwook Choi, Kyuhong Shim, Minsoo Kim, kkt20

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.04971) • [📄 arXiv](https://arxiv.org/abs/2609.04971) • [📥 PDF](https://arxiv.org/pdf/2609.04971)

**💻 Code:** [⭐ Code](https://github.com/aiha-lab/BeaconKV) • [⭐ Code](https://github.com/huggingface)

> We introduce BeaconKV, a training-free KV cache compression method for large reasoning models, based on our observation that queries revisiting distant context form a small number of clusters. BeaconKV combines representative "beacon queries" with...

</details>

<details>
<summary><b>13. CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shuguang Cui, Yiming Hao, Zeyu Jin, Mutian Xu, Hongxiang Zhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07498) • [📄 arXiv](https://arxiv.org/abs/2609.07498) • [📥 PDF](https://arxiv.org/pdf/2609.07498)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/GAP-LAB-CUHK-SZ/CosmoH2G)

> SIGGRAPH Aisa 2026; Project page: https://cosmoh2g.github.io/

</details>

<details>
<summary><b>14. Reason Through the Latent! Making Latent Visual Reasoning Necessary</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jaewoo Kang, JunhaJung, Codingchild

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06746) • [📄 arXiv](https://arxiv.org/abs/2609.06746) • [📥 PDF](https://arxiv.org/pdf/2609.06746)

**💻 Code:** [⭐ Code](https://github.com/dmis-lab/CVRR) • [⭐ Code](https://github.com/huggingface)

> Latent visual reasoning aims to perform multimodal reasoning through hidden-state computation rather than explicit textual chains of thought. However, visual information being present in a latent state does not imply that the model actually relies...

</details>

<details>
<summary><b>15. Steering Geometry: Validating Human Value Geometry in LLM Steering Space</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06289) • [📄 arXiv](https://arxiv.org/abs/2609.06289) • [📥 PDF](https://arxiv.org/pdf/2609.06289)

**💻 Code:** [⭐ Code](https://github.com/DeepRCL/Steering_Geometry) • [⭐ Code](https://github.com/huggingface)

> We’re excited to share Steering Geometry , accepted to EMNLP 2026 Main ! When we steer an LLM toward one human value, what happens to the others? We investigate whether steering directions capture the relationships predicted by psychological theor...

</details>

<details>
<summary><b>16. Agentic Visual Generation: From Generative Models to Agentic Control</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06758) • [📄 arXiv](https://arxiv.org/abs/2609.06758) • [📥 PDF](https://arxiv.org/pdf/2609.06758)

**💻 Code:** [⭐ Code](https://github.com/YinmingHuang/Awesome-agentic-visual-generation-model) • [⭐ Code](https://github.com/huggingface)

> Visual generation is evolving from generative models used through a single invocation into agentic control processes that can plan, select tools, inspect intermediate synthesized outputs, revise failures, and reuse prior experience. In most existi...

</details>

<details>
<summary><b>17. Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07108) • [📄 arXiv](https://arxiv.org/abs/2609.07108) • [📥 PDF](https://arxiv.org/pdf/2609.07108)

**💻 Code:** [⭐ Code](https://github.com/NVIDIA-NeMo/RL/issues/3698) • [⭐ Code](https://github.com/huggingface)

> We address system challenges for online speculative decoding in large-scale RL post-training with long contexts: branch attention in advanced draft models breaks causal context parallelism (CP), and intermediate features needed by the draft may re...

</details>

<details>
<summary><b>18. Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08404) • [📄 arXiv](https://arxiv.org/abs/2609.08404) • [📥 PDF](https://arxiv.org/pdf/2609.08404)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HongbangYuan/EnvAsScaffold)

> No abstract available.

</details>

<details>
<summary><b>19. RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05324) • [📄 arXiv](https://arxiv.org/abs/2609.05324) • [📥 PDF](https://arxiv.org/pdf/2609.05324)

**💻 Code:** [⭐ Code](https://github.com/fanzhenxuan/RoboSPA) • [⭐ Code](https://github.com/huggingface)

> Can VLA models go beyond simple scenes and short-horizon tasks? We introduce RoboSPA, a large-scale diagnostic benchmark for evaluating VLA models on fine-grained spatial reasoning and long-horizon procedural planning. It contains 56 tasks across ...

</details>

<details>
<summary><b>20. Kalman Delta Networks: Uncertainty-aware Associative Memory</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07816) • [📄 arXiv](https://arxiv.org/abs/2609.07816) • [📥 PDF](https://arxiv.org/pdf/2609.07816)

**💻 Code:** [⭐ Code](https://github.com/ngocbh/kalman-delta-networks) • [⭐ Code](https://github.com/huggingface)

> A key question behind this work is: should associative memory treat every new observation with the same level of confidence? Existing Delta-rule models decide how strongly to update memory from the current token, but they do not explicitly track h...

</details>

<details>
<summary><b>21. TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Junli Ren, Zhuo Cao, Zhaobo Li, Yuxin Chen, Anqi Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09158) • [📄 arXiv](https://arxiv.org/abs/2609.09158) • [📥 PDF](https://arxiv.org/pdf/2609.09158)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>22. Procedural Graphs: Self-Evolving Execution Structures for LLM Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.09153) • [📄 arXiv](https://arxiv.org/abs/2609.09153) • [📥 PDF](https://arxiv.org/pdf/2609.09153)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>23. CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.08345) • [📄 arXiv](https://arxiv.org/abs/2609.08345) • [📥 PDF](https://arxiv.org/pdf/2609.08345)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/humansensinglab/CoVeR)

> 🌐 Project: https://humansensinglab.github.io/CoVeR/ 💻 Code: https://github.com/humansensinglab/CoVeR

</details>

<details>
<summary><b>24. Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07470) • [📄 arXiv](https://arxiv.org/abs/2609.07470) • [📥 PDF](https://arxiv.org/pdf/2609.07470)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Hi folks, author here.👋 Almost every robot foundation model out there is trained and evaluated in English. For most of the world's languages there is no robot demonstration data at all, and nobody is going to collect it anytime soon. So we wanted ...

</details>

<details>
<summary><b>25. VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes</b> ⭐ 88</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06652) • [📄 arXiv](https://arxiv.org/abs/2609.06652) • [📥 PDF](https://arxiv.org/pdf/2609.06652)

**💻 Code:** [⭐ Code](https://github.com/GAIR-NLP/VidaForge) • [⭐ Code](https://github.com/huggingface)

> code: https://github.com/GAIR-NLP/VidaForge paper: https://arxiv.org/pdf/2609.06652

</details>

<details>
<summary><b>26. What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05663) • [📄 arXiv](https://arxiv.org/abs/2609.05663) • [📥 PDF](https://arxiv.org/pdf/2609.05663)

**💻 Code:** [⭐ Code](https://github.com/ProjectDXAI/continuous-record-llm-trading-agents) • [⭐ Code](https://github.com/huggingface)

> This paper records the pre-alpha systems behind DXAP: 3,505 user-funded Base vaults and a 500-599-agent Hyperliquid fleet with 231,638 finalized turns. P&L varied widely across agents and over time. The useful result was how the system around the ...

</details>

<details>
<summary><b>27. MOLE: Detecting Insider Threats in AI Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06966) • [📄 arXiv](https://arxiv.org/abs/2609.06966) • [📥 PDF](https://arxiv.org/pdf/2609.06966)

**💻 Code:** [⭐ Code](https://github.com/aashiqmuhamed/mole) • [⭐ Code](https://github.com/huggingface)

> Dataset: https://huggingface.co/datasets/forgelab/mole Code: https://github.com/aashiqmuhamed/mole

</details>

<details>
<summary><b>28. Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Keyang Xu, Yuhan Wang, Hardy Chen, Haoqin Tu, JiaMao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06373) • [📄 arXiv](https://arxiv.org/abs/2609.06373) • [📥 PDF](https://arxiv.org/pdf/2609.06373)

**💻 Code:** [⭐ Code](https://github.com/jwmao1/moviegrid) • [⭐ Code](https://github.com/huggingface)

> MovieGrid introduces Multi-Grid Post-Training for long-form, multi-shot video generation. It arranges temporally ordered video chunks on a spatial grid, enabling joint modeling and information exchange across shots. With the same token budget, Mov...

</details>

<details>
<summary><b>29. Recognition-Refusal Misalignment in LLMs: Why Models Answer Structurally Unanswerable Questions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29109) • [📄 arXiv](https://arxiv.org/abs/2608.29109) • [📥 PDF](https://arxiv.org/pdf/2608.29109)

**💻 Code:** [⭐ Code](https://github.com/yucheng-du/recognition-refusal-misalignment) • [⭐ Code](https://github.com/huggingface)

> Accepted to EMNLP main 2026. I'm the first author of this paper. We study why LLMs answer structurally unanswerable math and code questions even when their hidden states encode a signal of unanswerability. Across instruction-tuned models from 1.7B...

</details>

<details>
<summary><b>30. ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07941) • [📄 arXiv](https://arxiv.org/abs/2609.07941) • [📥 PDF](https://arxiv.org/pdf/2609.07941)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/huiyuiui/ReactVAU-code)

> In this paper, we propose ReactVAU, a Slow-Fast Decoupled Framework for real-time streaming Video Anomaly Understanding (VAU). Existing VAU methods rely on offline inference with global temporal sampling, which violates causality and prevents depl...

</details>

<details>
<summary><b>31. Encoded Early, Used Late: Where Transformers Begin to Act on an Inferred Partner's Expertise</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Gabriele Sarti, mokamoto

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07139) • [📄 arXiv](https://arxiv.org/abs/2609.07139) • [📥 PDF](https://arxiv.org/pdf/2609.07139)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> .

</details>

<details>
<summary><b>32. TransNormal-2: Geometry-Grounded Rectified Flow with Edge-Aware Decoding for Precise Normal Estimation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Hehe Fan, Yi Yang, Mingwei Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06665) • [📄 arXiv](https://arxiv.org/abs/2609.06665) • [📥 PDF](https://arxiv.org/pdf/2609.06665)

**💻 Code:** [⭐ Code](https://github.com/longxiang-ai/TransNormal-2) • [⭐ Code](https://github.com/huggingface)

> TL;DR: TransNormal-2 estimates surface normal maps from a single RGB image in one deterministic rectified-flow step on the FLUX.2 [klein] 9B backbone (LoRA-adapted), followed by a lightweight Geometric Refinement Module (GRM) that applies bounded ...

</details>

<details>
<summary><b>33. Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Series Foundation Model</b> ⭐ 1</summary>

<br/>

**👥 Authors:** robtacconelli

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06008) • [📄 arXiv](https://arxiv.org/abs/2609.06008) • [📥 PDF](https://arxiv.org/pdf/2609.06008)

**💻 Code:** [⭐ Code](https://github.com/robtacconelli/Cadence) • [⭐ Code](https://github.com/huggingface)

> We present Cadence, an error-bounded lossy compressor for numeric time series pairing a 330M-parameter time-series foundation model (Google TimesFM-3) with an adaptive arithmetic coder, guaranteeing |x^t−xt|≤τ on every sample.

</details>

<details>
<summary><b>34. SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2510.08999) • [📄 arXiv](https://arxiv.org/abs/2510.08999) • [📥 PDF](https://arxiv.org/pdf/2510.08999)

**💻 Code:** [⭐ Code](https://github.com/comeusr/SQS_TMLR) • [⭐ Code](https://github.com/huggingface)

> Published at TMLR 09/2026: https://openreview.net/forum?id=3nZb43fvAQ

</details>

<details>
<summary><b>35. Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yuhui Chen, Shun Zhang, Kai Li, Yi Zhou, Xuechao Zou

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07670) • [📄 arXiv](https://arxiv.org/abs/2609.07670) • [📥 PDF](https://arxiv.org/pdf/2609.07670)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XavierJiezou/UCF-Net)

> This paper introduces UCF-Net, an uncertainty-aware cascaded fusion network for generalizable deepfake image detection. It combines CLIP's language-aligned semantic priors with DINO's self-supervised visual-structure priors, extracting hierarchica...

</details>

<details>
<summary><b>36. A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fanyu Meng, Junlan Feng, Shuo Wang, Siyuan Liu, xxang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07821) • [📄 arXiv](https://arxiv.org/abs/2609.07821) • [📥 PDF](https://arxiv.org/pdf/2609.07821)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AI9Stars/AStar-Thought)

> Code: https://github.com/AI9Stars/AStar-Thought

</details>

<details>
<summary><b>37. RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07414) • [📄 arXiv](https://arxiv.org/abs/2609.07414) • [📥 PDF](https://arxiv.org/pdf/2609.07414)

**💻 Code:** [⭐ Code](https://github.com/vLAR-group/RelightFormer) • [⭐ Code](https://github.com/huggingface)

> Image relighting is traditionally tackled via complex inverse rendering pipelines, which suffer from ill-posed optimization, or single-image generative models that ignore crucial multi-view cues necessary for understanding 3D geometry and material...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 37 |
| 📅 Today | [`2026-09-09.json`](data/daily/2026-09-09.json) | 37 |
| 📆 This Week | [`2026-W36.json`](data/weekly/2026-W36.json) | 62 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 229 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-09 | 37 | [View JSON](data/daily/2026-09-09.json) |
| 📄 2026-09-08 | 6 | [View JSON](data/daily/2026-09-08.json) |
| 📄 2026-09-07 | 19 | [View JSON](data/daily/2026-09-07.json) |
| 📄 2026-09-06 | 31 | [View JSON](data/daily/2026-09-06.json) |
| 📄 2026-09-05 | 31 | [View JSON](data/daily/2026-09-05.json) |
| 📄 2026-09-04 | 23 | [View JSON](data/daily/2026-09-04.json) |
| 📄 2026-09-03 | 28 | [View JSON](data/daily/2026-09-03.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W36 | 62 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 229 | [View JSON](data/monthly/2026-09.json) |
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
