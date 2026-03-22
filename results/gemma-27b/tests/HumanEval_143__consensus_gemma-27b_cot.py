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

def test_words_in_sentence_empty_sentence():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_all_prime_length_words():
    assert words_in_sentence("go for") == "go for"

def test_words_in_sentence_mixed_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_single_prime_word():
    assert words_in_sentence("two") == "two"

def test_words_in_sentence_single_non_prime_word():
    assert words_in_sentence("one") == ""

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the over the"

def test_words_in_sentence_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_words_in_sentence_sentence_with_multiple_spaces():
    assert words_in_sentence("This  is   a    test") == "is"

def test_words_in_sentence_sentence_with_only_spaces():
    assert words_in_sentence("   ") == ""

def test_is_prime_negative_number():
    assert is_prime(-1) == False

def test_is_prime_zero():
    assert is_prime(0) == False

def test_is_prime_one():
    assert is_prime(1) == False

def test_is_prime_two():
    assert is_prime(2) == True

def test_is_prime_three():
    assert is_prime(3) == True

def test_is_prime_four():
    assert is_prime(4) == False

def test_is_prime_five():
    assert is_prime(5) == True

def test_is_prime_six():
    assert is_prime(6) == False

def test_is_prime_seven():
    assert is_prime(7) == True

def test_is_prime_eight():
    assert is_prime(8) == False

def test_is_prime_nine():
    assert is_prime(9) == False

def test_is_prime_ten():
    assert is_prime(10) == False

def test_is_prime_eleven():
    assert is_prime(11) == True

def test_is_prime_large_prime():
    assert is_prime(7919) == True

def test_is_prime_large_non_prime():
    assert is_prime(7920) == False