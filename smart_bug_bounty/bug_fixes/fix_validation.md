# Fix Validation Report

## bug1.py (`bug_fixes/bug1_fixed.py`)
- **Original Issue**: Off-by-one list slicing (`len(items) - n + 1`), shared mutable default list (`cache=[]`), and unhandled `ZeroDivisionError` on empty input in `calculate_average()`.
- **Fix Applied**: Replaced slice with `items[-n:]` (with `n <= 0` guard), changed default parameter to `cache=None` initialized inside the function, and added an empty-list guard returning `0.0`.
- **Test Results**: All 5 test cases passed (`[30, 40, 50]` returned for `n=3`, full list for `n > len`, `[]` for `n=0`, `30.0` average for `[10..50]`, and `0.0` for `[]`).

## bug2.js (`bug_fixes/bug2_fixed.js`)
- **Original Issue**: Out-of-bounds loop condition (`i <= prices.length`), loose equality (`prices[i] == false`), and function-scoped `var i` closure bug inside `setTimeout`.
- **Fix Applied**: Changed loop condition to `i < prices.length`, added strict numeric validation (`typeof price !== "number" || price <= 0`), and replaced `var` with block-scoped `let`.
- **Test Results**: All 4 test cases passed (`[100, 0, 50]` with `0.2` discount produced `[80, 0, 40]` with no `NaN`, and asynchronous reminder callbacks logged every user email cleanly).

## bug3.java (`bug_fixes/bug3_fixed.java`)
- **Original Issue**: Integer division truncating pass rates below `100%` to `0.0`, unhandled division by zero when `totalStudents == 0`, and `NullPointerException` when `username` is `null`.
- **Fix Applied**: Cast numerator to `(double)` prior to division, tightened denominator guard to `totalStudents <= 0`, and added null-safety + case-insensitive admin check in `normalizeUsername()`.
- **Test Results**: All 4 test cases passed (`computePassRate(15, 20)` returned `75.0`, `totalStudents == 0` threw `IllegalArgumentException`, `normalizeUsername(null)` returned `""`, and `" Admin "` returned `"ADMIN_USER"`).

## bug4.py (`bug_fixes/bug4_fixed.py`)
- **Original Issue**: SQL Injection vulnerability via f-string query formatting, leaked SQLite connections on exception, and identity comparison (`is`) instead of value comparison for API tokens.
- **Fix Applied**: Migrated to parameterized `?` placeholders inside a `with sqlite3.connect(...)` context manager and replaced `is` with constant-time `hmac.compare_digest()`.
- **Test Results**: All 4 test cases passed (SQL injection payload `"' OR '1'='1"` treated strictly as literal parameter with zero unauthorized rows returned, and dynamically constructed matching tokens validated as `True`).

## bug5.js (`bug_fixes/bug5_fixed.js`)
- **Original Issue**: In-place mutation of `item.price` corrupting caller input arrays on repeated invocations and unrounded IEEE-754 floating-point tax/total calculations.
- **Fix Applied**: Used `items.map(...)` with object spread to preserve original items immutably and added `roundCurrency()` for exact two-decimal rounding.
- **Test Results**: All 4 test cases passed (original `item.price` remained `19.99` after summary generation, `subtotal` equaled `39.98`, `tax` at `8%` rounded cleanly to `3.20`, and `total` equaled `43.18`).
