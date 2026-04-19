
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
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.
    """
    if not words:
        return None
    
    # To handle the tie-breaker (lexicographically first), we sort the list 
    # alphabetically first. Since Python's max() is stable (returns the first 
    # occurrence in case of a tie), it will return the lexicographically smallest 
    # word among those with the maximum unique character count.
    sorted_words = sorted(words)
    return max(sorted_words, key=lambda w: len(set(w)))

class TestFindMax:
    @pytest.mark.parametrize("words, expected", [
        # Provided examples
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        
        # Tie-breaking: Same unique count, different lexicographical order
        (["cat", "bat", "rat"], "bat"),
        (["apple", "pear"], "apple"),    # both have 4 unique: 'apple' < 'pear'
        (["abc", "cba", "bac"], "abc"),  # all have 3 unique: 'abc' is smallest
        (["z", "y", "x"], "x"),          # all have 1 unique: 'x' is smallest
        
        # Length vs Unique count
        (["aaaaaaaaaa", "abc"], "abc"),               # 1 unique vs 3 unique
        (["abcdef", "aaaaaaaaaaaaaaaa"], "abcdef"),   # 6 unique vs 1 unique
        (["abcd", "abcde"], "abcde"),                 # 4 unique vs 5 unique
        
        # Case sensitivity (Assuming 'A' < 'a')
        (["Aa", "B"], "Aa"), # 'Aa' (2 unique) vs 'B' (1 unique)
        (["Aa", "ab"], "Aa"), # both have 2 unique: 'Aa' < 'ab'
        
        # Special characters and numbers
        # "123" (3 unique), "!!!" (1 unique), "abc" (3 unique) -> "123" is smallest of the max
        (["123", "!!!", "abc"], "123"),
        
        # Strings with identical unique sets but different lengths
        # "abc" (3 unique), "aabbcc" (3 unique) -> "aabbcc" < "abc"
        (["abc", "aabbcc"], "aabbcc"),
        
        # Edge Case: Empty strings and single items
        ([""], ""),                                  # Single empty string
        (["", ""], ""),                              # Multiple empty strings
        (["", "a"], "a"),                            # Empty string vs one char
        (["hello"], "hello"),                        # Single word list
    ])
    def test_find_max_scenarios(self, words, expected):
        assert find_max(words) == expected

    def test_empty_list(self):
        """Test behavior when an empty list is passed."""
        assert find_max([]) is None

    def test_identical_words(self):
        """Test behavior when the list contains identical strings."""
        assert find_max(["test", "test", "test"]) == "test"

    def test_large_input(self):
        """Test with a larger set of strings to ensure stability and performance."""
        # 100 different single-char strings. Lexicographically smallest is chr(100).
        words = [chr(i) for i in range(100, 200)] 
        assert find_max(words) == chr(100)

    def test_all_same_unique_count(self):
        """Test where all strings have the same number of unique characters."""
        words = ["cat", "dog", "bat"] # all 3 unique
        # Lexicographical order: bat, cat, dog
        assert find_max(words) == "bat"