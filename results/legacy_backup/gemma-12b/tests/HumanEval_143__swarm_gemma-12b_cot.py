import pytest

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

def test_sentence_with_only_one_word():
    assert words_in_sentence("hello") == ""

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "world"

def test_sentence_with_multiple_prime_length_words():
    assert words_in_sentence("a bb ccc dddd eeeee ffffff") == "a bb ccc"