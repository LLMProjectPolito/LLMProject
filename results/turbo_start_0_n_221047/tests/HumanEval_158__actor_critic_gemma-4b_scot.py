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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `find_max` aims to find the word with the most unique characters
# in a given list of words. If multiple words have the same maximum number of
# unique characters, it should return the lexicographically smallest one.
# Edge cases include an empty input list, a list with only one word, and a
# list where multiple words have the same maximum number of unique characters.
# The function should handle strings with special characters and empty strings.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list: Test with an empty list of words.
# test_single_word: Test with a list containing only one word.
# test_multiple_words_different_unique_chars: Test with multiple words having
# different numbers of unique characters.
# test_multiple_words_same_unique_chars: Test with multiple words having the
# same number of unique characters, ensuring lexicographical order is maintained.
# test_empty_string: Test with an empty string in the list.
# test_special_characters: Test with words containing special characters.
# test_duplicate_words: Test with duplicate words in the list.
# test_lexicographical_order: Test with words that need to be compared lexicographically.


# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_empty_string():
    assert find_max(["aaaaaaa", "bb", "cc"]) == ""

def test_special_characters():
    assert find_max(["!@#", "abc", "def"]) == "!@#"

def test_duplicate_words():
    assert find_max(["apple", "apple", "banana"]) == "apple"

def test_lexicographical_order():
    assert find_max(["abc", "abd", "abe"]) == "abc"

def test_mixed_case():
    assert find_max(["Abc", "abc"]) == "abc"

def test_numbers_and_letters():
    assert find_max(["a123", "123a"]) == "a123"