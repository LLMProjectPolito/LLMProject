
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

# Assuming the function is defined as:
# def words_in_sentence(sentence: str) -> str:
#     ...

@pytest.mark.parametrize("input_str, expected", [
    # Boundary lengths: 1 is not prime, 2 & 3 are prime, 4 is not
    ("a", ""),               # len 1
    ("to", "to"),           # len 2
    ("the", "the"),         # len 3
    ("test", ""),           # len 4
    ("apple", "apple"),     # len 5
    ("banana", ""),         # len 6
    ("numbers", "numbers"), # len 7
    ("eighty", ""),         # len 6
    ("extraordinary", "extraordinary"), # len 13
    ("", ""),               # empty string
])
def test_words_in_sentence_individual_lengths(input_str, expected):
    """Verify primality logic for individual word lengths across boundaries."""
    assert words_in_sentence(input_str) == expected

def test_words_in_sentence_examples():
    """Test the specific examples provided in the problem description."""
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_primes():
    """Test sentences where no words have prime lengths."""
    # 'That' (4), 'test' (4), 'idea' (4), 'a' (1)
    assert words_in_sentence("That test idea a") == ""

def test_words_in_sentence_all_primes():
    """Test sentences where every word has a prime length."""
    # 'is' (2), 'the' (3), 'apple' (5)
    assert words_in_sentence("is the apple") == "is the apple"
    # 'prime' (5), 'numbers' (7)
    assert words_in_sentence("prime numbers") == "prime numbers"

def test_words_in_sentence_mixed_lengths():
    """Test complex sentences with a mix of prime and non-prime lengths."""
    # I(1), am(2)*, the(3)*, best(4), coder(5)*, here(4), today(5)*
    assert words_in_sentence("I am the best coder here today") == "am the coder today"
    
    # a(1), quick(5)*, brown(5)*, fox(3)*, jumps(5)*, over(4), the(3)*, lazy(4), dog(3)*
    assert words_in_sentence("a quick brown fox jumps over the lazy dog") == "quick brown fox jumps the dog"

def test_words_in_sentence_max_constraint():
    """Test a sentence approaching the maximum length constraint (~100 chars)."""
    sentence = "the quick brown fox jumps over the lazy dog and it is a very sunny day in the city of gold"
    # Primes: the(3), quick(5), brown(5), fox(3), jumps(5), the(3), dog(3), and(3), it(2), is(2), sunny(5), day(3), in(2), the(3), of(2)
    expected = "the quick brown fox jumps the dog and it is sunny day in the of"
    assert words_in_sentence(sentence) == expected