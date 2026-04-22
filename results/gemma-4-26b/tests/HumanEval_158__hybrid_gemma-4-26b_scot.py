
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
from your_module import find_max  # Replace 'your_module' with the actual filename

@pytest.mark.parametrize("input_list, expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
])
def test_docstring_examples(input_list, expected):
    """Validates the specific examples provided in the problem description."""
    assert find_max(input_list) == expected

def test_edge_cases():
    """Tests boundary conditions: empty lists, single elements, and empty strings."""
    # Empty list: Following Pythonic standard, max() on empty sequence raises ValueError
    with pytest.raises(ValueError):
        find_max([])
    
    # Single element
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""
    
    # Empty strings within a list
    assert find_max(["", "a", ""]) == "a"
    assert find_max(["", ""]) == ""
    assert find_max(["", "ab", "a"]) == "ab"

def test_tie_breaking_logic():
    """
    Tests the two-tier priority: 
    1. Maximize unique character count.
    2. Minimize lexicographical value (tie-breaker).
    """
    # Tie in unique count (5 each): 'grape' < 'peach'
    assert find_max(["apple", "peach", "grape"]) == "grape"
    
    # Tie in unique count (4 each): 'apple' < 'apply'
    assert find_max(["apply", "apple"]) == "apple"
    
    # Tie in unique count (3 each): 'abc' < 'abd' < 'abe'
    assert find_max(["abe", "abc", "abd"]) == "abc"
    
    # Tie in unique count (1 each): 'a' < 'b' < 'c'
    assert find_max(["c", "b", "a"]) == "a"
    
    # Tie in unique count (2 each): 'ab' < 'ba'
    assert find_max(["ba", "ab", "cb"]) == "ab"

def test_character_complexity():
    """Tests case sensitivity, numbers, and special characters."""
    # Case Sensitivity: Unique count priority
    # 'Aa' has 2 unique (A, a), 'aa' has 1 unique (a)
    assert find_max(["aa", "Aa"]) == "Aa"
    
    # Case Sensitivity: Lexicographical tie-breaker
    # 'A' (1 unique) vs 'a' (1 unique). 'A' < 'a'
    assert find_max(["a", "A"]) == "A"
    
    # Lexicographical tie: 'Aa' (2 unique) vs 'Ab' (2 unique). 'Aa' < 'Ab'
    assert find_max(["Ab", "Aa"]) == "Aa"

    # Special Characters & Numbers: Unique count priority
    # "!@#" (3 unique) vs "!!!" (1 unique)
    assert find_max(["!!!", "!@#"]) == "!@#"
    
    # Special Characters & Numbers: Lexicographical tie-breaker
    # "abc" (3) vs "123" (3). "123" < "abc"
    assert find_max(["abc", "123"]) == "123"
    
    # Spaces: "a b" (3 unique: 'a', ' ', 'b') vs "abc" (3 unique). "a b" < "abc"
    assert find_max(["abc", "a b"]) == "a b"
    
    # Symbols: "!!! " (3 unique) vs "123" (3 unique). "!!! " < "123"
    assert find_max(["123", "!!! "]) == "!!! "

@pytest.mark.parametrize("input_list, expected", [
    (["apple", "pear", "peach"], "apple"),      # All 4 unique, apple is lexicographically first
    (["dog", "cat", "elephant"], "elephant"),  # elephant has most unique (7)
    (["a", "abc", "ab"], "abc"),               # abc has most unique (3)
    (["zzzz", "yyyy", "xxxx"], "xxxx"),        # All 1 unique, xxxx is lexicographically first
    (["c", "b", "a", ""], "a"),                # Mix of empty and single chars
])
def test_comprehensive_scenarios(input_list, expected):
    """A collection of varied scenarios to ensure general robustness."""
    assert find_max(input_list) == expected