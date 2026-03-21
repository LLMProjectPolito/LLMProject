import pytest
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num
    return sum_result, product_result


def test_sum_product_empty_list():
    assert sum_product([]) == (0, 1)

def test_sum_product_single_element_list():
    assert sum_product([5]) == (5, 5)

def test_sum_product_multiple_elements_list():
    assert sum_product([1, 2, 3, 4]) == (10, 24)

def test_sum_product_negative_numbers_list():
    assert sum_product([-1, -2, -3, -4]) == (-10, 24)

def test_sum_product_mixed_numbers_list():
    assert sum_product([-1, 2, -3, 4]) == (2, -24)

def test_sum_product_zero_list():
    assert sum_product([0, 0, 0]) == (0, 0)

def test_sum_product_large_numbers_list():
    assert sum_product([100, 200, 300, 400]) == (1000, 2400000000)

def test_sum_product_float_numbers_list():
    with pytest.raises(TypeError):
        sum_product([1.0, 2.0, 3.0, 4.0])

def test_sum_product_non_numeric_list():
    with pytest.raises(TypeError):
        sum_product(['a', 'b', 'c', 'd'])

def test_sum_product_none_list():
    with pytest.raises(TypeError):
        sum_product([None, None, None, None])