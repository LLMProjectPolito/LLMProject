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
        raise ValueError("Input must be greater than 0")
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

@pytest.mark.parametrize("n", [1, 2])
def test_special_factorial_boundary_low(n):
    """Tests the function with the lowest valid boundary values."""
    assert special_factorial(n) == 1 if n == 1 else 2

@pytest.mark.parametrize("n", [3, 4, 5])
def test_special_factorial_boundary_mid(n):
    """Tests the function with mid-range boundary values."""
    assert special_factorial(n) == 12 if n == 3 else (288 if n == 4 else 34560)

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
    result = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result *= factorial
    return result

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function calculates a special factorial.  We need to test valid inputs
# and boundary conditions. Equivalence partitioning suggests partitioning
# the input domain into:
# 1. Valid positive integers (e.g., 1, 2, 3, 4, 5)
# 2. Invalid input (non-positive integers, e.g., 0, -1)

# STEP 2: PLAN - List test functions names and scenarios.
# test_special_factorial_valid: Tests valid positive integer inputs.
#   - Scenario 1: n = 1 (boundary)
#   - Scenario 2: n = 2
#   - Scenario 3: n = 3
#   - Scenario 4: n = 4 (example from docstring)
# test_special_factorial_invalid: Tests invalid inputs (non-positive integers).
#   - Scenario 1: n = 0
#   - Scenario 2: n = -1

# STEP 3: CODE - Write the high-quality pytest suite.
def test_special_factorial_valid():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560

def test_special_factorial_invalid():
    with pytest.raises(ValueError) as excinfo:
        special_factorial(0)
    assert "Input must be a positive integer." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        special_factorial(-1)
    assert "Input must be a positive integer." in str(excinfo.value)

# Focus: Error Handling/Invalid Input
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

    factorial = 1
    result = 1
    for i in range(1, n + 1):
        factorial *= i
        result *= factorial
    return result

def test_special_factorial_negative_input():
    """Test that ValueError is raised for negative input."""
    with pytest.raises(ValueError) as excinfo:
        special_factorial(-1)
    assert str(excinfo.value) == "Input must be a positive integer."

def test_special_factorial_zero_input():
    """Test that ValueError is raised for zero input."""
    with pytest.raises(ValueError) as excinfo:
        special_factorial(0)
    assert str(excinfo.value) == "Input must be a positive integer."

def test_special_factorial_non_integer_input():
    """Test that TypeError is raised for non-integer input."""
    with pytest.raises(TypeError):
        special_factorial(1.5)