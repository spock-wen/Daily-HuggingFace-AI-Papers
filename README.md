<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-63-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8641+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">63</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">194</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">880</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8641+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 15, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation</b> ⭐ 65</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20571) • [📄 arXiv](https://arxiv.org/abs/2610.20571) • [📥 PDF](https://arxiv.org/pdf/2610.20571)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ziplab/ATAS)

> Excited to share ATAS — Any Time, Any Space ! Video models can produce impressive individual shots, but keeping a whole story consistent is harder: a room should keep its layout when revisited, and different cameras should capture the same event a...

</details>

<details>
<summary><b>2. Player-1: Learning to Play from Synthetic Experience</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20584) • [📄 arXiv](https://arxiv.org/abs/2610.20584) • [📥 PDF](https://arxiv.org/pdf/2610.20584)

**💻 Code:** [⭐ Code](https://github.com/TencentARC/Player-1) • [⭐ Code](https://github.com/huggingface)

> Synthetic environments improve transferable agent capabilities: Player-1 is an agentic post-training pipeline that learns general game control beyond supervised demonstrations. 🌐  Project: player-1-project.github.io 📄  Paper: arxiv.org/abs/2610.20...

</details>

<details>
<summary><b>3. Recovering Reliable Supervision via Critique-Guided On-Policy Distillation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Amanda Hughes, Yuxiao Yang, Shangzhe Li, Tianrun Yu, kzhao5

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20572) • [📄 arXiv](https://arxiv.org/abs/2610.20572) • [📥 PDF](https://arxiv.org/pdf/2610.20572)

**💻 Code:** [⭐ Code](https://github.com/kzhao5/CriticOPD) • [⭐ Code](https://github.com/huggingface)

> 🤖 CriticOPD: Recovering Reliable Supervision via Critique-Guided On-Policy Distillation 🔍 Key finding: Teachers can recognize student mistakes yet still follow them when continuing a flawed solution, making OPD supervision unreliable. ✍️ Our appro...

</details>

<details>
<summary><b>4. Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents</b> ⭐ 32</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20344) • [📄 arXiv](https://arxiv.org/abs/2610.20344) • [📥 PDF](https://arxiv.org/pdf/2610.20344)

**💻 Code:** [⭐ Code](https://github.com/YuyaoGe/doc2harness) • [⭐ Code](https://github.com/huggingface)

> Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchma...

</details>

<details>
<summary><b>5. LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Zongliang Wu, Tong Zhu, Xiaoyang Chen, Yunkai Chai, Zefeng He

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19975) • [📄 arXiv](https://arxiv.org/abs/2610.19975) • [📥 PDF](https://arxiv.org/pdf/2610.19975)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lcqysl/LatentLoop)

> We introduce LatentLoop, which improves looped MoE models under matched budgets by compressing the first loop visit, preserving full resolution in the second, and reallocating the saved compute to increase model width.

</details>

<details>
<summary><b>6. Cortex: Consolidating Context into Parametric Memory</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20399) • [📄 arXiv](https://arxiv.org/abs/2610.20399) • [📥 PDF](https://arxiv.org/pdf/2610.20399)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Cortex turns context-induced performance gains into mergeable parameter updates, enabling LLMs to internalize new knowledge while preserving existing capabilities for continual learning.

</details>

<details>
<summary><b>7. ActionOPD: Distilling Decisions, Not Tokens</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19820) • [📄 arXiv](https://arxiv.org/abs/2610.19820) • [📥 PDF](https://arxiv.org/pdf/2610.19820)

**💻 Code:** [⭐ Code](https://github.com/thu-nics/ActionOPD) • [⭐ Code](https://github.com/huggingface)

> Hi everyone, author here! ActionOPD distills agent decisions through semantic agreement with black-box teachers, without requiring teacher token probabilities or tokenizer alignment. 🌐 Project Page 💻 Code 🤗 Models

</details>

<details>
<summary><b>8. Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13521) • [📄 arXiv](https://arxiv.org/abs/2610.13521) • [📥 PDF](https://arxiv.org/pdf/2610.13521)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Developed jointly by JD.com’s OxygenVLM team and Nanjing University, RoadMOPD mitigates learning conflicts among teachers with substantially different response styles and domain expertise, helping a student integrate multiple experts’ capabilities...

</details>

<details>
<summary><b>9. Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19366) • [📄 arXiv](https://arxiv.org/abs/2610.19366) • [📥 PDF](https://arxiv.org/pdf/2610.19366)

**💻 Code:** [⭐ Code](https://github.com/Seeing-Maintaining-Learning/multimodal-agent-memory-evolution) • [⭐ Code](https://github.com/huggingface)

> How can multimodal agents remember what they perceive, keep that memory useful as the world changes, and learn to manage it better over time? We are sharing our survey, “Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory.”...

</details>

<details>
<summary><b>10. LensErase: A Foundation Model for Erase Anything</b> ⭐ 29</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18072) • [📄 arXiv](https://arxiv.org/abs/2610.18072) • [📥 PDF](https://arxiv.org/pdf/2610.18072)

**💻 Code:** [⭐ Code](https://github.com/LensFamily/LensErase) • [⭐ Code](https://github.com/huggingface)

> LensErase: A foundation model for Erase Anything, enabling high-quality removal of objects, text, watermarks, and associated visual effects while precisely preserving unedited regions.

</details>

<details>
<summary><b>11. More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19789) • [📄 arXiv](https://arxiv.org/abs/2610.19789) • [📥 PDF](https://arxiv.org/pdf/2610.19789)

**💻 Code:** [⭐ Code](https://github.com/aim-uofa/Self-Distillation-AgentRL) • [⭐ Code](https://github.com/huggingface)

> We present a large-scale, systematic evaluation of self-distillation methods in agentic reinforcement learning, revealing that existing methods struggle to consistently outperform GRPO despite increased computational costs. We hope our work provid...

</details>

<details>
<summary><b>12. KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14448) • [📄 arXiv](https://arxiv.org/abs/2610.14448) • [📥 PDF](https://arxiv.org/pdf/2610.14448)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share KV4-RL! We investigate KV cache quantization for accelerating asynchronous RLVR rollouts. Our key finding is that asynchronous scheduling makes KV cache a major performance bottleneck, while aggressive INT4 quantization can compro...

</details>

<details>
<summary><b>13. Towards Agentic Robots: Model, Data, Environment, and Harness</b> ⭐ 25</summary>

<br/>

**👥 Authors:** Kaituo Feng, Dongming Wu, bingaochen, YijiaFan, J017athan

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20442) • [📄 arXiv](https://arxiv.org/abs/2610.20442) • [📥 PDF](https://arxiv.org/pdf/2610.20442)

**💻 Code:** [⭐ Code](https://github.com/chonghanqin/Awesome-Agentic-Robots) • [⭐ Code](https://github.com/huggingface)

> Repo: https://github.com/chonghanqin/Awesome-Agentic-Robots

</details>

<details>
<summary><b>14. Hybrid Reasoning Agents</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18861) • [📄 arXiv](https://arxiv.org/abs/2610.18861) • [📥 PDF](https://arxiv.org/pdf/2610.18861)

**💻 Code:** [⭐ Code](https://github.com/togethercomputer/HybridAgent) • [⭐ Code](https://github.com/huggingface)

> Your LLM agent has to think out loud, token by token, before it can search, run code, or act in the world. We humans don’t. We ponder in silence and speak when it matters. Human language was never meant to be the limit of machine thought. Introduc...

</details>

<details>
<summary><b>15. Super-Resolution in The Right Latent Space: A Frozen Vision-Foundation Substrate</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.04781) • [📄 arXiv](https://arxiv.org/abs/2610.04781) • [📥 PDF](https://arxiv.org/pdf/2610.04781)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> RAE-based super-resolution

</details>

<details>
<summary><b>16. APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18097) • [📄 arXiv](https://arxiv.org/abs/2610.18097) • [📥 PDF](https://arxiv.org/pdf/2610.18097)

**💻 Code:** [⭐ Code](https://github.com/siruizhang30/APT) • [⭐ Code](https://github.com/huggingface)

> Better models. Smarter training data. Different image models struggle with different things. A fixed training set cannot keep up with every model’s evolving strengths and weaknesses. APT makes post-training adaptive. Three agents work together to ...

</details>

<details>
<summary><b>17. HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.02089) • [📄 arXiv](https://arxiv.org/abs/2610.02089) • [📥 PDF](https://arxiv.org/pdf/2610.02089)

**💻 Code:** [⭐ Code](https://github.com/SNU-PI/HumanoidToolBench) • [⭐ Code](https://github.com/huggingface)

> Can humanoids choose the right tool and then actually use it? We introduce HumanoidToolBench, an 18-task benchmark evaluating humanoid tool selection and execution across three scenarios, three execution levels, and two tool-set modes. We also int...

</details>

<details>
<summary><b>18. RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chenxi Zhou, Chao Yin, Yinhao Xu, Bohan Yu, yuanchenhao

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19698) • [📄 arXiv](https://arxiv.org/abs/2610.19698) • [📥 PDF](https://arxiv.org/pdf/2610.19698)

**💻 Code:** [⭐ Code](https://github.com/yuan247/RuleTrek) • [⭐ Code](https://github.com/huggingface)

> RuleTrek is a multi-domain benchmark for evaluating agentic rule reasoning in complex scenarios. Unlike existing rule-reasoning benchmarks that represent scenarios using only a few factual statements, RuleTrek features complex, multi-file scenario...

</details>

<details>
<summary><b>19. τ-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through Real-World User Emotions</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19560) • [📄 arXiv](https://arxiv.org/abs/2610.19560) • [📥 PDF](https://arxiv.org/pdf/2610.19560)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/sahsaeedi/tau-emotion-bench)

> In long-horizon tool-calling tasks, LLM agents can fail not only because of tool-use errors, but also because of ineffective interaction with users. Yet existing benchmarks largely assume cooperative and behaviorally stable users, leaving the effe...

</details>

<details>
<summary><b>20. RAR: Rate-Adaptive Rollout for Time-Consistent Interactive World Models</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Zeke Xie, Shengju Qian, Yihua Du, Dongyu Yan, LazySheeep

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16302) • [📄 arXiv](https://arxiv.org/abs/2610.16302) • [📥 PDF](https://arxiv.org/pdf/2610.16302)

**💻 Code:** [⭐ Code](https://github.com/HKUST-LongGroup/RAR) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We’re sharing RAR (Rate-Adaptive Rollout), a framework for controllable generation rates in interactive world models. Most world models run at a fixed temporal rate, so differences in hardware throughput can unintentionally speed up o...

</details>

<details>
<summary><b>21. SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Wenxiang Hu, Congfeng Cao, Qianru Meng, din0s, X-iZhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20431) • [📄 arXiv](https://arxiv.org/abs/2610.20431) • [📥 PDF](https://arxiv.org/pdf/2610.20431)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Something I keep noticing with AI scientist agents: running more of them in parallel doesn’t make them smarter by default. Mostly they throw away each other’s work. 🧪 Picture a lab where a student has a promising idea but botches the implementatio...

</details>

<details>
<summary><b>22. SkillMarker: A KGW-Based Watermarking Method for Agent Skill Ownership Verification</b> ⭐ 4</summary>

<br/>

**👥 Authors:** Yantao Jia, Tao Zhang, Gang Wu, Lifeng Wang, Alan Tang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15725) • [📄 arXiv](https://arxiv.org/abs/2610.15725) • [📥 PDF](https://arxiv.org/pdf/2610.15725)

**💻 Code:** [⭐ Code](https://github.com/fuxi-ailabs/SkillMarker) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>23. GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Madalina Ciobanu, Zhifeng Li, Jiacheng Tang, Jiahao Tian, Qingsong Xie

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19100) • [📄 arXiv](https://arxiv.org/abs/2610.19100) • [📥 PDF](https://arxiv.org/pdf/2610.19100)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/PrentisAI/GroundGUI)

> ScreenRef and Distillation-to-Reinforcement Learning (D2RL) are the core contributions of GroundGUI. ScreenRef is a high-quality GUI grounding dataset spanning desktop, web, and mobile environments. It pairs diverse screenshots with referring expr...

</details>

<details>
<summary><b>24. Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18284) • [📄 arXiv](https://arxiv.org/abs/2610.18284) • [📥 PDF](https://arxiv.org/pdf/2610.18284)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 Great image, garbled text? Meet PixText, our approach to precise and efficient scene-text refinement. By generating only the target regions directly in pixel space, PixText corrects small text and complex characters while preserving the surround...

</details>

<details>
<summary><b>25. Diagnosing and Correcting Reward Hacking in Verifiable Instruction Following</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Donghoon Kim, Hyesoo Hong, Hamish Ivison, Wooseok Seo, sangyon

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19525) • [📄 arXiv](https://arxiv.org/abs/2610.19525) • [📥 PDF](https://arxiv.org/pdf/2610.19525)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> .

</details>

<details>
<summary><b>26. ProgAgent: Learning Tool Orchestration through Programmatic Training</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14774) • [📄 arXiv](https://arxiv.org/abs/2610.14774) • [📥 PDF](https://arxiv.org/pdf/2610.14774)

**💻 Code:** [⭐ Code](https://github.com/hkust-nlp/ProgAgent) • [⭐ Code](https://github.com/huggingface)

> 🌐 Project: https://llleoli.github.io/ProgAgent 📄 Paper: https://arxiv.org/abs/2610.14774 💻 Code: https://github.com/hkust-nlp/ProgAgent

</details>

<details>
<summary><b>27. Apertus 1.5: From Open Text Models to Open Multimodal Reasoners</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15542) • [📄 arXiv](https://arxiv.org/abs/2610.15542) • [📥 PDF](https://arxiv.org/pdf/2610.15542)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We release technical report for Apertus 1.5 - a series of fully open multimodal reasoning models. In the report we cover how we extended our previous v1 with continued pretraining and post-training to multimodal setup through vision tower-free eas...

</details>

<details>
<summary><b>28. SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20609) • [📄 arXiv](https://arxiv.org/abs/2610.20609) • [📥 PDF](https://arxiv.org/pdf/2610.20609)

**💻 Code:** [⭐ Code](https://github.com/ASGuard-UCI/safedrive-vla) • [⭐ Code](https://github.com/huggingface)

> Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructi...

</details>

<details>
<summary><b>29. Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18248) • [📄 arXiv](https://arxiv.org/abs/2610.18248) • [📥 PDF](https://arxiv.org/pdf/2610.18248)

**💻 Code:** [⭐ Code](https://github.com/MilkThink-Lab/Awesome-Benchmark-Compression) • [⭐ Code](https://github.com/huggingface)

> First Survey of Benchmark Compression for Efficient Evaluation of LLMs

</details>

<details>
<summary><b>30. Long-Horizon RL Needs Muon</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20256) • [📄 arXiv](https://arxiv.org/abs/2610.20256) • [📥 PDF](https://arxiv.org/pdf/2610.20256)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Long-horizon agents must coordinate reasoning, tool use, and environment feedback over extended interactions. Learning from sparse outcome rewards requires weighting trajectories of different lengths and updating the policy while rollouts are stil...

</details>

<details>
<summary><b>31. Acting Through Registers</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17638) • [📄 arXiv](https://arxiv.org/abs/2610.17638) • [📥 PDF](https://arxiv.org/pdf/2610.17638)

**💻 Code:** [⭐ Code](https://github.com/Z1zyw/RegisterWAM) • [⭐ Code](https://github.com/huggingface)

> World Action Models (WAMs) use generative visual representations to condition robot actions, yet how these representations organize action-relevant information remains poorly understood. We identify persistent high-norm spatial outliers in WAM rep...

</details>

<details>
<summary><b>32. Joint Subspace Sparse Attention for Efficient Long-Context Decoding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19026) • [📄 arXiv](https://arxiv.org/abs/2610.19026) • [📥 PDF](https://arxiv.org/pdf/2610.19026)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/jiwonsong-dev/JSSA)

> New token-level decoding-time sparse attention paper

</details>

<details>
<summary><b>33. VITAL: From Visual Motion to Precise Action</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20604) • [📄 arXiv](https://arxiv.org/abs/2610.20604) • [📥 PDF](https://arxiv.org/pdf/2610.20604)

**💻 Code:** [⭐ Code](https://github.com/worldbench/VITAL) • [⭐ Code](https://github.com/huggingface)

> World-action models aim to turn visual anticipation into driving decisions, yet typically train action experts on trajectory representations defined independently of visual dynamics. This motivates deriving action targets directly from visual moti...

</details>

<details>
<summary><b>34. TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19551) • [📄 arXiv](https://arxiv.org/abs/2610.19551) • [📥 PDF](https://arxiv.org/pdf/2610.19551)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🔍 Readable doesn’t always mean correctly rendered. Meet TextVerifier, our model for detecting subtle errors in generated Chinese text—from missing strokes to malformed components—that OCR and vision-language models can overlook. By representing ch...

</details>

<details>
<summary><b>35. LLM-to-Flow Distillation: Teaching Natural Language Goals to Scientific Generators</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17246) • [📄 arXiv](https://arxiv.org/abs/2610.17246) • [📥 PDF](https://arxiv.org/pdf/2610.17246)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/FedericoDiGennaro/LLM-to-Flow-Distillation)

> We’re bringing natural-language control to any scientific generator. We are very excited to introduce LLM-to-Flow Distillation (LFD), a method to adapt scientific generators to high-level natural-language discovery goals. Starting from textual goa...

</details>

<details>
<summary><b>36. Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Rui Zhao, Linjie Li, Hu Jian Guo, Junchao Yi, zhuobai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20220) • [📄 arXiv](https://arxiv.org/abs/2610.20220) • [📥 PDF](https://arxiv.org/pdf/2610.20220)

**💻 Code:** [⭐ Code](https://github.com/CSU-JPG/Glance-Forcing) • [⭐ Code](https://github.com/huggingface)

> we propose Glance Forcing, a lightweight distillation framework that decouples the denoising trajectory into two complementary slow and fast experts, each guided by a tailored, stage-specific objective. This decoupling further reveals a general me...

</details>

<details>
<summary><b>37. BigCell: Generating Gigapixel Whole-Slide Images</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14261) • [📄 arXiv](https://arxiv.org/abs/2610.14261) • [📥 PDF](https://arxiv.org/pdf/2610.14261)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Project page: https://histodiffusion.github.io/docs/projects/bigcell/

</details>

<details>
<summary><b>38. What Makes a Social Agent's Interactions Effective? Learning from Verifiable Outcomes in Paired Worlds</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20195) • [📄 arXiv](https://arxiv.org/abs/2610.20195) • [📥 PDF](https://arxiv.org/pdf/2610.20195)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Effective social interaction requires more than fluent responses: agents must reach plans that fit the participants' needs and circumstances. Existing evaluations of social agents mainly rely on LLM judges that rate the conversation, without check...

</details>

<details>
<summary><b>39. Physical Time as a Missing Dimension of Robot Policy Memory Dynamics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20524) • [📄 arXiv](https://arxiv.org/abs/2610.20524) • [📥 PDF](https://arxiv.org/pdf/2610.20524)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Robot policies act in physical time, but their memories are often organized around observation steps. What happens when these two clocks disagree? The same observation history can require different actions depending on how much time has elapsed. A...

</details>

<details>
<summary><b>40. Exploring the Limits of Combinatorial Generalization in Embodied Manipulation</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.15425) • [📄 arXiv](https://arxiv.org/abs/2610.15425) • [📥 PDF](https://arxiv.org/pdf/2610.15425)

**💻 Code:** [⭐ Code](https://github.com/AutoLab-SAI-SJTU/RoboCombine) • [⭐ Code](https://github.com/huggingface)

> In embodied manipulation, Vision Language Action (VLA) models can execute atomic skills, but long-horizon manipulation requires recombining these skills without demonstrations for every skill combination. The full instruction route treats skill ch...

</details>

<details>
<summary><b>41. DecisionRobust: Benchmarking Robustness for JEV Style Decision Models Across Text and Vision</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yongkang Du, Hanyu Wang, Yurui Chang, Zhongye Liu, yflantmy

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19118) • [📄 arXiv](https://arxiv.org/abs/2610.19118) • [📥 PDF](https://arxiv.org/pdf/2610.19118)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce DecisionRobust, a benchmark for testing the robustness of JEV-style decision models across text and vision, including classification, routing, tool selection, and robotics scenarios. Our public release contains 1,058 curated attack ex...

</details>

<details>
<summary><b>42. Continuum Attention</b> ⭐ 0</summary>

<br/>

**👥 Authors:** akhadangi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20586) • [📄 arXiv](https://arxiv.org/abs/2610.20586) • [📥 PDF](https://arxiv.org/pdf/2610.20586)

**💻 Code:** [⭐ Code](https://github.com/akhadangi/continuum-attention) • [⭐ Code](https://github.com/huggingface)

> We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve.

</details>

<details>
<summary><b>43. StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17309) • [📄 arXiv](https://arxiv.org/abs/2610.17309) • [📥 PDF](https://arxiv.org/pdf/2610.17309)

**💻 Code:** [⭐ Code](https://github.com/StartLuxLabs/StartLux-Decision) • [⭐ Code](https://github.com/huggingface)

> We introduce StartLux-Decision, decision models from 0.8B to 27B parameters that combine efficient single-pass prediction with adaptive, confidence-guided reasoning. The Instant models use bidirectional attention in full-attention layers to improv...

</details>

<details>
<summary><b>44. ProbabilityBench: Model Evaluation and Calibration with Exact Ground-Truth Uncertainty</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17016) • [📄 arXiv](https://arxiv.org/abs/2610.17016) • [📥 PDF](https://arxiv.org/pdf/2610.17016)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ishida-lab/ProbabilityBench)

> Decision models like Jev are designed to predict class probabilities directly, but how can we tell whether their predictions are actually correct? Suppose a decision model predicts a 70% probability that an instance belongs to the positive class i...

</details>

<details>
<summary><b>45. Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17771) • [📄 arXiv](https://arxiv.org/abs/2610.17771) • [📥 PDF](https://arxiv.org/pdf/2610.17771)

**💻 Code:** [⭐ Code](https://github.com/LiXin97/ReMaRk) • [⭐ Code](https://github.com/huggingface)

> Project Page: https://lixin.ai/ReMaRk/

</details>

<details>
<summary><b>46. Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19696) • [📄 arXiv](https://arxiv.org/abs/2610.19696) • [📥 PDF](https://arxiv.org/pdf/2610.19696)

**💻 Code:** [⭐ Code](https://github.com/LiXin97/SYNC) • [⭐ Code](https://github.com/huggingface)

> Project page: https://lixin.ai/SYNC/

</details>

<details>
<summary><b>47. Scaling Online Optimal Transport Minibatches for Flow Matching</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18838) • [📄 arXiv](https://arxiv.org/abs/2610.18838) • [📥 PDF](https://arxiv.org/pdf/2610.18838)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A central challenge in scaling flow models is maintaining stability in training and integration. In flow matching, this stability depends critically on how source samples are paired with data. Independent random pairing introduces substantial stoc...

</details>

<details>
<summary><b>48. Latent Compaction with Test-Time Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20582) • [📄 arXiv](https://arxiv.org/abs/2610.20582) • [📥 PDF](https://arxiv.org/pdf/2610.20582)

**💻 Code:** [⭐ Code](https://github.com/thunlp/latent-compaction) • [⭐ Code](https://github.com/huggingface)

> New SOTA performance for KV compression/context representation!

</details>

<details>
<summary><b>49. NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime</b> ⭐ 60</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.10787) • [📄 arXiv](https://arxiv.org/abs/2610.10787) • [📥 PDF](https://arxiv.org/pdf/2610.10787)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/metacognitionai/NavGPT-3)

> Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide...

</details>

<details>
<summary><b>50. SWEeper-Bench: Can Agents Discover Bugs in Interactive Software?</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14096) • [📄 arXiv](https://arxiv.org/abs/2610.14096) • [📥 PDF](https://arxiv.org/pdf/2610.14096)

**💻 Code:** [⭐ Code](https://github.com/zlab-princeton/sweeper-bench) • [⭐ Code](https://github.com/huggingface)

> SWEeper-Bench tests whether coding agents can find and fix bugs that nobody has reported yet. It has 200 tasks, each built from a real bug fix in a different open-source web app. The agent gets the codebase and an open-ended request such as "Find ...

</details>

<details>
<summary><b>51. MimicX: Policy-in-the-Loop Supervision Refinement for Video-Driven Humanoid Motion Tracking</b> ⭐ 27</summary>

<br/>

**👥 Authors:** Yifan Liao, Feiyang You, Xuhao Liu, Chenglong Zhang, Shuaijun Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09055) • [📄 arXiv](https://arxiv.org/abs/2610.09055) • [📥 PDF](https://arxiv.org/pdf/2610.09055)

**💻 Code:** [⭐ Code](https://github.com/NEBULIS-Lab/MimicX) • [⭐ Code](https://github.com/huggingface)

> 🚀 MimicX: Turning Execution Failures into Better Humanoid Learning A human video shows what a motion should look like. A physics-based rollout reveals what a robot still needs to learn. MimicX connects the two. Rather than repeatedly training agai...

</details>

<details>
<summary><b>52. Diff Diffusion: Predicting Edit Paths with Diffusion Models for Efficient Code Editing</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ningyuan Sun, Zhiwen Deng, Bo Jiang, Hao Jiang, Xiaolong Xu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17831) • [📄 arXiv](https://arxiv.org/abs/2610.17831) • [📥 PDF](https://arxiv.org/pdf/2610.17831)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Diffusion large language models (dLLMs) are appealing for code generation because they can update many tokens in parallel, yet many are optimized for sequence synthesis rather than edit prediction. This setting is poorly matched to modern AI-assis...

</details>

<details>
<summary><b>53. The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20456) • [📄 arXiv](https://arxiv.org/abs/2610.20456) • [📥 PDF](https://arxiv.org/pdf/2610.20456)

**💻 Code:** [⭐ Code](https://github.com/IanMagnusson/COUNT) • [⭐ Code](https://github.com/huggingface)

> COUNT adds an n-gram embedding to a transformer without adding learned parameters. At each position, it looks up the most frequent next tokens in a table of corpus n-gram counts held in CPU RAM, and adds the model’s own output-head rows for those ...

</details>

<details>
<summary><b>54. Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shaofeng Zou, Nathaniel D. Bastian, Yingbin Liang, Sen Lin, CliverChen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17893) • [📄 arXiv](https://arxiv.org/abs/2610.17893) • [📥 PDF](https://arxiv.org/pdf/2610.17893)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🚀 Can we train LLMs to collaborate, rather than only design better multi-agent workflows? I'm sharing our new preprint, Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards (CoSIR). Most LLM post-training focuses on chat...

</details>

<details>
<summary><b>55. Rethinking LLM-Guided Visual Question Answering: Does Deeper Knowledge Integration Really Help?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dhruv Bansal, Priyam Srivastava, Sameer Madhav D., Vijay Kumar, rishii100

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17079) • [📄 arXiv](https://arxiv.org/abs/2610.17079) • [📥 PDF](https://arxiv.org/pdf/2610.17079)

**💻 Code:** [⭐ Code](https://github.com/rishii100/Rethinking-LLM-Guided-Visual-Question-Answering-Does-Deeper-Knowledge-Integration-Really-Help) • [⭐ Code](https://github.com/huggingface)

> Does deeper knowledge integration always improve VQA? We compare late fusion and attention injection using LLM generated guidance, finding that the simpler late fusion strategy performs better under data scarce conditions. Curious to hear the comm...

</details>

<details>
<summary><b>56. StreamErase: Towards Ultra-Fast Streaming Video Erasing</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yinggui Wang, Jinkui Ren, Xiantao Zhang, Xiaobing Tu, zhuobai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20137) • [📄 arXiv](https://arxiv.org/abs/2610.20137) • [📥 PDF](https://arxiv.org/pdf/2610.20137)

**💻 Code:** [⭐ Code](https://github.com/zhuobaidong/StreamErase) • [⭐ Code](https://github.com/huggingface)

> We progressively transfer the erasing capability from a powerful bidirectional foundation model to an efficient unidirectional streaming eraser, enabling long-horizon erasing without sacrificing visual fidelity.

</details>

<details>
<summary><b>57. AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Cheng Jin, Ziyuan Zhou, Han Qi, Xiaoyu Wen, lalalamdbf

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19422) • [📄 arXiv](https://arxiv.org/abs/2610.19422) • [📥 PDF](https://arxiv.org/pdf/2610.19422)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/lalalamdbf/AgentSafeEvo)

> Hi, I’m one of the authors of AgentSafeEvo. We introduce an adversarial co-evolution framework that jointly trains attacker and defender LLM agents for safer multi-turn tool use. We evaluate across seven safety and capability benchmarks and releas...

</details>

<details>
<summary><b>58. Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ryan Ji, Yicheng Jiang, Dongming Wu, Jiaxu Wang, Yifan Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05230) • [📄 arXiv](https://arxiv.org/abs/2610.05230) • [📥 PDF](https://arxiv.org/pdf/2610.05230)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Most vision-language-action models represent future motion as fixed-rate action chunks, tying temporal resolution and prediction horizon to a fixed output budget. This pointwise representation wastes capacity on highly correlated neighboring actio...

</details>

<details>
<summary><b>59. Jag: Direct Box Prediction for Efficient Visual Grounding</b> ⭐ 19</summary>

<br/>

**👥 Authors:** Dongming Zhang, Zijin Du, Hao Wu, Ke Lu, xyzzzh

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.13239) • [📄 arXiv](https://arxiv.org/abs/2610.13239) • [📥 PDF](https://arxiv.org/pdf/2610.13239)

**💻 Code:** [⭐ Code](https://github.com/xyzzzh/Jag) • [⭐ Code](https://github.com/huggingface)

> We introduce Jag , a 0.8B visual grounding model that predicts bounding boxes in a single forward pass, without autoregressive coordinate generation. Jag improves over its base model on all five test splits and achieves overall Acc@0.5 comparable ...

</details>

<details>
<summary><b>60. Generative World Simulation with DAO and JING</b> ⭐ 285</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19726) • [📄 arXiv](https://arxiv.org/abs/2610.19726) • [📥 PDF](https://arxiv.org/pdf/2610.19726)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/XGEN-Labs/XGEN-JING)

> DAO (道) computes the shared world’s state and dynamics, while JING (镜) generates each observer’s first-person experience. Actions change the world; those changes shape what humans and agents experience and how they act next. This continuous loop c...

</details>

<details>
<summary><b>61. SyncReward: Human-Aligned Synchronization Reward for Audio-Visual Generation</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16338) • [📄 arXiv](https://arxiv.org/abs/2610.16338) • [📥 PDF](https://arxiv.org/pdf/2610.16338)

**💻 Code:** [⭐ Code](https://github.com/WeChatCV/SyncReward) • [⭐ Code](https://github.com/huggingface)

> Recent years have witnessed rapid progress in joint audio--visual generation. However, audio--visual synchronization remains a challenge, as generated speech and sound often temporally misalign with visual events. A key bottleneck is the lack of h...

</details>

<details>
<summary><b>62. G^3VLA: Geometric Inductive Bias for Vision-Language-Action Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yanheng Zhu, Khuyen Pham, Artur Habuda, ColinSkywalker, pengyue-polaron

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.24472) • [📄 arXiv](https://arxiv.org/abs/2606.24472) • [📥 PDF](https://arxiv.org/pdf/2606.24472)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce G³VLA, a camera-aware module that helps pretrained VLAs use the geometric relationships between multiple camera views. It combines intrinsic-conditioned ray embeddings, projective positional encoding, and bidirectional cross-view fusi...

</details>

<details>
<summary><b>63. MA-Bench: Measuring Operational Planning in Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yuan Xue, Phil Sage, Robert Sincero, Rodney Lafuente-Mercado

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19138) • [📄 arXiv](https://arxiv.org/abs/2610.19138) • [📥 PDF](https://arxiv.org/pdf/2610.19138)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 63 |
| 📅 Today | [`2026-10-15.json`](data/daily/2026-10-15.json) | 63 |
| 📆 This Week | [`2026-W41.json`](data/weekly/2026-W41.json) | 194 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 880 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-15 | 63 | [View JSON](data/daily/2026-10-15.json) |
| 📄 2026-10-14 | 69 | [View JSON](data/daily/2026-10-14.json) |
| 📄 2026-10-13 | 15 | [View JSON](data/daily/2026-10-13.json) |
| 📄 2026-10-12 | 47 | [View JSON](data/daily/2026-10-12.json) |
| 📄 2026-10-11 | 72 | [View JSON](data/daily/2026-10-11.json) |
| 📄 2026-10-10 | 72 | [View JSON](data/daily/2026-10-10.json) |
| 📄 2026-10-09 | 55 | [View JSON](data/daily/2026-10-09.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W41 | 194 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |
| 📅 2026-W38 | 146 | [View JSON](data/weekly/2026-W38.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 880 | [View JSON](data/monthly/2026-10.json) |
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
