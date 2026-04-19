
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
    # Basic examples
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    # Single word cases
    ("hello", "hello"),           # length 5 (prime)
    ("test", ""),                 # length 4 (not prime)
    ("a", ""),                    # length 1 (not prime)
    ("is", "is"),                 # length 2 (prime)
    ("cat", "cat"),               # length 3 (prime)
    ("banana", ""),               # length 6 (not prime)
    # Mixed lengths
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps the dog"),
    ("I am a student", "am student"), # I(1), am(2), a(1), student(7)
    ("The length of this sentence is quite long indeed", "The of is quite"),
    ("to the test hello", "to the hello"), # 2, 3, 4, 5
    # All prime lengths
    ("is the apple amazing", "is the apple amazing"), # 2, 3, 5, 7
    ("go for it", "go for it"), # 2, 3, 2
    # No prime lengths
    ("a test school basketball", ""), # 1, 4, 6, 10
    ("a b c d", ""), # 1, 1, 1, 1
    ("a test banana swimming alphabet dictionary", ""), # 1, 4, 6, 8, 8, 10
    # Case sensitivity check
    ("Is THIS a Test", "Is"), # 2, 4, 1, 4
])
def test_words_in_sentence_parametrized(sentence, expected):
    """Tests words_in_sentence with various inputs to ensure it correctly identifies
    words with prime lengths and maintains their original order.
    """
    assert words_in_sentence(sentence) == expected

def test_various_prime_lengths():
    """Tests words of different prime lengths: 2, 3, 5, 7, 13."""
    sentence = "to the apple amazing mathematician"
    # 2, 3, 5, 7, 13 are all prime.
    assert words_in_sentence(sentence) == "to the apple amazing mathematician"

def test_max_length_constraint():
    """Tests the upper boundary of the length constraint (100 characters)."""
    # "hi" is length 2 (prime). 33 repetitions of "hi " is 99 chars.
    sentence = ("hi " * 33).strip() # 98 chars
    assert words_in_sentence(sentence) == sentence

def test_single_character_words():
    """Tests that words of length 1 are not considered prime."""
    assert words_in_sentence("i a o u") == ""
    assert words_in_sentence("i do a lot") == "do lot" # i(1), do(2), a(1), lot(3)