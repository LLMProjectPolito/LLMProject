
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

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
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

def test_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_no_prime_lengths():
    # Lengths: 1, 4, 6 (None are prime)
    assert words_in_sentence("a test street") == ""

def test_all_prime_lengths():
    # Lengths: 2, 3, 2 (All are prime)
    assert words_in_sentence("go for it") == "go for it"

def test_single_character_word():
    # Length 1 is not prime
    assert words_in_sentence("a") == ""
    assert words_in_sentence("i am") == "am"  # 'i' is 1, 'am' is 2

def test_small_primes():
    # Length 2 and 3 are prime
    assert words_in_sentence("to the") == "to the"

def test_non_prime_composites():
    # "four"(4), "six"(3), "eight"(5), "nine"(4), "ten"(3)
    # Prime lengths are 3, 5, 3.
    assert words_in_sentence("four six eight nine ten") == "six eight ten"

def test_long_prime_length():
    # "extraordinary" has 13 characters (prime)
    # "professional" has 12 characters (not prime)
    assert words_in_sentence("professional extraordinary") == "extraordinary"

def test_sentence_with_mixed_cases():
    # Lengths: 5 (P), 4 (NP), 11 (P)
    assert words_in_sentence("Hello word imagination") == "Hello imagination"

def test_boundary_length_one():
    # Minimum constraint len(sentence) = 1
    assert words_in_sentence("a") == ""
    assert words_in_sentence("b") == ""

def test_boundary_max_length():
    # Max constraint len(sentence) = 100
    # 10 words of length 9 + 9 spaces = 99 chars
    sentence = "ninechars " * 9 + "ninechars" # All length 9 (not prime)
    assert words_in_sentence(sentence) == ""
    
    # 10 words of length 7 + 9 spaces = 79 chars
    sentence_prime = "sevench " * 9 + "sevench" # All length 7 (prime)
    assert words_in_sentence(sentence_prime) == sentence_prime

@pytest.mark.parametrize("input_str, expected", [
    ("a b c d", ""),               # All length 1
    ("hi there", "hi there"),      # 2 (P), 5 (P)
    ("apple pear peach", "apple peach"), # 5 (P), 4 (NP), 5 (P)
    ("the quick brown fox", "the quick brown fox"), # 3 (P), 5 (P), 5 (P), 3 (P)
])
def test_parametrized_cases(input_str, expected):
    assert words_in_sentence(input_str) == expected