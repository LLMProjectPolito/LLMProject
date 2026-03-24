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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_positive_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_zero():
    assert double_the_difference([0]) == 0

def test_mixed_positive_negative_and_zero():
    assert double_the_difference([1, -2, 0, 3]) == 10

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2, 3.0]) == 0

def test_string_in_list():
    assert double_the_difference([1, "a", 3]) == 10

def test_all_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_large_odd_number():
    assert double_the_difference([99]) == 9801

def test_mixed_types():
    assert double_the_difference([1, 2.5, "hello", 3]) == 10

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_large_list():
    assert double_the_difference([i for i in range(100) if i % 2 != 0]) == 2550