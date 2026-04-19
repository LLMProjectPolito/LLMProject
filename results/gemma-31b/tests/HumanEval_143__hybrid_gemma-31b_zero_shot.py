
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
    Returns words from the sentence whose lengths are prime numbers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = [word for word in words if is_prime(len(word))]
    return " ".join(result)

@pytest.mark.parametrize("sentence, expected", [
    # Basic Examples
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
    
    # Edge Case: No words have prime lengths
    ("a test", ""),             # 1, 4
    ("banana orange", ""),      # 6, 6
    ("four a", ""),             # 4, 1
    
    # Edge Case: All words have prime lengths
    ("go for it", "go for it"), # 2, 3, 2
    ("the cat sat", "the cat sat"), # 3, 3, 3
    ("hi you are", "hi you are"),   # 2, 3, 3
    
    # Edge Case: Single word sentences
    ("a", ""),                  # 1 (Not prime)
    ("to", "to"),              # 2 (Prime)
    ("the", "the"),            # 3 (Prime)
    ("test", ""),              # 4 (Not prime)
    ("apple", "apple"),        # 5 (Prime)
    ("hello", "hello"),        # 5 (Prime)
    
    # Length checks: Mixed Prime vs Composite
    ("i am a student", "am student"), # 1, 2, 1, 7 -> 2, 7
    ("The quick brown fox jumps over the lazy dog", "The quick brown fox jumps the dog"), 
    # Analysis: The(3), quick(5), brown(5), fox(3), jumps(5), over(4), the(3), lazy(4), dog(3)
    
    # Test with larger prime lengths
    ("this is an extraordinary circumstance", "is an extraordinary"), 
    # Analysis: this(4), is(2), an(2), extraordinary(13), circumstance(12)
    
    # Pattern-based prime length check
    ("aa aaa aaaa aaaaa aaaaaa aaaaaaa", "aa aaa aaaaa aaaaaaa"), 
    # Lengths: 2(P), 3(P), 4(NP), 5(P), 6(NP), 7(P)
])
def test_words_in_sentence_parametrized(sentence, expected):
    """Test the words_in_sentence function with a wide variety of scenarios."""
    assert words_in_sentence(sentence) == expected

def test_empty_and_whitespace():
    """Test behavior with empty strings or strings containing only whitespace."""
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""
    assert words_in_sentence("\n\t") == ""

def test_single_character():
    """Test a sentence consisting of a single character (length 1 is not prime)."""
    assert words_in_sentence("x") == ""

def test_long_words():
    """Test very long words to verify primality logic for larger numbers."""
    # 17 is prime
    long_prime = "a" * 17
    assert words_in_sentence(long_prime) == long_prime
    
    # 18 is composite
    long_composite = "a" * 18
    assert words_in_sentence(long_composite) == ""

def test_max_constraint_length():
    """Test a sentence approaching the maximum constraint length (e.g., 100 chars)."""
    # Create a string of 50 words, each 2 characters long (2 is prime)
    long_sentence = "ab " * 50
    long_sentence = long_sentence.strip()
    result = words_in_sentence(long_sentence)
    assert result == long_sentence
    assert len(result) <= 100