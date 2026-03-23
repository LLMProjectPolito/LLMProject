import pytest
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_multiple():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_length():
    assert words_in_sentence("a bb ccc dddd") == "c"

def test_words_in_sentence_hello():
    assert words_in_sentence("hello world") == "world"

def test_words_in_sentence_numbers():
    assert words_in_sentence("123 abc def") == "abc def"