import pytest

# ----------------------------------------------------------------------
# Adjust the import below to match the location of `order_by_points`.
# For example, if the function lives in `solution.py` use:
#   from solution import order_by_points
# ----------------------------------------------------------------------
from solution import order_by_points


# ----------------------------------------------------------------------
# Helper utilities
# ----------------------------------------------------------------------
def digit_sum(n: int) -> int:
    """Utility that mirrors the logic expected by `order_by_points`."""
    return sum(int(d) for d in str(abs(n)))


# ----------------------------------------------------------------------
# Basic behaviour
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([], []),                                            # empty list
        ([5], [5]),                                          # single element
        ([12, 3, 45], [3, 12, 45]),                         # simple ascending sums
        ([-1, -11, 1, 11, -12], [-1, -11, 1, -12, 11]),      # example from docstring
        ([0, 10, -20, 5], [0, 5, 10, -20]),                 # zeros and negatives
        ([101, 110, 11, 20], [20, 11, 101, 110]),           # same digit‑sum, keep original order
    ],
)
def test_basic_cases(input_list, expected):
    """Validate the function against known expected outputs."""
    # make a copy to ensure the original list is not mutated
    original = list(input_list)
    result = order_by_points(input_list)

    assert result == expected, "Sorted output does not match expected order"
    # original list must stay unchanged (function should be pure)
    assert input_list == original, "Input list was modified in‑place"


# ----------------------------------------------------------------------
# Stability – items with identical digit sums must keep original order
# ----------------------------------------------------------------------
def test_stability_with_identical_sums():
    data = [23, 32, 41, 14, 5]          # digit sums: 5,5,5,5,5
    expected = data[:]                 # order must be unchanged
    assert order_by_points(data) == expected


# ----------------------------------------------------------------------
# Mixed positive / negative numbers with same digit sum
# ----------------------------------------------------------------------
def test_mixed_signs_preserve_index_order():
    data = [ -12, 21, -30, 3, -3 ]      # all have digit sum = 3
    # original indices: 0,1,2,3,4 → order must stay the same
    assert order_by_points(data) == data


# ----------------------------------------------------------------------
# Large random list – compare against a reference implementation
# ----------------------------------------------------------------------
def reference_sort(nums):
    """Reference implementation using Python's stable sort."""
    return sorted(nums, key=lambda x: digit_sum(x))

def test_random_large_input():
    import random
    random.seed(0)                     # deterministic for reproducibility
    data = [random.randint(-10_000, 10_000) for _ in range(1_000)]
    expected = reference_sort(data)
    assert order_by_points(data) == expected


# ----------------------------------------------------------------------
# Edge cases – very large integers
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "num",
    [
        10**18,                     # huge positive
        -10**18,                    # huge negative
        999999999999999999,         # many 9's
        -999999999999999999,
    ],
)
def test_large_integers(num):
    # With a single element the result must be a list containing that element
    assert order_by_points([num]) == [num]


# ----------------------------------------------------------------------
# Type safety – non‑integer elements should raise a TypeError
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "bad_input",
    [
        [1, "2", 3],
        [None, 5],
        [3.14, 2],
        [{"a": 1}, 2],
    ],
)
def test_invalid_types_raise(bad_input):
    with pytest.raises(TypeError):
        order_by_points(bad_input)