import pytest

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 6

def test_list_with_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_list_with_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

def test_list_with_multiples_of_both_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 9 + 10 + 11 + 1728

def test_list_with_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + 25 + 4 + 1 + 125

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == 1 + 4 + 9 + 16 + 25 + 36

def test_list_with_zeros():
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 0 + 1 + 4 + 9 + 16 + 25

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 10000 + 8000000 + 90000 + 640000

def test_list_with_floats_converted_to_int():
    assert sum_squares([1.0, 2.0, 3.0, 4.0]) == 1 + 4 + 9 + 16