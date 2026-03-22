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
# Edge cases: Empty input list.
# Test cases: Provided examples and additional cases to cover different scenarios (e.g., all same characters, empty strings).

### STEP 2: PLAN
# Test cases:
# 1. Empty list: Should return an empty string.
# 2. Single word: Should return the word itself.
# 3. Multiple words with different unique character counts: Should return the word with the most unique characters.
# 4. Multiple words with the same unique character count: Should return the lexicographically smallest word.
# 5. Words with all same characters: Should return the first word in the list.
# 6. Empty strings in the list: Should handle them correctly.

### STEP 3: CODE
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_multiple_words_same_unique_chars_all_same():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_empty_string():
    assert find_max(["hello", ""]) == "hello"

def test_words_with_mixed_case():
    assert find_max(["Name", "name"]) == "Name"

def test_words_with_numbers():
    assert find_max(["word123", "word"]) == "word123"

def test_words_with_special_characters():
    assert find_max(["word!", "word"]) == "word!"

def test_words_with_duplicate_characters():
    assert find_max(["aabbcc", "abc"]) == "abc"