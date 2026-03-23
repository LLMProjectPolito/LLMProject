def list_sort(lst):
    """Sorts a list of strings based on their lengths, preserving the order of strings with the same length."""
    return sorted(lst, key=lambda x: (len(x), x))