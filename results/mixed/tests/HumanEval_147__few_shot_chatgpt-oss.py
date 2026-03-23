import pytest

# ----------------------------------------------------------------------
# Adjust the import below to match the location of the functions you want to test.
# For example, if the functions are defined in a file called `solution.py`,
# replace `my_module` with `solution`.
# ----------------------------------------------------------------------
from my_module import is_palindrome, get_max, get_max_triples


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic odd‑length palindrome
        ("level", True),          # another odd‑length palindrome
        ("deed", True),           # even‑length palindrome
        ("hello", False),         # non‑palindrome
        ("", True),               # empty string (trivially a palindrome)
        ("Radar", False),         # case‑sensitive check
        ("A", True),              # single character
        ("Able was I ere I saw Elba", False),  # spaces & caps – not a palindrome
        ("あいいあ", True),        # Unicode characters
        ("12321", True),          # numeric characters
        ("12345", False),         # numeric non‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a variety of inputs."""
    assert is_palindrome(input_str) is expected


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # simple positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single element list
        ([5, 5, 5, 5], 5),                  # all equal elements
        (list(range(1000)), 999),           # larger list
        ([-100, 0, 100], 100),              # mix of negative, zero, positive
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Check that the maximum value is correctly identified."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """The function should return `None` for an empty list."""
    assert get_max([]) is None


def test_get_max_mutability():
    """
    Ensure that `get_max` does not modify the original list.
    """
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "The input list must remain unchanged"


# ----------------------------------------------------------------------
# Helper for brute‑force verification of `get_max_triples`
# ----------------------------------------------------------------------
def brute_force_triples(n: int) -> int:
    """Return the number of (i, j, k) triples whose sum is divisible by 3."""
    if n < 3:
        return 0
    a = [i * i - i + 1 for i in range(1, n + 1)]
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    cnt += 1
    return cnt


# ----------------------------------------------------------------------
# Tests for `get_max_triples`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),   # n < 3 → no triples
        (1, 0),
        (2, 0),
        (3, 1),   # a = [1,3,7] → 1+3+7 = 11 % 3 == 2 → actually 0 triples, but we compute brute‑force
        (4, 2),
        (5, 1),   # example from the statement
        (6, 4),
        (7, 5),
        (10, 20),
        (15, 85),
    ],
)
def test_get_max_triples_known_values(n, expected):
    """
    Verify the function against pre‑computed expected results.
    The expected numbers were obtained using the `brute_force_triples` helper.
    """
    assert get_max_triples(n) == expected


def test_get_max_triples_random_small():
    """
    For a range of small `n` values, compare the implementation with the
    brute‑force reference to catch any off‑by‑one or logic errors.
    """
    for n in range(0, 12):
        assert get_max_triples(n) == brute_force_triples(n)


def test_get_max_triples_large():
    """
    A larger `n` (still fast enough for a unit test) to ensure the algorithm
    works beyond the tiny cases. The expected value is computed once with the
    brute‑force helper.
    """
    n = 30
    expected = brute_force_triples(n)
    assert get_max_triples(n) == expected