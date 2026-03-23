# STEP 1: REASONING
# The function `find_max` aims to find the word with the maximum number of unique characters from a list of strings.
# If multiple words have the same maximum number of unique characters, it should return the lexicographically smallest one.
# The test suite needs to cover various scenarios, including:
# 1. Basic case with different unique character counts.
# 2. Case with multiple words having the same maximum unique character count, testing lexicographical order.
# 3. Empty list input.
# 4. List with empty strings.
# 5. List with strings containing duplicate characters.
# 6. List with strings of varying lengths.
# 7. List with special characters.

# STEP 2: PLAN
# Test functions:
# - test_basic_case: Checks the basic functionality with different unique character counts.
# - test_lexicographical_order: Checks the lexicographical order when multiple words have the same maximum unique characters.
# - test_empty_list: Checks the behavior with an empty input list.
# - test_empty_strings: Checks the behavior with a list containing empty strings.
# - test_duplicate_characters: Checks the behavior with strings containing duplicate characters.
# - test_varying_lengths: Checks the behavior with strings of different lengths.
# - test_special_characters: Checks the behavior with strings containing special characters.

# STEP 3: CODE
import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return ""

    max_unique_count = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_count:
            max_unique_count = unique_chars
            result = word
        elif unique_chars == max_unique_count and word < result:
            result = word

    return result


class TestFindMax:
    def test_basic_case(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_lexicographical_order(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_empty_list(self):
        assert find_max([]) == ""

    def test_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_duplicate_characters(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_varying_lengths(self):
        assert find_max(["a", "bb", "ccc", "dddd"]) == "ccc"

    def test_special_characters(self):
        assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

    def test_same_unique_chars_lexicographical(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_mixed_case(self):
        assert find_max(["AbC", "aBc", "abc"]) == "AbC"

    def test_numbers_and_letters(self):
        assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"