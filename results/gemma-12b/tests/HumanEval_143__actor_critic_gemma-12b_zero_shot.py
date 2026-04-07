
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
from your_module import words_in_sentence  # Replace your_module

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""  # Empty sentence should return an empty string.

def test_single_word_prime_length():
    assert words_in_sentence("go") == "go"  # "go" has length 2, which is prime.

def test_single_word_non_prime_length():
    assert words_in_sentence("this") == ""  # "this" has length 4, which is not prime.

def test_multiple_words_with_prime_lengths():
    assert words_in_sentence("This is a test") == "is"  # "This" (4), "is" (2), "a" (1), "test" (4). Only "is" has prime length.

def test_multiple_words_with_mixed_lengths():
    assert words_in_sentence("lets go for swimming") == "go for"  # "lets" (4), "go" (2), "for" (3), "swimming" (8). "go" and "for" have prime lengths.

def test_all_words_non_prime_lengths():
    assert words_in_sentence("this is a very long sentence") == ""  # All words have non-prime lengths.

def test_all_words_prime_lengths():
    assert words_in_sentence("go for two five") == "go for"  # All words have prime lengths (2, 3, 3, 4). "two" has length 3, which is prime.

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  go for  ") == "go for"  # Leading/trailing spaces should be trimmed.

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence("go   for  two") == "go for two"  # Multiple spaces should be treated as single spaces.

def test_sentence_with_one_letter_prime_word():
    assert words_in_sentence("a go") == "go"  # "a" (1) is not prime, "go" (2) is prime.

def test_sentence_with_one_letter_non_prime_word():
    assert words_in_sentence("i go") == "go"  # "i" (1) is not prime, "go" (2) is prime.

def test_sentence_with_long_prime_length_word():
    assert words_in_sentence("This is a verylongword") == ""  # "verylongword" has length 14, which is not prime.

def test_sentence_with_long_non_prime_length_word():
    assert words_in_sentence("This is a verylongwordnotprime") == ""  # "verylongwordnotprime" has length 22, which is not prime.

def test_sentence_with_numbers_in_words():
    assert words_in_sentence("This is 2 test") == ""  # Words with numbers are considered invalid.

def test_sentence_with_special_characters():
    assert words_in_sentence("This is a test!") == ""  # Words with special characters are considered invalid.

def test_sentence_with_prime_and_non_prime_words_at_start_and_end():
    assert words_in_sentence("go this is a test") == "go"  # "go" (2) is prime, others are not.

def test_sentence_with_prime_and_non_prime_words_at_start_and_end2():
    assert words_in_sentence("this is a test go") == "go"  # "go" (2) is prime, others are not.

def test_whitespace_only_sentence():
    assert words_in_sentence("   ") == ""  # Sentence with only whitespace.

def test_case_sensitivity():
    assert words_in_sentence("Go For") == "" # Tests case sensitivity. "Go" (2) is prime, "For" (3) is prime, but the function is case sensitive.

def test_single_word_prime_palindrome():
    assert words_in_sentence("madam") == "madam" # "madam" has length 5, which is prime and is a palindrome.

def test_very_long_word_prime():
    long_word = "a" * 1001  # Length 1001, which is prime
    assert words_in_sentence(f"This is a {long_word}") == long_word

def test_very_long_word_non_prime():
    long_word = "a" * 1000  # Length 1000, which is not prime
    assert words_in_sentence(f"This is a {long_word}") == ""

def test_unicode_characters():
    assert words_in_sentence("你好世界") == "" # "你好世界" has length 4, which is not prime.