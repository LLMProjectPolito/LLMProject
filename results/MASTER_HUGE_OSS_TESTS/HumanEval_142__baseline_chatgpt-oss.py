import copy
import pytest

# Adjust the import path according to where the implementation lives.
# If the function is defined in the same directory in a file called `solution.py`,
# the following import works.  Change `solution` to the appropriate module name
# if it differs.
from solution import sum_squares


@pytest.mark.parametrize(
    "lst, expected",
    [
        # basic examples from the doc‑string
        ([1, 2, 3], 6),                     # no index is 3 or 4 → unchanged sum
        ([], 0),                            # empty list
        ([-1, -5, 2, -1, -5], -126),        # mixed signs, index 3 is cubed
        # single element – index 0 is a multiple of both 3 and 4 → square
        ([7], 7 ** 2),
        # index 3 (multiple of 3) → square, index 4 (multiple of 4, not 3) → cube
        ([1, 2, 3, 4, 5], 1 + 2 + 3 + 4 ** 2 + 5 ** 3),
        # index 12 is multiple of both 3 and 4 → square takes precedence
        ([i for i in range(13)], sum(
            i ** 2 if idx % 3 == 0 else
            i ** 3 if idx % 4 == 0 else i
            for idx, i in enumerate(range(13))
        )),
        # larger random list – compare with a reference implementation
        (list(range(20)), sum(
            x ** 2 if i % 3 == 0 else
            x ** 3 if i % 4 == 0 else x
            for i, x in enumerate(range(20))
        )),
    ],
)
def test_sum_squares_correctness(lst, expected):
    """Check that the function returns the correct summed value."""
    # keep a copy to verify the original list is not mutated
    original = copy.deepcopy(lst)
    result = sum_squares(lst)
    assert result == expected
    assert lst == original, "The input list must remain unchanged"


def test_index_12_precedence():
    """
    Index 12 is a multiple of both 3 and 4.
    According to the specification the square operation (multiple of 3) wins.
    """
    lst = [0] * 13
    lst[12] = 2  # simple non‑zero value to see the effect
    # Expected: 2 squared = 4, all other entries are 0
    assert sum_squares(lst) == 4


def test_immutability_complex():
    """
    Ensure that even when many elements are transformed,
    the original list object and its contents stay untouched.
    """
    lst = [i for i in range(-5, 6)]  # [-5, -4, ..., 5]
    lst_copy = lst.copy()
    _ = sum_squares(lst)            # ignore the result
    assert lst == lst_copy           # list content unchanged
    assert lst is not lst_copy       # a new list was not created in‑place


@pytest.mark.parametrize(
    "bad_input",
    [
        [1, "a", 3],          # string inside list
        [None, 2, 3],         # None inside list
        [1.5, 2, 3],          # float inside list
        "not a list",         # completely wrong type
        123,                  # not iterable
    ],
)
def test_invalid_input_raises(bad_input):
    """
    The implementation is expected to raise a TypeError (or a subclass)
    when the input is not a list of integers.
    """
    with pytest.raises(TypeError):
        sum_squares(bad_input)