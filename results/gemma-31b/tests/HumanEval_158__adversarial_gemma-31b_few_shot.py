
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
    """Test the examples provided in the docstring."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_lexicographical_tie():
    """
    Test that when unique character counts are equal, 
    the lexicographically smallest word is returned.
    """
    # 'apple' (a,p,l,e) = 4 unique
    # 'apply' (a,p,l,y) = 4 unique
    # 'apple' < 'apply'
    assert find_max(["apply", "apple"]) == "apple"
    
    # 'ball' (b,a,l) = 3 unique
    # 'able' (a,b,l,e) = 4 unique
    assert find_max(["ball", "able"]) == "able"

def test_find_max_empty_list():
    """Test behavior with an empty list. Should likely return None or raise an error."""
    # Depending on implementation, this might return None or raise IndexError.
    # A robust function should handle this gracefully.
    assert find_max([]) == None or find_max([]) == ""

def test_find_max_single_element():
    """Test a list containing only one word."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_find_max_with_empty_strings():
    """Test lists containing empty strings mixed with valid words."""
    assert find_max(["", "a"]) == "a"
    assert find_max(["", ""]) == ""

def test_find_max_case_sensitivity():
    """
    Test if the function treats uppercase and lowercase as different characters.
    Usually, 'A' and 'a' are distinct unique characters.
    """
    # 'Aa' has 2 unique characters, 'aa' has 1.
    assert find_max(["Aa", "aa"]) == "Aa"

def test_find_max_special_characters():
    """Test strings containing numbers, spaces, and symbols."""
    # 'a b' (a, space, b) = 3 unique
    # 'ab' (a, b) = 2 unique
    assert find_max(["a b", "ab"]) == "a b"
    # '123' (3 unique) vs '111' (1 unique)
    assert find_max(["111", "123"]) == "123"

def test_find_max_all_same_unique_count():
    """Test a scenario where every word has the exact same number of unique characters."""
    # All have 1 unique character. 'a' < 'b' < 'c'
    assert find_max(["ccc", "bbb", "aaa"]) == "aaa"

def test_find_max_large_strings():
    """Test with very long strings to ensure efficiency."""
    long_word_1 = "abcdefghijklmnopqrstuvwxyz" * 100 # 26 unique
    long_word_2 = "abcdefghijklmnopqrstuvwxy" * 100  # 25 unique
    assert find_max([long_word_1, long_word_2]) == long_word_1