import pytest
from math import gcd

def list_sort(lst):
    """
    Sorts a list of numbers in ascending order.

    Args:
        lst: A list of numbers.

    Returns:
        A new list containing the sorted numbers.
    """
    unique_sorted = sorted(list(set(lst)))
    return unique_sorted

def list_sort(lst):
    """
    Sorts a list of numbers in ascending order.

    Args:
        lst: A list of numbers.

    Returns:
        A new list containing the sorted numbers.
    """
    new_lst = []
    for s in lst:
        if len(s) % 2 == 0:
            new_lst.append(s)
        else:
            if s < new_lst[0]:
                new_lst.append(s)
            elif s > new_lst[-1]:
                new_lst.append(s)
    new_lst.sort()
    return new_lst

def list_sort(lst):
    """
    Sorts a list of numbers in ascending order.

    Args:
        lst: A list of numbers.

    Returns:
        A new list containing the sorted numbers.
    """
    new_lst = []
    for s in lst:
        if len(s) % 2 == 0:
            new_lst.append(s)
        else:
            if s < new_lst[0]:
                new_lst.append(s)
            else:
                new_lst.append(s)
    new_lst.sort()
    return new_lst

@pytest.mark.parametrize(
    "lst, expected"
)
def test_list_sort(lst):
    """
    Tests the list_sort function with a sample list.
    """
    assert list_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert list_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert list_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert list_sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
    assert list_sort([1, 2, 2, 4]) == [1, 2, 2, 4]
    assert list_sort([1, 2, 3, 3]) == [1, 2, 3, 3]
    assert list_sort([1, 2, 3, 4, 5, 5]) == [1, 2, 3, 4, 5, 5]
    assert list_sort([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert list_sort([]) == []