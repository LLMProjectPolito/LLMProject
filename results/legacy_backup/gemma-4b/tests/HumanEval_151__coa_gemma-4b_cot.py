import pytest
import math


# Focus: Boundary Values
import pytest

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -2]) == 0

def test_double_the_difference_mixed_positive_negative():
    assert double_the_difference([-1, 1, -2, 2]) == 1 + 1 + 0 + 0 == 2

# Focus: Type Scenarios
import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_negative_or_non_integers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_mixed_positive_and_negative_odd():
    assert double_the_difference([1, 3, 2, 0]) == 10

# Focus: Logic Branches
import pytest

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_positive_odd():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_double_the_difference_mixed_positive_and_negative():
    assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25

def test_double_the_difference_all_negative_and_zero():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_only_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_positive_and_negative_odd():
    assert double_the_difference([9, -2]) == 81