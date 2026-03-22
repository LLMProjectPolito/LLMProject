import copy
import pytest

# Import the function under test.
# Adjust the import path according to where `find_max` is defined.
# For example, if the implementation lives in `solution.py`:
# from solution import find_max
from find_max_module import find_max   # <-- replace with the actual module name


# ----------------------------------------------------------------------
# Helper data for parametrized tests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "words, expected",
    [
        # Basic examples from the problem statement
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),

        # Tie‑breaking by lexicographical order
        (["abc", "bca", "cab"], "abc"),          # all have 3 unique chars → "abc" is smallest
        (["zzz", "yy", "x"], "x"),               # each has 1 unique char → "x" is smallest

        # Mixed lengths and characters
        (["hello", "world", "python"], "python"),
        (["ab", "abcde", "abcd"], "abcde"),
        (["", "a", "aa"], "a"),                  # empty string has 0 unique chars

        # Unicode / non‑ASCII characters
        (["café", "naïve", "résumé"], "naïve"),
        (["😀😁", "😀😀", "😁😁"], "😀😁"),

        # Large input – ensure performance does not break correctness
        (["".join(chr(i) for i in range(1000)), "a"*1000, "b"*999 + "c"], "".join(chr(i) for i in range(1000))),
    ],
)
def test_find_max_basic(words, expected):
    """Validate correct output for a variety of normal inputs."""
    # Keep a copy to ensure the function does not mutate the original list
    original = copy.deepcopy(words)
    assert find_max(words) == expected
    assert words == original, "find_max should not modify the input list"


# ----------------------------------------------------------------------
# Edge‑case tests
# ----------------------------------------------------------------------
def test_empty_list_returns_empty_string():
    """An empty list should return an empty string (reasonable default)."""
    assert find_max([]) == ""


def test_list_with_non_string_elements_raises_type_error():
    """If the list contains non‑string items, a TypeError is expected."""
    with pytest.raises(TypeError):
        find_max(["valid", 123, None])


def test_input_is_not_iterable_raises_type_error():
    """Passing a non‑iterable (e.g., an int) should raise a TypeError."""
    with pytest.raises(TypeError):
        find_max(42)


def test_single_element_list():
    """A list with a single word should return that word unchanged."""
    assert find_max(["singleton"]) == "singleton"


def test_all_strings_identical():
    """When all strings are identical, that string is returned."""
    words = ["repeat", "repeat", "repeat"]
    assert find_max(words) == "repeat"


def test_strings_with_same_unique_count_but_different_lengths():
    """
    Ensure lexicographical tie‑breaking works even when lengths differ.
    Both "ab" and "ba" have 2 unique characters; "ab" is lexicographically smaller.
    """
    assert find_max(["ba", "ab", "aabbcc"]) == "ab"


def test_strings_containing_spaces_and_punctuation():
    """Spaces and punctuation count as characters for uniqueness."""
    words = ["a b c", "a,b,c", "abc"]
    # All have 3 unique non‑space characters, but "a b c" has a space → 4 unique chars
    assert find_max(words) == "a b c"


def test_case_sensitivity():
    """Upper‑case and lower‑case letters are distinct."""
    words = ["Aa", "aA", "AA"]
    # "Aa" and "aA" each have 2 unique chars; lexicographically "Aa" < "aA"
    assert find_max(words) == "Aa"


# ----------------------------------------------------------------------
# Performance‑related sanity check (not a strict benchmark)
# ----------------------------------------------------------------------
def test_large_number_of_strings():
    """
    Generate 10 000 strings where each successive string adds one new unique character.
    The last string should be selected.
    """
    base = "a"
    words = [base * i for i in range(1, 10001)]
    # Append a string with all unique characters (e.g., first 100 letters)
    unique = "".join(chr(ord("a") + i) for i in range(100))
    words.append(unique)

    assert find_max(words) == unique