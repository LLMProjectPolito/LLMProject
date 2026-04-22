
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

# Note: words_in_sentence is assumed to be imported from your source module

@pytest.mark.parametrize("sentence, expected", [
    ("This is a test", "is"),
    ("lets go for swimming", "go for"),
])
def test_provided_examples(sentence, expected):
    """Tests the specific examples provided in the problem description."""
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize("word, expected", [
    ("a", ""),               # len 1: Not Prime
    ("it", "it"),             # len 2: Prime
    ("cat", "cat"),           # len 3: Prime
    ("test", ""),             # len 4: Not Prime
    ("apple", "apple"),       # len 5: Prime
    ("banana", ""),           # len 6: Not Prime
    ("september", ""),        # len 9: Not Prime
    ("mathematics", "mathematics"), # len 11: Prime
    ("unbelievable", ""),     # len 12: Not Prime
    ("extraordinary", "extraordinary"), # len 13: Prime
])
def test_single_word_scenarios(word, expected):
    """
    Tests single-word inputs covering various lengths:
    - Non-primes: 1, 4, 6, 9, 12
    - Primes: 2, 3, 5, 11, 13
    """
    assert words_in_sentence(word) == expected

def test_sentence_composition():
    """Tests sentences where all words are prime or no words are prime."""
    # All Prime: 2, 2, 3, 5
    assert words_in_sentence("is it cat apple") == "is it cat apple"
    # All Prime: 2, 3, 2, 5, 7
    assert words_in_sentence("is the it apple amazing") == "is the it apple amazing"
    
    # No Prime: 1, 4, 6
    assert words_in_sentence("a abcd banana") == ""
    # No Prime: 1, 1, 1
    assert words_in_sentence("a b c") == ""
    # No Prime: 4, 4, 6
    assert words_in_sentence("abcd efgh ijklmn") == ""

@pytest.mark.parametrize("sentence, expected", [
    # Mixed: We(2-P), are(3-P), very(4-NP), happy(5-P), today(5-P), because(7-P), it(2-P), is(2-P), sunny(5-P), a(1-NP), day(3-P)
    ("We are very happy today because it is sunny a day", 
     "We are happy today because it is sunny day"),
    
    # Mixed: He(2-P), is(2-P), a(1-NP), very(4-NP), smart(5-P), boy(3-P), now(3-P)
    ("He is a very smart boy now", 
     "He is smart boy now"),
    
    # Mixed: abc(3-P), defg(4-NP), hi(2-P)
    ("abc defg hi", "abc hi"),
])
def test_mixed_sentence_complexity(sentence, expected):
    """Tests complex sentences with a mix of prime and non-prime word lengths."""
    assert words_in_sentence(sentence) == expected

def test_order_preservation_and_spacing():
    """Ensures the original word order is preserved and output is correctly formatted."""
    # go(2-P), for(3-P), swimming(8-NP), is(2-P)
    assert words_in_sentence("go for swimming is") == "go for is"
    # cat(3-P), is(2-P), apple(5-P)
    assert words_in_sentence("cat is apple") == "cat is apple"

def test_minimal_input_edge_cases():
    """Tests edge cases like minimal valid length and single characters."""
    # Constraint: 1 <= len(sentence) <= 100
    assert words_in_sentence("z") == ""  # len 1 is not prime
    assert words_in_sentence(" ") == "" # whitespace handling