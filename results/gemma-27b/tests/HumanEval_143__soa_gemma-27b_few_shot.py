
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
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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
    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_single_prime_word(self):
        assert words_in_sentence("is") == "is"

    def test_single_non_prime_word(self):
        assert words_in_sentence("test") == ""

    def test_multiple_words_with_primes(self):
        assert words_in_sentence("This is a test") == "is"

    def test_multiple_words_with_no_primes(self):
        assert words_in_sentence("hello world test") == ""

    def test_mixed_words(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  hello world  ") == ""

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("hello   world") == ""

    def test_long_sentence(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        assert words_in_sentence(sentence) == "the over dog"

    def test_all_prime_length_words(self):
        sentence = "is it a"
        assert words_in_sentence(sentence) == "is it a"

    def test_sentence_with_numbers(self):
        with pytest.raises(TypeError):
            words_in_sentence("123 abc")

    def test_sentence_with_special_characters(self):
        with pytest.raises(TypeError):
            words_in_sentence("hello! world?")