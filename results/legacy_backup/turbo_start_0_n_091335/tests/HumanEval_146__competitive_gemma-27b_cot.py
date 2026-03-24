import pytest

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_numbers_with_even_first_digit():
    assert specialFilter([21, 43, 65, 87, 09]) == 0

def test_numbers_with_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_with_both_even_digits():
    assert specialFilter([24, 46, 68, 80]) == 0

def test_numbers_greater_than_10_but_not_special():
    assert specialFilter([12, 14, 16, 18, 21]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_large_numbers():
    assert specialFilter([1001, 1002, 1003, 1005, 1007, 1009]) == 4

def test_all_special_numbers():
    assert specialFilter([11, 13, 15, 17, 19, 31, 33, 35, 37, 39]) == 10

def test_mixed_positive_and_negative():
    assert specialFilter([-11, 13, -15, 17, -19, 31]) == 3