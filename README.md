<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-17-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-7246+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">17</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">99</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">266</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">7246+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** September 11, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shuang Cheng, Chiyu Chen, NCP Team, Rubin-Wei, Clover-Hill

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10715) • [📄 arXiv](https://arxiv.org/abs/2609.10715) • [📥 PDF](https://arxiv.org/pdf/2609.10715)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> A large-scale new architecture with latent space prediction.

</details>

<details>
<summary><b>2. SenseNova-U1.5: Towards Native Unified Visual Intelligence</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiahao Wang, Zillionkkk, caizhongang, WRHC, Paranioar

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11929) • [📄 arXiv](https://arxiv.org/abs/2609.11929) • [📥 PDF](https://arxiv.org/pdf/2609.11929)

**💻 Code:** [⭐ Code](https://github.com/OpenSenseNova/SenseNova-U1) • [⭐ Code](https://github.com/huggingface)

> Github: https://github.com/OpenSenseNova/SenseNova-U1

</details>

<details>
<summary><b>3. SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.07064) • [📄 arXiv](https://arxiv.org/abs/2609.07064) • [📥 PDF](https://arxiv.org/pdf/2609.07064)

**💻 Code:** [⭐ Code](https://github.com/rsoohyun/SpatialBlock) • [⭐ Code](https://github.com/huggingface)

> Large vision-language models describe what a scene contains well, yet still struggle to reconstruct the 3D structure behind a 2D image and reason about it — spatial intelligence. SpatialBlock takes the route human spatial cognition develops along ...

</details>

<details>
<summary><b>4. EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.05903) • [📄 arXiv](https://arxiv.org/abs/2609.05903) • [📥 PDF](https://arxiv.org/pdf/2609.05903)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SaFo-Lab/EvoSafeHarness)

> LLM agents now move money, edit files and act on real systems. Yet most safety harnesses are designed once by experts and reused for every model and every domain. One size does not fit all. 🚀 We are excited to introduce EvoSafeHarness, a framework...

</details>

<details>
<summary><b>5. Mi-Ripple: Restoring Images Degraded by Iterative AI Editing</b> ⭐ 32</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11317) • [📄 arXiv](https://arxiv.org/abs/2609.11317) • [📥 PDF](https://arxiv.org/pdf/2609.11317)

**💻 Code:** [⭐ Code](https://github.com/miyang-ai/Mi-Ripple) • [⭐ Code](https://github.com/huggingface)

> We investigate “digital ripples” in AI-generated images, showing how resampling introduces periodic artifacts and why they can reappear after cleanup during subsequent editing.

</details>

<details>
<summary><b>6. X-AuT: Progressive Audio-Encoder Compression for Speech LLMs with Cross-Scale Distillation</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11412) • [📄 arXiv](https://arxiv.org/abs/2609.11412) • [📥 PDF](https://arxiv.org/pdf/2609.11412)

**💻 Code:** [⭐ Code](https://github.com/XPENG-AI/X-AuT) • [⭐ Code](https://github.com/huggingface)

> Project website: xpeng-ai.github.io/x-aut Paper: arXiv:2609.11412 Source code: XPENG-AI/X-AuT Model weights: XPENG-AI/X-AuT

</details>

<details>
<summary><b>7. TempCloze: Can Video-LLMs Identify the Missing Middle?</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.01515) • [📄 arXiv](https://arxiv.org/abs/2609.01515) • [📥 PDF](https://arxiv.org/pdf/2609.01515)

**💻 Code:** [⭐ Code](https://github.com/CedricPei/Temporal-Cloze) • [⭐ Code](https://github.com/huggingface)

> Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchm...

</details>

<details>
<summary><b>8. Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Bo Zhu, Yuxuan Liao, Zhiqi Li

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11499) • [📄 arXiv](https://arxiv.org/abs/2609.11499) • [📥 PDF](https://arxiv.org/pdf/2609.11499)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>9. CARDEA: Auditable Reasoning Grounded in Spatial Evidence for End-to-End Coronary Angiography Interpretation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Shih-Sheng Chang, Wei-Chun Wang, Kee Koon Ng, Shih-Yen Hou, benbayibaurba

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.06931) • [📄 arXiv](https://arxiv.org/abs/2609.06931) • [📥 PDF](https://arxiv.org/pdf/2609.06931)

**💻 Code:** [⭐ Code](https://github.com/benbayibaurba/cardea) • [⭐ Code](https://github.com/huggingface)

> English Existing AI systems can assist with coronary angiography interpretation, but most models still provide only the final prediction. The intermediate reasoning process remains largely a black box, making the output difficult to verify directl...

</details>

<details>
<summary><b>10. World in World: Explore the World with World Models</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Chi Zhang, Yanming Yang, Chenxi Song

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11548) • [📄 arXiv](https://arxiv.org/abs/2609.11548) • [📥 PDF](https://arxiv.org/pdf/2609.11548)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>11. FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation</b> ⭐ 2</summary>

<br/>

**👥 Authors:** Dmitriy Vatolin, Khaled Abud, Vladislav Bargatin, a-yakovenko

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11486) • [📄 arXiv](https://arxiv.org/abs/2609.11486) • [📥 PDF](https://arxiv.org/pdf/2609.11486)

**💻 Code:** [⭐ Code](https://github.com/msu-video-group/freeflow) • [⭐ Code](https://github.com/huggingface)

> State-of-the-art optical flow method without any task-specific biases.

</details>

<details>
<summary><b>12. DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning for Cooperative Air Combat</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11155) • [📄 arXiv](https://arxiv.org/abs/2609.11155) • [📥 PDF](https://arxiv.org/pdf/2609.11155)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Multi-Agent Reinforcement Learning (MARL) has emerged as a pivotal paradigm for complex decision-making in autonomous systems and air combat. While MARL has demonstrated significant potential in air combat, achieving sophisticated tactical coordin...

</details>

<details>
<summary><b>13. UniH^3: Unifying Hierarchical Homogeneity and Heterogeneity for All-in-One Medical Image Restoration</b> ⭐ 5</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11156) • [📄 arXiv](https://arxiv.org/abs/2609.11156) • [📥 PDF](https://arxiv.org/pdf/2609.11156)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/Yaziwel/UniH3)

> No abstract available.

</details>

<details>
<summary><b>14. Generative Late-Interaction Embeddings For Visual Document Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.11808) • [📄 arXiv](https://arxiv.org/abs/2609.11808) • [📥 PDF](https://arxiv.org/pdf/2609.11808)

**💻 Code:** [⭐ Code](https://github.com/mohammad2012191/GLIE) • [⭐ Code](https://github.com/huggingface)

> Visual document retrieval typically stores around a thousand vectors per page. GLIE learns a compact code that retrieves pages and supports on-demand regeneration of their embeddings. A small refiner and decoder are trained while the document enco...

</details>

<details>
<summary><b>15. MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10016) • [📄 arXiv](https://arxiv.org/abs/2609.10016) • [📥 PDF](https://arxiv.org/pdf/2609.10016)

**💻 Code:** [⭐ Code](https://github.com/continker/metrollm-bench) • [⭐ Code](https://github.com/huggingface)

> Can a small language model run a transit kiosk offline, adapted through a prose prompt rather than code? MetroLLM-Bench tests that with 955 tool-calling cases across six real metro systems (Atlanta, Doha, San Francisco, Taipei, Chicago, Beijing) a...

</details>

<details>
<summary><b>16. An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2609.10712) • [📄 arXiv](https://arxiv.org/abs/2609.10712) • [📥 PDF](https://arxiv.org/pdf/2609.10712)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>17. HyQuant: Hybrid-Precision Quantization for LLM Attention</b> ⭐ 8</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.27875) • [📄 arXiv](https://arxiv.org/abs/2608.27875) • [📥 PDF](https://arxiv.org/pdf/2608.27875)

**💻 Code:** [⭐ Code](https://github.com/jerrysfls/HyQuant) • [⭐ Code](https://github.com/huggingface)

> HyQuant: Hybrid-Precision Quantization for LLM Attention (EMNLP 2026 Main) Low-bit attention / KV-cache quantization often hurts long-context reasoning, because the error concentrates on a small set of tokens. Across Qwen3, Llama-3, Gemma 4 and Qw...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 17 |
| 📅 Today | [`2026-09-11.json`](data/daily/2026-09-11.json) | 17 |
| 📆 This Week | [`2026-W36.json`](data/weekly/2026-W36.json) | 99 |
| 🗓️ This Month | [`2026-09.json`](data/monthly/2026-09.json) | 266 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-09-11 | 17 | [View JSON](data/daily/2026-09-11.json) |
| 📄 2026-09-10 | 20 | [View JSON](data/daily/2026-09-10.json) |
| 📄 2026-09-09 | 37 | [View JSON](data/daily/2026-09-09.json) |
| 📄 2026-09-08 | 6 | [View JSON](data/daily/2026-09-08.json) |
| 📄 2026-09-07 | 19 | [View JSON](data/daily/2026-09-07.json) |
| 📄 2026-09-06 | 31 | [View JSON](data/daily/2026-09-06.json) |
| 📄 2026-09-05 | 31 | [View JSON](data/daily/2026-09-05.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W36 | 99 | [View JSON](data/weekly/2026-W36.json) |
| 📅 2026-W35 | 192 | [View JSON](data/weekly/2026-W35.json) |
| 📅 2026-W34 | 141 | [View JSON](data/weekly/2026-W34.json) |
| 📅 2026-W33 | 145 | [View JSON](data/weekly/2026-W33.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-09 | 266 | [View JSON](data/monthly/2026-09.json) |
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
