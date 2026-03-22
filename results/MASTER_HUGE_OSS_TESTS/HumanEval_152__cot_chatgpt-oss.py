import pytest
from copy import deepcopy

# Assume the function `compare` is imported from the module where it is defined.
# For example:
# from solution import compare

@pytest.mark.parametrize(
    "scores, guesses, expected",
    [
        # Basic examples from the docstring
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        # All correct guesses
        ([10, -5, 0], [10, -5, 0], [0, 0, 0]),
        # All incorrect guesses
        ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
        # Mixed positive and negative values
        ([-10, 20, -30], [10, -20, 30], [20, 40, 60]),
        # Single element cases
        ([0], [0], [0]),
        ([100], [0], [100]),
        # Empty input lists
        ([], [], []),
        # Very large integers
        ([10**12, -10**12], [10**12 - 1, -10**12 + 5], [1, 5]),
    ],
)
def test_compare_basic(scores, guesses, expected):
    """Test typical and edge‑case inputs for correct absolute differences."""
    # Keep copies to ensure the function does not mutate the inputs
    scores_copy = deepcopy(scores)
    guesses_copy = deepcopy(guesses)

    result = compare(scores, guesses)

    assert result == expected, "Returned list does not match expected differences"
    # Verify immutability of inputs
    assert scores == scores_copy, "Original scores list was mutated"
    assert guesses == guesses_copy, "Original guesses list was mutated"


def test_compare_length_mismatch():
    """If the two lists differ in length, the function should raise a ValueError."""
    scores = [1, 2, 3]
    guesses = [1, 2]  # shorter

    with pytest.raises(ValueError):
        compare(scores, guesses)


def test_compare_non_iterable_inputs():
    """Passing non‑iterable arguments should raise a TypeError."""
    with pytest.raises(TypeError):
        compare(123, [1, 2, 3])

    with pytest.raises(TypeError):
        compare([1, 2, 3], "not a list")