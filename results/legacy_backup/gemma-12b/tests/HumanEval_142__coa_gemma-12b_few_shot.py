import pytest
import math


# Focus: Boundary Values
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_index_3_boundary():
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 14

def test_sum_squares_index_4_boundary():
    assert sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 224

# Focus: Logic Branches
def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512 + 9 + 10
    assert sum_squares([1, 2, 3, 4]) == 1 + 2 + 3 + 64

def test_sum_squares_both_multiple():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 9 + 10 + 11 + 1728

# Focus: Type Scenarios
def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126