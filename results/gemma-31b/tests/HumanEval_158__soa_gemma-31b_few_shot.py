
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
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_tie_breaker():
    # All have 3 unique characters: 'abc', 'def', 'ghi'
    # 'abc' is lexicographically first
    assert find_max(["ghi", "def", "abc"]) == "abc"
    # 'apple' (a,p,l,e = 4) vs 'pear' (p,e,a,r = 4)
    assert find_max(["pear", "apple"]) == "apple"

def test_unique_character_count():
    # 'alphabet' has 6 unique (a,l,p,h,b,e,t - wait, a is repeated) -> 7 unique
    # 'world' has 5 unique
    assert find_max(["world", "alphabet"]) == "alphabet"
    # 'aaaaa' (1 unique) vs 'ab' (2 unique)
    assert find_max(["aaaaa", "ab"]) == "ab"

def test_single_element():
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_empty_list():
    # Depending on implementation, this might return None or raise an error.
    # Assuming it returns None or handles gracefully.
    assert find_max([]) is None or find_max([]) == ""

def test_case_sensitivity():
    # 'A' and 'a' are typically treated as different unique characters in Python sets
    # 'Aa' (2 unique) vs 'a' (1 unique)
    assert find_max(["Aa", "a"]) == "Aa"
    # 'Apple' (A,p,l,e = 4) vs 'apple' (a,p,l,e = 4)
    # 'Apple' comes before 'apple' lexicographically (Uppercase < Lowercase)
    assert find_max(["apple", "Apple"]) == "Apple"

def test_mixed_lengths_same_uniques():
    # 'abc' (3 unique) vs 'abcde' (5 unique)
    assert find_max(["abc", "abcde"]) == "abcde"
    # 'abc' (3 unique) vs 'aabbcc' (3 unique)
    # 'aabbcc' comes before 'abc' lexicographically
    assert find_max(["abc", "aabbcc"]) == "aabbcc"

def test_special_characters():
    # '123' (3 unique) vs '!!!' (1 unique)
    assert find_max(["!!!", "123"]) == "123"
    # ' @#' (3 unique) vs 'abc' (3 unique)
    # Space comes before 'a'
    assert find_max(["abc", " @#"]) == " @#"

@pytest.mark.parametrize("words, expected", [
    (["a", "b", "c"], "a"),
    (["zebra", "apple"], "apple"),
    (["python", "java", "c++"], "python"), # python: 6, java: 2, c++: 2
    (["", ""], ""),
    (["ab", "ba"], "ab"),
])
def test_parametrized_cases(words, expected):
    assert find_max(words) == expected