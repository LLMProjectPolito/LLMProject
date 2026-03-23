import pytest

# Import the functions to be tested.
# Adjust the module name if your implementation lives in a different file.
from solution import is_palindrome, get_max, order_by_points


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # classic palindrome
        ("hello", False),               # non‑palindrome
        ("", True),                     # empty string (trivially palindrome)
        ("a", True),                    # single character
        ("RaceCar", False),             # case‑sensitive check
        ("A man, a plan, a canal: Panama", False),  # punctuation & spaces (case‑sensitive)
        ("😀🙃😀", True),               # Unicode emoji palindrome
        ("12321", True),                # numeric palindrome
        ("123456", False),              # numeric non‑palindrome
        ("  ", True),                   # two spaces – same forwards/backwards
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_type_error():
    """The function expects a string; passing a non‑string should raise a TypeError."""
    with pytest.raises(TypeError):
        is_palindrome(123)          # type: ignore[arg-type]


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                # simple positive numbers
        ([-1, -5, -2], -1),            # all negative numbers
        ([], None),                    # empty list returns None
        ([42], 42),                    # single element list
        ([5, 5, 5], 5),                # duplicates
        ([-10, 0, 10, 20, -20], 20),   # mixed signs
        ([2**31 - 1, -2**31], 2**31 - 1),  # large integers (32‑bit boundary)
    ],
)
def test_get_max_various(arr, expected):
    """Parametrized test for typical, edge‑case and large‑value inputs."""
    assert get_max(arr) == expected


def test_get_max_mutability():
    """Ensure the original list is not altered by `get_max`."""
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "The input list should remain unchanged"


# ----------------------------------------------------------------------
# Tests for `order_by_points`
# ----------------------------------------------------------------------
def test_order_by_points_empty():
    assert order_by_points([]) == []


@pytest.mark.parametrize(
    "input_list,expected",
    [
        # basic ordering by digit sum
        ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
        # numbers with identical digit sum keep original order
        ([23, 32, 41, 14], [23, 32, 41, 14]),
        # zeros and single‑digit numbers
        ([0, 5, -5, 10, -10], [0, 5, -5, 10, -10]),
        # mixed positive/negative, larger values
        ([123, -321, 45, -54, 6], [6, 45, -54, 123, -321]),
        # repeated values
        ([7, 7, 7], [7, 7, 7]),
        # single element list
        ([999], [999]),
        # numbers where digit sum ties but original index matters
        ([19, 28, 37, 46], [19, 28, 37, 46]),  # all sum to 10, keep order
        # large numbers
        ([99999, 11111, -22222], [11111, -22222, 99999]),
    ],
)
def test_order_by_points_various(input_list, expected):
    """Parametrized test covering ordering rules, ties, negatives and large ints."""
    result = order_by_points(input_list)
    assert result == expected
    # Ensure a new list is returned (no in‑place modification)
    assert result is not input_list


def test_order_by_points_original_unchanged():
    """The function must not mutate the original list."""
    original = [12, 3, -21, 30]
    original_copy = original.copy()
    _ = order_by_points(original)
    assert original == original_copy


def test_order_by_points_digit_sum_correctness():
    """Explicitly verify that sorting is based on digit‑sum, not numeric value."""
    data = [101, 20, 11, -2]
    # digit sums: 101→2, 20→2, 11→2, -2→2 → all equal, so original order must be kept
    assert order_by_points(data) == data