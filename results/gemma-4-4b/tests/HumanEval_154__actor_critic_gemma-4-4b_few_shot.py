
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n = len(b)

    if n == 0:
        return True  # Empty string is a substring of any string

    if len(a) == 0 and n > 0:
        return False #If a is empty and b is not, b cannot be a substring of a

    if len(a) == n:
        return True #If a and b are same length, and a is a rotation of b

    for i in range(n):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

### Problem:
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """

### Tests (Pytest):