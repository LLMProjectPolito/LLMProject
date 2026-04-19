
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

def test_find_max_basic_examples():
    """Test basic functionality based on provided examples."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_unique_character_logic():
    """Test that the function correctly identifies the maximum number of unique characters, regardless of length."""
    # 'alphabet' has 7 unique (a,l,p,h,b,e,t), 'abc' has 3.
    assert find_max(["abc", "alphabet"]) == "alphabet"
    # 'Mississippi' has 4 unique (m,i,s,p), 'river' has 5 (r,i,v,e).
    assert find_max(["Mississippi", "river"]) == "river"
    # 'unique' (5), 'uniques' (6)
    assert find_max(["unique", "uniques"]) == "uniques"

def test_find_max_lexicographical_tie_breaking():
    """Test that tie-breaking is strictly lexicographical when unique counts are equal."""
    # All have 3 unique characters. Lexicographical order: 'abc' < 'bac' < 'cab'
    assert find_max(["cab", "bac", "abc"]) == "abc"
    # All have 1 unique character. 'aa' < 'bb' < 'cc'
    assert find_max(["cc", "bb", "aa"]) == "aa"
    # Same unique count (3), but different lengths. 'aabbcc' < 'abc'
    assert find_max(["abc", "aabbcc"]) == "aabbcc"
    # Same unique count (1), different lengths. 'aaaaaaaaaa' < 'b'
    assert find_max(["b", "aaaaaaaaaa"]) == "aaaaaaaaaa"

def test_find_max_case_sensitivity():
    """
    Test case sensitivity. Python sets treat 'A' and 'a' as different, 
    and 'A' < 'a' lexicographically.
    """
    # 'Aa' has 2 unique characters, 'a' has 1.
    assert find_max(["a", "Aa"]) == "Aa"
    # 'Apple' (A,p,l,e) = 4, 'apple' (a,p,l,e) = 4. 'Apple' < 'apple'.
    assert find_max(["apple", "Apple"]) == "Apple"

def test_find_max_special_characters_and_numbers():
    """Test that the function handles numbers and symbols as characters."""
    # '123' (3 unique), '!!!' (1 unique), 'abc' (3 unique). '123' < 'abc'.
    assert find_max(["abc", "!!!", "123"]) == "123"
    # ' @#$' (4 unique), 'abc' (3 unique)
    assert find_max(["abc", " @#$"]) == " @#$"

def test_find_max_edge_cases_strings():
    """Test edge cases involving empty strings and single-element lists."""
    # List with one element
    assert find_max(["hello"]) == "hello"
    # List with only empty strings
    assert find_max(["", ""]) == ""
    # Mix of empty and non-empty
    assert find_max(["", "a"]) == "a"
    # Space is a character (1 unique). " " < "  " is False, but unique count is same.
    # " " (1 unique), "  " (1 unique). "  " < " " is True.
    assert find_max([" ", "  "]) == "  "

def test_find_max_empty_list():
    """Test behavior with an empty list. Expects ValueError (standard max() behavior)."""
    with pytest.raises(ValueError):
        find_max([])

@pytest.mark.parametrize("words, expected", [
    (["abcde", "fghij", "klmno"], "abcde"), # Tie (5), alphabetical first
    (["a", "b", "c"], "a"),                 # Tie (1), alphabetical first
    (["zzzz", "aaaa"], "aaaa"),             # Tie (1), alphabetical first
    (["ab", "ba"], "ab"),                   # Tie (2), alphabetical first
    (["python", "java", "c++"], "python"),  # python: 6, java: 3, c++: 2
    (["world", "hello"], "world"),          # world: 5, hello: 4
    (["alphabet", "beta"], "alphabet"),     # alphabet: 7, beta: 4
])
def test_find_max_parametrized(words, expected):
    """Comprehensive parameterized tests for various scenarios."""
    assert find_max(words) == expected