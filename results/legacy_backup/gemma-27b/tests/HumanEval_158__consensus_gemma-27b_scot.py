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
    max_unique = 0
    max_word = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique and word < max_word:
            max_word = word
    return max_word

@pytest.mark.parametrize("words", [[]])
def test_empty_list(words):
    assert find_max(words) == ""

@pytest.mark.parametrize("words", [["hello"]])
def test_single_word(words):
    assert find_max(words) == "hello"

@pytest.mark.parametrize("words", [["name", "of", "string"]])
def test_multiple_words_different_unique_counts(words):
    assert find_max(words) == "string"

@pytest.mark.parametrize("words", [["name", "enam", "game"]])
def test_multiple_words_same_unique_counts_lexicographical_order(words):
    assert find_max(words) == "enam"

@pytest.mark.parametrize("words", [["", "abc", "de"]])
def test_words_with_empty_strings(words):
    assert find_max(words) == "abc"

@pytest.mark.parametrize("words", [["aaa", "bbb", "ccc"]])
def test_all_words_same_unique_chars(words):
    assert find_max(words) == "aaa"

@pytest.mark.parametrize("words", [["hello!", "world?", "python@"]])
def test_words_with_special_characters(words):
    assert find_max(words) == "python@"

@pytest.mark.parametrize("words", [["aaaaaaaaaa", "bbbbbbbbbb", "cccccccccc"]])
def test_long_words(words):
    assert find_max(words) == "aaaaaaaaaa"

@pytest.mark.parametrize("words", [["abc", "bca", "cab"]])
def test_cyclic_permutations(words):
    assert find_max(words) == "abc"

@pytest.mark.parametrize("words", [["abcde", "abcdf", "abcde"]])
def test_duplicate_max_words(words):
    assert find_max(words) == "abcde"

@pytest.mark.parametrize("words", [["aaaaaaa", "bb" ,"cc"]])
def test_words_with_repeated_chars(words):
    assert find_max(words) == "aaaaaaa"