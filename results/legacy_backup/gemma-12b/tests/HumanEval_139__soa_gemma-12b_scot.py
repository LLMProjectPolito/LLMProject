import pytest
from your_module import special_factorial  # Replace your_module

# STEP 1: REASONING
# The function `special_factorial(n)` calculates a special factorial based on the Brazilian factorial definition.
# The definition is n! * (n-1)! * (n-2)! * ... * 1! where n > 0.
# We need to test various scenarios including:
# - Base case: n = 1
# - Small values: n = 2, 3, 4
# - Larger values: n = 5, 6 (to check for potential overflow issues, though not explicitly required)
# - Edge case: n = 0 (should raise a ValueError, as the problem states n > 0)
# - Negative input: n < 0 (should raise a ValueError)

# STEP 2: PLAN
# Test functions:
# - test_base_case: Checks the base case when n = 1.
# - test_small_values: Checks for n = 2, 3, 4.
# - test_larger_values: Checks for n = 5, 6.
# - test_invalid_input_zero: Checks for n = 0, expecting a ValueError.
# - test_invalid_input_negative: Checks for n < 0, expecting a ValueError.

# STEP 3: CODE
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class TestSpecialFactorial:
    def test_base_case(self):
        assert special_factorial(1) == 1

    def test_small_values(self):
        assert special_factorial(2) == 2
        assert special_factorial(3) == 12
        assert special_factorial(4) == 288

    def test_larger_values(self):
        assert special_factorial(5) == 34560
        assert special_factorial(6) == 3628800

    def test_invalid_input_zero(self):
        with pytest.raises(ValueError):
            special_factorial(0)

    def test_invalid_input_negative(self):
        with pytest.raises(ValueError):
            special_factorial(-1)