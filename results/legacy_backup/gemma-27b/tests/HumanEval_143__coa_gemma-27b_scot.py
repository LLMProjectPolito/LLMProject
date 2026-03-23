import pytest
import math


# Focus: Prime Number Word Lengths
import pytest

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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `words_in_sentence` filters words from a sentence based on whether their lengths are prime numbers.
# We need to test cases with sentences containing words of prime and non-prime lengths,
# including empty sentences and sentences with only non-prime length words.

# STEP 2: PLAN - List test functions names and scenarios.
# test_prime_word_lengths_basic: Basic test case with a mix of prime and non-prime length words.
# test_prime_word_lengths_all_prime: Test case where all words have prime lengths.
# test_prime_word_lengths_no_prime: Test case where no words have prime lengths.
# test_prime_word_lengths_empty_sentence: Test case with an empty sentence.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_prime_word_lengths_basic():
    assert words_in_sentence("This is a test") == "is"

def test_prime_word_lengths_all_prime():
    assert words_in_sentence("go for") == "go for"

def test_prime_word_lengths_no_prime():
    assert words_in_sentence("hello world") == ""

def test_prime_word_lengths_empty_sentence():
    assert words_in_sentence("") == ""

# Focus: Empty/Null Input
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

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_null_sentence():
    with pytest.raises(TypeError):
        words_in_sentence(None)

def test_sentence_with_only_spaces():
    assert words_in_sentence("   ") == ""

# Focus: Sentence with Non-Space Characters Only
import pytest

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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `words_in_sentence` filters words from a sentence based on whether their lengths are prime numbers.
# The constraint is that the sentence contains only letters. We need to test cases where the sentence contains only letters and
# where the words have prime lengths, and where they don't.

# STEP 2: PLAN - List test functions names and scenarios.
# test_sentence_with_prime_length_words: Tests a sentence where some words have prime lengths.
# test_sentence_with_no_prime_length_words: Tests a sentence where no words have prime lengths.
# test_sentence_with_non_space_characters_only: Tests a sentence with no spaces.

def test_sentence_with_prime_length_words():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("two three five seven") == "two three five seven"

def test_sentence_with_no_prime_length_words():
    assert words_in_sentence("four six eight ten") == ""
    assert words_in_sentence("one two four") == "two"

def test_sentence_with_non_space_characters_only():
    assert words_in_sentence("abcdef") == ""
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("ab") == "ab"
    assert words_in_sentence("a") == "a"