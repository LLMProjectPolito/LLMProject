
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

# The function words_in_sentence is assumed to be defined in the environment.

@pytest.mark.parametrize("sentence, expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
])
def test_provided_examples(sentence, expected):
    """Verify the examples explicitly provided in the problem description."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("a", ""),                # len 1: Not Prime
    ("is", "is"),             # len 2: Prime
    ("the", "the"),           # len 3: Prime
    ("test", ""),             # len 4: Not Prime
    ("apple", "apple"),       # len 5: Prime
    ("banana", ""),           # len 6: Not Prime
    ("science", "science"),   # len 7: Prime
    ("eighteen", ""),         # len 8: Not Prime
    ("ninechars", ""),        # len 9: Not Prime
    ("tenchars!!", ""),       # len 10: Not Prime
    ("programming", "programming"), # len 11: Prime
    ("extraordinary", "extraordinary"), # len 13: Prime
])
def test_primality_logic(sentence, expected):
    """Test individual word lengths to ensure primality logic is correct."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    # Mix: The(3-P), quick(5-P), brown(5-P), fox(3-P), jumps(5-P), over(4-NP), the(3-P), lazy(4-NP), dog(3-P)
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"),
    # All Prime
    ("is it he", "is it he"),
    # None Prime
    ("this that word", ""),
    # Single word prime
    ("Hello", "Hello"),
    # Single word non-prime
    ("Test", ""),
])
def test_sentence_compositions(sentence, expected):
    """Test various combinations of prime and non-prime word lengths."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("HELLO hello", "HELLO hello"), # Case insensitivity (both len 5)
    ("go  for", "go for"),           # Multiple spaces between words
    (" a ", ""),                     # Leading/trailing spaces with non-prime
    (" is ", "is"),                  # Leading/trailing spaces with prime
])
def test_edge_cases_and_constraints(sentence, expected):
    """Test robustness against formatting and case variations."""
    assert words_in_sentence(sentence) == expected

def test_length_constraints():
    """Test the boundary constraints for sentence length (1 <= len <= 100)."""
    # Minimum length: 1
    assert words_in_sentence("a") == ""
    
    # Maximum length: 100
    # 25 words of length 3 (prime) + 24 spaces = 75 + 24 = 99 chars.
    long_sentence = "abc " * 24 + "abc" 
    assert len(long_sentence) <= 100
    assert words_in_sentence(long_sentence) == long_sentence

    # Max length with non-primes: 11 words of length 8 + 10 spaces = 88 + 10 = 98 chars.
    long_non_prime = "eighteea " * 10 + "eighteea"
    assert len(long_non_prime) <= 100
    assert words_in_sentence(long_non_prime) == ""

def test_output_formatting():
    """Ensure the result string is trimmed and uses single spaces."""
    # "is"(2-P), "test"(4-NP)
    result = words_in_sentence("is test")
    assert result == "is"
    assert not result.startswith(" ")
    assert not result.endswith(" ")
    
    # "is"(2-P), "a"(1-NP), "the"(3-P)
    result_mid = words_in_sentence("is a the")
    assert result_mid == "is the"
    assert "  " not in result_mid # No double spaces