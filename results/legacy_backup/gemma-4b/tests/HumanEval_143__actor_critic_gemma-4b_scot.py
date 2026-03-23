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
# and edge cases like single-word sentences. The `is_prime` helper function needs to be tested
# separately.

# STEP 2: PLAN - List test functions names and scenarios.
# - test_empty_sentence: Test with an empty sentence.
# - test_no_prime_words: Test with a sentence where no words have prime lengths.
# - test_single_prime_word: Test with a sentence containing only one word with a prime length.
# - test_multiple_prime_words: Test with a sentence containing multiple words with prime lengths.
# - test_mixed_prime_and_non_prime_words: Test with a sentence containing a mix of prime and non-prime words.
# - test_is_prime_negative_number: Test `is_prime` with a negative number.
# - test_is_prime_zero: Test `is_prime` with zero.
# - test_is_prime_one: Test `is_prime` with one.
# - test_is_prime_small_prime: Test `is_prime` with a small prime number.
# - test_is_prime_large_prime: Test `is_prime` with a large prime number.


# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_words():
    assert words_in_sentence("This is a test") == "This is a test"

def test_single_prime_word():
    assert words_in_sentence("is") == "is"

def test_multiple_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test sentence") == "is"

def test_is_prime_negative_number():
    assert is_prime(-5) == False

def test_is_prime_zero():
    assert is_prime(0) == False

def test_is_prime_one():
    assert is_prime(1) == False

def test_is_prime_small_prime():
    assert is_prime(2) == True

def test_is_prime_large_prime():
    assert is_prime(97) == True