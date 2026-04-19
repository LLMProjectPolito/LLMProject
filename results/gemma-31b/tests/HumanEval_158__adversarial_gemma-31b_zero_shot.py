
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
    Implementation of the function to be tested.
    """
    if not words:
        return None
    
    # We want to maximize unique characters (len(set(w)))
    # and minimize lexicographical order (w)
    # In Python, max() with a key can handle this. 
    # To handle the tie-breaker (lexicographical first), 
    # we can use a tuple: (unique_count, negative_lexicographical_order) 
    # OR more simply: sort the list lexicographically first, then use a stable max.
    
    # Correct logic: 
    # 1. Sort words lexicographically to handle the tie-breaker.
    # 2. Find the word with the maximum unique characters.
    # Since max() returns the first occurrence of the maximum value, 
    # sorting first ensures the lexicographically smallest is picked.
    
    sorted_words = sorted(words)
    return max(sorted_words, key=lambda w: len(set(w)))

class TestFindMax:
    @pytest.mark.parametrize("words, expected", [
        # Provided examples
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        
        # Edge Case: Empty list
        ([], None),
        
        # Edge Case: Single element
        (["hello"], "hello"),
        
        # Edge Case: Empty strings in list
        (["", "a"], "a"),
        (["", ""], ""),
        
        # Tie-breaker: Same unique count, different lengths
        # "abc" (3 unique), "aabbcc" (3 unique). "aabbcc" < "abc" lexicographically.
        (["abc", "aabbcc"], "aabbcc"),
        
        # Tie-breaker: Same unique count, different characters
        # "apple" (a,p,l,e = 4), "apply" (a,p,l,y = 4). "apple" < "apply".
        (["apply", "apple"], "apple"),
        
        # Case Sensitivity: 'A' and 'a' are different unique characters
        # "Aa" (2 unique), "a" (1 unique)
        (["Aa", "a"], "Aa"),
        
        # Special characters and numbers
        (["123", "abc", "!!!"], "!!!"), # "!!!" < "123" < "abc" lexicographically, all have 1 unique char
        
        # Large set of unique characters
        (["abcdefghijklmnopqrstuvwxyz", "abc"], "abcdefghijklmnopqrstuvwxyz"),
    ])
    def test_find_max_scenarios(self, words, expected):
        assert find_max(words) == expected

    def test_stability_with_identical_words(self):
        """Ensure that if the exact same word is repeated, it returns that word."""
        words = ["test", "test", "test"]
        assert find_max(words) == "test"

    def test_non_alphabetical_strings(self):
        """Test with strings containing spaces and symbols."""
        words = ["a b c", "abc", "  "]
        # "a b c" has {a, b, c, ' '} -> 4 unique
        # "abc" has {a, b, c} -> 3 unique
        # "  " has {' '} -> 1 unique
        assert find_max(words) == "a b c"