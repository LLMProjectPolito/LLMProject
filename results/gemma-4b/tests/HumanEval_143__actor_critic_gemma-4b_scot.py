
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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `words_in_sentence` takes a sentence as input and returns a new string
# containing only the words from the original sentence whose lengths are prime numbers,
# preserving the original order.  We need to test various scenarios including empty sentences,
# sentences with no prime-length words, sentences with multiple prime-length words,
# and edge cases like single-word sentences. The `is_prime` helper function needs to be tested as well.

# STEP 2: PLAN - List test functions names and scenarios.
# - test_empty_sentence: Test with an empty sentence.
# - test_no_prime_words: Test with a sentence where no words have prime lengths.
# - test_single_prime_word: Test with a sentence containing only one word with a prime length.
# - test_multiple_prime_words: Test with a sentence containing multiple words with prime lengths.
# - test_mixed_prime_and_non_prime_words: Test with a sentence containing a mix of prime and non-prime words.
# - test_prime_length_one: Test with a sentence where a single word has length 1 (not prime).
# - test_prime_length_two: Test with a sentence where a single word has length 2 (not prime).
# - test_prime_length_3: Test with a sentence where a single word has length 3 (prime).
# - test_prime_length_5: Test with a sentence where a single word has length 5 (prime).
# - test_prime_length_7: Test with a sentence where a single word has length 7 (prime).

# STEP 3: CODE - Write the high-quality pytest suite.
###
# test_empty_sentence
def test_empty_sentence():
    assert words_in_sentence("") == ""

# test_no_prime_words
def test_no_prime_words():
    assert words_in_sentence("hello world") == "hello world"

# test_single_prime_word
def test_single_prime_word():
    assert words_in_sentence("test") == "test"

# test_multiple_prime_words
def test_multiple_prime_words():
    assert words_in_sentence("this is a test") == "is"

# test_mixed_prime_and_non_prime_words
def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

# test_prime_length_one
def test_prime_length_one():
    assert words_in_sentence("a") == ""

# test_prime_length_two
def test_prime_length_two():
    assert words_in_sentence("ab") == ""

# test_prime_length_3
def test_prime_length_3():
    assert words_in_sentence("abc") == "abc"

# test_prime_length_5
def test_prime_length_5():
    assert words_in_sentence("hellofive") == "hellofive"

# test_prime_length_7
def test_prime_length_7():
    assert words_in_sentence("abcdefg") == "abcdefg"