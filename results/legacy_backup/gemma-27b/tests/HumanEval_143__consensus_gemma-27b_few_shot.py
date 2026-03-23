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

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_primes():
    assert words_in_sentence("one two four five") == ""

def test_words_in_sentence_all_primes():
    assert words_in_sentence("two three five seven") == "two three five seven"

def test_words_in_sentence_mixed():
    assert words_in_sentence("a bb ccc dddd") == "a bb"

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the quick fox over the dog"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("two") == "two"

def test_words_in_sentence_single_word_not_prime():
    assert words_in_sentence("one") == ""