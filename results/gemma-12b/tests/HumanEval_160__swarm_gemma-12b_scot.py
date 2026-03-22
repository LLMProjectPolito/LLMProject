import pytest
import math

def test_do_algebra_exponentiation_with_zero():
    """Test exponentiation with zero operand."""
    operator = ['**']
    operand = [2, 0]
    assert do_algebra(operator, operand) == 1