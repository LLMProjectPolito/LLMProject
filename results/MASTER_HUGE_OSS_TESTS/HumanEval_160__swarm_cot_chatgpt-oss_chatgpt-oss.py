import pytest
import math  # Imported as required by the rules; may be used by do_algebra internally.

from your_module import do_algebra  # Replace 'your_module' with the actual module name.


def test_operator_precedence_exponentiation():
    """
    Verify that exponentiation has higher precedence than addition and subtraction.
    Expected evaluation: 2 + (3 ** 2) - 5 = 6
    """
    operators = ['+', '**', '-']
    operands = [2, 3, 2, 5]
    assert do_algebra(operators, operands) == 6


def test_operator_precedence_and_zero_division():
    """
    - Confirm standard operator precedence (multiplication before addition).
    - Ensure floor‑division by zero raises ZeroDivisionError.
    """
    # 2 + 3 * 4 should be evaluated as 2 + (3 * 4) = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Floor division by zero must raise an exception.
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])