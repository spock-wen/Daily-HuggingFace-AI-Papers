<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-20-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6080+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">20</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">36</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">392</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6080+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** July 21, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17250) • [📄 arXiv](https://arxiv.org/abs/2607.17250) • [📥 PDF](https://arxiv.org/pdf/2607.17250)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKUST-KnowComp/EvolvingWorld)

> EvolvingWorld introduces an open-schema framework for long-horizon literary world simulation, enabling characters and world states to evolve together through ongoing interactions. Its benchmark spans 57 books, with 138K+ supervised training sample...

</details>

<details>
<summary><b>2. SWE-Pruner Pro: The Coder LLM Already Knows What to Prune</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.18213) • [📄 arXiv](https://arxiv.org/abs/2607.18213) • [📥 PDF](https://arxiv.org/pdf/2607.18213)

**💻 Code:** [⭐ Code](https://github.com/Ayanami1314/swe-pruner-pro) • [⭐ Code](https://github.com/huggingface)

> Prunes tool outputs in coding agents using internal representations for efficient context management without external classifiers.

</details>

<details>
<summary><b>3. TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17423) • [📄 arXiv](https://arxiv.org/abs/2607.17423) • [📥 PDF](https://arxiv.org/pdf/2607.17423)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/MCG-NJU/TimeLens2)

> Hi everyone! We are excited to share TimeLens2 , a generalist video temporal grounding MLLM that identifies not only what happens in a video, but also when the supporting evidence occurs. TimeLens2 treats temporal evidence as a variable-cardinalit...

</details>

<details>
<summary><b>4. RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17977) • [📄 arXiv](https://arxiv.org/abs/2607.17977) • [📥 PDF](https://arxiv.org/pdf/2607.17977)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/alibaba-damo-academy/RynnBrain)

> We present RynnBrain 1.1, a family of embodied foundation models spanning 2B, 9B, and 122B-A10B scales. Trained with a unified spatio-temporal and physically grounded framework, RynnBrain 1.1 supports embodied perception, spatial reasoning, locali...

</details>

<details>
<summary><b>5. HOMIE: Human-object Centric Video Personalization via Multimodal Intelligent Enchancement</b> ⭐ 11</summary>

<br/>

**👥 Authors:** Chunyang Jiang, Junwen Pan, Rongchang Xie, Nan Chen, Yiyang Cai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.18217) • [📄 arXiv](https://arxiv.org/abs/2607.18217) • [📥 PDF](https://arxiv.org/pdf/2607.18217)

**💻 Code:** [⭐ Code](https://github.com/YIYANGCAI/HOMIE) • [⭐ Code](https://github.com/huggingface)

> Checkpoint: https://huggingface.co/yychai/homie-r2v-wan2.1

</details>

<details>
<summary><b>6. Apple-π: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence</b> ⭐ 10</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16401) • [📄 arXiv](https://arxiv.org/abs/2607.16401) • [📥 PDF](https://arxiv.org/pdf/2607.16401)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/21yrm/Apple-PI)

> No abstract available.

</details>

<details>
<summary><b>7. ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams</b> ⭐ 68</summary>

<br/>

**👥 Authors:** Yudong Luo, Jie Gu, Zhihong Jin, Yifan Sun, Xiaokang Ma

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.09759) • [📄 arXiv](https://arxiv.org/abs/2607.09759) • [📥 PDF](https://arxiv.org/pdf/2607.09759)

**💻 Code:** [⭐ Code](https://github.com/addxai/ReflectWorld) • [⭐ Code](https://github.com/huggingface)

> ReflectWorld is live world memory for AI agents. It turns camera streams into persistent visual experience: what happened, who or what appeared, what changed, and what an agent should remember next.

</details>

<details>
<summary><b>8. Group Entropy-Controlled Policy Optimization</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16850) • [📄 arXiv](https://arxiv.org/abs/2607.16850) • [📥 PDF](https://arxiv.org/pdf/2607.16850)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A lightweight extension to GRPO that uses group entropy, estimated from existing grouped samples to perform entropy-conditioned asymmetric advantage shaping.

</details>

<details>
<summary><b>9. Environment-free Synthetic Data Generation for API-Calling Agents</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16900) • [📄 arXiv](https://arxiv.org/abs/2607.16900) • [📥 PDF](https://arxiv.org/pdf/2607.16900)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> synthetic data generation with LLM-based API simulation

</details>

<details>
<summary><b>10. LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.18110) • [📄 arXiv](https://arxiv.org/abs/2607.18110) • [📥 PDF](https://arxiv.org/pdf/2607.18110)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present LLM-as-a-Coach which repurposes LLM-as-a-Judge in RL as a experiential knowledge extractor for non-verifiable tasks. LLM-as-a-Coach extracts transferable knowledge given policy response and rubrics, and internalize it with on-policy con...

</details>

<details>
<summary><b>11. DiffGI: Differentiable Geometry Images for High-Fidelity Thin-Shell 3D Generation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.13365) • [📄 arXiv](https://arxiv.org/abs/2607.13365) • [📥 PDF](https://arxiv.org/pdf/2607.13365)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> High-fidelity thin-shell 3D generation in about a second on a consumer GPU — it even runs on a laptop CPU, no server needed. 🌐 Project page: https://ejshim.github.io/diffgi/ DiffGI replaces binary occupancy maps in geometry images with a continuou...

</details>

<details>
<summary><b>12. FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped Flow Field for Online Video Editing Data Generation and Modality Mimicry</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.18227) • [📄 arXiv](https://arxiv.org/abs/2607.18227) • [📥 PDF](https://arxiv.org/pdf/2607.18227)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> 🦋 FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped Flow Field for Online Video Editing Data Generation and Modality Mimicry ✨ Informations ☘️ 2026/07/21 : main.pdf in this dataset repository is the uncompressed file of the...

</details>

<details>
<summary><b>13. Distilled Reinforcement Learning for LLM Post-training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17247) • [📄 arXiv](https://arxiv.org/abs/2607.17247) • [📥 PDF](https://arxiv.org/pdf/2607.17247)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/597358816/Distilled-RL)

> Distilled Reinforcement Learning for LLM Post-Training Standard reinforcement learning relies on coarse-grained outcome rewards, while on-policy distillation usually encourages the student to imitate the teacher distribution unconditionally. Disti...

</details>

<details>
<summary><b>14. HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17097) • [📄 arXiv](https://arxiv.org/abs/2607.17097) • [📥 PDF](https://arxiv.org/pdf/2607.17097)

**💻 Code:** [⭐ Code](https://github.com/Droliven/HarmoHOI_project) • [⭐ Code](https://github.com/huggingface)

> Hand-Object Interaction (HOI) synthesis is a cornerstone for animation production and embodied AI. Despite the strong priors of video foundation models, multi-view consistent HOI synthesis remains challenging due to complex hand motions and occlus...

</details>

<details>
<summary><b>15. JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yongjian Guo, Hedan Yang, Junyang Hua, Wentao Zhang, Haoran231

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.16074) • [📄 arXiv](https://arxiv.org/abs/2607.16074) • [📥 PDF](https://arxiv.org/pdf/2607.16074)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We present JoyNexus, a service-oriented multi-tenant post-training framework for Vision-Language-Action (VLA) models. As illustrated in the following figure, JoyNexus decouples Training Model, Inference Model, and Environment Services, enabling co...

</details>

<details>
<summary><b>16. Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17986) • [📄 arXiv](https://arxiv.org/abs/2607.17986) • [📥 PDF](https://arxiv.org/pdf/2607.17986)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Self-state attacks target the agent’s own persistent files; legitimate and malicious operations converge to identical VFS operations on the same node.

</details>

<details>
<summary><b>17. OpenLongTail: Generative Scaling of Long-Tail Driving Data</b> ⭐ 24</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.09655) • [📄 arXiv](https://arxiv.org/abs/2607.09655) • [📥 PDF](https://arxiv.org/pdf/2607.09655)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/phai-lab/OpenLongTail)

> We introduce OpenLongTail, an open-source generative data engine that transforms monocular long-tail driving videos into temporally coherent and pose-aligned multi-view training assets. Our approach combines pose-informed extrapolative view synthe...

</details>

<details>
<summary><b>18. Token-Level Off-Policy Learning for Faithful Generation Under Distribution Shift</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17524) • [📄 arXiv](https://arxiv.org/abs/2607.17524) • [📥 PDF](https://arxiv.org/pdf/2607.17524)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We propose token-level off-policy labeling -- a method that reframes off-policy post-training as token correctness classification.

</details>

<details>
<summary><b>19. FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Atri Rudra, Zhenyu Gu, Yanyuan Qin, Zhuoming Chen, Krish Agarwal

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.18171) • [📄 arXiv](https://arxiv.org/abs/2607.18171) • [📥 PDF](https://arxiv.org/pdf/2607.18171)

**💻 Code:** [⭐ Code](https://github.com/Infini-AI-Lab/FlashRT) • [⭐ Code](https://github.com/huggingface)

> Github: https://github.com/Infini-AI-Lab/FlashRT

</details>

<details>
<summary><b>20. DiFA: Inference-Time Forward-Process Alignment for Diffusion Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2607.17972) • [📄 arXiv](https://arxiv.org/abs/2607.17972) • [📥 PDF](https://arxiv.org/pdf/2607.17972)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> By leveraging a causal history buffer to build consensus anchors, DiFA aligns the reverse inference trajectory directly with the forward diffusion process. This significantly reduces error accumulation during few-step sampling without any retraini...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 20 |
| 📅 Today | [`2026-07-21.json`](data/daily/2026-07-21.json) | 20 |
| 📆 This Week | [`2026-W29.json`](data/weekly/2026-W29.json) | 36 |
| 🗓️ This Month | [`2026-07.json`](data/monthly/2026-07.json) | 392 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-07-21 | 20 | [View JSON](data/daily/2026-07-21.json) |
| 📄 2026-07-20 | 16 | [View JSON](data/daily/2026-07-20.json) |
| 📄 2026-07-19 | 29 | [View JSON](data/daily/2026-07-19.json) |
| 📄 2026-07-18 | 29 | [View JSON](data/daily/2026-07-18.json) |
| 📄 2026-07-17 | 20 | [View JSON](data/daily/2026-07-17.json) |
| 📄 2026-07-16 | 0 | [View JSON](data/daily/2026-07-16.json) |
| 📄 2026-07-15 | 2 | [View JSON](data/daily/2026-07-15.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W29 | 36 | [View JSON](data/weekly/2026-W29.json) |
| 📅 2026-W28 | 105 | [View JSON](data/weekly/2026-W28.json) |
| 📅 2026-W27 | 133 | [View JSON](data/weekly/2026-W27.json) |
| 📅 2026-W26 | 165 | [View JSON](data/weekly/2026-W26.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-07 | 392 | [View JSON](data/monthly/2026-07.json) |
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
