import pytest

def test_empty_list():
    assert sum_squares([]) == 0

def test_list_with_one_element():
    assert sum_squares([5]) == 5

def test_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == -1 + -2 + 9 + -64 + -5

def test_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + -2 + 9 + -64 + 5 + -216

def test_edge_case_multiple_of_12():
    assert sum_squares([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 2 + 3 + 16 + 5 + 36 + 7 + 64 + 9 + 10 + 11 + 1728

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400, 500]) == 100 + 200 + 90000 + 64000000 + 500

def test_zeroes():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 9 + 36 + 81

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 64 + 512 + 1728

def test_list_with_only_multiples_of_12():
    assert sum_squares([12, 24, 36]) == 144 + 13824 + 46656