
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
        elif unique_chars == max_unique_chars:
            if word < result:
                result = word

    return result

@pytest.mark.parametrize(
    "words, expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "bca", "cab"], "abc"),
        (["abc", "bca", "cab", "def"], "def"),
        (["a", "aa", "aaa"], "a"),
        (["", "abc", "def"], "def"),
        (["abc", "", "def"], "def"),
        (["", "", ""], ""),
        (["abc", "abc", "def"], "def"),
        (["abc", "def", "abc"], "def"),
        (["aba", "abc", "def"], "def"),
        (["xyz", "abc", "def"], "def"),
        (["xyz", "def", "abc"], "def"),
        (["apple", "banana", "orange"], "banana"),
        (["apple", "banana", "orange", "grape"], "banana"),
        (["apple", "banana", "orange", "grape", "kiwi"], "kiwi"),
        (["a", "a", "b"], "b"),
        (["b", "a", "a"], "b"),
        (["aaa", "bbb", "ccc"], "aaa"),
        (["abcde", "fghij", "klmno"], "abcde"),
        (["racecar", "madam", "level"], "racecar"),
        (["level", "madam", "racecar"], "racecar"),
        (["hello", "world"], "hello"),
    ],
)
def test_find_max_basic(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        ([], ""),
        (["abc"], "abc"),
        (["abc", "def"], "def"),
        (["def", "abc"], "def"),
    ],
)
def test_find_max_empty_list(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["a", "aa", "aaa", "aaaa"], "aaaa"),
        (["aaaa", "aaa", "aa", "a"], "aaaa"),
        (["a", "aa", "aaa", "aaaa", "aaaa"], "aaaa"),
    ],
)
def test_find_max_same_unique_chars(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["abc", "bca", "cab", "cba"], "abc"),
        (["cba", "abc", "bca", "cab"], "abc"),
    ],
)
def test_find_max_lexicographical_order(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["aaaaaaa", "aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["bb", "cc", "aaaaaaa", "aaaaaaa"], "aaaaaaa"),
    ],
)
def test_find_max_duplicate_max_unique_chars(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "bca", "cab"], "abc"),
        (["xyz", "abc", "def"], "xyz"),
        (["", "abc", "def"], "abc"),
        (["abc", "", "def"], "abc"),
        (["", "", ""], ""),
        (["a", "aa", "aaa"], "a"),
        (["aba", "baa", "aab"], "aba"),
        (["hello", "world", "python"], "world"),
        (["apple", "banana", "orange"], "banana"),
        (["same", "same", "same"], "same"),  # Check for duplicates, should return first
        ([], ""), #empty list
        (["a", "aa", "a"], "a"),
        (["abcde", "abc", "ab"], "abcde"),
    ],
)
def test_find_max_basic(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["abcdefg", "abcde", "abcd"], "abcdefg"),
        (["abcde", "abcdefg", "abcd"], "abcdefg"),
        (["abcde", "abcde", "abcdefg"], "abcdefg"),
    ],
)
def test_find_max_length(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["12345", "54321", "123"], "12345"),
        (["54321", "12345", "123"], "12345"),
        (["123", "54321", "12345"], "12345"),
    ],
)
def test_find_max_numbers(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
       (["a", "a", "a", "b", "c"], "a"), #Test for multiple occurrences of same unique chars
       (["b", "c", "a", "a", "a"], "a"),
    ],
)
def test_find_max_multiple_occurrences(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["z", "y", "x"], "x"),
        (["x", "y", "z"], "z"),
        (["z", "x", "y"], "z"),
    ],
)
def test_find_max_lexicographical(words, expected):
    assert find_max(words) == expected

@pytest.mark.parametrize(
    "words, expected",
    [
        (["a", "aa", "aaa", "a"], "aaa"), #Test for multiple occurrences of same unique chars
        (["a", "a", "aa", "aaa"], "aaa"),
    ],
)
def test_find_max_equal_unique_chars(words, expected):
    assert find_max(words) == expected