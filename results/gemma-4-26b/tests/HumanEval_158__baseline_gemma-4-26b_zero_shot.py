
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

def test_provided_examples():
    """Tests the specific examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

@pytest.mark.parametrize("words, expected", [
    (["abc", "abd", "abe"], "abc"),        # Tie in unique count (3), lexicographical order
    (["apple", "pear", "peach"], "peach"), # Different unique counts (4, 4, 5)
    (["z", "a", "b"], "a"),                # Tie in unique count (1), lexicographical order
    (["ab", "ba"], "ab"),                  # Tie in unique count (2), lexicographical order
    (["A", "a"], "A"),                     # Case sensitivity (ASCII 'A' < 'a')
    (["123", "122", "111"], "123"),        # Numbers (3 unique vs 2 vs 1)
    (["!@#", "#@!", "@!#"], "!@#"),        # Special characters
    (["banana", "apple"], "apple"),        # banana (3 unique) vs apple (4 unique)
])
def test_logic_variations(words, expected):
    """Tests various combinations of unique counts and lexicographical ties."""
    assert find_max(words) == expected

def test_single_element_list():
    """Tests a list containing only one word."""
    assert find_max(["hello"]) == "hello"

def test_empty_strings_in_list():
    """Tests lists containing empty strings."""
    assert find_max(["", "a", ""]) == "a"
    assert find_max(["", ""]) == ""

def test_empty_list():
    """Tests an empty list input. 
    Assuming the function returns None for an empty input.
    """
    assert find_max([]) is None

def test_all_identical_words():
    """Tests a list where all words are identical."""
    assert find_max(["test", "test", "test"]) == "test"

def test_case_sensitivity_complex():
    """Tests that unique character counts respect case sensitivity."""
    # 'Aa' has 2 unique characters, 'aa' has 1.
    assert find_max(["Aa", "aa"]) == "Aa"