import pytest
from typing import List

@pytest.mark.parametrize("numbers, threshold, expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 1.1, 2.0], 0.2, True),
    ([1.0, 2.0, 3.0], 1.0, True),
    ([1.0, 2.0, 3.0], 1.5, True),
    ([1.0, 2.0, 3.0], 2.5, True),
    ([1.0, 1.0, 1.0], 0.5, True),
    ([-1.0, -2.0, -3.0], 0.5, False),
    ([1.0, 2.0, 3.0], 0.1, True),
    ([1.0, 2.0, 3.0], 1.5, True),
    ([1.0, 3.0, 5.0], 2.1, False),
    ([1.0], 0.5, False),
    ([], 0.5, False),
])
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool) -> None:
    assert has_close_elements(numbers, threshold) == expected

def test_has_close_elements_empty_list() -> None:
    assert has_close_elements([], 0.5) == False

def test_has_close_elements_single_element() -> None:
    assert has_close_elements([1.0], 0.5) == False

def test_has_close_elements_two_elements() -> None:
    assert has_close_elements([1.0, 2.0], 0.5) == False

def test_has_close_elements_negative_threshold() -> None:
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0], -0.5)

def test_has_close_elements_non_numeric_input() -> None:
    with pytest.raises(TypeError):
        has_close_elements(['a', 'b'], 0.5)

def test_has_close_elements_non_list_input() -> None:
    with pytest.raises(TypeError):
        has_close_elements('123', 0.5)