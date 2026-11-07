# Software Engineering Prompt Engineering Use Cases

## 1. Code Refactoring & Optimization
* **User Persona**: Senior Software Engineer
* **Task Description**: Refactor the provided code block in a specified language to improve readability, maintainability, and performance without changing its core functional behavior.
* **Input Parameters**: Source code snippet, target programming language.
* **Expected Output**: Clean, optimized code with inline comments explaining key performance and structural enhancements.

## 2. Style Enforcement & Standards Compliance
* **User Persona**: Code Quality & Standards Auditor
* **Task Description**: Reformat and rewrite the provided code block to strictly comply with target organization naming conventions, formatting rules, and code linting guidelines.
* **Input Parameters**: Unformatted source code, target style guide specification.
* **Expected Output**: Clean code rewritten according to specified style guidelines along with a summary of corrected formatting violations.

## 3. Architecture & Design Pattern Review
* **User Persona**: Lead Principal Architect
* **Task Description**: Evaluate the given class structure or software component design against established SOLID principles and software design patterns.
* **Input Parameters**: Architecture diagram description or multi-class codebase sample.
* **Expected Output**: Critique of architectural flaws, trade-off analysis, and concrete recommendations for structural improvement.

## 4. Bug Diagnosis & Root Cause Analysis
* **User Persona**: Senior Debugging Specialist
* **Task Description**: Analyze the provided error stack trace, failing input data, and buggy code snippet to determine the root cause of the failure and provide a resolution.
* **Input Parameters**: Stack trace, failing function code, runtime input.
* **Expected Output**: Detailed root cause analysis and a working fix with defensive programming adjustments.

## 5. Security Vulnerability Patching
* **User Persona**: Application Security Engineer
* **Task Description**: Inspect the given source code snippet for security vulnerabilities (such as SQL injection, XSS, or broken authentication) and patch them safely.
* **Input Parameters**: Vulnerable code block, vulnerability alert details.
* **Expected Output**: Hardened code implementation accompanied by a detailed security rationale.

## 6. Edge Case & Failure Mode Identification
* **User Persona**: QA Automation Specialist & Resilience Tester
* **Task Description**: Analyze the provided function implementation and input boundaries to identify unhandled edge cases and potential failure modes.
* **Input Parameters**: Function definition, business logic parameters.
* **Expected Output**: List of potential failure points, boundary condition scenarios, and defensive coding updates.

## 7. API Documentation Generation
* **User Persona**: Technical Writer & API Architect
* **Task Description**: Generate comprehensive, structured technical documentation for the given API endpoints, routes, or controller methods.
* **Input Parameters**: Controller code, API route handler.
* **Expected Output**: Markdown or OpenAPI/Swagger-compliant endpoint documentation including parameter tables and request/response schemas.

## 8. Codebase Explanation & Onboarding Walkthrough
* **User Persona**: Engineering Mentor
* **Task Description**: Provide a clear, structured breakdown and walkthrough of a complex algorithm or codebase directory to accelerate developer onboarding.
* **Input Parameters**: Complex algorithm source file, directory layout.
* **Expected Output**: High-level architectural overview, component interaction breakdown, and functional summary.

## 9. Automated Changelog & Release Notes Generation
* **User Persona**: Release Manager
* **Task Description**: Synthesize raw Git commit logs or diff summaries into a clear, professional changelog formatted for release distribution.
* **Input Parameters**: Raw Git commit history, pull request titles.
* **Expected Output**: Categorized release notes organized into Features, Bug Fixes, Security Updates, and Breaking Changes.

## 10. Unit Test Suite Generation
* **User Persona**: Test Automation Engineer
* **Task Description**: Automatically generate comprehensive unit tests covering happy paths and edge cases for the given target code using the specified testing framework.
* **Input Parameters**: Target code module, preferred test framework (e.g., PyTest, Jest).
* **Expected Output**: Complete test suite with mocks, stubs, assertions, and high line coverage.

## 11. Integration Test Scenario Design
* **User Persona**: Systems Integration Engineer
* **Task Description**: Design multi-component integration test workflows to validate dependencies between application modules, APIs, and databases.
* **Input Parameters**: System architecture specification, database model relationships.
* **Expected Output**: Step-by-step integration test plan accompanied by boilerplate test scripts.

## 12. End-to-End User Flow Test Automation
* **User Persona**: E2E Automation Lead
* **Task Description**: Create automated end-to-end user workflow test scripts based on provided user story flows and UI selectors.
* **Input Parameters**: User story acceptance criteria, UI element selectors.
* **Expected Output**: Robust Cypress or Playwright test script validating entire end-to-end user journeys.
