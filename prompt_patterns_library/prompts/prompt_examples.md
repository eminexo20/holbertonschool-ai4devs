# Prompt Testing Examples

## Example 1 – Refactoring Prompt

**Prompt**:  
You are a Senior Software Engineer. Refactor the provided Python code to improve readability, maintainability, and performance without changing its external behavior.

Language: Python  
Code:
```python
def process_users(users):
    res = []
    for u in users:
        if u['active'] == True:
            if u['age'] > 18:
                res.append(u['name'].upper())
    return res
