
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
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

class TestDoubleTheDifference:
    def test_empty_list(self):
        assert double_the_difference([]) == 0

    def test_positive_odd_numbers(self):
        assert double_the_difference([1, 3, 5]) == 35

    def test_mixed_numbers(self):
        assert double_the_difference([1, 3, 2, 0]) == 10

    def test_negative_numbers(self):
        assert double_the_difference([-1, -2, -3]) == 0

    def test_zero(self):
        assert double_the_difference([0]) == 0

    def test_mixed_positive_and_negative(self):
        assert double_the_difference([-1, 3, -5, 7]) == 58

    def test_single_odd_number(self):
        assert double_the_difference([5]) == 25

    def test_single_even_number(self):
        assert double_the_difference([2]) == 0

    def test_single_negative_number(self):
        assert double_the_difference([-3]) == 0

    def test_non_integer_numbers(self):
        assert double_the_difference([1.5, 2.0, 3.5]) == 0

    def test_strings_in_list(self):
        assert double_the_difference(["1", "2", "3"]) == 0

    def test_mixed_types(self):
        assert double_the_difference([1, 2, "3", 4.0, 5]) == 25

    def test_large_numbers(self):
        assert double_the_difference([1001, 1003]) == 2006000 + 2 #1001**2 + 1003**2

    def test_all_even_numbers(self):
        assert double_the_difference([2, 4, 6, 8]) == 0

    def test_all_negative_numbers(self):
        assert double_the_difference([-1, -2, -3, -4]) == 0

    def test_large_numbers_single(self):
        assert double_the_difference([99]) == 9801

    def test_multiple_odd_numbers_with_negatives(self):
        assert double_the_difference([1, 3, -5, 7, -9]) == 59