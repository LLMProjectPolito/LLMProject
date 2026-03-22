import pytest

def test_empty_list():
    assert find_max([]) == ""

def test_single_element_list():
    assert find_max(["hello"]) == "hello"

def test_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["abc", "ab", "a"]) == "abc"

def test_same_unique_counts_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["abc", "bca", "cab"]) == "abc"
    assert find_max(["xyz", "zyx"]) == "xyz"

def test_all_same_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["aaaa", "bbb", "ccc"]) == "aaaa"

def test_mixed_case():
    assert find_max(["Hello", "hello", "World"]) == "World"
    assert find_max(["aA", "Aa"]) == "Aa"
    assert find_max(["Name", "name", "Of"]) == "Name"

def test_special_characters():
    assert find_max(["hello!", "world@"]) == "world@"
    assert find_max(["abc!", "abc"]) == "abc!"
    assert find_max(["hello!", "world?", "abc"]) == "world?"

def test_long_words():
    long_word1 = "abcdefghijklmnopqrstuvwxyz"
    long_word2 = "zyxwvutsrqponmlkjihgfedcba"
    assert find_max([long_word1, long_word2]) == "abcdefghijklmnopqrstuvwxyz"

def test_zero_unique_characters():
    assert find_max(["", "abc"]) == "abc"
    assert find_max(["", ""]) == ""

def test_lexicographical_ties_complex():
    assert find_max(["abcde", "abcdf", "abcda"]) == "abcda"
    assert find_max(["aaa", "aab", "aac"]) == "aaa"

def test_duplicate_words():
    assert find_max(["hello", "hello", "world"]) == "world"

def test_numbers_and_letters():
    assert find_max(["123", "abc", "a1b2"]) == "a1b2"

def test_list_with_empty_strings():
    assert find_max(["", "abc", "de"]) == "abc"

def test_all_words_same_unique_count():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_unicode_characters():
    assert find_max(["你好", "世界", "abc"]) == "世界"

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_max_same_length():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_empty_string_first():
    assert find_max(["", "abc", "def"]) == "abc"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""