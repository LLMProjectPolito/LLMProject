
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
    num_str = str(abs(num))  # Handle negative numbers
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


@pytest.mark.parametrize("input_num, expected_output", [
    (-12, (1, 1)),
    (123, (1, 2)),
    (0, (0, 0)),
    (22, (2, 0)),
    (11, (0, 2)),
    (-2, (1, 0)),
    (-1, (0, 1)),
    (10, (1, 1)),
    (120, (2, 0)),
    (12345, (2, 3)),
    (-12345, (2, 3)),
    (123456789, (4, 5)),
    (-123456789, (4, 5)),
    (1, (0, 1)),
    (-1, (0, 1)),
    (2, (1, 0)),
    (-2, (1, 0)),
])
def test_even_odd_count(input_num, expected_output):
    """Test cases for even_odd_count function."""
    assert even_odd_count(input_num) == expected_output

@pytest.mark.parametrize("input_num", [
    123,
    456,
    789,
    101,
    202,
    303,
    404,
    505,
    606,
    707,
    808,
    909,
    111,
    222,
    333,
    444,
    555,
    666,
    777,
    888,
    999,
    -1,
    -2,
    -3,
    -4,
    -5,
    -6,
    -7,
    -8,
    -9,
    0
])
def test_even_odd_count_various_inputs(input_num):
    """Test cases with various inputs, including negative numbers and zero."""
    assert even_odd_count(input_num) == (0, 0) if input_num == 0 else even_odd_count(input_num) == (0, 0) if input_num < 0 else even_odd_count(input_num) == (0, 0) if input_num > 0 else even_odd_count(input_num) == (0, 0)