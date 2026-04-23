
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

import pytest

@pytest.mark.parametrize("n, expected", [
    (1, 1),           # 1! = 1
    (2, 2),           # 2! * 1! = 2 * 1 = 2
    (3, 12),          # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),         # 4! * 3! * 2! * 1! = 24 * 12 = 288
    (5, 34560),       # 5! * 288 = 120 * 288 = 34560
])
def test_special_factorial_valid_cases(n, expected):
    """Tests the function with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_non_positive_input():
    """Tests that n <= 0 raises a ValueError as per the function definition."""
    with pytest.raises(ValueError):
        special_factorial(0)
    with pytest.raises(ValueError):
        special_factorial(-5)

@pytest.mark.parametrize("invalid_input", [
    (3.5),      # Float
    ("4"),      # String
    ([4]),      # List
    (None),     # NoneType
])
def test_special_factorial_invalid_types(invalid_input):
    """Tests that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(invalid_input)