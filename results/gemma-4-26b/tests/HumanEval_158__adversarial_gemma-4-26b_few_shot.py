
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

# The function to be tested (assumed to be in the same file or imported)
# from solution import find_max

def test_find_max_provided_examples():
    """Verify the function passes the specific examples provided in the docstring."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    """
    Test behavior with an empty list. 
    Depending on implementation, this should return None or an empty string.
    """
    # Assuming the function should return None or handle empty input gracefully
    assert find_max([]) in [None, ""]

def test_find_max_single_element():
    """A list with one element should always return that element."""
    assert find_max(["apple"]) == "apple"
    assert find_max([""]) == ""

def test_find_max_tie_breaker_lexicographical():
    """
    Test the tie-breaker: If unique counts are equal, 
    return the one first in lexicographical order.
    """
    # All have 3 unique characters: 'a', 'b', 'c'
    # Lexicographical order: 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'
    assert find_max(["cba", "bac", "abc"]) == "abc"
    
    # Tie with different lengths but same unique count
    # 'apple' -> {a, p, l, e} (4)
    # 'apply' -> {a, p, l, y} (4)
    # 'apple' < 'apply'
    assert find_max(["apply", "apple"]) == "apple"

def test_find_max_unique_vs_length():
    """
    Ensure the function counts UNIQUE characters, not total length.
    'aaaaa' has length 5 but only 1 unique character.
    'abc' has length 3 and 3 unique characters.
    """
    assert find_max(["aaaaa", "abc"]) == "abc"
    assert find_max(["aabbcc", "abc"]) == "aabbcc" # both have 3 unique, 'aabbcc' is lexicographically larger? 
    # Wait, 'abc' < 'aabbcc' is False. 'aabbcc' < 'abc' is True.
    # Let's re-verify: 'a' is same, 'a' < 'b'. So 'aabbcc' comes first.
    assert find_max(["abc", "aabbcc"]) == "aabbcc"

def test_find_max_case_sensitivity():
    """
    Test how the function handles uppercase vs lowercase.
    In ASCII/Unicode, 'A' (65) comes before 'a' (97).
    """
    # 'A' and 'a' both have 1 unique character. 'A' is lexicographically first.
    assert find_max(["a", "A"]) == "A"
    
    # 'Abc' (3 unique) vs 'abc' (3 unique). 'Abc' is lexicographically first.
    assert find_max(["abc", "Abc"]) == "Abc"

def test_find_max_special_characters_and_spaces():
    """Test strings containing spaces, numbers, and symbols."""
    # "a b" has 3 unique: {'a', ' ', 'b'}
    # "abc" has 3 unique: {'a', 'b', 'c'}
    # "a b" comes before "abc" lexicographically (space < 'b')
    assert find_max(["abc", "a b"]) == "a b"
    
    # Numbers and symbols
    assert find_max(["123", "!!!", "12"]) == "123"

@pytest.mark.parametrize("input_list, expected", [
    (["dog", "cat", "bat"], "bat"), # All 3 unique, 'bat' is first lexicographically
    (["zzzz", "aaaa"], "aaaa"),    # Both 1 unique, 'aaaa' is first
    (["apple", "pear", "peach"], "peach"), # peach (5 unique: p,e,a,c,h), apple (4), pear (4)
])
def test_find_max_parameterized(input_list, expected):
    """Bulk testing various scenarios using parametrization."""
    assert find_max(input_list) == expected

def test_find_max_non_string_elements():
    """
    Blue Team: Check if the function crashes when non-string elements 
    are passed (Robustness check).
    """
    with pytest.raises(TypeError):
        find_max(["abc", 123])