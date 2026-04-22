
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

def find_max(words):
    """
    Finds the word with the maximum number of unique characters.
    In case of a tie, returns the lexicographically smallest word.
    Returns None if the input list is empty.
    """
    if not words:
        return None
    
    # Calculate the maximum number of unique characters present in any word
    max_unique_count = max(len(set(word)) for word in words)
    
    # Filter all words that have this maximum count
    candidates = [word for word in words if len(set(word)) == max_unique_count]
    
    # Return the one that comes first lexicographically
    return min(candidates)

# --- Superior Pytest Suite ---

@pytest.mark.parametrize("input_list, expected", [
    # 1. Provided examples from problem description
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    
    # 2. Tie-breaking: Lexicographical order (all have same unique count)
    (["cat", "bat", "rat"], "bat"),
    (["zebra", "apple", "berry"], "apple"),
    (["c", "a", "b"], "a"),
    (["xy", "ab", "cd"], "ab"),
    
    # 3. Unique characters vs total length (length is irrelevant)
    (["aaaaaaa", "abc"], "abc"),      # 1 unique vs 3 unique
    (["aabbcc", "abc"], "aabbcc"),    # Both 3 unique, 'aabbcc' < 'abc'
    (["abcde", "aaaaa"], "abcde"),   # 5 unique vs 1 unique
    
    # 4. Case sensitivity (ASCII: 'A' (65) < 'a' (97))
    (["a", "A"], "A"),
    (["Apple", "apple"], "Apple"),
    (["aA", "b"], "aA"),
    (["aa", "Aa"], "Aa"),
    
    # 5. Special characters, numbers, and spaces
    (["a b", "abc"], "a b"),         # Both 3 unique, 'a b' < 'abc' (space < 'b')
    (["!@#", "#@!"], "!@#"),         # Both 3 unique, '!@#' < '#@!'
    (["123", "111", "22"], "123"),   # 3 unique vs 1 unique
    (["123", "111", "!@#"], "!@#"),  # Both 3 unique, '!@#' < '123'
    
    # 6. Single element and empty strings
    (["hello"], "hello"),
    (["a"], "a"),
    ([""], ""),
    (["", "a"], "a"),
    (["", ""], ""),
])
def test_find_max_logic(input_list, expected):
    """Tests core logic: unique character counts and lexicographical tie-breaking."""
    assert find_max(input_list) == expected

def test_find_max_empty_list():
    """Tests that an empty list returns None."""
    assert find_max([]) is None

def test_find_max_identical_elements():
    """Tests that a list of identical elements returns that element."""
    assert find_max(["test", "test", "test"]) == "test"

def test_find_max_large_input():
    """Tests correctness with a larger set of words and varying lengths."""
    words = ["a" * 100, "abcde", "fghij", "zzzzzzzzzz"]
    # "abcde" and "fghij" both have 5 unique characters. 
    # "abcde" is lexicographically smaller.
    assert find_max(words) == "abcde"