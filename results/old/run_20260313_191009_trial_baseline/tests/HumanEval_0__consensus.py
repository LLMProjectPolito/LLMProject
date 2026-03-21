import pytest
from typing import List

@pytest.mark.parametrize("numbers, threshold, expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 1.1, 2.0], 0.2, True),
    ([1.0, 1.1, 2.0], 0.05, False),
    ([1.0], 0.5, False),
    ([], 0.5, False),
    ([1.0, 2.0], 1.0, False),
    ([1.0, 1.0], 0.5, True),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 10.0, True),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, True),
    ([1.0, 1.0, 1.0], 0.5, True),
    ([1.0, 1.5, 2.0], 0.4, True),
    ([1.0, 1.6, 2.0], 0.5, True),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 1.0, False),
])
def test_has_close_elements(numbers: List[float], threshold: float, expected: bool):
    assert has_close_elements(numbers, threshold) == expected

def test_has_close_elements_invalid_input_type():
    with pytest.raises(TypeError):
        has_close_elements("not a list", 0.5)

def test_has_close_elements_invalid_list_element_type():
    with pytest.raises(TypeError):
        has_close_elements([1, "not a float", 3.0], 0.5)

def test_has_close_elements_invalid_threshold_type():
    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, 3.0], "not a float")

def test_has_close_elements_negative_threshold():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0, 3.0], -0.5)

def test_has_close_elements_zero_threshold():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0, 3.0], 0.0)