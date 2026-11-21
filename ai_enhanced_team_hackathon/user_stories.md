# User Stories – AI Decision Helper & Sprint Prioritizer

## Core MVP User Stories

### US-01: Create a New Decision Session
- **As a** team lead or individual user,
- **I want to** enter a decision title, context description, and 2–4 candidate options,
- **So that** I can structure a complex choice for AI evaluation and team review.
- **Acceptance Criteria**:
  - Form validates a non-empty title and at least 2 distinct options.
  - Optional constraints (budget, deadline, priority criteria) can be attached.

### US-02: Generate AI Weighted Pros, Cons & Feasibility Scores
- **As a** decision creator,
- **I want** the AI assistant to analyze each option and produce structured pros, cons, hidden risks, and a 1–10 feasibility score,
- **So that** I can objectively compare trade-offs without manual bias.
- **Acceptance Criteria**:
  - AI returns valid JSON containing `pros[]`, `cons[]`, `risks[]`, and `score` (`1–10`) for every option.
  - Loading state and graceful error retry are displayed if the LLM call fails.

### US-03: Switch Evaluation Persona / Lens
- **As a** product builder,
- **I want to** re-evaluate the same options under different strategic lenses (*Speed-to-MVP*, *Cost-Efficiency*, *Long-Term Scalability*),
- **So that** I see how the recommended choice shifts based on current sprint priorities.
- **Acceptance Criteria**:
  - Selecting a persona triggers a fresh AI evaluation or displays cached persona results.
  - Score breakdowns visibly update per option.

### US-04: Share Decision Room via Link
- **As a** hackathon team member,
- **I want to** copy a shareable session URL for an active decision,
- **So that** my teammates can inspect the AI analysis and vote without creating an account.
- **Acceptance Criteria**:
  - Each decision session generates a unique slug/ID route (`/decisions/:id`).
  - One-click "Copy Link" button provides visual confirmation.

### US-05: Cast Team Votes & Leave Short Rationale
- **As a** collaborator in a decision room,
- **I want to** vote for my preferred option and attach a brief comment explaining why,
- **So that** the team reaches transparent consensus quickly.
- **Acceptance Criteria**:
  - Each participant can cast one active vote per decision (with ability to switch vote before lock).
  - Live vote counts and percentages update immediately on the option cards.

### US-06: AI Tie-Breaker & Consensus Summary
- **As a** team facilitator,
- **I want to** trigger an AI tie-breaker summary when votes are split,
- **So that** the AI synthesizes voter comments with risk scores to propose a final resolution.
- **Acceptance Criteria**:
  - Available whenever at least 2 votes have been cast.
  - Outputs a concise 3–4 sentence recommendation highlighting key trade-offs.

### US-07: Lock Final Decision
- **As a** decision creator,
- **I want to** mark a winning option as "Finalized / Locked",
- **So that** voting closes and the team has an official record of what was decided.
- **Acceptance Criteria**:
  - Locked decisions disable further voting and display a "Decided" badge with timestamp.

### US-08: Export Decision Report (Markdown & JSON)
- **As a** developer documenting architecture choices,
- **I want to** export the completed decision analysis and vote tally as Markdown or JSON,
- **So that** I can paste it directly into a GitHub PR, README, or Notion doc.
- **Acceptance Criteria**:
  - Clicking "Export Markdown" downloads or copies a clean formatted summary table.
  - Clicking "Export JSON" downloads the structured decision payload.

### US-09: View Recent Decision History
- **As a** returning user,
- **I want to** browse my past decision sessions filtered by status (*Open* vs. *Locked*),
- **So that** I can revisit previous architectural or sprint trade-offs.
- **Acceptance Criteria**:
  - Dashboard lists recent decisions sorted by `created_at` descending.
