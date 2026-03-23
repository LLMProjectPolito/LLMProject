import pytest
from your_module import sorted_list_sum  # Replace your_module

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "cd", "aa"]) == ["aa", "aa", "cd"]

def test_same_length_different_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_same_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef", "ab"]) == ["ab", "ab", "cd", "ef"]

def test_complex_case():
    assert sorted_list_sum(["abc", "a", "ab", "abcd", "bc", "cde", "abc"]) == ["a", "ab", "bc", "abc", "abc", "cde"]

def test_single_element_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_element_odd():
    assert sorted_list_sum(["a"]) == []

def test_long_strings():
    assert sorted_list_sum(["abcdefgh", "abc", "abcdef"]) == ["abc", "abcdef", "abcdefgh"]

def test_strings_with_spaces():
    assert sorted_list_sum(["a b", "aa", "aaa"]) == ["aa"]

def test_strings_with_special_characters():
    assert sorted_list_sum(["!@#", "a", "!!"]) == []

def test_strings_with_unicode():
    assert sorted_list_sum(["你好", "世界", "你好世界"]) == ["你好", "世界"]