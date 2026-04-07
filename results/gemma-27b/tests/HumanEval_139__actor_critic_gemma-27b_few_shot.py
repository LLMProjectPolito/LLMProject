
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

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288
    >>> special_factorial(5)
    34560

    The function will receive an integer as input and should return the special
    factorial of this integer.

    Note: This function can quickly lead to integer overflow for larger inputs.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    def factorial(num):
        if num == 0:
            return 1
        else:
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

    result = 1
    for i in range(n, 0, -1):
        result *= factorial(i)
    return result

def factorial(num):
    """Calculates the factorial of a non-negative integer."""
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result


def test_special_factorial_basic():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560

def test_special_factorial_edge_cases():
    with pytest.raises(ValueError):
        special_factorial(0)
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_larger_number():
    assert special_factorial(6) == 43545600
    assert special_factorial(7) == 6227020800
    assert special_factorial(8) == 103023535536000
    assert special_factorial(9) == 2092278988800000000  # Added test for n=9
    assert special_factorial(10) == 64023737057280000000000000 # Added test for n=10