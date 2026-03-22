import pytest

# Assume the function is defined elsewhere and imported here.
# For example: from my_module import generate_integers
from solution import generate_integers


@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Simple ascending range with both even and odd numbers
        (2, 8, [2, 4, 6, 8]),
        # Same range but descending order – result must still be ascending
        (8, 2, [2, 4, 6, 8]),
        # No even numbers in the interval
        (10, 14, []),
        # Single number that is even
        (4, 4, [4]),
        # Single number that is odd
        (5, 5, []),
        # Mixed range where only the lower bound is even
        (2, 3, [2]),
        # Mixed range where only the upper bound is even
        (3, 4, [4]),
        # Range that starts and ends with odd numbers but contains evens inside
        (3, 9, [4, 6, 8]),
        # Large range to ensure function scales and still returns sorted output
        (1, 20, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),
        # Edge case: lower bound is 1 (odd) and upper bound is 2 (even)
        (1, 2, [2]),
        # Edge case: lower bound is 2 (even) and upper bound is 1 (odd) – descending order
        (2, 1, [2]),
        # Very large numbers (performance‑wise we just check correctness)
        (999_990, 1_000_010, [999_990, 999_992, 999_994, 999_996, 999_998, 1_000_000, 1_000_002, 1_000_004, 1_000_006, 1_000_008, 1_000_010]),
    ],
)
def test_generate_integers_various_cases(a, b, expected):
    """Validate generate_integers across a spectrum of typical and edge cases."""
    result = generate_integers(a, b)
    assert result == expected, f"Failed for inputs ({a}, {b})"


def test_result_is_new_list():
    """Ensure the function returns a new list object each call."""
    first = generate_integers(2, 8)
    second = generate_integers(2, 8)
    assert first == second
    assert first is not second  # distinct objects


def test_invalid_input_type():
    """If non‑integer types are passed, a TypeError should be raised."""
    with pytest.raises(TypeError):
        generate_integers("a", 5)
    with pytest.raises(TypeError):
        generate_integers(5, None)


def test_negative_numbers_handling():
    """
    Although the specification mentions positive integers,
    the function should behave sensibly with negatives:
    it should treat the interval the same way (inclusive) and
    return even digits that fall within it.
    """
    assert generate_integers(-4, 2) == [-4, -2, 0, 2]
    assert generate_integers(2, -4) == [-4, -2, 0, 2]