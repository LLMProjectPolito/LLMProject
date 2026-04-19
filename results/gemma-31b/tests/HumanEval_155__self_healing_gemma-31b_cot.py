
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    for char in num_str:
        digit = int(char)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),        # Standard positive: 2 is even, 1 and 3 are odd
    (-12, (1, 1)),        # Negative number: 2 is even, 1 is odd
    (0, (1, 0)),          # Zero: 0 is even
    (2468, (4, 0)),       # All even
    (1357, (0, 4)),       # All odd
    (-246, (3, 0)),       # Negative all even
    (-135, (0, 3)),       # Negative all odd
    (102, (2, 1)),        # Zero inside positive: 0 and 2 are even, 1 is odd
    (-102, (2, 1)),       # Zero inside negative
    (1111, (0, 4)),       # Repeated odds
    (2222, (4, 0)),       # Repeated evens
    (123456789, (4, 5)),  # Large range
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected