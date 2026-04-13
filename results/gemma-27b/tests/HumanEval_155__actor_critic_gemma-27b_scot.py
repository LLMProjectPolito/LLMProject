
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)
    even_count = 0
    odd_count = 0
    for digit in str(num):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

# STEP 1: REASONING
# The function `even_odd_count` calculates the number of even and odd digits in an integer.
# The review identified a redundant test (`test_leading_zeros`), a missing edge case (invalid input),
# and similar tests that can be parameterized.
# We need to remove the redundant test, correct the exception type in `test_invalid_input`,
# and combine `test_positive_digits` and `test_negative_number` into a parameterized test.

# STEP 2: PLAN
# 1. Remove `test_leading_zeros` and `test_mixed_large_number`.
# 2. Change `pytest.raises(ValueError)` to `pytest.raises(TypeError)` in `test_invalid_input`.
# 3. Combine `test_positive_digits` and `test_negative_number` into `test_positive_negative_digits` using pytest.mark.parametrize.

# STEP 3: CODE
@pytest.mark.parametrize("num, expected", [
    (12345, (2, 3)),
    (-12345, (2, 3)),
    (2468, (4, 0)),
    (13579, (0, 5)),
    (2, (1, 0)),
    (1, (0, 1)),
    (0, (1, 0)),
    (1234567890, (5, 5)),
])
def test_positive_negative_digits(num, expected):
    assert even_odd_count(num) == expected

def test_invalid_input():
    with pytest.raises(TypeError):
        even_odd_count("abc")