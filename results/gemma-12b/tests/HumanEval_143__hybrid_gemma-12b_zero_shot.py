
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
from your_module import words_in_sentence  # Replace your_module

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestWordsInSentence:
    """Pytest class for testing the words_in_sentence function."""

    def test_empty_sentence(self):
        """Test with an empty sentence."""
        assert words_in_sentence("") == ""

    def test_no_prime_length_words(self):
        """Test with a sentence containing no words with prime length."""
        assert words_in_sentence("this is not a prime") == ""

    def test_single_prime_length_word(self):
        """Test with a sentence containing a single word with prime length."""
        assert words_in_sentence("a") == "a"

    def test_multiple_prime_length_words(self):
        """Test with a sentence containing multiple words with prime length."""
        assert words_in_sentence("This is a test") == "is"

    def test_mixed_prime_and_non_prime_words(self):
        """Test with a sentence containing both prime and non-prime length words."""
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_sentence_with_leading_and_trailing_spaces(self):
        """Test with a sentence containing leading and trailing spaces."""
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces_between_words(self):
        """Test with a sentence containing multiple spaces between words."""
        assert words_in_sentence("This  is   a    test") == "is"

    def test_sentence_with_all_prime_length_words(self):
        """Test with a sentence where all words have prime lengths."""
        assert words_in_sentence("a is go") == "a is go"

    def test_long_sentence(self):
        """Test with a longer sentence."""
        sentence = "This is a very long sentence with some words of prime and non-prime lengths"
        expected = "is a"
        assert words_in_sentence(sentence) == expected

    def test_sentence_with_one_character_words(self):
        """Test with a sentence containing only one-character words."""
        assert words_in_sentence("a b c d e") == "a b c d e"

    def test_sentence_with_prime_and_non_prime_one_char_words(self):
        """Test with a mix of one-char prime and non-prime words."""
        assert words_in_sentence("a bb c d e") == "a c e"

    def test_sentence_with_numbers_as_words(self):
        """Test with numbers as words (should still work as letters)."""
        assert words_in_sentence("1 2 3 4 5") == "2 3"

    def test_sentence_with_special_characters(self):
        """Test with special characters (should be ignored)."""
        assert words_in_sentence("!@#$ %^&*()") == ""

    def test_sentence_with_unicode_characters(self):
        """Test with unicode characters."""
        assert words_in_sentence("你好 世界") == "" # Assuming unicode characters are not considered letters

    @pytest.mark.parametrize(
        "sentence, expected",
        [
            ("abc def ghi", "def"),
            ("a b c d e f g", "a b c d e f g"),
            ("hello world", ""),
            ("the quick brown fox jumps over the lazy dog", "the"),
            ("a very long sentence", "a"),
        ],
    )
    def test_parametrize(self, sentence, expected):
        """Test using pytest.mark.parametrize for multiple test cases."""
        assert words_in_sentence(sentence) == expected

    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_no_prime_length_words(self):
        assert words_in_sentence("a bb ccc dddd") == ""

    def test_single_prime_length_word(self):
        assert words_in_sentence("a bb ccc dddd") == "a"

    def test_multiple_prime_length_words(self):
        assert words_in_sentence("This is a test") == "is"

    def test_mixed_prime_and_non_prime_words(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces_between_words(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_sentence_with_all_prime_length_words(self):
        assert words_in_sentence("a bb c d e") == "a bb c d e"

    def test_sentence_with_long_words(self):
        assert words_in_sentence("This is a very long sentence with some prime length words") == "is a"

    def test_sentence_with_same_length_words(self):
        assert words_in_sentence("aa bb cc dd") == ""

    def test_sentence_with_one_letter_words(self):
        assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"

    def test_sentence_with_numbers_in_words(self):
        with pytest.raises(TypeError):
            words_in_sentence("a1 b2 c3")

    def test_sentence_with_special_characters(self):
        with pytest.raises(TypeError):
            words_in_sentence("a! b@ c#")