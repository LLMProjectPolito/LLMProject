import pytest

def test_find_max_with_unique_characters():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_with_tied_unique_characters():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_with_no_unique_characters():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_with_empty_list():
    assert find_max([]) == ""

def test_find_max_with_single_element_list():
    assert find_max(["test"]) == "test"

def test_find_max_with_multiple_elements_and_tied_max_length():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_with_multiple_elements_and_tied_max_length_and_lexicographical_order():
    assert find_max(["abc", "bca", "aaa"]) == "aaa"

def test_find_max_with_special_characters():
    assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

def test_find_max_with_numbers():
    assert find_max(["123", "456", "789"]) == "123"

def test_find_max_with_mixed_characters():
    assert find_max(["abc123", "def456", "ghi789"]) == "abc123"