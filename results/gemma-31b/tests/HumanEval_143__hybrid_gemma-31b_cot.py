
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

@pytest.mark.parametrize("sentence, expected", [
    # --- Example Cases ---
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    
    # --- Length 1 (Not Prime) ---
    ("a", ""),
    ("a b c d", ""),
    ("a apple", "apple"),
    ("I am a boy", "am boy"), # I(1), am(2), a(1), boy(3)
    ("I am a student", "am student"), # I(1), am(2), a(1), student(7)
    
    # --- All Words Prime Length ---
    ("Hi you are", "Hi you are"), # 2, 3, 3
    ("The cat sat", "The cat sat"), # 3, 3, 3
    ("is the cat", "is the cat"), # 2, 3, 3
    ("to the apple science mathematics", "to the apple science mathematics"), # 2, 3, 5, 7, 11
    
    # --- No Words Prime Length ---
    ("a test case", ""), # 1, 4, 4
    ("abcd efgh", ""), # 4, 4
    ("a test", ""), # 1, 4
    
    # --- Single Word Tests ---
    ("Hello", "Hello"), # 5 (prime)
    ("Test", ""), # 4 (not prime)
    ("at", "at"), # 2 (prime)
    ("four", ""), # 4 (not prime)
    ("hi", "hi"), # 2 (prime)
    
    # --- Mixed Lengths & Larger Primes ---
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"), 
    # lengths: 3, 5, 5, 3, 5, 4, 3, 4, 3 -> Primes: 3, 5, 5, 3, 5, 3, 3
    ("apple banana cherry", "apple"), # 5(P), 6(NP), 6(NP)
    ("seventh eleven thirteen", "seventh"), # 7(P), 6(NP), 8(NP)
    ("Beautifully wonderful", "Beautifully"), # 11(P), 9(NP)
    
    # --- Constraints & Edge Cases ---
    ("", ""), # Empty string
    ("  ", ""), # Whitespace only
    ("is a", "is"), # Smallest prime vs non-prime
    ("a " * 49 + "hi", "hi"), # Max length boundary, mostly non-primes
    ("abc " * 19 + "abc", "abc " * 19 + "abc"), # All prime length (3)
    ("this is a very long sentence to test the prime length logic and ensure it works as expected always", 
     "is to the prime logic and it works as"), 
    # this(4)X, is(2)O, a(1)X, very(4)X, long(4)X, sentence(8)X, to(2)O, test(4)X, the(3)O, 
    # prime(5)O, length(6)X, logic(5)O, and(3)O, ensure(6)X, it(2)O, works(5)O, as(2)O, expected(8)X, always(6)X
])
def test_words_in_sentence(sentence, expected):
    """
    Comprehensive test suite for words_in_sentence function.
    Covers:
    - Prime boundaries (2, 3, 5, 7, 11)
    - Non-prime odd numbers (1, 9)
    - Mixed sentence structures
    - Empty and whitespace-only strings
    - Maximum length constraints (~100 chars)
    """
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_case_insensitivity():
    """
    Ensure that word length is calculated regardless of case.
    """
    # HELLO(5), world(5) - both prime
    assert words_in_sentence("HELLO world") == "HELLO world"

def test_words_in_sentence_whitespace_handling():
    """
    Ensure the function handles single space separation as per constraints.
    """
    assert words_in_sentence("is a") == "is"