
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

# The function find_max is assumed to be imported or defined in the environment.
# Since I am not allowed to redefine it, I will write the test suite assuming 
# it is available in the global scope.

def test_provided_examples():
    """Verify the examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_lexicographical_tie_breaking():
    """
    Test that when unique character counts are tied, 
    the lexicographically first word is returned.
    """
    # All have 4 unique characters: {a, p, l, e}, {a, p, l, y}, {a, p, l, t}
    # Lexicographical order: apple < apply < aplat (hypothetical)
    # Let's use real words:
    # 'apple' -> a, p, l, e (4)
    # 'apply' -> a, p, l, y (4)
    # 'apple' comes before 'apply'
    assert find_max(["apply", "apple"]) == "apple"
    
    # 'b' (1), 'a' (1), 'c' (1) -> 'a' is first
    assert find_max(["b", "a", "c"]) == "a"

def test_empty_list():
    """
    Test behavior with an empty list. 
    Note: Depending on implementation, this might return None or raise an error.
    We assume a robust implementation returns None or handles it.
    """
    # If the function is expected to return None for empty input:
    try:
        result = find_max([])
        assert result is None or result == ""
    except (ValueError, IndexError):
        # If the function is expected to raise an error, this is also a valid behavior
        pass

def test_single_element():
    """Test a list with only one word."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_all_empty_strings():
    """Test a list containing only empty strings."""
    assert find_max(["", "", ""]) == ""

def test_case_sensitivity():
    """
    Test that case sensitivity is respected.
    'A' and 'a' are different characters.
    """
    # 'Aa' has 2 unique chars, 'aa' has 1 unique char.
    assert find_max(["Aa", "aa"]) == "Aa"
    
    # 'a' (1), 'A' (1). Lexicographically 'A' < 'a' (ASCII 65 < 97)
    assert find_max(["a", "A"]) == "A"

def test_special_characters_and_numbers():
    """Test that numbers and symbols are handled correctly."""
    # '123' (3 unique), '!@#' (3 unique)
    # Lexicographically '!' (33) comes before '1' (49)
    assert find_max(["123", "!@#"]) == "!@#"
    
    # 'abc' (3), '123' (3), '!!!' (1)
    # '123' comes before 'abc'
    assert find_max(["abc", "123", "!!!"]) == "123"

def test_varying_lengths_same_uniques():
    """
    Test words of different lengths that have the same number of unique characters.
    """
    # 'aaaaa' (1 unique: a)
    # 'b' (1 unique: b)
    # 'a' is lexicographically smaller than 'b'
    assert find_max(["aaaaa", "b"]) == "aaaaa"
    
    # 'abc' (3 unique)
    # 'aabbcc' (3 unique)
    # 'aabbcc' is lexicographically larger than 'abc'
    assert find_max(["aabbcc", "abc"]) == "abc"

@pytest.mark.parametrize("input_list, expected", [
    (["dog", "cat", "bird"], "bird"), # bird(4), dog(3), cat(3)
    (["apple", "pear", "peach"], "apple"), # apple(4), pear(4), peach(4) -> apple is first
    (["z", "y", "x"], "x"), # all 1 unique, x is first
    (["1212", "123"], "123"), # 1212(2), 123(3)
])
def test_parameterized_scenarios(input_list, expected):
    """Run multiple scenarios through a single test logic."""
    assert find_max(input_list) == expected