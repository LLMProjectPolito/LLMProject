
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

# The function words_in_sentence is assumed to be imported or defined in the environment.

@pytest.mark.parametrize("sentence, expected", [
    # --- Standard Examples ---
    ("This is a test", "is"),                # lengths: 4, 2, 1, 4 -> 2 is prime
    ("lets go for swimming", "go for"),      # lengths: 4, 2, 3, 8 -> 2, 3 are prime
    
    # --- Prime Logic & Edge Cases ---
    ("a test this a", ""),                   # lengths: 1, 4, 4, 1 -> none prime
    ("is the apple", "is the apple"),        # lengths: 2, 3, 5 -> all prime
    ("i am a student", "am student"),        # lengths: 1, 2, 1, 7 -> 2, 7 are prime
    ("it is ok", "it is ok"),                # lengths: 2, 2, 2 -> all prime
    
    # --- Larger Primes ---
    # "The"(3), "extraordinary"(13), "phenomenon"(10)
    ("The extraordinary phenomenon", "The extraordinary"), 
    # "Communication"(13), "is"(2), "key"(3)
    ("Communication is key", "Communication is key"),
    
    # --- Numeric Strings ---
    ("123 1234", "123"),                     # lengths: 3, 4 -> 3 is prime
    ("11 13 17 19", "11 13 17 19"),          # lengths: 2, 2, 2, 2 -> all prime
    
    # --- Complex Sentence Verification ---
    # the(3), quick(5), brown(5), fox(3), jumps(5), over(4), the(3), lazy(4), dog(3)
    ("the quick brown fox jumps over the lazy dog", "the quick brown fox jumps the dog"),
    
    # --- Whitespace Handling ---
    ("  hello   world  ", "hello world"),    # lengths: 5, 5 -> both prime
    ("   ", ""),                             # Only whitespace
    ("", ""),                                # Empty string
    
    # --- Punctuation Handling ---
    ("Hi!", "Hi!"),                          # length: 3 -> prime
    ("Hello, world!", ""),                   # lengths: 6, 6 -> neither prime
    ("Wait... what?", "Wait... what?"),      # lengths: 7, 5 -> both prime
    
    # --- Non-ASCII / Unicode ---
    ("Étude", "Étude"),                      # length: 5 -> prime
    ("Café", ""),                            # length: 4 -> not prime
    ("🍎", ""),                              # length: 1 -> not prime
    ("Python 🐍", ""),                       # lengths: 6, 1 -> neither prime
    ("你好吗", "你好吗"),                      # length: 3 -> prime
])
def test_words_in_sentence(sentence, expected):
    """
    Tests the words_in_sentence function across various scenarios including
    prime logic, larger primes, numeric strings, irregular whitespace, 
    punctuation, and unicode characters.
    """
    assert words_in_sentence(sentence) == expected

def test_max_constraint():
    """
    Tests the upper boundary constraint of 100 characters.
    """
    # "is " is 3 chars. 33 * 3 = 99. 99 + "i" = 100.
    sentence = "is " * 33 + "i" 
    # "is" (2) is prime, "i" (1) is not.
    expected = " ".join(["is"] * 33)
    assert words_in_sentence(sentence) == expected