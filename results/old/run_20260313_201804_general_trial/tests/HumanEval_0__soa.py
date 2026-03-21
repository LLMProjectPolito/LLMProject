import pytest
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

def test_has_close_elements_empty_list():
    assert not has_close_elements([], 1.0)

def test_has_close_elements_single_element():
    assert not has_close_elements([1.0], 1.0)

def test_has_close_elements_no_close_elements():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)

def test_has_close_elements_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)

def test_has_close_elements_threshold_zero():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0)

def test_has_close_elements_threshold_negative():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0, 3.0], -0.5)

def test_has_close_elements_threshold_non_numeric():
    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, 3.0], 'a')

def test_has_close_elements_non_numeric_list():
    with pytest.raises(TypeError):
        has_close_elements(['a', 'b', 'c'], 1.0)

def test_has_close_elements_list_with_non_numeric_element():
    with pytest.raises(TypeError):
        has_close_elements([1.0, 'a', 3.0], 1.0)