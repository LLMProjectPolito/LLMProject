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

### STEP 1: REASONING
# The function `find_max` aims to find the word with the most unique characters in a list of strings.
# If multiple words have the same maximum number of unique characters, it should return the lexicographically smallest one.
# Edge cases to consider:
# 1. Empty input list: Should return an empty string.
# 2. List with only one word: Should return that word.
# 3. Multiple words with the same maximum number of unique characters: Should return the lexicographically smallest.
# 4. Words with no unique characters (all characters are the same): Should return the first such word.

### STEP 2: PLAN
# Test functions:
# 1. test_empty_list: Tests the case where the input list is empty.
# 2. test_single_word: Tests the case where the input list contains only one word.
# 3. test_multiple_words_different_unique_chars: Tests the case where multiple words have different numbers of unique characters.
# 4. test_multiple_words_same_unique_chars_lexicographical_order: Tests the case where multiple words have the same number of unique characters and needs lexicographical ordering.
# 5. test_all_same_characters: Tests the case where all words have the same characters.
# 6. test_mixed_case: Tests the case where the input words have mixed case.
# 7. test_numbers_and_letters: Tests the case where the input words contain numbers and letters.

### STEP 3: CODE
# test_empty_list.py
def test_empty_list():
    assert find_max([]) == ""

# test_single_word.py
def test_single_word():
    assert find_max(["hello"]) == "hello"

# test_multiple_words_different_unique_chars.py
def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

# test_multiple_words_same_unique_chars_lexicographical_order.py
def test_multiple_words_same_unique_chars_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

# test_all_same_characters.py
def test_all_same_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

# test_mixed_case.py
def test_mixed_case():
    assert find_max(["Name", "enam", "Game"]) == "enam"

# test_numbers_and_letters.py
def test_numbers_and_letters():
    assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"