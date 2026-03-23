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

class TestWordsInSentence:
    def test_empty_sentence(self):
        assert words_in_sentence("") == ""

    def test_single_prime_word(self):
        assert words_in_sentence("is") == "is"

    def test_single_non_prime_word(self):
        assert words_in_sentence("a") == ""
        assert words_in_sentence("test") == ""

    def test_example_1(self):
        assert words_in_sentence("This is a test") == "is"

    def test_example_2(self):
        assert words_in_sentence("lets go for swimming") == "go for"

    def test_all_prime_words(self):
        assert words_in_sentence("is are was") == "is are was"

    def test_all_non_prime_words(self):
        assert words_in_sentence("a an the") == ""

    def test_mixed_prime_and_non_prime(self):
        assert words_in_sentence("hello is a world") == "is"

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  is a test  ") == "is"

    def test_sentence_with_multiple_spaces(self):
        assert words_in_sentence("is   a    test") == "is"

    def test_long_sentence(self):
        assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the over dog"

    def test_sentence_with_long_prime_word(self):
        assert words_in_sentence("programming is fun") == "programming"

    def test_sentence_with_long_non_prime_word(self):
        assert words_in_sentence("abcdefghijk is fun") == "is"

    def test_sentence_with_numbers_and_letters(self):
        assert words_in_sentence("a1 is b2") == "is"

    def test_sentence_with_special_characters(self):
        assert words_in_sentence("a! is b@") == "is"

    def test_sentence_with_uppercase_and_lowercase(self):
        assert words_in_sentence("Is a Test") == "Is"

    def test_multiple_words_some_prime(self):
        assert words_in_sentence("This is a test") == "is"

    def test_multiple_words_all_prime(self):
        assert words_in_sentence("go for") == "go for"

    def test_multiple_words_none_prime(self):
        assert words_in_sentence("hello world test") == ""

    def test_sentence_with_leading_and_trailing_spaces(self):
        assert words_in_sentence("  This is a test  ") == "is"

    def test_sentence_with_multiple_spaces_between_words(self):
        assert words_in_sentence("This   is  a   test") == "is"

    def test_long_sentence_with_mixed_words(self):
        assert words_in_sentence("lets go for swimming and running") == "go for"

    def test_sentence_with_prime_and_non_prime_words_at_start_and_end(self):
        assert words_in_sentence("go hello for world") == "go for"

    def test_sentence_with_only_one_word_length_2(self):
        assert words_in_sentence("to") == "to"

    def test_sentence_with_only_one_word_length_3(self):
        assert words_in_sentence("cat") == "cat"

    def test_sentence_with_only_one_word_length_5(self):
        assert words_in_sentence("apple") == "apple"

    def test_sentence_with_only_one_word_length_7(self):
        assert words_in_sentence("orange") == "orange"

    def test_sentence_with_only_one_word_length_11(self):
        assert words_in_sentence("beautiful") == "beautiful"

    def test_sentence_with_words_of_length_1(self):
        assert words_in_sentence("a b c") == ""

    def test_sentence_with_words_of_length_4(self):
        assert words_in_sentence("four test word") == ""

    def test_sentence_with_words_of_length_6(self):
        assert words_in_sentence("sixteen number") == ""

    def test_sentence_with_words_of_length_8(self):
        assert words_in_sentence("eighteen example") == ""

    def test_sentence_with_words_of_length_9(self):
        assert words_in_sentence("nine words") == ""

    def test_sentence_with_words_of_length_10(self):
        assert words_in_sentence("ten words") == ""

    def test_sentence_with_mixed_lengths_and_primes(self):
        assert words_in_sentence("two three four five six seven") == "two three five seven"