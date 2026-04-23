
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

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_unique_chars = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word

    return result


@pytest.mark.parametrize(
    "words, expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "bca", "cab"], "abc"),
        (["a", "aa", "aaa"], "a"),
        (["", "abc", "def"], "abc"),
        (["abc", "", "def"], "def"),
        (["", "", ""], ""),
        (["apple", "banana", "orange"], "banana"),
        (["hello", "world", "python"], "python"),
        (["xyz", "abc", "pqr"], "xyz"),
        (["a", "a", "a"], "a"),
        ([], ""),
        (["abc", "def", "ghi"], "abc"),
        (["def", "abc", "ghi"], "abc"),
        (["abc", "def", "abc"], "abc"),
    ],
)
def test_find_max(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["a", "aa", "aaa", "aaaa"], "aaaa"),
        (["aaaa", "aaa", "aa", "a"], "aaaa"),
    ],
)
def test_max_unique_chars(words, expected):
    assert find_max(words) == expected