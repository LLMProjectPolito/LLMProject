import pytest
import math


# Focus: Boundary Values
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_sentence_with_one_word_prime_length():
    assert words_in_sentence("one") == "one"

def test_sentence_with_one_word_non_prime_length():
    assert words_in_sentence("two") == ""

def test_sentence_with_multiple_words_some_prime_some_not():
    assert words_in_sentence("This is a test") == "is"

def test_sentence_with_all_words_prime_length():
    assert words_in_sentence("one two three five") == "one two three five"

def test_sentence_with_all_words_non_prime_length():
    assert words_in_sentence("four six eight ten") == ""

# Focus: Type Scenarios
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("hello world") == ""

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test") == "is"

# Focus: Logic Branches
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_all_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"