import pytest
from your_module import find_max  # Replace your_module

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_duplicate_words():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_same_unique_count():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_special_characters():
    assert find_max(["!@#", "abc", "def"]) == "!@#"

def test_find_max_numbers():
    assert find_max(["123", "abc", "456"]) == "123"

def test_find_max_mixed_characters():
    assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"

def test_find_max_long_word():
    assert find_max(["thisisaverylongword"]) == "thisisaverylongword"

def test_find_max_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_find_max_normal_case():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_another_normal_case():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_lexicographical_tie():
    assert find_max(["abc", "abd", "abe"]) == "abc"