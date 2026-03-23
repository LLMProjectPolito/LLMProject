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
# We need to test various scenarios including empty sentences, sentences with no prime-length words, sentences with multiple prime-length words, and sentences with edge cases like single-word sentences.
# The `is_prime` helper function needs to be tested independently to ensure it correctly identifies prime numbers.

# STEP 2: PLAN
# Test cases:
# 1. Empty sentence: ""
# 2. Sentence with no prime-length words: "This is a test"
# 3. Sentence with one prime-length word: "is"
# 4. Sentence with multiple prime-length words: "lets go for swimming"
# 5. Sentence with a single word that is prime: "abc"
# 6. Sentence with a single word that is not prime: "abcd"
# 7. Sentence with a prime-length word at the beginning: "7 is a test"
# 8. Sentence with a prime-length word at the end: "This is 7 test"
# 9. Sentence with multiple prime-length words at the beginning: "2 is 3 go"
# 10. Sentence with multiple prime-length words at the end: "This is go 4"

# Test functions:
# - test_empty_sentence
# - test_no_prime_words
# - test_single_prime_word
# - test_multiple_prime_words
# - test_single_prime_word_sentence
# - test_single_non_prime_word_sentence
# - test_prime_word_at_beginning
# - test_prime_word_at_end
# - test_multiple_prime_words_beginning
# - test_multiple_prime_words_end


# STEP 3: CODE
###
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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_words():
    assert words_in_sentence("This is a test") == "This is a test"

def test_single_prime_word():
    assert words_in_sentence("is") == "is"

def test_multiple_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_single_prime_word_sentence():
    assert words_in_sentence("abc") == "abc"

def test_single_non_prime_word_sentence():
    assert words_in_sentence("abcd") == "abcd"

def test_prime_word_at_beginning():
    assert words_in_sentence("7 is a test") == "7 is"

def test_prime_word_at_end():
    assert words_in_sentence("This is 7 test") == "This is 7"

def test_multiple_prime_words_beginning():
    assert words_in_sentence("2 is 3 go") == "2 is 3"

def test_multiple_prime_words_end():
    assert words_in_sentence("This is go 4") == "This is go"