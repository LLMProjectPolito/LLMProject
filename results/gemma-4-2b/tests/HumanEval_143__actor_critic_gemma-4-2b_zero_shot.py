
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
from your_module import words_in_sentence  # Replace your_module

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestWordsInSentence:

    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_single_word_not_prime(self):
        assert words_in_sentence("abc") == ""

    def test_single_word_prime(self):
        assert words_in_sentence("abc") == "abc"

    def test_simple_case(self):
        assert words_in_sentence("This is a test") == "is"

    def test_another_simple_case(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_multiple_prime_words(self):
        assert words_in_sentence("The quick brown fox jumps over the lazy dog") == "quick brown"

    def test_mixed_prime_and_non_prime_words(self):
        assert words_in_sentence("This is a test sentence") == "is"

    def test_sentence_with_only_non_prime_words(self):
        assert words_in_sentence("abc def ghi") == ""

    def test_sentence_with_prime_words_at_start(self):
        assert words_in_sentence("abc is a test") == "is"

    def test_sentence_with_prime_words_at_end(self):
        assert words_in_sentence("a test is abc") == "is"

    def test_sentence_with_prime_words_in_middle(self):
        assert words_in_sentence("a test is abc") == "is"

    def test_long_sentence(self):
        sentence = "This is a very long sentence with many words"
        assert words_in_sentence(sentence) == "is"

    def test_sentence_with_numbers(self):
        assert words_in_sentence("123 abc def") == "def"

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("This sentence has !@#$%^&*()_+=-`~[]\{}|;':\",./<>?") == ""

    def test_sentence_with_spaces(self):
        assert words_in_sentence("  This  is   a   test  ") == "is"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("   This is a test   ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("This  is   a test") == "is"

    def test_sentence_with_only_spaces(self):
        assert words_in_sentence("   ") == ""

    def test_sentence_with_single_space(self):
        assert words_in_sentence("This ") == ""

    def test_sentence_with_only_spaces_and_a_word(self):
        assert words_in_sentence("   abc") == "abc"

    def test_sentence_with_spaces_and_punctuation(self):
        assert words_in_sentence("This is a test.") == "is"

    def test_sentence_with_mixed_case(self):
        assert words_in_sentence("This Is A Test") == "is"

    def test_sentence_with_unicode_characters(self):
        assert words_in_sentence("你好世界 abc") == "abc"

    def test_sentence_with_very_long_sentence(self):
        long_sentence = "a" * 1000 + "b"
        assert words_in_sentence(long_sentence) == "b"