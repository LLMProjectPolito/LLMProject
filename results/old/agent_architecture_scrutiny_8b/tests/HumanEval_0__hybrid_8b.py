import pytest
from typing import List

@pytest.mark.parametrize("numbers, threshold, expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 1.1, 2.0], 0.2, True),
    ([1.0, 2.0, 3.0], 1.0, True),
    ([1.0], 0.5, False),
    ([], 0.5, False),
    ([1.0, 1.0, 1.0], 0.5, True),
    ([10.0, 20.0, 30.0], 5.0, False),
    ([1.0, 2.0], 1.5, False),
])
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool):
    assert has_close_elements(numbers, threshold) == expected

def test_has_close_elements_empty_list():
    assert has_close_elements([], 0.5) == False

def test_has_close_elements_single_element():
    assert has_close_elements([1.0], 0.5) == False

def test_has_close_elements_threshold_zero():
    assert has_close_elements([1.0, 2.0], 0.0) == False

def test_has_close_elements_threshold_negative():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0], -0.5)

def test_has_close_elements_non_numeric_input():
    with pytest.raises(TypeError):
        has_close_elements([1.0, '2.0'], 0.5)

def test_has_close_elements_two_elements_list():
    assert has_close_elements([1.0, 2.0], 1.5) == False