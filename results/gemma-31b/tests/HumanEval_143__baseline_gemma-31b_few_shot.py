
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

def test_words_in_sentence_example1():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_primes():
    # 'a' (1) is not prime, 'test' (4) is not prime
    assert words_in_sentence("a test") == ""

def test_words_in_sentence_all_primes():
    # 'is' (2), 'the' (3), 'cat' (3) are all prime
    assert words_in_sentence("is the cat") == "is the cat"

def test_words_in_sentence_single_char():
    # length 1 is not prime
    assert words_in_sentence("a") == ""

def test_words_in_sentence_single_prime_word():
    # length 2 is prime
    assert words_in_sentence("it") == "it"

def test_words_in_sentence_long_prime():
    # 'extraordinary' has length 13, which is prime
    assert words_in_sentence("extraordinary") == "extraordinary"

def test_words_in_sentence_mixed_lengths():
    # The(3)-P, quick(5)-P, brown(5)-P, fox(3)-P, jumps(5)-P, over(4)-NP, the(3)-P, lazy(4)-NP, dog(3)-P
    sentence = "The quick brown fox jumps over the lazy dog"
    expected = "The quick brown fox jumps the dog"
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_boundary_length():
    # Testing a sentence near the constraint limit (100 chars)
    # 'a' (1) NP, 'bc' (2) P, 'def' (3) P, 'ghij' (4) NP, 'klmno' (5) P
    sentence = "a bc def ghij klmno " * 4
    # Each block: "bc def klmno"
    # Result should be 4 repetitions of those words
    expected = "bc def klmno bc def klmno bc def klmno bc def klmno"
    # Adjusting for the trailing space in the loop logic if necessary, 
    # but the function should handle words separated by spaces.
    assert words_in_sentence(sentence.strip()) == expected