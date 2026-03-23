import pytest

def test_basic_cases():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0
    assert specialFilter([12, 24, 36, 48, 50]) == 0

def test_all_matching_numbers():
    assert specialFilter([11, 33, 55, 77, 99]) == 5
    assert specialFilter([13, 35, 57, 79, 91]) == 5

def test_negative_numbers():
    assert specialFilter([-15, -33, -57, -71, -99]) == 5
    assert specialFilter([-12, -34, -56, -78, -90]) == 0
    assert specialFilter([-15, 15]) == 2

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_with_even_digits():
    assert specialFilter([12, 34, 56, 78, 90]) == 0
    assert specialFilter([21, 43, 65, 87, 09]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0

def test_large_numbers():
    assert specialFilter([1111111111, 3333333333, 5555555555]) == 3
    assert specialFilter([1234567891, 3456789123, 5678912345]) == 3

def test_boundary_conditions():
    assert specialFilter([11, 9, 10]) == 1
    assert specialFilter([10, 11, 12]) == 1
    assert specialFilter([9, 10, 11]) == 1

def test_zero():
    assert specialFilter([0]) == 0

def test_mixed_cases():
    assert specialFilter([15, 22, 33, 44, 55, 66, 77, 88, 99, 101]) == 5
    assert specialFilter([-11, -22, -33, -44, -55]) == 3