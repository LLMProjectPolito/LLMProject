
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
# Replace 'your_module' with the actual name of your file/module
from your_module import special_factorial

class TestSpecialFactorial:
    """
    A comprehensive suite of tests for the special_factorial function,
    covering correctness, mathematical properties, error handling, and scale.
    """

    @pytest.mark.parametrize("n, expected", [
        (1, 1),          # 1!
        (2, 2),          # 2! * 1!
        (3, 12),         # 3! * 2! * 1!
        (4, 288),        # 4! * 3! * 2! * 1!
        (5, 34560),      # 5! * 4! * 3! * 2! * 1!
        (6, 24883200),   # 6! * 5! * 4! * 3! * 2! * 1!
    ])
    def test_valid_inputs(self, n, expected):
        """Test the function with known valid positive integers."""
        assert special_factorial(n) == expected

    def test_recurrence_relation(self):
        """
        Verify the mathematical property: special_factorial(n) = special_factorial(n-1) * n!
        This ensures the logic holds for a range of values without hardcoding every result.
        """
        for n in range(2, 13):
            previous_val = special_factorial(n - 1)
            current_val = special_factorial(n)
            assert current_val == previous_val * math.factorial(n)

    @pytest.mark.parametrize("n", [0, -1, -10, -100])
    def test_non_positive_values(self, n):
        """Test that n <= 0 raises a ValueError as per the definition n > 0."""
        with pytest.raises(ValueError):
            special_factorial(n)

    @pytest.mark.parametrize("invalid_input", [3.5, "4", None, [5], {"n": 5}])
    def test_invalid_types(self, invalid_input):
        """Test that non-integer inputs raise a TypeError."""
        with pytest.raises(TypeError):
            special_factorial(invalid_input)

    def test_return_type_integrity(self):
        """Ensure the function returns a discrete integer, not a float."""
        result = special_factorial(4)
        assert isinstance(result, int), f"Expected int, got {type(result)}"
        assert not isinstance(result, float), "Result should not be a float"

    def test_large_value_growth(self):
        """
        Ensure the function handles the rapid growth of the Brazilian factorial.
        Python handles arbitrary precision integers, so we check if the 
        result for n=10 is a very large positive integer.
        """
        result = special_factorial(10)
        # n=10 is extremely large; we verify it is positive and exceeds a threshold
        assert result > 10**10
        assert isinstance(result, int)