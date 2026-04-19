
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

# Assuming the function is imported from the source module
# from solution import words_in_sentence

def test_words_in_sentence_examples():
    """ Test the provided examples to ensure basic functionality. """
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_prime_logic():
    """ 
    Test specific word lengths to verify prime number detection.
    Primes: 2, 3, 5, 7, 11...
    Non-Primes: 1, 4, 6, 8, 9, 10...
    """
    # Length 1 is NOT prime, Length 2 is prime, Length 3 is prime, Length 4 is NOT prime
    # "a" (1), "is" (2), "the" (3), "test" (4)
    assert words_in_sentence("a is the test") == "is the"
    
    # Length 5 is prime, Length 9 is NOT prime
    # "apple" (5), "education" (9)
    assert words_in_sentence("apple education") == "apple"

def test_words_in_sentence_no_primes():
    """ Test cases where no words have prime lengths. """
    # Lengths: 4, 1, 4 (None are prime)
    assert words_in_sentence("This a test") == ""
    # Lengths: 1 (Not prime)
    assert words_in_sentence("I") == ""

def test_words_in_sentence_all_primes():
    """ Test cases where all words have prime lengths. """
    # Lengths: 2, 3, 5 (All prime)
    assert words_in_sentence("it was great") == "it was great"

def test_words_in_sentence_single_word():
    """ Test sentences consisting of only one word. """
    assert words_in_sentence("hello") == "hello"  # length 5 is prime
    assert words_in_sentence("word") == ""        # length 4 is not prime

def test_words_in_sentence_boundaries():
    """ Test constraints: 1 <= len(sentence) <= 100. """
    # Minimum length
    assert words_in_sentence("a") == "" 
    
    # Maximum length (approx 100 chars) with mixed prime lengths
    long_sentence = "hi there my friend is a very smart person who loves coding" 
    # Lengths: 2(P), 5(P), 2(P), 6, 2(P), 1, 4, 5(P), 6, 3(P), 5(P), 6
    # Expected: "hi there my is smart who loves"
    expected = "hi there my is smart who loves"
    assert words_in_sentence(long_sentence) == expected

def test_words_in_sentence_whitespace_handling():
    """ 
    Defensive tests for whitespace. 
    Although constraints say 'separated by a space', robust code should handle 
    multiple spaces or leading/trailing spaces.
    """
    assert words_in_sentence("  is  the  ") == "is the"
    assert words_in_sentence("is the    ") == "is the"

@pytest.mark.parametrize("sentence, expected", [
    ("abc de fghij", "de fghij"), # 3(P), 2(P), 5(P) -> all prime
    ("a b c d", ""),              # all length 1 -> none prime
    ("abcdefghij k", ""),         # 10(NP), 1(NP) -> none prime
    ("hi", "hi"),                 # 2(P)
])
def test_words_in_sentence_parametrized(sentence, expected):
    """ Bulk test for various combinations. """
    assert words_in_sentence(sentence) == expected