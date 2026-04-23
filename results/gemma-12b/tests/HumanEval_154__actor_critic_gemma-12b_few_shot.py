
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

def cycpattern_check(a, b):
    """
    Checks if the second word (b) or any of its rotations is a substring in the first word (a).
    """
    if not b:
        return False
    if not a:
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False


def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_whassup():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_abab_baa():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_efef_eeff():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_himenss_simen():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_a_equals_b():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcdef") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_pattern_at_beginning():
    assert cycpattern_check("abcde", "abc") == True

def test_cycpattern_check_overlapping_pattern():
    assert cycpattern_check("ababab", "abab") == True

def test_cycpattern_check_repeated_characters():
    assert cycpattern_check("aabbcc", "bbcc") == True

def test_cycpattern_check_special_characters():
    assert cycpattern_check("a1b2c3", "b2c3") == True

def test_cycpattern_check_rotation_at_end():
    assert cycpattern_check("xyzabc", "abc") == True

def test_cycpattern_check_complex_rotation():
    assert cycpattern_check("abcdefgh", "efghabc") == True