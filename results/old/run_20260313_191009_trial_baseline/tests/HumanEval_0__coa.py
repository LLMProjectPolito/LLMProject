import pytest
import math


# Focus: Boundary Values
def test_has_close_elements_threshold_zero():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) is False

def test_has_close_elements_threshold_negative():
    assert has_close_elements([1.0, 2.0, 3.0], -0.5) is False

def test_has_close_elements_threshold_zero_with_duplicates():
    assert has_close_elements([1.0, 1.0, 1.0], 0.0) is False

# Focus: Empty and Single-Element Lists
def test_empty_list():
    assert not has_close_elements([], 1.0)

def test_single_element_list():
    assert not has_close_elements([1.0], 1.0)

def test_single_element_list_with_threshold_zero():
    assert not has_close_elements([1.0], 0.0)

# Focus: Duplicate and Unordered Elements
def test_has_close_elements_duplicate_elements():
    assert has_close_elements([1.0, 2.0, 3.0, 2.0], 0.5) is True

def test_has_close_elements_unordered_elements():
    assert has_close_elements([3.0, 2.0, 1.0, 2.0], 0.5) is True

def test_has_close_elements_no_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5) is False