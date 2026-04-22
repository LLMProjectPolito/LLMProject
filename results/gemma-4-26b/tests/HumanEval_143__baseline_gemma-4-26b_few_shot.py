
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
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_no_prime_length_words():
    # Lengths: 1, 4, 6, 8, 9, 10
    assert words_in_sentence("a test enough strength") == ""
    assert words_in_sentence("a") == ""

def test_all_prime_length_words():
    # Lengths: 2, 3, 5, 7
    assert words_in_sentence("is the apple seventh") == "is the apple seventh"
    assert words_in_sentence("to be or not") == "to be or not"

def test_mixed_prime_and_non_prime():
    # Lengths: 1 (NP), 2 (P), 3 (P), 4 (NP), 5 (P)
    assert words_in_sentence("a it the book apple") == "it the apple"

@pytest.mark.parametrize("sentence, expected", [
    ("hi", "hi"),                   # 2: Prime
    ("hey", "hey"),                 # 3: Prime
    ("hell", ""),                   # 4: Not Prime
    ("hello", "hello"),             # 5: Prime
    ("hellos", ""),                 # 6: Not Prime
    ("abcdefg", "abcdefg"),         # 7: Prime
    ("abcde fghij", "abcde fghij"), # 5, 5: Prime
    ("a b c d e", ""),              # All 1: Not Prime
])
def test_word_lengths(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_single_word_sentence():
    assert words_in_sentence("prime") == "prime"  # 5 is prime
    assert words_in_sentence("primes") == ""     # 6 is not prime

def test_sentence_with_many_spaces():
    # Testing robustness with spacing (though constraints imply single spaces)
    # Note: The problem says "words separated by a space", usually implying single spaces.
    # If the implementation uses .split(), it handles multiple spaces.
    assert words_in_sentence("is  the") == "is the"