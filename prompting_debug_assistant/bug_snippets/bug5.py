# Bug Snippet 5 - Python List Mutation & Sort
# Intended behavior: Merge two lists, remove duplicates, sort.
# -------------------------------------------------------------

def merge_and_sort_lists(list1, list2):
    """
    Combines two lists, removes duplicate elements, and sorts them.
    Fails due to list modification during loop and list.sort() returning None.
    """
    combined = list1 + list2
    
    # Modifying list during iteration bug:
    for item in combined:
        if combined.count(item) > 1:
            combined.remove(item)
            
    # list.sort() mutates in-place and returns None:
    return combined.sort()

# Example Usage:
# print(merge_and_sort_lists([3, 1, 2], [2, 4, 1]))
