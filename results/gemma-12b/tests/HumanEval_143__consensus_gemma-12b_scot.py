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
        assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox"

    def test_sentence_with_single_prime_word(self):
        assert words_in_sentence("a bb ccc dddd eeeee") == "a"

    def test_sentence_with_multiple_prime_words(self):
        assert words_in_sentence("one two three four five six seven eight nine ten") == "one two three five seven"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  hello world  ") == "world"

    def test_sentence_with_multiple_spaces_between_words(self):
        assert words_in_sentence("hello   world") == "world"

    def test_sentence_with_long_prime_length_words(self):
        assert words_in_sentence("abcdefghijk abcdefghijklm abcdefghijklmn") == "abcdefghijk abcdefghijklmn"

    def test_sentence_with_short_prime_length_words(self):
        assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"