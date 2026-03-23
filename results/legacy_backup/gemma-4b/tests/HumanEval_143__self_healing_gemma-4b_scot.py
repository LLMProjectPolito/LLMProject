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

# STEP 1: REASONING
# The function `words_in_sentence` takes a sentence as input and returns a new string containing only the words from the original sentence whose lengths are prime numbers, preserving the original order.
# We need to test various scenarios including empty sentences, sentences with no prime-length words, sentences with multiple prime-length words, and sentences with different word lengths.
# We also need to test the helper function `is_prime` to ensure it correctly identifies prime numbers.

# STEP 2: PLAN
# Test cases:
# 1. Empty sentence: ""
# 2. Sentence with no prime-length words: "This is a test"
# 3. Sentence with one prime-length word: "lets go for swimming"
# 4. Sentence with multiple prime-length words: "This is a test sentence"
# 5. Sentence with a prime-length word at the beginning: "2 is prime"
# 6. Sentence with a prime-length word at the end: "test is 3"
# 7. Sentence with a single word that is prime: "abc"
# 8. Sentence with a single word that is not prime: "abcd"
# 9. Sentence with multiple words, some prime, some not: "hello world test"
# 10. Edge case: sentence with only one word and it's length is prime.

# Test functions:
# - test_empty_sentence
# - test_no_prime_words
# - test_one_prime_word
# - test_multiple_prime_words
# - test_prime_word_at_beginning
# - test_prime_word_at_end
# - test_single_prime_word
# - test_single_non_prime_word
# - test_multiple_words_mixed
# - test_single_word_prime

# STEP 3: CODE
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_words():
    assert words_in_sentence("This is a test") == "This is a test"

def test_one_prime_word():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_multiple_prime_words():
    assert words_in_sentence("This is a test sentence") == "is a test"

def test_prime_word_at_beginning():
    assert words_in_sentence("2 is prime") == "2 is"

def test_prime_word_at_end():
    assert words_in_sentence("test is 3") == "test is"

def test_single_prime_word():
    assert words_in_sentence("abc") == "abc"

def test_single_non_prime_word():
    assert words_in_sentence("abcd") == "abcd"

def test_multiple_words_mixed():
    assert words_in_sentence("hello world test") == "hello test"

def test_single_word_prime():
    assert words_in_sentence("abcde") == "abcde"