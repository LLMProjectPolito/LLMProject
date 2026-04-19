
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
    (["apple", "pear"], "apple"),
    (["zebra", "apple"], "zebra"),
    (["abc", "def"], "abc"),
    (["", ""], ""),
    (["a", "b", "c"], "a"),
    (["hello", "world"], "hello"),
    (["test", "tset"], "test"),
    (["123", "111", "222"], "123"),
    (["Aa", "a"], "Aa"),
])
def test_find_max_standard_cases(words, expected):
    assert find_max(words) == expected

def test_find_max_single_element():
    assert find_max(["python"]) == "python"

def test_find_max_empty_list():
    # Depending on implementation, this might return None or raise an error.
    # Assuming standard behavior for max() on empty sequence without default.
    with pytest.raises(ValueError):
        find_max([])

def test_find_max_with_empty_strings():
    assert find_max(["", "a"]) == "a"
    assert find_max(["", ""]) == ""

def test_find_max_case_sensitivity():
    # 'A' and 'a' are unique characters
    # "Aa" has 2 unique, "a" has 1
    assert find_max(["Aa", "a"]) == "Aa"

def test_find_max_lexicographical_priority():
    # All have 3 unique characters: 'abc', 'abd', 'abe'
    # 'abc' is lexicographically first
    assert find_max(["abe", "abd", "abc"]) == "abc"