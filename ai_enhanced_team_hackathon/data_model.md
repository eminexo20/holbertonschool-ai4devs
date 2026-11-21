# Data Model – AI Decision Helper & Sprint Prioritizer

## Entity-Relationship Overview

[Decision] 1 ────< * [Option] 1 ────< * [Vote]
    │
    └────< * [AIAnalysis]

---

## Entities

### 1. Decision
Represents a decision-making session created by a user or team.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Not Null | Unique identifier for the decision session |
| slug | VARCHAR(64) | Unique, Indexed | URL-friendly shareable identifier |
| title | VARCHAR(200) | Not Null | Core question or decision headline |
| context | TEXT | Nullable | Background constraints (budget, deadline, stack) |
| active_persona | VARCHAR(50) | Default 'balanced' | Current evaluation lens (balanced, speed, cost, scale) |
| status | VARCHAR(20) | Default 'open' | Session state (open or locked) |
| winning_option_id | UUID | Foreign Key -> Option.id, Nullable | Selected final option once locked |
| created_by | VARCHAR(100) | Not Null | Display name or session token of creator |
| created_at | TIMESTAMP | Default NOW() | Creation timestamp |

---

### 2. Option
Represents one of the 2–4 candidate choices inside a Decision.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Not Null | Unique identifier for the option |
| decision_id | UUID | Foreign Key -> Decision.id (ON DELETE CASCADE) | Parent decision session |
| label | VARCHAR(150) | Not Null | Short name of the candidate option |
| description | TEXT | Nullable | Optional details about the option |
| position | INTEGER | Not Null | Display ordering index (0, 1, 2, ...) |

---

### 3. AIAnalysis
Stores structured LLM evaluation outputs for each (Option, persona) pair so switching lenses is fast and auditable.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Not Null | Unique identifier for the analysis record |
| decision_id | UUID | Foreign Key -> Decision.id (ON DELETE CASCADE) | Parent decision session |
| option_id | UUID | Foreign Key -> Option.id (ON DELETE CASCADE) | Evaluated option |
| persona | VARCHAR(50) | Not Null | Evaluation lens used (balanced, speed, cost, scale) |
| pros | JSONB | Not Null | Array of structured advantage strings |
| cons | JSONB | Not Null | Array of structured disadvantage strings |
| risks | JSONB | Not Null | Array of hidden technical/operational risk strings |
| feasibility_score | INTEGER | Check (1 <= score <= 10) | AI-assigned score from 1 to 10 |
| generated_at | TIMESTAMP | Default NOW() | Timestamp when LLM generated the evaluation |

---

### 4. Vote
Tracks participant votes and short rationales for options within an open decision.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Not Null | Unique identifier for the vote |
| decision_id | UUID | Foreign Key -> Decision.id (ON DELETE CASCADE) | Parent decision session |
| option_id | UUID | Foreign Key -> Option.id (ON DELETE CASCADE) | Chosen option |
| voter_name | VARCHAR(80) | Not Null | Name or handle of the team member |
| voter_fingerprint | VARCHAR(128) | Not Null | Session/browser token preventing duplicate votes |
| comment | VARCHAR(280) | Nullable | Short rationale explaining the vote |
| created_at | TIMESTAMP | Default NOW() | Timestamp when vote was cast |

*(Unique Constraint on (decision_id, voter_fingerprint) ensures one active vote per participant per decision.)*
