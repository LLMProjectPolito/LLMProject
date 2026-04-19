
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

# The function find_max is assumed to be defined in the environment.
# We are testing the logic described in the problem statement.

@pytest.mark.parametrize("words, expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
])
def test_docstring_examples(words, expected):
    """Verify the examples provided in the function docstring."""
    assert find_max(words) == expected

@pytest.mark.parametrize("words, expected", [
    (["zebra", "apple"], "apple"), # Both have 5 unique chars, 'apple' < 'zebra'
    (["cat", "bat", "rat"], "bat"), # All have 3 unique chars, 'bat' is first alphabetically
    (["dog", "dig"], "dig"),       # All have 3 unique chars, 'dig' < 'dog'
])
def test_lexicographical_tie_break(words, expected):
    """Ensure that ties in unique character counts are broken by lexicographical order."""
    assert find_max(words) == expected

@pytest.mark.parametrize("words, expected", [
    (["aaaaa", "bbbb", "cccc"], "aaaaa"), # All have 1 unique char, 'aaaaa' is first
    (["zzzz", "yyyy", "xxxx"], "xxxx"),   # All have 1 unique char, 'xxxx' is first
])
def test_single_unique_char(words, expected):
    """Test strings that have only one unique character regardless of length."""
    assert find_max(words) == expected

def test_single_element_list():
    """Test a list containing only one string."""
    assert find_max(["hello"]) == "hello"

def test_empty_strings_in_list():
    """Test lists containing empty strings."""
    # "" has 0 unique chars, "a" has 1.
    assert find_max(["", "a", ""]) == "a"
    # All empty strings, should return the first one (lexicographically)
    assert find_max(["", "", ""]) == ""

def test_case_sensitivity():
    """Verify that case sensitivity is handled (A != a)."""
    # "Aa" has 2 unique characters, "a" has 1.
    assert find_max(["Aa", "a"]) == "Aa"
    # "Apple" (A, p, l, e) = 4; "apple" (a, p, l, e) = 4. 
    # "Apple" comes before "apple" in ASCII/Lexicographical order.
    assert find_max(["Apple", "apple"]) == "Apple"

def test_special_characters():
    """Verify behavior with numbers and symbols."""
    # "123" (3 unique), "!!!" (1 unique)
    assert find_max(["123", "!!!"]) == "123"
    # "a1" (2 unique), "b1" (2 unique) -> "a1" is first
    assert find_max(["b1", "a1"]) == "a1"

def test_empty_list():
    """
    Test behavior with an empty list. 
    Depending on implementation, this might raise an IndexError or return None.
    We check if it handles it gracefully or raises a predictable error.
    """
    with pytest.raises((IndexError, ValueError, TypeError)):
        # Most implementations using max() on an empty list raise ValueError
        find_max([])