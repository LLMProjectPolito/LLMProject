
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

# Assuming find_max is imported from your module
# from your_module import find_max

def test_edge_cases():
    """Tests the boundaries of the input: empty lists and single elements."""
    # Empty list: Based on Suite 1, we expect None. 
    # If the implementation varies, this is the primary point of failure.
    assert find_max([]) is None
    
    # Single element: Should always return the element itself
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""
    assert find_max(["a"]) == "a"

def test_core_logic_unique_counts():
    """Tests that the function correctly prioritizes unique character counts over string length."""
    # "apple" (4 unique: a,p,l,e) vs "aaaaa" (1 unique: a)
    assert find_max(["apple", "aaaaa"]) == "apple"
    # "abcde" (5 unique) vs "aabbcc" (3 unique)
    assert find_max(["aabbcc", "abcde"]) == "abcde"

def test_tie_breaking_lexicographical():
    """
    Tests the tie-breaking rule: if unique character counts are equal,
    return the one that comes first lexicographically.
    """
    # Tie in unique count (3): 'abc' < 'def' < 'ghi'
    assert find_max(["ghi", "def", "abc"]) == "abc"
    
    # Tie in unique count (1): 'a' < 'b' < 'c'
    assert find_max(["c", "b", "a"]) == "a"
    
    # Mixed lengths, same unique count: 'apple' (4) vs 'pear' (4). 'apple' < 'pear'
    assert find_max(["pear", "apple"]) == "apple"

def test_character_complexity():
    """Tests handling of case sensitivity, numbers, and special characters."""
    # Case Sensitivity: 'A' (ASCII 65) comes before 'a' (ASCII 97)
    assert find_max(["a", "A"]) == "A"
    assert find_max(["ab", "Aa"]) == "Aa"
    
    # Numbers and Special Characters:
    # '123' (3 unique) vs '!!!' (1 unique)
    assert find_max(["123", "!!!"]) == "123"
    
    # Lexicographical tie with special chars: 'a b' (3 unique: a, space, b) vs 'abc' (3 unique)
    # Space ' ' comes before 'c' in ASCII
    assert find_max(["abc", "a b"]) == "a b"
    
    # Symbols: '!@#' (3 unique) vs '123' (3 unique). '!@#' comes first.
    assert find_max(["123", "!@#"]) == "!@#"

@pytest.mark.parametrize("input_list, expected", [
    # Provided Examples
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    
    # Tie-breaking scenarios
    (["dog", "cat", "bat"], "bat"),       # All 3 unique, 'bat' is first
    (["aaaa", "bbbb", "cccc"], "aaaa"),    # All 1 unique, 'aaaa' is first
    (["xyz", "abc", "def"], "abc"),          # All 3 unique, 'abc' is first
    
    # Unique count priority
    (["apple", "pear", "peach"], "peach"), # peach (5) wins over apple/pear (4)
    (["apple", "banana", "cherry"], "cherry"), # cherry (5) wins
    (["abc", "abcd", "abcde"], "abcde"),      # Increasing counts
    
    # Duplicates and exact matches
    (["abcde", "abcde"], "abcde"),
    
    # Case and Special Char combinations
    (["a", "A"], "A"),
    (["abc", "123", "!!!"], "123"),
])
def test_comprehensive_scenarios(input_list, expected):
    """A massive collection of diverse scenarios to ensure regression testing."""
    assert find_max(input_list) == expected