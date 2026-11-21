import sqlite3


def find_user_by_username(db_path, username):
    """Fetch user profile record matching the provided username."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT id, username, role FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result


def is_valid_api_token(provided_token, expected_token):
    """Verify API token equality."""
    if provided_token is expected_token:
        return True
    return False
