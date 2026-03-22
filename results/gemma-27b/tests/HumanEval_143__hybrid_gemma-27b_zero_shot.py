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
        assert words_in_sentence("this") == ""
        assert words_in_sentence("a") == ""

    def test_example_1(self):
        assert words_in_sentence("This is a test") == "is"

    def test_example_2(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_multiple_prime_words(self):
        assert words_in_sentence("is a go to") == "is go to"

    def test_mixed_prime_and_non_prime(self):
        assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox over"

    def test_all_non_prime_words(self):
        assert words_in_sentence("hello world python programming") == ""

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  is a test  ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("is  a   test") == "is test"

    def test_long_sentence(self):
        sentence = "a very long sentence with some prime and non prime words"
        assert words_in_sentence(sentence) == "very long some"

    def test_sentence_with_same_word_multiple_times(self):
        assert words_in_sentence("is is is a test") == "is is is"

    def test_prime_word_at_start_and_end(self):
        assert words_in_sentence("is a test is") == "is is"

    def test_sentence_with_only_prime_words(self):
        assert words_in_sentence("is it a go") == "is it go"

    def test_sentence_with_numbers_as_words(self):
        # Although the prompt says only letters, testing for robustness
        assert words_in_sentence("1 2 3 4 5") == ""

    def test_sentence_with_special_characters(self):
        # Although the prompt says only letters, testing for robustness
        assert words_in_sentence("is! a? test.") == "is"

    def test_sentence_with_mixed_case(self):
        assert words_in_sentence("Is a Test") == "Is Test"

    def test_sentence_with_long_prime_word(self):
        assert words_in_sentence("programming is fun") == "programming"

    def test_all_prime_words(self):
        assert words_in_sentence("is are was") == "is are was"

    def test_sentence_with_long_non_prime_word(self):
        assert words_in_sentence("abcdefghijk is fun") == "is"

    def test_sentence_with_uppercase_and_lowercase(self):
        assert words_in_sentence("Is a Test") == "Is Test"