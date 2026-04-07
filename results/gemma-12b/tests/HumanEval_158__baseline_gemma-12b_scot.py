
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

# STEP 1: REASONING
# The function `find_max` aims to find the word with the maximum number of unique characters from a list of strings.
# If multiple words have the same maximum number of unique characters, it should return the lexicographically smallest one.
# The test suite needs to cover various scenarios, including:
# - Empty list input
# - List with a single word
# - List with multiple words, where one word has the maximum unique characters
# - List with multiple words, where multiple words have the same maximum unique characters (lexicographical comparison)
# - List with words containing repeated characters
# - List with empty strings
# - List with mixed case strings (should be case-sensitive)

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Test with an empty list as input.
# - test_single_word: Test with a list containing a single word.
# - test_multiple_words_unique_max: Test with multiple words, where one has the maximum unique characters.
# - test_multiple_words_same_max_lexicographical: Test with multiple words having the same maximum unique characters, checking lexicographical order.
# - test_words_with_repeated_characters: Test with words containing repeated characters.
# - test_empty_strings: Test with a list containing empty strings.
# - test_mixed_case_strings: Test with mixed-case strings to ensure case sensitivity.

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

    max_unique_chars = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word

    return result

class TestFindMax:
    def test_empty_list(self):
        assert find_max([]) == ""

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_multiple_words_unique_max(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_multiple_words_same_max_lexicographical(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_words_with_repeated_characters(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_empty_strings(self):
        assert find_max(["", "abc", ""]) == "abc"

    def test_mixed_case_strings(self):
        assert find_max(["Name", "name", "STRING", "string"]) == "Name"