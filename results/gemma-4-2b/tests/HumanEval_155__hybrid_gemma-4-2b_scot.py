
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
    num_str = str(abs(num))  # Convert to string and handle negative numbers
    even_count = 0
    odd_count = 0
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def test_positive_integer_even_odd_count():
    assert even_odd_count(12345) == (2, 3)

def test_negative_integer_even_odd_count():
    assert even_odd_count(-12) == (1, 1)

def test_zero_even_odd_count():
    assert even_odd_count(0) == (0, 0)

def test_single_digit_even_odd_count():
    assert even_odd_count(5) == (0, 1)

def test_large_positive_integer_even_odd_count():
    assert even_odd_count(1234567890) == (4, 5)

def test_all_even_digits_even_odd_count():
    assert even_odd_count(2468) == (4, 0)

def test_all_odd_digits_even_odd_count():
    assert even_odd_count(13579) == (0, 5)

def test_negative_integer_with_negative_sign_even_odd_count():
    assert even_odd_count(-123) == (1, 2)  # Expecting to ignore the negative sign.

def test_invalid_input_even_odd_count():
    with pytest.raises(TypeError):
        even_odd_count("123")



@pytest.mark.parametrize(
    "input_num, expected_output",
    [
        (-12, (1, 1)),
        (123, (1, 2)),
        (0, (0, 0)),
        (2222, (4, 0)),
        (1111, (0, 4)),
        (123456789, (4, 5)),
        (24680, (5, 0)),
        (13579, (0, 5)),
        (10, (1, 1)),
        (-10, (1, 1)),
        (1234567890, (4, 6)),
        (-1234567890, (4, 6)),
        (1, (0, 1)),
        (-1, (0, 1)),
        (2, (1, 0)),
        (-2, (1, 0)),
        (11, (1, 0)),
        (-11, (1, 0)),
        (12, (1, 1)),
        (-12, (1, 1)),
    ],
)
def test_even_odd_count_parametrize(input_num, expected_output):
    assert even_odd_count(input_num) == expected_output

@pytest.mark.insensitive
def test_even_odd_count_negative_sign(input_num):
    assert even_odd_count(input_num) == (1, 1)

@pytest.mark.insensitive
def test_even_odd_count_zero(input_num):
    assert even_odd_count(input_num) == (0, 0)

@pytest.mark.insensitive
def test_even_odd_count_only_even(input_num):
    assert even_odd_count(input_num) == (input_num.count(int(digit) for digit in str(input_num) if int(digit) % 2 == 0), 0)

@pytest.mark.insensitive
def test_even_odd_count_only_odd(input_num):
    assert even_odd_count(input_num) == (0, input_num.count(int(digit) for digit in str(input_num) if int(digit) % 2 != 0))

@pytest.mark.insensitive
def test_even_odd_count_mixed_digits(input_num):
    assert even_odd_count(input_num) == (input_num.count(int(digit) for digit in str(input_num) if int(digit) % 2 == 0), input_num.count(int(digit) for digit in str(input_num) if int(digit) % 2 != 0))

@pytest.mark.insensitive
def test_even_odd_count_single_digit(input_num):
    assert even_odd_count(input_num) == (0, 1) if int(input_num) % 2 != 0 else (1, 0)

@pytest.mark.insensitive
def test_even_odd_count_large_number(input_num):
    assert even_odd_count(input_num) == (input_num.count(int(digit) for digit in str(input_num) if int(digit) % 2 == 0), input_num.count(int(digit) for digit in str(input_num) if int(digit) % 2 != 0))