
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """

import pytest

def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    filtered_list.sort(key=lambda x: (len(x), x))
    return filtered_list

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_odd_lengths():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "ab", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "aa", "ab", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_complex_case():
    assert sorted_list_sum(["ab", "cd", "ef", "gh", "ij", "kl"]) == ["ab", "cd", "ef", "gh", "ij", "kl"]

def test_sorted_list_sum_single_element():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_complex_case_2():
    assert sorted_list_sum(["abc", "def", "ghi", "jkl"]) == ["def", "ghi", "jkl"]
    
def test_sorted_list_sum_complex_case_3():
    assert sorted_list_sum(["a", "aa", "aaa", "ab", "cd"]) == ["ab", "cd"]



def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_multiple_chars():
    assert is_palindrome('madam') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('refer') == True

def test_palindrome_not_palindrome():
    assert is_palindrome('hello') == False
    assert is_palindrome('world') == False
    assert is_palindrome('python') == False
    assert is_palindrome('algorithm') == False

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == False

def test_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam') == False

def test_palindrome_with_mixed_case():
    assert is_palindrome('Racecar') == False

def test_palindrome_empty_string():
    assert is_palindrome("") == True