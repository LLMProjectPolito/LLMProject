
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

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def words_in_sentence(sentence):
    return sentence

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_is_prime_less_than_or_equal_to_1():
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False

def test_is_prime_2_and_3():
    assert is_prime(2) == True
    assert is_prime(3) == True

def test_is_prime_divisible_by_2_or_3():
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(9) == False

def test_is_prime_larger_numbers():
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(19) == True
    assert is_prime(23) == True
    assert is_prime(29) == True
    assert is_prime(31) == True
    assert is_prime(37) == True

def test_is_prime_not_prime():
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_prime(16) == False
    assert is_prime(21) == False
    assert is_prime(25) == False
    assert is_prime(27) == False