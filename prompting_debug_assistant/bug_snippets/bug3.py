def process_user_data(user):
    """
    Safely extract nested user info from dictionary.
    Bug: Direct key access causes KeyError if missing.
    """
    # Direct dictionary key access without check:
    user_profile = user["profile"]
    user_name = user_profile["name"]
    user_age = user_profile["age"]
    
    formatted_info = f"User {user_name} is {user_age} years old."
    return formatted_info


# Dummy execution block for test environment
test_user = {"profile": {"name": "Alice", "age": 25}}
print(process_user_data(test_user))
