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

### STEP 1: REASONING
# The function `find_max` takes a list of strings as input and returns the string with the most unique characters.
# If multiple strings have the same maximum number of unique characters, it returns the lexicographically smallest one.
# The function should handle empty input lists gracefully.
# Test cases should cover various scenarios: empty list, list with one element, list with multiple elements,
# list with strings having different numbers of unique characters, and list with strings having the same number of unique characters.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with one element: ["word"]
# 3. List with multiple elements, different unique character counts: ["abc", "ab", "a"]
# 4. List with multiple elements, same unique character counts, different lexicographical order: ["abc", "acb", "bac"]
# 5. List with multiple elements, same unique character counts, same lexicographical order: ["abc", "abc"]
# 6. List with strings containing special characters: ["!@#", "abc"]
# 7. List with empty strings: ["", "abc"]
# 8. List with mixed case strings: ["Abc", "abc"]

### STEP 3: CODE
def test_empty_list():
    assert find_max([]) == ""

def test_single_element_list():
    assert find_max(["word"]) == "word"

def test_different_unique_counts():
    assert find_max(["abc", "ab", "a"]) == "abc"

def test_same_unique_counts_different_lexicographical_order():
    assert find_max(["abc", "acb", "bac"]) == "abc"

def test_same_unique_counts_same_lexicographical_order():
    assert find_max(["abc", "abc"]) == "abc"

def test_special_characters():
    assert find_max(["!@#", "abc"]) == "!@#"

def test_empty_string():
    assert find_max(["", "abc"]) == ""

def test_mixed_case_strings():
    assert find_max(["Abc", "abc"]) == "Abc"

def test_example_1():
    assert find_max(["name", "of", "string"]) == "string"

def test_example_2():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_example_3():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"