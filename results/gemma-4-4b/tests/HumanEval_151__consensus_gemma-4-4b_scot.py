
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

    def test_example_1(self):
        assert double_the_difference([1, 3, 2, 0]) == 10

    def test_example_2(self):
        assert double_the_difference([-1, -2, 0]) == 0

    def test_example_3(self):
        assert double_the_difference([9, -2]) == 81

    def test_example_4(self):
        assert double_the_difference([0]) == 0

    def test_all_even(self):
        assert double_the_difference([2, 4, 6]) == 0

    def test_all_odd(self):
        assert double_the_difference([1, 3, 5, 7]) == 84

    def test_mixed_positive_negative_odd_even(self):
        assert double_the_difference([-1, 2, 3, -4, 5]) == 35

    def test_with_zero(self):
        assert double_the_difference([0, 1, 0, 3]) == 10

    def test_with_large_numbers(self):
        assert double_the_difference([1001, 2000, 3003]) == 1002002

    def test_non_integer_input(self):
        assert double_the_difference([1.5, 2, 3]) == 9

    def test_negative_integer_input(self):
        assert double_the_difference([-1, -3, -5]) == 0

    def test_mixed_valid_invalid(self):
        assert double_the_difference([1, "a", 3, 2.5, 5]) == 35