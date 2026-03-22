def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_example2():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_prime():
    assert words_in_sentence("This is a test sentence") == ""

def test_words_in_sentence_multiple_prime():
    assert words_in_sentence("one two three four five") == "two three"

def test_words_in_sentence_all_prime():
    assert words_in_sentence("one two three") == "two three"

def test_words_in_sentence_single_word_prime():
    assert words_in_sentence("abc") == "abc"

def test_words_in_sentence_single_word_non_prime():
    assert words_in_sentence("abcd") == ""

def test_is_prime_1():
    assert is_prime(1) == False

def test_is_prime_2():
    assert is_prime(2) == True

def test_is_prime_3():
    assert is_prime(3) == True

def test_is_prime_4():
    assert is_prime(4) == False

def test_is_prime_5():
    assert is_prime(5) == True

def test_is_prime_6():
    assert is_prime(6) == False

def test_is_prime_7():
    assert is_prime(7) == True