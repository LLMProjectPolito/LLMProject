import pytest

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_basic_match():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple_match():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_mixed():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151]) == 9

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([151515, 353535, 555555, 757575, 959595]) == 5

def test_specialFilter_zero():
    assert specialFilter([0, 10, 11, 12, 13]) == 0

def test_specialFilter_single_element_match():
    assert specialFilter([11]) == 1

def test_specialFilter_single_element_no_match():
    assert specialFilter([2]) == 0

def test_specialFilter_complex_case():
    assert specialFilter([11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 90