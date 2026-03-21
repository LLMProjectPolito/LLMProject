import pytest
from typing import List

@pytest.mark.parametrize("numbers, threshold, expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 1.0], 0.5, True),
    ([1.0, 2.0, 3.0], 1.1, True),
    ([1.0, 2.0, 3.0], 2.1, True),
    ([1.0], 0.5, False),
    ([], 0.5, False),
    ([1.0, 2.0, 3.0], 0.1, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0], 10.0, False),
    ([-1.0, 1.0], 1.5, False),
    ([1.5, 1.6, 1.7, 1.8], 0.1, True),
])
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool) -> None:
    assert has_close_elements(numbers, threshold) == expected

def test_has_close_elements_empty_list() -> None:
    assert not has_close_elements([], 0.5)

def test_has_close_elements_single_element() -> None:
    assert not has_close_elements([1.0], 0.5)

def test_has_close_elements_negative_threshold() -> None:
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0], -0.5)

def test_has_close_elements_zero_threshold() -> None:
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0], 0.0)