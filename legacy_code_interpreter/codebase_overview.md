# Codebase Overview - osCommerce Online Merchant v2.3.4 (Legacy E-Commerce Platform)

## Project Summary
osCommerce Online Merchant v2.3.4 is an open-source PHP/MySQL e-commerce platform widely deployed in small-to-medium online stores during the late 2000s and early 2010s. The system handles product catalogs, shopping carts, checkout workflows, tax calculations, and order management through a tightly coupled server-rendered architecture.

## Age
- **First Release:** March 2000 (v2.2 milestone in 2003)
- **Target Version Release:** June 2014 (v2.3.4)
- **Last Official Maintenance Update:** August 2017 (community security patch v2.3.4.1; core architecture effectively frozen since 2014)

## Size
- **Total Lines of Code (LOC):** ~68,400 LOC across 612 files
  - **PHP:** ~54,200 LOC (79.2%)
  - **HTML / Inline Templates:** ~8,900 LOC (13.0%)
  - **JavaScript (jQuery 1.11 / legacy inline scripts):** ~3,100 LOC (4.5%)
  - **SQL Schema & Seed Scripts:** ~2,200 LOC (3.3%)

## Main Dependencies & Runtime Stack
- **Language Runtime:** PHP 5.3 – 5.6 (incompatible with PHP 8.x due to removed `mysql_*` functions, `create_function()`, and legacy constructor syntax)
- **Database:** MySQL 5.1 / 5.5 (MyISAM storage engine used by default without foreign key constraints or transactional rollback support)
- **Frontend Libraries:** jQuery 1.11.1, jQuery UI 1.10.4, 960 Grid System CSS
- **Server Environment:** Apache HTTP Server 2.2+ with `.htaccess` URL rewrites and `register_globals` compatibility shims
- **External Integrations:** Legacy PayPal Standard, Authorize.Net AIM, and flat-rate shipping modules using procedural cURL wrappers

## Architecture & Key Modules
- `catalog/includes/application_top.php`: Global bootstrap script initializing sessions, database connections, currency/language state, and shopping cart objects via global variables.
- `catalog/includes/classes/shopping_cart.php`: Stateful session-backed cart calculation engine handling product attributes, quantities, and totals.
- `catalog/includes/classes/order.php`: Order aggregation class coupling database queries directly with checkout session state.
- `catalog/checkout_process.php`: Procedural transaction script executing inventory updates, payment calls, and email notifications without database transactions.
- `admin/`: Separate administrative backend duplicating core business logic and database queries rather than sharing a common service layer.

## Known Issues & Pain Points
- **Zero Automated Test Coverage:** No unit, integration, or end-to-end test suite exists; all regression verification relies on manual checkout testing.
- **SQL Injection & Security Vulnerabilities:** Heavy reliance on string concatenation in raw SQL queries (`tep_db_query()`) and legacy salted MD5 password hashing (`tep_encrypt_password()`).
- **Tight Coupling & Global State:** Extensive use of `global` variables (`$currencies`, `$cart`, `$customer_id`, `$languages_id`) makes isolated refactoring or dependency injection nearly impossible.
- **Mixed Presentation and Business Logic:** HTML markup, SQL queries, and payment processing logic are interleaved inside single procedural scripts (e.g., `checkout_process.php`, `product_info.php`).
- **Lack of Transactional Integrity:** Order creation, stock deduction, and payment confirmation run as sequential auto-committed MyISAM queries, risking partial state corruption on failure.
- **Duplicated Admin/Catalog Codebase:** Core classes (`order`, `currencies`, `language`) are duplicated between `catalog/includes/` and `admin/includes/`, causing drift when bug fixes are applied.
