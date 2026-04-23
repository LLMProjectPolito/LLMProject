
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


@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (-12, (1, 1)),
        (123, (1, 2)),
        (0, (1, 0)),
        (2468, (4, 0)),
        (13579, (0, 5)),
        (1, (0, 1)),
        (-1, (0, 1)),
        (2, (1, 0)),
        (10101, (2, 3)),
        (-2020, (2, 2)),
        (9876543210, (5, 5)),
        (1111111111, (0, 10)),
        (-1234567890, (5, 5)),
        (123456789, (4, 5)),
        (-1000, (3, 0)),
        (1000, (1, 3)),
        (12, (1, 1)),
    ],
)
def test_even_odd_count_positive_numbers(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output


@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (-12, (1, 1)),
        (-123, (1, 2)),
        (-1, (0, 1)),
        (-2, (1, 0)),
        (-10101, (2, 3)),
        (-2020, (2, 2)),
        (-9876543210, (5, 5)),
        (-1111111111, (0, 10)),
        (-123456789, (4, 5)),
        (-1000, (3, 0)),
    ],
)
def test_even_odd_count_negative_numbers(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output


@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (0, (1, 0)),
    ],
)
def test_even_odd_count_zero(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output


@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (1000, (1, 3)),
        (123456789, (4, 5)),
    ],
)
def test_even_odd_count_edge_cases(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output

@pytest.mark.parametrize(
    "input_num",
    [1111111111, -1111111111, 1234567890, -1234567890, 1000000000, -1000000000],
)
def test_even_odd_count_large_numbers(input_num):
    assert even_odd_count(input_num) == (5, 5)