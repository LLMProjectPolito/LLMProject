
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
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
    (6, 24883200),
    (7, 125411328000),
])
def test_special_factorial_correctness(n, expected):
    """Test that special_factorial returns the correct Brazilian factorial for valid positive integers."""
    result = special_factorial(n)
    assert result == expected
    assert isinstance(result, int), f"Expected integer output for n={n}, but got {type(result)}"

def test_special_factorial_large_value():
    """Test the function with a larger integer to ensure it handles large integer growth."""
    # n=8: 8! * 7! * 6! * 5! * 4! * 3! * 2! * 1! = 5056584744960000
    assert special_factorial(8) == 5056584744960000

def test_special_factorial_invalid_type():
    """Test that the function raises a TypeError when provided with non-integer inputs."""
    with pytest.raises(TypeError):
        special_factorial("4")
    with pytest.raises(TypeError):
        special_factorial(4.5)
    with pytest.raises(TypeError):
        special_factorial(None)

def test_special_factorial_out_of_domain():
    """Test that the function raises a ValueError for integers n <= 0."""
    with pytest.raises(ValueError):
        special_factorial(0)
    with pytest.raises(ValueError):
        special_factorial(-1)
    with pytest.raises(ValueError):
        special_factorial(-10)