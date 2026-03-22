import pytest
import math


# Focus: Boundary Values
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
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result *= factorial
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@pytest.mark.parametrize("n", [1])
def test_special_factorial_boundary_1(n):
    assert special_factorial(n) == 1

@pytest.mark.parametrize("n", [2])
def test_special_factorial_boundary_2(n):
    assert special_factorial(n) == 2

@pytest.mark.parametrize("n", [3])
def test_special_factorial_boundary_3(n):
    assert special_factorial(n) == 12

# Focus: Equivalence Partitioning
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
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    factorial_product = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        factorial_product *= factorial
    return factorial_product

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@pytest.mark.parametrize("n", [1])
def test_special_factorial_equivalence_partition_1(n):
    assert special_factorial(n) == 1

@pytest.mark.parametrize("n", [2])
def test_special_factorial_equivalence_partition_2(n):
    assert special_factorial(n) == 2

@pytest.mark.parametrize("n", [3])
def test_special_factorial_equivalence_partition_3(n):
    assert special_factorial(n) == 12

@pytest.mark.parametrize("n", [4])
def test_special_factorial_equivalence_partition_4(n):
    assert special_factorial(n) == 288

# Focus: Error Handling/Invalid Input
import pytest

def test_special_factorial_negative_input():
    """Test with a negative integer input."""
    with pytest.raises(ValueError) as excinfo:
        special_factorial(-1)
    assert "Input must be a positive integer." == str(excinfo.value)

def test_special_factorial_zero_input():
    """Test with zero as input."""
    with pytest.raises(ValueError) as excinfo:
        special_factorial(0)
    assert "Input must be a positive integer." == str(excinfo.value)

def test_special_factorial_non_integer_input():
    """Test with a non-integer input (float)."""
    with pytest.raises(TypeError) as excinfo:
        special_factorial(3.14)
    assert "Input must be an integer." == str(excinfo.value)