
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
    """Verify the examples provided in the problem description."""
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

@pytest.mark.parametrize("sentence, expected", [
    ("a", ""),              # Length 1: Not prime
    ("to", "to"),           # Length 2: Prime
    ("the", "the"),         # Length 3: Prime
    ("test", ""),           # Length 4: Not prime
    ("abcde", "abcde"),     # Length 5: Prime
    ("abcdef", ""),         # Length 6: Not prime
])
def test_prime_boundary_lengths(sentence, expected):
    """Test specific word lengths to validate primality logic (1, 2, 3, 4, 5, 6)."""
    assert words_in_sentence(sentence) == expected

def test_no_prime_words():
    """Test a sentence where no words have prime lengths."""
    # lengths: 1, 4, 6, 8, 9, 10
    sentence = "a test abcdef ghijklmnopqrst uvwxyz abcdefghij"
    assert words_in_sentence(sentence) == ""

def test_all_prime_words():
    """Test a sentence where all words have prime lengths."""
    # lengths: 2, 3, 5, 7
    sentence = "is the apple amazing"
    assert words_in_sentence(sentence) == "is the apple amazing"

def test_single_word_scenarios():
    """Test sentences consisting of only one word."""
    assert words_in_sentence("hi") == "hi"        # length 2 (prime)
    assert words_in_sentence("hey") == "hey"     # length 3 (prime)
    assert words_in_sentence("hell") == ""       # length 4 (not prime)

def test_large_prime_lengths():
    """Test words with larger prime lengths to ensure robust primality testing."""
    # length 11: 'elevenwords'
    # length 13: 'thirteentexts'
    # length 17: 'seventeenletters'
    sentence = "elevenwords thirteentexts seventeenletters"
    assert words_in_sentence(sentence) == "elevenwords thirteentexts seventeenletters"

def test_mixed_sentence_complex():
    """A complex mix of prime and non-prime lengths."""
    # This (4) is (2) a (1) prime (5) test (4) case (4)
    # Expected: "is prime"
    sentence = "This is a prime test case"
    assert words_in_sentence(sentence) == "is prime"

def test_sentence_with_only_spaces():
    """
    While constraints say 'contains only letters', 
    robustness check for whitespace-only or multiple spaces.
    """
    # If the implementation uses .split(), it handles multiple spaces automatically.
    assert words_in_sentence("is   go") == "is go"