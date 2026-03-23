import pytest
import math


# Focus: Boundary Values
import pytest

def test_special_filter_empty_array():
    assert specialFilter([]) == 0

def test_special_filter_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12, 20]) == 0

def test_special_filter_single_special_number():
    assert specialFilter([15]) == 1

def test_special_filter_all_special_numbers():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_special_filter_negative_numbers():
    assert specialFilter([-15, -33, -11]) == 3

def test_special_filter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_large_numbers():
    assert specialFilter([109, 111, 123, 135, 157, 179, 191]) == 7

def test_special_filter_boundary_10():
    assert specialFilter([10]) == 0

def test_special_filter_boundary_11():
    assert specialFilter([11]) == 1

def test_special_filter_boundary_99():
    assert specialFilter([99]) == 1

def test_special_filter_boundary_100():
    assert specialFilter([100]) == 0

# Focus: Logic Branches
import pytest

def test_special_filter_empty_list():
    assert specialFilter([]) == 0

def test_special_filter_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_special_filter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_multiple_special_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_special_filter_single_special_number():
    assert specialFilter([11]) == 1

def test_special_filter_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_special_filter_numbers_close_to_10():
    assert specialFilter([9, 11, 10, 12]) == 1

# Focus: Invalid Input Handling
import pytest

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        specialFilter("not a list")

def test_invalid_input_list_with_non_numbers():
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 35])

def test_invalid_input_empty_list():
    assert specialFilter([]) == 0