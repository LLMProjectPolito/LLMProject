import pytest

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_counts_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_words_same_length():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_words_with_special_characters():
    assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

def test_words_with_numbers():
    assert find_max(["123", "4567", "89"]) == "4567"

def test_words_with_mixed_characters():
    assert find_max(["a1b2", "c3d4e", "f5"]) == "c3d4e"

def test_duplicate_words():
    assert find_max(["hello", "hello", "world"]) == "hello"

def test_words_with_uppercase_and_lowercase():
    assert find_max(["Hello", "world", "WorlD"]) == "Hello"

def test_long_words():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_words_with_spaces():
    assert find_max(["hello world", "abc"]) == "hello world"

def test_words_with_unicode_characters():
    assert find_max(["你好世界", "abc"]) == "你好世界"

def test_words_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_multiple_max_words_lexicographical():
    assert find_max(["abc", "bca", "cab"]) == "abc"