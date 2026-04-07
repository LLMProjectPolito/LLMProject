
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

import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
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

def test_basic():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_no_primes():
    assert words_in_sentence("hello world") == ""

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_prime_word():
    assert words_in_sentence("two") == "two"

def test_single_non_prime_word():
    assert words_in_sentence("one") == ""

def test_mixed_lengths():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox the dog"

def test_long_sentence():
    assert words_in_sentence("a very long sentence with some words of prime length") == "very long some"

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_multiple_spaces():
    assert words_in_sentence("This  is   a test") == "is a"

def test_one_word_not_prime():
    assert words_in_sentence("hello") == ""

def test_constraint_violation():
    with pytest.raises(ValueError):
        words_in_sentence("This is a test1") # Enforces the constraint
    #Alternatively, if the function is meant to ignore non-letter characters:
    #assert words_in_sentence("This is a test1") == "is a" # and document this behavior in the docstring