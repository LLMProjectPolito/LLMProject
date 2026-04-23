
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

# STEP 1: REASONING
# The function `generate_integers(a, b)` needs to return a list of even integers
# between `a` and `b` (inclusive), sorted in ascending order.
# The range is inclusive, meaning `a` and `b` are included in the range.
# If there are no even numbers in the range, an empty list should be returned.
# The function should handle cases where `a` is greater than `b` gracefully,
# returning the same even numbers as if `b` were greater than `a`.

# Test cases:
# 1. a = 2, b = 8: Expected output [2, 4, 6, 8]
# 2. a = 8, b = 2: Expected output [2, 4, 6, 8]
# 3. a = 10, b = 14: Expected output []
# 4. a = 2, b = 2: Expected output [2]
# 5. a = 1, b = 1: Expected output []
# 6. a = 1, b = 2: Expected output [2]
# 7. a = 2, b = 1: Expected output [2]
# 8. a = 1, b = 3: Expected output [2]
# 9. a = 3, b = 1: Expected output [2]
# 10. a = 2, b = 4: Expected output [2, 4]
# 11. a = 4, b = 2: Expected output [2, 4]
# 12. a = 2, b = 10: Expected output [2, 4, 6, 8, 10]
# 13. a = 10, b = 2: Expected output [2, 4, 6, 8, 10]



# STEP 2: PLAN
# The test suite will include functions to test the following scenarios:
# - Basic cases with a and b in the range.
# - Cases where a > b.
# - Cases where there are no even numbers in the range.
# - Cases where a and b are equal.
# - Cases where a and b are adjacent.
# - Cases where a and b are separated by a few numbers.
# - Cases where a and b are larger numbers.

# STEP 3: CODE
import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_numbers = []
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_equal():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(1, 1) == []

def test_generate_integers_adjacent():
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 1) == [2]
    assert generate_integers(3, 4) == [4]
    assert generate_integers(4, 3) == [4]

def test_generate_integers_separated():
    assert generate_integers(2, 4) == [2, 4]
    assert generate_integers(4, 2) == [2, 4]
    assert generate_integers(2, 10) == [2, 4, 6, 8, 10]
    assert generate_integers(10, 2) == [2, 4, 6, 8, 10]

def test_generate_integers_larger_numbers():
    assert generate_integers(100, 104) == [100, 102, 104]
    assert generate_integers(104, 100) == [100, 102, 104]
    assert generate_integers(1000, 1002) == [1000, 1002]
    assert generate_integers(1002, 1000) == [1000, 1002]