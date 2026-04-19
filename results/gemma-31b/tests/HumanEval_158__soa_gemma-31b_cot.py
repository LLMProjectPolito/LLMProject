
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

@pytest.mark.parametrize("words, expected", [
    # Provided examples
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    
    # Tie-breaking: Lexicographical order (same unique count)
    (["apple", "pear"], "apple"),  # apple: 4 unique, pear: 4 unique. 'apple' < 'pear'
    (["zebra", "apple"], "apple"), # zebra: 5 unique, apple: 4 unique. 'zebra' wins on count.
    (["abc", "def", "ghi"], "abc"), # all 3 unique. 'abc' is smallest.
    
    # Unique character count priority
    (["banana", "apple"], "apple"), # banana: 3 unique (b,a,n), apple: 4 unique (a,p,l,e)
    (["abcdef", "ghijk"], "abcdef"), # 6 unique vs 5 unique
    
    # Edge cases: Single element
    (["hello"], "hello"),
    
    # Edge cases: Empty strings
    (["", "a"], "a"),
    (["", ""], ""),
    
    # Edge cases: Case sensitivity (assuming 'A' != 'a')
    (["Aa", "B"], "Aa"), # Aa: 2 unique, B: 1 unique
    (["a", "A"], "A"),   # both 1 unique, 'A' < 'a' in ASCII
    
    # Edge cases: Special characters and numbers
    (["123", "abc"], "123"), # both 3 unique, '123' < 'abc'
    (["!@#$", "abc"], "!@#$"), # 4 unique vs 3 unique
])
def test_find_max(words, expected):
    assert find_max(words) == expected

def test_find_max_empty_list():
    """Test behavior with an empty list. 
    Depending on implementation, this might return None or raise an error.
    Assuming it returns None or handles gracefully."""
    with pytest.raises(Exception): # Or assert find_max([]) is None
        find_max([])

def test_find_max_all_same_length_and_unique():
    """Test where all words are identical."""
    assert find_max(["test", "test", "test"]) == "test"

def test_find_max_varying_lengths_same_unique():
    """Test words with different lengths but same number of unique characters."""
    # "aaaaa" (1 unique), "bb" (1 unique), "c" (1 unique)
    # Lexicographically: "aaaaa" < "bb" < "c"
    assert find_max(["aaaaa", "bb", "c"]) == "aaaaa"