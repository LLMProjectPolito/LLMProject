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
#   - Test case 1: Empty list - Should return ""
#   - Test case 2: Single word - Should return the word itself
#   - Test case 3: Multiple words with different unique character counts - Should return the word with the most unique characters.
#   - Test case 4: Multiple words with the same unique character count - Should return the lexicographically smallest word.
#   - Test case 5: Words with all same characters - Should return the first word.
#   - Test case 6: Mixed words - Should return the word with the most unique characters and lexicographically smallest if there are ties.
# STEP 3: CODE -
###
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

def test_mixed_words():
    assert find_max(["apple", "banana", "orange"]) == "banana"

def test_mixed_words_with_ties():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_mixed_words_with_ties_lexicographical():
    assert find_max(["abc", "acb", "bac"]) == "abc"

def test_words_with_duplicates():
    assert find_max(["aabbcc", "abc"]) == "aabbcc"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc"]) == "!@#"