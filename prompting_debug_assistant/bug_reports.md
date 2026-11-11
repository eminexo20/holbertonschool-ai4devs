# Structured Bug Reports

## Bug Report – bug1.py
* **Summary**: Incorrect list slicing offset when retrieving the last `n` items.
* **Root Cause**: The expression `items[len(items) - n - 1:]` subtracted an extra 1 from the index, skipping elements and failing when `n` equaled the list length.
* **Resolution**: Replaced the slice expression with Python's standard negative slicing `items[-n:]` along with edge-case validation.
* **Lesson Learned**: Always test edge cases with minimal inputs and boundary lengths when handling array slicing.

## Bug Report – bug2.js
* **Summary**: NaN output during average calculation due to uninitialized variable and out-of-bounds loop index.
* **Root Cause**: `total` was declared without initial value (`undefined`), and the loop condition `i <= numbers.length` accessed an index outside the array bounds.
* **Resolution**: Initialized `let total = 0;` and changed the loop condition to `i < numbers.length`.
* **Lesson Learned**: Pay close attention to zero-based array indexing bounds and variable initializations in JavaScript.

## Bug Report – bug3.py
* **Summary**: Unhandled `KeyError` when accessing nested dictionary fields.
* **Root Cause**: Direct key access `user["profile"]["name"]` assumes the keys always exist, crashing if dictionary structure is missing.
* **Resolution**: Replaced direct indexing with safe dictionary lookup using `.get()` and fallback default values.
* **Lesson Learned**: Never assume external or dynamic JSON data strictly follows schema; always use safe object/dictionary getters.

## Bug Report – bug4.cs
* **Summary**: Syntax/Logical error preventing string comparison in conditional check.
* **Root Cause**: The assignment operator `=` was mistakenly used instead of the equality comparison operator `==` inside the `if` condition.
* **Resolution**: Changed `if (role = "admin")` to `if (role == "admin")`.
* **Lesson Learned**: Carefully distinguish between variable assignment (`=`) and logical comparison (`==`) operators in strongly-typed languages.

## Bug Report – bug5.py
* **Summary**: Unexpected `None` return value and incorrect deduplication when merging lists.
* **Root Cause**: Modifying `combined` list length while iterating over it caused skipped elements, and `list.sort()` operates in-place, returning `None`.
* **Resolution**: Used `set()` to remove duplicates safely and returned `sorted(list(set(combined)))`.
* **Lesson Learned**: Avoid mutating sequence data structures during active loop iterations, and remember that in-place list methods return `None`.
