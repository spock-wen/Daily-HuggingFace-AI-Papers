<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-54-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-8932+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">54</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">54</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">1171</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">8932+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** October 19, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Has GPT-6-Astra Achieved Embodied Intelligence?</b> ⭐ 76</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22471) • [📄 arXiv](https://arxiv.org/abs/2610.22471) • [📥 PDF](https://arxiv.org/pdf/2610.22471)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenSenseNova/SenseNova-RoboRSI)

> Has GPT-6-Astra Achieved Embodied Intelligence? Embodied competence — largely yes. Practical embodied intelligence — not yet.

</details>

<details>
<summary><b>2. BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for Real-World Business</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20424) • [📄 arXiv](https://arxiv.org/abs/2610.20424) • [📥 PDF](https://arxiv.org/pdf/2610.20424)

**💻 Code:** [⭐ Code](https://github.com/ant-intl/BizAgentBench) • [⭐ Code](https://github.com/huggingface)

> AI agents are moving from answering questions to executing business workflows, where actions change business states, commit resources, and shape later decisions. We introduce BizAgentBench, a long-horizon benchmark grounded in workflows from a glo...

</details>

<details>
<summary><b>3. Learning to Think and Explore in 3D World</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21783) • [📄 arXiv](https://arxiv.org/abs/2610.21783) • [📥 PDF](https://arxiv.org/pdf/2610.21783)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We study how vision-language models (VLMs) can learn to think and actively explore in 3D space. Instead of providing multi-view images, videos, or 3D representations to the model, we preserve the native visual encoding of VLMs, i.e., a single imag...

</details>

<details>
<summary><b>4. Into the Unknown: Benchmarking AI agents on open scientific research problems</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19159) • [📄 arXiv](https://arxiv.org/abs/2610.19159) • [📥 PDF](https://arxiv.org/pdf/2610.19159)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/prometheus-eval/into-the-unknown)

> Can AI agents carry out research on open scientific problems? We introduce Into the Unknown, a benchmark that provides an agent with a science paper along with a research direction to pursue and tasks it to write a follow-up paper. We work with sc...

</details>

<details>
<summary><b>5. Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18784) • [📄 arXiv](https://arxiv.org/abs/2610.18784) • [📥 PDF](https://arxiv.org/pdf/2610.18784)

**💻 Code:** [⭐ Code](https://github.com/Ethannju/carryon) • [⭐ Code](https://github.com/huggingface)

> Long-horizon agents often keep revisiting how work was done, even when the results are already preserved in files and task state. We introduce CarryOn, an object-oriented context runtime that enables agents to continue from reusable task progress ...

</details>

<details>
<summary><b>6. HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents</b> ⭐ 22</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23479) • [📄 arXiv](https://arxiv.org/abs/2610.23479) • [📥 PDF](https://arxiv.org/pdf/2610.23479)

**💻 Code:** [⭐ Code](https://github.com/HexaFuture/HexaShell) • [⭐ Code](https://github.com/huggingface)

> A thin harness in which a coding agent drives a robot from RGB images and writes its own tools; frozen tools for the 42 RoboDojo tasks

</details>

<details>
<summary><b>7. LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09872) • [📄 arXiv](https://arxiv.org/abs/2610.09872) • [📥 PDF](https://arxiv.org/pdf/2610.09872)

**💻 Code:** [⭐ Code](https://github.com/RaymondVoldemortFu/LiveMACE) • [⭐ Code](https://github.com/huggingface)

> We introduce LiveMACE , a benchmark that uses live financial markets to evaluate LLM agent capabilities. Static benchmark questions can enter training data; future market events have yet to occur. This makes evolving markets a natural environment ...

</details>

<details>
<summary><b>8. Scene-Designer: Learning Design Intelligence for Agentic 3D Scene Generation</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23121) • [📄 arXiv](https://arxiv.org/abs/2610.23121) • [📥 PDF](https://arxiv.org/pdf/2610.23121)

**💻 Code:** [⭐ Code](https://github.com/ZJU-OmniAI/Scene-Designer) • [⭐ Code](https://github.com/huggingface)

> Generating complete, coherent, and usable 3D scenes from natural language requires design intelligence —the ability to both design scenes and critique their quality. We introduce Scene-Designer, an agentic framework that learns these complementary...

</details>

<details>
<summary><b>9. Speculative Sampling in Interactive Video Generation</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20556) • [📄 arXiv](https://arxiv.org/abs/2610.20556) • [📥 PDF](https://arxiv.org/pdf/2610.20556)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yubo-Shankui/SpeculativeSampling)

> Speculative Sampling is a serving method for autoregressive video generation. It preserves the strong modeling capability of large bidirectional attention windows while retaining the low-latency interaction of small bidirectional attention windows...

</details>

<details>
<summary><b>10. OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14157) • [📄 arXiv](https://arxiv.org/abs/2610.14157) • [📥 PDF](https://arxiv.org/pdf/2610.14157)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenMobile2/OpenMobile2-Code) • [⭐ Code](https://github.com/OpenMobile2/MobileGym-plusplus)

> 🚀 Introducing OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools We're excited to share OpenMobile-2 , our latest work on mobile agents, with environments, data, benchmarks, and models fully open-sourced...

</details>

<details>
<summary><b>11. BridgeWAM: Bridging Video and Action Experts via Latent Bridge Queries</b> ⭐ 22</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14746) • [📄 arXiv](https://arxiv.org/abs/2610.14746) • [📥 PDF](https://arxiv.org/pdf/2610.14746)

**💻 Code:** [⭐ Code](https://github.com/jxfang04/BridgeWAM-code) • [⭐ Code](https://github.com/huggingface)

> We hope this work offers a new direction for WAM architecture design beyond MoT: a learnable, capacity-limited latent space that guides the Video Expert to produce representations better suited for retrieval by the Action Expert, while enabling a ...

</details>

<details>
<summary><b>12. From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21767) • [📄 arXiv](https://arxiv.org/abs/2610.21767) • [📥 PDF](https://arxiv.org/pdf/2610.21767)

**💻 Code:** [⭐ Code](https://github.com/uncertainty2019/PhysClosureBench) • [⭐ Code](https://github.com/huggingface)

> Can AI agents do more than produce plausible calculations—can they establish a well-supported scientific answer? PhysClosureBench leaves the investigation to the agent. Across 50 physics tasks, we evaluate both the scientific work accomplished and...

</details>

<details>
<summary><b>13. Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23181) • [📄 arXiv](https://arxiv.org/abs/2610.23181) • [📥 PDF](https://arxiv.org/pdf/2610.23181)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We are excited to share TreeOPSD (Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning). Training long-horizon LLM agents with verifiable rewards faces two practical bottlenecks: terminal rewards alone make turn-level ...

</details>

<details>
<summary><b>14. Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Aldeida Aleti, Chunyang Chen, Hongyu Zhang, jianguda

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22169) • [📄 arXiv](https://arxiv.org/abs/2610.22169) • [📥 PDF](https://arxiv.org/pdf/2610.22169)

**💻 Code:** [⭐ Code](https://github.com/jianguda/lexframe) • [⭐ Code](https://github.com/huggingface)

> Lenses such as the logit and Jacobian lenses misread the residual stream in the middle layers of a language model. They read all hidden states of a layer alike, through the prediction head or a map fitted to that layer. Blind to context, they ofte...

</details>

<details>
<summary><b>15. RAP: A Dataset for Paper-to-Poster Generation via Declarative Markup from Human-Crafted Exemplars</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23230) • [📄 arXiv](https://arxiv.org/abs/2610.23230) • [📥 PDF](https://arxiv.org/pdf/2610.23230)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/VincentHancoder/RAP)

> No abstract available.

</details>

<details>
<summary><b>16. Execution Before Memory: Diagnosing Memory Failures in Video World Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23542) • [📄 arXiv](https://arxiv.org/abs/2610.23542) • [📥 PDF](https://arxiv.org/pdf/2610.23542)

**💻 Code:** [⭐ Code](https://github.com/HKU-MMLab/MIST) • [⭐ Code](https://github.com/huggingface)

> An interesting finding in video models, you can have a reference for explorations!

</details>

<details>
<summary><b>17. DLite: History-free Speculative Decoding for Agentic AI</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23787) • [📄 arXiv](https://arxiv.org/abs/2610.23787) • [📥 PDF](https://arxiv.org/pdf/2610.23787)

**💻 Code:** [⭐ Code](https://github.com/SJTU-DAI-Sys/DLite) • [⭐ Code](https://github.com/huggingface)

> Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workl...

</details>

<details>
<summary><b>18. OfficeTown: Generative Organizations for Evolving Agent Intelligence</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23194) • [📄 arXiv](https://arxiv.org/abs/2610.23194) • [📥 PDF](https://arxiv.org/pdf/2610.23194)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> OfficeTown is a generative organizational simulation framework that creates thousands of persistent, tool-enabled professional work environments across diverse domains, generating realistic long-horizon tasks, contextual materials, agent trajector...

</details>

<details>
<summary><b>19. DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23839) • [📄 arXiv](https://arxiv.org/abs/2610.23839) • [📥 PDF](https://arxiv.org/pdf/2610.23839)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Gen-Verse/DiscoveryRSI)

> Code: https://github.com/Gen-Verse/DiscoveryRSI

</details>

<details>
<summary><b>20. Can Visual Generation Expand What Unified Multimodal Models Know?</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21459) • [📄 arXiv](https://arxiv.org/abs/2610.21459) • [📥 PDF](https://arxiv.org/pdf/2610.21459)

**💻 Code:** [⭐ Code](https://github.com/kevinlllee/Knowledge-Transfer-Probing) • [⭐ Code](https://github.com/huggingface)

> We introduce Knowledge Transfer Probing (KTP) to test whether new facts supplied only through images during generation training become accessible through text-only question answering. Across three unified multimodal models and seven knowledge cate...

</details>

<details>
<summary><b>21. MOSS-Image Technical Report</b> ⭐ 741</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23374) • [📄 arXiv](https://arxiv.org/abs/2610.23374) • [📥 PDF](https://arxiv.org/pdf/2610.23374)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenMOSS/MOSS-Image)

> MOSS-Image Technical Report

</details>

<details>
<summary><b>22. Belief-Trajectory Energy: Measuring the Path to a Prediction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yaoning Wang, Boxian Ai, Wei Tang, SII-Molu, jhying

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.05114) • [📄 arXiv](https://arxiv.org/abs/2610.05114) • [📥 PDF](https://arxiv.org/pdf/2610.05114)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We introduce Belief-Trajectory Energy (BTE), a model-grounded measure that leverages information flowing across layers to characterize how language models progressively revise their predictions. By quantifying layerwise belief changes, BTE provide...

</details>

<details>
<summary><b>23. SciΠvot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Di Wu, Kejia Zhang, Chugang Yi, Youran Sun, Phy-Ren

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21082) • [📄 arXiv](https://arxiv.org/abs/2610.21082) • [📥 PDF](https://arxiv.org/pdf/2610.21082)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 248 cases from six months of real research.

</details>

<details>
<summary><b>24. Stuck on Shuffle: On Attribute-Object Binding in Vision-Language Models</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Dvir Samuel, Or Shimshi, Issar Tzachor, Michael Green, NetanelTamir

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22602) • [📄 arXiv](https://arxiv.org/abs/2610.22602) • [📥 PDF](https://arxiv.org/pdf/2610.22602)

**💻 Code:** [⭐ Code](https://github.com/Netanel-Tamir/Stuck-On-Shuffle) • [⭐ Code](https://github.com/huggingface)

> Retrieval is a fundamental task in multimodal systems: given an image or text query, the goal is to find the most relevant images or texts in a collection, often using a shared embedding space. Reliable retrieval requires these embeddings to captu...

</details>

<details>
<summary><b>25. OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22234) • [📄 arXiv](https://arxiv.org/abs/2610.22234) • [📥 PDF](https://arxiv.org/pdf/2610.22234)

**💻 Code:** [⭐ Code](https://github.com/OS-Copilot/OS-Helix) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We introduce OS-Helix , a computer-using agent trained to coordinate GUI interaction and code execution within a single policy. Desktop tasks often need both: the GUI exposes what users see, while code can work precisely with files an...

</details>

<details>
<summary><b>26. Xiaomi-Lens-0 Technical Report</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23279) • [📄 arXiv](https://arxiv.org/abs/2610.23279) • [📥 PDF](https://arxiv.org/pdf/2610.23279)

**💻 Code:** [⭐ Code](https://github.com/SeerRay-Lab/Xiaomi-Lens-0) • [⭐ Code](https://github.com/huggingface)

> Xiaomi-Lens-0 is a 4B multimodal model that predicts masks from internal visual representations to improve fine-grained region reasoning and referring comprehension.

</details>

<details>
<summary><b>27. OPMD: On-Policy Mechanism Distillation Beyond Output Supervision</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.14022) • [📄 arXiv](https://arxiv.org/abs/2610.14022) • [📥 PDF](https://arxiv.org/pdf/2610.14022)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Beyond output-level distillation! OPMD focuses on transferring how a teacher computes, rather than just what it predicts. By combining student-compatible intermediate states with on-policy training, it achieves stronger reasoning performance with ...

</details>

<details>
<summary><b>28. AVC-Reward: Event-Centric Audio-Video Consistency Evaluation</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22321) • [📄 arXiv](https://arxiv.org/abs/2610.22321) • [📥 PDF](https://arxiv.org/pdf/2610.22321)

**💻 Code:** [⭐ Code](https://github.com/Tsuki0512/AVC-Reward) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! 👋 We’re excited to share AVC-Reward , an event-centric reward model for evaluating audio-video consistency in modern joint audio-video generation. Existing metrics often evaluate entire clips or rely on predefined matching rules, maki...

</details>

<details>
<summary><b>29. Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23036) • [📄 arXiv](https://arxiv.org/abs/2610.23036) • [📥 PDF](https://arxiv.org/pdf/2610.23036)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ifm-ai/xllm-loop)

> fully open-sourced at: https://github.com/ifm-ai/xllm-loop

</details>

<details>
<summary><b>30. DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.17184) • [📄 arXiv](https://arxiv.org/abs/2610.17184) • [📥 PDF](https://arxiv.org/pdf/2610.17184)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Agents can write a code change in seconds, but real evals take hours (85 min for vLLM, up to 28 h for CPU design). DuoDiscover has each agent find a target to optimize and a fast eval for it, keeps those evals honest against the real one, and scal...

</details>

<details>
<summary><b>31. PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20628) • [📄 arXiv](https://arxiv.org/abs/2610.20628) • [📥 PDF](https://arxiv.org/pdf/2610.20628)

**💻 Code:** [⭐ Code](https://github.com/tuandattt/PRISM) • [⭐ Code](https://github.com/huggingface)

> The novel topology design method for multi-agent system

</details>

<details>
<summary><b>32. Dream2Discern: Learning from Hard Latent Variants for Runtime Failure Prediction in Multi-Agent Systems</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.16071) • [📄 arXiv](https://arxiv.org/abs/2610.16071) • [📥 PDF](https://arxiv.org/pdf/2610.16071)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ZBox1005/Dream2Discern)

> We’re excited to share Dream2Discern, a runtime failure auditor for multi-agent systems. During training, Dream creates hard latent variants guided by the auditor’s prediction loss, and Discern learns from them using the original outcome labels. A...

</details>

<details>
<summary><b>33. MorphAct: Robot Policies Morphing with the Worlds They Act In</b> ⭐ 19</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20019) • [📄 arXiv](https://arxiv.org/abs/2610.20019) • [📥 PDF](https://arxiv.org/pdf/2610.20019)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MINT-SJTU/MorphAct)

> Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions. However, existing robot policies use shared parameters that remain fixed across interaction contexts. When dif...

</details>

<details>
<summary><b>34. Embeddings Are Overpriced? A Frozen 16 MB Vocabulary for Small and Ternary Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sai Kiran Bathula

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22428) • [📄 arXiv](https://arxiv.org/abs/2610.22428) • [📥 PDF](https://arxiv.org/pdf/2610.22428)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> In small language models the vocabulary table is the biggest part: 168M of 268M parameters in Gemma 3 270M. This paper replaces it with one frozen 512-bit code per token, derived from Gemma 3's own embedding and never trained. Trained on the same ...

</details>

<details>
<summary><b>35. FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.07898) • [📄 arXiv](https://arxiv.org/abs/2610.07898) • [📥 PDF](https://arxiv.org/pdf/2610.07898)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Excited to share FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents ! How can we train coding agents to learn from failed attempts? FC-SWE makes recovery part of reinforcement learning. After a patch fails verification, we...

</details>

<details>
<summary><b>36. Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18082) • [📄 arXiv](https://arxiv.org/abs/2610.18082) • [📥 PDF](https://arxiv.org/pdf/2610.18082)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>37. PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Lichao Sun, Yuxuan Zhang, Ziqian Zhang, Zhiling Yan, songdj

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21046) • [📄 arXiv](https://arxiv.org/abs/2610.21046) • [📥 PDF](https://arxiv.org/pdf/2610.21046)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/OpenLAIR/PremiseCheck)

> TL;DR: Review comments, written by humans or AI, sometimes misstate what the paper says. PremiseCheck flags them cheaply: an LLM rewrites each comment as explicit premises without reading the paper , and a small decision model checks each premise ...

</details>

<details>
<summary><b>38. LEV: Thinking Fast and Deep with Looped Decision Models</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Lichao Sun, Yuxuan Zhang, Zhiling Yan, songdj

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20951) • [📄 arXiv](https://arxiv.org/abs/2610.20951) • [📥 PDF](https://arxiv.org/pdf/2610.20951)

**💻 Code:** [⭐ Code](https://github.com/OpenLAIR/lev) • [⭐ Code](https://github.com/huggingface)

> Can a decision model think longer without writing a longer answer? Lev is a System 1.5 decision model: it reruns a looped backbone and scores the options after every loop, without decoding a chain of thought, so one checkpoint answers at any depth...

</details>

<details>
<summary><b>39. Game2Real-Bench: Do Toy Games Reveal and Transfer to Real-World Visual Reasoning?</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xinzhe Han, Yujie Cheng, Yue Zhu, Juntong Feng, liuqa

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.18834) • [📄 arXiv](https://arxiv.org/abs/2610.18834) • [📥 PDF](https://arxiv.org/pdf/2610.18834)

**💻 Code:** [⭐ Code](https://github.com/QingAnLiu/Game2Real-Bench) • [⭐ Code](https://github.com/huggingface)

> Visual reasoning is an important capability for vision-language models (VLMs) to understand visual evidence, spatial structure, constraints, and state changes. Existing evaluations mainly rely on either real-world data or procedurally generated ta...

</details>

<details>
<summary><b>40. Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21073) • [📄 arXiv](https://arxiv.org/abs/2610.21073) • [📥 PDF](https://arxiv.org/pdf/2610.21073)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> TL;DR: At a fixed token budget, a coding agent fixes more issues when it spends the budget choosing a few whole files and showing them verbatim than when it prunes tokens or retrieves chunks. Our simple selector, CQ2-CARE, needs no compression mod...

</details>

<details>
<summary><b>41. Resisting Harmful Instructions through Training-Free Weight Editing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21189) • [📄 arXiv](https://arxiv.org/abs/2610.21189) • [📥 PDF](https://arxiv.org/pdf/2610.21189v1)

**💻 Code:** [⭐ Code](https://github.com/AI-Interpretability-Illinois/Resisting-Harmful-Instruction) • [⭐ Code](https://github.com/huggingface)

> TL;DR: A training-free weight edit that makes instruction-tuned LLMs resist targeted harmful instructions, such as orders to lie or to produce sexist content. It is built from about 25 prompt pairs using forward passes only, and because it lives i...

</details>

<details>
<summary><b>42. DAGFormer: Global Topology Prediction for Transformer Cross-Layer Connections</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19625) • [📄 arXiv](https://arxiv.org/abs/2610.19625) • [📥 PDF](https://arxiv.org/pdf/2610.19625)

**💻 Code:** [⭐ Code](https://github.com/AI-Interpretability-Illinois/Dagformer) • [⭐ Code](https://github.com/huggingface)

> TL;DR: DAGFormer plans a Transformer's cross-layer connections up front as a global topology for each token. A small topology predictor reads the input tokens and, before the backbone runs, outputs a signed weight on every earlier layer for each h...

</details>

<details>
<summary><b>43. Selection Is Not Learning: Choosing Model Futures</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22029) • [📄 arXiv](https://arxiv.org/abs/2610.22029) • [📥 PDF](https://arxiv.org/pdf/2610.22029)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Self-evolving LLMs choose tasks that look learnable, then keep every update those tasks produce. But a learnable task doesn't guarantee a useful update. We judge the updated model itself instead: HeirCommit keeps an update only if the new model be...

</details>

<details>
<summary><b>44. ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models</b> ⭐ 7</summary>

<br/>

**👥 Authors:** Ngai Wong, Jianjin Li, Lie24, zunhai, Bohansss

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.20503) • [📄 arXiv](https://arxiv.org/abs/2610.20503) • [📥 PDF](https://arxiv.org/pdf/2610.20503)

**💻 Code:** [⭐ Code](https://github.com/StartLuxLabs/ReaDy) • [⭐ Code](https://github.com/huggingface)

> Speculative decoding accelerates autoregressive generation by drafting multiple tokens per step, yet feature-based drafters rely on target hidden features whose contextual emphasis may not align with the needs of subsequent draft positions. Hybrid...

</details>

<details>
<summary><b>45. Persistent Planar Memory for Video World Models</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23795) • [📄 arXiv](https://arxiv.org/abs/2610.23795) • [📥 PDF](https://arxiv.org/pdf/2610.23795)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/robbyant-research/PPMem)

> No abstract available.

</details>

<details>
<summary><b>46. Dusting the Phantom: Gaussian Allocation for Fading Dynamic Content</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Lucas Yunkyu Lee, Byeonghyeon Lee, Jun Young Jeong, Minseo Lee, mhroh01

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21302) • [📄 arXiv](https://arxiv.org/abs/2610.21302) • [📥 PDF](https://arxiv.org/pdf/2610.21302)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Where and when should Gaussians be allocated? Dynamic 3D Gaussian Splatting can struggle to reconstruct small, fast-moving objects, even with longer training or more Gaussians. In Dusting the Phantom , we investigate Gaussian allocation as a key b...

</details>

<details>
<summary><b>47. Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.19636) • [📄 arXiv](https://arxiv.org/abs/2610.19636) • [📥 PDF](https://arxiv.org/pdf/2610.19636)

**💻 Code:** [⭐ Code](https://github.com/AI-Interpretability-Illinois/Symbolic-Merge) • [⭐ Code](https://github.com/huggingface)

> TL;DR: An LLM's sparse autoencoder works as a shared coordinate system for matching symbols across heterogeneous systems (formal provers, code, table schemas, knowledge graphs, ontologies), with no training and no aligned pairs. How SAE-IDF works ...

</details>

<details>
<summary><b>48. DuET: Note-Frame Dual Encoding for Piano Performance-to-Score Transcription</b> ⭐ 13</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21467) • [📄 arXiv](https://arxiv.org/abs/2610.21467) • [📥 PDF](https://arxiv.org/pdf/2610.21467)

**💻 Code:** [⭐ Code](https://github.com/wei-zeng98/DuET) • [⭐ Code](https://github.com/huggingface)

> 🎹 Excited to share DuET, our piano transcription model! DuET converts expressive piano performances into readable sheet music by jointly modeling note-level transcription and beat tracking. Try DuET and explore our resources: 🎹 Online Demo: https:...

</details>

<details>
<summary><b>49. StopWatch: Goal Grounding for Object-goal Navigation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23841) • [📄 arXiv](https://arxiv.org/abs/2610.23841) • [📥 PDF](https://arxiv.org/pdf/2610.23841)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Why do navigation policies walk past a goal that is already in view? We introduce StopWatch, which explicitly grounds the navigation goal by predicting whether it is visible and how far away it is. We find that goal grounding is the dominant failu...

</details>

<details>
<summary><b>50. AI-Driven Disaster Response and Displacement Monitoring</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.21482) • [📄 arXiv](https://arxiv.org/abs/2610.21482) • [📥 PDF](https://arxiv.org/pdf/2610.21482)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> AI-Driven Disaster Response and Displacement Monitoring explores how artificial intelligence can support humanitarian response when conventional information sources are limited or disrupted. The article presents two case studies from the Arab worl...

</details>

<details>
<summary><b>51. MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.23751) • [📄 arXiv](https://arxiv.org/abs/2610.23751) • [📥 PDF](https://arxiv.org/pdf/2610.23751)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Introducing MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing! How can we build multi-turn image editing data without accumulating visual-quality drift? Our key idea is Packed Trajectory Canvas (PTC): jointly generating multip...

</details>

<details>
<summary><b>52. Consistent Distribution Matching for Data-Free Diffusion Distillation</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.09221) • [📄 arXiv](https://arxiv.org/abs/2610.09221) • [📥 PDF](https://arxiv.org/pdf/2610.09221)

**💻 Code:** [⭐ Code](https://github.com/felix-yuxiang/CDMD) • [⭐ Code](https://github.com/huggingface)

> Excited to share our work on Consistent Distribution Matching! 🚀 Inspired by Distribution Matching Distillation (DMD) and Score Identity Distillation (SiD), we ask a simple question: Can we achieve distribution matching without training an auxilia...

</details>

<details>
<summary><b>53. GeoState: Learning View-Decoupled Geometry States for 3D World Modeling</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22343) • [📄 arXiv](https://arxiv.org/abs/2610.22343) • [📥 PDF](https://arxiv.org/pdf/2610.22343)

**💻 Code:** [⭐ Code](https://github.com/Hongchang-Liu/GeoState) • [⭐ Code](https://github.com/huggingface)

> Existing geometry-based world models often rely on view-dependent features, entangling scene dynamics with camera-induced variations. GeoState addresses this by learning a view-decoupled scene state, allowing the world model to focus on scene dyna...

</details>

<details>
<summary><b>54. ARC-SORT: Adaptive, Robust, Compensated Multi-Object Tracking with Interacting Multiple Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Asuran9

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2610.22306) • [📄 arXiv](https://arxiv.org/abs/2610.22306) • [📥 PDF](https://arxiv.org/pdf/2610.22306)

**💻 Code:** [⭐ Code](https://github.com/Athlitix/arcsort) • [⭐ Code](https://github.com/huggingface)

> ARC-SORT is a multi-object tracker built for fast, non-linear motion under a moving camera, such as athletes in sports broadcasts. Nothing is trained: it works with any detector and runs at about 50 FPS on a laptop RTX 3060. The core idea is that ...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 54 |
| 📅 Today | [`2026-10-19.json`](data/daily/2026-10-19.json) | 54 |
| 📆 This Week | [`2026-W42.json`](data/weekly/2026-W42.json) | 54 |
| 🗓️ This Month | [`2026-10.json`](data/monthly/2026-10.json) | 1171 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-10-19 | 54 | [View JSON](data/daily/2026-10-19.json) |
| 📄 2026-10-18 | 84 | [View JSON](data/daily/2026-10-18.json) |
| 📄 2026-10-17 | 84 | [View JSON](data/daily/2026-10-17.json) |
| 📄 2026-10-16 | 69 | [View JSON](data/daily/2026-10-16.json) |
| 📄 2026-10-15 | 63 | [View JSON](data/daily/2026-10-15.json) |
| 📄 2026-10-14 | 69 | [View JSON](data/daily/2026-10-14.json) |
| 📄 2026-10-13 | 15 | [View JSON](data/daily/2026-10-13.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W42 | 54 | [View JSON](data/weekly/2026-W42.json) |
| 📅 2026-W41 | 431 | [View JSON](data/weekly/2026-W41.json) |
| 📅 2026-W40 | 391 | [View JSON](data/weekly/2026-W40.json) |
| 📅 2026-W39 | 474 | [View JSON](data/weekly/2026-W39.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-10 | 1171 | [View JSON](data/monthly/2026-10.json) |
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
