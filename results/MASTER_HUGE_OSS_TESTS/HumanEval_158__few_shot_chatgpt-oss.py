import pytest

# ----------------------------------------------------------------------
# NOTE:
# The functions under test are assumed to be defined in a module named
# `solution.py` that lives in the same directory as this test file.
# If the module has a different name, replace `solution` with the correct
# module name.
# ----------------------------------------------------------------------
from solution import is_palindrome, get_max, find_max


# ----------------------------------------------------------------------
# Tests for `is_palindrome`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("radar", True),                # classic palindrome
        ("hello", False),               # simple non‑palindrome
        ("", True),                     # empty string – vacuously palindrome
        ("A", True),                    # single character
        ("RaceCar", False),             # case‑sensitive check
        ("12321", True),                # numeric palindrome
        ("12345", False),               # numeric non‑palindrome
        ("Able was I ere I saw Elba", False),  # spaces & mixed case → False
        ("😀🙃😀", True),               # Unicode characters (emoji)
        ("😀🙃😎", False),              # Unicode non‑palindrome
        ("  ", True),                   # two spaces – palindrome
        ("a b a", True),                # spaces are considered characters
    ],
)
def test_is_palindrome_various(input_str, expected):
    """Parametrized test covering typical, edge‑case and Unicode inputs."""
    assert is_palindrome(input_str) is expected


def test_is_palindrome_long_string():
    """A long palindrome should still be detected correctly."""
    long_pal = "a" * 1000 + "b" + "a" * 1000
    assert is_palindrome(long_pal) is True

    long_non_pal = "a" * 1000 + "b" + "c" + "a" * 999
    assert is_palindrome(long_non_pal) is False


# ----------------------------------------------------------------------
# Tests for `get_max`
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 3),                     # simple positive numbers
        ([-1, -5, -2], -1),                 # all negative numbers
        ([42], 42),                         # single‑element list
        ([0, 0, 0], 0),                     # all equal elements
        (list(range(1000)), 999),           # large list, increasing order
        (list(range(1000, 0, -1)), 1000),   # large list, decreasing order
        ([5, -10, 5, -10, 5], 5),           # duplicates
    ],
)
def test_get_max_various(arr, expected):
    """Parametrized test for typical and edge cases."""
    assert get_max(arr) == expected


def test_get_max_empty():
    """Empty list should return None (as per specification)."""
    assert get_max([]) is None


def test_get_max_mutability():
    """The function must not modify the original list."""
    original = [3, 1, 4, 1, 5]
    copy = original.copy()
    _ = get_max(original)
    assert original == copy, "Original list was mutated"


# ----------------------------------------------------------------------
# Tests for `find_max`
# ----------------------------------------------------------------------
def _unique_char_count(s: str) -> int:
    """Helper used only inside the test suite to verify expectations."""
    return len(set(s))


@pytest.mark.parametrize(
    "words,expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "bcd", "cde"], "abc"),          # tie → lexicographically first
        (["zzz", "yy", "x"], "zzz"),             # all unique counts = 1, pick first lexicographically
        (["ab", "aab", "abb"], "aab"),           # both "aab" and "abb" have 2 uniques, "aab" < "abb"
        (["", "a", "aa"], "a"),                  # empty string has 0 uniques
        (["😀🙃😀", "😀🙃😎", "😀"], "😀🙃😀"),   # Unicode handling, first has 2 uniques, second 3, third 1 → second wins
        (["12345", "112233", "123"], "12345"),   # digits, unique counts 5, 2, 3 → first wins
        (["same", "same"], "same"),              # duplicate entries, result is that word
        (["apple", "aple", "aplee"], "aple"),    # "aple" has 4 uniques, others have 4 as well but "aple" is lexicographically smallest
    ],
)
def test_find_max_various(words, expected):
    """Parametrized test covering normal operation, ties and Unicode."""
    assert find_max(words) == expected


def test_find_max_single_element():
    """A list with a single word should return that word."""
    assert find_max(["singleton"]) == "singleton"


def test_find_max_all_empty_strings():
    """When all entries are empty, the first empty string should be returned."""
    assert find_max(["", "", ""]) == ""


def test_find_max_mutates_input():
    """The function must not modify the original list."""
    words = ["abc", "defg", "hij"]
    copy = words.copy()
    _ = find_max(words)
    assert words == copy, "Input list was mutated"


def test_find_max_invalid_input():
    """If the input is not iterable, a TypeError should be raised."""
    with pytest.raises(TypeError):
        find_max(None)          # type: ignore[arg-type]
    with pytest.raises(TypeError):
        find_max(123)           # type: ignore[arg-type]