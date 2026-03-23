import pytest

# Assuming the implementation is available as `sum_squares` in the import path.
# If the function lives in a module named `solution`, you would use:
# from solution import sum_squares
# For the purpose of this test suite we rely on the name being already importable.

def manual_sum_squares(lst):
    """Reference implementation used to compute the expected result."""
    total = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:               # square for multiples of 3 (including 0)
            total += val ** 2
        elif idx % 4 == 0:             # cube for multiples of 4 that are NOT multiples of 3
            total += val ** 3
        else:
            total += val
    return total


@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([], 0),                                 # empty list
        ([1, 2, 3], 6),                          # example from docstring
        ([-1, -5, 2, -1, -5], -126),             # example with negatives
        ([0], 0),                                # single zero (index 0 -> square)
        ([5], 25),                               # single element, index 0 -> square
        ([1, 2, 3, 4], 1**2 + 2 + 3 + 4**3),      # index 0 square, index 3 not special, index 4 cube
        ([1, 2, 3, 4, 5], 1**2 + 2 + 3 + 4 + 5**3), # index 4 cube
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
         # compute manually:
         # idx0 1^2=1, idx1 2, idx2 3, idx3 4^2=16, idx4 5^3=125,
         # idx5 6, idx6 7^2=49, idx7 8, idx8 9^3=729, idx9 10,
         # idx10 11, idx11 12^2=144, idx12 13
         1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 729 + 10 + 11 + 144 + 13),
    ],
)
def test_sum_squares_examples(input_list, expected):
    """Test the function against a variety of hand‑crafted cases."""
    assert sum_squares(input_list) == expected


def test_original_list_unchanged():
    """The function must not mutate the input list."""
    original = [1, -2, 3, 4, 5, 6, 7, 8]
    copy = original.copy()
    _ = sum_squares(original)
    assert original == copy, "The input list was modified by sum_squares"


@pytest.mark.parametrize(
    "size",
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20],
)
def test_randomized_against_reference(size):
    """Generate random integer lists and compare the result with the reference implementation."""
    import random

    random.seed(0)  # deterministic for reproducibility
    lst = [random.randint(-100, 100) for _ in range(size)]
    expected = manual_sum_squares(lst)
    assert sum_squares(lst) == expected


def test_large_numbers():
    """Verify that the function works with very large integers (Python handles big ints)."""
    big = 10**12
    lst = [big, big, big, big, big, big, big, big, big, big]
    # indices 0,3,6,9 are multiples of 3 -> square
    # indices 4,8 are multiples of 4 but not 3 -> cube
    expected = (
        big ** 2 +               # idx0
        big +                    # idx1
        big +                    # idx2
        big ** 2 +               # idx3
        big ** 3 +               # idx4
        big +                    # idx5
        big ** 2 +               # idx6
        big +                    # idx7
        big ** 3 +               # idx8
        big ** 2                 # idx9
    )
    assert sum_squares(lst) == expected