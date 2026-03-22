import pytest

def is_prime(n):
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
    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_no_prime_length_words(self):
        assert words_in_sentence("this is a test") == "is"

    def test_all_prime_length_words(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_mixed_prime_and_non_prime_words(self):
        assert words_in_sentence("This is a very long test") == "is a"

    def test_single_prime_length_word(self):
        assert words_in_sentence("a") == "a"

    def test_single_non_prime_length_word(self):
        assert words_in_sentence("this") == ""

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces_between_words(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_sentence_with_only_spaces(self):
        assert words_in_sentence("   ") == ""

    def test_long_sentence(self):
        sentence = "This is a very very very long sentence with some prime and non-prime words"
        expected = "is a very"
        assert words_in_sentence(sentence) == expected

    def test_sentence_with_same_length_words(self):
        assert words_in_sentence("go do re mi") == "go do"

    def test_prime_length_words_at_end(self):
        assert words_in_sentence("This is a long test go") == "is go"

    def test_non_prime_length_words_at_end(self):
        assert words_in_sentence("This is a long test") == "is a"