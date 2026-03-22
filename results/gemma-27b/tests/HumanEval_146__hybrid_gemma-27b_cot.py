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

def test_more_mixed_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -37, -59, -71, -93]) == 5

def test_numbers_with_even_first_digit():
    assert specialFilter([25, 47, 69, 81]) == 0

def test_numbers_with_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_with_both_even_digits():
    assert specialFilter([24, 46, 68, 80]) == 0

def test_numbers_greater_than_10_but_not_special():
    assert specialFilter([12, 14, 16, 18, 21, 23]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_large_numbers():
    assert specialFilter([111, 131, 151, 171, 191]) == 5

def test_large_numbers_mixed():
    assert specialFilter([111, 131, 222, 343, 565]) == 2

def test_edge_case_11():
    assert specialFilter([11]) == 1

def test_edge_case_99():
    assert specialFilter([99]) == 1

def test_edge_case_101():
    assert specialFilter([101]) == 0

def test_edge_case_1111():
    assert specialFilter([1111]) == 0

def test_zero_in_number():
    assert specialFilter([103, 305, 507, 709]) == 0

def test_mixed_positive_negative():
    assert specialFilter([15, -37, 14, -59, 21, -71]) == 2

def test_all_negative_not_special():
    assert specialFilter([-2, -4, -6, -8, -10]) == 0

def test_large_numbers_2():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_large_numbers_mixed_2():
    assert specialFilter([111, 222, 333, 444, 555]) == 3