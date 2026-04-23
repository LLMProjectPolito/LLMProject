
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


def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["word"]) == "word"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_same_unique_chars():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_words_with_repeated_characters():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_mixed_case_characters():
    assert find_max(["aA", "bB", "cC"]) == "aA"

def test_empty_string_in_list():
    assert find_max(["", "abc", "def"]) == "abc"

def test_list_with_empty_string_and_other_strings():
    assert find_max(["", "abc", ""]) == "abc"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_long_word_with_many_unique_characters():
    assert find_max(["abcdefghijklmnopqrstuvwxyz"]) == "abcdefghijklmnopqrstuvwxyz"

def test_word_with_only_one_unique_character():
    assert find_max(["a", "aa", "aaa"]) == "a"

def test_word_with_duplicate_characters_and_long_word_with_many_unique_characters():
    assert find_max(["aabbcc", "abcdefgh"]) == "abcdefgh"

def test_case_sensitivity():
    assert find_max(["a", "A"]) == "a"  # Case-sensitive

def test_mixed_characters_and_numbers():
    assert find_max(["a1", "b2", "c3"]) == "a1"

@pytest.mark.parametrize(
    "words, expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "ab", "a"], "abc"),
        (["abc", "ac", "ab"], "abc"),
        (["a", "b", "c"], "a"),
        ([], ""),
        ([""], ""),
        (["aaaa", "bb", "cc", "dd"], "aaaa"),
        (["abcde", "abcd", "ab"], "abcde"),
        (["abc", "bca", "cab"], "abc"),
        (["hello", "world", "python"], "hello"),
        (["apple", "banana", "orange"], "apple"),
        (["xyz", "abc", "def"], "xyz"),
        (["a", "a", "a"], "a"),
        (["aa", "bb", "cc"], "aa"),
        (["aaa", "bbb", "ccc"], "aaa"),
        (["a", "aa", "aaa"], "aaa"),
        (["abcabc", "abccba"], "abcabc"),
        (["abcdefg", "abcef", "abdef"], "abcdefg"),
        (["abcdefg", "abc", "def"], "abcdefg"),
    ],
)
def test_find_max(words: List[str], expected: str) -> None:
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["name", "of", "string", "string"], "string"),
        (["name", "enam", "game", "enam"], "enam"),
        (["aaaaaaa", "bb", "cc", "aaaaaaa"], "aaaaaaa"),
    ],
)
def test_multiple_max_unique(words: List[str], expected: str) -> None:
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["abc", "def", "ghi"], "abc"),
        (["ghi", "def", "abc"], "abc"),
    ],
)
def test_lexicographical_order(words: List[str], expected: str) -> None:
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
       (["aaaa", "aaa", "a"], "aaa"),
       (["aaaa", "a", "aaa"], "aaa"),
    ],
)

def test_tie_lexicographical(words: List[str], expected: str) -> None:
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words",
    [
        [],
        ["a"],
        ["a", "b"],
        ["ab", "a"],
        ["abc", "ab"],
    ],
)
def test_empty_list(words):
  assert find_max(words) == ""