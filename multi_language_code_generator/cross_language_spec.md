
# Cross-Language Specification - Server Log Analyzer

## Algorithm Description
The Server Log Analyzer parses raw web server access log lines (Common/Combined Log Format), filters out malformed entries, and computes aggregate traffic and reliability statistics across all valid requests.

### Processing Rules
1. Split input text into individual lines and skip empty or whitespace-only lines.
2. Parse each line using the structured format: IP - - [timestamp] "METHOD PATH PROTOCOL" STATUS_CODE BYTES.
3. Validate that STATUS_CODE is a valid 3-digit integer (100-599) and BYTES is a non-negative integer (treat "-" as 0). Lines failing validation are counted under malformed_entries and excluded from request metrics.
4. Compute across all valid lines:
   - total_requests: Total count of valid parsed log lines.
   - unique_visitors: Number of distinct client IP addresses.
   - error_rate: Percentage of valid requests with HTTP status code >= 400, rounded to 2 decimal places (0.0 if total_requests == 0).
   - total_bytes: Sum of response bytes across all valid requests.
   - top_endpoint: Most frequently requested path (tie-broken lexicographically, or null if total_requests == 0).
   - malformed_entries: Count of non-empty lines that failed format validation.

## Input Format
- Type: Multi-line UTF-8 string representing raw server access logs.
- Example Line: 192.168.1.10 - - [15/Nov/2026:10:15:32 +0000] "GET /api/users HTTP/1.1" 200 1024

## Output Format
- Type: JSON object with deterministic keys and types:
  {"total_requests": 4, "unique_visitors": 3, "error_rate": 25.0, "total_bytes": 3584, "top_endpoint": "/api/users", "malformed_entries": 0}

## Edge Cases
1. Empty Input: Must return 0 for numeric counts, 0.0 for error_rate, and null for top_endpoint without division-by-zero errors.
2. Malformed Entries: Corrupted lines (missing quotes, invalid status codes like ABC, negative bytes) must increment malformed_entries without crashing.
3. 100% Error Traffic: When all valid requests have status codes 4xx or 5xx, error_rate must equal 100.0.
4. Dash Byte Size: Standard server logs often emit "-" when response body size is 0; must be parsed as 0 bytes.
5. Endpoint Tie-Breaking: If two endpoints share the highest request count, return the lexicographically smaller path (e.g., "/about" before "/home").

## Test Cases

### Test Case 1: Empty Log (log_empty.txt)
- Input: ""
- Expected Output: {"total_requests": 0, "unique_visitors": 0, "error_rate": 0.0, "total_bytes": 0, "top_endpoint": null, "malformed_entries": 0}

### Test Case 2: Standard Mixed Traffic (log_standard.txt)
- Input:
  10.0.0.1 - - [15/Nov/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 2048
  10.0.0.2 - - [15/Nov/2026:12:00:02 +0000] "POST /api/login HTTP/1.1" 401 512
  10.0.0.1 - - [15/Nov/2026:12:00:03 +0000] "GET /index.html HTTP/1.1" 200 2048
  10.0.0.3 - - [15/Nov/2026:12:00:04 +0000] "GET /dashboard HTTP/1.1" 500 256
- Expected Output: {"total_requests": 4, "unique_visitors": 3, "error_rate": 50.0, "total_bytes": 4864, "top_endpoint": "/index.html", "malformed_entries": 0}

### Test Case 3: Malformed Lines Mixed with Valid Logs (log_malformed.txt)
- Input:
  CORRUPTED_LINE_WITHOUT_STRUCTURE
  192.168.0.5 - - [15/Nov/2026:12:05:00 +0000] "GET /health HTTP/1.1" 200 64
  192.168.0.6 - - [15/Nov/2026:12:05:01 +0000] "GET /broken HTTP/1.1" NOT_A_CODE 100
- Expected Output: {"total_requests": 1, "unique_visitors": 1, "error_rate": 0.0, "total_bytes": 64, "top_endpoint": "/health", "malformed_entries": 2}

### Test Case 4: Dash Byte Size & 100% Errors (log_errors.txt)
- Input:
  172.16.0.1 - - [15/Nov/2026:12:10:00 +0000] "DELETE /api/item/9 HTTP/1.1" 404 -
  172.16.0.1 - - [15/Nov/2026:12:10:05 +0000] "GET /api/secret HTTP/1.1" 403 128
- Expected Output: {"total_requests": 2, "unique_visitors": 1, "error_rate": 100.0, "total_bytes": 128, "top_endpoint": "/api/item/9", "malformed_entries": 0}

### Test Case 5: Endpoint Tie-Breaking (log_tie.txt)
- Input:
  10.1.1.1 - - [15/Nov/2026:12:15:00 +0000] "GET /zebra HTTP/1.1" 200 100
  10.1.1.2 - - [15/Nov/2026:12:15:01 +0000] "GET /alpha HTTP/1.1" 200 100
- Expected Output: {"total_requests": 2, "unique_visitors": 2, "error_rate": 0.0, "total_bytes": 200, "top_endpoint": "/alpha", "malformed_entries": 0}
