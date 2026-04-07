
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
# Edge cases: Empty input list, multiple words with the same maximum unique characters.
# We need to test various scenarios including empty lists, lists with single words, lists with duplicate words,
# lists with words having different numbers of unique characters, and lists where multiple words have the same maximum.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Checks the behavior with an empty input list.
# - test_single_word: Checks the behavior with a list containing only one word.
# - test_multiple_words_different_unique_chars: Checks the behavior with multiple words having different numbers of unique characters.
# - test_multiple_words_same_unique_chars_lexicographical_order: Checks the behavior with multiple words having the same maximum number of unique characters, ensuring lexicographical order is maintained.
# - test_duplicate_words: Checks the behavior with duplicate words in the input list.
# - test_mixed_case: Checks the behavior with mixed case words.
# - test_special_characters: Checks the behavior with words containing special characters.

# STEP 3: CODE
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["abc", "ab", "abcd"]) == "abcd"

def test_multiple_words_same_unique_chars_lexicographical_order():
    assert find_max(["enam", "name", "game"]) == "enam"

def test_duplicate_words():
    assert find_max(["name", "name", "enam"]) == "enam"

def test_mixed_case():
    assert find_max(["Name", "name", "Enam"]) == "Enam"

def test_special_characters():
    assert find_max(["!@#", "abc", "!@#$"]) == "!@#"

def test_complex_case():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_another_complex_case():
    assert find_max(["abc", "ab", "abcd", "bac"]) == "abcd"

def test_all_same_characters():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_lexicographical_tie():
    assert find_max(["apple", "banana", "orange"]) == "apple"