
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

import pytest

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result *= factorial
    return result


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 288),
        (5, 34560),
        (6, 15511200),
        (7, 10378368000),
        (8, 622702080000),
        (9, 47900160000000),
    ],
)
def test_special_factorial_small_values(n, expected):
    assert special_factorial(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (7, 10378368000),
        (8, 622702080000),
        (9, 47900160000000),
    ],
)
def test_special_factorial_larger_values(n, expected):
    assert special_factorial(n) == expected


def test_special_factorial_invalid_input_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)


def test_special_factorial_invalid_input_zero():
    with pytest.raises(ValueError):
        special_factorial(0)