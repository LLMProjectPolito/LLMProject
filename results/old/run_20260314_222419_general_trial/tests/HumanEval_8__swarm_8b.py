import pytest
import math

def test_sum_product_single_negative_number():
    """ Test case to verify that a single negative number in the list 
    doesn't affect the product, which remains 1 when multiplied by a negative number."""
    result = sum_product([-1])
    assert result == (0, -1)  # Since empty sum should be equal to 0 and empty product should be equal to -1 for single negative number

def test_sum_product_with_single_zero():
    result = sum_product([0])
    assert result == (0, 0)

def test_sum_product_with_negative_numbers():
    """ Test a scenario where negative numbers in the list."""
    result = sum_product([-1, -2, -3, -4])
    assert result[0] == -10  # Expected sum for given list
    assert result[1] == 24  # Expected product for given list