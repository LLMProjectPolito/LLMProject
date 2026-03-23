def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not a or not b:
        return False

    if len(a) == 0 or len(b) == 0:
        return False

    if a == b:
        return True

    if len(a) == 1 and len(b) == 1:
        return a == b

    if len(a) == 1 and len(b) == 2:
        return b in a

    if len(a) == 2 and len(b) == 1:
        return b in a

    if len(a) == 1 and len(b) == 2:
        return a in b

    if len(a) == 2 and len(b) == 2:
        return b in a
        
    return False