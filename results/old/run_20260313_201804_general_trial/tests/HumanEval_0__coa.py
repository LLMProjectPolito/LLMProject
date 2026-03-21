import pytest
import math


# Focus: Boundary Values
def test_has_close_elements_threshold_zero():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) is False

def test_has_close_elements_threshold_negative():
    assert has_close_elements([1.0, 2.0, 3.0], -0.1) is False

def test_has_close_elements_threshold_zero_list():
    assert has_close_elements([1.0, 1.0, 3.0], 0.0) is True

# Focus: Type Scenarios
def test_has_close_elements_empty_list():
    assert not has_close_elements([], 0.5)

def test_has_close_elements_single_element():
    assert not has_close_elements([1.0], 0.5)

def test_has_close_elements_no_close_elements():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)

def test_has_close_elements_threshold_zero():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0)

def test_has_close_elements_negative_numbers():
    assert has_close_elements([-1.0, 0.0, 1.0], 0.5)

def test_has_close_elements_decimal_numbers():
    assert has_close_elements([1.1, 2.2, 3.3], 0.5)

# Focus: Logic Branches
def test_has_close_elements_empty_list():
    assert not has_close_elements([], 0.5)

def test_has_close_elements_single_element():
    assert not has_close_elements([1.0], 0.5)

def test_has_close_elements_no_close_elements():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)