
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
])
def test_special_factorial_valid_inputs(n, expected):
    """Tests the function with valid positive integers."""
    assert special_factorial(n) == expected

@pytest.mark.parametrize("n", [0, -1, -10, -100])
def test_special_factorial_non_positive_input(n):
    """Tests that the function raises ValueError for n <= 0."""
    with pytest.raises(ValueError):
        special_factorial(n)

@pytest.mark.parametrize("n", [3.5, "4", [4], None, 4.0])
def test_special_factorial_invalid_types(n):
    """Tests that the function raises TypeError for non-integer inputs."""
    with pytest.raises(TypeError):
        special_factorial(n)

def test_special_factorial_large_value_consistency():
    """
    Tests a slightly larger value to ensure no overflow issues 
    (though Python handles arbitrarily large integers).
    n=6: 6! * 34560 = 720 * 34560 = 24883200
    """
    assert special_factorial(6) == 24883200