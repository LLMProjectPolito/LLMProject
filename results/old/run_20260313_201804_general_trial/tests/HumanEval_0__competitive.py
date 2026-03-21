import pytest
from typing import List

def test_has_close_elements_empty_list():
    assert not has_close_elements([], 0.5)

def test_has_close_elements_single_element():
    assert not has_close_elements([1.0], 0.5)

def test_has_close_elements_no_close_elements():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)

def test_has_close_elements_negative_numbers():
    assert has_close_elements([-1.0, -2.8, -3.0, -4.0, -5.0, -2.0], 0.3)

def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 2.0, 3.0], 0)

def test_has_close_elements_large_threshold():
    assert not has_close_elements([1.0, 2.0, 3.0], 10.0)

def test_has_close_elements_float_threshold():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)

def test_has_close_elements_large_list():
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], 0.5)

def test_has_close_elements_list_with_duplicates():
    assert has_close_elements([1.0, 2.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.3)