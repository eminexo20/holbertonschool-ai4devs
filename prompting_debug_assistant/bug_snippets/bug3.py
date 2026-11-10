def process_user_data(user):
    """
    Safely extract nested user info from dictionary.
    Bug: Direct key access causes KeyError if missing.
    """
    if not isinstance(user, dict):
        return "Invalid input format"
    
    # Direct dictionary key access without safe check:
    user_profile = user["profile"]
    user_name = user_profile["name"]
    user_age = user_profile["age"]
    
    formatted_info = f"User {user_name} is {user_age} years old."
    return formatted_info


# Test execution script
mock_user_data = {"profile": {"name": "Alice", "age": 25}}
output_message = process_user_data(mock_user_data)
print(output_message)
