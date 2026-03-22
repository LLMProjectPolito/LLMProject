import pytest

# The function `find_max` is assumed to be imported from the module under test.
# from mymodule import find_max


@pytest.mark.parametrize(
    "words, expected",
    [
        # Basic examples from the problem statement
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        # Lexicographical tie‑break when unique‑char counts are equal
        (["abc", "bca", "cab"], "abc"),
        (["ab", "cd", "aabb"], "ab"),
        # Empty string handling
        (["", "a", "ab"], "ab"),
        # Unicode characters – lexicographic order follows Unicode code points
        (["áéí", "abc", "áé"], "abc"),
        # Single element list
        (["singleton"], "singleton"),
        # All strings have zero unique characters (empty strings)
        (["", "", ""], ""),
        # Large strings with many unique characters
        (["".join(chr(i) for i in range(32, 127)),  # all printable ASCII
          "".join(chr(i) for i in range(65, 91))],  # only uppercase letters
         "".join(chr(i) for i in range(32, 127))),
    ],
)
def test_find_max_basic(words, expected):
    """Test typical and edge cases for find_max."""
    # Preserve a copy to verify the function does not mutate the input list
    original = list(words)
    result = find_max(words)
    assert result == expected
    assert words == original, "find_max should not modify the input list"


def test_find_max_empty_list():
    """When the input list is empty, the function should return None (or a falsy value)."""
    result = find_max([])
    # The exact contract for an empty list is not defined; we accept None or empty string.
    assert result in (None, ""), "Expected None or empty string for empty input list"


def test_find_max_non_string_elements():
    """The function is expected to work with strings; non‑string elements should raise a TypeError."""
    with pytest.raises(TypeError):
        find_max(["valid", 123, "another"])


def test_find_max_mutability_of_strings():
    """Ensure that the strings themselves are not altered (strings are immutable, but check reference)."""
    words = ["abc", "defg"]
    result = find_max(words)
    # Strings are immutable; just verify the original strings are unchanged.
    assert words[0] == "abc"
    assert words[1] == "defg"
    assert result in words