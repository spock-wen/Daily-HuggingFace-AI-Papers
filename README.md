<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-49-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-3633+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">49</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">81</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">475</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">3633+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** April 22, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Extending One-Step Image Generation from Class Labels to Text via Discriminative Text Representation</b> ⭐ 85</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18168) • [📄 arXiv](https://arxiv.org/abs/2604.18168) • [📥 PDF](https://arxiv.org/pdf/2604.18168)

**💻 Code:** [⭐ Code](https://github.com/AMAP-ML/EMF)

> An interesting work (CVPR26) to extend One-Step Image Generation from Class Labels to Text via Discriminative Text Representation!

</details>

<details>
<summary><b>2. OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18486) • [📄 arXiv](https://arxiv.org/abs/2604.18486) • [📥 PDF](https://arxiv.org/pdf/2604.18486)

> OneVL is the first latent CoT method to surpass explicit CoT, delivering state-of-the-art accuracy on NAVSIM, ROADWork, Impromptu, and APR1 at answer-only latency, by compressing reasoning through both a language decoder and a visual world model d...

</details>

<details>
<summary><b>3. Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18292) • [📄 arXiv](https://arxiv.org/abs/2604.18292) • [📥 PDF](https://arxiv.org/pdf/2604.18292)

> We introduce Agent-World , a general-purpose agent training arena that couples real-world environment synthesis with continuous self-evolving training, forming a closed loop in which agents and environments co-evolve. It consists of two parts: (1)...

</details>

<details>
<summary><b>4. OpenGame: Open Agentic Coding for Games</b> ⭐ 140</summary>

<br/>

**👥 Authors:** Ruize Ma, Qianyin Xiao, Jinyuan Hu, Yilei Jiang, Jimmyzheng-10

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18394) • [📄 arXiv](https://arxiv.org/abs/2604.18394) • [📥 PDF](https://arxiv.org/pdf/2604.18394)

**💻 Code:** [⭐ Code](https://github.com/leigest519/OpenGame)

> Game development sits at the intersection of creative design and intricate software engineering, demanding the joint orchestration of game engines, real-time loops, and tightly coupled state across many files. While Large Language Models (LLMs) an...

</details>

<details>
<summary><b>5. MultiWorld: Scalable Multi-Agent Multi-View Video World Models</b> ⭐ 77</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18564) • [📄 arXiv](https://arxiv.org/abs/2604.18564) • [📥 PDF](https://arxiv.org/pdf/2604.18564)

**💻 Code:** [⭐ Code](https://github.com/CIntellifusion/MultiWorld)

> We present MultiWorld, a scalable multi-agent, multi-view video world model that generates action-controllable, multi-view-consistent videos for both multi-player games and multi-robot manipulation.

</details>

<details>
<summary><b>6. EasyVideoR1: Easier RL for Video Understanding</b> ⭐ 50</summary>

<br/>

**👥 Authors:** Dingyu Yao, Naibin Gu, Qingyi Si, Chenxu Yang, Chuanyu Qin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16893) • [📄 arXiv](https://arxiv.org/abs/2604.16893) • [📥 PDF](https://arxiv.org/pdf/2604.16893)

**💻 Code:** [⭐ Code](https://github.com/cyuQ1n/EasyVideoR1)

> EasyVideoR1 is an easier RL framework  for Video Understanding

</details>

<details>
<summary><b>7. GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification</b> ⭐ 25</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.14258) • [📄 arXiv](https://arxiv.org/abs/2604.14258) • [📥 PDF](https://arxiv.org/pdf/2604.14258)

**💻 Code:** [⭐ Code](https://github.com/ZJU-OmniAI/GFT) • [⭐ Code](https://github.com/ZJU-OmniAI/GFT/tree/main)

> Hi everyone, I'd like to share our lab's recent work that has been accepted to ACL 2026 Findings: GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification 🎉🚀 Currently, large language models he...

</details>

<details>
<summary><b>8. When Can LLMs Learn to Reason with Weak Supervision?</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Hamid Palangi, Anna Mordvina, Salman Rahman, pavelizmailov, Evangelinejy

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18574) • [📄 arXiv](https://arxiv.org/abs/2604.18574) • [📥 PDF](https://arxiv.org/pdf/2604.18574)

**💻 Code:** [⭐ Code](https://github.com/pavelslab-nyu/rlvr-weak-supervision)

> As LLMs get stronger, reliable reward signals get harder to build. We study when RLVR generalizes under weak supervision: scarce data, noisy rewards, and self-supervised proxies. Some models generalize, others fail entirely. The difference is reas...

</details>

<details>
<summary><b>9. WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yukai Huang, Chenchen Zhang, Junqi Xiong, Xinyu Che, Xinping Lei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18224) • [📄 arXiv](https://arxiv.org/abs/2604.18224) • [📥 PDF](https://arxiv.org/pdf/2604.18224)

> The dataset is released ( https://huggingface.co/datasets/NJU-LINK/WebCompass )

</details>

<details>
<summary><b>10. ClawEnvKit: Automatic Environment Generation for Claw-Like Agents</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18543) • [📄 arXiv](https://arxiv.org/abs/2604.18543) • [📥 PDF](https://arxiv.org/pdf/2604.18543)

**💻 Code:** [⭐ Code](https://github.com/xirui-li/ClawEnvKit)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents (2026) ClawsB...

</details>

<details>
<summary><b>11. SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents</b> ⭐ 18</summary>

<br/>

**👥 Authors:** Shiting Huang, Kou Shi, gaotiexinqu, YuZeng260, zhang-ziao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17308) • [📄 arXiv](https://arxiv.org/abs/2604.17308) • [📥 PDF](https://arxiv.org/pdf/2604.17308)

**💻 Code:** [⭐ Code](https://github.com/ZhangZi-a/SkillFlow)

> We propose SkillFlow, a benchmark for studying whether agents can summarize skills from experience and continuously iterate on and reuse a skill library over time. SkillFlow contains20 task families, each comprising8--9 tasks that share the same u...

</details>

<details>
<summary><b>12. Crowded in B-Space: Calibrating Shared Directions for LoRA Merging</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yi Yang, Yixuan Tang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16826) • [📄 arXiv](https://arxiv.org/abs/2604.16826) • [📥 PDF](https://arxiv.org/pdf/2604.16826)

> 🤗 Meet Pico : a lightweight method for better LoRA merging . The key insight? Not all parts of LoRA cause the same amount of interference. Pico focuses on the crowded directions in the B space , calibrates them before merging, and unlocks stronger...

</details>

<details>
<summary><b>13. The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16830) • [📄 arXiv](https://arxiv.org/abs/2604.16830) • [📥 PDF](https://arxiv.org/pdf/2604.16830)

**💻 Code:** [⭐ Code](https://github.com/SalesforceAIResearch/CaOPD)

> The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Distillation: On-policy distillation (OPD) improves task accuracy but systematically traps models in severe overconfidence. We trace this to an information mismatch betw...

</details>

<details>
<summary><b>14. Concrete Jungle: Towards Concreteness Paved Contrastive Negative Mining for Compositional Understanding</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vivek Gupta, Dhruv Madhwal, eunwooim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.13313) • [📄 arXiv](https://arxiv.org/abs/2604.13313) • [📥 PDF](https://arxiv.org/pdf/2604.13313)

> This paper studies data quality factors in compositional understanding and identifies an optimization issue in contrastive learning. We propose a simple margin-based improvement to InfoNCE, and opensource both a concreteness-aware training dataset...

</details>

<details>
<summary><b>15. On the Reliability of Computer Use Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17849) • [📄 arXiv](https://arxiv.org/abs/2604.17849) • [📥 PDF](https://arxiv.org/pdf/2604.17849)

**💻 Code:** [⭐ Code](https://github.com/simular-ai/cua_reliability)

> Computer-use agents have rapidly improved on real-world tasks such as web navigation, desktop automation, and software interaction, in some cases surpassing human performance. Yet even when the task and model are unchanged, an agent that succeeds ...

</details>

<details>
<summary><b>16. MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18584) • [📄 arXiv](https://arxiv.org/abs/2604.18584) • [📥 PDF](https://arxiv.org/pdf/2604.18584)

**💻 Code:** [⭐ Code](https://github.com/ShadeAlsha/MathNet)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API MMOU: A Massive Multi-Task Omni Understanding and Reasoning Benchmark for L...

</details>

<details>
<summary><b>17. GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)</b> ⭐ 5.51k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17091) • [📄 arXiv](https://arxiv.org/abs/2604.17091) • [📥 PDF](https://arxiv.org/pdf/2604.17091)

**💻 Code:** [⭐ Code](https://github.com/lsdefine/GenericAgent)

> Context information density is all a self-evolving LLM agent needs. Current agent frameworks pursue ever-longer context windows, yet agent performance is bounded by context quality , not length . We identify three compounding failure modes: positi...

</details>

<details>
<summary><b>18. VoxMind: An End-to-End Agentic Spoken Dialogue System</b> ⭐ 23</summary>

<br/>

**👥 Authors:** Zhiyang Jia, Yijun Chen, Shengpeng Ji, Yifu Chen, leungtianle

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.15710) • [📄 arXiv](https://arxiv.org/abs/2604.15710) • [📥 PDF](https://arxiv.org/pdf/2604.15710)

**💻 Code:** [⭐ Code](https://github.com/MM-Speech/VoxMind)

> Recent end-to-end spoken dialogue models enable natural interaction. However, as user demands become increasingly complex, models that rely solely on conversational abilities often struggle to cope. Incorporating agentic capabilities is therefore ...

</details>

<details>
<summary><b>19. OmniScript: Towards Audio-Visual Script Generation for Long-Form Cinematic Video</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.11102) • [📄 arXiv](https://arxiv.org/abs/2604.11102) • [📥 PDF](https://arxiv.org/pdf/2604.11102)

> OmniScript is an 8B-parameter omni-modal LLM for cinematic video understanding and structured script generation. It automatically translates narrative videos into temporally grounded scripts, segmenting them scene-by-scene, identifying precise tim...

</details>

<details>
<summary><b>20. Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17609) • [📄 arXiv](https://arxiv.org/abs/2604.17609) • [📥 PDF](https://arxiv.org/pdf/2604.17609)

> Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity LLM agents are assumed to integrate environmental observations into their reasoning. It turns out they don't. We inject complete solutions into agent environments as a file or API...

</details>

<details>
<summary><b>21. Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Jing Tang, Jia Li, Tianqing Fang, Dongyang Ma, Qifan Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18131) • [📄 arXiv](https://arxiv.org/abs/2604.18131) • [📥 PDF](https://arxiv.org/pdf/2604.18131)

**💻 Code:** [⭐ Code](https://github.com/Bklight999/world-knowledge)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Beyond Stochastic Exploration: What Makes Training Data Valuable for Agenti...

</details>

<details>
<summary><b>22. Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17696) • [📄 arXiv](https://arxiv.org/abs/2604.17696) • [📥 PDF](https://arxiv.org/pdf/2604.17696)

**💻 Code:** [⭐ Code](https://github.com/ydyyyy/Stratagem)

> Happy to share our latest paper: STRATAGEM. Our key idea is that not all successful game trajectories are equally useful for building general reasoning ability, so we explicitly reinforce those with higher transferability and stronger reasoning ev...

</details>

<details>
<summary><b>23. Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.08537) • [📄 arXiv](https://arxiv.org/abs/2604.08537) • [📥 PDF](https://arxiv.org/pdf/2604.08537)

**💻 Code:** [⭐ Code](https://github.com/ezacngm/brainCodec)

> Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, ...

</details>

<details>
<summary><b>24. Multiplication in Multimodal LLMs: Computation with Text, Image, and Audio Inputs</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18203) • [📄 arXiv](https://arxiv.org/abs/2604.18203) • [📥 PDF](https://arxiv.org/pdf/2604.18203)

> You can try out the multimodal benchmark yourself here! 😅 https://www.youtube.com/watch?v=WyxnP3UVc58&t=5560s Or train your models on it using the Hugging Face data repo: https://huggingface.co/datasets/cjerzak/MultimodalMathBenchmarks

</details>

<details>
<summary><b>25. Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16593) • [📄 arXiv](https://arxiv.org/abs/2604.16593) • [📥 PDF](https://arxiv.org/pdf/2604.16593)

**💻 Code:** [⭐ Code](https://github.com/jacklanda/SemanticQA)

> CFBR

</details>

<details>
<summary><b>26. River-LLM: Large Language Model Seamless Exit Based on KV Share</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18396) • [📄 arXiv](https://arxiv.org/abs/2604.18396) • [📥 PDF](https://arxiv.org/pdf/2604.18396)

> A training-free framework (River-LLM) to enable seamless token-level Early Exit in decoder-only LLMs via an innovative KV-sharing mechanism!

</details>

<details>
<summary><b>27. Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17338) • [📄 arXiv](https://arxiv.org/abs/2604.17338) • [📥 PDF](https://arxiv.org/pdf/2604.17338)

**💻 Code:** [⭐ Code](https://github.com/Bill1235813/PDB)

> PDB is an automatic pipeline that converts any coding dataset into a debugging benchmark with precision-aware evaluation. It generates buggy programs by synthesizing verified atomic bugs and composing them into multi-bug programs, then evaluates m...

</details>

<details>
<summary><b>28. Beyond Text-Dominance: Understanding Modality Preference of Omni-modal Large Language Models</b> ⭐ 5</summary>

<br/>

**👥 Authors:** Weixiang Zhou, Hongyu Lin, Yaojie Lu, Boxi Cao, Xinru Yan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16902) • [📄 arXiv](https://arxiv.org/abs/2604.16902) • [📥 PDF](https://arxiv.org/pdf/2604.16902)

**💻 Code:** [⭐ Code](https://github.com/icip-cas/OmniPreference)

> Proposing a modality preference evaluation framework for OLLMs: Constructing a tri-modal semantic conflict dataset with quantitative metrics to systematically measure model modality preferences. Revealing the modality preference landscape of OLLMs...

</details>

<details>
<summary><b>29. MedConclusion: A Benchmark for Biomedical Conclusion Generation from Structured Abstracts</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.06505) • [📄 arXiv](https://arxiv.org/abs/2604.06505) • [📥 PDF](https://arxiv.org/pdf/2604.06505)

**💻 Code:** [⭐ Code](https://github.com/Harvard-AI-and-Robotics-Lab/MedConclusion)

> We introduce MedConclusion, a large-scale dataset of 5.7M PubMed structured abstracts for biomedical conclusion generation. Each instance pairs the non-conclusion sections of an abstract with the original author-written conclusion, providing natur...

</details>

<details>
<summary><b>30. MARCO: Navigating the Unseen Space of Semantic Correspondence</b> ⭐ 25</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.18267) • [📄 arXiv](https://arxiv.org/abs/2604.18267) • [📥 PDF](https://arxiv.org/pdf/2604.18267)

**💻 Code:** [⭐ Code](https://github.com/visinf/MARCO)

> MARCO (CVPR 2026 Oral) learns dense, generalizable correspondences from sparse keypoints. It achieves state-of-the-art on standard benchmarks, improving fine-grained precision and generalizing to unseen keypoints and categories. Built on a single ...

</details>

<details>
<summary><b>31. Latent Preference Modeling for Cross-Session Personalized Tool Calling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17886) • [📄 arXiv](https://arxiv.org/abs/2604.17886) • [📥 PDF](https://arxiv.org/pdf/2604.17886)

> LLM agents are increasingly expected to call APIs on behalf of users, but real users rarely spell out every argument they want — they just say "book a flight for my trip" and expect the agent to know they always fly economy. We argue this isn't a ...

</details>

<details>
<summary><b>32. Modeling Multiple Support Strategies within a Single Turn for Emotional Support Conversations</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17972) • [📄 arXiv](https://arxiv.org/abs/2604.17972) • [📥 PDF](https://arxiv.org/pdf/2604.17972)

**💻 Code:** [⭐ Code](https://github.com/aliyun/qwen-dianjin)

> This paper reformulates emotional support conversation from single-strategy utterance generation to multi-strategy utterance generation, better reflecting real-world supportive replies that often combine multiple strategies in one turn. It propose...

</details>

<details>
<summary><b>33. The Geometric Canary: Predicting Steerability and Detecting Drift via Representational Stability</b> ⭐ 0</summary>

<br/>

**👥 Authors:** pcr2120

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17698) • [📄 arXiv](https://arxiv.org/abs/2604.17698) • [📥 PDF](https://arxiv.org/pdf/2604.17698)

**💻 Code:** [⭐ Code](https://github.com/prashantcraju/geometric-canary)

> The Geometric Canary introduces geometric stability as a dual diagnostic for LLM deployment. Supervised Shesha predicts which embedding models will accept linear steering with near-perfect accuracy (rho = 0.89-0.96 across 35-69 models and three NL...

</details>

<details>
<summary><b>34. When Background Matters: Breaking Medical Vision Language Models by Transferable Attack</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17318) • [📄 arXiv](https://arxiv.org/abs/2604.17318) • [📥 PDF](https://arxiv.org/pdf/2604.17318)

**💻 Code:** [⭐ Code](https://github.com/AkashGhosh/When-Background-Matters-Breaking-Medical-Vision-Language-Models-by-Transferable-Attack)

> The First black box transferable attack paper for Medical Vision Language Models

</details>

<details>
<summary><b>35. EvoMaster: A Foundational Agent Framework for Building Evolving Autonomous Scientific Agents at Scale</b> ⭐ 119</summary>

<br/>

**👥 Authors:** Fengyang Li, Cheng Wang, Zexi Liu, Yuzhu Cai, Xinyu Zhu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17406) • [📄 arXiv](https://arxiv.org/abs/2604.17406) • [📥 PDF](https://arxiv.org/pdf/2604.17406)

**💻 Code:** [⭐ Code](https://github.com/sjtu-sai-agents/EvoMaster)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Sci...

</details>

<details>
<summary><b>36. MNAFT: modality neuron-aware fine-tuning of multimodal large language models for image translation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shaolin Zhu, Shaobo Wang, Tianyu Dong, Ningyuan Deng, liboaccn

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16943) • [📄 arXiv](https://arxiv.org/abs/2604.16943) • [📥 PDF](https://arxiv.org/pdf/2604.16943)

> Multimodal large language models (MLLMs) have shown impressive capabilities, yet they often struggle to effectively capture the fine-grained textual information within images crucial for accurate image translation. This often leads to a modality g...

</details>

<details>
<summary><b>37. Modeling Sparse and Bursty Vulnerability Sightings: Forecasting Under Data Constraints</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16038) • [📄 arXiv](https://arxiv.org/abs/2604.16038) • [📥 PDF](https://arxiv.org/pdf/2604.16038)

**💻 Code:** [⭐ Code](https://github.com/vulnerability-lookup/TARDISsight)

> This work is using the VLAI Severity Classification model ( https://huggingface.co/CIRCL/vulnerability-severity-classification-roberta-base ). The severity score is used as a exogenous variable. Understanding and anticipating vulnerability-related...

</details>

<details>
<summary><b>38. Geometric coherence of single-cell CRISPR perturbations reveals regulatory architecture and predicts cellular stress</b> ⭐ 0</summary>

<br/>

**👥 Authors:** pcr2120

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16642) • [📄 arXiv](https://arxiv.org/abs/2604.16642) • [📥 PDF](https://arxiv.org/pdf/2604.16642)

**💻 Code:** [⭐ Code](https://github.com/prashantcraju/geometric-stability-crispr)

> We introduce Shesha perturbation stability, a geometric metric that measures whether cells respond to a CRISPR perturbation by moving together or scattering across expression space. Across 5 datasets and 2,200+ perturbations, we find that pleiotro...

</details>

<details>
<summary><b>39. MTR-DuplexBench: Towards a Comprehensive Evaluation of Multi-Round Conversations for Full-Duplex Speech Language Models</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Lei Zhu, Xiaohui Li, Haoning Xu, Wenqian Cui, Jeff0918

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2511.10262) • [📄 arXiv](https://arxiv.org/abs/2511.10262) • [📥 PDF](https://arxiv.org/pdf/2511.10262)

**💻 Code:** [⭐ Code](https://github.com/ZhangHe0918/MTR-DuplexBench)

> We present MTR-DuplexBench, the comprehensive benchmark for evaluating full-duplex speech language models across  multi-round conversations. Our benchmark evaluates models on four critical dimensions: Conversational Features (smooth-turntaking,int...

</details>

<details>
<summary><b>40. Forge-UGC: FX optimization and register-graph engine for universal graph compiler</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Saurabh Jha, Satyam Kumar

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16498) • [📄 arXiv](https://arxiv.org/abs/2604.16498) • [📥 PDF](https://arxiv.org/pdf/2604.16498)

> 🚀 Forge-UGC just dropped — a brand-new transparent 4-phase FX + register-graph compiler that makes transformer deployment on heterogeneous accelerators (validated on Intel AI Boost NPU) dramatically faster and more efficient! Key wins over OpenVIN...

</details>

<details>
<summary><b>41. Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17596) • [📄 arXiv](https://arxiv.org/abs/2604.17596) • [📥 PDF](https://arxiv.org/pdf/2604.17596)

**💻 Code:** [⭐ Code](https://github.com/few-sh/terminal-wrench)

> Terminal Wrench is a dataset of terminal-bench style environments that have shown evidence of being reward-hackable, paired with agent trajectories that lead to hacking and non-hacking rewards. Each entry preserves the original task definition alo...

</details>

<details>
<summary><b>42. The Continuity Layer: Why Intelligence Needs an Architecture for What It Carries Forward</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17273) • [📄 arXiv](https://arxiv.org/abs/2604.17273) • [📥 PDF](https://arxiv.org/pdf/2604.17273)

**💻 Code:** [⭐ Code](https://github.com/Kenotic-Labs/continuity-layer)

> The most important architectural problem in AI is not the size of the model. It is the absence of any layer that carries forward what the model has come to understand. This position paper argues that the continuity layer is the most consequential ...

</details>

<details>
<summary><b>43. Back to Repair: A Minimal Denoising Network\ for Time Series Anomaly Detection</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17388) • [📄 arXiv](https://arxiv.org/abs/2604.17388) • [📥 PDF](https://arxiv.org/pdf/2604.17388)

**💻 Code:** [⭐ Code](https://github.com/iis-esslingen/JuRe)

> We introduce JuRe (Just Repair), a minimal denoising network for time series anomaly detection, showing that architectural complexity is unnecessary when the objective enforces manifold projection. JuRe uses a single depthwise-separable convolutio...

</details>

<details>
<summary><b>44. HSG: Hyperbolic Scene Graph</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.17454) • [📄 arXiv](https://arxiv.org/abs/2604.17454) • [📥 PDF](https://arxiv.org/pdf/2604.17454)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/HSG)

> Although this is a relatively foundational work, we do open source it: https://github.com/AIGeeksGroup/HSG . IMO, scene graphs are a very important domain for spatial and embodied intelligence and should not be ignored.

</details>

<details>
<summary><b>45. On the Robustness of LLM-Based Dense Retrievers: A Systematic Analysis of Generalizability and Stability</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.16576) • [📄 arXiv](https://arxiv.org/abs/2604.16576) • [📥 PDF](https://arxiv.org/pdf/2604.16576)

**💻 Code:** [⭐ Code](https://github.com/liyongkang123/Robust_LLM_Retriever_Eval)

> In this paper, we evaluate the robustness of state-of-the-art (SOTA) open-source LLM-based dense retrievers.

</details>

<details>
<summary><b>46. KWBench: Measuring Unprompted Problem Recognition in Knowledge Work</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.15760) • [📄 arXiv](https://arxiv.org/abs/2604.15760) • [📥 PDF](https://arxiv.org/pdf/2604.15760)

**💻 Code:** [⭐ Code](https://github.com/ankitmaloo/fasteval)

> a benchmark for knowledge work

</details>

<details>
<summary><b>47. Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.15579) • [📄 arXiv](https://arxiv.org/abs/2604.15579) • [📥 PDF](https://arxiv.org/pdf/2604.15579)

**💻 Code:** [⭐ Code](https://github.com/hyn0027/agent-symbolic-guardrails)

> In this paper, we discuss symbolic guardrails for AI agents and provide evidence that symbolic guardrails improve safety while not harming agents' capabilities. We advocate adopting symbolic guardrails for guaranteed non-probabilistic agent safety...

</details>

<details>
<summary><b>48. Protecting Language Models Against Unauthorized Distillation through Trace Rewriting</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Yevgeniy Vorobeychik, Ning Zhang, William Yeoh, xXiaobuding

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15143) • [📄 arXiv](https://arxiv.org/abs/2602.15143) • [📥 PDF](https://arxiv.org/pdf/2602.15143)

**💻 Code:** [⭐ Code](https://github.com/xhOwenMa/trace-rewriting)

> We show four variants of reasoning trace rewriting methods -- two gradient-based and two easy-to-use instruction-based -- to achieve anti-distillation and easily verifiable watermarks that are also stealthy. Accepted to ACL 2026^^

</details>

<details>
<summary><b>49. Significance and Stability Analysis of Gene-Environment Interaction using RGxEStat</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2604.03337) • [📄 arXiv](https://arxiv.org/abs/2604.03337) • [📥 PDF](https://arxiv.org/pdf/2604.03337)

**💻 Code:** [⭐ Code](https://github.com/mason-ching/RGxEStat)

> Genotype-by-Environment (GxE) interactions influence the performance of genotypes across diverse environments, reducing the predictability of phenotypes in target environments. In-depth analysis of GxE interactions facilitates the identification o...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 49 |
| 📅 Today | [`2026-04-22.json`](data/daily/2026-04-22.json) | 49 |
| 📆 This Week | [`2026-W16.json`](data/weekly/2026-W16.json) | 81 |
| 🗓️ This Month | [`2026-04.json`](data/monthly/2026-04.json) | 475 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-04-22 | 49 | [View JSON](data/daily/2026-04-22.json) |
| 📄 2026-04-21 | 26 | [View JSON](data/daily/2026-04-21.json) |
| 📄 2026-04-20 | 3 | [View JSON](data/daily/2026-04-20.json) |
| 📄 2026-04-19 | 29 | [View JSON](data/daily/2026-04-19.json) |
| 📄 2026-04-18 | 29 | [View JSON](data/daily/2026-04-18.json) |
| 📄 2026-04-17 | 4 | [View JSON](data/daily/2026-04-17.json) |
| 📄 2026-04-16 | 7 | [View JSON](data/daily/2026-04-16.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W16 | 81 | [View JSON](data/weekly/2026-W16.json) |
| 📅 2026-W15 | 125 | [View JSON](data/weekly/2026-W15.json) |
| 📅 2026-W14 | 147 | [View JSON](data/weekly/2026-W14.json) |
| 📅 2026-W13 | 125 | [View JSON](data/weekly/2026-W13.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-04 | 475 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
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
