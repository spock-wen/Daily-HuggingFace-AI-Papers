<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-21-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-4930+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">21</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">108</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">108</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">4930+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 03, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Trust Region On-Policy Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01249) • [📄 arXiv](https://arxiv.org/abs/2606.01249) • [📥 PDF](https://arxiv.org/pdf/2606.01249)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> On-Policy Distillation (OPD) is a fundamental technique for efficient post-training of large language models (LLMs), with broad applications in agent learning, multi-task enhancement, and model compression. However, OPD training becomes unstable w...

</details>

<details>
<summary><b>2. Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yunrui Lian, Chenghuai Lin, Dairu Liu, Xuchuan Chen, Zekun Qi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03985) • [📄 arXiv](https://arxiv.org/abs/2606.03985) • [📥 PDF](https://arxiv.org/pdf/2606.03985)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>3. A Local Perturbation Theory for Cross-Domain Interference and Recovery in Multi-Domain RL</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Deyi Xiong, Siyu Ding, yl-9

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02398) • [📄 arXiv](https://arxiv.org/abs/2606.02398) • [📥 PDF](https://arxiv.org/pdf/2606.02398)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Our new work on multi-domain RL: A Local Perturbation Theory for Cross-Domain Interference and Recovery in Multi-Domain RL

</details>

<details>
<summary><b>4. World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03603) • [📄 arXiv](https://arxiv.org/abs/2606.03603) • [📥 PDF](https://arxiv.org/pdf/2606.03603)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/yczhou001/PF-OPSD)

> World Models Meet Language Models: Bridging Concrete and Abstract Reasoning Can we bridge the gap between physical intuition and logical thought? We explore the powerful synergy between World Models (concrete reasoning) and Large Language Models (...

</details>

<details>
<summary><b>5. AutoMedBench: Towards Medical AutoResearch with Agentic AI Models</b> ⭐ 32</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01961) • [📄 arXiv](https://arxiv.org/abs/2606.01961) • [📥 PDF](https://arxiv.org/pdf/2606.01961)

**💻 Code:** [⭐ Code](https://github.com/AutoMedBench/AutoMedBench) • [⭐ Code](https://github.com/huggingface)

> -- Your medical AI agent didn't fail because it lacked medical knowledge. It failed because it didn't verify its own work. A strong agent produces fewer errors and recovers gracefully from the ones it makes. 📖Our Paper -- AutoMedBench, is now onli...

</details>

<details>
<summary><b>6. Decoupled Residual Denoising Diffusion Models for Unified and Data Efficient Image-to-Image Translation</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01048) • [📄 arXiv](https://arxiv.org/abs/2606.01048) • [📥 PDF](https://arxiv.org/pdf/2606.01048)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HKU-HealthAI/DRDD)

> We propose Decoupled Residual Denoising Diffusion models (DRDD) for unified and data-efficient image-to-image (I2I) translation. While diffusion models have advanced I2I translation in terms of quality and diversity, we uncover a previously under-...

</details>

<details>
<summary><b>7. Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03979) • [📄 arXiv](https://arxiv.org/abs/2606.03979) • [📥 PDF](https://arxiv.org/pdf/2606.03979)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> The authors introduce a 'Sleep' paradigm for LLMs, enabling continual learning through memory consolidation via knowledge seeding and a self-improvement 'Dreaming' process driven by reinforcement learning.

</details>

<details>
<summary><b>8. TRON: Targeted Rule-Verifiable Online Environments for Visual Reasoning RL</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01599) • [📄 arXiv](https://arxiv.org/abs/2606.01599) • [📥 PDF](https://arxiv.org/pdf/2606.01599)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/YangTianze009/TRON)

> TRON introduces a generator–verifier framework for visual reasoning RL, where Python-based environments continuously generate new images, questions, and exactly verifiable rewards on demand. The current suite contains 520 environments covering spa...

</details>

<details>
<summary><b>9. Ψ-Bench: Evaluating Persona-Sensitive Influencing in Persuasive Dialogues</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Yutong Liu, Yihang Sun, Jiayu Liu, Hongyi Du, Peixuan Han

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.02754) • [📄 arXiv](https://arxiv.org/abs/2606.02754) • [📥 PDF](https://arxiv.org/pdf/2606.02754)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A benchmark for personalized persuasion

</details>

<details>
<summary><b>10. Decentralized Instruction Tuning: Conflict-Aware Splitting and Weight Merging</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Geewook Kim, Minsik Choi

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01717) • [📄 arXiv](https://arxiv.org/abs/2606.01717) • [📥 PDF](https://arxiv.org/pdf/2606.01717)

**💻 Code:** [⭐ Code](https://github.com/naver-ai/merit) • [⭐ Code](https://github.com/huggingface)

> Large-scale instruction tuning hits two walls: heterogeneous tasks produce conflicting gradients (negative transfer), and joint training needs constant gradient sync across a tightly-coupled cluster. We show both can be handled at once—by training...

</details>

<details>
<summary><b>11. Small RL Controller, Large Language Model: RL-Guided Adaptive Sampling for Test-Time Scaling</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Hongtu Zhu, Chengsong Huang, Rui Liu, Tong Zheng, Runpeng Dai

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03102) • [📄 arXiv](https://arxiv.org/abs/2606.03102) • [📥 PDF](https://arxiv.org/pdf/2606.03102)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Test-time scaling improves the reasoning performance of large language models but incurs substantial cost in both total computation and latency. Existing adaptive sampling methods partially mitigate this issue by dynamically deciding when to stop ...

</details>

<details>
<summary><b>12. PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training</b> ⭐ 79.4k</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03264) • [📄 arXiv](https://arxiv.org/abs/2606.03264) • [📥 PDF](https://arxiv.org/pdf/2606.03264)

**💻 Code:** [⭐ Code](https://github.com/PaddlePaddle/PaddleOCR) • [⭐ Code](https://github.com/huggingface)

> https://arxiv.org/pdf/2606.03264

</details>

<details>
<summary><b>13. PlatonicNav: Unveiling Semantic Correspondence in Navigation with Platonic Topological Maps</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01788) • [📄 arXiv](https://arxiv.org/abs/2606.01788) • [📥 PDF](https://arxiv.org/pdf/2606.01788)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AIGeeksGroup/PlatonicNav)

> Open-sourced.

</details>

<details>
<summary><b>14. Diagnosing Harmful Continuation in Answer-Correct Long-CoT Training Traces</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Fumin Shen, Wenxuan Zhang, Lei Wang, Yuhao Wu, Chen He

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.29288) • [📄 arXiv](https://arxiv.org/abs/2605.29288) • [📥 PDF](https://arxiv.org/pdf/2605.29288)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> This paper studies a hidden data-quality problem in long-CoT SFT: even when a reasoning trace reaches the correct answer, extra reasoning after the conclusion can harm training. The authors define this as post-conclusion continuation, build diagno...

</details>

<details>
<summary><b>15. MERIT: Learning Disentangled Music Representations for Audio Similarity</b> ⭐ 20</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27346) • [📄 arXiv](https://arxiv.org/abs/2605.27346) • [📥 PDF](https://arxiv.org/pdf/2605.27346)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/AMAAI-Lab/MERIT)

> Most similarity models collapse melody, rhythm, and timbre into a single undifferentiated score. MERIT exposes all three as independent, interpretable signals from the same audio query.

</details>

<details>
<summary><b>16. NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03159) • [📄 arXiv](https://arxiv.org/abs/2606.03159) • [📥 PDF](https://arxiv.org/pdf/2606.03159)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> NVIDIA OmniDreams is an action-conditioned foundation generative world model that provides real-time, photorealistic, and reactive simulation environments for training and evaluating autonomous driving policies.

</details>

<details>
<summary><b>17. Benchmarking Visual State Tracking in Multimodal Video Understanding</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03920) • [📄 arXiv](https://arxiv.org/abs/2606.03920) • [📥 PDF](https://arxiv.org/pdf/2606.03920)

**💻 Code:** [⭐ Code](https://github.com/vision-x-nyu/vstat) • [⭐ Code](https://github.com/huggingface)

> VSTAT: https://vision-x-nyu.github.io/vstat-site/

</details>

<details>
<summary><b>18. Value-Aware Stochastic KV Cache Eviction for Reasoning Models</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.03928) • [📄 arXiv](https://arxiv.org/abs/2606.03928) • [📥 PDF](https://arxiv.org/pdf/2606.03928)

**💻 Code:** [⭐ Code](https://github.com/terarachang/VaSE) • [⭐ Code](https://github.com/huggingface)

> Reasoning models improve accuracy through extended chains of thought, but their long outputs create a memory and compute bottleneck. KV cache eviction methods reduce this cost by evicting unimportant key-value pairs from the cache, yet they often ...

</details>

<details>
<summary><b>19. ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.01494) • [📄 arXiv](https://arxiv.org/abs/2606.01494) • [📥 PDF](https://arxiv.org/pdf/2606.01494)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Why Agent Skills Are a Different Security Problem Most security tooling starts with a familiar question: does this artifact contain malware? That question matters for agent skills too, but it underdetermines the risk. An agent skill can be a Markd...

</details>

<details>
<summary><b>20. αDepth: Learning Single-Pass Soft Boundary Decomposition for Stereo Conversion</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.00386) • [📄 arXiv](https://arxiv.org/abs/2606.00386) • [📥 PDF](https://arxiv.org/pdf/2606.00386)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Accurately modeling soft boundaries, e.g., hair and defocus blur, is a fundamental challenge in stereo conversion due to the ambiguous blending of foreground and background. Existing depth models primarily predict single-layer depth, leading to am...

</details>

<details>
<summary><b>21. Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Sachin Kumar

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2605.27958) • [📄 arXiv](https://arxiv.org/abs/2605.27958) • [📥 PDF](https://arxiv.org/pdf/2605.27958)

**💻 Code:** [⭐ Code](https://github.com/techsachinkr/llm-deception-probe-stress-test) • [⭐ Code](https://github.com/huggingface)

> Accepted at the GEM Workshop @ ACL 2026

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 21 |
| 📅 Today | [`2026-06-03.json`](data/daily/2026-06-03.json) | 21 |
| 📆 This Week | [`2026-W22.json`](data/weekly/2026-W22.json) | 108 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 108 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-03 | 21 | [View JSON](data/daily/2026-06-03.json) |
| 📄 2026-06-02 | 44 | [View JSON](data/daily/2026-06-02.json) |
| 📄 2026-06-01 | 43 | [View JSON](data/daily/2026-06-01.json) |
| 📄 2026-05-31 | 59 | [View JSON](data/daily/2026-05-31.json) |
| 📄 2026-05-30 | 59 | [View JSON](data/daily/2026-05-30.json) |
| 📄 2026-05-29 | 43 | [View JSON](data/daily/2026-05-29.json) |
| 📄 2026-05-28 | 39 | [View JSON](data/daily/2026-05-28.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W22 | 108 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |
| 📅 2026-W20 | 243 | [View JSON](data/weekly/2026-W20.json) |
| 📅 2026-W19 | 310 | [View JSON](data/weekly/2026-W19.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 108 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |
| 🗓️ 2026-02 | 1048 | [View JSON](data/monthly/2026-02.json) |
| 🗓️ 2026-01 | 781 | [View JSON](data/monthly/2026-01.json) |

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
