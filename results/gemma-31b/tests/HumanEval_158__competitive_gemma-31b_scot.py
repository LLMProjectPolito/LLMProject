
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
    (["apple", "banana", "cherry"], "banana"), # apple: 4, banana: 3, cherry: 5 -> cherry
    (["abc", "def", "ghi"], "abc"), # All 3 unique, "abc" is first lexicographically
    (["a", "b", "c"], "a"), # All 1 unique, "a" is first
    (["", "a"], "a"), # empty string has 0 unique
    ([""], ""), # single empty string
    (["apple", "Apple"], "Apple"), # 'A' comes before 'a'
    (["test", "tess"], "tess"), # test: 3 (t,e,s), tess: 3 (t,e,s). "tess" < "test"
    (["abcdef", "fedcba"], "abcdef"), # both 6 unique, "abcdef" < "fedcba"
])
def test_find_max_parametrized(words, expected):
    # Note: The example ["apple", "banana", "cherry"] logic:
    # apple: {a, p, l, e} = 4
    # banana: {b, a, n} = 3
    # cherry: {c, h, e, r, y} = 5
    # Result should be "cherry". Correcting the parametrize list.
    pass

# Redefining the parametrize list with correct logic for the specific test case
@pytest.mark.parametrize("words, expected", [
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    (["apple", "banana", "cherry"], "cherry"),
    (["abc", "def", "ghi"], "abc"),
    (["a", "b", "c"], "a"),
    (["", "a"], "a"),
    ([""], ""),
    (["apple", "Apple"], "Apple"),
    (["test", "tess"], "tess"),
    (["abcdef", "fedcba"], "abcdef"),
])
def test_find_max_logic(words, expected):
    assert find_max(words) == expected

def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"

def test_find_max_all_same_unique_count():
    # "cat" (3), "dog" (3), "bat" (3)
    # Lexicographical: bat < cat < dog
    assert find_max(["cat", "dog", "bat"]) == "bat"

def test_find_max_different_lengths_same_unique():
    # "abc" (3), "aabbcc" (3)
    # Lexicographical: "aabbcc" < "abc"
    assert find_max(["abc", "aabbcc"]) == "aabbcc"