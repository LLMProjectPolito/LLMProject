
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
    """Tests the specific examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_tie_breaking():
    """Tests that if unique counts are equal, the lexicographically first word is returned."""
    # All have 3 unique characters: 'a', 'b', 'c'
    # Lexicographical order: 'abc' < 'abd' < 'abe'
    assert find_max(["abe", "abd", "abc"]) == "abc"
    
    # All have 1 unique character
    # Lexicographical order: 'a' < 'b' < 'c'
    assert find_max(["c", "b", "a"]) == "a"
    
    # Tie with different lengths: 'aaa' (1 unique) vs 'b' (1 unique)
    # 'aaa' comes before 'b' lexicographically
    assert find_max(["b", "aaa"]) == "aaa"

def test_single_element():
    """Tests a list containing only one word."""
    assert find_max(["hello"]) == "hello"
    assert find_max(["a"]) == "a"

def test_empty_list():
    """Tests the behavior when the input list is empty."""
    # Based on the get_max example provided, an empty input should return None
    assert find_max([]) is None

def test_empty_strings_in_list():
    """Tests lists containing empty strings."""
    assert find_max(["", "a", ""]) == "a"
    assert find_max(["", ""]) == ""

def test_case_sensitivity():
    """Tests that unique character counting is case-sensitive (standard Python behavior)."""
    # 'Aa' has 2 unique characters ('A' and 'a')
    # 'aa' has 1 unique character ('a')
    assert find_max(["aa", "Aa"]) == "Aa"

def test_special_characters_and_numbers():
    """Tests that the function handles non-alphabetic characters correctly."""
    # "a!b" has 3 unique: 'a', '!', 'b'
    # "abc" has 3 unique: 'a', 'b', 'c'
    # '!' comes before 'b' in ASCII/lexicographical order
    assert find_max(["abc", "a!b"]) == "a!b"
    
    # "123" has 3 unique
    # "111" has 1 unique
    assert find_max(["111", "123"]) == "123"

def test_all_identical_words():
    """Tests a list where all words are the same."""
    assert find_max(["test", "test", "test"]) == "test"