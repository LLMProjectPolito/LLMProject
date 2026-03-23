import pytest
import math

def compare(list1, list2):
    """
    Compares two lists and returns a list of differences.
    """
    result = []
    for i in range(min(len(list1), len(list2))):
        diff = list1[i] - list2[i]
        result.append(diff)
    return result

def test_compare_perfect_guess():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]