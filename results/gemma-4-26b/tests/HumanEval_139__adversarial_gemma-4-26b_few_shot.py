
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

# Assuming the function is in a file named solution.py
# from solution import special_factorial

def test_special_factorial_happy_path():
    """Tests standard valid inputs provided in the specification."""
    assert special_factorial(1) == 1      # 1! = 1
    assert special_factorial(2) == 2      # 2! * 1! = 2 * 1 = 2
    assert special_factorial(3) == 12     # 3! * 2! * 1! = 6 * 2 * 1 = 12
    assert special_factorial(4) == 288    # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 12),
    (4, 288),
    (5, 34560), # 120 * 288 = 34560
])
def test_special_factorial_parametrized(n, expected):
    """Uses parametrization to efficiently test multiple valid integer inputs."""
    assert special_factorial(n) == expected

def test_special_factorial_boundary_zero():
    """
    The docstring states n > 0. 
    A robust implementation should handle n=0 by either raising a ValueError 
    or returning a specific value (like 1 or 0) depending on requirements.
    We test for ValueError here as it violates the 'n > 0' constraint.
    """
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_negative_input():
    """Tests that negative integers raise a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(-1)
    with pytest.raises(ValueError):
        special_factorial(-10)

@pytest.mark.parametrize("invalid_input", [
    (3.5),          # Float
    ("4"),          # String
    (None),         # NoneType
    ([4]),          # List
    (4.0),          # Float that looks like an int (should ideally be rejected if strict)
])
def test_special_factorial_type_safety(invalid_input):
    """
    Tests that the function raises a TypeError when non-integer 
    types are provided.
    """
    with pytest.raises(TypeError):
        special_factorial(invalid_input)

def test_special_factorial_large_input():
    """
    Tests the function with a larger input to ensure it handles 
    Python's arbitrary-precision integers correctly without overflow errors.
    """
    # n=10 is large enough to produce a massive number but small enough 
    # to run instantly.
    # 10! * 9! * ... * 1! is a very large number.
    result = special_factorial(10)
    assert isinstance(result, int)
    assert result > 0

def test_special_factorial_performance_check():
    """
    A basic smoke test for performance. 
    If the implementation is O(n^2) or worse due to repeated factorial 
    re-calculations, this might hang.
    """
    import time
    start_time = time.time()
    special_factorial(100)
    end_time = time.time()
    
    # Ensure it completes in a reasonable timeframe (e.g., < 1 second)
    assert end_time - start_time < 1.0