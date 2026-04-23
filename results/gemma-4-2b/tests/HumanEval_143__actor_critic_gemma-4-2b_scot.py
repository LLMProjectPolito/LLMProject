
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
from typing import List

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def words_in_sentence(sentence: str) -> str:
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
    result = ""
    for word in words:
        if len(word) > 0 and is_prime(len(word)):
            result += word
    return result


class TestWordsInSentence:

    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_no_prime_length_words(self):
        assert words_in_sentence("abc def ghi") == ""

    def test_only_prime_length_words(self):
        assert words_in_sentence("abc def ghi") == "abc def ghi"

    def test_mixed_prime_and_non_prime_length_words(self):
        assert words_in_sentence("This is a test") == "is"
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_single_word_prime_length(self):
        assert words_in_sentence("is") == "is"

    def test_single_word_non_prime_length(self):
        assert words_in_sentence("abc") == ""

    def test_longer_sentence(self):
        assert words_in_sentence("This is a very long sentence with some words") == "is a"

    def test_spaces_only(self):
        assert words_in_sentence("   ") == ""

    def test_special_characters(self):
        assert words_in_sentence("This sentence has !@#$%^&*()_+=-`~[]\{}|;':\",./<>?") == ""

    def test_spaces_only_explicit(self):
        assert words_in_sentence("   ") == ""

    def test_very_long_sentence(self):
        long_sentence = "This is a very long sentence with many words to test performance. " * 100
        assert words_in_sentence(long_sentence) == "is a"

    def test_multiple_same_prime_length_words(self):
        assert words_in_sentence("is is is") == "is is is"