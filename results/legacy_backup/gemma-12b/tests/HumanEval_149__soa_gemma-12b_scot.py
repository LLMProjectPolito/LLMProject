import pytest

def test_empty_list():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_list_with_only_odd_length_strings():
    """Test with a list containing only strings with odd lengths."""
    assert sorted_list_sum(["a", "abc", "de"]) == []

def test_list_with_only_even_length_strings():
    """Test with a list containing only strings with even lengths."""
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_even_and_odd_length_strings():
    """Test with a list containing both even and odd length strings."""
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c"]) == ["aa", "bb"]

def test_duplicate_strings():
    """Test with a list containing duplicate strings."""
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_strings_with_same_length():
    """Test with strings of the same length, checking alphabetical order."""
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_strings_with_same_length_and_duplicates():
    """Test with strings of the same length and duplicates, checking alphabetical order."""
    assert sorted_list_sum(["ab", "ab", "cd", "ef"]) == ["ab", "ab", "cd", "ef"]

def test_complex_list():
    """Test with a more complex list of strings."""
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c", "cc", "ddd", "ee"]) == ["aa", "bb", "cc", "ee"]

def test_list_with_single_string():
    """Test with a list containing a single string."""
    assert sorted_list_sum(["a"]) == []
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_list_with_single_even_and_odd_string():
    """Test with a list containing a single even and odd string."""
    assert sorted_list_sum(["a", "aa"]) == ["aa"]