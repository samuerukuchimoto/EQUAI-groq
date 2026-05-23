<div align="center">

# 🔍 BiasLens

### Real-time cognitive bias detection for human decision-making

[![Live Demo](https://img.shields.io/badge/Live%20Demo-biaslens.streamlit.app-blue?style=for-the-badge)](https://biaslens.streamlit.app)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live%20Beta-orange?style=for-the-badge)]()
[![Built With](https://img.shields.io/badge/AI-Llama%203.3%2070B-purple?style=for-the-badge)]()

**[Try it live →](https://biaslens.streamlit.app) · [Watch demo](#demo) · [Collaborate](#-for-technical-collaborators) · [Invest](#-for-investors)**

</div>

---

## The problem — in one sentence

Every day, millions of decisions about people — who gets hired, promoted, funded, or partnered with — are made using language that reveals unconscious bias. No one catches it in the moment.

**BiasLens does.**

---

## What it does

You type your raw thoughts about a person — a candidate, a potential partner, a collaborator.
BiasLens runs multimodal AI analysis on your language and returns one of two signals:

| 🔴 RED | 🔵 BLUE |
|--------|---------|
| Bias detected | Objective reasoning |
| Gut-feel, appearance, affinity language | Evidence-based, competency-anchored |
| Subjective judgment dominates | Role requirements dominate |

With a bias score (0–100%), the specific flagged phrases, and the type of bias detected — so the decision-maker can actually learn from it, not just be judged.

**Then they share the result with a colleague.** That share is the growth engine.

---

## Demo

> *Input:* "She's technically solid but I'm not sure she'd fit the team culture. Something about her energy felt off. She's from a very different background than us."

> *BiasLens output:*
> 🔴 **RED — 84% bias probability**
> Flagged: `"fit the team culture"` · `"her energy felt off"` · `"very different background"`
> Bias types detected: `Culture Fit Proxy` · `Affinity Bias` · `Vague Negative Framing`
> Analysis: *The evaluator's language consistently anchors to personal similarity and subjective impression rather than demonstrated competence or role requirements. The phrase "different background" functions as an affinity signal with no professional context provided.*

---

## Why now

- **$200B+** is spent annually on hiring in the US. Bias-driven bad hires cost an average of $17,000 each (SHRM, 2023).
- **EU AI Act (2024)** classifies hiring AI as high-risk — companies are scrambling for compliant, explainable tools.
- **DEI pressure is at an all-time high** — but existing tools audit job descriptions, not the actual human judgment making the call.
- **LLMs reached the capability threshold** to do this reliably in 2024. This product could not have existed two years ago.

---

## Market

| Segment | Size | Our Entry |
|---|---|---|
| HR Tech Global | $39.9B by 2029 | V2 enterprise suite |
| DEI software | $3.4B by 2026 | V2 audit module |
| Collaboration tools | $50B+ | **V1 — right now** |

V1 is intentionally positioned as a **general collaboration and partnership tool** — avoiding high-risk EU AI Act classification while we build the user base and refine the model. V2 enters the enterprise HR market with audit trails, GDPR compliance, and XAI reports already validated by 10,000+ real-world analyses.

---

## Traction

> *Updated live — this section reflects real usage*

| Metric | Count |
|---|---|
| 🔍 Total analyses run | *[live counter — Supabase]* |
| 📤 Share rate | *[% of users who share results]* |
| 🌍 Countries reached | *[PostHog geo data]* |
| ↩️ Return user rate | *[7-day retention]* |

---

## How the AI works — for technical readers

BiasLens is not a fine-tuned model. It is a **prompt-engineered inference pipeline** built on top of Llama 3.3 70B (via Groq) — and that is a deliberate architectural choice.

```
User input (natural language)
        ↓
Tokenization → vector embeddings in 4096-dimensional space
        ↓
Transformer attention layers compute semantic relationships
"energy felt off" clusters near bias concept vectors
"8 years Python experience" clusters near competency vectors
        ↓
Structured JSON output constrained by response_format
{ color, score, rationale, flags, bias_types }
        ↓
Supabase: every result stored anonymously
→ Building a proprietary labeled dataset for future fine-tuning
```

**The real IP is the prompt** — a 600-token instruction set that operationalizes 40+ years of cognitive bias research (WEAT methodology, iEAT visual framing, affinity/halo/horn effect taxonomy) into a single inference call.

**The data moat builds automatically.** Every analysis is an anonymized training example. At 50,000 analyses we have enough to fine-tune a dedicated bias-detection model that we own entirely — dramatically reducing inference costs and increasing accuracy on domain-specific language.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    USER INTERFACE                    │
│              Streamlit (Python, free host)           │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                   AI INFERENCE                       │
│         Llama 3.3 70B · Groq API · 200 t/s          │
│         (V2: multimodal — vision + audio)            │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                 DATA + TRACKING                      │
│    Supabase PostgreSQL · anonymous per-analysis row  │
│    color · score · bias_types · shared · timestamp   │
└─────────────────────────────────────────────────────┘
```

**V1 (now):** Text only · Streamlit · Groq · Supabase · share links
**V2 (Q3 2025):** + CV upload · photo analysis · video transcription · Next.js
**V3 (Q1 2026):** Enterprise HR suite · audit trails · EU AI Act compliance · team dashboards

---

## For Investors

### The bet

We are not building a bias checker. We are building **the reputation layer for human judgment** — the tool that sits between a decision-maker's raw thought and the action that affects someone's life.

Every share is a network effect. Every analysis is a data point. Every Red result is a moment of self-awareness that brings the user back.

### Business model (V2)

| Tier | Price | Target |
|---|---|---|
| Free | $0 | Individual users, virality engine |
| Pro | $29/month | Individual HR professionals, hiring managers |
| Team | $199/month | Teams of 5–20, shared dashboard |
| Enterprise | Custom | Companies, compliance, audit logs, API access |

### Why this team / why now

- V1 shipped in under 24 hours from concept to live URL
- Zero infrastructure cost to 10,000 users
- Data collection begins on day one
- Regulatory tailwind: EU AI Act creates demand for exactly this category

### What we're looking for

Pre-seed funding to hire one ML engineer (fine-tuning pipeline) and one growth lead.
Target raise: **$500K–$1.5M** at idea-stage valuation.

### 📩 Contact
- **Email:** samuelclermont.contact@gmail.com
- **Website:** samuellouissaint.carrd.co
- **LinkedIn:** [samuel-louissaint](https://www.linkedin.com/in/samuel-louissaint-92366b382)

---

## For Technical Collaborators

This is an early-stage, high-velocity project. The codebase is intentionally lean — one Python file, no over-engineering. Here is where skilled collaborators can have immediate impact:

### Open problems we want to solve together

| Problem | Skills needed | Priority |
|---|---|---|
| Fine-tune Llama 3.1 8B on our growing dataset | PyTorch, HuggingFace, LoRA | 🔴 High |
| Build multimodal pipeline (image + audio bias) | OpenCV, Whisper, vision models | 🔴 High |
| Replace Streamlit with Next.js + FastAPI | React, TypeScript, Python | 🟡 Medium |
| WEAT/iEAT score implementation from scratch | NLP, embedding math, sklearn | 🟡 Medium |
| Build audit trail + GDPR compliance module | Backend, data engineering | 🟢 V2 |
| Animated video output (Red/Blue generative viz) | Three.js, Remotion, React | 🟢 V2 |

### How to contribute

```bash
# 1. Fork the repo
git clone https://github.com/samuerukuchimoto/biaslens
cd biaslens

# 2. Set up environment
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Add your free Groq key (groq.com — no credit card)
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit secrets.toml with your GROQ_API_KEY

# 4. Run locally
streamlit run app.py
# Opens at http://localhost:8501

# 5. Open a PR — we review within 24h
```

### Research foundation

This project is grounded in published academic work:

- Caliskan et al. (2017) — *Semantics derived from language corpora contain human-like biases* (WEAT methodology)
- Pena et al. (2020) — *Bias in Multimodal AI: Testbed for Fair Automatic Recruitment* (CV)
- ViLBias framework (2024) — *Detecting and reasoning about bias in multimodal content* (image)
- EU AI Act Annex III (2024) — High-risk AI system classification for employment use cases

---

## Tech stack

| Layer | Tool | Cost |
|---|---|---|
| AI inference | Llama 3.3 70B · Groq | **Free** (14,400 req/day) |
| Frontend | Streamlit | **Free** |
| Hosting | Streamlit Community Cloud | **Free** |
| Database | Supabase | **Free** (500MB) |
| Analytics | PostHog | **Free** (1M events/month) |
| CI/CD | GitHub Actions | **Free** |

**Total monthly cost at 10,000 users: $0.**

---

## Roadmap

```
NOW ──────── Q3 2025 ──────── Q1 2026 ──────── Q3 2026
  │               │                │                │
V1 Live        V2 Beta         V3 Enterprise    V4 API
Text only      + CV upload     + Audit trails   + B2B SaaS
Share links    + Photo/video   + GDPR module    + Fine-tuned
Free users     + Next.js UI    + Team dash      + Custom models
0→10K users    10K→50K         Enterprise GTM   Series A
```

---

## License

MIT — open source, use freely, contribute back.

---

<div align="center">

**Built to make human decisions more fair.**

[🚀 Try BiasLens](https://biaslens.streamlit.app) · [💬 Open an issue](https://github.com/samuerukuchimoto/biaslens/issues) · [📩 Contact the founder](mailto:samuelclermont.contact.com)

*If this resonates — star the repo. It signals traction to investors.*

</div>
