import pytest

def test_find_max_unicode_and_lexicographic_tie():
    # Edge case: includes empty string, Unicode emojis, and a tie on unique character count.
    words = ["", "😀😁😂", "ab", "ba", "abcde", "edcba"]
    # Both "abcde" and "edcba" have 5 unique characters; "abcde" is lexicographically smaller.
    assert find_max(words) == "abcde"

def test_find_max_with_empty_string_and_lexicographic_tie_simple():
    # Edge case: includes an empty string and multiple candidates with the same
    # number of unique characters. The function should ignore the empty string,
    # count unique characters correctly, and return the lexicographically smallest
    # word among the ties.
    words = ["", "a", "ab", "ba"]
    assert find_max(words) == "ab"

def test_find_max_with_empty_string_and_lexicographic_tie_multiple():
    # All non-empty strings have the same number of unique characters (3),
    # the empty string has 0 unique characters.
    # The function should return the lexicographically smallest among the ties.
    words = ["", "cba", "bca", "abc"]
    assert find_max(words) == "abc"