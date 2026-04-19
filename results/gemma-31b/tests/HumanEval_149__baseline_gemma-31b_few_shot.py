
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

def test_sorted_list_sum_examples():
    # Testing examples provided in the docstring
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty():
    # Testing an empty list
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    # Testing a list where all strings have odd lengths
    assert sorted_list_sum(["a", "aaa", "apple"]) == []

def test_sorted_list_sum_all_even():
    # Testing a list where all strings have even lengths
    # Should be sorted by length first, then alphabetically
    assert sorted_list_sum(["zz", "aa", "bbbb", "cccc"]) == ["aa", "zz", "bbbb", "cccc"]

def test_sorted_list_sum_mixed_lengths():
    # Testing mixed lengths: filter odd, sort by length, then alpha
    # "cat" (3) - odd, "dog" (3) - odd, "bird" (4) - even, "fish" (4) - even, "apple" (5) - odd, "banana" (6) - even
    input_list = ["cat", "dog", "bird", "fish", "apple", "banana"]
    # Expected: ["bird", "fish", "banana"] (bird < fish alphabetically)
    assert sorted_list_sum(input_list) == ["bird", "fish", "banana"]

def test_sorted_list_sum_alphabetical_tie():
    # Testing that strings of the same even length are sorted alphabetically
    assert sorted_list_sum(["dc", "ba", "ca", "ad"]) == ["ad", "ba", "ca", "dc"]

def test_sorted_list_sum_duplicates():
    # Testing that duplicates are preserved and sorted correctly
    assert sorted_list_sum(["aa", "aa", "bb", "a"]) == ["aa", "aa", "bb"]

def test_sorted_list_sum_case_sensitivity():
    # Testing case sensitivity (standard Python sort: Uppercase comes before lowercase)
    assert sorted_list_sum(["Bb", "Aa"]) == ["Aa", "Bb"]