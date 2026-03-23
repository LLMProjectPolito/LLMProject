import pytest

def list_sort(lst):
    """Sorts a list of strings based on length, with duplicates handled."""
    return sorted(lst, key=lambda x: (len(x), x))