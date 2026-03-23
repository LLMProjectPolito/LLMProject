import pytest

def list_sort(lst):
    """Sorts a list of strings based on word length, ascending by length, and alphabetically for duplicates."""
    return sorted(lst, key=lambda x: (len(x), x))