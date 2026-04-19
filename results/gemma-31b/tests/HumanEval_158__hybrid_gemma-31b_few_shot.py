
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

# =============================================================================
# IMPLEMENTATIONS
# =============================================================================

def find_max(words):
    """
    Returns the word with the maximum number of unique characters.
    Tie-breaker: Return the lexicographically smallest word.
    """
    if not words:
        return None
    
    # Step 1: Sort lexicographically first. 
    # Because Python's max() is stable (returns the first occurrence of the max),
    # sorting ensures the lexicographically first word is chosen in a tie.
    sorted_words = sorted(words)
    return max(sorted_words, key=lambda w: len(set(w)))

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """Returns the maximum element in a list, or None if empty."""
    return max(arr) if arr else None


# =============================================================================
# TESTS FOR find_max
# =============================================================================

@pytest.mark.parametrize("words, expected", [
    # Basic cases & Provided examples
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    
    # Clear winners (Unique count)
    (["apple", "banana", "cherry"], "cherry"), # cherry: 5, apple: 4, banana: 3
    (["a", "ab", "abc"], "abc"),
    (["aaaaa", "abc"], "abc"),
    (["python", "java", "c++"], "python"),
    
    # Lexicographical tie-breaking (Same unique count)
    (["pear", "apple"], "apple"), 
    (["zebra", "apple"], "apple"),
    (["cat", "dog", "bat"], "bat"),
    (["zzzz", "bbbb", "aaaa"], "aaaa"),
    (["hello", "world"], "hello"),
    
    # Different lengths, same unique count
    (["aaabbbccc", "aabbcc", "abc"], "abc"),
    
    # Mixed characters and numbers
    (["112", "123"], "123"),
    (["123", "111", "222"], "123"),
    
    # Single element and empty strings
    (["hello"], "hello"),
    (["", "a"], "a"),
    (["", ""], ""),
])
def test_find_max_scenarios(words, expected):
    """Tests a wide variety of standard and tie-breaking scenarios."""
    assert find_max(words) == expected

def test_find_max_empty_list():
    """Tests how the function handles an empty input list."""
    assert find_max([]) is None

def test_find_max_case_sensitivity():
    """
    Tests case sensitivity. 
    In ASCII, Uppercase comes before Lowercase.
    """
    # 'Ab' and 'ab' both have 2 unique chars. 'Ab' < 'ab'
    assert find_max(["Ab", "ab"]) == "Ab"
    # 'Aa' (2 unique) vs 'B' (1 unique)
    assert find_max(["Aa", "B"]) == "Aa"

def test_find_max_ascii_ordering():
    """Tests performance and correctness with long strings and ASCII boundaries."""
    word_lower = "abcdefghijklmnopqrstuvwxyz" # 26 unique
    word_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 26 unique
    # Uppercase letters have lower ASCII values than lowercase
    assert find_max([word_lower, word_upper]) == word_upper

# =============================================================================
# TESTS FOR is_palindrome
# =============================================================================

@pytest.mark.parametrize("s, expected", [
    ("radar", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("racecar", True),
    ("step on no pets", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected

# =============================================================================
# TESTS FOR get_max
# =============================================================================

@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3], 3),
    ([-1, -5, -2], -1),
    ([10], 10),
    ([], None),
])
def test_get_max(arr, expected):
    assert get_max(arr) == expected