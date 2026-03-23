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
# edge cases for prime number checking (e.g., 2, 3, 5, 7, 11).

# STEP 2: PLAN - List test functions names and scenarios.
# Test functions:
# - test_empty_sentence: Test with an empty sentence.
# - test_no_prime_length_words: Test with a sentence containing only words with non-prime lengths.
# - test_all_prime_length_words: Test with a sentence containing only words with prime lengths.
# - test_mixed_length_words: Test with a sentence containing a mix of prime and non-prime length words.
# - test_single_prime_word: Test with a sentence containing only one prime-length word.
# - test_sentence_with_spaces: Test with leading/trailing spaces.
# - test_prime_numbers: Test with words of lengths 2, 3, 5, 7, 11.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is a test") == ""

def test_all_prime_length_words():
    assert words_in_sentence("go to do") == "go to do"

def test_mixed_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_single_prime_word():
    assert words_in_sentence("go") == "go"

def test_sentence_with_spaces():
    assert words_in_sentence("  lets go for swimming  ") == "go for"

def test_prime_numbers():
    assert words_in_sentence("a bb ccc dddd eeeee") == "a bb ccc"

def test_longer_sentence():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox the dog"

def test_sentence_with_one_long_word():
    assert words_in_sentence("abcdefghijk") == "abcdefghijk"