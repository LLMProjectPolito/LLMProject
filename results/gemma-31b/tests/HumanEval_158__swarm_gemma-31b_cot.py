
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

import pytest
import math

@pytest.mark.parametrize("input_list, expected", [
    (["apple", "aple", "apply"], "aple"),
    (["abc", "abcc", "abbc"], "abbc"),
    (["apple", "apply", "banana"], "apple"),
])
def test_find_max_tie_breaker(input_list, expected):
    """
    Test that find_max returns the string with the maximum number of unique characters,
    using lexicographical order as the tie-breaker when unique counts are equal.
    """
    assert find_max(input_list) == expected