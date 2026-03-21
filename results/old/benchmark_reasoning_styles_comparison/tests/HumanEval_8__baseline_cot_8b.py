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
    assert sum_product([1000, 2000, 3000, 4000]) == (10000, 24000000000000)

def test_sum_product_floats_list():
    with pytest.raises(TypeError):
        sum_product([1.0, 2.0, 3.0, 4.0])

def test_sum_product_non_numeric_list():
    with pytest.raises(TypeError):
        sum_product(['a', 'b', 'c', 'd'])

def test_sum_product_none_list():
    with pytest.raises(TypeError):
        sum_product([None, None, None, None])