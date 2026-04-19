
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

import pytest

# The function implementation is assumed to be available in the environment
# def find_max(words):
#     ...

@pytest.mark.parametrize("words, expected", [
    # Basic functionality from docstring
    (["name", "of", "string"], "string"), 
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    # Lexicographical tie-breaking
    (["pear", "apple"], "apple"),           # Both have 4 unique; 'apple' < 'pear'
    (["cat", "bat"], "bat"),               # Both have 3 unique; 'bat' < 'cat'
    (["abc", "def", "ghi"], "abc"),        # All 3 unique; 'abc' is first
    (["zzzz", "yyyy", "xxxx"], "xxxx"),    # All 1 unique; 'xxxx' is first
    # Unique count vs Length
    (["aaaaa", "abc"], "abc"),             # Length 5 (1 unique) vs Length 3 (3 unique)
    # General cases
    (["apple", "banana", "cherry"], "cherry"), # cherry(5), apple(4), banana(3)
])
def test_find_max_scenarios(words, expected):
    """Consolidated test for basic functionality, ties, and unique character priority."""
    assert find_max(words) == expected

def test_find_max_single_element():
    """Test with a list containing only one word."""
    assert find_max(["hello"]) == "hello"

def test_find_max_empty_list():
    """Test with an empty list. Defined behavior: return None."""
    assert find_max([]) is None

def test_find_max_null_input():
    """Test behavior when the input is None."""
    assert find_max(None) is None

def test_find_max_with_empty_strings():
    """Test behavior when the list contains empty strings."""
    assert find_max(["", "a"]) == "a"
    assert find_max(["", ""]) == ""

def test_find_max_whitespace():
    """Test that whitespace is counted as a unique character."""
    # "a b" has 3 unique characters ('a', ' ', 'b')
    # "ab" has 2 unique characters ('a', 'b')
    assert find_max(["a b", "ab"]) == "a b"

def test_find_max_case_sensitivity():
    """Test that case sensitivity is handled ('A' and 'a' are distinct)."""
    # "Aa" has 2 unique characters, "B" has 1
    assert find_max(["Aa", "B"]) == "Aa"

def test_find_max_special_characters():
    """Test with strings containing numbers or special characters."""
    # "123" (3 unique) vs "abc" (3 unique) -> "123" comes first lexicographically
    assert find_max(["abc", "123"]) == "123"