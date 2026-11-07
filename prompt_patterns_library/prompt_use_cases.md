# Prompt Use Cases

## 1. Code Quality
- **Refactoring**
  - **Goal**: Improve code readability, maintainability, and performance.
  - **Input**: Source code function or module in [LANGUAGE].
  - **Expected output**: Refactored code block along with a concise explanation of optimizations.
- **Style Enforcement**
  - **Goal**: Enforce organization-specific naming conventions, formatting, and linting rules.
  - **Input**: Raw unformatted code block.
  - **Expected output**: Clean code rewritten according to specified style guidelines.
- **Architecture & Design Review**
  - **Goal**: Evaluate implementation against design patterns and SOLID principles.
  - **Input**: Class structure or module design.
  - **Expected output**: Critique of architectural flaws and recommendations for improvement.

## 2. Debugging & Error Handling
- **Bug Diagnosis**
  - **Goal**: Identify root causes of runtime exceptions or logic errors.
  - **Input**: Error stack trace, failing input data, and buggy code snippet.
  - **Expected output**: Detailed root cause analysis and a working fix.
- **Security Vulnerability Patching**
  - **Goal**: Detect and patch security risks (e.g., SQL injection, XSS, insecure auth).
  - **Input**: Potentially vulnerable code snippet.
  - **Expected output**: Hardened code implementation with security rationale.
- **Edge Case Analysis**
  - **Goal**: Uncover unhandled boundary conditions and edge cases in business logic.
  - **Input**: Function implementation and target parameters.
  - **Expected output**: List of potential failure points and defensive coding updates.

## 3. Documentation & Knowledge Sharing
- **API Documentation Generation**
  - **Goal**: Create structured API docs, parameter tables, and request/response schemas.
  - **Input**: Controller methods, API routes, or data models.
  - **Expected output**: Markdown or OpenAPI/Swagger-compliant endpoint documentation.
- **Codebase Explanation & Onboarding**
  - **Goal**: Summarize legacy or complex algorithms for fast developer onboarding.
  - **Input**: Complex algorithm or multi-file directory structure.
  - **Expected output**: High-level architectural overview and functional breakdown.
- **Changelog & Release Notes**
  - **Goal**: Synthesize commit histories into human-readable release notes.
  - **Input**: Git commit logs or diff summary.
  - **Expected output**: Categorized release notes (Features, Bug Fixes, Breaking Changes).

## 4. Testing & Test Automation
- **Unit Test Generation**
  - **Goal**: Automatically generate comprehensive unit tests covering edge cases.
  - **Input**: Target function/class + choice of testing framework (e.g., Jest, PyTest, JUnit).
  - **Expected output**: Complete test suite with mocks and assertions.
- **Integration Test Scenarios**
  - **Goal**: Design multi-component integration test workflows.
  - **Input**: System architecture overview and database/service dependency details.
  - **Expected output**: Step-by-step integration test plan and boilerplate test scripts.
- **End-to-End Test Automation**
  - **Goal**: Create automated UI and workflow validation scripts.
  - **Input**: User story descriptions and DOM selectors.
  - **Expected output**: Cypress or Playwright test script validating user flows.
