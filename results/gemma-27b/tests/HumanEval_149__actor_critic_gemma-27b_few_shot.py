
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
    For example:
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

### Tests (Pytest):
def test_example_1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_lengths_only():
    assert sorted_list_sum(["a", "c", "e"]) == []

def test_duplicates():
    assert sorted_list_sum(["bb", "aa", "dd", "cc"]) == ["aa", "bb", "cc", "dd"]

def test_mixed_lengths():
    assert sorted_list_sum(["abc", "ab", "abcd", "a"]) == ["ab", "abcd"]

def test_strings_with_spaces():
    assert sorted_list_sum(["ab c", "a", "abc"]) == ["ab c"]

def test_large_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape", "pear", "plum", "date", "fig"]) == ["date", "fig", "grape", "kiwi", "pear", "plum"]