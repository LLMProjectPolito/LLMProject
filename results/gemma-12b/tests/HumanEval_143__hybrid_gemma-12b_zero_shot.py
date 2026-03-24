
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
        assert words_in_sentence("a b c d e f g") == "a b c d e f g"

    def test_long_sentence(self):
        """Test with a longer sentence."""
        sentence = "The quick brown fox jumps over the lazy dog"
        expected = "The fox over the dog"
        assert words_in_sentence(sentence) == expected

    def test_sentence_with_one_character_words(self):
        """Test with a sentence containing only one-character words."""
        assert words_in_sentence("a b c") == "a b c"

    def test_sentence_with_prime_and_non_prime_one_char_words(self):
        """Test with a sentence containing one-character words, some prime, some not."""
        assert words_in_sentence("a bb c") == "a c"

    def test_sentence_with_numbers_as_words(self):
        """Test with a sentence containing numbers as words (should still work)."""
        assert words_in_sentence("1 2 3 4 5") == "2 3 5"

    def test_sentence_with_special_characters(self):
        """Test with a sentence containing special characters (should ignore them)."""
        assert words_in_sentence("!@#$ %^&*()") == ""

    def test_sentence_with_unicode_characters(self):
        """Test with a sentence containing unicode characters."""
        assert words_in_sentence("你好 世界") == "" # Assuming unicode chars are not considered letters

    @pytest.mark.parametrize(
        "sentence, expected",
        [
            ("hello world", "world"),
            ("a b c d e", "a b c d e"),
            ("this is a very long sentence", "is a"),
            ("the quick brown fox jumps over the lazy dog", "The fox over the dog"),
            ("1 2 3 4 5 6 7 8 9 10", "2 3 5 7"),
        ],
    )
    def test_parametrize(self, sentence, expected):
        """Test using pytest.mark.parametrize for multiple test cases."""
        assert words_in_sentence(sentence) == expected

    def test_sentence_with_same_length_words(self):
        assert words_in_sentence("aa bb cc dd") == ""

    def test_sentence_with_one_letter_words(self):
        assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"

    def test_sentence_with_numbers_in_words(self):
        with pytest.raises(TypeError):
            words_in_sentence("This is 1 test")

    def test_sentence_with_special_characters(self):
        with pytest.raises(TypeError):
            words_in_sentence("This is a! test")

    def test_prime_length_at_end(self):
        assert words_in_sentence("This is a long test") == "is a"

    def test_prime_length_at_beginning(self):
        assert words_in_sentence("a This is a test") == "a"