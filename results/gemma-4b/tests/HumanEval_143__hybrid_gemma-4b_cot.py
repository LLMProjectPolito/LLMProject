
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestWordsInSentence:
    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_no_prime_length_words(self):
        assert words_in_sentence("This is a test") == ""

    def test_single_prime_length_word(self):
        assert words_in_sentence("is") == "is"

    def test_multiple_prime_length_words(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_mixed_prime_and_non_prime_words(self):
        assert words_in_sentence("This is a test sentence") == "is"

    def test_sentence_with_only_prime_length_words(self):
        assert words_in_sentence("abc def ghi") == "abc def"

    def test_sentence_with_long_prime_length_words(self):
        assert words_in_sentence("abcdefghijk") == "abcdefghijk"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_numbers(self):
        assert words_in_sentence("This is 123 test") == "is"

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("This is a!@# test") == "is"

    def test_prime_length_one(self):
        assert words_in_sentence("a") == "a"

    def test_prime_length_two(self):
        assert words_in_sentence("ab") == "ab"

    def test_prime_length_three(self):
        assert words_in_sentence("abc") == "abc"

    def test_prime_length_four(self):
        assert words_in_sentence("abcd") == ""

    def test_prime_length_five(self):
        assert words_in_sentence("abcde") == "abcde"