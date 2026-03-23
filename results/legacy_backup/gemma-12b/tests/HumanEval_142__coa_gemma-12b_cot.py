import pytest
import math


# Focus: Boundary Values
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_sum_squares_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_sum_squares_single_element_neither_multiple():
    assert sum_squares([5]) == 5

def test_sum_squares_multiple_of_3_and_4():
    assert sum_squares([12]) == 144

# Focus: Logic Branches
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 14

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4]) == 22

def test_sum_squares_mixed_cases():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 249

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

# Focus: Type Scenarios
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_basic_list():
    assert sum_squares([1, 2, 3]) == 14

def test_sum_squares_mixed_list():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126