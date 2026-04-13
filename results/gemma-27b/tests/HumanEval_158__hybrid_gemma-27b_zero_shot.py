
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
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return ""

    max_unique_chars = -1
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word

    return max_word

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_counts_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_words_same_unique_counts():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_mixed_case():
    assert find_max(["Hello", "hello", "World"]) == "World"

def test_words_with_numbers():
    assert find_max(["word1", "word22", "word333"]) == "word1"

def test_words_with_special_characters():
    assert find_max(["word!", "word@", "word#"]) == "word!"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdef"]) == "abcdefghijklmnopqrstuvwxyz"

def test_words_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_multiple_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_empty_string_and_word():
    assert find_max(["", "a"]) == "a"

def test_same_word_multiple_times():
    assert find_max(["abc", "abc", "abc"]) == "abc"

def test_complex_case():
    assert find_max(["abcde", "abcfg", "abchj", "abc"]) == "abcde"

def test_long_string_with_few_unique():
    assert find_max(["aaaaaaaaaaaaaaaaaaaa", "abc"]) == "abc"

def test_all_words_same_unique_count():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_mixed_case_words():
    assert find_max(["Hello", "world", "Python"]) == "Python"

def test_empty_string_and_repeated_chars():
    assert find_max(["", "aaaaa"]) == "aaaaa"

def test_multiple_max_words():
    assert find_max(["abc", "bac", "cba"]) == "abc"

def test_words_with_unicode_characters():
    assert find_max(["你好", "世界"]) == "世界"

def test_words_with_mixed_unicode_and_ascii():
    assert find_max(["hello", "你好世界"]) == "你好世界"

def test_long_list_of_words():
    words = ["a" * i for i in range(1, 11)]
    assert find_max(words) == "a" * 10

def test_words_with_same_length_but_different_unique_chars():
    assert find_max(["abcd", "abcc"]) == "abcd"

def test_words_with_same_length_and_same_unique_chars():
    assert find_max(["abcd", "dcba"]) == "abcd"