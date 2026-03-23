import pytest
import math

def test_do_algebra_exponentiation_with_zero_base():
    """Test exponentiation with zero as the base."""
    operator = ['**']
    operand = [0, 2]
    assert do_algebra(operator, operand) == 0

def test_do_algebra_exponentiation_with_zero_exponent():
    """Test exponentiation with zero as the exponent."""
    operator = ['**']
    operand = [2, 0]
    assert do_algebra(operator, operand) == 1