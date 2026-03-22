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

    max_unique = -1
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique and word < max_word:
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

def test_all_words_same_unique_count():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_mixed_case_words():
    assert find_max(["Hello", "hello", "World"]) == "World"

def test_words_with_numbers():
    assert find_max(["word1", "word22", "word333"]) == "word1"

def test_words_with_special_characters():
    assert find_max(["word!", "word@", "word#"]) == "word!"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_words_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_multiple_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_words_with_unicode_characters():
    assert find_max(["你好", "世界"]) == "世界"

def test_words_with_mixed_unicode_and_ascii():
    assert find_max(["hello", "你好"]) == "hello"

def test_large_list_of_words():
    words = ["word" + str(i) for i in range(100)]
    assert find_max(words) == "word0"

def test_words_with_same_length_but_different_unique_chars():
    assert find_max(["abcd", "abcc"]) == "abcd"

def test_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_mixed_empty_and_nonempty():
    assert find_max(["", "abc", ""]) == "abc"

def test_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_lexicographical_tiebreaker():
    assert find_max(["zabc", "aabc"]) == "aabc"

def test_long_string_with_many_unique_chars():
    assert find_max(["abcdefghijk", "abc"]) == "abcdefghijk"

def test_string_with_all_unique_chars():
    assert find_max(["abcdefg", "abc"]) == "abcdefg"

def test_words_with_spaces():
    assert find_max(["hello world", "hello"]) == "hello world"