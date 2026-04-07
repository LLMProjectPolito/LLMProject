
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

STEP 1: REASONING -
The function `words_in_sentence` takes a sentence as input and returns a new string containing only the words from the original sentence whose lengths are prime numbers, preserving the original order.  We need to test various scenarios including empty sentences, sentences with no prime-length words, sentences with multiple prime-length words, and sentences with a mix of prime and non-prime length words. The `is_prime` helper function needs to be tested as well.

STEP 2: PLAN -
Test functions:
1. `test_empty_sentence`: Checks the behavior with an empty sentence.
2. `test_no_prime_words`: Checks the behavior when no words have prime lengths.
3. `test_single_prime_word`: Checks the behavior with a single prime-length word.
4. `test_multiple_prime_words`: Checks the behavior with multiple prime-length words.
5. `test_mixed_prime_and_non_prime_words`: Checks the behavior with a mix of prime and non-prime length words.
6. `test_is_prime_small_numbers`: Tests the `is_prime` function with small numbers.
7. `test_is_prime_large_numbers`: Tests the `is_prime` function with larger numbers.
8. `test_is_prime_non_prime_numbers`: Tests the `is_prime` function with non-prime numbers.

STEP 3: CODE -