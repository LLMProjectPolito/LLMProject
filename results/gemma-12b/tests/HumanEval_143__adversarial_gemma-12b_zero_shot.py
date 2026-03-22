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

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("This  is   a    test") == "is"

def test_sentence_with_long_words():
    assert words_in_sentence("This is a verylongword") == ""

def test_sentence_with_short_words():
    assert words_in_sentence("a b c d e") == "a b c d e"

def test_sentence_with_prime_and_non_prime_words_at_edges():
    assert words_in_sentence("a This is not a b") == "a b"

def test_sentence_with_only_one_word():
    assert words_in_sentence("test") == ""

def test_sentence_with_prime_length_word_at_end():
    assert words_in_sentence("This is a test b") == "is"

def test_sentence_with_prime_length_word_at_beginning():
    assert words_in_sentence("a This is a test") == "a"

def test_sentence_with_same_length_words():
    assert words_in_sentence("aa bb cc") == ""

def test_sentence_with_numbers_and_letters():
    assert words_in_sentence("a1 b2 c3") == ""

def test_sentence_with_special_characters():
    assert words_in_sentence("a! b@ c#") == ""