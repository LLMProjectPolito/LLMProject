import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                result.append(int(digit))
                break
    return sorted(list(set(result)))

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam.') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_multiple_even():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_large_range():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_generate_integers_with_zero():
    assert generate_integers(0, 10) == [0, 2, 4, 6, 8, 10]

def test_generate_integers_mixed():
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(5, 1) == [2, 4]
    assert generate_integers(11, 15) == [12, 14]
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(10, 20) == [12, 14, 16, 18]
    assert generate_integers(20, 30) == [22, 24, 26, 28]

def test_generate_integers_edge_cases():
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]