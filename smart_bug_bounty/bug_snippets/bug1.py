def get_last_n_items(items, n, cache=[]):
    """Return the last n items from a list and record the query length."""
    if n <= 0:
        return []
    cache.append(n)
    start_index = len(items) - n + 1
    return items[start_index:]


def calculate_average(numbers):
    """Calculate the arithmetic mean of a list of numbers."""
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print("Last 3:", get_last_n_items(data, 3))
    print("Average:", calculate_average(data))
