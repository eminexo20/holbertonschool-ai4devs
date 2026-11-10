# Prompt Testing Examples

## Example 1 – Refactoring Prompt

**Prompt**:  
Role: Senior Software Engineer  
Task: Refactor the provided Python code to improve readability, maintainability, and performance without changing its external behavior.  
Input Placeholder: [CODE_BLOCK]  
Expected Output Format:  
- Refactored code snippet  
- List of optimizations made  
- Explanation of changes  

Language: Python  
Input:
def process_users(users):
    res = []
    for u in users:
        if u['active'] == True:
            if u['age'] > 18:
                res.append(u['name'].upper())
    return res

**AI Output**:
from typing import List, Dict, Any

def get_active_adult_user_names(users: List[Dict[str, Any]]) -> List[str]:
    """Extract and uppercase names of active users aged above 18."""
    return [
        user['name'].upper() 
        for user in users 
        if user.get('active') and user.get('age', 0) > 18
    ]

**Feedback**: Excellent output. List comprehension improved readability, function naming is clearer, type hinting was added, and defensive dictionary `.get()` calls prevent potential key errors.

---

## Example 2 – Bug Fixing Prompt

**Prompt**:  
Role: Senior Debugging Expert & QA Engineer  
Task: Identify the root cause of the error or bug in the provided JavaScript code snippet and provide a corrected version.  
Input Placeholder: [CODE_BLOCK]  
Expected Output Format:  
- Root cause explanation  
- Corrected code snippet  
- Prevention recommendations  

Language: JavaScript  
Input:
function calculateAverage(numbers) {
    let total;
    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }
    return total / numbers.length;
}

**AI Output**:
function calculateAverage(numbers) {
    if (!numbers || numbers.length === 0) return 0;
    
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total / numbers.length;
}

**Feedback**: Successfully identified two major bugs: off-by-one loop index causing out-of-bounds access, and uninitialized total variable resulting in NaN.

---

## Example 3 – Unit Testing Prompt

**Prompt**:  
Role: Lead Test Automation Engineer  
Task: Generate comprehensive unit tests for the given code snippet using pytest, covering happy paths, edge cases, and failure scenarios.  
Input Placeholder: [CODE_BLOCK]  
Expected Output Format:  
- Complete test suite code  
- List of covered edge cases  

Language: Python  
Input:
def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

**AI Output**:
import pytest

def test_divide_numbers_success():
    assert divide_numbers(10, 2) == 5.0
    assert divide_numbers(-6, 3) == -2.0

def test_divide_numbers_float():
    assert divide_numbers(5, 2) == 2.5

def test_divide_numbers_zero_division():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide_numbers(10, 0)

**Feedback**: Great result. The generated tests use standard pytest assertions and correctly test for raised exceptions.

---

## Example 4 – Security Audit Prompt

**Prompt**:  
Role: Cybersecurity Specialist  
Task: Analyze the provided code for security vulnerabilities and injection vectors.  
Input Placeholder: [CODE_BLOCK]  
Expected Output Format:  
- Identified vulnerabilities  
- Remediated secure code  
- Mitigation best practices  

Language: Python (Flask)  
Input:
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

**AI Output**:
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()

**Feedback**: The security audit accurately flagged the SQL Injection vulnerability and provided a parameterized query solution.

---

## Example 5 – Performance Optimization Prompt

**Prompt**:  
Role: Performance Tuning Engineer  
Task: Analyze the given code snippet for performance bottlenecks and optimize Big-O complexity.  
Input Placeholder: [CODE_BLOCK]  
Expected Output Format:  
- Time and Space Complexity analysis  
- Optimized code snippet  
- Performance comparison  

Language: Python  
Input:
def find_duplicates(nums):
    dups = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in dups:
                dups.append(nums[i])
    return dups

**AI Output**:
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

**Feedback**: Exceptional optimization. Reduced time complexity from O(n^2) down to linear O(n) time using Hash Sets.
