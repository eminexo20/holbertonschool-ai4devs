# Fix Validation Log

## Bug 1 – bug1_fixed.py
* **Input**: `items = [10, 20, 30, 40, 50]`, `n = 2`
* **Expected Output**: `[40, 50]`
* **Actual Output**: `[40, 50]` ✅
* **Validation Outcome**: Pass. The negative slice offset operates correctly for all valid values of n.

## Bug 2 – bug2_fixed.js
* **Input**: `data = [10, 20, 30, 40]`
* **Expected Output**: `25`
* **Actual Output**: `25` ✅
* **Validation Outcome**: Pass. Loop index bounds fixed and total initialized properly to zero.

## Bug 3 – bug3_fixed.py
* **Input**: `user_dict = {"id": 1}`
* **Expected Output**: `User Unknown is N/A years old.`
* **Actual Output**: `User Unknown is N/A years old.` ✅
* **Validation Outcome**: Pass. Dictionary access is now safe against missing nested keys.

## Bug 4 – bug4_fixed.cs
* **Input**: `role = "admin"`
* **Expected Output**: `Access Granted`
* **Actual Output**: `Access Granted` ✅
* **Validation Outcome**: Pass. Replaced assignment operator with equality comparison operator.

## Bug 5 – bug5_fixed.py
* **Input**: `list1 = [3, 1, 2]`, `list2 = [2, 4, 1]`
* **Expected Output**: `[1, 2, 3, 4]`
* **Actual Output**: `[1, 2, 3, 4]` ✅
* **Validation Outcome**: Pass. Deduplication and sorting now work correctly without mutating active loops.
