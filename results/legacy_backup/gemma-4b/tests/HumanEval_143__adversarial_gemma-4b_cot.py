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

    def test_single_word_prime(self):
        assert words_in_sentence("test") == "test"

    def test_single_word_non_prime(self):
        assert words_in_sentence("hello") == ""

    def test_multiple_words_some_prime(self):
        assert words_in_sentence("This is a test") == "is"

    def test_multiple_words_all_prime(self):
        assert words_in_sentence("let go for swimming") == "go for"

    def test_multiple_words_no_prime(self):
        assert words_in_sentence("This is a long sentence") == ""

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("This   is  a test") == "is"

    def test_prime_length_words_at_start_and_end(self):
        assert words_in_sentence("prime test another") == "prime test"

    def test_large_prime_length_word(self):
        assert words_in_sentence("abcdefghijk") == "abcdefghijk"

    def test_sentence_with_numbers(self):
        assert words_in_sentence("123 abc 456") == "abc"

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("hello! world?") == ""

    def test_sentence_with_mixed_case(self):
        assert words_in_sentence("ThIs Is A tEsT") == "is"