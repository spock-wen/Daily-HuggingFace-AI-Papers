<div align="center">

# 🤖 Daily HuggingFace AI Papers

### 📊 Your Automated AI Research Companion

> **Never miss groundbreaking AI research again!** Get daily updates on the hottest papers from HuggingFace, automatically curated and archived. Perfect for researchers, ML engineers, and AI enthusiasts. 🔥

[![Update Daily](https://img.shields.io/badge/Update-Daily-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/actions)
[![Papers Today](https://img.shields.io/badge/Papers%20Today-16-blue?style=for-the-badge&logo=arxiv)](data/latest.json)
[![Total Papers](https://img.shields.io/badge/Total%20Papers-5393+-orange?style=for-the-badge&logo=academia)](data/)
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
<td align="center"><b>📄 Today</b><br/><font size="5">16</font><br/>papers</td>
<td align="center"><b>📅 This Week</b><br/><font size="5">101</font><br/>papers</td>
<td align="center"><b>📆 This Month</b><br/><font size="5">571</font><br/>papers</td>
<td align="center"><b>🗄️ Total Archive</b><br/><font size="5">5393+</font><br/>papers</td>
</tr>
</table>

**Last Updated:** June 18, 2026

---

## 🔥 Today's Trending Papers

> Latest AI research papers from HuggingFace Papers, updated daily

<details>
<summary><b>1. Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19338) • [📄 arXiv](https://arxiv.org/abs/2606.19338) • [📥 PDF](https://arxiv.org/pdf/2606.19338)

**💻 Code:** [⭐ Code](https://github.com/InternLM/RNGBench) • [⭐ Code](https://github.com/huggingface)

> 🔥Github Repo: https://github.com/InternLM/RNGBench

</details>

<details>
<summary><b>2. Guava: An Effective and Universal Harness for Embodied Manipulation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Tianyi Zhou, Peng Shi, Shaoxiong Yao, Xirui Li, Haowen Liu

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18363) • [📄 arXiv](https://arxiv.org/abs/2606.18363) • [📥 PDF](https://arxiv.org/pdf/2606.18363)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> Language models trained on large-scale vision-language data have demonstrated strong potential for embodied agents. Harnessing models through embodied tools use offers a promising alternative to end-to-end vision-language-action systems by combini...

</details>

<details>
<summary><b>3. Kairos: A Native World Model Stack for Physical AI</b> ⭐ 712</summary>

<br/>

**👥 Authors:** Tao Huang, Qiming Zhang, Shan You, Fei Wang, Kairos Team

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.16533) • [📄 arXiv](https://arxiv.org/abs/2606.16533) • [📥 PDF](https://arxiv.org/pdf/2606.16533)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/kairos-agi/kairos-sensenova)

> Kairos Technical Report

</details>

<details>
<summary><b>4. Reinforcing Dual-Path Reasoning in Spatial Vision Language Models</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.17539) • [📄 arXiv](https://arxiv.org/abs/2606.17539) • [📥 PDF](https://arxiv.org/pdf/2606.17539)

**💻 Code:** [⭐ Code](https://github.com/jiyt17/SR-REAL) • [⭐ Code](https://github.com/huggingface)

> We present a unified framework that equips a spatial VLM with two complementary reasoning paths: Language-Only Reasoning (LOR), which performs step-by-step linguistic deduction, and Detect-Then-Reason (DTR), which detects 3D geometric cues (e.g., ...

</details>

<details>
<summary><b>5. SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18322) • [📄 arXiv](https://arxiv.org/abs/2606.18322) • [📥 PDF](https://arxiv.org/pdf/2606.18322)

**💻 Code:** [⭐ Code](https://github.com/Mingyuee88/sae-post-intervention-recovery) • [⭐ Code](https://github.com/huggingface)

> SAE interventions are not as reliable as they look! 🧠🔒 We show that clamping unsafe SAE features does not reliably remove bad behaviors. Even with interventions active, suppressed behaviors can still recover through alternative residual-space dire...

</details>

<details>
<summary><b>6. Trust the Right Teacher: Quality-Aware Self-Distillation for GUI Grounding</b> ⭐ 0</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18101) • [📄 arXiv](https://arxiv.org/abs/2606.18101) • [📥 PDF](https://arxiv.org/pdf/2606.18101)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> We use GUI grounding as a directly verifiable testbed to study a broader question in on-policy self-distillation: when the student-generated prefix is already wrong, are the teacher's next-token signals still reliable? Because GUI grounding answer...

</details>

<details>
<summary><b>7. Native Active Perception as Reasoning for Omni-Modal Understanding</b> ⭐ 9</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19341) • [📄 arXiv](https://arxiv.org/abs/2606.19341) • [📥 PDF](https://arxiv.org/pdf/2606.19341)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/harryhsing/OmniAgent)

> TL;DR: OmniAgent is, to our knowledge, the first native omni-modal agent that turns video understanding into active perception . Instead of watching every frame, it runs an Observation–Thought–Action loop, fetching only the frames, audio, or clips...

</details>

<details>
<summary><b>8. Sumi: Open Uniform Diffusion Language Model from Scratch</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Keisuke Sakaguchi, Ryosuke Matsuda, Wataru Ikeda, Keito Kudo, Mengyu Ye

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19005) • [📄 arXiv](https://arxiv.org/abs/2606.19005) • [📥 PDF](https://arxiv.org/pdf/2606.19005)

**💻 Code:** [⭐ Code](https://github.com/tohoku-nlp/sumi) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>9. SciOrch: Learning to Orchestrate Expert LLMs for Solving Frontier Multimodal Scientific Reasoning Tasks</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Siki Chen, Wanghan Xu, Lian Zhang, Xiangyuan Xue, Jingru Guo

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.15872) • [📄 arXiv](https://arxiv.org/abs/2606.15872) • [📥 PDF](https://arxiv.org/pdf/2606.15872)

**💻 Code:** [⭐ Code](https://github.com/llexieguo/SciOrch) • [⭐ Code](https://github.com/huggingface)

> We’re excited to share our latest work, SciOrch: Learning to Orchestrate Expert LLMs for Frontier Multimodal Scientific Reasoning 🧬 Scientific reasoning often requires reading complex figures, combining knowledge from different fields, and solving...

</details>

<details>
<summary><b>10. Learning User Simulators with Turing Rewards</b> ⭐ 1</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.19336) • [📄 arXiv](https://arxiv.org/abs/2606.19336) • [📥 PDF](https://arxiv.org/pdf/2606.19336)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/SusanWYS/turing-rl)

> We propose Turing-RL: a Turing-Test-based reinforcement learning approach for training user simulator models. Across two different domains—conversational chat and Reddit forum discussion—we find that Turing-RL consistently outperforms baseline met...

</details>

<details>
<summary><b>11. Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness</b> ⭐ 12</summary>

<br/>

**👥 Authors:** Shenghan Zuo, Zijian Hu, Ziyue Yang, Hanqi Li, Zijian Wang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18874) • [📄 arXiv](https://arxiv.org/abs/2606.18874) • [📥 PDF](https://arxiv.org/pdf/2606.18874)

**💻 Code:** [⭐ Code](https://github.com/OpenDFM/Xcientist) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>12. PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Jiazhao Zhang, Zhiyuan Yu, Junyan Xu, Xuan Lv, Yuhang Huang

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18375) • [📄 arXiv](https://arxiv.org/abs/2606.18375) • [📥 PDF](https://arxiv.org/pdf/2606.18375)

**💻 Code:** [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>13. CEO-Bench: Can Agents Play the Long Game?</b> ⭐ 1</summary>

<br/>

**👥 Authors:** Zhuang Liu, Karthik Narasimhan, Haozhe Chen

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18543) • [📄 arXiv](https://arxiv.org/abs/2606.18543) • [📥 PDF](https://arxiv.org/pdf/2606.18543)

**💻 Code:** [⭐ Code](https://github.com/zlab-princeton/ceobench-src) • [⭐ Code](https://github.com/huggingface)

> No abstract available.

</details>

<details>
<summary><b>14. IndustryBench-MIPU: Benchmarking Multi-Image Attribute Value Extraction for Industrial Products</b> ⭐ 3</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.14383) • [📄 arXiv](https://arxiv.org/abs/2606.14383) • [📥 PDF](https://arxiv.org/pdf/2606.14383)

**💻 Code:** [⭐ Code](https://github.com/alibaba-multimodal-industrial-ai/IndustryBench-MIPU) • [⭐ Code](https://github.com/huggingface)

> Hi everyone! We are excited to share our team's latest work from Alibaba: IndustryBench-MIPU . While MLLMs are increasingly deployed for general visual tasks, understanding complex industrial products requires assembling dense technical specificat...

</details>

<details>
<summary><b>15. Physics-IQ Verified</b> ⭐ 0</summary>

<br/>

**👥 Authors:** Priyank Jaini, Stefan Bauer, Hilde Kuehne, Yuki M Asano, Tim Rädsch

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.18943) • [📄 arXiv](https://arxiv.org/abs/2606.18943) • [📥 PDF](https://arxiv.org/pdf/2606.18943)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/google-deepmind/physics-iq-benchmark)

> Github: https://github.com/google-deepmind/physics-iq-benchmark

</details>

<details>
<summary><b>16. Beyond Alignment: Value Diversity as a Collective Property in Multicultural Agent Systems</b> ⭐ 2</summary>

<br/>

**🔗 Links:** [🤗 HuggingFace](https://huggingface.co/papers/2606.05985) • [📄 arXiv](https://arxiv.org/abs/2606.05985) • [📥 PDF](https://arxiv.org/pdf/2606.05985)

**💻 Code:** [⭐ Code](https://github.com/huggingface) • [⭐ Code](https://github.com/iNLP-Lab/MultiAgent-Diversity)

> Multi-agent systems are inherently multicultural as well. This is especially apparent given the recent popularity of Moltbook and the subsequent line of analytical work (e.g., #MoltNet). These build on the premise that different agents represent d...

</details>

---

## 📅 Historical Archives

### 📊 Quick Access

| Type | Link | Papers |
|------|------|--------|
| 🕐 Latest | [`latest.json`](data/latest.json) | 16 |
| 📅 Today | [`2026-06-18.json`](data/daily/2026-06-18.json) | 16 |
| 📆 This Week | [`2026-W24.json`](data/weekly/2026-W24.json) | 101 |
| 🗓️ This Month | [`2026-06.json`](data/monthly/2026-06.json) | 571 |

### 📜 Recent Days

| Date | Papers | Link |
|------|--------|------|
| 📌 2026-06-18 | 16 | [View JSON](data/daily/2026-06-18.json) |
| 📄 2026-06-17 | 21 | [View JSON](data/daily/2026-06-17.json) |
| 📄 2026-06-16 | 32 | [View JSON](data/daily/2026-06-16.json) |
| 📄 2026-06-15 | 32 | [View JSON](data/daily/2026-06-15.json) |
| 📄 2026-06-14 | 44 | [View JSON](data/daily/2026-06-14.json) |
| 📄 2026-06-13 | 44 | [View JSON](data/daily/2026-06-13.json) |
| 📄 2026-06-12 | 35 | [View JSON](data/daily/2026-06-12.json) |

### 📚 Weekly Archives

| Week | Papers | Link |
|------|--------|------|
| 📅 2026-W24 | 101 | [View JSON](data/weekly/2026-W24.json) |
| 📅 2026-W23 | 247 | [View JSON](data/weekly/2026-W23.json) |
| 📅 2026-W22 | 223 | [View JSON](data/weekly/2026-W22.json) |
| 📅 2026-W21 | 283 | [View JSON](data/weekly/2026-W21.json) |

### 🗂️ Monthly Archives

| Month | Papers | Link |
|------|--------|------|
| 🗓️ 2026-06 | 571 | [View JSON](data/monthly/2026-06.json) |
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
