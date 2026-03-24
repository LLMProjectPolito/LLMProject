
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    """Test with an empty sentence."""
    assert words_in_sentence("") == ""

def test_no_prime_words():
    """Test when no words have prime length."""
    assert words_in_sentence("This is a test") == ""

def test_single_prime_word():
    """Test with a single word of prime length."""
    assert words_in_sentence("is") == "is"

def test_multiple_prime_words():
    """Test with multiple words of prime length."""
    assert words_in_sentence("lets go for swimming") == "go for"

def test_mixed_prime_and_non_prime_words():
    """Test with a mix of prime and non-prime length words."""
    assert words_in_sentence("hello world test") == "world test"

def test_is_prime_small_numbers():
    """Test the is_prime function with small numbers."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False

def test_is_prime_large_numbers():
    """Test the is_prime function with larger numbers."""
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(17) == True

def test_is_prime_one():
    """Test the is_prime function with 1."""
    assert is_prime(1) == False

def test_is_prime_two():
    """Test the is_prime function with 2."""
    assert is_prime(2) == True