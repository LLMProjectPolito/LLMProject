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

def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative():
    assert even_odd_count(-123) == (1, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (0, 0)

def test_even_odd_count_single_digit():
    assert even_odd_count(5) == (1, 0)

def test_even_odd_count_multiple_digits():
    assert even_odd_count(12345) == (2, 2)

def test_even_odd_count_large_number():
    assert even_odd_count(1234567890) == (4, 2)

def test_even_odd_count_with_leading_zeros():
    assert even_odd_count(102) == (2, 1)

def test_even_odd_count_negative_one():
    assert even_odd_count(-1) == (1, 1)

def test_even_odd_count_negative_two():
    assert even_odd_count(-2) == (1, 1)

def test_even_odd_count_negative_three():
    assert even_odd_count(-3) == (1, 1)

def test_even_odd_count_four():
    assert even_odd_count(4) == (2, 0)

def test_even_odd_count_five():
    assert even_odd_count(5) == (1, 1)

def test_even_odd_count_six():
    assert even_odd_count(6) == (2, 0)

def test_even_odd_count_seven():
    assert even_odd_count(7) == (1, 0)

def test_even_odd_count_eight():
    assert even_odd_count(8) == (2, 0)

def test_even_odd_count_nine():
    assert even_odd_count(9) == (1, 0)

def test_even_odd_count_ten():
    assert even_odd_count(10) == (1, 1)

def test_even_odd_count_negative_one():
    assert even_odd_count(-1) == (1, 1)

def test_even_odd_count_negative_two():
    assert even_odd_count(-2) == (1, 1)

def test_even_odd_count_negative_three():
    assert even_odd_count(-3) == (1, 1)

def test_even_odd_count_negative_four():
    assert even_odd_count(-4) == (2, 0)

def test_even_odd_count_negative_five():
    assert even_odd_count(-5) == (1, 1)

def test_even_odd_count_negative_six():
    assert even_odd_count(-6) == (2, 0)

def test_even_odd_count_negative_seven():
    assert even_odd_count(-7) == (1, 0)

def test_even_odd_count_negative_eight():
    assert even_odd_count(-8) == (2, 0)