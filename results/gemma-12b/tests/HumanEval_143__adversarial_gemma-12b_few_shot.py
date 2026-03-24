
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
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)


class TestWordsInSentence:
    def test_basic_case(self):
        assert words_in_sentence("This is a test") == "is"

    def test_another_basic_case(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_no_prime_length_words(self):
        assert words_in_sentence("hello world") == ""

    def test_all_prime_length_words(self):
        assert words_in_sentence("a is be do") == "a is be do"

    def test_mixed_prime_and_non_prime(self):
        assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  hello world  ") == "world"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("hello   world") == "world"

    def test_sentence_with_single_prime_word(self):
        assert words_in_sentence("a b c d e") == "a"

    def test_sentence_with_long_prime_length_words(self):
        assert words_in_sentence("this is a very long prime word") == "is a"

    def test_sentence_with_numbers_in_words(self):
        assert words_in_sentence("word1 word2 word3") == "" #Numbers are not letters

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("word! word@ word#") == "" #Special characters are not letters