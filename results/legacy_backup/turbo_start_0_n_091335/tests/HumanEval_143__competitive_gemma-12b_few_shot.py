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

    def test_example_1(self):
        assert words_in_sentence("This is a test") == "is"

    def test_example_2(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_no_prime_length_words(self):
        assert words_in_sentence("hello world") == ""

    def test_all_prime_length_words(self):
        assert words_in_sentence("a be do") == "a be do"

    def test_mixed_prime_and_non_prime_words(self):
        assert words_in_sentence("a be do hello") == "a be do"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  a be do  ") == "a be do"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("a   be  do") == "a be do"

    def test_single_word_prime_length(self):
        assert words_in_sentence("go") == "go"

    def test_single_word_non_prime_length(self):
        assert words_in_sentence("hello") == ""

    def test_long_sentence(self):
        sentence = "This is a very long sentence with some words of prime and non-prime lengths"
        expected = "is a very"
        assert words_in_sentence(sentence) == expected

    def test_sentence_with_numbers_in_words(self):
        assert words_in_sentence("a1 b2 c3") == ""

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("a! b@ c#") == ""