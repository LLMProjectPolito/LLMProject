
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

# Assuming special_factorial is imported from your module
# from your_module import special_factorial

@pytest.mark.parametrize("n, expected", [
    (1, 1),          # Base case
    (2, 2),          # 2! * 1!
    (3, 12),         # 3! * 2! * 1!
    (4, 288),        # 4! * 3! * 2! * 1!
    (5, 34560),      # 5! * 4! * 3! * 2! * 1!
    (6, 24883200),   # Large value check
])
def test_special_factorial_success(n, expected):
    """Tests valid positive integer inputs (the 'happy path')."""
    assert special_factorial(n) == expected

@pytest.mark.parametrize("n", [0, -1, -5, -100])
def test_special_factorial_value_error(n):
    """Tests that inputs outside the valid domain (n > 0) raise ValueError."""
    with pytest.raises(ValueError):
        special_factorial(n)

@pytest.mark.parametrize("invalid_input", [
    "4",      # String
    4.5,      # Float
    None,     # NoneType
    [5],      # List
])
def test_special_factorial_type_error(invalid_input):
    """Tests that non-integer inputs raise TypeError."""
    with pytest.raises(TypeError):
        special_factorial(invalid_input)