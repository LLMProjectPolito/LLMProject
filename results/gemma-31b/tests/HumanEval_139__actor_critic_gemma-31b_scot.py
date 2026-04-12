
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

# The function special_factorial is assumed to be defined in the environment.
# def special_factorial(n):
#     ...

@pytest.mark.parametrize("n, expected", [
    (1, 1),             # 1! = 1
    (2, 2),             # 2! * 1! = 2 * 1 = 2
    (3, 12),            # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),           # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),         # 5! * 288 = 120 * 288 = 34560
    (6, 24883200),      # 6! * 34560 = 720 * 34560 = 24883200
])
def test_special_factorial_valid_inputs(n, expected):
    """Test the function with a range of valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """
    Test with a larger value (n=10) to verify correctness with 
    Python's arbitrary-precision integers.
    """
    # B(10) = 10! * 9! * ... * 1!
    expected_b10 = 6658606584104736550400000000
    assert special_factorial(10) == expected_b10

@pytest.mark.parametrize("invalid_n", [0, -1, -10])
def test_special_factorial_invalid_domain(invalid_n):
    """
    Test that inputs outside the defined domain (n > 0) raise a ValueError.
    """
    with pytest.raises(ValueError):
        special_factorial(invalid_n)

@pytest.mark.parametrize("invalid_type", ["4", 4.5, [4], None])
def test_special_factorial_invalid_type(invalid_type):
    """
    Test that non-integer inputs raise a TypeError.
    """
    with pytest.raises(TypeError):
        special_factorial(invalid_type)