
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
import math


# Focus: Boundary Values
import pytest

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_matches():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_match():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matches():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([11, 13, 15, 17, 19, 21, 33]) == 3

# Focus: Type Scenarios
import pytest

def test_type_scenarios_empty():
    assert specialFilter([]) == 0

def test_type_scenarios_integers():
    assert specialFilter([15, 33, 45, 109]) == 2

def test_type_scenarios_mixed():
    assert specialFilter([15, -73, 14, -15]) == 1

# Focus: Logic Branches
import pytest

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_matches():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_match():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matches():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([11, 13, 15, 17, 19, 21, 33]) == 3