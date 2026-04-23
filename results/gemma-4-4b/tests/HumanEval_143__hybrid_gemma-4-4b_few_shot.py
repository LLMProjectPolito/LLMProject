
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
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]


def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Pytest Suite
def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == "world"
    assert words_in_sentence("") == ""
    assert words_in_sentence("a") == "a"
    assert words_in_sentence("ab") == "ab"
    assert words_in_sentence("racecar") == "racecar"
    assert words_in_sentence("madam") == "madam"
    assert words_in_sentence("level") == "level"
    assert words_in_sentence("rotor") == "rotor"
    assert words_in_sentence("deified") == "deified"
    assert words_in_sentence("refer") == "refer"
    assert words_in_sentence("noon") == "noon"
    assert words_in_sentence("kayak") == "kayak"
    assert words_in_sentence("stats") == "stats"
    assert words_in_sentence("civic") == "civic"
    assert words_in_sentence("redder") == "redder"
    assert words_in_sentence("wow") == "wow"
    assert words_in_sentence("a man a plan a canal panama") == "a a a a"
    assert words_in_sentence("able was I ere I saw elba") == "able was I ere I saw elba"



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man a plan a canal Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('') == True

def test_palindrome_empty():
    assert is_palindrome('') == True


def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_single():
    assert get_max([5]) == 5

def test_get_max_all_same():
    assert get_max([7, 7, 7]) == 7