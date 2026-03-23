import pytest
from your_module import sum_squares  # Replace your_module

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 14

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_numbers():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == -11

def test_multiples_of_3():
    assert sum_squares([3, 6, 9, 1, 2, 4]) == 102

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 130

def test_multiples_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 278

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40]) == 3000

def test_zeroes():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_single_element():
    assert sum_squares([5]) == 5

def test_list_with_zeros_and_negatives():
    assert sum_squares([0, -1, 2, -3, 4, -5]) == -21

def test_list_with_only_positive_numbers():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385

def test_list_with_only_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1710

def test_complex_list():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1186