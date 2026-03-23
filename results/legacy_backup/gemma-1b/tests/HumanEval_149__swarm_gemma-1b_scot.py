import pytest
from typing import List

def list_sort(lst: List[str]) -> List[str]:
    """Sorts a list of strings by length, then alphabetically, and removes strings with odd lengths."""
    return sorted(lst, key=lambda x: (len(x), x))

def list_sort(lst: List[str]) -> List[str]:
    """Sorts a list of strings based on length, then alphabetically."""
    return sorted(lst, key=lambda x: (len(x), x))

def list_sort(lst: List[str]) -> List[str]:
    """Sorts a list of strings based on length, then alphabetically."""
    return sorted(lst, key=lambda x: (len(x), x))

Final Suite:
    import pytest

    def test_empty_list():
        assert list_sort([]) == []

    def test_single_element_list():
        assert list_sort([1]) == [1]

    def test_even_length_list():
        assert list_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_odd_length_list():
        assert list_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_mixed_length_list():
        assert list_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]