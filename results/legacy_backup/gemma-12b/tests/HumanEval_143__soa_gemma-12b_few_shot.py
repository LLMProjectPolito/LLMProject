import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_words_in_sentence_example1():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("hello world") == ""

def test_words_in_sentence_all_prime_length():
    assert words_in_sentence("the quick brown fox") == "the quick fox"

def test_words_in_sentence_mixed_lengths():
    assert words_in_sentence("a bb ccc dddd eeeee") == "a bb ccc"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("prime") == "prime"

def test_words_in_sentence_single_word_not_prime():
    assert words_in_sentence("hello") == ""

def test_words_in_sentence_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "hello world"

def test_words_in_sentence_multiple_spaces():
    assert words_in_sentence("hello   world") == "hello world"