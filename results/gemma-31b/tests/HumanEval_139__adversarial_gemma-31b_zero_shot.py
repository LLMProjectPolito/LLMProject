
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

# Assuming the function is defined in the same module or imported
# from the target module. 
# If testing an external file, use: from target_module import special_factorial

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be an integer greater than 0.")
    
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result

class TestSpecialFactorial:
    """Robust test suite for special_factorial function."""

    @pytest.mark.parametrize("n, expected", [
        (1, 1),            # 1! = 1
        (2, 2),            # 2! * 1! = 2 * 1 = 2
        (3, 12),           # 3! * 2! * 1! = 6 * 2 * 1 = 12
        (4, 288),          # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
        (5, 34560),        # 5! * 288 = 120 * 288 = 34560
        (6, 24883200),     # 6! * 34560 = 720 * 34560 = 24883200
    ])
    def test_correct_values(self, n, expected):
        """Test standard positive integers to ensure mathematical correctness."""
        assert special_factorial(n) == expected

    def test_large_input(self):
        """Test a larger input to ensure Python's arbitrary-precision integers handle it."""
        # 10! * 9! ... * 1! is a very large number, but should be computable
        # We verify it doesn't crash and returns a positive integer
        result = special_factorial(10)
        assert isinstance(result, int)
        assert result > 0

    @pytest.mark.parametrize("invalid_n", [0, -1, -100])
    def test_non_positive_integers(self, invalid_n):
        """Test that inputs <= 0 raise a ValueError as per the 'n > 0' constraint."""
        with pytest.raises(ValueError):
            special_factorial(invalid_n)

    @pytest.mark.parametrize("invalid_type", [3.14, "5", [5], None, {"n": 5}])
    def test_invalid_types(self, invalid_type):
        """Test that non-integer inputs raise a TypeError."""
        with pytest.raises(TypeError):
            special_factorial(invalid_type)

    def test_idempotency(self):
        """Ensure that calling the function multiple times with the same input yields the same result."""
        n = 4
        assert special_factorial(n) == special_factorial(n)

    def test_growth_rate(self):
        """Verify that special_factorial(n) is always greater than special_factorial(n-1) for n > 1."""
        assert special_factorial(5) > special_factorial(4)
        assert special_factorial(2) > special_factorial(1)