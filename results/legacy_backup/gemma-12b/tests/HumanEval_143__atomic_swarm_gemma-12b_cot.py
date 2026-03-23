import pytest
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_words_in_sentence():
    sentence = "This is a test"
    expected = "is"
    actual = words_in_sentence(sentence)
    assert actual == expected

    sentence = "lets go for swimming"
    expected = "go for"
    actual = words_in_sentence(sentence)
    assert actual == expected

    sentence = "the quick brown fox jumps over the lazy dog"
    expected = "quick fox over lazy"
    actual = words_in_sentence(sentence)
    assert actual == expected

    sentence = "a b c d e f g"
    expected = "a b c d e f g"
    actual = words_in_sentence(sentence)
    assert actual == expected

    sentence = "one two three four five six seven eight nine ten"
    expected = "two three five seven"
    actual = words_in_sentence(sentence)
    assert actual == expected

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

def test_sentence_with_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_sentence_with_single_prime_length_word():
    assert words_in_sentence("a") == "a"

def test_sentence_with_multiple_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("This  is   a    test") == "is"

def test_sentence_with_long_prime_length_word():
    assert words_in_sentence("This is a verylongword") == "verylongword"

def test_sentence_with_all_prime_length_words():
    assert words_in_sentence("a is go") == "a is go"

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
    assert words_in_sentence("a bb ccc dddd") == ""

def test_sentence_with_only_one_prime_length_word():
    assert words_in_sentence("a bb ccc dddd e") == "a"

def test_sentence_with_multiple_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("This  is   a    test") == "is"

def test_sentence_with_long_prime_length_word():
    assert words_in_sentence("This is a verylongword test") == "is"

def test_sentence_with_all_prime_length_words():
    assert words_in_sentence("a bb c d e") == "a bb c d e"