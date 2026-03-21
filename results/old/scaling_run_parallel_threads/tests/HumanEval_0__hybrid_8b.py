import pytest
from typing import List

@pytest.mark.parametrize("numbers, threshold, expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 1.1, 3.0], 0.3, True),
    ([1.0, 1.1, 3.0], 0.05, False),
    ([1.0, 1.0, 3.0], 0.1, True),
    ([], 0.1, False),
    ([1.0], 0.1, False),
    ([1.0, 2.0], 1.5, True),
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 1.1, 2.0], 0.2, True),
    ([1.0, 1.1, 2.0], 0.1, False),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 1.0, False),
    ([1.0, 1.0, 2.0], 0.1, True),
    ([], 0.5, False),
    ([1.0], 0.5, False),
])
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool):
    assert has_close_elements(numbers, threshold) == expected

def test_has_close_elements_empty_list():
    assert has_close_elements([], 0.1) == False

def test_has_close_elements_single_element():
    assert has_close_elements([1.0], 0.1) == False

def test_has_close_elements_two_elements_far_apart():
    assert has_close_elements([1.0, 2.0], 0.5) == False

def test_has_close_elements_two_elements_close_together():
    assert has_close_elements([1.0, 1.1], 0.2) == True