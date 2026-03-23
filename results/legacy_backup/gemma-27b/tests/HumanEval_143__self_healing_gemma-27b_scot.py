import pytest

def is_prime(n):
    """Helper function to check if a number is prime."""
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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_words():
    assert words_in_sentence("this is a test") == ""

def test_some_prime_words():
    assert words_in_sentence("This is a test") == "is"

def test_all_prime_words():
    assert words_in_sentence("go for") == "go for"

def test_mixed_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_single_prime_word():
    assert words_in_sentence("go") == "go"

def test_sentence_with_long_word():
    assert words_in_sentence("programming is fun") == "programming"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("  hello   world  ") == "hello world"

def test_prime_length_2():
    assert words_in_sentence("to be") == "to be"

def test_prime_length_3():
    assert words_in_sentence("the cat") == "the cat"

def test_prime_length_5():
    assert words_in_sentence("apple hello") == "apple hello"

def test_prime_length_7():
    assert words_in_sentence("amazing world") == "amazing world"