
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
from typing import List

def find_max(words: List[str]) -> str:
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
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
        (["abc", "def", "ghi"], "abc"),
        (["a", "aa", "aaa"], "a"),
        ([], ""),
        ([""], ""),
        (["abc", "abc"], "abc"),
        (["abc", "def", "abc"], "abc"),
        (["xyz", "abc", "def"], "xyz"),
        (["hello", "world", "python"], "hello"),
        (["apple", "banana", "orange"], "apple"),
    ],
)
def test_find_max(words: List[str], expected: str):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "def", "ghi"], "abc"),
        (["a", "aa", "aaa"], "a"),
        ([], ""),
        ([""], ""),
        (["abc", "abc"], "abc"),
        (["abc", "def", "abc"], "abc"),
        (["xyz", "abc", "def"], "xyz"),
        (["hello", "world", "python"], "hello"),
        (["apple", "banana", "orange"], "apple"),
    ],
)
def test_empty_list(words: List[str], expected: str):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["abc", "def", "ghi"], "abc"),
        (["a", "aa", "aaa"], "a"),
        ([], ""),
        ([""], ""),
        (["abc", "abc"], "abc"),
        (["abc", "def", "abc"], "abc"),
        (["xyz", "abc", "def"], "xyz"),
        (["hello", "world", "python"], "hello"),
        (["apple", "banana", "orange"], "apple"),
    ],
)
def test_lexicographical_order(words: List[str], expected: str):
    assert find_max(words) == expected