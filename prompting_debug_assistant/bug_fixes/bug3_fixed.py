def process_user_data(user):
    """
    Extracts name and age from nested dictionary structure safely.
    """
    profile = user.get("profile", {})
    name = profile.get("name", "Unknown")
    age = profile.get("age", "N/A")
    
    result_string = f"User {name} is {age} years old."
    return result_string

# Example Usage:
if __name__ == "__main__":
    user_dict = {"id": 1}
    print(process_user_data(user_dict))
