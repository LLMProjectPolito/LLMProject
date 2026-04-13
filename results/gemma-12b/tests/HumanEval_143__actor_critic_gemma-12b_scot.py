
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
    for word in words:
        if not word.isalpha():
            raise ValueError("Sentence contains non-letter characters")
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("This is a long sentence") == ""

def test_all_prime_length_words():
    assert words_in_sentence("This is a test") == "is a"

def test_mixed_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_single_word_prime_length():
    assert words_in_sentence("test") == "test"

def test_single_word_non_prime_length():
    assert words_in_sentence("testing") == ""

def test_space_handling():
    assert words_in_sentence("  This is a test  ") == "is a"
    assert words_in_sentence("This  is   a    test") == "is a"

def test_long_sentence():
    assert words_in_sentence("This is a very long sentence with many words of varying lengths") == "is a very long sentence"

def test_sentence_with_only_spaces():
    assert words_in_sentence("   ") == ""

def test_is_prime_small_primes():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

def test_is_prime_larger_primes():
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True

def test_is_prime_non_primes():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_long_word():
    long_word = "a" * 17  # Prime length
    assert words_in_sentence(long_word) == long_word

def test_very_long_sentence():
    long_sentence = "This is a " + "word " * 20 + "with some prime and non-prime length words"
    assert words_in_sentence(long_sentence) == "is a word word word word word word word word word word word"

def test_non_letter_characters():
    with pytest.raises(ValueError):
        words_in_sentence("This is a 1 test")