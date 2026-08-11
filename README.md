<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-17-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-6549+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📅 This Week</b><br/><font size="5">36</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">278</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">6549+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** August 11, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09802) • [📄 arXiv](https://arxiv.org/abs/2608.09802) • [📥 PDF](https://arxiv.org/pdf/2608.09802)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> New benchmark for coding agents with more complex problems.

</details>

<details>
<summary><b>2. Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09819) • [📄 arXiv](https://arxiv.org/abs/2608.09819) • [📥 PDF](https://arxiv.org/pdf/2608.09819)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA

</details>

<details>
<summary><b>3. Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.07169) • [📄 arXiv](https://arxiv.org/abs/2608.07169) • [📥 PDF](https://arxiv.org/pdf/2608.07169)

**💻 Code:** [⭐ Code](https://github.com/taeilkim2465/agentic_memory_distillation) • [⭐ Code](https://github.com/huggingface)

> We propose Agent Memory Distillation (AMD) , a framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher t...

</details>

<details>
<summary><b>4. Motif 3: Technical Report</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09119) • [📄 arXiv](https://arxiv.org/abs/2608.09119) • [📥 PDF](https://arxiv.org/pdf/2608.09119)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>5. Sci-VBench: Evaluating Knowledge- and Reasoning-Intensive Video Generation in Science Domains</b> ⭐ 3</summary>

<br/>

**👥 Authors:** Yilun Zhao, Zheyuan Yang, Lin Fu, Tingyu Song, Diandian Zhang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09873) • [📄 arXiv](https://arxiv.org/abs/2608.09873) • [📥 PDF](https://arxiv.org/pdf/2608.09873)

**💻 Code:** [⭐ Code](https://github.com/sci-vbench/sci-vbench) • [⭐ Code](https://github.com/huggingface)

> We also evaluate the latest models Gemini-Omni-Flash, HappyHorse-1.1, and MiniMax-H3. Welcome any feedback!

</details>

<details>
<summary><b>6. Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution</b> ⭐ 1.06k</summary>

<br/>

**👥 Authors:** Roman Yampolskiy, Nikita Dragunov, Andrei Kaznacheev, Andrei Gritsaev, Anton Razzhigaev

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08311) • [📄 arXiv](https://arxiv.org/abs/2608.08311) • [📥 PDF](https://arxiv.org/pdf/2608.08311)

**💻 Code:** [⭐ Code](https://github.com/razzant/ouroboros) • [⭐ Code](https://github.com/huggingface)

> We present Ouroboros, a self-developing agent harness whose tools, prompts, context assembly, and core implementation improve through reviewed commits that become the runtime for later work. Core evolution proceeds in two modes. In recursive free ...

</details>

<details>
<summary><b>7. SPOT: Sparse Probing and Outcome Calibration for On-Policy Distillation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.04419) • [📄 arXiv](https://arxiv.org/abs/2608.04419) • [📥 PDF](https://arxiv.org/pdf/2608.04419)

**💻 Code:** [⭐ Code](https://github.com/QuZikun/SPOT) • [⭐ Code](https://github.com/huggingface)

> Standard OPD may under-cover plausible alternatives, while EOPD relies solely on teacher entropy and uncalibrated targets. SPOT sparsely probes informative positions and uses verifier-scored continuations to construct outcome-calibrated targets. A...

</details>

<details>
<summary><b>8. What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conversational Systems</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.07565) • [📄 arXiv](https://arxiv.org/abs/2608.07565) • [📥 PDF](https://arxiv.org/pdf/2608.07565)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Image-generation conversations rarely end after a single turn—but suggesting what users should edit next requires more than text-only recommendation. In this work, we study follow-up edit suggestions grounded in the current image and user intent. ...

</details>

<details>
<summary><b>9. OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08097) • [📄 arXiv](https://arxiv.org/abs/2608.08097) • [📥 PDF](https://arxiv.org/pdf/2608.08097)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We proposed OasisKV, a KV-cache prefetching framework, to expand effective in-decode memory capacity using off-GPU memory.

</details>

<details>
<summary><b>10. RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States</b> ⭐ 8</summary>

<br/>

**👥 Authors:** Yinan Chen, Tiehan Fan, Yihong Zhuang, Zhennan Chen, yangyiking

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.02508) • [📄 arXiv](https://arxiv.org/abs/2608.02508) • [📥 PDF](https://arxiv.org/pdf/2608.02508)

**💻 Code:** [⭐ Code](https://github.com/YOUNG-fnxm/RoMeRL) • [⭐ Code](https://github.com/huggingface)

> Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, ...

</details>

<details>
<summary><b>11. Evo-Bench: Can Language Models Improve Agent Harness?</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09096) • [📄 arXiv](https://arxiv.org/abs/2608.09096) • [📥 PDF](https://arxiv.org/pdf/2608.09096)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/RUCAIBox/Evo-Bench)

> Large Language Models (LLMs) have driven rapid progress in autonomous agents, yet standard evaluations remain confined to static task solving. An emerging frontier is harness evolution---the agent's capacity to autonomously optimize its own operat...

</details>

<details>
<summary><b>12. Evidence-RL: Towards Evidence-intensive Visual Reasoning</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Cheng Yang, Zhangquan Chen, Chengming Xu, Xinlei Yu, Haojie Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.08021) • [📄 arXiv](https://arxiv.org/abs/2608.08021) • [📥 PDF](https://arxiv.org/pdf/2608.08021)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Vision-Language Models (VLMs) should answer from concrete image evidence rather than language priors, dataset shortcuts, or irrelevant visual context. Existing perception-aware post-training methods encourage image use through global perturbations...

</details>

<details>
<summary><b>13. Scaling Inherently Interpretable Language Models</b> ⭐ 238</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.07594) • [📄 arXiv](https://arxiv.org/abs/2608.07594) • [📥 PDF](https://arxiv.org/pdf/2608.07594)

**💻 Code:** [⭐ Code](https://github.com/guidelabs/steerling) • [⭐ Code](https://github.com/huggingface)

> Technical Report Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this prem...

</details>

<details>
<summary><b>14. RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance</b> ⭐ 7</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09853) • [📄 arXiv](https://arxiv.org/abs/2608.09853) • [📥 PDF](https://arxiv.org/pdf/2608.09853)

**💻 Code:** [⭐ Code](https://github.com/alibaba-damo-academy/RynnValue) • [⭐ Code](https://github.com/huggingface)

> Model weights and code are available at Github: https://github.com/alibaba-damo-academy/RynnValue HuggingFace: https://huggingface.co/collections/Alibaba-DAMO-Academy/rynnvalue Modelscope: https://www.modelscope.cn/collections/DAMO_Academy/RynnValue

</details>

<details>
<summary><b>15. Intent Speaks Louder: Controllable User Simulation Beyond Response Imitation</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.09420) • [📄 arXiv](https://arxiv.org/abs/2608.09420) • [📥 PDF](https://arxiv.org/pdf/2608.09420)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/ptwang773/UserIDA)

> User simulators are widely used as scalable environments for training and evaluating interactive assistants. Generating the next user turn is inherently one-to-many: the same profile and dialogue context may support multiple plausible continuation...

</details>

<details>
<summary><b>16. An End-to-End Agent Auditing Engine</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Xia Hu, Yingjun Shang, Chenyue Yu, Mingxun Zhang, Haoning Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.07346) • [📄 arXiv](https://arxiv.org/abs/2608.07346) • [📥 PDF](https://arxiv.org/pdf/2608.07346)

**💻 Code:** [⭐ Code](https://github.com/datamllab/A2E) • [⭐ Code](https://github.com/huggingface)

> An End-to-End Agent Auditing Engine Our code is available at https://github.com/datamllab/A2E

</details>

<details>
<summary><b>17. Factorized Hypothesis Search for Evidence-to-Taxonomy Retrieval</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2608.06614) • [📄 arXiv](https://arxiv.org/abs/2608.06614) • [📥 PDF](https://arxiv.org/pdf/2608.06614)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Large-taxonomy retrieval often assumes that the input already expresses the target concept. In many settings, however, the input is indirect evidence, such as a table cell whose meaning depends on its row, column, datatype, and context. We call th...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 17 |
| 📅 Today | [`2026-08-11.json`](data/daily/2026-08-11.json) | 17 |
| 📆 This Week | [`2026-W32.json`](data/weekly/2026-W32.json) | 36 |
| 🗓️ This Month | [`2026-08.json`](data/monthly/2026-08.json) | 278 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-08-11 | 17 | [View JSON](data/daily/2026-08-11.json) |
| 📄 2026-08-10 | 19 | [View JSON](data/daily/2026-08-10.json) |
| 📄 2026-08-09 | 30 | [View JSON](data/daily/2026-08-09.json) |
| 📄 2026-08-08 | 30 | [View JSON](data/daily/2026-08-08.json) |
| 📄 2026-08-07 | 17 | [View JSON](data/daily/2026-08-07.json) |
| 📄 2026-08-06 | 23 | [View JSON](data/daily/2026-08-06.json) |
| 📄 2026-08-05 | 24 | [View JSON](data/daily/2026-08-05.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W32 | 36 | [View JSON](data/weekly/2026-W32.json) |
| 📅 2026-W31 | 166 | [View JSON](data/weekly/2026-W31.json) |
| 📅 2026-W30 | 174 | [View JSON](data/weekly/2026-W30.json) |
| 📅 2026-W29 | 129 | [View JSON](data/weekly/2026-W29.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-08 | 278 | [View JSON](data/monthly/2026-08.json) |
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
