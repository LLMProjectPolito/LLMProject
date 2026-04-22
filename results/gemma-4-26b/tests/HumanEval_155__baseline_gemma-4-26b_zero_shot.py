
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),          # Mixed positive: 1(O), 2(E), 3(O)
    (-12, (1, 1)),          # Mixed negative: 1(O), 2(E)
    (0, (1, 0)),            # Zero: 0 is even
    (2, (1, 0)),            # Single even digit
    (3, (0, 1)),            # Single odd digit
    (2468, (4, 0)),         # All even digits
    (1357, (0, 4)),         # All odd digits
    (10, (1, 1)),           # Zero as a digit (even)
    (-10, (1, 1)),          # Negative with zero digit
    (123456789, (4, 5)),    # Large mixed positive
    (987654321, (4, 5)),    # Large mixed negative-style sequence
    (11111, (0, 5)),        # Multiple odd digits
    (22222, (5, 0)),        # Multiple even digits
    (10203, (3, 2)),        # Mixed with multiple zeros: 1(O), 0(E), 2(E), 0(E), 3(O)
])
def test_even_odd_count(num, expected):
    """
    Tests the even_odd_count function with various integer inputs including
    positive, negative, zero, single-digit, and multi-digit numbers.
    """
    assert even_odd_count(num) == expected

def test_even_odd_count_large_integer():
    """Tests the function with a very large integer."""
    large_num = 24680135792468013579
    # Even digits: 2,4,6,8,0,2,4,6,8,0 (10)
    # Odd digits: 1,3,5,7,9,1,3,5,7,9 (10)
    assert even_odd_count(large_num) == (10, 10)