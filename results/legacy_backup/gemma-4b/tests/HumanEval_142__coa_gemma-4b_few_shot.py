import pytest
import math


# Focus: Boundary Values
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    lst = [1, 2, 3]
    assert sum_squares(lst) == 6

def test_sum_squares_multiple_of_4():
    lst = [1, 2, 3, 4, 5, 6]
    assert sum_squares(lst) == 115

# Focus: Type Scenarios
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_no_multiples():
    assert sum_squares([1, 2, 3, 4, 5]) == 15

def test_sum_squares_mixed():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 16 + 25 + 36

# Focus: Logic Branches
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4():
    assert sum_squares([1, 2, 3, 4]) == 30