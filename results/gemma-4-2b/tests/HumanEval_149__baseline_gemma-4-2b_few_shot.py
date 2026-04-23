
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
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    result = [s for s in lst if len(s) % 2 == 0]
    result.sort(key=lambda x: (len(x), x))
    return result

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_only():
    assert sorted_list_sum(["a", "c", "e"]) == []

def test_sorted_list_sum_even_only():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "aa"]) == ["aa", "aa"]

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "ef", "gh"]) == ["ab", "cd", "ef", "gh"]