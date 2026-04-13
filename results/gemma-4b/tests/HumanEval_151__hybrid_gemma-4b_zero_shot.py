
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
    total = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            total += num * num
    return total

class TestDoubleTheDifference:
    def test_empty_list(self):
        assert double_the_difference([]) == 0

    def test_positive_odd_numbers(self):
        assert double_the_difference([1, 3, 5]) == 35

    def test_mixed_positive_and_negative(self):
        assert double_the_difference([1, -2, 3, -4, 5]) == 35

    def test_with_zero(self):
        assert double_the_difference([1, 0, 3, 0, 5]) == 35

    def test_with_negative_numbers(self):
        assert double_the_difference([-1, -3, -5]) == 0

    def test_with_non_integers(self):
        assert double_the_difference([1.5, 3.2, 5.7]) == 0

    def test_with_mixed_types(self):
        assert double_the_difference([1, 2, "a", 3, 4.5]) == 10

    def test_single_odd_number(self):
        assert double_the_difference([1]) == 1

    def test_single_negative_odd_number(self):
        assert double_the_difference([-1]) == 1

    def test_single_zero(self):
        assert double_the_difference([0]) == 0

    def test_example_1(self):
        assert double_the_difference([1, 3, 2, 0]) == 10

    def test_example_2(self):
        assert double_the_difference([-1, -2, 0]) == 0

    def test_example_3(self):
        assert double_the_difference([9, -2]) == 81

    def test_example_4(self):
        assert double_the_difference([0]) == 0