
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

def test_find_max_provided_examples():
    """Test the examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_single_element():
    """Test with a list containing only one string."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_find_max_empty_list():
    """Test with an empty list. Depending on implementation, this might raise ValueError or return None."""
    # Since the problem doesn't specify, we assume it might return None or raise an error.
    # If the function uses max(), it will raise a ValueError.
    with pytest.raises(ValueError):
        find_max([])

def test_find_max_lexicographical_tie():
    """Test that the lexicographically first word is returned when unique counts are equal."""
    # 'apple' and 'apply' both have 4 unique characters: {a, p, l, e} and {a, p, l, y}
    # 'apple' < 'apply'
    assert find_max(["apply", "apple"]) == "apple"
    
    # 'abc' and 'abd' both have 3 unique characters
    assert find_max(["abd", "abc"]) == "abc"

def test_find_max_all_same_unique_count():
    """Test when all words have the same number of unique characters."""
    assert find_max(["c", "b", "a"]) == "a"
    assert find_max(["zzz", "yyy", "xxx"]) == "xxx"

def test_find_max_different_lengths_same_unique():
    """Test words with different lengths but the same number of unique characters."""
    # 'aaaaa' has 1 unique char, 'b' has 1 unique char. 'aaaaa' < 'b'
    assert find_max(["aaaaa", "b"]) == "aaaaa"
    # 'bb' has 1 unique char, 'aaaaa' has 1 unique char. 'aaaaa' < 'bb'
    assert find_max(["bb", "aaaaa"]) == "aaaaa"

def test_find_max_case_sensitivity():
    """Test that unique character counting is case-sensitive."""
    # 'Aa' has 2 unique characters, 'a' has 1.
    assert find_max(["Aa", "a"]) == "Aa"
    # 'Apple' (A, p, l, e) has 4, 'apple' (a, p, l, e) has 4.
    # 'Apple' < 'apple' (Uppercase comes before lowercase in ASCII)
    assert find_max(["apple", "Apple"]) == "Apple"

def test_find_max_special_characters():
    """Test with strings containing spaces and special characters."""
    # 'a b' has 3 unique characters ('a', ' ', 'b')
    # 'ab' has 2 unique characters
    assert find_max(["a b", "ab"]) == "a b"
    # '!@#' (3) vs '$%^' (3). '!@#' < '$%^'
    assert find_max(["$%^", "!@#"]) == "!@#"

@pytest.mark.parametrize("words, expected", [
    (["python", "java", "c++"], "python"), # python: 6, java: 3, c++: 2
    (["test", "tess"], "tess"),           # test: 3, tess: 3. tess < test
    (["", ""], ""),                       # empty strings
    (["123", "111", "222"], "123"),       # numbers as strings
])
def test_find_max_parametrized(words, expected):
    """Run a variety of test cases using parametrization."""
    assert find_max(words) == expected