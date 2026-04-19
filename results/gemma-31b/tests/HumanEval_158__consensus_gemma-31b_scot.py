
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
    """Test basic functionality with provided examples."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_lexicographical_tie():
    """Test that lexicographical order is the tie-breaker for same unique character count."""
    # All have 3 unique characters: 'abc', 'bac', 'cab'
    assert find_max(["cab", "bac", "abc"]) == "abc"
    # 'apple' (4 unique) and 'pear' (4 unique)
    assert find_max(["apple", "pear"]) == "apple"
    assert find_max(["pear", "apple"]) == "apple"
    # All have 1 unique character
    assert find_max(["ccc", "bbb", "aaa"]) == "aaa"
    assert find_max(["aaa", "bbb", "ccc"]) == "aaa"

def test_find_max_unique_vs_length():
    """Test strings where length does not equal unique character count."""
    # "aaaaa" (1 unique), "bb" (1 unique), "c" (1 unique). "aaaaa" is smallest lexicographically.
    assert find_max(["aaaaa", "bb", "c"]) == "aaaaa"
    # "abcdef" (6 unique) vs "abcdefghii" (9 unique)
    assert find_max(["abcdef", "abcdefghii"]) == "abcdefghii"
    # "abcdef" (6 unique) vs "abc" (3 unique)
    assert find_max(["abcdef", "abc"]) == "abcdef"

def test_find_max_edge_cases():
    """Test lists with single elements, empty strings, or identical words."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""
    assert find_max(["", "a"]) == "a"
    assert find_max(["", "a", ""]) == "a"
    assert find_max(["", ""]) == ""
    assert find_max(["test", "test", "test"]) == "test"

def test_find_max_case_sensitivity():
    """Test lexicographical ordering with mixed cases."""
    # "Aa" (2 unique) vs "a" (1 unique)
    assert find_max(["Aa", "a"]) == "Aa"
    # "Apple" (4 unique: A,p,l,e) vs "apple" (4 unique: a,p,l,e). 'A' < 'a'
    assert find_max(["Apple", "apple"]) == "Apple"
    # "B" (1 unique) vs "A" (1 unique). 'A' < 'B'
    assert find_max(["B", "A"]) == "A"

def test_find_max_special_characters():
    """Test strings with numbers, symbols, and spaces."""
    # "123" (3 unique), "abc" (3 unique). "123" < "abc"
    assert find_max(["abc", "123"]) == "123"
    # "!!!" (1 unique), "???" (1 unique). "!!!" < "???"
    assert find_max(["???", "!!!"]) == "!!!"
    # "a b c" (4 unique: a, space, b, c) vs "abc" (3 unique)
    assert find_max(["a b c", "abc"]) == "a b c"
    # "!@#" (3 unique) vs "$%^" (3 unique). "!" < "$"
    assert find_max(["$%^", "!@#"]) == "!@#"

@pytest.mark.parametrize("words, expected", [
    (["apple", "banana", "cherry"], "cherry"), # apple:4, banana:3, cherry:5
    (["dog", "cat", "bird"], "bird"),         # dog:3, cat:3, bird:4
    (["a", "b", "c"], "a"),                   # all 1, 'a' is smallest
    (["zzzz", "aaaa"], "aaaa"),               # all 1, 'aaaa' is smallest
    (["abc", "def", "ghi"], "abc"),           # all 3, 'abc' is smallest
    (["python", "java", "c++"], "python"),    # python:6, java:3, c++:2
    (["aba", "bab"], "aba"),                  # both 2, 'aba' < 'bab'
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected