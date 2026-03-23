import pytest

# Assume the function is imported from the module where it is defined.
# Replace `your_module` with the actual module name if needed.
from your_module import do_algebra


@pytest.mark.parametrize(
    "operators, operands, expected",
    [
        # Simple addition
        (["+"], [1, 2], 3),
        # Mixed precedence: addition, multiplication, subtraction
        (["+", "*", "-"], [2, 3, 4, 5], 9),
        # Floor division after addition
        (["//", "+"], [7, 2, 3], 6),  # 7//2 + 3 = 3 + 3 = 6
        # Exponentiation then addition
        (["**", "+"], [2, 3, 4], 12),  # 2**3 + 4 = 8 + 4 = 12
        # All operators together, respecting Python precedence
        (["+", "-", "*", "//", "**"], [10, 5, 2, 8, 3, 2], 14),
        # Zero operand with multiplication
        (["*", "+"], [0, 5, 6], 6),  # 0*5 + 6 = 6
        # Large exponentiation
        (["**"], [2, 10], 1024),
        # Single operator (subtraction)
        (["-"], [10, 4], 6),
    ],
)
def test_do_algebra_correct_results(operators, operands, expected):
    """Test normal and edge arithmetic cases."""
    assert do_algebra(operators, operands) == expected


def test_do_algebra_division_by_zero():
    """Floor division by zero should raise ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(["//"], [5, 0])


def test_do_algebra_mismatched_lengths():
    """
    The function expects len(operators) == len(operands) - 1.
    Supplying mismatched lengths should raise an exception (ValueError or IndexError).
    """
    with pytest.raises(Exception):
        do_algebra(["+", "-"], [1, 2])  # operators length 2, operands length 2


def test_do_algebra_non_negative_operands():
    """
    Operands are defined as non‑negative. Supplying a negative operand should raise an error.
    """
    with pytest.raises(Exception):
        do_algebra(["+"], [-1, 5])