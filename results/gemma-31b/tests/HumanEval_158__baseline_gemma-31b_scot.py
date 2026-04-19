
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
    """Test the examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_tie_break():
    """Test that the lexicographically first word is returned when unique counts are tied."""
    # All have 3 unique characters: 'abc', 'bac', 'cab'
    # 'abc' is lexicographically first
    assert find_max(["cab", "bac", "abc"]) == "abc"
    
    # 'apple' (a,p,l,e = 4), 'apply' (a,p,l,y = 4)
    # 'apple' < 'apply'
    assert find_max(["apply", "apple"]) == "apple"

def test_single_element():
    """Test a list containing only one string."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_empty_strings():
    """Test lists containing empty strings or strings with no unique variety."""
    # Empty string has 0 unique chars, "a" has 1.
    assert find_max(["", "a"]) == "a"
    # Both have 0 unique chars, "" is lexicographically first.
    assert find_max(["", ""]) == ""

def test_case_sensitivity():
    """Test that case sensitivity is handled (A != a)."""
    # "Aa" has 2 unique characters, "a" has 1.
    assert find_max(["a", "Aa"]) == "Aa"
    # "Apple" (A,p,l,e = 4), "apple" (a,p,l,e = 4)
    # "Apple" comes before "apple" in ASCII/lexicographical order.
    assert find_max(["apple", "Apple"]) == "Apple"

def test_special_characters():
    """Test strings containing numbers and symbols."""
    # "123" (3 unique), "!!!" (1 unique)
    assert find_max(["!!!", "123"]) == "123"
    # "a1" (2 unique), "b1" (2 unique) -> "a1" is first
    assert find_max(["b1", "a1"]) == "a1"

def test_empty_list():
    """Test behavior with an empty list."""
    # Depending on implementation, this might return None or raise ValueError.
    # We assume the function should handle it or we test for the expected exception.
    with pytest.raises((ValueError, TypeError, IndexError)):
        # If the function uses max() without a default, it raises ValueError
        find_max([])

@pytest.mark.parametrize("words, expected", [
    (["abc", "def", "ghi"], "abc"), # Tie: all 3 unique, 'abc' is first
    (["zzzz", "aaaa"], "aaaa"),     # Tie: all 1 unique, 'aaaa' is first
    (["world", "hello"], "world"),  # world: 5 unique, hello: 4 unique
    (["python", "java"], "python"), # python: 6 unique, java: 2 unique
])
def test_parametrized_cases(words, expected):
    """Run a variety of cases using parametrization."""
    assert find_max(words) == expected