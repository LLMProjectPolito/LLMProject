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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_prime_word():
    assert words_in_sentence("is") == "is"

def test_single_non_prime_word():
    assert words_in_sentence("this") == ""

def test_multiple_words_with_primes():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_words_with_no_primes():
    assert words_in_sentence("the quick brown fox") == ""

def test_mixed_prime_and_non_prime():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "world"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("hello   world") == "world"

def test_long_sentence():
    sentence = "a very long sentence with some prime words like two five seven eleven"
    assert words_in_sentence(sentence) == "two five seven eleven"

def test_all_prime_words():
    sentence = "two three five seven eleven"
    assert words_in_sentence(sentence) == "two three five seven eleven"

def test_sentence_with_one_letter_words():
    assert words_in_sentence("a i") == "a i"

def test_sentence_with_numbers_as_words():
    assert words_in_sentence("one two three") == "two three"

def test_sentence_with_special_characters():
    with pytest.raises(TypeError):
        words_in_sentence("hello! world?")