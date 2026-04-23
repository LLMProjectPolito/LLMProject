
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
    """Tests the specific examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

@pytest.mark.parametrize("input_list, expected", [
    (["apple", "apply", "ape"], "apple"),  # apple (4: a,p,l,e), apply (4: a,p,l,y), ape (3) -> apple < apply
    (["zebra", "apple", "apply"], "apple"), # apple (4), apply (4), zebra (5) -> zebra is max
    (["b", "a", "c"], "a"),                # All have 1 unique char, 'a' is lexicographically first
    (["dog", "cat", "bat"], "bat"),        # dog(3), cat(3), bat(3) -> bat is lexicographically first
])
def test_find_max_tie_breaking_logic(input_list, expected):
    """Tests that the tie-breaker (lexicographical order) works correctly."""
    assert find_max(input_list) == expected

def test_find_max_empty_list():
    """Tests behavior with an empty list. Assuming it returns None or handles gracefully."""
    # Depending on implementation, this might raise ValueError or return None.
    # Given the context of such problems, returning None or an empty string is common.
    # We will check for None as a standard robust implementation.
    try:
        result = find_max([])
        assert result is None or result == ""
    except ValueError:
        pass # If the function uses max() without a default, it raises ValueError

def test_find_max_single_element():
    """Tests a list with exactly one element."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_find_max_all_empty_strings():
    """Tests a list containing only empty strings."""
    assert find_max(["", "", ""]) == ""

def test_find_max_case_sensitivity():
    """Tests that uppercase and lowercase are treated as unique characters."""
    # 'A' (1 unique), 'a' (1 unique). 'A' comes before 'a' lexicographically.
    assert find_max(["a", "A"]) == "A"
    # 'Aa' (2 unique), 'ab' (2 unique). 'Aa' comes before 'ab'.
    assert find_max(["ab", "Aa"]) == "Aa"

def test_find_max_with_special_characters():
    """Tests that numbers and symbols are handled correctly."""
    # "123" (3 unique), "abc" (3 unique). "123" comes first lexicographically.
    assert find_max(["abc", "123"]) == "123"
    # "!@#" (3 unique), "!!!" (1 unique)
    assert find_max(["!!!", "!@#"]) == "!@#"

def test_find_max_long_strings_same_unique_count():
    """Tests long strings that have the same number of unique characters."""
    # "abcdef" (6 unique), "abcdeg" (6 unique)
    assert find_max(["abcdeg", "abcdef"]) == "abcdef"