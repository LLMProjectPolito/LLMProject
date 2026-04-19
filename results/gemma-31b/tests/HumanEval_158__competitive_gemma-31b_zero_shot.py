
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

@pytest.mark.parametrize("words, expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    (["apple", "pear"], "apple"),  # Both have 4 unique, 'apple' < 'pear'
    (["banana", "apple"], "apple"), # banana: 3 unique, apple: 4 unique
    (["zebra", "apple"], "zebra"),  # zebra: 5 unique, apple: 4 unique
    (["abc", "def"], "abc"),        # Both have 3 unique, 'abc' < 'def'
    (["", "a"], "a"),               # empty string vs 1 char
    (["", ""], ""),                 # multiple empty strings
    (["123", "111", "222"], "123"), # numbers
    (["Aa", "a"], "Aa"),            # Case sensitivity: 'A' and 'a' are unique
])
def test_find_max_scenarios(words, expected):
    assert find_max(words) == expected

def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"

def test_find_max_empty_list():
    # Depending on implementation, this might return None or raise an error.
    # Assuming standard behavior for max() on empty sequence without default.
    with pytest.raises(ValueError):
        find_max([])

def test_find_max_all_same_unique_count():
    # All have 1 unique character, should return lexicographically first
    words = ["zzzz", "yyyy", "xxxx", "aaaa"]
    assert find_max(words) == "aaaa"

def test_find_max_different_lengths_same_unique():
    # "abc" (3 unique), "abcc" (3 unique), "abccc" (3 unique)
    # Lexicographically "abc" < "abcc" < "abccc"
    words = ["abccc", "abcc", "abc"]
    assert find_max(words) == "abc"