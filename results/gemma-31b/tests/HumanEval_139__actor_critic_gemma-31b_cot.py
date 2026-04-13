
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
import math

@pytest.mark.parametrize("n, expected", [
    (1, 1),               # 1! = 1
    (2, 2),               # 2! * 1! = 2 * 1 = 2
    (3, 12),              # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),             # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),           # 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560
    (6, 24883200),        # 6! * 34560 = 720 * 34560 = 24,883,200
])
def test_special_factorial_valid_inputs(n, expected):
    """Test the special_factorial function with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a larger value to ensure it handles large integer growth."""
    n = 10
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert special_factorial(n) == expected

@pytest.mark.parametrize("invalid_input", [
    (0),        # Domain is n > 0
    (-1),       # Negative integer
    (-10),      # Negative integer
])
def test_special_factorial_out_of_domain(invalid_input):
    """
    Test that inputs outside the specified domain (n > 0) raise a ValueError.
    """
    with pytest.raises(ValueError):
        special_factorial(invalid_input)

@pytest.mark.parametrize("bad_type", [
    ("5"),      # String
    (5.5),      # Float
    (None),     # NoneType
    ([5]),      # List
    (True),     # Boolean (subclass of int)
    (False),    # Boolean (subclass of int)
])
def test_special_factorial_type_safety(bad_type):
    """Test that non-integer inputs (including booleans) raise a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(bad_type)

def test_special_factorial_recursion_limit():
    """
    Test with a moderately large n to ensure the implementation does not 
    trigger a RecursionError and returns a valid integer.
    """
    # n=100 is large enough to test logic/recursion without causing 
    # performance bottlenecks or exceeding default recursion limits.
    n = 100
    result = special_factorial(n)
    assert isinstance(result, int)
    assert result > 0