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
    assert sorted_list_sum(["aa", "a", "aaa"]) => ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    new_list = []
    for s in lst:
        if len(s) % 2 == 0:
            new_list.append(s)
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

### STEP 1: REASONING
# The function `sorted_list_sum` takes a list of strings as input.
# It filters out strings with odd lengths, keeping only even-length strings.
# Then, it sorts the remaining strings first by length (ascending) and then alphabetically (ascending) for strings of the same length.
# The function returns the sorted list of strings.
# We need to create a pytest suite to test this function with various inputs, including empty lists, lists with odd and even length strings, lists with duplicate strings, and lists with strings of the same length.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with only odd length strings: ["a", "b", "c"]
# 3. List with only even length strings: ["aa", "bb", "cc"]
# 4. List with mixed odd and even length strings: ["aa", "a", "aaa", "cd"]
# 5. List with duplicate strings: ["aa", "aa", "a", "aaa"]
# 6. List with strings of the same length: ["ab", "ac", "ad"]
# 7. List with a single element: ["aa"]
# 8. List with a single odd length element: ["a"]

### STEP 3: CODE
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_length_strings():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_even_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "ac", "ad"]) == ["ab", "ac", "ad"]

def test_single_element_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_element_odd():
    assert sorted_list_sum(["a"]) == []

def test_complex_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["banana", "orange"]