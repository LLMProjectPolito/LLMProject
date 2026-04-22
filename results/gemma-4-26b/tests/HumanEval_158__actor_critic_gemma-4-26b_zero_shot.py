
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

def find_max(words):
    """
    Finds the word with the maximum number of unique characters.
    In case of a tie, returns the lexicographically first word.
    """
    if not words:
        return None
    
    # We use min() with a custom key to handle both requirements in one pass:
    # 1. -len(set(w)): Negating the unique count allows us to use min() to find the maximum.
    # 2. w: The second element in the tuple handles the lexicographical tie-breaker.
    return min(words, key=lambda w: (-len(set(w)), w))

def test_provided_examples():
    """Tests the examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_tie_break():
    """Tests that the lexicographically first word is returned when unique counts are equal."""
    # All have 3 unique characters; 'bat' is lexicographically first
    assert find_max(["cat", "bat", "rat"]) == "bat"
    
    # All have 4 unique characters; 'apple' is lexicographically first
    assert find_max(["zebra", "apple", "mango"]) == "apple"
    
    # Tie in unique count: 'aabbcc' (3) vs 'abc' (3). 'aabbcc' comes first lexicographically.
    assert find_max(["abc", "aabbcc"]) == "aabbcc"
    
    # Tie in unique count: 'a' vs 'b' vs 'c'
    assert find_max(["c", "b", "a"]) == "a"

def test_edge_cases():
    """Tests edge cases like empty lists, empty strings, and single elements."""
    # Empty list
    assert find_max([]) is None
    
    # Single element
    assert find_max(["hello"]) == "hello"
    
    # Empty strings in list
    assert find_max(["", "a", ""]) == "a"
    assert find_max(["", ""]) == ""
    
    # Case sensitivity (ASCII 'A' is 65, 'a' is 97, so 'A' comes first)
    assert find_max(["a", "A"]) == "A"
    
    # Numbers and special characters
    # '1!2' has 3 unique chars, '123' has 3 unique chars. '!' < '2'
    assert find_max(["123", "12", "1!2"]) == "1!2"

def test_all_same_unique_count():
    """Tests scenarios where all words have the same number of unique characters."""
    assert find_max(["z", "y", "x"]) == "x"
    assert find_max(["aaa", "bbb", "ccc"]) == "aaa"

def test_large_input():
    """Tests the function with a larger list of words."""
    words = ["abcdefg", "abc", "def", "ghij", "abcde", "zzzzzzzzzz"]
    # abcdefg: 7, abc: 3, def: 3, ghij: 4, abcde: 5, zzz...: 1
    assert find_max(words) == "abcdefg"