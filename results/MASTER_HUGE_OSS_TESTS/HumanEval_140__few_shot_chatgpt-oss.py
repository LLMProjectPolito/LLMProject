import pytest

# The functions under test are assumed to live in a module named `solution`.
# Adjust the import path if the actual module name differs.
from solution import is_palindrome, get_max, fix_spaces


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                     # simple palindrome
        ("hello", False),                    # simple non‑palindrome
        ("", True),                          # empty string (edge case)
        ("Radar", False),                    # case‑sensitive check
        ("A", True),                         # single character
        ("Able was I ere I saw Elba", False),# spaces & mixed case – still False
        ("12321", True),                     # numeric palindrome
        ("12345", False),                    # numeric non‑palindrome
        ("😀🙃😀", True),                     # Unicode characters
        ("😀🙃😎", False),                    # Unicode non‑palindrome
        ("  ", True),                        # two spaces – palindrome by definition
        (" a ", True),                       # spaces around a single char
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_long_string():
    """A long palindrome should still be detected correctly."""
    long_pal = "step on no pets" * 10  # repeats a known palindrome phrase
    assert is_palindrome(long_pal) is True


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                      # normal positive list
        ([-1, -5, -2], -1),                  # all negative numbers
        ([42], 42),                          # single element list
        ([0, 0, 0], 0),                      # duplicates of the same value
        (list(range(1000)), 999),            # large list
        ([-10, 5, 5, -10], 5),               # duplicate max values
    ],
)
def test_get_max_normal_cases(arr, expected):
    """Check that `get_max` returns the correct maximum for typical inputs."""
    assert get_max(arr) == expected


def test_get_max_empty_list():
    """Empty list should return `None`."""
    assert get_max([]) is None


def test_get_max_mutable_input_not_modified():
    """`get_max` must not mutate the original list."""
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "The input list was altered by `get_max`"


# ----------------------------------------------------------------------
# Tests for `fix_spaces`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "text,expected",
    [
        ("Example", "Example"),                     # no spaces
        ("Example 1", "Example_1"),                 # single space → underscore
        (" Example 2", "_Example_2"),               # leading space → underscore
        (" Example   3", "_Example-3"),             # >2 spaces → hyphen
        ("A  B", "A_B"),                            # exactly two spaces → underscores
        ("A   B", "A-B"),                           # three spaces → hyphen
        ("A    B", "A-B"),                          # four spaces → hyphen (single hyphen)
        ("Multiple   spaces   here", "Multiple-spaces-here"),
        ("Trailing space ", "Trailing_space_"),    # trailing single space
        ("  Leading and  double  ", "_Leading_and_double_"),
        ("Mix of   single  and   triple", "Mix of-single_and-triple"),
        ("", ""),                                   # empty string
        ("   ", "-"),                               # only >2 spaces → single hyphen
        ("  ", "__"),                               # exactly two spaces → two underscores
    ],
)
def test_fix_spaces_various_cases(text, expected):
    """Parametrized test covering all documented behaviours and edge cases."""
    assert fix_spaces(text) == expected


def test_fix_spaces_multiple_runs():
    """String with several runs of spaces of different lengths."""
    src = "One  Two   Three    Four"
    # 2 spaces → "__", 3 spaces → "-", 4 spaces → "-"
    expected = "One__Two-Three-Four"
    assert fix_spaces(src) == expected


def test_fix_spaces_no_alteration_of_non_space_chars():
    """All non‑space characters must stay exactly the same."""
    src = "AbC!@#123"
    assert fix_spaces(src) == src


def test_fix_spaces_preserves_type_and_encoding():
    """The function should return a `str` object, even for Unicode input."""
    src = "Üñïçødé   test"
    result = fix_spaces(src)
    assert isinstance(result, str)
    assert result == "Üñïçødé-test"


# ----------------------------------------------------------------------
# Property‑based sanity checks (optional, requires hypothesis)
# ----------------------------------------------------------------------
try:
    from hypothesis import given, strategies as st

    @given(st.text())
    def test_fix_spaces_idempotent(text):
        """
        Applying `fix_spaces` twice should be the same as applying it once
        (the operation is idempotent).
        """
        assert fix_spaces(fix_spaces(text)) == fix_spaces(text)

    @given(st.lists(st.integers()))
    def test_get_max_consistency(arr):
        """
        For any integer list, `get_max` should either return None (empty)
        or the same value as Python's built‑in `max`.
        """
        assert (get_max(arr) is None) == (len(arr) == 0)
        if arr:
            assert get_max(arr) == max(arr)

except ImportError:
    # hypothesis is optional; the core tests above are sufficient.
    pass