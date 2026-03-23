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
def test_filter_and_sort_even_length_strings_example1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_filter_and_sort_even_length_strings_example2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_filter_and_sort_even_length_strings_with_empty_list():
    assert sorted_list_sum([]) == []

def test_filter_and_sort_even_length_strings_odd_lengths_only():
    assert sorted_list_sum(["a", "c", "e"]) == []

def test_filter_and_sort_even_length_strings_same_length():
    assert sorted_list_sum(["bb", "aa", "dd", "cc"]) == ["aa", "bb", "cc", "dd"]

def test_filter_and_sort_even_length_strings_mixed_lengths():
    assert sorted_list_sum(["abc", "ab", "abcd", "a"]) == ["ab", "abcd"]

def test_filter_and_sort_even_length_strings_large_mixed():
    assert sorted_list_sum(["abc", "ab", "abcd", "a", "efgh", "e", "ef", "ijkl"]) == ["ab", "ef", "abcd", "efgh", "ijkl"]

def test_filter_and_sort_even_length_strings_with_numbers():
    try:
        sorted_list_sum([1, "aa"])
    except TypeError:
        pass  # Expected TypeError
    else:
        assert False, "TypeError not raised when input contains a number"

def test_filter_and_sort_even_length_strings_with_special_chars():
    assert sorted_list_sum(["!@#", "a", "!!"]) == ["!@#", "!!"]