import pytest
from typing import List, Tuple

@pytest.mark.parametrize("input_list, expected_result", [
    ([], (0, 1)),
    ([1], (1, 1)),
    ([1, 2, 3, 4], (10, 24)),
    ([-1, -2, -3, -4], (-10, 24)),
    ([0, 0, 0], (0, 0)),
    ([1, 0, 1], (2, 0)),
])
def test_sum_product(input_list: List[int], expected_result: Tuple[int, int]):
    assert sum_product(input_list) == expected_result

@pytest.mark.parametrize("numbers, expected", [
    ([], (0, 1)),
    ([1], (1, 1)),
    ([1, 2, 3], (6, 6)),
    ([4, 5, 6], (15, 120)),
    ([-1, -2, -3], (-6, -6)),
    ([0, 0, 0], (0, 0)),
])
def test_sum_product_additional(numbers, expected):
    assert sum_product(numbers) == expected

def test_sum_product_type():
    result = sum_product([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)

def test_sum_product_empty_list():
    assert sum_product([]) == (0, 1)

def test_sum_product_single_element_list():
    assert sum_product([5]) == (5, 5)

def test_sum_product_empty_product():
    result = sum_product([])
    assert result[1] == 1

def test_sum_product_empty_sum():
    result = sum_product([])
    assert result[0] == 0