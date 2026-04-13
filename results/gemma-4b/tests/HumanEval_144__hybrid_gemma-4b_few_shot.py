
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

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

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))

    product_num = num_x * num_n
    product_den = den_x * den_n

    return product_num % product_den == 0

# Pytest suite for is_palindrome
def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Madam') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

# Pytest suite for get_max
def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

# Pytest suite for simplify
def test_simplify_basic_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/2", "2/1") == True

def test_simplify_basic_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "4/3") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("100/10", "100/1") == True
    assert simplify("100/10", "101/1") == False

def test_simplify_single_digit():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False

def test_simplify_zero_denominator():
    # Although the problem states that x and n do not have zero as denominator,
    # it's good to test the edge case for robustness.
    assert simplify("1/0", "1/1") == False
    assert simplify("1/1", "1/0") == False

def test_simplify_negative_numbers():
    assert simplify("-1/2", "2/1") == False # Should handle negative numbers correctly

def test_simplify_mixed_positive_negative():
    assert simplify("1/2", "-2/1") == False

def test_simplify_complex_fraction():
    assert simplify("3/4", "4/3") == True

def test_simplify_complex_fraction_false():
    assert simplify("3/4", "4/2") == False

# Pytest suite for is_palindrome
def test_is_palindrome_edge_cases():
    assert is_palindrome("A") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("aba") == True
    assert is_palindrome("abcba") == True
    assert is_palindrome("abc") == False

# Pytest suite for get_max
def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_all_same():
    assert get_max([2, 2, 2]) == 2

# Pytest suite for simplify
def test_simplify_zero_numerator():
    assert simplify("0/5", "5/1") == True

def test_simplify_zero_denominator():
    assert simplify("1/0", "1/1") == False

def test_simplify_fraction_with_zero_numerator():
    assert simplify("0/2", "2/1") == True

def test_simplify_fraction_with_zero_denominator():
    assert simplify("1/0", "1/1") == False