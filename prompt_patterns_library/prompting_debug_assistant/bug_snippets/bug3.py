def process_user_data(user):
    """Access nested data safely."""
    name = user["profile"]["name"]
    age = user["profile"]["age"]
    return f"User {name} is {age} years old."
