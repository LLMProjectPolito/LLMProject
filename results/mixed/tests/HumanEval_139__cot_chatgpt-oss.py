import math
import pytest

# Assume the implementation is imported from the module under test.
# Adjust the import path as needed (e.g., `from solution import special_factorial`).
from solution import special_factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),                     # 1! = 1
        (2, 2),                     # 2! * 1! = 2 * 1
        (3, 12),                    # 3! * 2! * 1! = 6 * 2 * 1
        (4, 288),                   # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1
        (5, 34_560),                # 5! * 4! * 3! * 2! * 1!
    ],
)
def test_special_factorial_known_values(n, expected):
    """Verify known small inputs produce the correct product."""
    assert special_factorial(n) == expected


def test_special_factorial_large_input():
    """Compare the result for a larger n with a reference implementation."""
    n = 10
    # Reference: product of factorials from 1 to n
    reference = 1
    for i in range(1, n + 1):
        reference *= math.factorial(i)

    assert special_factorial(n) == reference


@pytest.mark.parametrize(
    "invalid_input",
    [
        0,          # zero is not allowed (n > 0)
        -1,         # negative integer
        -10,        # another negative case
        3.5,        # non‑integer numeric type
        "5",        # string representation of a number
        None,       # NoneType
        [3],        # list containing an integer
        (2, 3),     # tuple
        True,       # bool is a subclass of int but semantically invalid here
    ],
)
def test_special_factorial_invalid_inputs(invalid_input):
    """The function should raise an exception for any input that is not a positive integer."""
    with pytest.raises(Exception):
        special_factorial(invalid_input)