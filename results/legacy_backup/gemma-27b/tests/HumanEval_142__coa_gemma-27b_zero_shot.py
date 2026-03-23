import pytest
import math


# Focus: Index-based Calculations
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed_indices():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 440

def test_sum_squares_only_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 14 + 36

def test_sum_squares_only_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

# Focus: Empty List Handling
def test_empty_list():
    assert sum_squares([]) == 0

def test_empty_list_with_none():
    assert sum_squares([None]) == 0

# Focus: Positive/Negative Numbers
import pytest

def test_positive_numbers():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 29
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 140

def test_negative_numbers():
    assert sum_squares([-1, -2, -3]) == -6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([-1, -2, -3, -4, -5, -6]) == -29

def test_mixed_numbers():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == -29