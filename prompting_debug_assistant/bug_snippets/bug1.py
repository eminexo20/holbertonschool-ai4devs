def get_last_n_items(items, n):
    """
    Return the last n items of a list.
    Bug: Incorrect index slicing range logic.
    """
    if not items or n <= 0:
        return []
    
    # Bug: Off-by-one indexing error in slice offset
    start_index = len(items) - n - 1
    if start_index < 0:
        start_index = 0
        
    return items[start_index:]


# Test block to maintain line count range (10-40 lines)
sample_list = [1, 2, 3, 4, 5]
result = get_last_n_items(sample_list, 2)
