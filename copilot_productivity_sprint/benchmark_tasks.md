# Benchmark Coding Tasks

## Task 1 - CRUD Endpoint (User Registration)
**Requirements**: Implement a `POST /users` REST API endpoint with input validation and in-memory user storage.
**Inputs**: JSON object `{ "name": string, "email": string }`
**Outputs**: JSON object of the created user with a generated `id` and `createdAt` timestamp.
**Acceptance Criteria**:
- Returns HTTP `201 Created` with the stored user object on valid input.
- Returns HTTP `400 Bad Request` if `name` is empty or `email` format is invalid.
- Returns HTTP `409 Conflict` if the email already exists.

## Task 2 - CSV Expense Log Aggregator
**Requirements**: Write a function `summarizeExpenses(csvString)` that parses multi-line CSV expense records (`date,category,amount`) and calculates total spending per category.
**Inputs**: A multi-line CSV string with header row `date,category,amount`.
**Outputs**: An object/dictionary mapping each category name to its rounded total amount (e.g., `{ Food: 45.5, Transport: 12.0 }`).
**Acceptance Criteria**:
- Accurately sums numeric amounts grouped by category.
- Ignores empty lines and trims extra whitespace around fields.
- Throws a descriptive error if an amount is not a valid positive number.

## Task 3 - Rate Limiter Middleware
**Requirements**: Implement a sliding-window rate limiter function `createRateLimiter(maxRequests, windowMs)` that tracks requests per client IP.
**Inputs**: `clientIp` (string) and current timestamp `now` (number in milliseconds).
**Outputs**: Boolean (`true` if the request is allowed, `false` if the rate limit is exceeded).
**Acceptance Criteria**:
- Allows up to `maxRequests` within any `windowMs` millisecond interval per IP.
- Blocks subsequent requests once the limit is reached until older timestamps expire.
- Tracks different client IPs independently without cross-interference.
