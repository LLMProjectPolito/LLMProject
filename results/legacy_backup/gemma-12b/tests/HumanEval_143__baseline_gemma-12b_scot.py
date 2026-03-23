import pytest

# STEP 1: REASONING
# The function `words_in_sentence` takes a sentence as input and returns a string containing words from the original sentence whose lengths are prime numbers, maintaining the original order.
# We need to test various scenarios including:
# 1. Empty sentence: Should return an empty string.
# 2. Sentence with no prime-length words: Should return an empty string.
# 3. Sentence with some prime-length words: Should return the prime-length words in the original order.
# 4. Sentence with all prime-length words: Should return all words in the original order.
# 5. Sentence with leading/trailing spaces: Should handle them correctly.
# 6. Sentence with multiple spaces between words: Should handle them correctly.
# 7. Sentence with single-character words (prime length): Should handle them correctly.
# 8. Sentence with longer words (prime length): Should handle them correctly.

# STEP 2: PLAN
# Test functions:
# - test_empty_sentence: Test with an empty sentence.
# - test_no_prime_words: Test with a sentence containing no prime-length words.
# - test_some_prime_words: Test with a sentence containing some prime-length words.
# - test_all_prime_words: Test with a sentence containing all prime-length words.
# - test_leading_trailing_spaces: Test with leading and trailing spaces.
# - test_multiple_spaces: Test with multiple spaces between words.
# - test_single_char_prime: Test with single-character prime-length words.
# - test_longer_prime_words: Test with longer prime-length words.

# STEP 3: CODE
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

    def test_no_prime_words(self):
        assert words_in_sentence("This is a test") == "is"

    def test_some_prime_words(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_all_prime_words(self):
        assert words_in_sentence("a is I") == "a is I"

    def test_leading_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_multiple_spaces(self):
        assert words_in_sentence("This  is   a    test") == "is"

    def test_single_char_prime(self):
        assert words_in_sentence("a b c d e") == "a b c d e"

    def test_longer_prime_words(self):
        assert words_in_sentence("This is a longer test sentence") == "This is a"