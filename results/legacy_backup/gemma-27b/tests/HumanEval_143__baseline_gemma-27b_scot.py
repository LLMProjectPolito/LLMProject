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

@pytest.mark.parametrize("sentence, expected", [
    ("", ""),
    ("hello world", ""),
    ("a bb ccc dddd", "a bb ccc"),
    ("lets go for swimming", "go for"),
    ("This is a test", "is"),
    ("two three five seven", "two three five seven"),
    ("one", ""),
    ("two", "two"),
    ("  hello world  ", ""),
    ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "a b c d e f g h i j k l m n o p q r s t u v w x y z")
])
def test_words_in_sentence(sentence, expected):
    assert words_in_sentence(sentence) == expected

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("hello world") == ""

def test_all_prime_length_words():
    assert words_in_sentence("two three five seven") == "two three five seven"

def test_mixed_length_words():
    assert words_in_sentence("a bb ccc dddd") == "a bb ccc"

def test_single_word_prime():
    assert words_in_sentence("two") == "two"

def test_single_word_non_prime():
    assert words_in_sentence("one") == ""

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == ""

def test_prime_number_check():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False