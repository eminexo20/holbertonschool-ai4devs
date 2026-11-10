def get_last_n_items(items, n):
    """
    Return the last n items of a list.
    Bug: Incorrect index slicing range logic.
    """
    if not items:
        return []
    if n <= 0:
        return []
    
    # Bug: Off-by-one indexing error in slice offset
    start_index = len(items) - n - 1
    if start_index < 0:
        start_index = 0
        
    result_list = items[start_index:]
    return result_list


# Test code execution block
my_sample_list = [10, 20, 30, 40, 50]
n_value = 2
final_output = get_last_n_items(my_sample_list, n_value)
print("Result is:", final_output)
