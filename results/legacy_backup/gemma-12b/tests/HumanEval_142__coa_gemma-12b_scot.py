import pytest
import math


# Focus: Boundary Values
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_index_0_multiple_of_3():
    assert sum_squares([1]) == 1

def test_sum_squares_index_0_not_multiple_of_3():
    assert sum_squares([2]) == 2

def test_sum_squares_index_3_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4]) == 1 + 4 + 9 + 64

def test_sum_squares_index_3_multiple_of_4_not_multiple_of_3():
    assert sum_squares([1, 2, 3, 4]) == 1 + 4 + 9 + 64

def test_sum_squares_index_6_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7]) == 1 + 4 + 9 + 64 + 25 + 36 + 49

# Focus: Logic Branches
def test_sum_squares_multiple_of_3():
    """Test case where list elements at indices that are multiples of 3 are squared."""
    lst = [1, 2, 3, 4, 5, 6]
    expected = 1 + 2 + 9 + 4 + 5 + 36
    assert sum_squares(lst) == expected

def test_sum_squares_multiple_of_4_not_3():
    """Test case where list elements at indices that are multiples of 4 (but not 3) are cubed."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512
    assert sum_squares(lst) == expected

def test_sum_squares_empty_list():
    """Test case for an empty list."""
    lst = []
    expected = 0
    assert sum_squares(lst) == expected

# Focus: Type Scenarios
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_list_with_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == (1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2)

def test_sum_squares_list_with_multiples_of_4_and_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == (1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144)