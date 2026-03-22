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

def test_sum_squares_large_numbers():
    assert sum_squares([10, 20, 30, 40, 50]) == 5000

# Focus: Empty List/Null Input
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_null_input():
    with pytest.raises(TypeError):
        sum_squares(None)

# Focus: Positive/Negative/Zero Integers
import pytest

def test_sum_squares_positive_integers():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 605

def test_sum_squares_negative_integers():
    assert sum_squares([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]) == 605

def test_sum_squares_mixed_integers():
    assert sum_squares([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12]) == 187