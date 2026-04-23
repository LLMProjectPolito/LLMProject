
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

def test_find_max_provided_examples():
    """Tests the examples provided in the docstring."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_lexicographical_tie():
    """Tests that the lexicographically first word is returned when unique counts are tied."""
    # All have 3 unique characters: 'a', 'b', 'c'
    # Lexicographical order: "abc" < "acb" < "bac" < "bca" < "cab" < "cba"
    assert find_max(["cba", "abc", "bac"]) == "abc"
    
    # Tie in unique characters (4 each): 'a', 'p', 'l', 'e' vs 'a', 'p', 'l', 'y'
    # "apple" < "apply"
    assert find_max(["apply", "apple"]) == "apple"

def test_find_max_single_element():
    """Tests a list containing only one word."""
    assert find_max(["hello"]) == "hello"
    assert find_max(["a"]) == "a"

def test_find_max_empty_list():
    """Tests the behavior when an empty list is provided."""
    # Based on standard Python practices for 'find max' functions, 
    # we expect None or an empty string. Given the context, None is most likely.
    assert find_max([]) is None

def test_find_max_case_sensitivity():
    """Tests that character uniqueness and lexicographical order respect case sensitivity."""
    # 'A' (ASCII 65) comes before 'a' (ASCII 97)
    # Both have 1 unique character
    assert find_max(["a", "A"]) == "A"
    
    # "Aa" has 2 unique characters, "aa" has 1
    assert find_max(["aa", "Aa"]) == "Aa"

def test_find_max_different_lengths_same_unique():
    """Tests words with different lengths but the same number of unique characters."""
    # "aabbcc" has 3 unique (a, b, c)
    # "abc" has 3 unique (a, b, c)
    # "aabbcc" is lexicographically smaller than "abc"
    assert find_max(["abc", "aabbcc"]) == "aabbcc"

def test_find_max_with_special_characters():
    """Tests words containing spaces or special characters."""
    # "a b" has 3 unique ('a', ' ', 'b')
    # "abc" has 3 unique ('a', 'b', 'c')
    # "a b" comes before "abc" lexicographically (space < 'c')
    assert find_max(["abc", "a b"]) == "a b"