
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

def test_sorted_list_sum_basic():
    """Tests the examples provided in the docstring."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty_list():
    """Tests that an empty list returns an empty list."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    """Tests that a list containing only odd-length strings returns an empty list."""
    assert sorted_list_sum(["a", "abc", "abcde"]) == []

def test_sorted_list_sum_all_even():
    """Tests that a list of even-length strings is sorted correctly."""
    # "aa" (2), "bb" (2), "cccc" (4)
    assert sorted_list_sum(["cccc", "bb", "aa"]) == ["aa", "bb", "cccc"]

def test_sorted_list_sum_alphabetical_tiebreak():
    """Tests that strings of the same length are sorted alphabetically."""
    # All length 2: "ba", "ab", "ac" -> sorted: "ab", "ac", "ba"
    assert sorted_list_sum(["ba", "ab", "ac"]) == ["ab", "ac", "ba"]

def test_sorted_list_sum_mixed_lengths_and_alphabetical():
    """Tests complex sorting: first by length, then alphabetically."""
    input_list = ["zebra", "apple", "do", "cat", "be", "dog", "banana", "at"]
    # Even lengths: "do" (2), "be" (2), "at" (2), "banana" (6)
    # Sorted by length: ["do", "be", "at", "banana"]
    # Sorted alphabetically within length 2: ["at", "be", "do", "banana"]
    assert sorted_list_sum(input_list) == ["at", "be", "do", "banana"]

def test_sorted_list_sum_duplicates():
    """Tests that duplicate strings are preserved and sorted."""
    assert sorted_list_sum(["aa", "bb", "aa", "a"]) == ["aa", "aa", "bb"]

def test_sorted_list_sum_empty_strings():
    """Tests that empty strings (length 0, which is even) are handled correctly."""
    # "" is length 0, "aa" is length 2
    assert sorted_list_sum(["", "a", "aa"]) == ["", "aa"]

def test_sorted_list_sum_case_sensitivity():
    """Tests that sorting follows standard Python string comparison (ASCII)."""
    # "B" comes before "a" in ASCII
    assert sorted_list_sum(["aa", "BB"]) == ["BB", "aa"]