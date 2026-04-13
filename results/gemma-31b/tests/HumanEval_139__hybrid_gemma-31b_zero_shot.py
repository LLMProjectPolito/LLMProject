
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
        raise ValueError("Input must be a positive integer greater than 0.")
    
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result

class TestSpecialFactorial:
    """Comprehensive test suite for the special_factorial function."""

    @pytest.mark.parametrize("n, expected", [
        (1, 1),              # 1! = 1
        (2, 2),              # 2! * 1! = 2
        (3, 12),             # 3! * 2! * 1! = 12
        (4, 288),            # 4! * 3! * 2! * 1! = 288
        (5, 34560),          # 5! * 4! * 3! * 2! * 1! = 34560
        (6, 24883200),       # 6! * 34560 = 24883200
    ])
    def test_known_values(self, n, expected):
        """Test the function against known calculated Brazilian factorials."""
        assert special_factorial(n) == expected

    def test_minimum_valid_input(self):
        """Test the lower boundary of the valid input range (n=1)."""
        assert special_factorial(1) == 1

    def test_large_value_dynamic(self):
        """Test a larger value by dynamically calculating the expected result."""
        n = 10
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert special_factorial(n) == expected

    def test_performance_stress(self):
        """Check if the function handles a moderately high n using Python's arbitrary precision integers."""
        n = 20
        try:
            result = special_factorial(n)
            assert isinstance(result, int)
            assert result > 0
        except Exception as e:
            pytest.fail(f"special_factorial({n}) raised an unexpected exception: {e}")

    @pytest.mark.parametrize("invalid_n", [0, -1, -5, -100])
    def test_non_positive_integers(self, invalid_n):
        """Ensure ValueError is raised for n <= 0."""
        with pytest.raises(ValueError, match="Input must be a positive integer"):
            special_factorial(invalid_n)

    @pytest.mark.parametrize("invalid_type", [3.5, "4", None, [5], {"n": 4}, {5}])
    def test_invalid_types(self, invalid_type):
        """Ensure TypeError is raised for non-integer inputs."""
        with pytest.raises(TypeError, match="Input must be an integer"):
            special_factorial(invalid_type)

    def test_mathematical_consistency(self):
        """
        Verify the recursive mathematical property: 
        special_factorial(n) = n! * special_factorial(n-1)
        """
        for n in range(2, 12):
            assert special_factorial(n) == math.factorial(n) * special_factorial(n - 1)