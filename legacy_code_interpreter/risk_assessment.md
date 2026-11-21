# Risk Assessment - osCommerce Online Merchant v2.3.4

This document identifies, categorizes, and prioritizes the primary security, architectural, and operational risks discovered in the **osCommerce v2.3.4** legacy PHP/MySQL codebase.

## Risk Prioritization Matrix

| Risk | Severity | Category | Affected Components | Notes & Remediation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| SQL Injection via raw string concatenation | High | Security | `tep_db_query()`, `checkout_process.php`, `product_info.php` | User-supplied query parameters and IDs are concatenated directly into SQL strings without prepared statements. Migrate all database access to PDO with parameterized queries. |
| Weak password hashing (MD5 with 2-char salt) | High | Security | `catalog/includes/functions/password_funcs.php` | `tep_encrypt_password()` uses broken MD5 hashing and a 2-character hex salt (only 256 combinations), making passwords trivial to crack via GPU brute-force. Upgrade to `password_hash()` (bcrypt/Argon2id) with lazy migration on login. |
| Removed PHP 5.x APIs & runtime incompatibility | High | Compatibility | `shopping_cart.php`, `application_top.php` | Relies on `mysql_*` extensions, `each()`, `create_function()`, and `session_register()` emulators removed in PHP 7/8, preventing security upgrades of the underlying server runtime. Refactor to PHP 8.2+ compatible syntax and `mysqli`/`PDO`. |
| Lack of ACID transactions & stock race conditions | High | Data Integrity | `catalog/checkout_process.php`, MyISAM tables | Order creation and inventory deduction execute as auto-committed MyISAM queries without row locks, risking negative inventory and partial orders on failure. Convert tables to InnoDB and wrap checkout in atomic transactions. |
| Hardcoded database credentials in config files | High | Security | `catalog/includes/configure.php`, `admin/includes/configure.php` | Database host, username, and password are stored as plain-text PHP constants inside web-directory files, risking full database exposure if misconfigured or committed to VCS. Move secrets to environment variables (`.env`). |
| Zero automated test coverage | Medium | Maintainability | Entire codebase (`catalog/` and `admin/`) | No unit, integration, or end-to-end tests exist; every bug fix or refactoring step risks silent checkout or tax-calculation regressions. Build characterization tests around cart, tax, and order flows before refactoring. |
| Tight coupling & pervasive global state | Medium | Architecture | `application_top.php`, `shopping_cart.php`, `order.php` | Heavy reliance on `global` variables (`$cart`, `$currencies`, `$customer_id`) and mixed HTML/SQL/business logic blocks isolated unit testing and modular replacement. Extract domain services and introduce dependency injection. |
| Duplicated business logic between Catalog and Admin | Medium | Maintainability | `catalog/includes/classes/` vs `admin/includes/classes/` | Core classes (`order`, `currencies`, `language`) are copy-pasted across storefront and admin directories, causing logic drift when patches are applied to only one side. Consolidate into a shared `src/` composer package. |
| N+1 database query loops in cart calculation | Medium | Performance | `shopping_cart::calculate()` | Executes two separate SQL queries (`TABLE_PRODUCTS` and `TABLE_SPECIALS`) per cart item on every page load, degrading latency as cart size grows. Batch fetch items using `WHERE products_id IN (...)` with a `LEFT JOIN`. |
| Missing structured application & error logging | Low | Observability | Payment & checkout workflows (`checkout_process.php`) | Failed payment gateway responses and database errors are either suppressed or printed raw to users without centralized structured logs, slowing incident diagnosis. Implement PSR-3 logging (Monolog) with masked sensitive fields. |

## Summary of Findings
- **High Severity (5 risks):** Immediate security, data-corruption, and runtime-end-of-life blockers (`SQL Injection`, `MD5 passwords`, `PHP 5.x APIs`, `Non-transactional MyISAM stock updates`, and `Hardcoded credentials`) must be remediated first.
- **Medium Severity (4 risks):** Structural technical debt (`Zero test coverage`, `Global state coupling`, `Catalog/Admin duplication`, and `N+1 queries`) increases maintenance cost and slows feature delivery.
- **Low Severity (1 risk):** `Lack of structured logging` reduces operational visibility during production incidents.
