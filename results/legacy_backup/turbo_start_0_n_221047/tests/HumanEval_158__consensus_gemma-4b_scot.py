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
# STEP 1: REASONING - The function `find_max` aims to find the word with the most unique characters in a list of strings. If multiple words have the same maximum number of unique characters, it should return the lexicographically smallest one. Edge cases include an empty input list.

# STEP 2: PLAN -
# Test cases:
# 1. Empty list: Should return an empty string.
# 2. Single word: Should return the word itself.
# 3. Multiple words with different unique character counts: Should return the word with the maximum count.
# 4. Multiple words with the same maximum unique character count: Should return the lexicographically smallest word.
# 5. Words with repeated characters: Should correctly calculate unique characters.
# 6. Mixed case words: Should handle case sensitivity correctly.

# Test functions:
# test_empty_list
# test_single_word
# test_multiple_words_different_counts
# test_multiple_words_same_counts
# test_words_with_repeated_characters
# test_mixed_case_words


# STEP 3: CODE -
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_counts():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == ""aaaaaaa"

def test_mixed_case_words():
    assert find_max(["Name", "enam", "Game"]) == "enam"

def test_multiple_words_same_counts_lexicographical():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_words_with_spaces():
    assert find_max(["hello world", "hello"]) == "hello world"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc"]) == "!@#"

def test_all_same_characters():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"