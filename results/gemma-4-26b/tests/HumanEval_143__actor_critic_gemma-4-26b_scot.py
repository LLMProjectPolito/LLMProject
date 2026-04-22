
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

def test_provided_examples():
    """Tests the examples provided in the problem description."""
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

@pytest.mark.parametrize("sentence, expected", [
    ("abcd efgh", ""),        # Lengths 4 and 4 are not prime
    ("a b c d", ""),          # All length 1 (not prime)
    ("python code", ""),      # Lengths 6 and 4 are not prime
])
def test_no_prime_lengths(sentence, expected):
    """Tests sentences where no words have prime lengths."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("is go for", "is go for"),       # Lengths 2, 2, 3 (all prime)
    ("it is up", "it is up"),         # Lengths 2, 2, 2 (all prime)
    ("abc de fghij", "abc de fghij"), # Lengths 3, 2, 5 (all prime)
])
def test_all_prime_lengths(sentence, expected):
    """Tests sentences where every word has a prime length."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("is", "is"),              # Single word, prime length (2)
    ("this", ""),              # Single word, non-prime length (4)
    ("a", ""),                 # Single word, length 1 (not prime)
    ("apple", "apple"),        # Single word, prime length (5)
])
def test_single_word_scenarios(sentence, expected):
    """Tests various single-word sentence scenarios."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("the cat sat on a mat", "the cat sat on mat"), # 3, 3, 3, 2, 1, 3 -> 3, 3, 3, 2, 3
    ("python is fun", "is fun"),                   # 6, 2, 3 -> 2, 3
    ("a prime number is two", "prime is two"),     # 1, 5, 6, 2, 3 -> 5, 2, 3
    ("testing various word lengths", "testing various lengths"), # 7, 7, 4, 7 -> 7, 7, 7
])
def test_mixed_lengths(sentence, expected):
    """Tests sentences with a mix of prime and non-prime word lengths."""
    assert words_in_sentence(sentence) == expected

def test_boundary_prime_lengths():
    """Tests specific boundary cases for prime numbers (2, 3, 4, 5)."""
    # 2 is prime, 3 is prime, 4 is not, 5 is prime
    sentence = "ab abc abcd abcde"
    assert words_in_sentence(sentence) == "ab abc abcde"

def test_long_sentence_constraint():
    """Tests a sentence approaching the maximum constraint length with strong assertion."""
    # 100 characters max. 
    # "is" repeated 25 times is 75 characters.
    sentence = "is " * 25
    expected = "is " * 24 + "is" 
    assert words_in_sentence(sentence) == expected

def test_empty_string():
    """Tests how the function handles an empty string."""
    assert words_in_sentence("") == ""

@pytest.mark.parametrize("sentence, expected", [
    ("  is   fun  ", "is fun"),       # Leading, trailing, and multiple internal spaces
    ("is\nfun", "is fun"),            # Newlines (if treated as whitespace)
    ("is    fun", "is fun"),          # Multiple spaces
])
def test_whitespace_variations(sentence, expected):
    """Tests various whitespace configurations."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("is! fun?", "is!"),              # "is!" (3) is prime, "fun?" (4) is not
    ("wow!!!", "wow!!!"),             # "wow!!!" (6) is not prime -> ""
    ("is? fun", "fun"),               # "is?" (3) is prime, "fun" (3) is prime -> "is? fun"
])
def test_punctuation(sentence, expected):
    """Tests behavior when words contain punctuation (affects length)."""
    # Note: Based on standard .split() behavior, punctuation is part of the word string.
    # "is!" length is 3 (prime). "fun?" length is 4 (not prime).
    if sentence == "is? fun":
        assert words_in_sentence(sentence) == "is? fun"
    elif sentence == "wow!!!":
        assert words_in_sentence(sentence) == ""
    else:
        assert words_in_sentence(sentence) == expected