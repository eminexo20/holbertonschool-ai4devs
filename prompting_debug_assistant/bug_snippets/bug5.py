def merge_and_sort_lists(list1, list2):
    """
    Merge two lists, remove duplicate items, and sort them.
    Bug: Mutates list during loop and returns list.sort() (None).
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        return []
        
    combined = list1 + list2
    
    # Bug: Modifying array length during iteration
    for item in combined:
        if combined.count(item) > 1:
            combined.remove(item)
            
    # Bug: list.sort() returns None in Python
    return combined.sort()


# Test script execution
first_list = [3, 1, 4]
second_list = [4, 2, 5]
final_result = merge_and_sort_lists(first_list, second_list)
print("Sorted Result:", final_result)
