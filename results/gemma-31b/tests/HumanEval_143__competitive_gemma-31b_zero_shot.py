
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
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a i o", ""),
    ("apple banana cherry", "apple"), # 5, 6, 6
    ("is the cat", "is the cat"), # 2, 3, 3
    ("four eight", "eight"), # 4, 5
    ("hello world", "hello world"), # 5, 5
    ("a", ""), # 1 is not prime
    ("hi", "hi"), # 2 is prime
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps over the lazy dog"), 
    # lengths: 3, 5, 5, 3, 5, 4, 3, 4, 3
    # primes: 3, 5, 5, 3, 5, (4 no), 3, (4 no), 3
    # expected: "the quick brown fox jumps over the lazy dog" -> wait, "over" is 4, "lazy" is 4.
    # Correct: "the quick brown fox jumps the dog"
])
def test_words_in_sentence_parametrized(sentence, expected):
    # Recalculating the long sentence example for accuracy:
    # "the"(3), "quick"(5), "brown"(5), "fox"(3), "jumps"(5), "over"(4), "the"(3), "lazy"(4), "dog"(3)
    # Primes: 3, 5, 5, 3, 5, 3, 3
    # Result: "the quick brown fox jumps the dog"
    if sentence == "the quick brown fox jumps over the lazy dog":
        expected = "the quick brown fox jumps the dog"
    
    assert words_in_sentence(sentence) == expected

def test_no_prime_lengths():
    assert words_in_sentence("four eight") == "eight" # 4, 5 (5 is prime)
    assert words_in_sentence("four") == "" # 4 is not prime

def test_all_prime_lengths():
    assert words_in_sentence("is the cat") == "is the cat"

def test_single_character_words():
    # 1 is not a prime number
    assert words_in_sentence("a b c d") == ""

def test_long_prime_word():
    # 13 is prime
    assert words_in_sentence("extraordinary") == "extraordinary"

def test_non_prime_long_word():
    # 14 is not prime
    assert words_in_sentence("institutionalize") == ""

def test_mixed_case():
    # Lengths are independent of case
    assert words_in_sentence("Hello is a Test") == "Hello is" # 5, 2, 1, 4

def test_boundary_length():
    # Constraint: 1 <= len(sentence) <= 100
    sentence = "a" * 100
    # length 100 is not prime
    assert words_in_sentence(sentence) == ""
    
    sentence_prime = "a" * 97 # 97 is prime
    assert words_in_sentence(sentence_prime) == sentence_prime