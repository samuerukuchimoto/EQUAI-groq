<div align="center">

# 🔍 BiasLens

### Real-time cognitive bias detection for human decision-making

[![Live Demo](https://img.shields.io/badge/Live%20Demo-equai--biaslens.streamlit.app-blue?style=for-the-badge)](https://equai-biaslens.streamlit.app)
[![GitHub](https://img.shields.io/badge/GitHub-samuerukuchimoto-black?style=for-the-badge&logo=github)](https://github.com/samuerukuchimoto)
[![Built With](https://img.shields.io/badge/AI-Llama%203.3%2070B%20%C2%B7%20Groq-purple?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Live%20%F0%9F%9F%A2-brightgreen?style=for-the-badge)]()

**[🚀 Try it live →](https://equai-biaslens.streamlit.app)**

*Type your thoughts about a person. Get an instant bias signal. Share with a colleague.*

</div>

---

## The problem — in one sentence

Every day, millions of decisions about people — who gets hired, promoted, funded, or partnered with — are made using language that reveals unconscious bias. No tool catches it **in the moment**, before the decision is made.

**BiasLens does.**

---

## What it does

You type your raw thoughts about a person — a candidate, a potential partner, a collaborator. BiasLens analyzes your language in real time and returns one of two signals:

| 🔴 RED | 🔵 BLUE |
|--------|---------|
| Bias detected | Objective reasoning |
| Gut-feel, appearance, affinity language | Evidence-based, competency-anchored |
| Subjective judgment dominates | Role requirements dominate |

With a **bias score (0–100%)**, the **specific flagged phrases**, and a **plain-English explanation** — so the decision-maker can actually learn from it.

---

## Live demo — tested today

> **Input:** *"She's brilliant technically but I'm not sure she'd fit our team culture. Something about her energy felt off during the interview. She comes from a very different background than the rest of us."*

> **BiasLens output:**
> 🔴 **RED — 80% bias probability**
>
> *"The statement expresses concern about the candidate's fit with the team culture based on subjective feelings and differences in background, which may indicate affinity bias or cultural bias. The phrase 'something about her energy felt off' is particularly subjective and suggests an intuitive judgment rather than an objective assessment."*

---

## Why now

- **$200B+** spent annually on hiring in the US. Bias-driven bad hires cost an average of $17,000 each (SHRM)
- **EU AI Act (2024)** classifies hiring AI as high-risk — companies need compliant, explainable tools now
- **DEI accountability** is at an all-time high — but existing tools audit job descriptions, not the actual human judgment making the call
- **LLMs reached the capability threshold** to do this reliably in 2024 — this product could not have existed two years ago

---

## How the AI works

BiasLens is a **prompt-engineered inference pipeline** built on Llama 3.3 70B (via Groq). This is a deliberate architectural choice — not a limitation.

```
User types decision language (natural text)
        ↓
Tokenization → embeddings in high-dimensional vector space
"energy felt off" clusters near bias concept vectors
"8 years Python experience" clusters near competency vectors
        ↓
Transformer attention layers compute semantic relationships
        ↓
Structured JSON output: { color, score, rationale, flags }
        ↓
Every result stored anonymously in Supabase
→ Building proprietary labeled dataset for future fine-tuning
```

**The real IP is the prompt** — a structured instruction set that operationalizes 40+ years of cognitive bias research (WEAT methodology, affinity/halo/horn effect taxonomy, culture-fit proxy detection) into a single inference call.

**The data moat builds automatically.** Every analysis is an anonymized training example. At 50,000 analyses we have enough to fine-tune a dedicated bias-detection model — reducing inference costs and increasing domain accuracy.

---

## Architecture

```
┌─────────────────────────────────────────┐
│           USER INTERFACE                │
│     Streamlit · Python · Free host      │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│           AI INFERENCE                  │
│   Llama 3.3 70B · Groq · 200 tok/sec   │
│   (V2: multimodal — vision + audio)     │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         DATA + TRACKING                 │
│  Supabase PostgreSQL · anonymous rows   │
│  color · score · bias_types · timestamp │
└─────────────────────────────────────────┘
```

---

## Roadmap

```
TODAY ──────── Q3 2025 ──────── Q1 2026 ──────── Q3 2026
  │                │                │                │
V1 Live         V2 Beta         V3 Enterprise    V4 API
Text analysis   + CV upload     + Audit trails   + B2B SaaS
Share links     + Photo/video   + GDPR module    + Fine-tuned
Free users      + Next.js UI    + Team dash        model
0 → 10K users   10K → 50K       Enterprise GTM   Series A
```

---

## For Investors

### The bet
We are not building a bias checker. We are building the **reputation layer for human judgment** — the tool that sits between a decision-maker's raw thought and the action that affects someone's life.

Every share is a network effect. Every analysis is a data point. Every Red result is a moment of self-awareness that brings the user back.

### Business model (V2)

| Tier | Price | Target |
|---|---|---|
| Free | $0 | Individual users — virality engine |
| Pro | $29/month | HR professionals, hiring managers |
| Team | $199/month | Teams of 5–20, shared dashboard |
| Enterprise | Custom | Compliance, audit logs, API access |

### Traction signals
- ✅ V1 shipped and live in under 24 hours
- ✅ Zero infrastructure cost to first 10,000 users
- ✅ Data collection begins day one
- ✅ Regulatory tailwind: EU AI Act creates demand for exactly this category
- ✅ Viral mechanic built in: every result is shareable

### What we're looking for
Pre-seed conversations. Target raise: **$500K–$1.5M**.

📩 [samuelclermont.contact.com](mailto:samuelclermont.contact.com) · [samuellouissaint.carrd.co](https://samuellouissaint.carrd.co)

---

## For Tech Founders & Collaborators

This is an early-stage, high-velocity project. One Python file, no over-engineering, live in production. Here is where skilled collaborators can have immediate impact:

| Problem | Skills needed | Priority |
|---|---|---|
| Fine-tune Llama 3.1 8B on our growing dataset | PyTorch, HuggingFace, LoRA | 🔴 High |
| Build multimodal pipeline (CV + image + audio) | OpenCV, Whisper, vision models | 🔴 High |
| Replace Streamlit with Next.js + FastAPI | React, TypeScript, Python | 🟡 Medium |
| WEAT/iEAT score implementation from scratch | NLP, embeddings, sklearn | 🟡 Medium |
| Animated video output (Red/Blue generative viz) | Three.js, Remotion, React | 🟢 V2 |
| EU AI Act compliance module + audit trail | Backend, data engineering | 🟢 V2 |

### Run locally in 3 commands
```bash
git clone https://github.com/samuerukuchimoto/EQUAI-groq
cd EQUAI-groq
pip install streamlit groq
# Add GROQ_API_KEY to .streamlit/secrets.toml (get free at groq.com)
streamlit run app.py
```

---

## For Hiring Managers — AI Technical PM

This project demonstrates end-to-end AI product ownership:

| Capability | Evidence |
|---|---|
| **Problem framing** | Identified gap in existing HR tech landscape (Textio, HireVue, Pymetrics) — none audit the decision-maker's own language |
| **AI/ML literacy** | Designed prompt engineering pipeline using WEAT methodology, embedding theory, and LLM inference constraints |
| **Zero-to-one execution** | Shipped working product in under 24 hours: concept → code → deployed → tested → documented |
| **Regulatory awareness** | Built V1/V2 phased rollout specifically to navigate EU AI Act Article 6 high-risk classification |
| **Growth strategy** | Designed viral share mechanic as core feature, not afterthought — every result generates a shareable link |
| **Data strategy** | Anonymous result collection from day one builds proprietary training dataset for future model fine-tuning |
| **Stakeholder communication** | README written simultaneously for three distinct audiences: investors, engineers, hiring managers |

**Looking for:** AI Technical PM, Product Lead AI/ML, or Founding PM roles at companies building with LLMs.

📩 [samuelclermont.contact.com](mailto:samuelclermont.contact.com) · [samuellouissaint.carrd.co](https://samuellouissaint.carrd.co)

---

## Tech stack — total cost $0

| Layer | Tool | Cost |
|---|---|---|
| AI inference | Llama 3.3 70B · Groq | **Free** (14,400 req/day) |
| Frontend | Streamlit | **Free** |
| Hosting | Streamlit Community Cloud | **Free** |
| Database | Supabase | **Free** (500MB) |
| Code | GitHub | **Free** |

---

## Research foundation

- Caliskan et al. (2017) — *Semantics derived from language corpora contain human-like biases* (WEAT)
- Pena et al. (2020) — *Bias in Multimodal AI: Testbed for Fair Automatic Recruitment*
- ViLBias (2024) — *Detecting and reasoning about bias in multimodal content*
- EU AI Act Annex III (2024) — High-risk AI classification for employment contexts

---

## License

MIT — open source, use freely, contribute back.

---

<div align="center">

**Built to make human decisions more fair.**

[🚀 Try BiasLens](https://equai-biaslens.streamlit.app) · [💬 Open an issue](https://github.com/samuerukuchimoto/EQUAI-groq/issues) · [📩 Contact](mailto:samuelclermont.contact.com)

*If this resonates — ⭐ star the repo. It signals traction to investors and recruiters.*

</div>
