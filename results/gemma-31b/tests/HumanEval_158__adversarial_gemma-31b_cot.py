
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

def test_provided_examples():
    """Test the examples provided in the docstring."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_tie_breaker():
    """Test that the lexicographically first word is returned when unique counts are equal."""
    # All have 3 unique characters: 'a', 'b', 'c'
    assert find_max(["cba", "abc", "bac"]) == "abc"
    # All have 2 unique characters
    assert find_max(["zz", "aa", "bb"]) == "aa"

def test_unique_count_priority():
    """Test that the number of unique characters takes priority over lexicographical order."""
    # 'zebra' has 5 unique, 'apple' has 4 unique. 'apple' is lexicographically smaller, but 'zebra' wins.
    assert find_max(["apple", "zebra"]) == "zebra"
    # 'banana' has 3 unique (b, a, n), 'cat' has 3 unique (c, a, t). 'banana' < 'cat'.
    assert find_max(["banana", "cat"]) == "banana"

def test_single_element_list():
    """Test a list containing only one string."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_empty_strings():
    """Test lists containing empty strings or only empty strings."""
    assert find_max(["", ""]) == ""
    assert find_max(["", "a"]) == "a"
    assert find_max(["a", ""]) == "a"

def test_case_sensitivity():
    """Test that unique character counting is case-sensitive (standard Python behavior)."""
    # 'Aa' has 2 unique characters, 'a' has 1.
    assert find_max(["Aa", "a"]) == "Aa"
    # 'A' and 'a' are different; 'A' comes before 'a' lexicographically.
    assert find_max(["a", "A"]) == "A"

def test_special_characters_and_numbers():
    """Test strings with numbers and symbols."""
    # '123' (3 unique), 'abc' (3 unique). '123' < 'abc'.
    assert find_max(["abc", "123"]) == "123"
    # '!!!' (1 unique), '???' (1 unique). '!!!' < '???'.
    assert find_max(["???", "!!!"]) == "!!!"

def test_large_strings():
    """Test with longer strings to ensure efficiency and correctness."""
    s1 = "abcdefghijklmnopqrstuvwxyz" # 26 unique
    s2 = "abcdefghijklmnopqrstuvwxy"  # 25 unique
    s3 = "bcdefghijklmnopqrstuvwxyz"  # 26 unique
    # s1 and s3 both have 26, s1 is lexicographically smaller.
    assert find_max([s1, s2, s3]) == s1

def test_empty_list():
    """Test behavior with an empty list. 
    Depending on implementation, this might raise an error or return None.
    We test for common failure modes.
    """
    try:
        result = find_max([])
        # If it doesn't crash, it should probably return None or an empty string
        assert result in [None, ""]
    except (ValueError, IndexError):
        # Some implementations might raise these; as a QA, we note this behavior.
        pass