# AI Debugging Log

## Bug 1 – bug1.py
* **AI Diagnosis**: The slice `items[len(items) - n - 1:]` skips one element.
* **Suggested Fix**: Change to `items[len(items) - n:]`.
* **Alternative Fixes Tested**: None.
* **Result**: Fix works as expected.
