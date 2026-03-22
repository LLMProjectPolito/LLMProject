import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `even_odd_count` takes an integer as input and returns a tuple containing the counts of even and odd digits.
# The input integer can be positive, negative, or zero.
# The function should handle single-digit numbers, multi-digit numbers, and zero correctly.
# The function should treat the absolute value of the input number.

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Positive numbers with even and odd digits (e.g., 12345)
# 2. Positive numbers with only even digits (e.g., 2468)
# 3. Positive numbers with only odd digits (e.g., 13579)
# 4. Negative numbers with even and odd digits (e.g., -12345)
# 5. Negative numbers with only even digits (e.g., -2468)
# 6. Negative numbers with only odd digits (e.g., -13579)
# 7. Zero (0)
# 8. Single-digit even number (e.g., 2)
# 9. Single-digit odd number (e.g., 1)
# 10. Large numbers (e.g., 1234567890)
# 11. Numbers with leading zeros (should be treated as strings, not octal)

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("num, expected", [
    (12345, (2, 3)),
    (2468, (4, 0)),
    (13579, (0, 5)),
    (-12345, (2, 3)),
    (-2468, (4, 0)),
    (-13579, (0, 5)),
    (0, (1, 0)),
    (2, (1, 0)),
    (1, (0, 1)),
    (1234567890, (5, 5)),
    (10203, (2, 3)),
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected

def test_negative_number():
    assert even_odd_count(-12) == (1, 1)

def test_large_number():
    assert even_odd_count(9876543210) == (5, 5)

def test_zero():
    assert even_odd_count(0) == (1, 0)