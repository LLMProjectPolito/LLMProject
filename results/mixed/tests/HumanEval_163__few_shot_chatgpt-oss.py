import pytest

# ----------------------------------------------------------------------
# is_palindrome ---------------------------------------------------------
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),          # classic palindrome
        ("hello", False),         # simple non‑palindrome
        ("", True),               # empty string is a palindrome
        ("a", True),              # single character
        ("RaceCar", False),       # case‑sensitive check
        ("Able was I ere I saw Elba", False),  # spaces & case make it false
        ("12321", True),          # numeric palindrome
        ("123321", True),         # even length palindrome
        ("😀🙃😀", True),          # Unicode characters
        ("😀🙃😎", False),         # Unicode non‑palindrome
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Validate palindrome detection across a variety of inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_mutation():
    """Ensure the function does not mutate the original string."""
    s = "radar"
    _ = is_palindrome(s)
    assert s == "radar"


# ----------------------------------------------------------------------
# get_max ---------------------------------------------------------------
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                # typical positive numbers
        ([-1, -5, -2], -1),            # all negative numbers
        ([42], 42),                    # single element list
        ([0, 0, 0], 0),                # all zeros
        ([5, 5, 5, 5], 5),             # duplicates
        (list(range(-1000, 1001)), 1000),  # large range
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Check that get_max returns the correct maximum for non‑empty lists."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """The function should return None for an empty list."""
    assert get_max([]) is None


def test_get_max_none_input():
    """Passing None should raise a TypeError (consistent with list operations)."""
    with pytest.raises(TypeError):
        get_max(None)


# ----------------------------------------------------------------------
# generate_integers ------------------------------------------------------
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 8, [2, 4, 6, 8]),          # normal ascending range
        (8, 2, [2, 4, 6, 8]),          # descending range – order must be ascending
        (10, 14, []),                  # no even digits in the interval
        (1, 1, []),                    # single odd number
        (2, 2, [2]),                   # single even number
        (0, 5, [0, 2, 4]),             # includes zero (still even)
        (5, 0, [0, 2, 4]),             # descending with zero
        (7, 13, [8, 10, 12]),          # mixed odd/even bounds
        (100, 110, [100, 102, 104, 106, 108, 110]),  # larger numbers
    ],
)
def test_generate_integers_various(a, b, expected):
    """Check that generate_integers returns the correct even numbers."""
    result = generate_integers(a, b)
    assert result == expected
    # additional sanity checks
    assert all(isinstance(x, int) for x in result)
    assert result == sorted(result)          # must be ascending
    assert all(x % 2 == 0 for x in result)   # all numbers must be even


def test_generate_integers_invalid_type():
    """Non‑integer inputs should raise a TypeError."""
    with pytest.raises(TypeError):
        generate_integers("a", 5)
    with pytest.raises(TypeError):
        generate_integers(3, None)


def test_generate_integers_negative_input():
    """Even though the docstring says “positive”, the function should handle
    non‑positive values gracefully (treat them as normal integers)."""
    assert generate_integers(-4, 4) == [-4, -2, 0, 2, 4]


def test_generate_integers_large_range_performance():
    """A sanity check that the function works for a relatively large range
    without blowing up memory or time."""
    a, b = 1, 10_000
    result = generate_integers(a, b)
    # The result should contain exactly half of the numbers in the interval
    # (rounded up because 1 is odd).
    expected_len = (b - a) // 2 + 1
    assert len(result) == expected_len
    assert result[0] == 2
    assert result[-1] == b if b % 2 == 0 else b - 1