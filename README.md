<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-14-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6856+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">14</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">42</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">585</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6856+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 26, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs</b> ⭐ 18</summary>

<br/>

**👥 Authors:** Dingwen Zhang, Shengsheng Qian, Hao Li, Guohong Mu, Yunheng Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.20492) • [📄 arXiv](https://arxiv.org/abs/2608.20492) • [📥 PDF](https://arxiv.org/pdf/2608.20492)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/HVision-NKU/OraRL)

> We introduce OraRL (Annotations as Rollouts) , an efficient and scalable reinforcement learning framework for unified video MLLMs. OraRL converts each annotation into a reliable oracle rollout while preserving on-policy exploration. A decoupled ad...

</details>

<details>
<summary><b>2. WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report</b> ⭐ 31</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24053) • [📄 arXiv](https://arxiv.org/abs/2608.24053) • [📥 PDF](https://arxiv.org/pdf/2608.24053)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Tencent/WeMM-Embedding)

> WeMM-Embedding is a family of universal multimodal embedding models developed by the WeChat Vision team. It provides unified representations for text, images, videos, visual documents, and interleaved multimodal inputs, achieving state-of-the-art ...

</details>

<details>
<summary><b>3. AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces</b> ⭐ 6</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23041) • [📄 arXiv](https://arxiv.org/abs/2608.23041) • [📥 PDF](https://arxiv.org/pdf/2608.23041)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/microsoft/AutoSaddler)

> https://github.com/microsoft/AutoSaddler

</details>

<details>
<summary><b>4. On-Policy Self-Distillation in Diffusion Models</b> ⭐ 11</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24646) • [📄 arXiv](https://arxiv.org/abs/2608.24646) • [📥 PDF](https://arxiv.org/pdf/2608.24646)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/worldbench/DiffusionOPSD)

> On-Policy Self-Distillation in Diffusion Models I’m excited to introduce our latest work at ByteDance Seed, DiffusionOPSD, a follow-up to DanceOPD. Diffusion and flow models generate images through multi-step denoising trajectories, while mainstre...

</details>

<details>
<summary><b>5. Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses</b> ⭐ 4</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24876) • [📄 arXiv](https://arxiv.org/abs/2608.24876) • [📥 PDF](https://arxiv.org/pdf/2608.24876)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Gen-Verse/Recuris)

> https://github.com/Gen-Verse/Recuris

</details>

<details>
<summary><b>6. On-policy Distillation with Verifiable Reward</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yining Li, Songde Rao, Xitai Jiang, Jiale Zhao, Wenze Lin

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24696) • [📄 arXiv](https://arxiv.org/abs/2608.24696) • [📥 PDF](https://arxiv.org/pdf/2608.24696)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/LeapLabTHU/OPDVR)

> No abstract available.

</details>

<details>
<summary><b>7. Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24680) • [📄 arXiv](https://arxiv.org/abs/2608.24680) • [📥 PDF](https://arxiv.org/pdf/2608.24680)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Dongping-Chen/Game2World)

> We are currently building Gaming World Model and data engine that transfers game dynamics to robotics. Feel free to contact Dongping Chen ( dongpingchen0612@gmail.com ) if you are interested in research collaboration or financial support.

</details>

<details>
<summary><b>8. From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yong Liu, Haojun Chen, Jiangning Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24877) • [📄 arXiv](https://arxiv.org/abs/2608.24877) • [📥 PDF](https://arxiv.org/pdf/2608.24877)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/zhangzjn/awesome-smart-glasses)

> Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-body viewpoint aligns with the wearer's vision, au...

</details>

<details>
<summary><b>9. Best Practice Critic Optimization</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.23566) • [📄 arXiv](https://arxiv.org/abs/2608.23566) • [📥 PDF](https://arxiv.org/pdf/2608.23566)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/QPHutu/golden_critic)

> How to train a critic reliably in LLM RL? No secret sauce. No novelty. Just implementation details that matter.

</details>

<details>
<summary><b>10. LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Thaddäus Wiedemer, Andrej Radonjic, Mehdi Cherti, Marianna Nezhurina, Andreas Hochlehnert

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24845) • [📄 arXiv](https://arxiv.org/abs/2608.24845) • [📥 PDF](https://arxiv.org/pdf/2608.24845)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. Meta^n: Recursive Self-Improvement through Emergent Depth</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Dongyeop Kang, Seungyeon Jwa, Young-Jun Lee, Zae Myung Kim

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24735) • [📄 arXiv](https://arxiv.org/abs/2608.24735) • [📥 PDF](https://arxiv.org/pdf/2608.24735)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. CAFE: Self-Improving Search Agents Need Co-Evolving Feedback</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24794) • [📄 arXiv](https://arxiv.org/abs/2608.24794) • [📥 PDF](https://arxiv.org/pdf/2608.24794)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>13. Length-Adaptive Decoding for Masked Diffusion Machine Translation</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.22274) • [📄 arXiv](https://arxiv.org/abs/2608.22274) • [📥 PDF](https://arxiv.org/pdf/2608.22274)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Entropy-Valley/Entropy-Valley)

> Masked diffusion LMs must pick the target canvas length before denoising starts — there is no autoregressive EOS to stop generation, so a wrong length drops source content or pads the output before a single token is revealed. Entropy-Valley takes ...

</details>

<details>
<summary><b>14. TorchMorph: CUDA-accelerated Morphological Transforms</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.24738) • [📄 arXiv](https://arxiv.org/abs/2608.24738) • [📥 PDF](https://arxiv.org/pdf/2608.24738)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/intcomp/torchmorph)

> This paper presents TorchMorph, a CUDA-accelerated morphological transforms library for PyTorch. It exposes 22 operators (binary and greyscale morphology, exact/chamfer/brute-force distance transforms, entropic optimal transport) as fused CUDA ker...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 14 |
| 📅 Today | [`2026-08-26.json`](data/daily/2026-08-26.json) | 14 |
| 📆 This Week | [`2026-W34.json`](data/weekly/2026-W34.json) | 42 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 585 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-26 | 14 | [View JSON](data/daily/2026-08-26.json) |
| 📄 2026-08-25 | 16 | [View JSON](data/daily/2026-08-25.json) |
| 📄 2026-08-24 | 12 | [View JSON](data/daily/2026-08-24.json) |
| 📄 2026-08-23 | 26 | [View JSON](data/daily/2026-08-23.json) |
| 📄 2026-08-22 | 26 | [View JSON](data/daily/2026-08-22.json) |
| 📄 2026-08-21 | 15 | [View JSON](data/daily/2026-08-21.json) |
| 📄 2026-08-20 | 13 | [View JSON](data/daily/2026-08-20.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W34 | 42 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |
| 📅 2026-W32 | 156 | [View JSON](data/weekly/2026-W32.json) |
| 📅 2026-W31 | 166 | [View JSON](data/weekly/2026-W31.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 585 | [View JSON](data/monthly/2026-08.json) |
| 🗓️ 2026-07 | 583 | [View JSON](data/monthly/2026-07.json) |
| 🗓️ 2026-06 | 866 | [View JSON](data/monthly/2026-06.json) |
| 🗓️ 2026-05 | 1058 | [View JSON](data/monthly/2026-05.json) |
| 🗓️ 2026-04 | 606 | [View JSON](data/monthly/2026-04.json) |
| 🗓️ 2026-03 | 604 | [View JSON](data/monthly/2026-03.json) |

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
