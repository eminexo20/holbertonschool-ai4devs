# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error / Slice indexing mistake.
**Notes**: Incorrect negative slice offset indexing causes index error when n == len(items).

## Bug 2 – bug2.js
**Intended Behavior**: Compute the average value of an array of numbers.
**Issue Type**: Uninitialized variable and off-by-one loop boundary condition.
**Notes**: Variable total is undefined resulting in NaN, and loop condition i <= numbers.length accesses array index out-of-bounds.

## Bug 3 – bug3.py
**Intended Behavior**: Safely extract and format user profile details from a dictionary.
**Issue Type**: Runtime exception (KeyError / TypeError).
**Notes**: Direct dictionary key access raises KeyError if nested keys are missing or user is None.

## Bug 4 – bug4.cs
**Intended Behavior**: Check user role permissions and return status string.
**Issue Type**: Compilation failure / Assignment inside conditional.
**Notes**: Single equals assignment operator used inside if statement instead of equality operator.

## Bug 5 – bug5.py
**Intended Behavior**: Merge two lists, remove duplicates, and return a sorted list.
**Issue Type**: In-place mutation returning None and modifying list during iteration.
**Notes**: list.sort() mutates in-place and returns None, and modifying a list while iterating leads to skipped elements.
