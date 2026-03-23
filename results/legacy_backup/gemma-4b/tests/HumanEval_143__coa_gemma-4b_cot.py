import pytest
import math


# Focus: Boundary Values
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

@pytest.mark.boundary
def test_empty_sentence():
    assert words_in_sentence("") == ""

@pytest.mark.boundary
def test_single_word_prime():
    assert words_in_sentence("abc") == "abc"

@pytest.mark.boundary
def test_single_word_non_prime():
    assert words_in_sentence("abcd") == ""

@pytest.mark.boundary
def test_multiple_words_some_prime():
    assert words_in_sentence("This is a test") == "is"

@pytest.mark.boundary
def test_multiple_words_all_non_prime():
    assert words_in_sentence("abcdefg") == ""

@pytest.mark.boundary
def test_multiple_words_all_prime():
    assert words_in_sentence("abc def ghi") == "abc def ghi"

# Focus: Type Scenarios
import pytest

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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("hello world") == "hello world"

def test_single_prime_length_word():
    assert words_in_sentence("test") == "test"

def test_multiple_prime_length_words():
    assert words_in_sentence("This is a test") == "is test"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

# Focus: Logic Branches
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("This is a test") == ""

def test_single_prime_length_word():
    assert words_in_sentence("is") == "is"

def test_multiple_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test sentence") == "is a"