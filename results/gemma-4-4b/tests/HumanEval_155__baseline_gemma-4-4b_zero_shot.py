
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
        (2468, (4, 0)),
        (13579, (0, 5)),
        (-1, (0, 1)),
        (1, (0, 1)),
        (12, (1, 1)),
        (-2, (1, 0)),
        (1010, (2, 2)),
        (9876543210, (5, 5)),
        (-9876543210, (5, 5)),
    ],
)
def test_even_odd_count_positive(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output

@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (-123, (1, 2)),
        (-456, (2, 3)),
        (-789, (0, 3)),
    ],
)
def test_even_odd_count_negative(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output

@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (10, (1, 1)),
        (20, (1, 0)),
        (11, (0, 2)),
        (22, (2, 0)),
    ],
)
def test_even_odd_count_zero(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output