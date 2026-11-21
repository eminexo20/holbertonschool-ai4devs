import hmac
import sqlite3


def find_user_by_username(db_path, username):
    """Safely fetch a user profile record using parameterized SQL queries."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, username, role FROM users WHERE username = ?",
            (username,),
        )
        return cursor.fetchone()


def is_valid_api_token(provided_token, expected_token):
    """Verify API token equality using constant-time string comparison."""
    if not isinstance(provided_token, str) or not isinstance(expected_token, str):
        return False
    return hmac.compare_digest(provided_token, expected_token)


if __name__ == "__main__":
    t1 = "".join(["secret", "_token_123"])
    t2 = "secret_token_123"
    assert is_valid_api_token(t1, t2) is True
    assert is_valid_api_token("wrong", t2) is False
    print("bug4_fixed.py: All assertions passed.")
