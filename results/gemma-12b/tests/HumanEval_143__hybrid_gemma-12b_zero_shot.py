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

    def test_sentence_with_same_length_words(self):
        """Test with a sentence containing words of the same length."""
        assert words_in_sentence("aa bb cc") == ""

    def test_sentence_with_prime_length_words_at_start_and_end(self):
        """Test with prime length words at the beginning and end."""
        assert words_in_sentence("a This is a test b") == "a b"

    def test_sentence_with_non_prime_length_words_at_start_and_end(self):
        """Test with non-prime length words at the beginning and end."""
        assert words_in_sentence("This is a test abc") == "is"

    def test_sentence_with_mixed_lengths_and_order(self):
        """Test with a complex sentence with mixed lengths and order."""
        assert words_in_sentence("a bb c ddd e f g hhh") == "a c f"

    @pytest.mark.parametrize(
        "sentence, expected",
        [
            ("hello world", "world"),
            ("a b c d e", "a b c d e"),
            ("this is a long sentence", "is a"),
            ("the quick brown fox", "the fox"),
            ("one two three four five", "one two five"),
        ],
    )
    def test_parameterized_sentences(self, sentence, expected):
        """Test with a variety of sentences using pytest.mark.parametrize."""
        assert words_in_sentence(sentence) == expected

    def test_sentence_with_unicode_characters(self):
        assert words_in_sentence("你好 世界") == "" # Assuming unicode characters are not considered letters

    def test_sentence_with_mixed_case(self):
        assert words_in_sentence("This Is A Test") == "Is A"

    def test_sentence_with_numbers_in_words(self):
        with pytest.raises(TypeError):
            words_in_sentence("a1 b2 c3")

    def test_sentence_with_special_characters(self):
        with pytest.raises(TypeError):
            words_in_sentence("a! b@ c#")