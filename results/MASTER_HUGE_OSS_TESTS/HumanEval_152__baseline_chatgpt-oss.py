import pytest

# The function under test is assumed to live in a module named `solution.py`.
# Adjust the import path if the implementation resides elsewhere.
from solution import compare


# ----------------------------------------------------------------------
# Helper fixtures
# ----------------------------------------------------------------------
@pytest.fixture
def sample_data():
    """Typical data used by several tests."""
    return {
        "scores":   [1, 2, 3, 4, 5, 1],
        "guesses":  [1, 2, 3, 4, 2, -2],
        "expected": [0, 0, 0, 0, 3, 3],
    }


# ----------------------------------------------------------------------
# Basic functional tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "scores, guesses, expected",
    [
        # Example from the problem statement
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        # All correct guesses
        ([10, 20, 30], [10, 20, 30], [0, 0, 0]),
        # No correct guesses
        ([5, 5, 5], [0, 0, 0], [5, 5, 5]),
        # Mixed positive and negative numbers
        ([-3, 0, 7, -2], [-1, 0, 10, -5], [2, 0, 3, 3]),
        # Floating‑point numbers (absolute difference works the same)
        ([1.5, 2.2, -3.3], [1.5, 0.0, -4.0], [0, 2.2, 0.7]),
        # Empty input – should return an empty list
        ([], [], []),
    ],
)
def test_compare_basic(scores, guesses, expected):
    """Validate that `compare` returns the correct absolute differences."""
    result = compare(scores, guesses)
    assert result == expected, f"Expected {expected}, got {result}"


# ----------------------------------------------------------------------
# Immutability tests
# ----------------------------------------------------------------------
def test_input_immutability(sample_data):
    """`compare` must not modify the original score or guess lists."""
    scores = sample_data["scores"][:]
    guesses = sample_data["guesses"][:]

    # Call the function
    _ = compare(scores, guesses)

    # Verify the inputs are unchanged
    assert scores == sample_data["scores"]
    assert guesses == sample_data["guesses"]


# ----------------------------------------------------------------------
# Error handling tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "scores, guesses, exc_type",
    [
        # Different lengths – the contract says the arrays are of equal length,
        # so a sensible implementation should raise an error.
        ([1, 2, 3], [1, 2], ValueError),
        ([1], [], ValueError),
        # Non‑numeric entries – the operation requires subtraction, so a TypeError
        # (or a subclass) is appropriate.
        (["a", "b"], ["c", "d"], TypeError),
        ([1, 2], [None, 3], TypeError),
    ],
)
def test_compare_invalid_input(scores, guesses, exc_type):
    """Check that inappropriate inputs raise the expected exceptions."""
    with pytest.raises(exc_type):
        compare(scores, guesses)


# ----------------------------------------------------------------------
# Performance / scalability test
# ----------------------------------------------------------------------
def test_compare_large_input():
    """A large input should still produce the correct result quickly."""
    size = 10_000
    scores = list(range(size))
    guesses = list(range(size - 1, -1, -1))  # reversed order

    # Expected: absolute difference between i and (size-1-i)
    expected = [abs(i - (size - 1 - i)) for i in range(size)]

    result = compare(scores, guesses)
    assert result == expected