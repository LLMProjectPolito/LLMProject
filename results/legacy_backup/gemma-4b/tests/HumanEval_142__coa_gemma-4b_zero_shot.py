import pytest
import math


# Focus: Boundary Values
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 225

# Focus: Type Scenarios
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_no_multiples_of_3_or_4():
    assert sum_squares([1, 2, 3, 4, 5]) == 15

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5]) == 15

# Focus: Logic Branches
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 225