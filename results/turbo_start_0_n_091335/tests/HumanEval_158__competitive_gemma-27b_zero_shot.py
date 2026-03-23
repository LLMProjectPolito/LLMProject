import pytest

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
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_words_with_mixed_case():
    assert find_max(["Hello", "world"]) == "world"

def test_words_with_special_characters():
    assert find_max(["abc!", "def@"]) == "abc!"

def test_words_with_numbers():
    assert find_max(["abc1", "def2"]) == "abc1"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdef"]) == "abcdefghijklmnopqrstuvwxyz"

def test_words_with_spaces():
    assert find_max(["hello world", "hello"]) == "hello world"

def test_mixed_words():
    assert find_max(["abc", "ab", "a", "abcdef"]) == "abcdef"

def test_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_empty_string_in_list():
    assert find_max(["", "abc"]) == "abc"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""