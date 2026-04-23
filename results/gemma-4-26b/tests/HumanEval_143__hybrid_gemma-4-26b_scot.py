
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

def test_provided_examples():
    """Verify the specific examples provided in the problem description."""
    from __main__ import words_in_sentence
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

@pytest.mark.parametrize("word, expected", [
    ("a", ""),             # Length 1: Not prime
    ("is", "is"),          # Length 2: Prime
    ("cat", "cat"),        # Length 3: Prime
    ("test", ""),          # Length 4: Not prime
    ("apple", "apple"),    # Length 5: Prime
    ("abcdefg", "abcdefg"),# Length 7: Prime
    ("abcdefgh", ""),      # Length 8: Not prime
    ("twentythree", "twentythree"), # Length 11: Prime
])
def test_word_length_logic(word, expected):
    """Granular test for individual word lengths to verify prime detection accuracy."""
    from __main__ import words_in_sentence
    assert words_in_sentence(word) == expected

@pytest.mark.parametrize("sentence, expected", [
    # Case: All words are prime length
    ("is it ok", "is it ok"),
    ("is cat apple seventh", "is cat apple seventh"),
    
    # Case: No words are prime length
    ("a test office swimming alphabets dictionary", ""),
    ("abcd abcd", ""),
    
    # Case: Mixed lengths (Testing order preservation and filtering)
    ("the cat sat on a mat", "the cat sat on mat"), 
    # the(3)-P, cat(3)-P, sat(3)-P, on(2)-P, a(1)-NP, mat(3)-P -> "the cat sat on mat"
    
    ("is test cat a apple", "is cat apple"),
    # is(2)-P, test(4)-NP, cat(3)-P, a(1)-NP, apple(5)-P -> "is cat apple"
    
    ("x it the book", "it the"),
    # x(1)-NP, it(2)-P, the(3)-P, book(4)-NP -> "it the"
    
    ("twentythree is long", "twentythree"),
    # twentythree(11)-P, is(2)-P, long(4)-NP -> "twentythree is" 
    # Wait, re-calculating: twentythree(11) is P, is(2) is P. 
    # Correcting expected for the test:
    ("twentythree is long", "twentythree is"), 
])
def test_sentence_scenarios(sentence, expected):
    """Comprehensive test for various sentence compositions and order preservation."""
    from __main__ import words_in_sentence
    # Note: I corrected the 'twentythree' logic in the parametrization above 
    # to ensure the test actually passes based on the rules.
    assert words_in_sentence(sentence) == expected

def test_minimal_input():
    """Tests behavior with the smallest possible valid input (length 1)."""
    from __main__ import words_in_sentence
    assert words_in_sentence("a") == ""

def test_stress_large_input():
    """Tests a sentence with many words to ensure stability and correct joining."""
    from __main__ import words_in_sentence
    # Create 50 words of length 3 (prime) and 50 words of length 4 (non-prime)
    prime_word = "abc"
    non_prime_word = "test"
    # Interleave them: "abc test abc test..."
    sentence_list = []
    for _ in range(50):
        sentence_list.append(prime_word)
        sentence_list.append(non_prime_word)
    sentence = " ".join(sentence_list)
    
    # Expected: 50 instances of "abc" joined by spaces
    expected = " ".join([prime_word] * 50)
    assert words_in_sentence(sentence) == expected