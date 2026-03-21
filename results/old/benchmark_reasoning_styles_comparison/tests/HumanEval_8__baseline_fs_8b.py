import pytest

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
    assert sum_product([1000, 2000, 3000]) == (6000, 6000000000)

def test_sum_product_invalid_input():
    with pytest.raises(TypeError):
        sum_product("123")

def test_sum_product_none_input():
    with pytest.raises(TypeError):
        sum_product(None)