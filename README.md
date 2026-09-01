<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-33-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7013+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">33</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">58</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">33</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7013+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 01, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution</b> ⭐ 37</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31106) • [📄 arXiv](https://arxiv.org/abs/2608.31106) • [📥 PDF](https://arxiv.org/pdf/2608.31106)

**💻 Code:** [⭐ Code](https://github.com/AMAP-ML/DreamX-Creator) • [⭐ Code](https://github.com/huggingface)

> github： https://github.com/AMAP-ML/DreamX-Creator

</details>

<details>
<summary><b>2. Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31046) • [📄 arXiv](https://arxiv.org/abs/2608.31046) • [📥 PDF](https://arxiv.org/pdf/2608.31046)

**💻 Code:** [⭐ Code](https://github.com/DripNowhy/On-Policy-Self-Adaptation) • [⭐ Code](https://github.com/huggingface)

> On-policy distillation can improve reasoning without meaningful teacher guidance: its gains largely come from suppressing unlikely tokens sampled by the student, motivating OPSA—a teacher-free method that uses the model’s own uncertainty for self-...

</details>

<details>
<summary><b>3. GenFirst: Generation Before Reconstruction for Stable End-to-End Latent Generative Modeling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29335) • [📄 arXiv](https://arxiv.org/abs/2608.29335) • [📥 PDF](https://arxiv.org/pdf/2608.29335)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> GenFirst: Generation Before Reconstruction for Stable End-to-End Latent Generative Modeling

</details>

<details>
<summary><b>4. Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30821) • [📄 arXiv](https://arxiv.org/abs/2608.30821) • [📥 PDF](https://arxiv.org/pdf/2608.30821)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> arxiv: https://arxiv.org/abs/2608.30821 project page: https://lucida-r2s.github.io/

</details>

<details>
<summary><b>5. Normalized Low-Rank Adaptation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Weiyang Liu, Yangyi Huang, Zheng Zhan, Ziyin Yue, Jiale Kang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31036) • [📄 arXiv](https://arxiv.org/abs/2510.01938) • [📥 PDF](https://arxiv.org/pdf/2608.31036)

**💻 Code:** [⭐ Code](https://github.com/Joluck/NoRA) • [⭐ Code](https://github.com/huggingface)

> to be better

</details>

<details>
<summary><b>6. PaperGym: Rubric-Centered Evolution for Research-Plan Generation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Wenqi Zhang, Kaitao Song, Yuchen Yan, Yuhan Wang, LZXzju

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31119) • [📄 arXiv](https://arxiv.org/abs/2608.31119) • [📥 PDF](https://arxiv.org/pdf/2608.31119)

**💻 Code:** [⭐ Code](https://github.com/ZJU-REAL/PaperGym) • [⭐ Code](https://github.com/huggingface)

> We propose PaperGym, a low-leakage benchmark that turns arXiv papers into training environments by separating each paper's research question from its answer. Rubrics score proposals on methodological innovation and experimental design, and the sam...

</details>

<details>
<summary><b>7. CogEvol: Towards Efficient and Reliable Learning Environment Generation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30968) • [📄 arXiv](https://arxiv.org/abs/2608.30968) • [📥 PDF](https://arxiv.org/pdf/2608.30968)

**💻 Code:** [⭐ Code](https://github.com/CogEvol/CogEvol-4B) • [⭐ Code](https://github.com/huggingface)

> CogEvol-4B turns a one-line brief into a complete interactive lesson: structured slides plus self-contained HTML simulations, in a single forward pass, running fully offline on a laptop with no APIs, no cloud, and no agent loops😁

</details>

<details>
<summary><b>8. LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation</b> ⭐ 180</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30935) • [📄 arXiv](https://arxiv.org/abs/2608.30935) • [📥 PDF](https://arxiv.org/pdf/2608.30935)

**💻 Code:** [⭐ Code](https://github.com/lightorigins/LightNav-0) • [⭐ Code](https://github.com/huggingface)

> Embodied navigation requires agents to translate heterogeneous goals and visual observations into actions across tasks, environments, and robot embodiments. Modern vision-language models (VLMs) already encode spatial priors for visual grounding, s...

</details>

<details>
<summary><b>9. On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30320) • [📄 arXiv](https://arxiv.org/abs/2608.30320) • [📥 PDF](https://arxiv.org/pdf/2608.30320)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>10. SHAPE of Chain-of-Thought in Math Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28600) • [📄 arXiv](https://arxiv.org/abs/2608.28600) • [📥 PDF](https://arxiv.org/pdf/2608.28600)

**💻 Code:** [⭐ Code](https://github.com/holi-lab/SHAPE-of-CoT) • [⭐ Code](https://github.com/huggingface)

> Impressive work

</details>

<details>
<summary><b>11. Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence</b> ⭐ 6</summary>

<br/>

**👥 Authors:** Yonggang Zhang, Hengyu Liu, Yuhan Liu, Jingwen Fu, visity

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31075) • [📄 arXiv](https://arxiv.org/abs/2608.31075) • [📥 PDF](https://arxiv.org/pdf/2608.31075)

**💻 Code:** [⭐ Code](https://github.com/visitworld123/Awesome-Scaling-LRM-Beyond-Human-Supervision) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. Super Library Agent: Joint Generation and Maintenance of Multiple Applications Beyond the Single Codebase</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29310) • [📄 arXiv](https://arxiv.org/abs/2608.29310) • [📥 PDF](https://arxiv.org/pdf/2608.29310)

**💻 Code:** [⭐ Code](https://github.com/sbigstar0310/super-library-agent) • [⭐ Code](https://github.com/huggingface)

> An agent writes several related apps in sequence. Rather than letting each app reimplement the same components, SLA extracts what they share into a library and migrates the earlier apps onto it as the library grows. On WebGen-Bench, against the sa...

</details>

<details>
<summary><b>13. Evaluating the Hidden Costs of Personalization in Large Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28833) • [📄 arXiv](https://arxiv.org/abs/2608.28833) • [📥 PDF](https://arxiv.org/pdf/2608.28833)

**💻 Code:** [⭐ Code](https://github.com/yumeng-10/personalization_risk) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24293) • [📄 arXiv](https://arxiv.org/abs/2608.24293) • [📥 PDF](https://arxiv.org/pdf/2608.24293)

**💻 Code:** [⭐ Code](https://github.com/kakao/KATok) • [⭐ Code](https://github.com/huggingface)

> Adaptive video tokenization with learned keep-or-drop selection and sparse-token generation. project page: https://github.com/kakao/KATok youtube : https://www.youtube.com/watch?v=QCI3hB_UUOc

</details>

<details>
<summary><b>15. Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents</b> ⭐ 14</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31076) • [📄 arXiv](https://arxiv.org/abs/2608.31076) • [📥 PDF](https://arxiv.org/pdf/2608.31076)

**💻 Code:** [⭐ Code](https://github.com/zjunlp/AutoSciRub) • [⭐ Code](https://github.com/zjunlp/AutoSciRub%7D) • [⭐ Code](https://github.com/huggingface)

> Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify ...

</details>

<details>
<summary><b>16. Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30428) • [📄 arXiv](https://arxiv.org/abs/2608.30428) • [📥 PDF](https://arxiv.org/pdf/2608.30428)

**💻 Code:** [⭐ Code](https://github.com/JunseoKim0103/Lies-We-Can-See) • [⭐ Code](https://github.com/huggingface)

> “Can an agent lie with its body, not just its words?” The blind spot: Deception follows the action space Chatbots could deceive only in conversation: a false claim in the transcript. Digital agents (e.g., code agents) now hold real permissions and...

</details>

<details>
<summary><b>17. CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Vivek Gupta, Naman Ahuja, Rishitosh Singh, Zehua Zhang, Amir Saeidi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30147) • [📄 arXiv](https://arxiv.org/abs/2608.30147) • [📥 PDF](https://arxiv.org/pdf/2608.30147)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large language model (LLM) agents are increasingly deployed in long-horizon, interactive, and stateful environments. In these settings, a single wrong action, such as refunding the wrong purchase, can cause irreversible task failure and must be in...

</details>

<details>
<summary><b>18. Weaving Visual Narratives: Agentic Image Bundle Composition Beyond Atomic Visual Matching</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.28695) • [📄 arXiv](https://arxiv.org/abs/2608.28695) • [📥 PDF](https://arxiv.org/pdf/2608.28695)

**💻 Code:** [⭐ Code](https://github.com/LaVieEnRose365/Image-Bundle-Composition) • [⭐ Code](https://github.com/huggingface)

> Accepted by EMNLP'26 Main Conference

</details>

<details>
<summary><b>19. PaperBanana-Interact: Scientific Diagram Refinement with Multi-Turn Human Feedback</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30241) • [📄 arXiv](https://arxiv.org/abs/2608.30241) • [📥 PDF](https://arxiv.org/pdf/2608.30241)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>20. MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31022) • [📄 arXiv](https://arxiv.org/abs/2608.31022) • [📥 PDF](https://arxiv.org/pdf/2608.31022)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents

</details>

<details>
<summary><b>21. Verification-Aware Training for Speculative Decoding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30135) • [📄 arXiv](https://arxiv.org/abs/2608.30135) • [📥 PDF](https://arxiv.org/pdf/2608.30135)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We propose Verification-Aware Training (VAT), a plug-in framework that improves speculative decoding by training the draft model using simulated verification patterns and adaptive weighting.

</details>

<details>
<summary><b>22. Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yiyang Huang, Jiazhao Zhang, Xiong-Hui Chen, Gengze Zhou, Zixing Lei

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30396) • [📄 arXiv](https://arxiv.org/abs/2608.30396) • [📥 PDF](https://arxiv.org/pdf/2608.30396)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>23. Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29464) • [📄 arXiv](https://arxiv.org/abs/2608.29464) • [📥 PDF](https://arxiv.org/pdf/2608.29464)

**💻 Code:** [⭐ Code](https://github.com/aryopg/face-eval) • [⭐ Code](https://github.com/huggingface)

> Model faithfulness is closely tied to environmental factors, and faithfulness/mechinter/safety research should account for that!

</details>

<details>
<summary><b>24. WebWorld: The Browser as a World Model for Self-Improving Web Code</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30530) • [📄 arXiv](https://arxiv.org/abs/2608.30530) • [📥 PDF](https://arxiv.org/pdf/2608.30530)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🌐 This paper introduces WebWorld, a system that fundamentally resolves the structural flaw of VLM-driven web-code self-improvement—where the same model acts as both proposer and judge—by treating the browser as a deterministic, executable world mo...

</details>

<details>
<summary><b>25. SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29098) • [📄 arXiv](https://arxiv.org/abs/2608.29098) • [📥 PDF](https://arxiv.org/pdf/2608.29098)

**💻 Code:** [⭐ Code](https://github.com/zrwang1211/SafeAtlas-VL) • [⭐ Code](https://github.com/huggingface)

> Multimodal safety moderation requires distinguishing risks arising from visual content, user intent, and assistant behavior. Existing safeguards, however, are typically trained for a single judgment target and reduce safety assessment to a binary ...

</details>

<details>
<summary><b>26. BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.31113) • [📄 arXiv](https://arxiv.org/abs/2608.31113) • [📥 PDF](https://arxiv.org/pdf/2608.31113)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>27. DICS: Exploring Data Intrinsic Consistency for Visual Instruction Selection</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30209) • [📄 arXiv](https://arxiv.org/abs/2608.30209) • [📥 PDF](https://arxiv.org/pdf/2608.30209)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> EMNLP2026

</details>

<details>
<summary><b>28. Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory</b> ⭐ 145</summary>

<br/>

**👥 Authors:** Wei Yu, Kai Zou, Jihai Zhang, Zile Wang, Runjia Qian

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29910) • [📄 arXiv](https://arxiv.org/abs/2608.29910) • [📥 PDF](https://arxiv.org/pdf/2608.29910)

**💻 Code:** [⭐ Code](https://github.com/Riemann-Dynamics/Matrix-Game-3.5) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>29. Chat-Edit-3D++: Interactive 3D and 4D Scene Editing via Large Language Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29137) • [📄 arXiv](https://arxiv.org/abs/2608.29137) • [📥 PDF](https://arxiv.org/pdf/2608.29137)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Recent work on image content manipulation based on vision-language pre-training models has been effectively extended to text-driven 3D scene editing. However, existing schemes for 3D scene editing still have certain shortcomings, hindering their f...

</details>

<details>
<summary><b>30. Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation and Model Contributions</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.30795) • [📄 arXiv](https://arxiv.org/abs/2608.30795) • [📥 PDF](https://arxiv.org/pdf/2608.30795)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We make an end-to-end AI weather model (Aardvark Weather) probabilistic with learned noise in the observation encoder and MC dropout in the processor, so a nested ensemble can split forecast uncertainty into observation-driven (aleatoric) and mode...

</details>

<details>
<summary><b>31. Cross-lingual Functional Vectors for Emotion Detection in Large Language Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shogo Okada, Minh Le Nguyen, Phuong Minh Nguyen, Jieying Xue

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29613) • [📄 arXiv](https://arxiv.org/abs/2608.29613) • [📥 PDF](https://arxiv.org/pdf/2608.29613)

**💻 Code:** [⭐ Code](https://github.com/yingjie7/cross_lingual_fvs) • [⭐ Code](https://github.com/huggingface)

> We examine whether Functional Vectors extracted from a source language can steer task behavior in another language under both standard clean and perturbed zero-shot settings without providing demonstrations during inference.

</details>

<details>
<summary><b>32. EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29387) • [📄 arXiv](https://arxiv.org/abs/2608.29387) • [📥 PDF](https://arxiv.org/pdf/2608.29387)

**💻 Code:** [⭐ Code](https://github.com/MAPS-research/EvoGenUI-Bench) • [⭐ Code](https://github.com/huggingface)

> Can generative UI assistants keep one executable interface correct as user requirements evolve across multiple turns? EvoGenUI-Bench introduces 150 five-turn tasks (750 turns) spanning information presentation, executable interaction, and tool-gro...

</details>

<details>
<summary><b>33. Dynamic Important Example Mining for Reinforcement Finetuning</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.29252) • [📄 arXiv](https://arxiv.org/abs/2608.29252) • [📥 PDF](https://arxiv.org/pdf/2608.29252)

**💻 Code:** [⭐ Code](https://github.com/hrtan/DIEM) • [⭐ Code](https://github.com/huggingface)

> Reinforcement fine-tuning (RFT) is increasingly used to strengthen the reasoning abilities of large models, yet its effectiveness is bound by how training data are selected and used. Most data-centric RFT methods rely on static or heuristic sample...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 33 |
| 📅 Today | [`2026-09-01.json`](data/daily/2026-09-01.json) | 33 |
| 📆 This Week | [`2026-W35.json`](data/weekly/2026-W35.json) | 58 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 33 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-01 | 33 | [View JSON](data/daily/2026-09-01.json) |
| 📄 2026-08-31 | 25 | [View JSON](data/daily/2026-08-31.json) |
| 📄 2026-08-30 | 23 | [View JSON](data/daily/2026-08-30.json) |
| 📄 2026-08-29 | 23 | [View JSON](data/daily/2026-08-29.json) |
| 📄 2026-08-28 | 21 | [View JSON](data/daily/2026-08-28.json) |
| 📄 2026-08-27 | 32 | [View JSON](data/daily/2026-08-27.json) |
| 📄 2026-08-26 | 14 | [View JSON](data/daily/2026-08-26.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W35 | 58 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |
| 📅 2026-W32 | 156 | [View JSON](data/weekly/2026-W32.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 33 | [View JSON](data/monthly/2026-09.json) |
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
