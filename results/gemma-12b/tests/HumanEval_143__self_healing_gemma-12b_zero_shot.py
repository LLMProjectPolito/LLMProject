import pytest
from your_module import words_in_sentence  # Replace your_module

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_single_prime_length_word():
    assert words_in_sentence("a") == "a"

def test_multiple_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_all_words_prime_length():
    assert words_in_sentence("I am here") == "I am"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("This  is   a    test") == "is"

def test_long_sentence():
    sentence = "This is a very long sentence with some words of prime lengths and some not"
    expected = "is a with"
    assert words_in_sentence(sentence) == expected

def test_sentence_with_only_one_word():
    assert words_in_sentence("prime") == "prime"

def test_sentence_with_same_length_words():
    assert words_in_sentence("go do re mi") == "go do"

def test_sentence_with_prime_and_non_prime_same_length():
    assert words_in_sentence("go do re") == "go do"

def test_sentence_with_numbers_as_words():
    assert words_in_sentence("1 2 3 4 5") == "1 2 3 5"