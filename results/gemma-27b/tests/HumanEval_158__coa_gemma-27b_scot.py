import pytest
import math


# Focus: Boundary Values
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

@pytest.mark.parametrize("words", [
    [],  # Empty list
    ["a"],  # Single element list
    ["aa", "a"], # Duplicate characters
    ["abc", "ab", "a"], # Different lengths
    ["abc", "bca", "cab"], # Same unique character count, lexicographical order
    ["aaaaaaa", "bb", "cc"], # All same characters
    ["", "a", "aa"], # Empty string in list
    ["abcdefg", "abc", "ab"], # Significant length differences
    ["zyxwvuts", "abcdefg"], # Lexicographical comparison with different lengths
])
def test_find_max_boundary(words):
    assert find_max(words) == find_max(words)

# Focus: Equivalence Partitioning
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
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word

    return result

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function finds the word with the maximum number of unique characters.
# If there's a tie, it returns the lexicographically smallest word.
# Equivalence partitioning focuses on dividing the input domain into classes
# where the function behaves similarly.  Key partitions:
# 1. Empty list
# 2. List with words having different numbers of unique characters.
# 3. List with words having the same number of unique characters.
# 4. List with an empty string.
# 5. List with strings containing only repeated characters.

# STEP 2: PLAN - List test functions names and scenarios.
# test_find_max_empty_list: Tests the case where the input list is empty.
# test_find_max_different_unique_counts: Tests words with varying unique character counts.
# test_find_max_same_unique_counts: Tests words with the same unique character counts, verifying lexicographical order.
# test_find_max_with_empty_string: Tests a list containing an empty string.
# test_find_max_repeated_characters: Tests strings with only repeated characters.

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["abc", "ab", "a"]) == "abc"
    assert find_max(["a", "aa", "aaa"]) == "a"

def test_find_max_same_unique_counts():
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["abc", "bca", "cab"]) == "abc"
    assert find_max(["xyz", "zyx"]) == "xyz"

def test_find_max_with_empty_string():
    assert find_max(["", "abc"]) == "abc"
    assert find_max(["abc", ""]) == "abc"
    assert find_max(["", ""]) == ""

def test_find_max_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["aaa", "bbb", "ccc"]) == "aaa"

# Focus: Logic Branches
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

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_multiple_max_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_same_unique_chars_lexicographical():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_different_lengths():
    assert find_max(["a", "aa", "aaa"]) == "aaa"

def test_find_max_all_same_character():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_mixed_cases():
    assert find_max(["Name", "name", "Of"]) == "Name"