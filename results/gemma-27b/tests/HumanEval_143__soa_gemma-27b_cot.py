
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

class TestWordsInSentence:
    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_single_word_prime_length(self):
        assert words_in_sentence("two") == "two"

    def test_single_word_non_prime_length(self):
        assert words_in_sentence("three") == ""

    def test_multiple_words_mixed_lengths(self):
        assert words_in_sentence("This is a test") == "is"

    def test_multiple_words_all_prime(self):
        assert words_in_sentence("two five seven") == "two five seven"

    def test_multiple_words_all_non_prime(self):
        assert words_in_sentence("four six eight") == ""

    def test_example_1(self):
        assert words_in_sentence("This is a test") == "is"

    def test_example_2(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_long_sentence(self):
        assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the over dog"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  hello world  ") == "hello world"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("hello   world") == "hello world"

    def test_sentence_with_only_spaces(self):
        assert words_in_sentence("   ") == ""

    def test_sentence_with_prime_and_non_prime_adjacent(self):
        assert words_in_sentence("two three five") == "two five"

    def test_sentence_with_same_word_multiple_times(self):
        assert words_in_sentence("two two three") == "two two"

    def test_sentence_with_long_prime_word(self):
        assert words_in_sentence("programming is fun") == "programming"