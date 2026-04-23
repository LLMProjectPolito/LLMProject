
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

```python
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
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares


def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_double_the_difference_all_odd():
    assert double_the_difference([1, 3, 5, 7]) == 84

def test_double_the_difference_mixed_positive_negative():
    assert double_the_difference([-1, 2, 3, -4, 5]) == 9 + 25 == 34

def test_double_the_difference_mixed_positive_zero():
    assert double_the_difference([1, 0, 3, 2, 0]) == 1 + 9 == 10

def test_double_the_difference_mixed_positive_negative_zero_negative():
    assert double_the_difference([1, -2, 3, -4, 0]) == 1 + 9 == 10

def test_double_the_difference_large_numbers():
    assert double_the_difference([1000, 2000, 3000]) == 1000000 + 9000000 == 10000000

def test_double_the_difference_with_floats():
    assert double_the_difference([1.0, 2.0, 3.0]) == 0

def test_double_the_difference_with_strings():
    assert double_the_difference(["a", "b", "c"]) == 0

def test_double_the_difference_with_mixed_types():
    assert double_the_difference([1, "a", 3, 2.0]) == 9

def test_double_the_difference_negative_integer():
    assert double_the_difference([-1]) == 1

def test_double_the_difference_single_negative_integer():
    assert double_the_difference([-5]) == 25

def test_double_the_difference_mixed_types_with_negative():
    assert double_the_difference([-1, 2, 3, -4, 5, "a"]) == 9 + 25 == 34

def test_double_the_difference_only_zeroes():
    assert double_the_difference([0, 0, 0]) == 0

def test_double_the_difference_only_negatives():
    assert double_the_difference([-1, -2, -3]) == 0

def test_double_the_difference_only_positives():
    assert double_the_difference([1, 2, 3]) == 14

def test_double_the_difference_with_large_odd_numbers():
    assert double_the_difference([1000000000, 1000000001]) == 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000