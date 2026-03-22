import pytest
import math


# Focus: Boundary Values
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["word"]) == "word"

def test_find_max_same_unique_chars_lexicographical():
    assert find_max(["abc", "bca", "cab"]) == "abc"

# Focus: Type Scenarios
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_multiple_words_same_unique_chars_and_same_lexicographical():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_words_with_duplicates():
    assert find_max(["apple", "banana", "orange"]) == "orange"

def test_find_max_words_with_special_characters():
    assert find_max(["abc!", "def?", "ghi#"]) == "abc!"

# Focus: Logic Branches
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_multiple_words_same_unique_chars_and_same_lexicographical():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_words_with_duplicates():
    assert find_max(["apple", "banana", "orange"]) == "orange"

def test_find_max_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"