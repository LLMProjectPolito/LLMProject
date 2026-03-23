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
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    """Test with an empty sentence."""
    assert words_in_sentence("") == ""

def test_no_prime_words():
    """Test when no words have prime length."""
    assert words_in_sentence("This is a test") == ""

def test_single_prime_word():
    """Test with a single word of prime length."""
    assert words_in_sentence("is") == "is"

def test_multiple_prime_words():
    """Test with multiple words of prime length."""
    assert words_in_sentence("lets go for swimming") == "go for"

def test_all_prime_length_words():
    """Test when all words have prime length."""
    assert words_in_sentence("prime test") == "prime test"

def test_mixed_prime_and_non_prime_words():
    """Test with a mix of prime and non-prime length words."""
    assert words_in_sentence("This is a test sentence") == "is"

def test_long_sentence():
    """Test with a longer sentence."""
    assert words_in_sentence("This is a very long sentence with many words") == "is"

def test_sentence_with_numbers():
    """Test with a sentence containing numbers (should still work)."""
    assert words_in_sentence("123 is 456") == "is"

def test_sentence_with_special_characters():
    """Test with a sentence containing special characters (should still work)."""
    assert words_in_sentence("hello! world?") == ""

def test_prime_length_word_at_start():
    """Test when a prime length word is at the beginning of the sentence."""
    assert words_in_sentence("two three") == "two three"

def test_prime_length_word_at_end():
    """Test when a prime length word is at the end of the sentence."""
    assert words_in_sentence("one two three") == "one two three"