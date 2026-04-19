
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
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a b c d", ""),
    ("hello world", "hello world"),
    ("I am a student", "am student"),
    ("The quick brown fox", "The quick brown fox"),
    ("A very long sentence with some words", "words"),
    ("prime numbers are cool", "prime numbers are"),
    ("one two three four five six seven eight nine ten", "one two three six seven eight ten"),
    ("a", ""),
    ("to", "to"),
    ("the", "the"),
    ("four", ""),
    ("seven", "seven"),
    ("eleven", ""),
    ("thirteen", ""),
    ("seventeen", "seventeen"),
    ("nineteen", "nineteen"),
    ("twenty three", "twenty three"), # 6, 5 -> "three" (Wait, 23 is prime, but word length is 6 and 5)
    # Let's re-evaluate "twenty three": "twenty" (6), "three" (5). Result: "three"
])
def test_words_in_sentence_basic(sentence, expected):
    # Correcting the "twenty three" case in the logic:
    # "twenty" length 6 (not prime), "three" length 5 (prime).
    if sentence == "twenty three":
        expected = "three"
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("apple") == "apple"  # length 5

def test_words_in_sentence_single_word_non_prime():
    assert words_in_sentence("pear") == ""  # length 4

def test_words_in_sentence_all_non_prime():
    assert words_in_sentence("this that test") == ""  # 4, 4, 4

def test_words_in_sentence_all_prime():
    assert words_in_sentence("is the apple") == "is the apple"  # 2, 3, 5

def test_words_in_sentence_max_length():
    # Sentence of 100 characters, all words length 2 (prime)
    sentence = "is " * 49 + "is" 
    expected = " ".join(["is"] * 50)
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_length_one():
    assert words_in_sentence("a") == ""

def test_words_in_sentence_length_two():
    assert words_in_sentence("it") == "it"

def test_words_in_sentence_length_three():
    assert words_in_sentence("cat") == "cat"

def test_words_in_sentence_length_four():
    assert words_in_sentence("bird") == ""