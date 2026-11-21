def get_last_n_items(items, n, cache=None):
    """Return the exact last n items from a list without shared mutable state."""
    if cache is None:
        cache = []
    if n <= 0 or not items:
        return []
    cache.append(n)
    return items[-n:]


def calculate_average(numbers):
    """Calculate the arithmetic mean of a list of numbers safely."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    assert get_last_n_items(data, 3) == [30, 40, 50]
    assert get_last_n_items(data, 10) == [10, 20, 30, 40, 50]
    assert get_last_n_items(data, 0) == []
    assert calculate_average(data) == 30.0
    assert calculate_average([]) == 0.0
    print("bug1_fixed.py: All 5 assertions passed.")
