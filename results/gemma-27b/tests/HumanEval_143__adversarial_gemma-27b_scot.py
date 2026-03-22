import pytest

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
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

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
    assert words_in_sentence("this is a test") == ""

def test_all_prime_words():
    assert words_in_sentence("is a go") == "is a go"

def test_mixed_words():
    assert words_in_sentence("This is a test") == "is"

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_single_prime_word():
    assert words_in_sentence("go") == "go"

def test_single_non_prime_word():
    assert words_in_sentence("test") == ""

def test_longer_words():
    assert words_in_sentence("programming is fun") == "programming is"

def test_edge_case_primes():
    assert words_in_sentence("go to be") == "go to be"
    assert words_in_sentence("hi there") == "hi"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("two three five seven") == "two three five seven"
    assert words_in_sentence("eleven") == "eleven"