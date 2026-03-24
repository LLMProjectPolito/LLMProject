
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

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

class TestWordsInSentence:
    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_single_prime_word(self):
        assert words_in_sentence("is") == "is"

    def test_single_non_prime_word(self):
        assert words_in_sentence("a") == ""
        assert words_in_sentence("test") == ""

    def test_multiple_words_some_prime(self):
        assert words_in_sentence("This is a test") == "is"

    def test_multiple_words_all_prime(self):
        assert words_in_sentence("go for") == "go for"

    def test_multiple_words_none_prime(self):
        assert words_in_sentence("hello world test") == ""

    def test_mixed_case(self):
        assert words_in_sentence("Is a Test") == "Is Test"

    def test_long_sentence(self):
        assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the over dog"

    def test_sentence_with_numbers(self):
        with pytest.raises(TypeError):
            words_in_sentence("123 abc")

    def test_sentence_with_symbols(self):
        with pytest.raises(TypeError):
            words_in_sentence("hello! world?")

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_prime_word_at_start(self):
        assert words_in_sentence("go to the store") == "go to"

    def test_prime_word_at_end(self):
        assert words_in_sentence("go to the end") == "go end"

    def test_sentence_with_only_prime_length_words(self):
        assert words_in_sentence("go no so") == "go no so"

    def test_sentence_with_long_prime_word(self):
        assert words_in_sentence("programming is fun") == "programming"

    def test_sentence_with_long_non_prime_word(self):
        assert words_in_sentence("supercalifragilisticexpialidocious is fun") == "is fun"

    def test_sentence_with_repeated_prime_words(self):
        assert words_in_sentence("go go go") == "go go go"

    def test_sentence_with_prime_and_composite_length_words(self):
        assert words_in_sentence("two three four five") == "three five"

    def test_sentence_with_repeated_words(self):
        assert words_in_sentence("is is is") == "is is is"