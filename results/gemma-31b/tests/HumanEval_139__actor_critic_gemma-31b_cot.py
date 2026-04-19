
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
    (2, 2),           # 2! * 1! = 2 * 1
    (3, 12),          # 3! * 2! * 1! = 6 * 2 * 1
    (4, 288),         # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1
    (5, 34560),       # 5! * 4! * 3! * 2! * 1! = 120 * 288
    (6, 24883200),    # 6! * 34560 = 720 * 34560
])
def test_special_factorial_standard_values(n, expected):
    """Test the function with standard positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """
    Test with a larger value to verify correctness of arbitrary-precision integers.
    special_factorial(10) = 10! * 9! * ... * 1!
    """
    expected = 6658606584104768000000000000
    assert special_factorial(10) == expected

@pytest.mark.parametrize("invalid_input", [
    (0),       # Boundary case: n > 0 is specified
    (-1),      # Negative integer
    (-10),     # Negative integer
])
def test_special_factorial_out_of_domain(invalid_input):
    """
    Test that the function raises a ValueError for inputs outside the 
    specified domain (n > 0).
    """
    with pytest.raises(ValueError):
        special_factorial(invalid_input)

@pytest.mark.parametrize("type_input", [
    (1.5),     # Float
    ("4"),     # String
    (None),    # NoneType
])
def test_special_factorial_invalid_types(type_input):
    """Test that the function raises a TypeError when provided with non-integer inputs."""
    with pytest.raises(TypeError):
        special_factorial(type_input)

def test_special_factorial_recursion_limit():
    """
    Verify that the implementation handles larger n without hitting 
    Python's default recursion limit (typically 1000).
    """
    try:
        # We don't need to check the exact value, just that it completes 
        # without a RecursionError.
        special_factorial(1000)
    except RecursionError:
        pytest.fail("special_factorial raised RecursionError; implementation should be iterative.")