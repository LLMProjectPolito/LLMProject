import pytest
from decimal import Decimal
import time

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
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1

    result = Decimal(1)
    for i in range(1, n + 1):
        factorial = Decimal(1)
        for j in range(1, i + 1):
            factorial *= Decimal(j)
        result *= factorial
    return result

@pytest.mark.parametrize("input_val, expected_output", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560),
])
def test_special_factorial_basic(input_val, expected_output):
    assert special_factorial(input_val) == expected_output

def test_special_factorial_zero():
    assert special_factorial(0) == 1

def test_special_factorial_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)

@pytest.mark.parametrize("n", [6, 7, 8, 9, 10])
def test_special_factorial_large(n):
    # Test with larger numbers.  Using Decimal to prevent overflow.
    if n == 6:
        assert special_factorial(n) == Decimal("4354560000")
    elif n == 7:
        assert special_factorial(n) == Decimal("125411328000000")
    elif n == 8:
        assert special_factorial(n) == Decimal("3991680000000000000000000")
    elif n == 9:
        assert special_factorial(n) == Decimal("199584000000000000000000000000")
    elif n == 10:
        assert special_factorial(n) == Decimal("1316818944000000000000000000000")

def test_special_factorial_very_large():
    # Test with a very large input to check for performance issues.
    start_time = time.time()
    special_factorial(12)
    end_time = time.time()
    assert end_time - start_time < 60  # Ensure it doesn't take excessively long

def test_special_factorial_intermediate_factorial():
    # Test the factorial calculation within the nested loop.
    n = 4
    result = special_factorial(n)
    
    # Calculate the expected result manually
    expected_factorial_1 = 1
    expected_factorial_2 = 2
    expected_factorial_3 = 6
    expected_factorial_4 = 24
    expected_result = expected_factorial_1 * expected_factorial_2 * expected_factorial_3 * expected_factorial_4
    
    assert result == expected_result