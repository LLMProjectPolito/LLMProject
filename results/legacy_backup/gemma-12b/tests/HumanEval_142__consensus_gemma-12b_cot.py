import pytest

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 14

def test_list_with_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_list_with_mixed_numbers():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 245

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 234

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 384

def test_list_with_multiples_of_both_3_and_4():
    assert sum_squares([3, 4, 6, 8, 9, 12, 15, 16]) == 456

def test_list_with_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 1010000

def test_list_with_floats_converted_to_ints():
    assert sum_squares([1.0, 2.0, 3.0, 4.0]) == 30

def test_list_with_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_list_with_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_list_with_single_element_not_multiple_of_3_or_4():
    assert sum_squares([5]) == 5