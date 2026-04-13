
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
# We need to test various scenarios including empty list, list with one element, list with multiple elements, and cases where multiple strings have the same maximum number of unique characters.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with one element: ["word"]
# 3. List with multiple elements, one with maximum unique chars: ["name", "of", "string"]
# 4. List with multiple elements, multiple with maximum unique chars, check lexicographical order: ["name", "enam", "game"]
# 5. List with multiple elements, all with same unique chars, check lexicographical order: ["aaaaaaa", "bb", "cc"]
# 6. List with duplicate words, check correct behavior: ["apple", "apple"]
# 7. List with empty string: ["", "abc"]
# 8. List with special characters: ["!@#", "abc"]

### STEP 3: CODE
def test_empty_list():
    assert find_max([]) == ""

def test_single_element_list():
    assert find_max(["word"]) == "word"

def test_multiple_elements_max_unique():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_elements_max_unique_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_multiple_elements_same_max_unique_lexicographical():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_duplicate_words():
    assert find_max(["apple", "apple"]) == "apple"

def test_list_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_list_with_special_characters():
    assert find_max(["!@#", "abc"]) == "!@#"

def test_mixed_case():
    assert find_max(["Name", "name"]) == "Name"

def test_numbers_and_letters():
    assert find_max(["123", "abc"]) == "abc"

def test_long_word():
    assert find_max(["thisisalongword"]) == "thisisalongword"

def test_complex_case():
    assert find_max(["hello", "world", "programming"]) == "programming"

def test_another_complex_case():
    assert find_max(["abc", "def", "ghi"]) == "abc"