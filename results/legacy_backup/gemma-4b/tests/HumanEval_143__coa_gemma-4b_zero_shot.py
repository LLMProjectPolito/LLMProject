import pytest
import math


# Focus: Boundary Values
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_words():
    assert words_in_sentence("hello world") == ""

def test_words_in_sentence_single_prime_word():
    assert words_in_sentence("test") == "test"

def test_words_in_sentence_multiple_prime_words():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_prime_words_at_boundaries():
    assert words_in_sentence("a b c d") == "a b"

# Focus: Type Scenarios
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

def test_no_prime_words():
    assert words_in_sentence("hello world") == ""

def test_single_prime_word():
    assert words_in_sentence("prime") == "prime"

def test_multiple_prime_words():
    assert words_in_sentence("this is a test") == "is"

def test_prime_words_with_spaces():
    assert words_in_sentence("lets go for swimming") == "go for"

# Focus: Logic Branches
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_words_in_sentence_empty_sentence():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_words():
    assert words_in_sentence("hello world") == ""

def test_words_in_sentence_single_prime_word():
    assert words_in_sentence("test") == "test"

def test_words_in_sentence_multiple_prime_words():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_prime_words_with_spaces():
    assert words_in_sentence("lets go for swimming") == "go for"