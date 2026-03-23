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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("a bb ccc dddd") == ""

def test_single_prime_length_word():
    assert words_in_sentence("a") == "a"

def test_multiple_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  a b c  ") == "a b c"

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("a  b   c") == "a b c"

# Focus: Type Scenarios
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test") == "is"

def test_all_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_sentence_with_single_prime_word():
    assert words_in_sentence("a b c d") == "a"

def test_sentence_with_multiple_prime_words():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox the dog"

# Focus: Logic Branches
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_mixed_prime_and_non_prime():
    assert words_in_sentence("This is a test") == "is"

def test_all_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_sentence_with_one_word():
    assert words_in_sentence("prime") == "prime"

def test_sentence_with_multiple_spaces():
    assert words_in_sentence("  this   is  a  test  ") == "is"