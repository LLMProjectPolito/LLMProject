
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
    """Comprehensive test suite for the special_factorial function."""

    @pytest.mark.parametrize("n, expected", [
        (1, 1),             # 1! = 1
        (2, 2),             # 2! * 1! = 2 * 1 = 2
        (3, 12),            # 3! * 2! * 1! = 6 * 2 * 1 = 12
        (4, 288),           # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
        (5, 34560),         # 5! * 288 = 120 * 288 = 34560
        (6, 24883200),      # 6! * 34560 = 720 * 34560 = 24883200
    ])
    def test_valid_inputs(self, n, expected):
        """Test known correct outputs for small positive integers."""
        assert special_factorial(n) == expected

    def test_large_value_dynamic(self):
        """Test a larger value by verifying it against a manual calculation loop."""
        n = 10
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert special_factorial(n) == expected

    def test_large_value_static(self):
        """Test a specific large value to ensure regression stability."""
        # 7! = 5040; 24883200 * 5040 = 125,411,328,000
        assert special_factorial(7) == 125411328000

    @pytest.mark.parametrize("invalid_n", [0, -1, -100])
    def test_non_positive_integers(self, invalid_n):
        """Test that non-positive integers raise a ValueError with the correct message."""
        with pytest.raises(ValueError, match="Input must be an integer greater than 0."):
            special_factorial(invalid_n)

    @pytest.mark.parametrize("invalid_type", [3.14, "4", None, [5], {"n": 5}])
    def test_invalid_types(self, invalid_type):
        """Test that non-integer inputs raise a TypeError with the correct message."""
        with pytest.raises(TypeError, match="Input must be an integer."):
            special_factorial(invalid_type)

    def test_mathematical_property(self):
        """Verify the recursive property: B(n) = n! * B(n-1)."""
        n = 10
        assert special_factorial(n) == math.factorial(n) * special_factorial(n - 1)