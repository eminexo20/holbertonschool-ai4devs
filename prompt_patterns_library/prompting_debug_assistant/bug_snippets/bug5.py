def merge_and_sort_lists(list1, list2):
    """Merge two lists and return sorted unique elements."""
    combined = list1 + list2
    for item in combined:
        if combined.count(item) > 1:
            combined.remove(item)
    return combined.sort()
