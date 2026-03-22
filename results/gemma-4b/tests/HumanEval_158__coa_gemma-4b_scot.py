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
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_word = ""
    max_unique = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique and word < max_word:
            max_word = word

    return max_word

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `find_max` needs to be tested for boundary conditions related to the input list `words`.
### Specifically, we need to test empty lists, lists with only one word, lists with duplicate words,
### and lists where multiple words have the same maximum number of unique characters.
### The function should return the word with the maximum number of unique characters,
### prioritizing lexicographical order in case of ties.

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_empty_list: Tests the case where the input list is empty.
### - test_single_word: Tests the case where the input list contains only one word.
### - test_multiple_words_different_unique_chars: Tests the case where multiple words have different numbers of unique characters.
### - test_multiple_words_same_unique_chars_lexicographical_order: Tests the case where multiple words have the same number of unique characters and should be sorted lexicographically.

### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `find_max` needs to be tested for boundary conditions related to the input list `words`.
### Specifically, we need to test empty lists, lists with only one word, lists with duplicate words,
### and lists where multiple words have the same maximum number of unique characters.
### The function should return the word with the maximum number of unique characters,
### prioritizing lexicographical order in case of ties.

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_empty_list: Tests the case where the input list is empty.
### - test_single_word: Tests the case where the input list contains only one word.
### - test_multiple_words_different_unique_chars: Tests the case where multiple words have different numbers of unique characters.
### - test_multiple_words_same_unique_chars_lexicographical_order: Tests the case where multiple words have the same number of unique characters and should be sorted lexicographically.

### STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

# Focus: Type Scenarios
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


### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `find_max` should return the word with the most unique characters.
# If multiple words have the same number of unique characters, it should return the lexicographically smallest one.
# The function should handle empty input lists gracefully.

# STEP 2: PLAN - List test functions names and scenarios.
# test_find_max_empty_list
# test_find_max_single_word
# test_find_max_multiple_words_different_unique_counts
# test_find_max_multiple_words_same_unique_counts_lexicographical_order

# STEP 3: CODE - Write the high-quality pytest suite.
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_counts_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

# Focus: Logic Branches
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
    max_unique = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique and word < max_word:
            max_word = word

    return max_word

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `find_max` needs to find the word with the most unique characters.
### If multiple words have the same number of unique characters, it should return the lexicographically smallest one.
### Empty input list should return an empty string.
### STEP 2: PLAN - List test functions names and scenarios.
### test_find_max_empty_list
### test_find_max_single_word
### test_find_max_multiple_words_different_unique_counts
### test_find_max_multiple_words_same_unique_counts
### STEP 3: CODE - Write the high-quality pytest suite.

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_counts():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_multiple_words_same_unique_counts_lexicographical():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_mixed_case():
    assert find_max(["Name", "name"]) == "Name"