# Bug Snippet 3 - Python Nested Dictionary Access
# Intended behavior: Safely extract user profile information.

def process_user_data(user):
    """
    Extracts name and age from nested dictionary structure.
    Raises KeyError or TypeError if dictionary keys are missing.
    """
    # BUG: Unsafe direct key access raises KeyError if nested keys missing
    name = user["profile"]["name"]
    age = user["profile"]["age"]
    
    result_string = f"User {name} is {age} years old."
    return result_string

# Example Usage:
user_dict = {"id": 1}
print(process_user_data(user_dict))
