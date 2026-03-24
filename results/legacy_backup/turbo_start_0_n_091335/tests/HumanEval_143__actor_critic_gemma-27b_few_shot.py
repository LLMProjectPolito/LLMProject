import pytest

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
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
    prime_words = [word for word in words if is_prime(len(word)) and word.isalpha()]
    return " ".join(prime_words)

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is", f"Expected 'is' but got '{words_in_sentence('This is a test')}'"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for", f"Expected 'go for' but got '{words_in_sentence('lets go for swimming')}'"

def test_words_in_sentence_no_prime_length_words():
    assert words_in_sentence("hello world") == "", f"Expected '' but got '{words_in_sentence('hello world')}'"

def test_words_in_sentence_handles_empty_string():
    assert words_in_sentence("") == "", f"Expected '' but got '{words_in_sentence('')}'"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("two") == "two", f"Expected 'two' but got '{words_in_sentence('two')}'"

def test_words_in_sentence_single_word_not_prime():
    assert words_in_sentence("one") == "", f"Expected '' but got '{words_in_sentence('one')}'"

def test_words_in_sentence_mixed_lengths():
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the fox the dog", f"Expected 'the fox the dog' but got '{words_in_sentence('the quick brown fox jumps over the lazy dog')}'"

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("a very long sentence with some words of prime length") == "very long some", f"Expected 'very long some' but got '{words_in_sentence('a very long sentence with some words of prime length')}'"

def test_words_in_sentence_with_punctuation():
    with pytest.raises(TypeError):
        words_in_sentence("hello, world!")

def test_words_in_sentence_with_numbers():
    with pytest.raises(TypeError):
        words_in_sentence("one 2 three")

def test_words_in_sentence_case_sensitivity():
    assert words_in_sentence("This Is A Test") == "Is", f"Expected 'Is' but got '{words_in_sentence('This Is A Test')}'"

def test_words_in_sentence_leading_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "hello world", f"Expected 'hello world' but got '{words_in_sentence('  hello world  ')}'"

def test_words_in_sentence_long_input():
    long_sentence = "a" * 90 + " b " + "c" * 90
    assert words_in_sentence(long_sentence) == "b", f"Expected 'b' but got '{words_in_sentence(long_sentence)}'"