
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
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps the dog"),
    ("I am a student", "am student"),
    ("a", ""),
    ("hi", "hi"),
    ("apple", "apple"),
    ("banana", ""),
    ("prime numbers are cool", "prime numbers are"),
    ("one two three four five six seven eight nine ten", "two three five seven"),
    (" ", ""),
    ("abc defgh ijk lmnopq", "abc defgh ijk lmnopq"), # 3, 5, 3, 7 - all prime
    ("abcd efghij klmno pqrstuv", "klmno"), # 4, 6, 5, 7 - wait, 7 is prime. 
    # Let's re-evaluate: "abcd"(4), "efghij"(6), "klmno"(5), "pqrstuv"(7) -> "klmno pqrstuv"
])
def test_words_in_sentence(sentence, expected):
    # Note: The last case in the list above was a thought process, 
    # I will refine the parametrization for the final output.
    pass

# Refined test suite
@pytest.mark.parametrize("sentence, expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a b c d", ""),
    ("hello world", "hello world"),
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps the dog"),
    ("I am a student", "am student"),
    ("a", ""),
    ("hi", "hi"),
    ("apple", "apple"),
    ("banana", ""),
    ("prime numbers are cool", "prime numbers are"),
    ("one two three four five six seven eight nine ten", "two three five seven"),
    ("abc defgh ijk lmnopq", "abc defgh ijk lmnopq"),
    ("abcd efghij klmno pqrstuv", "klmno pqrstuv"),
])
def test_words_in_sentence_final(sentence, expected):
    from solution import words_in_sentence # Assuming the function is in solution.py
    assert words_in_sentence(sentence) == expected

# Since I cannot know the module name, I will write the tests assuming the function is available in the namespace.
# However, the prompt asks for the pytest suite. I will provide the tests calling the function directly.

@pytest.mark.parametrize("sentence, expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a b c d", ""),
    ("hello world", "hello world"),
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps the dog"),
    ("I am a student", "am student"),
    ("a", ""),
    ("hi", "hi"),
    ("apple", "apple"),
    ("banana", ""),
    ("prime numbers are cool", "prime numbers are"),
    ("one two three four five six seven eight nine ten", "two three five seven"),
    ("abc defgh ijk lmnopq", "abc defgh ijk lmnopq"),
    ("abcd efghij klmno pqrstuv", "klmno pqrstuv"),
])
def test_words_in_sentence_logic(sentence, expected):
    assert words_in_sentence(sentence) == expected