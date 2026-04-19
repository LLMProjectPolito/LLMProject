
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

def test_find_max_basic():
    """Test basic functionality with different unique character counts."""
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical_tie():
    """Test tie-breaking using lexicographical order when unique counts are equal."""
    # unique chars: name(4), enam(4), game(4). "enam" < "game" < "name"
    assert find_max(["name", "enam", "game"]) == "enam"
    # All have 3 unique characters: 'abc', 'bac', 'cab'
    assert find_max(["cab", "bac", "abc"]) == "abc"

def test_find_max_single_char_tie():
    """Test tie-breaking when all words have only one unique character."""
    # unique chars: aaaaaaa(1), bb(1), cc(1). "aaaaaaa" < "bb" < "cc"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["zzzz", "yyyy", "xxxx"]) == "xxxx"

def test_find_max_single_element():
    """Test with a list containing only one string."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_find_max_empty_strings():
    """Test with empty strings in the list."""
    assert find_max(["", "a", ""]) == "a"
    assert find_max(["", ""]) == ""

def test_find_max_varying_lengths():
    """Test that word length doesn't override unique character count."""
    # 'abcdef' (6 unique), 'aaaaaaaaaa' (1 unique)
    assert find_max(["aaaaaaaaaa", "abcdef"]) == "abcdef"

def test_find_max_different_lengths_same_unique():
    """Test words of different lengths but same number of unique characters."""
    # "abc" (3), "aabbcc" (3), "aaabbbccc" (3)
    # Lexicographically: "aaabbbccc" < "aabbcc" < "abc"
    assert find_max(["abc", "aabbcc", "aaabbbccc"]) == "aaabbbccc"
    # "banana" (3 unique), "cat" (3 unique). "banana" < "cat"
    assert find_max(["cat", "banana"]) == "banana"

def test_find_max_case_sensitivity():
    """Test that the function handles case sensitivity (standard ASCII sorting)."""
    # 'Apple' (4 unique), 'apple' (4 unique). 'Apple' < 'apple'
    assert find_max(["Apple", "apple"]) == "Apple"
    # "Aa" (2 unique), "a" (1 unique)
    assert find_max(["a", "Aa"]) == "Aa"

def test_find_max_special_characters():
    """Test words containing numbers and special characters."""
    # "123" (3), "!!!" (1), "a1!" (3). "123" < "a1!"
    assert find_max(["123", "!!!", "a1!"]) == "123"

def test_find_max_empty_list():
    """Test behavior with an empty list, expecting standard max() behavior."""
    with pytest.raises((ValueError, TypeError)):
        find_max([])

@pytest.mark.parametrize("words, expected", [
    (["apple", "banana", "cherry"], "cherry"), # apple: 4, banana: 3, cherry: 5
    (["abc", "abd", "abe"], "abc"),           # all 3, 'abc' is first
    (["z", "y", "x"], "x"),                   # all 1, 'x' is first
    (["123", "111", "222"], "123"),           # 3 unique vs 1 unique
    (["dog", "cat", "bird"], "bird"),         # dog(3), cat(3), bird(4)
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected