# STEP 1: REASONING
# The function `find_max` aims to find the word with the maximum number of unique characters in a list of strings.
# If there's a tie in the number of unique characters, it should return the lexicographically smallest word.
# The tests should cover:
#   - Empty list input
#   - List with a single word
#   - List with multiple words, where one word has the maximum unique characters
#   - List with multiple words, where multiple words have the same maximum number of unique characters (tie-breaker: lexicographical order)
#   - List with words containing repeated characters
#   - List with empty strings
#   - List with a mix of empty and non-empty strings

# STEP 2: PLAN
# 1. test_empty_list: Test with an empty list. Expected output: ""
# 2. test_single_word: Test with a list containing a single word. Expected output: the word itself.
# 3. test_multiple_words_unique_max: Test with multiple words, one having the maximum unique characters.
# 4. test_multiple_words_tie: Test with multiple words having the same maximum unique characters, verifying lexicographical order.
# 5. test_words_with_repeats: Test with words containing repeated characters.
# 6. test_empty_strings: Test with a list containing only empty strings. Expected output: ""
# 7. test_mixed_empty_and_non_empty: Test with a mix of empty and non-empty strings.
# 8. test_all_same_length: Test with words of the same length, but different unique characters.
# 9. test_long_strings: Test with longer strings to ensure efficiency.

# STEP 3: CODE
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

    max_unique = 0
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            result = word
        elif unique_chars == max_unique and word < result:
            result = word

    return result

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_unique_max():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_tie():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_repeats():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_mixed_empty_and_non_empty():
    assert find_max(["", "abc", "de"]) == "abc"

def test_all_same_length():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_long_strings():
    assert find_max(["abcdefgh", "ijklmnop", "qrstuvwx"]) == "abcdefgh"

def test_complex_case():
    assert find_max(["abcabcbb", "bbbbb", "pwwkew"]) == "pwwkew"

def test_tie_with_empty_string():
    assert find_max(["", "abc", ""]) == "abc"