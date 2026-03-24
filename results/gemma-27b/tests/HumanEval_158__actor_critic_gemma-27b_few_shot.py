
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    Args:
        words: A list of strings.

    Returns:
        The word with the maximum number of unique characters, or the
        lexicographically smallest word if multiple words have the same
        maximum number of unique characters.  Returns an empty string if the input list is empty.

    Raises:
        TypeError: if input is not a list or if list contains non-string elements

    Examples:
        find_max(["name", "of", "string"]) == "string"
        find_max(["name", "enam", "game"]) == "enam"
        find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
        find_max(["", "", ""]) == ""
        find_max(["abc", "a1b2c", "ab"]) == "a1b2c"
    """
    if not isinstance(words, list):
        raise TypeError("Input must be a list.")
    for word in words:
        if not isinstance(word, str):
            raise TypeError("List elements must be strings.")

    if not words:
        return ""

    max_unique = 0
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique:
            # Lexicographical comparison: word < max_word means word comes earlier
            if word < max_word:
                max_word = word

    return max_word
import pytest

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_same_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same_char():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_find_max_special_chars():
    assert find_max(["abc", "a1b2c", "ab"]) == "a1b2c"

def test_find_max_mixed_lengths():
    assert find_max(["a", "aa", "aaa", "aaaa"]) == "aaaa"

def test_find_max_numbers_and_letters():
    assert find_max(["123", "abc", "a1b"]) == "123"

def test_find_max_with_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_find_max_type_error():
    with pytest.raises(TypeError):
        find_max("not a list")

def test_find_max_type_error_element():
    with pytest.raises(TypeError):
        find_max([1, 2, 3])

def test_find_max_case_sensitivity():
    assert find_max(["aBc", "AbC", "abc"]) == "AbC"