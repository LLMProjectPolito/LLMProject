import pytest

def cycpattern_check(a, b):
    """
    Checks if the second word or any of its rotations is a substring of the first word.
    """
    if len(a) == 0 or len(b) == 0:
        return False

    if len(a) == 1 and len(b) == 1:
        return a.lower() in b.lower()

    if len(a) == 1:
        return a.lower() in b.lower()

    if len(b) == 1:
        return b.lower() in a.lower()

    for i in range(1, len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True

    return False


def test_cycpattern_check():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

    # Test cases with different lengths
    assert cycpattern_check("abc", "cba") == True
    assert cycpattern_check("abcd", "dcb") == True
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abc", "ab") == False
    assert cycpattern_check("abc", "a") == False
    assert cycpattern_check("abc", "ab") == False
    assert cycpattern_check("abc", "abc") == True

    # Edge cases - empty strings
    assert cycpattern_check("", "") == False
    assert cycpattern_check("a", "") == False
    assert cycpattern_check("", "a") == False

    # More complex cases
    assert cycpattern_check("abcdefg", "cdefg") == True
    assert cycpattern_check("abcdefg", "fedc") == False
    assert cycpattern_check("abcdefg", "gfed") == True
    assert cycpattern_check("abcdefg", "efg") == False
    assert cycpattern_check("abcdefg", "abcdef") == True
    assert cycpattern_check("abcdefg", "abcdefgh") == False

    print("All test cases passed!")