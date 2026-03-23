import pytest

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_special_numbers():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_numbers_less_than_10():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_equal_to_10():
    assert specialFilter([10]) == 0

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_large_numbers_mixed():
    assert specialFilter([111, 222, 333, 444, 555]) == 3

def test_edge_case_1():
    assert specialFilter([11]) == 1

def test_edge_case_2():
    assert specialFilter([99]) == 1

def test_edge_case_3():
    assert specialFilter([12]) == 0

def test_edge_case_4():
    assert specialFilter([21]) == 0

def test_all_even_digits():
    assert specialFilter([22, 44, 66, 88]) == 0

def test_mixed_positive_negative():
    assert specialFilter([-15, 37, -59, 71, -93]) == 5

def test_zero_in_number():
    assert specialFilter([101, 303, 505, 707, 909]) == 0

def test_numbers_with_leading_zeros():
    assert specialFilter([01, 03, 05, 07, 09]) == 0