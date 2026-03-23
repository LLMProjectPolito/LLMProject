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

# STEP 2: PLAN
# Test functions:
# - test_empty_sentence: Test with an empty sentence.
# - test_no_prime_length_words: Test with a sentence containing only words with non-prime lengths.
# - test_all_prime_length_words: Test with a sentence containing only words with prime lengths.
# - test_mixed_length_words: Test with a sentence containing a mix of prime and non-prime length words.
# - test_single_prime_length_word: Test with a sentence containing only one word with a prime length.
# - test_sentence_with_leading_and_trailing_spaces: Test with leading and trailing spaces.
# - test_sentence_with_multiple_spaces: Test with multiple spaces between words.
# - test_long_sentence: Test with a longer sentence.
# - test_sentence_with_same_length_words: Test with words of the same length, some prime, some not.

@pytest.mark.parametrize("sentence, expected", [
    ("", ""),
    ("hello world", ""),
    ("is a", "is a"),
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    ("a bb ccc dddd", "a bb ccc"),
    ("abc def ghi jklm", "abc def jklm"),
    ("very long sentence with many words", "very long"),
    ("  leading and trailing spaces  ", "leading trailing"),
    ("multiple   spaces   between   words", "multiple between words"),
    ("two two two", ""),
    ("a ab abc abcd abcde", "a ab abc abcde"),
    ("a a a a", ""),
    ("a bb ccc dddd eeeee", "a bb ccc eeeee"),
    ("hello  world", "hello world"),
    ("two three five seven", "two three five seven"),
    ("two three four five", "two three five"),
    ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "a b c d e f g h i j k l m n o p q r s t u v w x y z"),
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected