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

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_words_in_sentence_basic1():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_basic2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_primes():
    assert words_in_sentence("one two four five") == ""

def test_words_in_sentence_all_primes():
    assert words_in_sentence("two three five seven") == "two three five seven"

def test_words_in_sentence_mixed():
    assert words_in_sentence("one two three four five six seven eight nine ten") == "two three five seven"

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("This is a very long sentence with some words of prime length") == "This is a very"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("two") == "two"

def test_words_in_sentence_single_word_not_prime():
    assert words_in_sentence("one") == ""