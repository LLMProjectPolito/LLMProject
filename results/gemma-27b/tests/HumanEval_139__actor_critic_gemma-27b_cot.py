import pytest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    Raises ValueError if n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result

def test_factorial_base_case():
    assert factorial(0) == 1

def test_factorial_small_number():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24

def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_special_factorial_positive():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(7) == 103219200
    assert special_factorial(8) == 40320 * 103219200
    assert special_factorial(9) == 362880 * 40320 * 103219200

def test_special_factorial_type_error():
    with pytest.raises(ValueError):
        special_factorial(1.5)
    with pytest.raises(ValueError):
        special_factorial("2")
    with pytest.raises(ValueError):
        special_factorial([2])

def test_special_factorial_negative_number():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_large_number():
    with pytest.raises(OverflowError):
        special_factorial(12)