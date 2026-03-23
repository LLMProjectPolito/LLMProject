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

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("This is a test") == ""

def test_words_in_sentence_single_prime_length():
    assert words_in_sentence("This is a test") == "is"

# Focus: Type Scenarios
def test_words_in_sentence_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("hello world") == ""

# Focus: Logic Branches
def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_multiple():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_primes():
    assert words_in_sentence("This is sentence") == ""