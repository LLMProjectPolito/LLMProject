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
# STEP 1: REASONING - The function `find_max` takes a list of strings as input and returns the string with the most unique characters. If multiple strings have the same number of unique characters, it returns the lexicographically smallest one. The edge case of an empty input list should be handled.
# STEP 2: PLAN -
#   - Test case 1: Empty list input.
#   - Test case 2: List with one word.
#   - Test case 3: List with multiple words, one with more unique characters.
#   - Test case 4: List with multiple words, some with the same number of unique characters, and one should be lexicographically smaller.
#   - Test case 5: List with duplicate words.
#   - Test case 6: List with words containing special characters.
# STEP 3: CODE -
###
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_more_unique():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_multiple_words_same_unique_lexicographical_reverse():
    assert find_max(["game", "enam", "name"]) == "enam"

def test_duplicate_words():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc", "def"]) == "!@#"

def test_mixed_case():
    assert find_max(["Name", "name"]) == "Name"

def test_empty_string_in_list():
    assert find_max(["", "abc", "def"]) == "abc"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_long_words():
    assert find_max(["abcdefgh", "ijklmnop"]) == "abcdefgh"

def test_words_with_same_unique_chars_and_length():
    assert find_max(["abc", "def"]) == "abc"