
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
    """
    Implementation based on the provided requirements:
    1. Delete strings with odd lengths.
    2. Sort by length (ascending).
    3. Sort alphabetically if lengths are equal.
    """
    # Filter out odd lengths
    filtered = [s for s in lst if len(s) % 2 == 0]
    # Sort by length first, then alphabetically
    filtered.sort(key=lambda x: (len(x), x))
    return filtered

class TestSortedListSum:
    def test_empty_list(self):
        """Should return an empty list when input is empty."""
        assert sorted_list_sum([]) == []

    def test_all_odd_lengths(self):
        """Should return an empty list if all strings have odd lengths."""
        assert sorted_list_sum(["a", "aaa", "abcde", "123"]) == []

    def test_all_even_lengths(self):
        """Should return all strings sorted by length and then alphabetically."""
        # "aa" and "bb" same length (alpha sort), "cccc" longer
        assert sorted_list_sum(["bb", "cccc", "aa"]) == ["aa", "bb", "cccc"]

    def test_mixed_lengths(self):
        """Should remove odd lengths and sort the remaining even lengths."""
        # "a" (1), "aa" (2), "aaa" (3), "bbbb" (4), "c" (1)
        # Remaining: ["aa", "bbbb"]
        assert sorted_list_sum(["a", "aa", "aaa", "bbbb", "c"]) == ["aa", "bbbb"]

    def test_alphabetical_tie_break(self):
        """Should sort alphabetically when lengths are identical."""
        assert sorted_list_sum(["dc", "ba", "ab", "zz"]) == ["ab", "ba", "dc", "zz"]

    def test_duplicates(self):
        """Should handle duplicate strings correctly."""
        assert sorted_list_sum(["aa", "bb", "aa", "bbbb"]) == ["aa", "aa", "bb", "bbbb"]

    def test_case_sensitivity(self):
        """Should follow standard Python string sorting (ASCII/Unicode) for alphabetical tie-breaks."""
        # Uppercase usually comes before lowercase in Python sorting
        assert sorted_list_sum(["ba", "BA", "ab", "AB"]) == ["AB", "AB", "ab", "ba"] # Wait, logic check:
        # "AB" (2), "AB" (2), "ab" (2), "ba" (2) -> Sorted: AB, AB, ab, ba
        # Let's use a clearer set:
        assert sorted_list_sum(["Zz", "Aa"]) == ["Aa", "Zz"]

    def test_complex_scenario(self):
        """Comprehensive test with mixed lengths, duplicates, and alphabetical requirements."""
        input_list = ["apple", "pear", "banana", "kiwi", "plum", "orange", "aa", "bb"]
        # Lengths:
        # apple: 5 (odd) -> remove
        # pear: 4 (even)
        # banana: 6 (even)
        # kiwi: 4 (even)
        # plum: 4 (even)
        # orange: 6 (even)
        # aa: 2 (even)
        # bb: 2 (even)
        
        # Even lengths: ["pear", "banana", "kiwi", "plum", "orange", "aa", "bb"]
        # Sorted by length:
        # len 2: ["aa", "bb"]
        # len 4: ["kiwi", "pear", "plum"] (alphabetical)
        # len 6: ["banana", "orange"] (alphabetical)
        
        expected = ["aa", "bb", "kiwi", "pear", "plum", "banana", "orange"]
        assert sorted_list_sum(input_list) == expected

    @pytest.mark.parametrize("input_val, expected_val", [
        (["aa", "a", "aaa"], ["aa"]),
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        (["", "a", "bb"], ["", "bb"]), # Empty string has length 0 (even)
    ])
    def test_provided_examples(self, input_val, expected_val):
        """Tests the specific examples provided in the problem description."""
        assert sorted_list_sum(input_val) == expected_val