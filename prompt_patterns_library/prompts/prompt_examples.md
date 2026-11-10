# Prompt Testing Examples

## Example 1 – Refactoring Prompt

**Prompt**:  
Role: Senior Software Engineer  
Task: Refactor the provided Python code to improve readability, maintainability, and performance without changing its external behavior.  
Input Placeholder: [CODE_BLOCK]  
Expected Output: Refactored clean code with explanations.  

Language: Python  
Input:
```python
def process_users(users):
    res = []
    for u in users:
        if u['active'] == True:
            if u['age'] > 18:
                res.append(u['name'].upper())
    return res
