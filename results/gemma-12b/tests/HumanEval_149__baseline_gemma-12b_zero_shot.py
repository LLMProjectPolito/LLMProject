import pytest

def test_empty_list():
    from main import sorted_list_sum
    assert sorted_list_sum([]) == []

def test_list_with_only_odd_length_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["a", "bc", "de"]) == []

def test_list_with_only_even_length_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_even_and_odd_length_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c"]) == ["aa", "bb"]

def test_duplicate_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_strings_with_same_length():
    from main import sorted_list_sum
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_strings_with_same_length_and_different_alphabetical_order():
    from main import sorted_list_sum
    assert sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]

def test_complex_list():
    from main import sorted_list_sum
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c", "cc", "d", "eee", "ff"]) == ["aa", "bb", "cc", "ff"]

def test_list_with_one_string():
    from main import sorted_list_sum
    assert sorted_list_sum(["a"]) == []

def test_list_with_one_even_string():
    from main import sorted_list_sum
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_list_with_special_characters():
    from main import sorted_list_sum
    assert sorted_list_sum(["a!", "aa", "!!!"]) == ["aa"]

def test_list_with_numbers_as_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["1", "12", "123"]) == ["12"]

def test_list_with_mixed_characters_and_numbers():
    from main import sorted_list_sum
    assert sorted_list_sum(["a1", "12", "abc"]) == ["a1", "12"]