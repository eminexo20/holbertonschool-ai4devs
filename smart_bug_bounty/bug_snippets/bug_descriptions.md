# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the exact last `n` elements of a list without shared state across calls, and safely compute the arithmetic mean of a numeric list (returning `0` for empty lists).
- **Current Issue**: Off-by-one slicing (`len(items) - n + 1` drops the first requested element), mutable default list argument (`cache=[]`) persists across invocations, and `calculate_average([])` raises a `ZeroDivisionError`.

## bug2.js
- **Intended Behavior**: Apply a percentage discount to each item in a price array and asynchronously log reminder emails for each user in a list.
- **Current Issue**: Loop boundary `i <= prices.length` reads `undefined` on the final iteration (producing `NaN`), loose equality `== false` treats `0` as falsy, and `var i` inside `setTimeout` causes a closure bug throwing a `TypeError` (`users[users.length]` is `undefined`).

## bug3.java
- **Intended Behavior**: Calculate the pass percentage as a floating-point value between `0.0` and `100.0` and safely normalize usernames without crashing on `null` input.
- **Current Issue**: Integer division `(passedStudents / totalStudents)` truncates fractional results to `0.0` whenever `passedStudents < totalStudents`, `totalStudents == 0` causes an `ArithmeticException`, and `username.trim()` throws a `NullPointerException` if `username` is `null`.

## bug4.py
- **Intended Behavior**: Safely query a user record from SQLite by username and accurately compare two dynamically created API token strings.
- **Current Issue**: Direct string interpolation (`f"... '{username}'"`) introduces a critical SQL Injection vulnerability and leaks database connections on error, while `is` checks object identity instead of string value equality (`==` / `hmac.compare_digest`).

## bug5.js
- **Intended Behavior**: Compute cart `subtotal`, `tax`, and `total` rounded to two decimal places without mutating the caller's original `items` array.
- **Current Issue**: Mutates `item.price` in place (`item.price = item.price * item.quantity`), corrupting input objects on repeated calls, and leaves IEEE-754 floating-point precision artifacts unrounded (e.g., `19.99 * 0.08`).
