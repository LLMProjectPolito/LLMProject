
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

def test_find_max_basic():
    """Test the basic examples provided in the docstring."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_unique_counts():
    """Test cases where one word clearly has more unique characters."""
    assert find_max(["apple", "pear", "peach"]) == "peach"  # peach: 5, apple: 4, pear: 4
    assert find_max(["a", "ab", "abc"]) == "abc"
    assert find_max(["abcdef", "a"]) == "abcdef"

def test_find_max_lexicographical_tie():
    """Test that the function returns the lexicographically first word when unique counts are equal."""
    # All have 3 unique characters: 'abc', 'def', 'ghi'. 'abc' is smallest.
    assert find_max(["ghi", "def", "abc"]) == "abc"
    # All have 1 unique character: 'z', 'b', 'a'. 'a' is smallest.
    assert find_max(["z", "b", "a"]) == "a"
    # Tie between 'ball' (b,a,l) and 'call' (c,a,l). 'ball' is smaller.
    assert find_max(["call", "ball"]) == "ball"
    # unique counts: 'apple' (4), 'apply' (4), 'ample' (4)
    assert find_max(["apple", "apply", "ample"]) == "ample"

def test_find_max_varying_lengths():
    """Test words with different lengths but same number of unique characters."""
    # 'abc' (3 unique), 'aabbcc' (3 unique)
    # Lexicographically: 'aabbcc' < 'abc'
    assert find_max(["abc", "aabbcc"]) == "aabbcc"
    # 'abc' (3), 'aabbcc' (3), 'aaabbbccc' (3)
    # Lexicographically: 'aaabbbccc' < 'aabbcc' < 'abc'
    assert find_max(["abc", "aabbcc", "aaabbbccc"]) == "aaabbbccc"

def test_find_max_single_element():
    """Test a list with only one string."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_find_max_empty_strings():
    """Test lists containing empty strings."""
    assert find_max(["", ""]) == ""
    assert find_max(["", "a", ""]) == "a"
    assert find_max(["", "abc", ""]) == "abc"

def test_find_max_empty_list():
    """Test an empty list input (should raise ValueError as per standard max() behavior)."""
    with pytest.raises(ValueError):
        find_max([])

def test_find_max_special_characters():
    """Test strings containing numbers, spaces, and special characters."""
    # "123" (3), "!!!" (1), " @#" (3)
    # " @#" comes before "123" in ASCII/lexicographical order
    assert find_max(["123", "!!!", " @#"]) == " @#"
    # '123' (3), '!!!' (1), 'abc' (3)
    # Lexicographical: '123' < 'abc'
    assert find_max(["123", "!!!", "abc"]) == "123"

def test_find_max_case_sensitivity():
    """Test that the function treats uppercase and lowercase as distinct and follows ASCII order."""
    # "Aa" has 2 unique characters, "aa" has 1
    assert find_max(["aa", "Aa"]) == "Aa"
    # 'Apple' (4 unique), 'apple' (4 unique). 'Apple' < 'apple'
    assert find_max(["Apple", "apple"]) == "Apple"

def test_find_max_identical_words():
    """Test with a list of identical strings."""
    assert find_max(["test", "test", "test"]) == "test"

def test_find_max_large_input():
    """Test with a larger list of strings."""
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    # apple: 4, banana: 3, cherry: 5, date: 4, elderberry: 6, fig: 3, grape: 5
    assert find_max(words) == "elderberry"

@pytest.mark.parametrize("words, expected", [
    (["a", "b", "c"], "a"),
    (["zebra", "apple"], "zebra"), # zebra (5), apple (4)
    (["ab", "ba"], "ab"),
    (["abc", "def", "ghi"], "abc"),
    (["zyx", "wvu", "tsr"], "tsr"),
    (["test", "testing"], "testing"),
    (["dog", "cat"], "cat"), # both 3, 'cat' < 'dog'
    (["", " "], " "), # "" is 0 unique, " " is 1 unique
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected