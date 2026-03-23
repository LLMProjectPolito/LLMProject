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
    if not lst:
        return 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

class TestDoubleTheDifference:
    def test_empty_list(self):
        assert double_the_difference([]) == 0

    def test_positive_odd_numbers(self):
        assert double_the_difference([1, 3, 5]) == 1 + 9 + 25 == 35

    def test_mixed_numbers(self):
        assert double_the_difference([1, 3, 2, 0]) == 1 + 9 == 10

    def test_negative_numbers(self):
        assert double_the_difference([-1, -2, -3]) == 0

    def test_negative_and_positive(self):
        assert double_the_difference([-1, 3, -5, 7]) == 9 + 49 == 58

    def test_zero(self):
        assert double_the_difference([0]) == 0

    def test_single_odd_number(self):
        assert double_the_difference([5]) == 25

    def test_single_even_number(self):
        assert double_the_difference([2]) == 0

    def test_single_negative_number(self):
        assert double_the_difference([-3]) == 0

    def test_large_numbers(self):
        assert double_the_difference([9, 21]) == 81 + 441 == 522

    def test_floats_and_strings(self):
        assert double_the_difference([1, 3.14, "hello", 5]) == 1 + 25 == 26

    def test_mixed_types(self):
        assert double_the_difference([1, -2, 3.0, 5, "a"]) == 1 + 25 == 26

    def test_all_even_numbers(self):
        assert double_the_difference([2, 4, 6, 8]) == 0

    def test_all_negative_numbers(self):
        assert double_the_difference([-1, -2, -3, -4]) == 0