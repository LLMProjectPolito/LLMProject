
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
from solution import special_factorial

@pytest.mark.parametrize("n, expected", [
    (1, 1),               # 1! = 1
    (2, 2),               # 2! * 1! = 2 * 1 = 2
    (3, 12),              # 3! * 2! * 1! = 6 * 2 * 1 = 12
    (4, 288),             # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
    (5, 34560),           # 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560
    (6, 24883200),        # 6! * 5! * 4! * 3! * 2! * 1! = 720 * 34560 = 24883200
])
def test_special_factorial_valid_inputs(n, expected):
    """Test the special_factorial function with valid positive integers."""
    assert special_factorial(n) == expected

def test_special_factorial_large_value():
    """Test with a larger value to ensure it handles large integer growth."""
    # n=10: 10! * 9! * ... * 1!
    # 10! = 3,628,800
    # 9! = 362,880
    # 8! = 40,320
    # 7! = 5,040
    # 6! = 720
    # 5! = 120
    # 4! = 24
    # 3! = 6
    # 2! = 2
    # 1! = 1
    # Product = 665,860,658,410,473,600,000
    expected_10 = 665860658410473600000
    assert special_factorial(10) == expected_10

def test_special_factorial_type_consistency():
    """Ensure the return type is an integer."""
    result = special_factorial(3)
    assert isinstance(result, int)

@pytest.mark.parametrize("invalid_input", [
    (0),
    (-1),
    (-10),
])
def test_special_factorial_out_of_domain(invalid_input):
    """
    Test how the function handles inputs outside the specified domain (n > 0).
    Depending on implementation, it might raise a ValueError or return a specific value.
    This test documents the behavior for non-positive integers.
    """
    # Since the prompt specifies n > 0, we check if the function handles it gracefully.
    # If the implementation is strict, it should raise an exception.
    # If it's loose, it might return 1 or 0. 
    # We use a try-except or check for a specific expected behavior.
    try:
        result = special_factorial(invalid_input)
        # If it doesn't raise an error, we just ensure it doesn't crash.
        assert isinstance(result, (int, float))
    except (ValueError, TypeError):
        # Raising an error for invalid domain is also acceptable behavior.
        pass