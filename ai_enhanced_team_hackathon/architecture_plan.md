# High-Level Architecture Plan – AI Decision Helper & Sprint Prioritizer

## 1. System Architecture Diagram

+-------------------------------------------------------------------+
|                        Client (React + Vite)                      |
|  - Decision Builder Form      - Persona Lens Switcher             |
|  - Weighted Pros/Cons Cards   - Live Voting & Markdown Exporter   |
+---------------------------------+---------------------------------+
                                  | HTTPS / REST JSON
                                  v
+-------------------------------------------------------------------+
|                   Backend API (FastAPI / Node.js)                 |
|  - Input Validation & Rate Limiter                                |
|  - Prompt Orchestrator & JSON Schema Parser                       |
|  - Consensus & Tie-Breaker Aggregator                             |
+----------------+---------------------------------+----------------+
                 |                                 |
                 v                                 v
+---------------------------------+ +-------------------------------+
|   Database (PostgreSQL/Supabase)| |   LLM Provider (OpenAI /      |
|  - decisions, options           | |   Gemini Structured Output)   |
|  - ai_analyses, votes           | |  - Persona-conditioned rubric |
+---------------------------------+ +-------------------------------+

---

## 2. Component Breakdown

### Frontend Layer (React + Tailwind CSS)
- **Decision Composer**: Captures title, context constraints, and 2–4 options with client-side validation.
- **Comparison Matrix View**: Side-by-side responsive cards showing AI feasibility scores (1–10), pros, cons, risks, and live vote bars.
- **Persona Selector Bar**: Switches between *Balanced*, *Speed-to-MVP*, *Cost-Efficiency*, and *Scalability* lenses without losing existing vote state.
- **Client-Side Exporter**: Serializes the active decision, AI analysis, and vote breakdown directly into downloadable `.md` or `.json` files.

### Backend API Layer (FastAPI / Express REST Service)
- **REST Endpoints**:
  - `POST /api/decisions` – Creates a decision + options and triggers initial AI evaluation.
  - `GET /api/decisions/:slug` – Fetches full decision state, cached AI analyses, and aggregated votes.
  - `POST /api/decisions/:slug/analyze` – Runs persona-specific AI scoring and persists `AIAnalysis` rows.
  - `POST /api/decisions/:slug/votes` – Upserts a participant's vote (rejected if `status == 'locked'`).
  - `POST /api/decisions/:slug/tie-breaker` – Synthesizes voter comments + option risks into a final AI recommendation.
  - `PATCH /api/decisions/:slug/lock` – Locks the decision and records `winning_option_id`.
- **Reliability & Guardrails**:
  - Enforces strict JSON schema validation on LLM responses with automatic retry on malformed output.
  - Applies IP/session rate limiting on AI endpoints to protect API quota during hackathon demos.

### Data Persistence Layer (PostgreSQL / Supabase)
- Relational schema (`decisions`, `options`, `ai_analyses`, `votes`) with cascading deletes and unique `(decision_id, voter_fingerprint)` vote constraints.
- Caches `AIAnalysis` records by `(option_id, persona)` so toggling personas repeatedly does not incur redundant LLM latency or token costs.

---

## 3. 24-Hour Hackathon Delivery & Deployment Plan
1. **Hours 0–3 (Setup & Schema)**: Initialize monorepo, configure Supabase PostgreSQL tables, and scaffold React + FastAPI boilerplate.
2. **Hours 3–10 (Core AI Pipeline)**: Implement prompt templates, JSON schema parser, and `POST /api/decisions` + `/analyze` endpoints.
3. **Hours 10–18 (UI & Team Voting)**: Build comparison matrix cards, persona switcher, shareable links, and live voting endpoints.
4. **Hours 18–22 (Testing & Export)**: Add unit/API tests (`pytest` + `Jest`), Markdown/JSON export, and error boundaries.
5. **Hours 22–24 (Deployment & Demo)**: Deploy frontend on **Vercel**, backend on **Render**, verify live end-to-end flow, and record demo walkthrough.
