import pytest
from your_module import special_factorial  # Replace your_module

# STEP 1: REASONING
# The function `special_factorial(n)` calculates a special factorial based on the Brazilian factorial definition.
# The input `n` is a positive integer.
# The output is an integer representing the calculated special factorial.
# We need to test various scenarios, including:
# - Base case: n = 1
# - Small values: n = 2, 3, 4
# - Larger values: n = 5, 6 (to check for potential overflow issues, though not explicitly required)
# - Edge case: n = 0 (should raise a ValueError, as the problem states n > 0)
# - Invalid input: n = -1 (should raise a ValueError)
# - Invalid input: n = 1.5 (should raise a TypeError)

# STEP 2: PLAN
# Test functions:
# - test_special_factorial_base_case: Checks the base case n = 1.
# - test_special_factorial_small_values: Checks n = 2, 3, 4.
# - test_special_factorial_larger_values: Checks n = 5, 6.
# - test_special_factorial_zero: Checks that ValueError is raised when n = 0.
# - test_special_factorial_negative: Checks that ValueError is raised when n is negative.
# - test_special_factorial_invalid_type: Checks that TypeError is raised when n is not an integer.


# STEP 3: CODE
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class TestSpecialFactorial:
    def test_special_factorial_base_case(self):
        assert special_factorial(1) == 1

    def test_special_factorial_small_values(self):
        assert special_factorial(2) == 2
        assert special_factorial(3) == 12
        assert special_factorial(4) == 288

    def test_special_factorial_larger_values(self):
        assert special_factorial(5) == 34560
        assert special_factorial(6) == 3628800

    def test_special_factorial_zero(self):
        with pytest.raises(ValueError):
            special_factorial(0)

    def test_special_factorial_negative(self):
        with pytest.raises(ValueError):
            special_factorial(-1)

    def test_special_factorial_invalid_type(self):
        with pytest.raises(TypeError):
            special_factorial(1.5)