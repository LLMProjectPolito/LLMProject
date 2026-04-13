
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

    def test_example_1(self):
        assert words_in_sentence("This is a test") == "is"

    def test_example_2(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_all_prime_words(self):
        assert words_in_sentence("is are was") == "is are was"

    def test_all_non_prime_words(self):
        assert words_in_sentence("a an the") == ""
        assert words_in_sentence("hello world test example") == ""

    def test_mixed_prime_and_non_prime(self):
        assert words_in_sentence("hello is a world") == "is"
        assert words_in_sentence("hello world is test") == "is"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  is a test  ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("is   a    test") == "is"

    def test_long_sentence(self):
        assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "quick"
        sentence = "This is a very long sentence with some prime words like go and to"
        assert words_in_sentence(sentence) == "go to"

    def test_sentence_with_long_prime_word(self):
        assert words_in_sentence("programming is fun") == "programming"

    def test_sentence_with_long_non_prime_word(self):
        assert words_in_sentence("abcdefghijk is fun") == "is"

    def test_sentence_with_numbers_and_letters(self):
        assert words_in_sentence("123 is a test") == "is"

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("is a test!") == "is"

    def test_sentence_with_uppercase_and_lowercase(self):
        assert words_in_sentence("Is a Test") == "Is"

    def test_sentence_with_repeated_words(self):
        assert words_in_sentence("is is is") == "is is is"

    def test_sentence_with_prime_and_composite_length_words(self):
        assert words_in_sentence("two three four five") == "three five"

    def test_multiple_prime_words(self):
        assert words_in_sentence("is a go to") == "is go to"

    def test_sentence_with_only_prime_length_words(self):
        assert words_in_sentence("is it a go") == "is it go"

    def test_sentence_with_numbers_as_words(self):
        # Although the prompt says only letters, test this edge case
        assert words_in_sentence("1 2 3 4 5") == "2 3 5"

    def test_sentence_with_special_characters(self):
        # Although the prompt says only letters, test this edge case
        assert words_in_sentence("hello! world? is.") == "is"

    def test_prime_word_at_start(self):
        assert words_in_sentence("go for swimming") == "go"

    def test_prime_word_at_end(self):
        assert words_in_sentence("swimming go for") == "go"

    def test_sentence_with_repeated_prime_words(self):
        assert words_in_sentence("is is is") == "is is is"