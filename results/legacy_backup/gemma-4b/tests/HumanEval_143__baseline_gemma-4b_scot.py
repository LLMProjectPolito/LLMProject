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

### STEP 1: REASONING
# The function `words_in_sentence` takes a sentence as input and returns a new string containing only the words from the original sentence whose lengths are prime numbers, preserving the original order.
# We need to test various scenarios including empty sentences, sentences with no prime-length words, sentences with multiple prime-length words, and sentences with different word lengths.
# We also need to test the `is_prime` helper function to ensure it correctly identifies prime numbers.

### STEP 2: PLAN
# Test cases:
# 1. Empty sentence: ""
# 2. Sentence with no prime-length words: "This is a test"
# 3. Sentence with one prime-length word: "lets go for swimming"
# 4. Sentence with multiple prime-length words: "This is a test sentence"
# 5. Sentence with a single word that is prime: "abc"
# 6. Sentence with a single word that is not prime: "abcd"
# 7. Sentence with a prime length word at the beginning: "7 abc"
# 8. Sentence with a prime length word at the end: "abc 7"
# 9. Sentence with multiple prime length words in a row: "abc def ghi"
# 10. Sentence with a mix of prime and non-prime length words: "abc def ghi jkl"

### STEP 3: CODE
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("This is a test") == "This is a test"

def test_one_prime_length_word():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_multiple_prime_length_words():
    assert words_in_sentence("This is a test sentence") == "is a test"

def test_single_prime_word():
    assert words_in_sentence("abc") == "abc"

def test_single_non_prime_word():
    assert words_in_sentence("abcd") == "abcd"

def test_prime_word_at_beginning():
    assert words_in_sentence("7 abc") == "7"

def test_prime_word_at_end():
    assert words_in_sentence("abc 7") == "abc"

def test_multiple_prime_words_in_a_row():
    assert words_in_sentence("abc def ghi") == "abc def"

def test_mix_prime_and_non_prime_words():
    assert words_in_sentence("abc def ghi jkl") == "abc def ghi"

def test_prime_length_word_with_spaces():
    assert words_in_sentence("  abc def  ") == "abc def"

def test_is_prime_2():
    assert is_prime(2) == True

def test_is_prime_3():
    assert is_prime(3) == True

def test_is_prime_4():
    assert is_prime(4) == False

def test_is_prime_5():
    assert is_prime(5) == True

def test_is_prime_6():
    assert is_prime(6) == False

def test_is_prime_7():
    assert is_prime(7) == True

def test_is_prime_11():
    assert is_prime(11) == True

def test_is_prime_13():
    assert is_prime(13) == True