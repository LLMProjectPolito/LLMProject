import pytest
import math


# Focus: Boundary Values
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_sentence_with_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_sentence_with_single_prime_length_word_at_boundary():
    assert words_in_sentence("a") == "a"

def test_sentence_with_multiple_prime_length_words_at_boundaries():
    assert words_in_sentence("a is test") == "a is"

def test_sentence_with_prime_length_words_including_boundary_cases():
    assert words_in_sentence("This is a test") == "is"

# Focus: Type Scenarios
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test") == "is"

def test_all_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

# Focus: Logic Branches
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)