import pytest

# Adjust the import path according to where the `eat` function is defined.
# For example, if the function lives in a file named `solution.py`,
# you would use: `from solution import eat`
from solution import eat


@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        # Examples from the problem statement
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        # Need is zero – nothing more is eaten
        (5, 0, 10, [5, 10]),
        (0, 0, 0, [0, 0]),
        # No carrots left in stock
        (3, 5, 0, [3, 0]),
        # No carrots have been eaten yet
        (0, 5, 10, [5, 5]),
        (0, 12, 7, [7, 0]),
        # Need larger than remaining (partial eat)
        (500, 400, 200, [700, 0]),
        # Need exactly equals remaining
        (100, 250, 250, [350, 0]),
        # Edge of constraints
        (1000, 0, 0, [1000, 0]),
        (0, 1000, 1000, [1000, 0]),
    ],
)
def test_eat_various_cases(number, need, remaining, expected):
    """
    Verify that `eat` returns the correct total eaten carrots and remaining stock
    for a wide range of input combinations.
    """
    result = eat(number, need, remaining)
    assert result == expected, f"Failed for ({number}, {need}, {remaining})"


def test_return_type_and_structure():
    """
    The function must always return a list of exactly two integers.
    """
    result = eat(3, 4, 5)          # typical case
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 2, "Result list must contain exactly two elements"
    total, left = result
    assert isinstance(total, int), "First element (total) must be int"
    assert isinstance(left, int), "Second element (remaining) must be int"


def test_no_side_effects():
    """
    Ensure that the original arguments are not altered.
    (Integers are immutable, but this test documents the expectation.)
    """
    number = 7
    need = 9
    remaining = 12
    _ = eat(number, need, remaining)
    assert number == 7
    assert need == 9
    assert remaining == 12