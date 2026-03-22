import pytest
import math


# Focus: Boundary Values
def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element_correct():
    assert compare([5], [5]) == [0]

def test_compare_single_element_incorrect():
    assert compare([5], [2]) == [3]

def test_compare_all_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_all_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed_correct_incorrect():
    assert compare([1, 2, 3, 4, 5], [1, 5, 3, 0, 5]) == [0, 3, 0, 4, 0]

# Focus: Equivalence Partitioning
def test_compare_all_correct():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_compare_all_incorrect():
    assert compare([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == [5, 5, 5, 5, 5]

def test_compare_mixed():
    assert compare([1, 2, 3, 4, 5], [1, 2, 0, 4, 6]) == [0, 0, 3, 0, 1]

def test_compare_negative_values():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_empty_lists():
    assert compare([], []) == []

# Focus: Error Handling/Invalid Input
def test_compare_invalid_input_different_lengths():
    assert compare([1, 2, 3], [1, 2]) == [0, 0, 1]

def test_compare_invalid_input_non_integer_elements():
    assert compare([1, 2, 'a'], [1, 2, 3]) == [0, 0, 'a']