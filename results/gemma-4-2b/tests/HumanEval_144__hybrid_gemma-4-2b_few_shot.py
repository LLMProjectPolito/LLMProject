
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
    try:
        num1, den1 = map(int, x.split('/'))
        num2, den2 = map(int, n.split('/'))
        
        result_num = num1 * num2
        result_den = den1 * den2

        if result_den == 0:
            return False

        if result_num % result_den == 0:
            return True
        else:
            return False
    except ValueError:
        return False



def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/2") == True

def test_simplify_different_numbers():
    assert simplify("1/2", "3/4") == False
    assert simplify("5/7", "14/2") == True
    assert simplify("1/3", "6/1") == True

def test_simplify_same_numbers():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("3/3", "3/3") == True

def test_simplify_larger_numbers():
    assert simplify("12/15", "15/3") == True
    assert simplify("123/456", "456/123") == True
    assert simplify("123/456", "123/456") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("2/1", "1/1") == False
    assert simplify("1/2", "1/2") == True
    assert simplify("1/2", "2/2") == False
    assert simplify("1/2", "3/3") == False


def test_simplify_fraction_conversion():
    assert simplify("1/3", "3/1") == True
    assert simplify("2/5", "5/2") == True

def test_simplify_negative_numbers():
    assert simplify("-1/2", "2/1") == False  #Because the function isn't designed for negative fractions, but we test behavior
    assert simplify("1/-2", "2/1") == False #Because the function isn't designed for negative fractions, but we test behavior

def test_simplify_empty_string_input():
    assert simplify("", "1/1") == False #Handle edge case where one of inputs is empty

def test_simplify_invalid_input():
    assert simplify("1/a", "1/1") == False #Test invalid numerator
    assert simplify("1/1", "1/1") == False #Test invalid denominator
    assert simplify("1", "1/1") == False #Test invalid numerator
    assert simplify("1/1", "1") == False #Test invalid denominator



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_special_chars():
    assert is_palindrome('A man, a plan, a canal: Panama') == False #Not a palindrome

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('madam') == True