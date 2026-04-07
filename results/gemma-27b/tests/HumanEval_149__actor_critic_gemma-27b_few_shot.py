
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
    and returns the resulted list with a sorted order.
    The list is always a list of strings.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    """
    # Optional: Add a check for non-string elements for robustness
    # for item in lst:
    #     if not isinstance(item, str):
    #         raise TypeError("Input list must contain only strings.")

    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

# Test Cases
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
assert sorted_list_sum([]) == []  # Empty list
assert sorted_list_sum(["a", "c", "e"]) == []  # All odd lengths
assert sorted_list_sum(["bb", "aa", "dd", "cc"]) == ["aa", "bb", "cc", "dd"] # Same length, alphabetical
assert sorted_list_sum(["abc", "ab", "abcd", "a"]) == ["ab", "abcd"] # Mixed lengths
assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "pear"]) == ["kiwi", "pear"] # Larger list, mixed lengths, same lengths
assert sorted_list_sum(["a", "aa", "aaa", "aaaa", "aaaaa"]) == ["aa", "aaaa"] # Test with increasing lengths
assert sorted_list_sum(["abc", "def", "ghi"]) == [] # All odd lengths
assert sorted_list_sum(["abcd", "efgh", "ijkl"]) == ["abcd", "efgh", "ijkl"] # All even lengths, alphabetical