
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''

import pytest

def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    if not lst:
        return 0
    
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

class TestDoubleTheDifference:
    """
    Pytest class for testing the double_the_difference function.
    """

    def test_basic_case(self):
        """Tests a standard case with positive and negative numbers."""
        assert double_the_difference([1, 3, 2, 0]) == 10

    def test_all_negative(self):
        """Tests a case with all negative numbers."""
        assert double_the_difference([-1, -2, 0]) == 0

    def test_single_odd_positive(self):
        """Tests a case with a single odd positive number."""
        assert double_the_difference([9, -2]) == 81

    def test_single_zero(self):
        """Tests a case with a single zero."""
        assert double_the_difference([0]) == 0

    def test_empty_list(self):
        """Tests the case of an empty list."""
        assert double_the_difference([]) == 0

    def test_mixed_types(self):
        """Tests a list with mixed data types (should ignore non-integers)."""
        assert double_the_difference([1, 2.5, "hello", 3]) == 10

    def test_large_numbers(self):
        """Tests with larger odd numbers."""
        assert double_the_difference([11, 13, 15]) == 121 + 169 + 225

    def test_only_even_numbers(self):
        """Tests a list with only even numbers."""
        assert double_the_difference([2, 4, 6]) == 0

    def test_zero_and_odd(self):
        """Tests a list with zero and odd numbers."""
        assert double_the_difference([0, 1, 3]) == 10

    def test_negative_and_odd(self):
        """Tests a list with negative and odd numbers."""
        assert double_the_difference([-1, 3, 5]) == 0

    def test_positive_odd_numbers(self):
        """Tests a list with only positive odd numbers."""
        assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

    def test_mixed_numbers(self):
        """Tests a list with mixed numbers."""
        assert double_the_difference([1, 3, 2, 0]) == 1 + 9

    def test_negative_numbers(self):
        """Tests a list with only negative numbers."""
        assert double_the_difference([-1, -2, -3]) == 0

    def test_negative_and_positive(self):
        """Tests a list with negative and positive numbers."""
        assert double_the_difference([-1, 1, -2, 3]) == 1 + 9

    def test_zero(self):
        """Tests a list with only zero."""
        assert double_the_difference([0]) == 0

    def test_large_numbers2(self):
        """Tests with larger odd numbers."""
        assert double_the_difference([9, 11, 13]) == 81 + 121 + 169

    def test_non_integer_numbers(self):
        """Tests with non-integer numbers."""
        assert double_the_difference([1.5, 2, 3.0]) == 0

    def test_mixed_types2(self):
        """Tests a list with mixed data types (should ignore non-integers)."""
        assert double_the_difference([1, "a", 3, 5.5, 7]) == 1 + 9 + 49

    def test_all_even2(self):
        """Tests a list with only even numbers."""
        assert double_the_difference([2, 4, 6, 8]) == 0

    def test_single_odd_number(self):
        """Tests a list with a single odd number."""
        assert double_the_difference([7]) == 49

    def test_complex_list(self):
        """Tests a complex list with various numbers."""
        assert double_the_difference([1, 2, -3, 4, 5, -6, 7, 8, 9, -10]) == 1 + 25 + 49 + 81

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None