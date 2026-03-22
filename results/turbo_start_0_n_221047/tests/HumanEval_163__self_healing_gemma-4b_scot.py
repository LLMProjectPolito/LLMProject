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
    result = []
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

### SCoT Steps:
# STEP 1: REASONING - The function `generate_integers(a, b)` should return a list of even digits between `a` and `b` (inclusive), sorted in ascending order.  The function should handle cases where `a > b`, where no even digits exist within the range, and where the input integers are single-digit numbers.
# STEP 2: PLAN -
#   - Test case 1: a < b, all even digits present.
#   - Test case 2: a > b, all even digits present.
#   - Test case 3: a < b, no even digits present.
#   - Test case 4: a == b, single digit number, even.
#   - Test case 5: a == b, single digit number, odd.
#   - Test case 6: a and b are single digits, a < b.
#   - Test case 7: a and b are single digits, a > b.
# STEP 3: CODE -
###
def test_generate_integers_a_less_than_b():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(4, 6) == [4, 6]
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(6, 4) == [4, 6]
    assert generate_integers(5, 1) == [2, 4]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []
    assert generate_integers(11, 13) == []
    assert generate_integers(10, 11) == []

def test_generate_integers_single_digit_even():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(6, 6) == [6]

def test_generate_integers_single_digit_odd():
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(5, 5) == []

def test_generate_integers_single_digits_a_less_than_b():
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 4) == [2, 4]

def test_generate_integers_single_digits_a_greater_than_b():
    assert generate_integers(2, 1) == [2]
    assert generate_integers(3, 2) == [2]
    assert generate_integers(4, 3) == [2, 4]