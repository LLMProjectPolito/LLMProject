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
# - test_multiple_words_different_unique_counts: Checks the behavior with multiple words having different unique character counts.
# - test_multiple_words_same_unique_counts_lexicographical_order: Checks the behavior with multiple words having the same unique character count, ensuring lexicographical order is respected.
# - test_words_with_repeated_characters: Checks the behavior with words containing repeated characters.
# - test_words_with_empty_string: Checks the behavior with an empty string in the list.
# - test_all_words_same_length: Checks the behavior when all words have the same length.

# STEP 3: CODE
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_counts_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_all_words_same_length():
    assert find_max(["abcd", "efgh", "ijkl"]) == "abcd"

def test_mixed_case():
    assert find_max(["aBcD", "EfGh", "iJkL"]) == "aBcD"

def test_special_characters():
    assert find_max(["!@#$", "%^&*"]) == "!@#$"

def test_numbers_and_letters():
    assert find_max(["1234", "abcde", "a1b2c"]) == "abcde"

def test_long_strings():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdefghijklm"]) == "abcdefghijklmnopqrstuvwxyz"

def test_duplicate_words():
    assert find_max(["hello", "hello", "world"]) == "hello"