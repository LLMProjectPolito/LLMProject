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
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word

    return max_word

# STEP 1: REASONING
# The function `find_max` aims to find the word with the maximum number of unique characters in a list of strings.
# If there's a tie, it returns the lexicographically smallest word.
# Edge cases include an empty input list.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Checks the behavior with an empty input list.
# - test_single_word: Checks the behavior with a list containing only one word.
# - test_multiple_words_different_unique_counts: Checks the behavior with multiple words having different numbers of unique characters.
# - test_multiple_words_same_unique_counts: Checks the behavior with multiple words having the same number of unique characters, verifying lexicographical order.
# - test_words_with_duplicates: Checks the behavior with words containing duplicate characters.
# - test_all_words_same_character: Checks the behavior when all words consist of the same character repeated.
# - test_mixed_case: Checks the behavior with mixed case strings.
# - test_words_with_special_characters: Checks the behavior with words containing special characters.

# STEP 3: CODE
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_counts():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_duplicates():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_all_words_same_character():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_mixed_case():
    assert find_max(["Hello", "hello", "World"]) == "World"

def test_words_with_special_characters():
    assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

def test_tie_lexicographical_order():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_long_words():
    assert find_max(["abcdefgh", "abcdefg", "abcdef"]) == "abcdefgh"

def test_empty_string_in_list():
    assert find_max(["", "abc", "def"]) == "abc"

def test_multiple_empty_strings():
    assert find_max(["", "", ""]) == ""