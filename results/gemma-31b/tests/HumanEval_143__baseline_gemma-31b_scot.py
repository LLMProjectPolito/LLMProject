
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

import pytest

def is_prime(n):
    """Helper to verify prime logic if needed, though we test the main function."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestWordsInSentence:
    def test_example_1(self):
        """Test Example 1: 'This is a test' -> 'is' (Lengths: 4, 2, 1, 4)"""
        assert words_in_sentence("This is a test") == "is"

    def test_example_2(self):
        """Test Example 2: 'lets go for swimming' -> 'go for' (Lengths: 4, 2, 3, 8)"""
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_no_primes(self):
        """Test sentence where no words have prime lengths (1 is not prime)."""
        assert words_in_sentence("a b c d") == ""
        assert words_in_sentence("test this that") == "" # Lengths: 4, 4, 4

    def test_all_primes(self):
        """Test sentence where all words have prime lengths."""
        # Lengths: 2, 3, 5 (all prime)
        assert words_in_sentence("it the apple") == "it the apple"

    def test_single_word_prime(self):
        """Test a single word that has a prime length."""
        assert words_in_sentence("apple") == "apple" # Length 5

    def test_single_word_non_prime(self):
        """Test a single word that does not have a prime length."""
        assert words_in_sentence("test") == "" # Length 4
        assert words_in_sentence("a") == "" # Length 1

    def test_mixed_primes(self):
        """Test a complex sentence with various prime and non-prime lengths."""
        # The(3-P), quick(5-P), brown(5-P), fox(3-P), jumps(5-P), over(4-NP), the(3-P), lazy(4-NP), dog(3-P)
        sentence = "The quick brown fox jumps over the lazy dog"
        expected = "The quick brown fox jumps the dog"
        assert words_in_sentence(sentence) == expected

    def test_large_prime_length(self):
        """Test words with larger prime lengths (e.g., 7, 11)."""
        # 'through' (7), 'communication' (13)
        sentence = "through communication"
        assert words_in_sentence(sentence) == "through communication"

    def test_boundary_length_one(self):
        """Test the smallest possible sentence length constraint."""
        assert words_in_sentence("a") == ""
        assert words_in_sentence("is") == "is"

    def test_max_length_constraint(self):
        """Test a sentence approaching the 100 character limit."""
        # 10 words of length 9 (non-prime) + 9 spaces = 99 chars
        sentence = "ninechars " * 9 + "ninechars" 
        assert words_in_sentence(sentence) == ""
        
        # 10 words of length 7 (prime) + 9 spaces = 79 chars
        sentence_prime = "sevench " * 9 + "sevench"
        assert words_in_sentence(sentence_prime) == sentence_prime