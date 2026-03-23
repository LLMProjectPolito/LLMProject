import pytest

def list_sort(lst):
    """Sorts a list of strings by length, then alphabetically, and handles duplicates."""
    unique_words = sorted(list(set(lst)))
    result = []
    for word in unique_words:
        result.append(word)
    result.sort(key=lambda x: (len(x), x))
    return result

def test_empty_list():
    assert list_sort([]) == []

def test_single_element():
    assert list_sort(["a"]) == ["a"]

def test_example_1():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_words():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "a", "aaa"]

def test_same_length_words():
    assert list_sort(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_mixed_lengths():
    assert list_sort(["abc", "ab", "a", "abcd"]) == ["a", "ab", "abc", "abcd"]

def test_long_list():
    assert list_sort(["a", "bb", "ccc", "dd", "e"]) == ["a", "bb", "ccc", "dd"]

def test_empty_list_with_duplicates():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "a", "aaa"]

def test_single_element_with_duplicates():
    assert list_sort(["a"]) == ["a"]

def test_example_2_with_duplicates():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_example_3_with_duplicates():
    assert list_sort(["abc", "ab", "a", "abcd"]) == ["a", "ab", "abc", "abcd"]

def test_example_4_with_long_list():
    assert list_sort(["a", "bb", "ccc", "dd", "e"]) == ["a", "bb", "ccc", "dd"]