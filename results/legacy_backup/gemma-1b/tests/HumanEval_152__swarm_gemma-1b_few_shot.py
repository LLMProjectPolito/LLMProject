import pytest
import math

def compare(list1, list2):
    """
    Compares two lists element by element.

    Args:
        list1: The first list.
        list2: The second list.

    Returns:
        A list containing the results of comparing the two lists.
    """
    result = []
    for i in range(min(len(list1), len(list2))):
        if list1[i] == list2[i]:
            result.append(i)
        else:
            result.append(0)
    return result

def test_compare_positive():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_positive():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

Final Suite:
    test_compare_positive()