import pytest

# The functions under test are assumed to be defined in the same module that pytest
# will import (e.g. `solution.py`).  If they live in a different file, replace the
# import below with the appropriate module name, e.g.:
# from my_module import is_palindrome, get_max, specialFilter
from __future__ import annotations

# ----------------------------------------------------------------------
# Palindrome tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # classic palindrome
        ("hello", False),               # simple non‑palindrome
        ("", True),                     # empty string – edge case
        ("A", True),                    # single character
        ("Able was I ere I saw ElbA", False),  # case‑sensitive, includes spaces
        ("12321", True),                # numeric palindrome
        ("123321", True),               # even length palindrome
        ("123456", False),              # longer non‑palindrome
        ("😀🙃😀", True),               # Unicode characters
        ("😀🙃😎", False),              # Unicode non‑palindrome
    ],
)
def test_is_palindrome_various(input_str: str, expected: bool) -> None:
    """Validate `is_palindrome` against a variety of inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_case_sensitivity() -> None:
    """Explicit test for case‑sensitivity (already covered in parametrize but kept for clarity)."""
    assert is_palindrome("Radar") is False
    assert is_palindrome("Radar".lower()) is True


# ----------------------------------------------------------------------
# get_max tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # normal positive list
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([0, 0, 0], 0),                     # duplicates of zero
        ([-10, 10, -20, 20], 20),           # mix of signs
        ([999999999, 1, 2], 999999999),     # very large integer
    ],
)
def test_get_max_various(arr: list[int], expected: int | None) -> None:
    """Check `get_max` returns the correct maximum for typical and edge cases."""
    assert get_max(arr) == expected


def test_get_max_empty() -> None:
    """Empty list should return None."""
    assert get_max([]) is None


def test_get_max_mutability() -> None:
    """Ensure the original list is not altered."""
    original = [5, 3, 9]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "Function must not modify the input list"


# ----------------------------------------------------------------------
# specialFilter tests
# ----------------------------------------------------------------------
def _count_special(nums: list[int]) -> int:
    """Helper that mirrors the specification – used to cross‑check the implementation."""
    def first_last_odd(n: int) -> bool:
        s = str(abs(n))          # ignore sign for digit extraction
        return int(s[0]) % 2 == 1 and int(s[-1]) % 2 == 1

    return sum(1 for n in nums if n > 10 and first_last_odd(n))


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([15, -73, 14, -15], 1),                     # example from the prompt
        ([33, -2, -3, 45, 21, 109], 2),              # example from the prompt
        ([], 0),                                     # empty list
        ([11, 13, 17, 19], 4),                       # all qualify (first & last odd, >10)
        ([20, 30, 40], 0),                           # none qualify (first/last even)
        ([101, 202, 303, 404, 505], 2),              # mixed – 101 and 505 qualify
        ([9, 10, 11], 1),                            # 11 qualifies, 9 & 10 do not (<=10)
        ([-11, -13, -17], 0),                        # negatives are excluded because of leading '-'
        ([1111111111], 1),                           # large number, first & last digit odd
    ],
)
def test_special_filter_various(nums: list[int], expected: int) -> None:
    """Validate `specialFilter` against a broad set of scenarios."""
    assert specialFilter(nums) == expected


def test_special_filter_consistency_with_helper() -> None:
    """Randomised cross‑check against a reference implementation."""
    import random

    for _ in range(200):
        # generate a list of random integers between -200 and 200
        lst = [random.randint(-200, 200) for _ in range(random.randint(0, 20))]
        assert specialFilter(lst) == _count_special(lst)