
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

def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == ""
    assert words_in_sentence("a bb ccc dddd") == "a bb ccc"
    assert words_in_sentence("very long sentence with some words") == "very long some"
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the quick fox jumps over dog"
    assert words_in_sentence("a") == "a"
    assert words_in_sentence("aa") == ""  # Length 2 is not prime
    assert words_in_sentence("aaa") == "aaa"
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""  # Handle whitespace only
    assert words_in_sentence("  hello world  ") == "hello world" # Leading/trailing spaces
    assert words_in_sentence("p") == "p"
    assert words_in_sentence("pp") == ""
    assert words_in_sentence("ppp") == "ppp"
    assert words_in_sentence("This is a very very long sentence") == "is very long"
    assert words_in_sentence("one two three four five six seven eight nine ten") == "one three five seven"
    assert words_in_sentence("two three five seven eleven thirteen seventeen nineteen") == "two three five seven eleven thirteen seventeen nineteen"

    # Longer sentence with a mix of prime and non-prime word lengths
    assert words_in_sentence("the quick brown fox jumps over the lazy dog and cat") == "the quick fox jumps over dog cat"

    # Test with a larger prime number
    assert words_in_sentence("a verylongword") == "verylongword"

    # Test case with mixed case
    assert words_in_sentence("This Is A Test") == "Is Test"

    # Test case with punctuation - should ideally raise an exception or filter
    # For now, we'll just check it doesn't crash.  A more robust solution would handle this.
    assert words_in_sentence("hello, world!") == ""

    # Test case with numbers - should ideally raise an exception or filter
    # For now, we'll just check it doesn't crash. A more robust solution would handle this.
    assert words_in_sentence("one 2 three 4 five") == "one three five"