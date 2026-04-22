
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

def test_empty_list():
    """Test that an empty list returns an empty list."""
    assert filter_and_sort_even_strings([]) == []

def test_all_odd_lengths():
    """Test that a list containing only odd-length strings returns an empty list."""
    assert filter_and_sort_even_strings(["a", "abc", "abcde", "123"]) == []

def test_filtering_logic():
    """Test that the function correctly filters out strings with odd lengths."""
    input_list = ["a", "ab", "abc", "abcd", "abcde"]
    # Even: "ab", "abcd"
    expected = ["ab", "abcd"]
    assert filter_and_sort_even_strings(input_list) == expected

def test_sorting_logic():
    """
    Test that even-length strings are sorted by length (ascending) 
    and then alphabetically.
    """
    # Length 2: "zz", "aa" | Length 4: "cccc", "aaaa"
    input_list = ["cccc", "aa", "zz", "aaaa"]
    # Expected: "aa" (len 2, alpha), "zz" (len 2, alpha), "aaaa" (len 4, alpha), "cccc" (len 4, alpha)
    expected = ["aa", "zz", "aaaa", "cccc"]
    assert filter_and_sort_even_strings(input_list) == expected

def test_duplicates():
    """Test that duplicate even-length strings are preserved and sorted."""
    input_list = ["bb", "aa", "aa", "a", "cccc", "bb"]
    expected = ["aa", "aa", "bb", "bb", "cccc"]
    assert filter_and_sort_even_strings(input_list) == expected

def test_empty_strings():
    """Test that empty strings (length 0, which is even) are handled."""
    input_list = ["a", "", "bb", ""]
    expected = ["", "", "bb"]
    assert filter_and_sort_even_strings(input_list) == expected

def test_special_characters():
    """Test that sorting handles numbers and special characters via ASCII order."""
    # Length 2 strings: "12", "!!", "aa"
    # ASCII: '!' is 33, '1' is 49, 'a' is 97
    input_list = ["aa", "12", "!!"]
    expected = ["!!", "12", "aa"]
    assert filter_and_sort_even_strings(input_list) == expected

def test_case_sensitivity():
    """Test that alphabetical sorting respects standard ASCII order (Uppercase < lowercase)."""
    input_list = ["bb", "AA", "aa", "BB"]
    expected = ["AA", "BB", "aa", "bb"]
    assert filter_and_sort_even_strings(input_list) == expected

def test_unicode_and_emojis():
    """Test that multi-byte characters and emojis are handled correctly."""
    # "🐍" is len 1 (odd), "🐍🐍" is len 2 (even)
    # "🔥" is len 1 (odd), "🔥🔥" is len 2 (even)
    # "abcd" is len 4 (even)
    # Sorting order for emojis is based on Unicode code points
    input_list = ["🐍", "🐍🐍", "🔥", "🔥🔥", "abcd"]
    # Even: "🐍🐍", "🔥🔥", "abcd"
    # Unicode: 🔥 (U+1F525) > 🐍 (U+1F40D), so 🐍🐍 comes before 🔥🔥
    # Lengths: 2, 2, 4
    expected = ["🐍🐍", "🔥🔥", "abcd"]
    assert filter_and_sort_even_strings(input_list) == expected

def test_whitespace_edge_cases():
    """Test that strings consisting of whitespace are correctly treated by length."""
    # " " (len 1, odd), "  " (len 2, even), "\t\t" (len 2, even), "    " (len 4, even)
    # ASCII: \t is 9, space is 32
    input_list = [" ", "  ", "\t\t", "    "]
    expected = ["\t\t", "  ", "    "]
    assert filter_and_sort_even_strings(input_list) == expected

def test_invalid_input_type():
    """Test that passing a non-list input raises a TypeError."""
    with pytest.raises(TypeError):
        filter_and_sort_even_strings(None)
    with pytest.raises(TypeError):
        filter_and_sort_even_strings(123)

def test_non_string_elements():
    """Test that a list containing non-string elements raises a TypeError."""
    with pytest.raises(TypeError):
        filter_and_sort_even_strings(["aa", 1, "bb"])
    with pytest.raises(TypeError):
        filter_and_sort_even_strings(["aa", None, "bb"])

def test_performance_large_list():
    """Test that the function handles a large number of elements efficiently."""
    # Create a list of 10,000 strings with alternating even and odd lengths
    input_list = [("a" * (i % 4)) for i in range(10000)]
    # This contains lengths 0, 1, 2, 3. Even lengths are 0 and 2.
    result = filter_and_sort_even_strings(input_list)
    assert len(result) == 5000  # Half should be even (0 and 2)
    assert isinstance(result, list)

@pytest.mark.parametrize("input_val, expected_val", [
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
])
def test_docstring_examples(input_val, expected_val):
    """Test the specific examples provided in the problem description."""
    assert filter_and_sort_even_strings(input_val) == expected_val