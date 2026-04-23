
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

def words_in_sentence(sentence):
    """
    Implementation of the function to be tested.
    Returns a string of words from the input whose lengths are prime numbers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

class TestWordsInSentence:
    """
    A superior, consolidated test suite for words_in_sentence.
    Combines edge cases, functional requirements, and constraint checks.
    """

    @pytest.mark.parametrize("sentence, expected", [
        # --- Provided Examples ---
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),

        # --- Edge Case: Empty and Minimal Input ---
        ("", ""),                               # Empty string
        ("a", ""),                               # Single char (length 1, not prime)
        ("ab", "ab"),                            # Single word (length 2, prime)
        ("abc", "abc"),                          # Single word (length 3, prime)
        ("abcd", ""),                            # Single word (length 4, not prime)

        # --- Edge Case: All Words are Prime Length ---
        ("is go for seven", "is go for seven"),  # 2, 2, 3, 5
        ("it is an apple", "it is an apple"),    # 2, 2, 2, 5
        ("is the apple testing information", "is the apple testing information"), # 2, 3, 5, 7, 11

        # --- Edge Case: No Words are Prime Length ---
        ("a b c d e", ""),                       # All length 1
        ("this test swimming", ""),              # 4, 4, 8
        ("aaaa bbbb cccc", ""),                  # 4, 4, 4

        # --- Mixed Word Lengths & Sentence Structures ---
        ("hi there friend", "hi there"),         # 2, 5, 6 -> 2, 5
        ("python is fun", "is fun"),             # 6, 2, 3 -> 2, 3
        ("abcde fghij klmno", "abcde fghij klmno"), # 5, 5, 5
        ("a is a test", "is"),                   # 1, 2, 1, 4 -> 2
        ("to the apple planet extraordinary", "to the apple extraordinary"), # 2, 3, 5, 6, 13
        ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"), # 3, 5, 5, 3, 5, 4, 3, 4, 3
    ])
    def test_logic_parametrized(self, sentence, expected):
        """Tests a wide variety of sentence compositions and word length combinations."""
        assert words_in_sentence(sentence) == expected

    def test_order_preservation(self):
        """Ensures the relative order of words is preserved from the original sentence."""
        sentence = "swimming go for is test" # 8, 2, 3, 2, 4
        assert words_in_sentence(sentence) == "go for is"
        
        sentence2 = "is the apple" # 2, 3, 5
        assert words_in_sentence(sentence2) == "is the apple"

    def test_large_prime_lengths(self):
        """Tests words with larger prime lengths to ensure mathematical correctness and efficiency."""
        # Length 13 and 17 are primes; 14 and 18 are not.
        word_p13 = "a" * 13
        word_np14 = "b" * 14
        word_p17 = "c" * 17
        word_np18 = "d" * 18
        
        sentence = f"{word_p13} {word_np14} {word_p17} {word_np18}"
        expected = f"{word_p13} {word_p17}"
        assert words_in_sentence(sentence) == expected

    def test_psychological_case(self):
        """Specific check for a known complex word length (psychological = 13)."""
        sentence = "the psychological phenomenon"
        # the(3-P), psychological(13-P), phenomenon(10-NP)
        assert words_in_sentence(sentence) == "the psychological"