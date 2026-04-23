
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
    def fraction_to_float(fraction):
        num, den = map(int, fraction.split('/'))
        return num / den

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)
    product = x_float * n_float

    return product.is_integer()

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


class TestSimplify:

    def test_simplify_basic_true(self):
        assert simplify("1/5", "5/1") == True

    def test_simplify_basic_false(self):
        assert simplify("1/6", "2/1") == False

    def test_simplify_another_false(self):
        assert simplify("7/10", "10/2") == False

    def test_simplify_small_true(self):
        assert simplify("1/2", "2/1") == True

    def test_simplify_small_false(self):
        assert simplify("1/3", "2/5") == False
    
    def test_simplify_larger_numbers_true(self):
         assert simplify("1/4", "4/1") == True
    
    def test_simplify_larger_numbers_false(self):
        assert simplify("3/8", "4/5") == False

    def test_simplify_same_numerator_true(self):
        assert simplify("2/7", "14/1") == True

    def test_simplify_same_denominator_true(self):
        assert simplify("1/3", "1/3") == True

    def test_simplify_mixed_case(self):
        assert simplify("1/5", "5/1") == True

    def test_simplify_large_values_true(self):
        assert simplify("100/200", "200/100") == True
    
    def test_simplify_large_values_false(self):
         assert simplify("100/200", "201/100") == False

    def test_simplify_decimal_representation_true(self):
        assert simplify("2/4", "4/2") == True
    
    def test_simplify_decimal_representation_false(self):
        assert simplify("3/4", "5/2") == False
    
    def test_simplify_numerator_denominator_swap(self):
        assert simplify("5/1", "1/5") == True

    def test_simplify_edge_case_one(self):
        assert simplify("1/1", "1/1") == True

    def test_simplify_edge_case_zero_numerator(self):
        assert simplify("0/1", "1/1") == True # edge case, though question states numerator must be positive

    def test_simplify_edge_case_zero_denominator(self):
        with pytest.raises(ZeroDivisionError):
            simplify("1/1", "1/0")

class TestPalindrome:

    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

    def test_palindrome_case_insensitive(self):
        assert is_palindrome('Racecar') == True

    def test_palindrome_with_spaces(self):
        assert is_palindrome('A man, a plan, a canal: Panama') == True

    def test_palindrome_with_punctuation(self):
        assert is_palindrome('Madam, I\'m Adam!') == True

class TestGetMax:

    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None

    def test_max_single_element(self):
        assert get_max([5]) == 5

    def test_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4

    def test_max_duplicate(self):
        assert get_max([1, 1, 1]) == 1