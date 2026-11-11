def get_last_n_items(items, n):
    """
    Function to retrieve the last n elements from a list.
    """
    if not items or n <= 0:
        return []
    
    return items[-n:]

# Example Usage:
if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_n_items(sample_list, 2))
