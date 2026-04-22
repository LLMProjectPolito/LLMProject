
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

# STEP 1: REASONING
# The problem requires merging two pytest suites that both define the same function, 'find_max'.
# The function's goal is to find the word with the maximum number of unique characters in a list of words.
# If multiple words have the same maximum number of unique characters, the function should return the lexicographically smallest word among them.
# Both suites have identical function definitions and test cases.
# The goal is to create a single, comprehensive pytest suite that includes all the tests from both original suites, ensuring code reusability and avoiding redundancy.

# STEP 2: PLAN
# The plan is to combine the test functions from both suites into a single pytest file.
# The test functions will be named descriptively to reflect the scenarios they test.
# The test suite will cover various cases, including:
# 1. Basic cases with different words and varying numbers of unique characters.
# 2. Cases where multiple words have the same maximum number of unique characters.
# 3. Cases with empty input list.
# 4. Cases with words containing repeated characters.
# 5. Cases with words of different lengths.

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


@pytest.mark.parametrize(
    "words, expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "bca", "cab"], "abc"),
        (["a", "aa", "aaa"], "a"),
        (["", "abc", "def"], "abc"),
        (["abc", "def", "ghi"], "abc"),
        (["xyz", "abc", "def"], "xyz"),
        (["hello", "world", "python"], "python"),
        (["apple", "banana", "orange"], "banana"),
        (["a", "b", "c"], "a"),
        (["ab", "ac", "ba", "ca"], "ab"),
        ([], ""),
    ],
)
def test_find_max_basic(words, expected):
    assert find_max(words) == expected