
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

def test_special_factorial_basic():
    """Tests the example provided in the docstring and basic small integers."""
    assert special_factorial(1) == 1        # 1! = 1
    assert special_factorial(2) == 2        # 2! * 1! = 2 * 1 = 2
    assert special_factorial(3) == 12       # 3! * 2! * 1! = 6 * 2 * 1 = 12
    assert special_factorial(4) == 288      # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288

def test_special_factorial_larger_value():
    """Tests a slightly larger value to ensure the product accumulates correctly."""
    # 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560
    assert special_factorial(5) == 34560

@pytest.mark.parametrize("invalid_input", [0, -1, -10])
def test_special_factorial_non_positive_integers(invalid_input):
    """
    The docstring specifies n > 0. 
    Depending on implementation, this should either raise a ValueError 
    or handle it gracefully. A robust implementation should not enter an infinite loop.
    """
    with pytest.raises((ValueError, AssertionError)):
        special_factorial(invalid_input)

@pytest.mark.parametrize("wrong_type", [3.5, "5", [5], None])
def test_special_factorial_type_safety(wrong_type):
    """Ensures the function handles non-integer types by raising a TypeError."""
    with pytest.raises(TypeError):
        special_factorial(wrong_type)

def test_special_factorial_performance_large_n():
    """
    Tests that the function can handle a moderately large n without crashing.
    Python handles arbitrary precision integers, so we check for completion.
    """
    try:
        result = special_factorial(20)
        assert isinstance(result, int)
        assert result > 0
    except RecursionError:
        pytest.fail("special_factorial raised RecursionError; consider an iterative approach.")