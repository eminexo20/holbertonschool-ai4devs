def merge_and_sort_lists(list1, list2):
    """
    Combines two lists, removes duplicate elements, and sorts them.
    """
    combined = list1 + list2
    unique_items = list(set(combined))
    return sorted(unique_items)

# Example Usage:
if __name__ == "__main__":
    print(merge_and_sort_lists([3, 1, 2], [2, 4, 1]))
