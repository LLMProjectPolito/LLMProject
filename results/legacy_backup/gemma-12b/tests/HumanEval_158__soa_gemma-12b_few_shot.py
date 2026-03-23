import pytest

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_repeated_chars():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_max_unique():
    assert find_max(["abc", "cba", "xyz"]) == "abc"

def test_find_max_with_duplicates():
    assert find_max(["apple", "banana", "apple"]) == "banana"

def test_find_max_mixed_lengths():
    assert find_max(["a", "bb", "ccc", "dddd"]) == "ccc"

def test_find_max_all_same_length():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_special_characters():
    assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

def test_find_max_unicode_characters():
    assert find_max(["你好", "世界", "你好世界"]) == "你好世界"

def test_find_max_numbers_as_strings():
    assert find_max(["123", "45", "6789"]) == "6789"