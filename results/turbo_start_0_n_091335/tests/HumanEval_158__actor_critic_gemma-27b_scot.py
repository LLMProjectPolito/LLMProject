import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    Examples:
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
    assert find_max(["hello"]) == "hello"

def test_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_empty_strings():
    assert find_max(["", "abc", "de"]) == "abc"

def test_duplicate_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_order_tiebreaker():
    assert find_max(["ab", "abc"]) == "abc"

def test_mixed_case_words():
    """
    Tests words with mixed casing. The function is case-sensitive.
    """
    assert find_max(["Hello", "hello", "World"]) == "World"

def test_special_characters():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_words_with_numbers():
    assert find_max(["12345", "abc"]) == "12345"

def test_all_zero_unique_chars():
    assert find_max(["", "", ""]) == ""

def test_unicode_characters():
    assert find_max(["你好", "世界", "abc"]) == "世界"

def test_large_list():
    words = [f"word{i}" for i in range(20)]
    assert find_max(words) == "word19"