import pytest
from typing import List

def test_has_close_elements_empty_list():
    assert not has_close_elements([], 1.0)

def test_has_close_elements_single_element():
    assert not has_close_elements([1.0], 1.0)

def test_has_close_elements_no_close_elements():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)

def test_has_close_elements_close_elements_at_start():
    assert has_close_elements([1.0, 1.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements_at_end():
    assert has_close_elements([1.0, 2.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements_at_both_ends():
    assert has_close_elements([1.0, 1.0, 2.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements_with_negative_numbers():
    assert has_close_elements([-1.0, -2.0, -2.0, -3.0], 0.5)

def test_has_close_elements_close_elements_with_large_threshold():
    assert not has_close_elements([1.0, 2.0, 3.0], 10.0)

def test_has_close_elements_close_elements_with_small_threshold():
    assert has_close_elements([1.0, 2.0, 3.0], 0.01)

def test_has_close_elements_close_elements_with_duplicates():
    assert has_close_elements([1.0, 1.0, 2.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements_with_empty_list_and_large_threshold():
    assert not has_close_elements([], 10.0)

def test_has_close_elements_close_elements_with_single_element_and_large_threshold():
    assert not has_close_elements([1.0], 10.0)