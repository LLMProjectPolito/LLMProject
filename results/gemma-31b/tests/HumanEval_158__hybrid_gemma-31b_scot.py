
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

class TestFindMax:
    """
    Comprehensive test suite for find_max(words).
    Criteria:
    1. Maximize number of unique characters.
    2. Tie-break: Lexicographically smallest string.
    """

    @pytest.mark.parametrize("words, expected", [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    ])
    def test_provided_examples(self, words, expected):
        """Verify the examples provided in the problem description."""
        assert find_max(words) == expected

    @pytest.mark.parametrize("words, expected", [
        # Unique count dominance: 'abcdef' (6) wins over 'zzzzzz' (1)
        (["zzzzzz", "abcdef"], "abcdef"),
        # Unique count dominance: 'world' (5) wins over 'hello' (4)
        (["hello", "world"], "world"),
        # Large unique set scaling
        (["a", "ab", "abc", "abcd", "abcde"], "abcde"),
    ])
    def test_unique_count_dominance(self, words, expected):
        """Test that the number of unique characters takes precedence over everything else."""
        assert find_max(words) == expected

    @pytest.mark.parametrize("words, expected", [
        # Tie-break: 'apple' (4 unique) vs 'apply' (4 unique) -> 'apple' is smaller
        (["apple", "apply"], "apple"),
        # Tie-break: 'dog' (3) vs 'cat' (3) -> 'cat' is smaller
        (["dog", "cat"], "cat"),
        # Tie-break: 'zebra' (5) vs 'apple' (5) -> 'apple' is smaller
        (["zebra", "apple"], "apple"),
        # Tie-break: Multiple options, 'abc' is smallest
        (["abc", "cba", "bac"], "abc"),
        # Tie-break: 'bat' is smallest among 3-unique strings
        (["cat", "bat", "rat"], "bat"),
        # Tie-break: 'dig' < 'dog'
        (["dog", "dig"], "dig"),
    ])
    def test_lexicographical_tie_break(self, words, expected):
        """Verify that the lexicographically first word is returned during ties."""
        assert find_max(words) == expected

    @pytest.mark.parametrize("words, expected", [
        # Length is ignored: 'aaaaa' (1 unique) vs 'bb' (1 unique) -> 'aaaaa' < 'bb'
        (["aaaaa", "bb"], "aaaaa"),
        # 'aa' (1 unique) vs 'zzzz' (1 unique) -> 'aa' < 'zzzz'
        (["zzzz", "aa"], "aa"),
        # All have 1 unique: 'a' is smallest
        (["a", "b", "c"], "a"),
        # All have 1 unique: 'aaaaa' is smallest
        (["aaaaa", "bbbbb", "ccccc"], "aaaaa"),
    ])
    def test_single_unique_char_behavior(self, words, expected):
        """Verify that string length is ignored in favor of unique count and lexicographical order."""
        assert find_max(words) == expected

    @pytest.mark.parametrize("words, expected", [
        # Case sensitivity: 'Apple' (A=65) < 'apple' (a=97)
        (["apple", "Apple"], "Apple"),
        # Mixed case tie-break: 'Apple' < 'Banana'
        (["Banana", "Apple"], "Apple"),
        # Numbers vs Letters: '123' < 'abc'
        (["abc", "123"], "123"),
        # Symbols vs Letters: '!@#' < 'abc'
        (["abc", "!@#"], "!@#"),
        # Symbol tie-break: '!' < '$'
        (["!@#", "$%^"], "!@#"),
        # Alphanumeric tie-break: 'a1b2' < 'c3d4'
        (["a1b2", "c3d4"], "a1b2"),
    ])
    def test_case_and_special_chars(self, words, expected):
        """Verify that ASCII values (case, numbers, symbols) are handled correctly."""
        assert find_max(words) == expected

    @pytest.mark.parametrize("words, expected", [
        (["hello"], "hello"),      # Single word
        ([""], ""),                # Single empty string
        (["", "a"], "a"),          # Empty string vs character
        (["", ""], ""),            # Multiple empty strings
    ])
    def test_string_edge_cases(self, words, expected):
        """Test behavior with empty strings and single-element lists."""
        assert find_max(words) == expected

    def test_empty_list_exception(self):
        """
        Verify behavior with an empty list.
        Standard Python max() raises ValueError on empty sequences.
        """
        with pytest.raises((ValueError, TypeError)):
            find_max([])