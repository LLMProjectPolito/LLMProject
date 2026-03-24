
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

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `words_in_sentence` filters words from a sentence, keeping only those with prime-length.
# The constraints are: sentence length <= 100, sentence contains only letters.
# We need to test various scenarios: empty sentence, sentence with no prime-length words,
# sentence with all prime-length words, sentence with a mix of prime and non-prime length words,
# and edge cases like single-letter words and sentences with leading/trailing spaces.
# The two provided suites have different implementations of `is_prime`. We will use the first one.

# STEP 2: PLAN - List test functions names and scenarios.
# Test functions:
# - test_empty_sentence: Tests with an empty sentence.
# - test_no_prime_length_words: Tests a sentence with no words of prime length.
# - test_all_prime_length_words: Tests a sentence where all words have prime lengths.
# - test_mixed_length_words: Tests a sentence with a mix of prime and non-prime length words.
# - test_single_letter_words: Tests a sentence with single-letter words.
# - test_leading_trailing_spaces: Tests a sentence with leading and trailing spaces.
# - test_sentence_length_constraint: Tests a sentence close to the length constraint.
# - test_long_word: Tests a sentence with a long word.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is a test") == ""

def test_all_prime_length_words():
    assert words_in_sentence("is it a") == "is it a"

def test_mixed_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_single_letter_words():
    assert words_in_sentence("a b c d e") == "a b c d e"

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_sentence_length_constraint():
    long_sentence = "a " * 99 + "b"
    assert len(words_in_sentence(long_sentence)) <= 100

def test_long_word():
    assert words_in_sentence("abcdefghijk") == "abcdefghijk"