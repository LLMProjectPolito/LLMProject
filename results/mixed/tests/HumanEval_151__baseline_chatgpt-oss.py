import copy
import pytest

# Import the function under test.
# Adjust the import path if the implementation lives in a different module.
from solution import double_the_difference


@pytest.mark.parametrize(
    "input_list, expected",
    [
        # Basic mixed list (example from the docstring)
        ([1, 3, 2, 0], 10),
        # Only negative numbers – all ignored
        ([-1, -2, -3, -4], 0),
        # Mix of positive odds and negatives
        ([9, -2], 81),
        # Single zero – even, contributes 0
        ([0], 0),
        # Empty list
        ([], 0),
        # All odds
        ([1, 5, 7, 11], 1**2 + 5**2 + 7**2 + 11**2),
        # All evens (including zero)
        ([2, 4, 6, 0], 0),
        # Large numbers to check for overflow handling (Python ints are unbounded)
        ([101, 202, 303], 101**2 + 303**2),
        # Floats that are mathematically odd but not integers – should be ignored
        ([1.0, 3.5, 5.0, -7.0], 1.0**2 + 5.0**2),  # only integer‑type values count
        # Mixed types: strings, None, bools (bool is subclass of int, treat as int)
        (["1", None, True, False, 3], 3**2 + True**2),  # True == 1 (odd), False == 0 (even)
        # List containing a bool – bool is an int subclass, 1 is odd, 0 is even
        ([True, False, 2, 3], 1**2 + 3**2),
    ],
)
def test_double_the_difference_various_inputs(input_list, expected):
    """
    Verify that `double_the_difference` returns the correct sum of squares
    for a wide variety of inputs.
    """
    # Keep a copy to ensure the function does not mutate the original list
    original = copy.deepcopy(input_list)

    result = double_the_difference(input_list)

    assert result == expected, f"Expected {expected} but got {result}"
    # The function must not modify the caller's list
    assert input_list == original


def test_input_is_not_a_list():
    """
    The function is documented to accept a list. Supplying a non‑list
    (e.g., a tuple) should raise a TypeError rather than silently succeed.
    """
    with pytest.raises(TypeError):
        double_the_difference((1, 3, 5))  # tuple, not list


def test_ignores_non_integer_numbers():
    """
    Floats that are whole numbers (e.g., 2.0) are *not* instances of int,
    so they must be ignored even if their value is odd.
    """
    lst = [2.0, 3.0, 4.5, -1.0]  # only 3.0 is an odd *value* but not an int
    assert double_the_difference(lst) == 0


def test_negative_and_non_integer_combination():
    """
    A list mixing negative integers, positive odds, and non‑integers.
    Only the positive odd integers should contribute.
    """
    lst = [-5, -3, -1, 0, 2, 4, 6, 7, 8.0, 9.5, 11]
    # Expected: 7 and 11 are the only odd ints ≥0
    expected = 7**2 + 11**2
    assert double_the_difference(lst) == expected


def test_large_input_performance():
    """
    Ensure the function works correctly on a large list (e.g., 10 000 elements)
    without raising errors or taking excessive time.
    """
    large_list = list(range(10000))  # 0 … 9999
    # Compute expected sum of squares of odd, non‑negative ints
    expected = sum(i * i for i in large_list if i % 2 == 1)
    assert double_the_difference(large_list) == expected