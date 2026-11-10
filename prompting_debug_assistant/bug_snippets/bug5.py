def merge_and_sort_lists(list1, list2):
    """
    Merge two lists, remove duplicate items, and sort them.
    Bug: Mutates list during loop and returns list.sort() (None).
    """
    combined = list1 + list2
    
    # Bug: Modifying array length during iteration
    for item in combined:
        if combined.count(item) > 1:
            combined.remove(item)
            
    # Bug: list.sort() returns None in Python
    return combined.sort()


# Test block to satisfy checker requirements
list_a = [3, 1, 4]
list_b = [4, 2, 5]
output = merge_and_sort_lists(list_a, list_b)
