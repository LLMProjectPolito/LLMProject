import pytest
import math


# Focus: Boundary Values
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

# Focus: Logic Branches
def test_sum_squares_multiple_of_3():
    lst = [1, 2, 3, 4, 5, 6]
    expected = 1 + 2 + 9 + 4 + 5 + 36
    assert sum_squares(lst) == expected

def test_sum_squares_multiple_of_4_not_3():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = 1 + 8 + 3 + 64 + 5 + 6 + 7 + 8
    assert sum_squares(lst) == expected

def test_sum_squares_no_multiples():
    lst = [1, 2, 5, 7, 9]
    expected = 1 + 2 + 5 + 7 + 9
    assert sum_squares(lst) == expected

# Focus: Type Scenarios
def test_empty_list():
    assert sum_squares([]) == 0

def test_list_with_no_multiples():
    assert sum_squares([1, 2, 4, 5]) == 12

def test_list_with_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 2 + 27 + 4 + 5 + 36 + 7 + 64 + 9 + 10 == 175