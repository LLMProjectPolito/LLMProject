import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(222) == (2, 2)
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(123456789) == (3, 3)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(1) == (1, 0)
    assert even_odd_count(2) == (2, 0)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(4) == (0, 0)
    assert even_odd_count(5) == (1, 0)
    assert even_odd_count(6) == (0, 1)
    assert even_odd_count(7) == (1, 0)
    assert even_odd_count(8) == (0, 0)
    assert even_odd_count(9) == (0, 1)
    assert even_odd_count(10) == (1, 0)
    assert even_odd_count(11) == (0, 1)
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(1234567890) == (3, 3)
    assert even_odd_count(12345678901) == (3, 3)
    assert even_odd_count(123456789012) == (3, 3)
    print("All tests passed")