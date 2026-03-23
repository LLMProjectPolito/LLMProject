import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.
    If the input list is empty, an empty string is returned.

    Examples:
    >>> find_max(["name", "of", "string"])
    'string'
    >>> find_max(["name", "enam", "game"])
    'enam'
    >>> find_max(["aaaaaaa", "bb" ,"cc"])
    'aaaaaaa'
    >>> find_max(["", "", ""])
    ''
    >>> find_max(["abc", "ab", "a"])
    'abc'
    >>> find_max(["abc", "bca", "cab"])
    'abc'
    >>> find_max(["!@#", "abc", "123"])
    '!@#'
    >>> find_max(["a1b2", "abc", "123"])
    'a1b2'
    """
    if not words:
        return ""

    max_unique_count = 0
    max_word = ""

    for word in words:
        if not isinstance(word, str):
            raise TypeError("Input list must contain only strings.")
        unique_chars_count = len(set(word))
        if unique_chars_count > max_unique_count:
            max_unique_count = unique_chars_count
            max_word = word
        elif unique_chars_count == max_unique_count:
            if word < max_word:
                max_word = word

    return max_word

### Tests (Pytest):

def test_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_same_length():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_empty_list():
    assert find_max([]) == ""

def test_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_different_lengths():
    assert find_max(["abc", "ab", "a"]) == "abc"

def test_same_unique_count():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_special_characters():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

def test_mixed_characters():
    assert find_max(["a1b2", "abc", "123"]) == "a1b2"

def test_none_input():
    with pytest.raises(TypeError):
        find_max(["abc", None, "def"])

def test_int_input():
    with pytest.raises(TypeError):
        find_max(["abc", 123, "def"])