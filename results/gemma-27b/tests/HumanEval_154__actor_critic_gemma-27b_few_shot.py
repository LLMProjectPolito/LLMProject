
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
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    The check is case-insensitive.

    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    cycpattern_check("abc","") => True
    cycpattern_check("","abc") => False
    cycpattern_check("","") => False
    cycpattern_check("abc","abc") => True

    >>> cycpattern_check("abcd","abd")
    False
    >>> cycpattern_check("hello","ell")
    True
    >>> cycpattern_check("whassup","psus")
    False
    >>> cycpattern_check("abab","baa")
    True
    >>> cycpattern_check("efef","eeff")
    False
    >>> cycpattern_check("himenss","simen")
    True
    >>> cycpattern_check("abc","")
    True
    >>> cycpattern_check("","abc")
    False
    >>> cycpattern_check("","")
    False
    >>> cycpattern_check("abc","abc")
    True
    """
    a = a.lower()
    b = b.lower()

    if not b:
        return True

    if not a:
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False