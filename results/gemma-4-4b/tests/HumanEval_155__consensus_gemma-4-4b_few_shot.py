
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
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (-12, (1, 1)),
        (123, (1, 2)),
        (0, (1, 0)),
        (222, (3, 0)),
        (111, (0, 3)),
        (12, (1, 1)),
        (-1, (0, 1)),
        (2, (1, 0)),
        (-2, (1, 0)),
        (1023, (2, 3)),
        (-9876, (4, 3)),
        (1100, (2, 2)),
        (-1100, (2, 2)),
        (1, (0, 1)),
        (-1, (0, 1)),
    ],
)
def test_even_odd_count(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output