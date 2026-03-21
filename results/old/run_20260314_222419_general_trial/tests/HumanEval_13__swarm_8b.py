import pytest
from math import gcd

def test_greatest_common_divisor_zero():
    """Test the greatest common divisor function with one zero input"""
    assert greatest_common_divisor(0, 5) == 5

def test_greatest_common_divisor_both_zeros():
    """Test case: Both numbers are zero"""
    assert greatest_common_divisor(0, 0) == 0

def test_greatest_common_divisor_zero_and_non_zero_match_math_gcd():
    """Test case: Compare with math.gcd for zero and non-zero input"""
    assert greatest_common_divisor(0, 5) == gcd(0, 5)