
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

def test_unique_character_counts():
    """Test that the function correctly identifies the word with the most unique characters."""
    # "apple" (4), "banana" (3), "cherry" (5)
    assert find_max(["apple", "banana", "cherry"]) == "cherry"
    # "abc" (3), "abcd" (4), "abcde" (5)
    assert find_max(["abc", "abcd", "abcde"]) == "abcde"
    # 'zebra' (5) vs 'apple' (4)
    assert find_max(["apple", "zebra"]) == "zebra"
    # 'alphabet' (6) vs 'zoo' (2)
    assert find_max(["zoo", "alphabet"]) == "alphabet"
    # Length doesn't matter, only unique count: 'aaaaaaaaaa' (1) vs 'abc' (3)
    assert find_max(["aaaaaaaaaa", "abc"]) == "abc"

def test_lexicographical_tie_breaker():
    """Test that lexicographical order is used as a tie-breaker for same unique counts."""
    # All have 3 unique characters: 'abc' is smallest
    assert find_max(["def", "abc", "ghi"]) == "abc"
    assert find_max(["cab", "bac", "abc"]) == "abc"
    # All have 4 unique characters: 'apple' < 'pear'
    assert find_max(["pear", "apple"]) == "apple"
    # All have 4 unique characters: 'apple' < 'apply'
    assert find_max(["apply", "apple"]) == "apple"
    # All have 2 unique characters: 'aa' < 'bb' < 'cc'
    assert find_max(["cc", "bb", "aa"]) == "aa"
    # All have 1 unique character: 'x' < 'y' < 'z'
    assert find_max(["z", "y", "x"]) == "x"
    # Different lengths, same unique count: "aaaaa" (1) vs "b" (1) -> "aaaaa" < "b"
    assert find_max(["aaaaa", "b"]) == "aaaaa"
    # Different lengths, same unique count: "abc" (3) vs "aabbcc" (3) -> "aabbcc" < "abc"
    assert find_max(["abc", "aabbcc"]) == "aabbcc"

def test_single_element():
    """Test behavior with a single element in the list."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_empty_list():
    """Test behavior with an empty list (expecting ValueError from max())."""
    with pytest.raises(ValueError):
        find_max([])

def test_empty_strings_in_list():
    """Test behavior when the list contains empty strings."""
    # "" has 0 unique, "a" has 1
    assert find_max(["", "a"]) == "a"
    # Both have 0 unique, "" is lexicographically first
    assert find_max(["", ""]) == ""

def test_case_sensitivity():
    """Test that unique characters are case-sensitive and affect lexicographical order."""
    # "Aa" (2 unique) vs "a" (1 unique)
    assert find_max(["Aa", "a"]) == "Aa"
    # "Apple" (4 unique) vs "apple" (4 unique). 'A' < 'a'
    assert find_max(["apple", "Apple"]) == "Apple"
    # 'A' (1 unique) vs 'a' (1 unique). 'A' < 'a'
    assert find_max(["a", "A"]) == "A"

def test_special_characters_and_numbers():
    """Test behavior with numbers and special characters."""
    # "123" (3 unique) vs "!!!" (1 unique)
    assert find_max(["123", "!!!"]) == "123"
    # "a1!" (3 unique) vs "b2@" (3 unique) -> "a1!" < "b2@"
    assert find_max(["b2@", "a1!"]) == "a1!"
    # " @#" (3 unique) vs "123" (3 unique). Space comes before '1'
    assert find_max(["123", "!!!", " @#"]) == " @#"
    # " @#" (3 unique) vs "abc" (3 unique). Space comes before 'a'
    assert find_max(["abc", " @#"]) == " @#"

def test_identical_words():
    """Test behavior when the list contains duplicate words."""
    assert find_max(["test", "test", "test"]) == "test"