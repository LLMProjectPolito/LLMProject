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
# Edge cases: empty list, multiple strings with the same maximum unique characters.
# We need to test various scenarios including empty list, strings with different unique character counts, and strings with the same unique character counts.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: Should return an empty string.
# 2. Single word: Should return the word itself.
# 3. Multiple words with different unique character counts: Should return the word with the maximum unique characters.
# 4. Multiple words with the same maximum unique character count: Should return the lexicographically smallest word.
# 5. Words with all same characters: Should return the first word.
# 6. Mixed cases: Combination of different scenarios.

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

def test_mixed_cases():
    assert find_max(["abc", "ab", "abcd"]) == "abcd"

def test_mixed_cases_lexicographical():
    assert find_max(["abc", "ab", "bac"]) == "abc"

def test_empty_string_in_list():
    assert find_max(["", "abc", "def"]) == "abc"

def test_duplicate_words():
    assert find_max(["apple", "apple", "banana"]) == "apple"

def test_long_words():
    assert find_max(["supercalifragilisticexpialidocious", "hello"]) == "supercalifragilisticexpialidocious"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc"]) == "!@#"

def test_words_with_numbers():
    assert find_max(["123", "abc"]) == "123"

def test_words_with_mixed_characters():
    assert find_max(["a1b2c", "abc"]) == "a1b2c"