import pytest
from typing import List

def test_has_close_elements_no_close_elements():
    # Test case: No close elements in the list
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements():
    # Test case: Close elements in the list
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)

def test_has_close_elements_threshold_zero():
    # Test case: Threshold is zero
    assert has_close_elements([1.0, 2.0, 3.0], 0.0)

def test_has_close_elements_threshold_negative():
    # Test case: Threshold is negative
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0, 3.0], -0.5)

def test_has_close_elements_empty_list():
    # Test case: Empty list
    assert not has_close_elements([], 0.5)

def test_has_close_elements_single_element():
    # Test case: Single element in the list
    assert not has_close_elements([1.0], 0.5)

def test_has_close_elements_duplicate_elements():
    # Test case: Duplicate elements in the list
    assert not has_close_elements([1.0, 1.0, 2.0], 0.5)

def test_has_close_elements_float_precision():
    # Test case: Float precision
    assert has_close_elements([1.0, 2.0, 3.0], 0.5)

def test_has_close_elements_large_threshold():
    # Test case: Large threshold
    assert not has_close_elements([1.0, 2.0, 3.0], 10.0)

def test_has_close_elements_small_threshold():
    # Test case: Small threshold
    assert has_close_elements([1.0, 2.0, 3.0], 0.01)

def test_has_close_elements_large_list():
    # Test case: Large list
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], 0.5)

def test_has_close_elements_small_list():
    # Test case: Small list
    assert not has_close_elements([1.0, 2.0], 0.5)