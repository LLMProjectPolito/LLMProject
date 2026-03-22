import pytest
import math


# Focus: Boundary Values
import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_list_with_only_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_list_with_only_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_list_with_zero():
    assert double_the_difference([0]) == 0

def test_list_with_one_odd_number():
    assert double_the_difference([1]) == 1

def test_list_with_one_even_number():
    assert double_the_difference([2]) == 0

def test_list_with_max_int():
    assert double_the_difference([2**31 - 1]) == (2**31 - 1)**2

def test_list_with_min_int():
    assert double_the_difference([-2**31]) == 0

# Focus: Invalid Input Handling
import pytest

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        double_the_difference("not a list")

def test_invalid_input_list_with_non_numeric():
    with pytest.raises(TypeError):
        double_the_difference([1, "a", 2])

def test_invalid_input_list_with_float():
    with pytest.raises(TypeError):
        double_the_difference([1, 2.5, 3])

# Focus: Logic Branches
import pytest

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_negative_and_non_integer():
    assert double_the_difference([-1, -2, 0, 2.5]) == 0

def test_double_the_difference_mixed_positive_negative_odd_even():
    assert double_the_difference([1, 3, -2, 0, 5, -7]) == 1 + 9 + 25