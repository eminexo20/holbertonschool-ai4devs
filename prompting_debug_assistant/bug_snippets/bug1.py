# Bug Snippet 1 - Python List Slicing Issue
# Intended behavior: Return the last n items of a given list.

def get_last_n_items(items, n):
    """
    Function to retrieve the last n elements from a list.
    Fails when n equals the total length of the list.
    """
    if not items:
        return []
    
    # BUG: Incorrect negative slice offset indexing
    return items[len(items) - n - 1:]

# Example Usage:
sample_list = [10, 20, 30, 40, 50]
print(get_last_n_items(sample_list, 2))
