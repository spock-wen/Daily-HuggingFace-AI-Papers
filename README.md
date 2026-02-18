<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-35-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-2322+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">35</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">108</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">803</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">2322+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** February 18, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. DeepImageSearch: Benchmarking Multimodal Agents for Context-Aware Image Retrieval in Visual Histories</b> ⭐ 27</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.10809) • [📄 arXiv](https://arxiv.org/abs/2602.10809) • [📥 PDF](https://arxiv.org/pdf/2602.10809)

**💻 Code:** [⭐ Code](https://github.com/RUC-NLPIR/DeepImageSearch)

> Paper link: https://arxiv.org/abs/2602.10809 Github Repo: https://github.com/RUC-NLPIR/DeepImageSearch Leaderboard: https://huggingface.co/spaces/RUC-NLPIR/DISBench-Leaderboard

</details>

<details>
<summary><b>2. Experiential Reinforcement Learning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13949) • [📄 arXiv](https://arxiv.org/abs/2602.13949) • [📥 PDF](https://arxiv.org/pdf/2602.13949)

> Experiential Reinforcement Learning is a new training paradigm that shifts language model learning from simple imitation or trial and error toward structured learning from experience. Instead of just copying examples like supervised finetuning or ...

</details>

<details>
<summary><b>3. BitDance: Scaling Autoregressive Generative Models with Binary Tokens</b> ⭐ 153</summary>

<br/>

**👥 Authors:** Xuefeng Hu, Weijia Mao, Shaobin Zhuang, Jiaming Han, Yuang Ai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14041) • [📄 arXiv](https://arxiv.org/abs/2602.14041) • [📥 PDF](https://arxiv.org/pdf/2602.14041)

**💻 Code:** [⭐ Code](https://github.com/shallowdream204/BitDance)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Autoregressive Image Generation with Masked Bit Modeling (2026) NextFlow: U...

</details>

<details>
<summary><b>4. REDSearcher: A Scalable and Cost-Efficient Framework for Long-Horizon Search Agents</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14234) • [📄 arXiv](https://arxiv.org/abs/2602.14234) • [📥 PDF](https://arxiv.org/pdf/2602.14234)

**💻 Code:** [⭐ Code](https://github.com/RedSearchAgent/REDSearcher)

> Large language models are transitioning from general purpose knowledge engines to real world problem solvers, yet optimizing them for deep search tasks remains challenging. The central bottleneck lies in the extreme sparsity of high quality search...

</details>

<details>
<summary><b>5. Query as Anchor: Scenario-Adaptive User Representation via Large Language Model</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14492) • [📄 arXiv](https://arxiv.org/abs/2602.14492) • [📥 PDF](https://arxiv.org/pdf/2602.14492)

**💻 Code:** [⭐ Code](https://github.com/JhCircle/Q-Anchor)

> Query as Anchor: Scenario-Adaptive User Representation via Large Language Model Q-Anchor is a query-conditioned user representation framework that transforms static user embeddings into dynamic, scenario-adaptive representations using Large Langua...

</details>

<details>
<summary><b>6. STATe-of-Thoughts: Structured Action Templates for Tree-of-Thoughts</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Brandon M. Stewart, Ofra Amir, Gilad Morad, Zachary Bamberger, TillRS

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14265) • [📄 arXiv](https://arxiv.org/abs/2602.14265) • [📥 PDF](https://arxiv.org/pdf/2602.14265)

**💻 Code:** [⭐ Code](https://github.com/zbambergerNLP/state-of-thoughts)

> STATe introduces an interpretable Inference-Time-Compute (ITC) framework that replaces stochastic sampling with structured textual interventions to guide high-level reasoning choices. This approach significantly improves output diversity and quali...

</details>

<details>
<summary><b>7. InnoEval: On Research Idea Evaluation as a Knowledge-Grounded, Multi-Perspective Reasoning Problem</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14367) • [📄 arXiv](https://arxiv.org/abs/2602.14367) • [📥 PDF](https://arxiv.org/pdf/2602.14367)

**💻 Code:** [⭐ Code](https://github.com/zjunlp/InnoEval)

> As LLMs generate research ideas at an unprecedented scale, we face a critical bottleneck: who evaluates these ideas? We frame idea evaluation as a knowledge-grounded, multi-perspective reasoning problem. InnoEval doesn't just predict accept/reject...

</details>

<details>
<summary><b>8. Data Darwinism Part I: Unlocking the Value of Scientific Data for Pre-training</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.07824) • [📄 arXiv](https://arxiv.org/abs/2602.07824) • [📥 PDF](https://arxiv.org/pdf/2602.07824)

**💻 Code:** [⭐ Code](https://github.com/GAIR-NLP/Data-Darwinism)

> Data Darwinism The quality of training data fundamentally determines foundation model performance, yet the field lacks systematic frameworks for data processing. We introduce Data Darwinism , a ten-level hierarchical taxonomy (L0--L9) organizing d...

</details>

<details>
<summary><b>9. Qute: Towards Quantum-Native Database</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Surui Tang, Bangrui Xu, Wei Zhou, Xuanhe Zhou, Muzhi Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14699) • [📄 arXiv](https://arxiv.org/abs/2602.14699) • [📥 PDF](https://arxiv.org/pdf/2602.14699)

**💻 Code:** [⭐ Code](https://github.com/weAIDB/Qute)

> Please refer to our open-source prototype at: https://github.com/weAIDB/Qute .

</details>

<details>
<summary><b>10. Nanbeige4.1-3B: A Small General Model that Reasons, Aligns, and Acts</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13367) • [📄 arXiv](https://arxiv.org/abs/2602.13367) • [📥 PDF](https://arxiv.org/pdf/2602.13367)

> Via Victor Mustar's recommendation here. ** I am not affiliated with this paper! ** I am only submitting it to the Daily so that others can enjoy it! https://x.com/victormustar/status/2023423300278583727

</details>

<details>
<summary><b>11. UniWeTok: An Unified Binary Tokenizer with Codebook Size 2^{128} for Unified Multimodal Large Language Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14178) • [📄 arXiv](https://arxiv.org/abs/2602.14178) • [📥 PDF](https://arxiv.org/pdf/2602.14178)

**💻 Code:** [⭐ Code](https://github.com/shallowdream204/BitDance)

> Github: https://github.com/shallowdream204/BitDance

</details>

<details>
<summary><b>12. Learning to Configure Agentic AI Systems</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11574) • [📄 arXiv](https://arxiv.org/abs/2602.11574) • [📥 PDF](https://arxiv.org/pdf/2602.11574)

**💻 Code:** [⭐ Code](https://github.com/somsagar07/Context_Optimization)

> Building agentic systems is hard, but configuring them is even harder. We all know the struggle: Which LLM should handle the planning? Which tool does it need? How much context is too much? What is the most effective workflow? In our new paper, Le...

</details>

<details>
<summary><b>13. Embed-RL: Reinforcement Learning for Reasoning-Driven Multimodal Embeddings</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13823) • [📄 arXiv](https://arxiv.org/abs/2602.13823) • [📥 PDF](https://arxiv.org/pdf/2602.13823)

**💻 Code:** [⭐ Code](https://github.com/ZoengHN/Embed-RL)

> Project Page: https://github.com/ZoengHN/Embed-RL

</details>

<details>
<summary><b>14. BrowseComp-V^3: A Visual, Vertical, and Verifiable Benchmark for Multimodal Browsing Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yanzhe Dan, Bowen Zhou, Bo Li, Jiepeng Zhou, Huanyao Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12876) • [📄 arXiv](https://arxiv.org/abs/2602.12876) • [📥 PDF](https://arxiv.org/pdf/2602.12876)

> Introduces BrowseComp-V3, a 300-question multimodal web-browsing benchmark and OmniSeeker framework to evaluate deep, cross-modal reasoning and evidence-driven search in LLM-based agents.

</details>

<details>
<summary><b>15. WebWorld: A Large-Scale World Model for Web Agent Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14721) • [📄 arXiv](https://arxiv.org/abs/2602.14721) • [📥 PDF](https://arxiv.org/pdf/2602.14721)

> WebWorld presents a scalable large-scale web-world model trained on 1M+ open-web trajectories, enabling long-horizon simulation, cross-domain generalization, and effective inference-time search for web agents.

</details>

<details>
<summary><b>16. Conversational Image Segmentation: Grounding Abstract Concepts with Scalable Supervision</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13195) • [📄 arXiv](https://arxiv.org/abs/2602.13195) • [📥 PDF](https://arxiv.org/pdf/2602.13195)

**💻 Code:** [⭐ Code](https://github.com/AadSah/ConverSeg)

> Conversational image segmentation grounds abstract, intent-driven concepts into pixel-accurate masks. Prior work on referring image grounding focuses on categorical and spatial queries (e.g., “left-most apple”) and overlooks functional and physica...

</details>

<details>
<summary><b>17. LaViDa-R1: Advancing Reasoning for Unified Multimodal Diffusion Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14147) • [📄 arXiv](https://arxiv.org/abs/2602.14147) • [📥 PDF](https://arxiv.org/pdf/2602.14147)

> Unified RL-SFT for multi-modal diffusion language models.

</details>

<details>
<summary><b>18. FireRed-Image-Edit-1.0 Techinical Report</b> ⭐ 390</summary>

<br/>

**👥 Authors:** Cunzheng Wang, Chen Li, Chao Hui, Changhao Qiao, Super Intelligence Team

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13344) • [📄 arXiv](https://arxiv.org/abs/2602.13344) • [📥 PDF](https://arxiv.org/pdf/2602.13344)

**💻 Code:** [⭐ Code](https://github.com/FireRedTeam/FireRed-Image-Edit)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API PosterOmni: Generalized Artistic Poster Creation via Task Distillation and ...

</details>

<details>
<summary><b>19. MoRL: Reinforced Reasoning for Unified Motion Understanding and Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14534) • [📄 arXiv](https://arxiv.org/abs/2602.14534) • [📥 PDF](https://arxiv.org/pdf/2602.14534)

**💻 Code:** [⭐ Code](https://github.com/AIGeeksGroup/MoRL)

> https://aigeeksgroup.github.io/MoRL/

</details>

<details>
<summary><b>20. LM-Lexicon: Improving Definition Modeling via Harmonizing Semantic Experts</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14060) • [📄 arXiv](https://arxiv.org/abs/2602.14060) • [📥 PDF](https://arxiv.org/pdf/2602.14060)

**💻 Code:** [⭐ Code](https://github.com/jacklanda/LMLexicon)

> We introduce LM-Lexicon, an innovative definition modeling approach that incorporates data clustering, semantic expert learning, and model merging using a sparse mixture-of-experts architecture. By decomposing the definition modeling task into spe...

</details>

<details>
<summary><b>21. AIDev: Studying AI Coding Agents on GitHub</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Ahmed E. Hassan, Haoxiang Zhang, hao-li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.09185) • [📄 arXiv](https://arxiv.org/abs/2507.15003) • [📥 PDF](https://arxiv.org/pdf/2602.09185)

> AIDev is a dataset ( https://huggingface.co/datasets/hao-li/AIDev ) capturing agent-authored pull requests (Agentic-PRs) from real-world GitHub repositories: Scale: 932,791 Agentic-PRs Breadth: 116,211 repositories and 72,189 developers, across fi...

</details>

<details>
<summary><b>22. EditCtrl: Disentangled Local and Global Control for Real-Time Generative Video Editing</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.15031) • [📄 arXiv](https://arxiv.org/abs/2602.15031) • [📥 PDF](https://arxiv.org/pdf/2602.15031)

**💻 Code:** [⭐ Code](https://github.com/yehonathanlitman/EditCtrl)

> Abstract: High-fidelity generative video editing has seen significant quality improvements by leveraging pre-trained video foundation models. However, their computational cost is a major bottleneck, as they are often designed to inefficiently proc...

</details>

<details>
<summary><b>23. AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories</b> ⭐ 12</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14941) • [📄 arXiv](https://arxiv.org/abs/2602.14941) • [📥 PDF](https://arxiv.org/pdf/2602.14941)

**💻 Code:** [⭐ Code](https://github.com/wz0919/AnchorWeave)

> No abstract available.

</details>

<details>
<summary><b>24. Exposing the Systematic Vulnerability of Open-Weight Models to Prefill Attacks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14689) • [📄 arXiv](https://arxiv.org/abs/2602.14689) • [📥 PDF](https://arxiv.org/pdf/2602.14689)

> We conducted the largest empirical study of prefill attacks to date, testing 50 state-of-the-art open-weight models against 23 distinct attack strategies. Results show universal vulnerability with attack success rates approaching 100%.

</details>

<details>
<summary><b>25. Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shay B. Cohen, Wenda Li, Mihaela Cătălina Stoian, Yu Zhao, Joshua Ong Jun Leang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12586) • [📄 arXiv](https://arxiv.org/abs/2602.12586) • [📥 PDF](https://arxiv.org/pdf/2602.12586)

> We introduce McDiffuSE, a framework that formulates slot selection as decision making and optimises infilling orders through Monte Carlo Tree Search (MCTS). McDiffuSE uses look-ahead simulations to evaluate partial completions before commitment, s...

</details>

<details>
<summary><b>26. CellMaster: Collaborative Cell Type Annotation in Single-Cell Analysis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13346) • [📄 arXiv](https://arxiv.org/abs/2602.13346) • [📥 PDF](https://arxiv.org/pdf/2602.13346)

> CellMaster: Collaborative Cell Type Annotation in Single-Cell Analysis

</details>

<details>
<summary><b>27. DHPLT: large-scale multilingual diachronic corpora and word representations for semantic change modelling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.11968) • [📄 arXiv](https://arxiv.org/abs/2602.11968) • [📥 PDF](https://arxiv.org/pdf/2602.11968)

**💻 Code:** [⭐ Code](https://github.com/ltgoslo/scdisc_hplt)

> DHPLT is an open collection of diachronic corpora for semantic change modeling in 41 languages. The collection covers three time periods: 2011-2015, 2020-2021 and 2024-present (1 million documents per time period for each language). We additionall...

</details>

<details>
<summary><b>28. Acoustivision Pro: An Open-Source Interactive Platform for Room Impulse Response Analysis and Acoustic Characterization</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Mandip Goswami

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.12299) • [📄 arXiv](https://arxiv.org/abs/2602.12299) • [📥 PDF](https://arxiv.org/pdf/2602.12299)

> Room acoustics analysis plays a central role in architectural design, audio engineering, speech intelligibility assessment, and hearing research. Despite the availability of standardized metrics such as reverberation time, clarity, and speech tran...

</details>

<details>
<summary><b>29. Benchmarking Knowledge-Extraction Attack and Defense on Retrieval-Augmented Generation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Haoyu Han, Li Ma, Utkarsh Sahu, Zhisheng Qi, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.09319) • [📄 arXiv](https://arxiv.org/abs/2602.09319) • [📥 PDF](https://arxiv.org/pdf/2602.09319)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Subgraph Reconstruction Attacks on Graph RAG Deployments with Practical Def...

</details>

<details>
<summary><b>30. Blind to the Human Touch: Overlap Bias in LLM-Based Summary Evaluation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Nesreen K. Ahmed, Hanieh Deilamsalehy, Cheng-Tse Liu, Jiangnan Fang, Franck-Dernoncourt

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.07673) • [📄 arXiv](https://arxiv.org/abs/2602.07673) • [📥 PDF](https://arxiv.org/pdf/2602.07673)

> This is an automated message from the Librarian Bot . I found the following papers similar to this paper. The following papers were recommended by the Semantic Scholar API Exploring the features used for summary evaluation by Human and GPT (2025) ...

</details>

<details>
<summary><b>31. A Critical Look at Targeted Instruction Selection: Disentangling What Matters (and What Doesn't)</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14696) • [📄 arXiv](https://arxiv.org/abs/2602.14696) • [📥 PDF](https://arxiv.org/pdf/2602.14696)

**💻 Code:** [⭐ Code](https://github.com/dcml-lab/targeted-instruction-selection)

> Code: https://github.com/dcml-lab/targeted-instruction-selection Datasets: https://huggingface.co/collections/Harvard-DCML/targeted-instruction-selection

</details>

<details>
<summary><b>32. Preliminary sonification of ENSO using traditional Javanese gamelan scales</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.14560) • [📄 arXiv](https://arxiv.org/abs/2602.14560) • [📥 PDF](https://arxiv.org/pdf/2602.14560)

**💻 Code:** [⭐ Code](https://github.com/sandyherho/suppl-enso-javanese-sonification)

> This study presents a novel approach to climate data sonification by mapping the El Niño-Southern Oscillation (ENSO) Niño 3.4 index (1870–2024) onto traditional Javanese Gamelan scales, treating the auditory display itself as a complex dynamical s...

</details>

<details>
<summary><b>33. SPILLage: Agentic Oversharing on the Web</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13516) • [📄 arXiv](https://www.arxiv.org/abs/2602.13516) • [📥 PDF](https://arxiv.org/pdf/2602.13516)

**💻 Code:** [⭐ Code](https://github.com/jrohsc/SPILLage)

> Paper link: https://www.arxiv.org/abs/2602.13516 Github Repo: https://github.com/jrohsc/SPILLage

</details>

<details>
<summary><b>34. Found-RL: foundation model-enhanced reinforcement learning for autonomous driving</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.10458) • [📄 arXiv](https://arxiv.org/abs/2602.10458) • [📥 PDF](https://arxiv.org/pdf/2602.10458)

**💻 Code:** [⭐ Code](https://github.com/ys-qu/found-rl)

> We present Found-RL, a unified framework that integrates foundation models into reinforcement learning for autonomous driving. The method combines asynchronous batch inference of VLMs with action guidance and semantic reward shaping, enabling safe...

</details>

<details>
<summary><b>35. VisPhyWorld: Probing Physical Reasoning via Code-Driven Video Reconstruction</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2602.13294) • [📄 arXiv](https://arxiv.org/abs/2602.13294) • [📥 PDF](https://arxiv.org/pdf/2602.13294)

**💻 Code:** [⭐ Code](https://github.com/TIGER-AI-Lab/VisPhyWorld)

> Evaluating whether Multimodal Large Language Models (MLLMs) genuinely reason about physical dynamics remains challenging. Most existing benchmarks rely on recognition-style protocols such as Visual Question Answering (VQA) and Violation of Expecta...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 35 |
| 📅 Today | [`2026-02-18.json`](data/daily/2026-02-18.json) | 35 |
| 📆 This Week | [`2026-W07.json`](data/weekly/2026-W07.json) | 108 |
| 🗓️ This Month | [`2026-02.json`](data/monthly/2026-02.json) | 803 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-02-18 | 35 | [View JSON](data/daily/2026-02-18.json) |
| 📄 2026-02-17 | 32 | [View JSON](data/daily/2026-02-17.json) |
| 📄 2026-02-16 | 41 | [View JSON](data/daily/2026-02-16.json) |
| 📄 2026-02-15 | 41 | [View JSON](data/daily/2026-02-15.json) |
| 📄 2026-02-14 | 41 | [View JSON](data/daily/2026-02-14.json) |
| 📄 2026-02-13 | 47 | [View JSON](data/daily/2026-02-13.json) |
| 📄 2026-02-12 | 57 | [View JSON](data/daily/2026-02-12.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W07 | 108 | [View JSON](data/weekly/2026-W07.json) |
| 📅 2026-W06 | 293 | [View JSON](data/weekly/2026-W06.json) |
| 📅 2026-W05 | 357 | [View JSON](data/weekly/2026-W05.json) |
| 📅 2026-W04 | 214 | [View JSON](data/weekly/2026-W04.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-02 | 803 | [View JSON](data/monthly/2026-02.json) |
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
