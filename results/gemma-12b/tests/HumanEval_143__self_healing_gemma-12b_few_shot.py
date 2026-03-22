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

def test_words_in_sentence_example1():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime():
    assert words_in_sentence("hello world") == ""

def test_words_in_sentence_all_prime():
    assert words_in_sentence("a is be do") == "a is be do"

def test_words_in_sentence_mixed():
    assert words_in_sentence("a bb ccc d e fff") == "a e"

def test_words_in_sentence_leading_trailing_spaces():
    assert words_in_sentence("  a b c  ") == "a b c"

def test_words_in_sentence_multiple_spaces():
    assert words_in_sentence("a  b   c") == "a b c"

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("this is a very long sentence with some prime length words") == "is a very long sentence with some"