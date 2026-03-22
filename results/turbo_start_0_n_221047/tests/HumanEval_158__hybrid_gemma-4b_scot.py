import pytest

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_word = ""
    max_unique_chars = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word

    return max_word


### SCoT Steps:

# STEP 1: REASONING
# The function `find_max` aims to find the word with the most unique characters in a list of strings.
# If multiple words have the same maximum number of unique characters, it should return the lexicographically smallest one.
# Edge cases to consider:
#   - Empty input list: Should return an empty string.
#   - List with only one word: Should return that word.
#   - Multiple words with the same maximum number of unique characters: Should return the lexicographically smallest.
#   - Words with no unique characters: Should return the first such word.

# STEP 2: PLAN
# Test functions:
#   - test_empty_list: Tests the case where the input list is empty.
#   - test_single_word: Tests the case where the input list contains only one word.
#   - test_multiple_words_different_unique_chars: Tests the case where multiple words have different numbers of unique characters.
#   - test_multiple_words_same_unique_chars_lexicographical_order: Tests the case where multiple words have the same number of unique characters and should be sorted lexicographically.
#   - test_words_with_no_unique_chars: Tests the case where all words have no unique characters.
#   - test_mixed_case: Tests the case where the input words have mixed case.
#   - test_duplicate_characters: Tests the case where words have duplicate characters.

# STEP 3: CODE
#

### Test Suite
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["hello", "world", "python"]) == "python"

def test_multiple_words_same_unique_chars_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_no_unique_chars():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_mixed_case():
    assert find_max(["Hello", "world", "Python"]) == "Python"

def test_duplicate_characters():
    assert find_max(["aabbcc", "abc", "ab"]) == "abc"