# Team Ideation

## Brainstormed Ideas
1. **AI Study & Exam Flashcard Generator** – Converts lecture notes into spaced-repetition flashcards and mini-quizzes.
2. **Smart Campus Commute & Event Radar** – Real-time student transit tracker and campus meetup notifier.
3. **AI Decision Helper & Sprint Prioritizer** ✅ *(Chosen)* – Structured decision-making assistant that evaluates complex technical or everyday choices with weighted pros, cons, risk scores, and team voting.

## Problem Statement
Developers, students, and small product teams frequently face decision fatigue when choosing between tech stacks, feature priorities, or daily action plans under tight deadlines. Without a structured framework, discussions drag on and key trade-offs get overlooked. An AI-powered decision helper transforms messy options into clear, weighted pros/cons matrices and enables fast, transparent team consensus.

## MVP Features
- **Decision Prompt & Options Input**: Users enter a decision question along with 2–4 candidate options and optional constraints (budget, timeline, skill level).
- **AI Weighted Pros/Cons & Risk Analysis**: Generates structured advantages, disadvantages, hidden risks, and a 1–10 feasibility score for each option.
- **Scenario & Persona Toggle**: Re-evaluates the decision from different perspectives (e.g., *Speed-to-MVP*, *Cost-Efficiency*, *Scalability*).
- **Collaborative Team Voting & Tie-Breaker**: Shareable decision room where team members cast votes and add short comments before locking the final choice.
- **Markdown / JSON Export**: One-click export of the final decision summary for project documentation or GitHub issues.

## Team Roles

| Member | Role | Core Responsibilities |
|--------|------|-----------------------|
| Emin (Lead) | Frontend & UI Developer | React/Tailwind interface, responsive decision cards, interactive voting UI, and state management |
| Member 2 (TBD) | Backend & AI Prompt Strategist | REST API endpoints, LLM structured-output prompts, rate limiting, and persistence |
| Member 3 (TBD) | UI/UX & Product Designer | User flow wireframes, accessibility, visual hierarchy, and demo presentation assets |
| Member 4 (TBD) | QA, DevOps & Testing Lead | Automated unit/API tests (`pytest`/`Jest`), CI/CD pipeline, and live Vercel/Render deployment |
