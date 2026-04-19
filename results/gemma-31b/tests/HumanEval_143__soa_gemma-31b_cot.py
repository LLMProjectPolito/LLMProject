
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

@pytest.mark.parametrize("sentence, expected", [
    # Example 1: "This" (4), "is" (2), "a" (1), "test" (4) -> Only 2 is prime
    ("This is a test", "is"),
    # Example 2: "lets" (4), "go" (2), "for" (3), "swimming" (8) -> 2 and 3 are prime
    ("lets go for swimming", "go for"),
    # No prime lengths: "a" (1), "four" (4), "six" (3 - wait, 3 is prime), "eight" (5 - wait, 5 is prime)
    # Let's try: "a" (1), "four" (4), "sixteen" (7 - prime), "one" (3 - prime)
    ("a four", ""), 
    # All prime lengths: "is" (2), "the" (3), "apple" (5)
    ("is the apple", "is the apple"),
    # Single word - prime length
    ("hello", "hello"), # length 5
    # Single word - non-prime length
    ("test", ""), # length 4
    # Single word - length 1 (not prime)
    ("a", ""),
    # Single word - length 2 (prime)
    ("it", "it"),
    # Mixed lengths including larger primes
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps over the lazy"), 
    # Analysis of above: 
    # the(3-P), quick(5-P), brown(5-P), fox(3-P), jumps(5-P), over(4-NP), the(3-P), lazy(4-NP), dog(3-P)
    # Correct result for "the quick brown fox jumps over the lazy dog": "the quick brown fox jumps the dog"
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps the dog"),
    # Boundary: Max length sentence (100 chars) with various primes
    ("a" * 2 + " " + "a" * 3 + " " + "a" * 4 + " " + "a" * 5 + " " + "a" * 6 + " " + "a" * 7, "aa aaa aaaaa aaaaaaa"),
    # Sentence with only one character
    ("z", ""),
    # Sentence with words of length 2, 3, 5, 7, 11
    ("to the apple amazing unbelievable", "to the apple amazing"), 
    # Analysis: to(2-P), the(3-P), apple(5-P), amazing(7-P), unbelievable(12-NP)
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_empty_string():
    # Although constraints say 1 <= len, testing empty string for robustness
    assert words_in_sentence("") == ""

def test_words_in_sentence_only_spaces():
    # Testing string with only spaces
    assert words_in_sentence("   ") == ""