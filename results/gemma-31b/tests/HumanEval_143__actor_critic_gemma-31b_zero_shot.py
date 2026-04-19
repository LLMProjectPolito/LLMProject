
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
    Returns a string containing words from the original sentence whose lengths are prime numbers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_length_words)

# --- Pytest Suite ---

def test_example_1():
    """Test Example 1 from the problem description."""
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    """Test Example 2 from the problem description."""
    assert words_in_sentence("lets go for swimming") == "go for"

def test_no_prime_lengths():
    """Test sentence where no words have prime lengths (1, 4, 6, 8, 9, 10...)."""
    # 'a' (1), 'test' (4), 'banana' (6)
    assert words_in_sentence("a test banana") == ""

def test_all_prime_lengths():
    """Test sentence where all words have prime lengths (2, 3, 5, 7...)."""
    # 'is' (2), 'the' (3), 'apple' (5), 'quality' (7)
    assert words_in_sentence("is the apple quality") == "is the apple quality"

def test_single_character_word():
    """Test that words of length 1 are not considered prime."""
    assert words_in_sentence("a i o") == ""

def test_two_character_word():
    """Test that words of length 2 are considered prime."""
    assert words_in_sentence("it is") == "it is"

def test_three_character_word():
    """Test that words of length 3 are considered prime."""
    assert words_in_sentence("the cat") == "the cat"

def test_four_character_word():
    """Test that words of length 4 are not considered prime."""
    assert words_in_sentence("word test") == ""

def test_long_prime_length():
    """Test words with larger prime lengths (e.g., 11, 13)."""
    # 'extraordinary' is 13 chars (prime)
    # 'responsibility' is 14 chars (not prime)
    assert words_in_sentence("extraordinary responsibility") == "extraordinary"

def test_single_word_sentence():
    """Test a sentence consisting of only one word."""
    assert words_in_sentence("hello") == "hello"  # 5 is prime
    assert words_in_sentence("test") == ""        # 4 is not prime

def test_empty_or_whitespace_string():
    """Test edge cases with empty or whitespace-only strings."""
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""

def test_multiple_spaces():
    """Test that multiple spaces between words are handled correctly."""
    assert words_in_sentence("go    for   swimming") == "go for"

def test_max_constraint_length():
    """Test a sentence near the maximum constraint length (100)."""
    # 10 words of length 9 (not prime) + 9 spaces = 99 chars
    sentence = "ninechars " * 9 + "ninechars"
    assert words_in_sentence(sentence) == ""
    
    # 10 words of length 7 (prime) + 9 spaces = 79 chars
    sentence_prime = "sevench " * 9 + "sevench"
    assert words_in_sentence(sentence_prime) == sentence_prime