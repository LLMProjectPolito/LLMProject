
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

```python
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()


import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('race a car') == False
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('abccba') == True
    assert is_palindrome('abcba') == True
    assert is_palindrome('a') == True
    assert is_palindrome('b') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('abc') == False
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome('civic') == True
    assert is_palindrome('reviver') == True
    assert is_palindrome('redder') == True
    assert is_palindrome('madam') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('Amore, Roma') == True
    assert is_palindrome('No lemon, no melon') == True
    assert is_palindrome('Eva, can I see bees dance on a one-eyed walrus?') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([10, 5, 20, 1]) == 20
    assert get_max([1, 1, 1]) == 1
    assert get_max([1]) == 1

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-10, -5, -20, -1]) == -1
    assert get_max([-1, -1, -1]) == -1

def test_get_max_mixed():
    assert get_max([-1, 0, 1]) == 1
    assert get_max([-1, 0, -1]) == 0
    assert get_max([1, 0, -1]) == 1

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("abc def ghi") == ""

def test_words_in_sentence_single_prime_length():
    assert words_in_sentence("is") == "is"
    assert words_in_sentence("go for") == "go for"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_multiple_prime_lengths():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("I am a test") == "am"
    assert words_in_sentence("hello world") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == ""

def test_words_in_sentence_mixed_lengths():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("I am a test") == "am"
    assert words_in_sentence("hello world") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n") == ""
    assert words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z