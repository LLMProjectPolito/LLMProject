
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
# The function `find_max` takes a list of strings as input and returns the string with the most unique characters.
# If multiple strings have the same maximum number of unique characters, it returns the lexicographically smallest one.
# The edge case is an empty input list, which should return an empty string.
# We need to test various scenarios including:
# 1. Empty input list
# 2. List with a single word
# 3. List with multiple words, some with more unique characters than others
# 4. List with multiple words having the same maximum number of unique characters (test lexicographical order)
# 5. List with words containing repeated characters

### STEP 2: PLAN
# Test cases:
# - test_empty_list: Empty input list
# - test_single_word: List with a single word
# - test_multiple_words_different_unique_chars: List with multiple words, some with more unique characters than others
# - test_multiple_words_same_unique_chars: List with multiple words having the same maximum number of unique characters (test lexicographical order)
# - test_repeated_chars: List with words containing repeated characters

### STEP 3: CODE
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_repeated_chars():
    assert find_max(["aabbcc", "abc"]) == "abc"

def test_mixed_case():
    assert find_max(["Name", "name"]) == "Name"

def test_numbers_and_letters():
    assert find_max(["a1b2c", "abc"]) == "a1b2c"

def test_empty_string_in_list():
    assert find_max(["", "abc"]) == "abc"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""