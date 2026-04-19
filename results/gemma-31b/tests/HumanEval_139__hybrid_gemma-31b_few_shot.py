
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

# --- Valid Input Tests ---

@pytest.mark.parametrize("n, expected", [
    (1, 1),             # 1! = 1
    (2, 2),             # 2! * 1! = 2
    (3, 12),            # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),           # 4! * 3! * 2! * 1! = 24 * 12 = 288
    (5, 34560),         # 5! * 288 = 120 * 288 = 34560
    (6, 24883200),      # 6! * 34560 = 720 * 34560 = 24,883,200
])
def test_special_factorial_valid_values(n, expected):
    """Tests a range of valid positive integers from base cases to larger growth values."""
    assert special_factorial(n) == expected

# --- Edge Case & Error Handling Tests ---

@pytest.mark.parametrize("invalid_input", [0, -1, -100])
def test_special_factorial_out_of_bounds(invalid_input):
    """
    Tests that inputs not satisfying n > 0 raise a ValueError.
    This ensures the function adheres to the defined mathematical constraints.
    """
    with pytest.raises(ValueError):
        special_factorial(invalid_input)

@pytest.mark.parametrize("wrong_type", ["4", 4.5, None, [], {}])
def test_special_factorial_type_safety(wrong_type):
    """Tests that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(wrong_type)