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

# STEP 2: PLAN
# Test function names and scenarios:
# - test_empty_sentence: Test with an empty sentence.
# - test_no_prime_length_words: Test with a sentence containing no words with prime lengths.
# - test_single_prime_length_word: Test with a sentence containing only one word with a prime length.
# - test_multiple_prime_length_words: Test with a sentence containing multiple words with prime lengths.
# - test_mixed_length_words: Test with a sentence containing a mix of prime and non-prime length words.
# - test_sentence_with_leading_and_trailing_spaces: Test with a sentence containing leading and trailing spaces.
# - test_long_sentence: Test with a longer sentence.
# - test_sentence_with_all_prime_length_words: Test with a sentence where all words have prime lengths.
# - test_sentence_with_same_length_words: Test with a sentence containing words of the same length, some prime and some not.

# STEP 3: CODE
@pytest.mark.parametrize("sentence, expected", [
    ("", ""),
    ("hello world", ""),
    ("is", "is"),
    ("go for", "go for"),
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("  test  ", ""),
    ("a bb ccc dddd eeeee", "bb ccc"),
    ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "a b c d e f g h i j k l m n o p q r s t u v w x y z"),
    ("aa aaa aaaa aaaaa", "aa aaa aaaaa"),
    ("abc def ghi jkl mno", "abc def ghi jkl mno")
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected