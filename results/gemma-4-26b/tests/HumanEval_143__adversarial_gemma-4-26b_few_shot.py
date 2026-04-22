
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

# Note: The function words_in_sentence is assumed to be imported from the source module

@pytest.mark.parametrize("sentence, expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
])
def test_provided_examples(sentence, expected):
    """Verify the function works against the provided examples."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("sentence, expected", [
    ("a", ""),                # Length 1: 1 is NOT prime
    ("at", "at"),             # Length 2: 2 is prime
    ("the", "the"),           # Length 3: 3 is prime
    ("test", ""),             # Length 4: 4 is not prime
    ("apple", "apple"),       # Length 5: 5 is prime
    ("abcdefg", "abcdefg"),   # Length 7: 7 is prime
    ("abcdefgh", ""),         # Length 8: 8 is not prime
    ("abcdefghij", ""),       # Length 10: 10 is not prime
    ("abcdefghijk", "abcdefghijk"), # Length 11: 11 is prime
])
def test_prime_number_logic(sentence, expected):
    """
    Targeting the mathematical core. 
    Crucial check: Does the dev correctly identify that 1 is NOT prime 
    and 2 IS prime?
    """
    assert words_in_sentence(sentence) == expected

def test_mixed_sentence_logic():
    """Test a complex sentence with a mix of prime and non-prime lengths."""
    # lengths: 1(N), 2(P), 1(N), 3(P), 4(N), 5(P)
    sentence = "a is a cat test apple"
    expected = "is cat apple"
    assert words_in_sentence(sentence) == expected

def test_no_prime_words():
    """Test a sentence where no words have prime lengths."""
    sentence = "a abcd abcdefgh"
    assert words_in_sentence(sentence) == ""

def test_all_prime_words():
    """Test a sentence where all words have prime lengths."""
    sentence = "at the apple"
    assert words_in_sentence(sentence) == "at the apple"

def test_constraint_boundaries():
    """
    Test the upper boundary of the constraints (len <= 100).
    97 is the largest prime under 100.
    """
    # Case: Single word of length 97 (Prime)
    prime_word = "a" * 97
    assert words_in_sentence(prime_word) == prime_word

    # Case: Single word of length 100 (Not Prime)
    non_prime_word = "a" * 100
    assert words_in_sentence(non_prime_word) == ""

def test_whitespace_handling():
    """
    Check how the function handles multiple spaces. 
    While constraints say 'separated by a space', robust code 
    should handle variations or at least not crash.
    """
    # If the implementation uses .split(' '), it might return empty strings 
    # which have length 0 (not prime). If it uses .split(), it's cleaner.
    sentence = "is  go" # Double space
    # 'is' (2) is prime, 'go' (2) is prime.
    assert words_in_sentence(sentence) == "is go"

def test_empty_string():
    """Test behavior with an empty string (though constraints say len >= 1)."""
    assert words_in_sentence("") == ""