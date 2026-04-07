
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
        if isinstance(num, int) and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert pytest.approx(double_the_difference([])) == 0

def test_positive_numbers():
    assert pytest.approx(double_the_difference([1, 3, 2, 0])) == 10
    assert pytest.approx(double_the_difference([-1, -2, 0])) == 0
    assert pytest.approx(double_the_difference([9, -2])) == 81
    assert pytest.approx(double_the_difference([0])) == 0

def test_mixed_numbers():
    assert pytest.approx(double_the_difference([1, 2, 3, 4])) == 1 + 9 + 16
    assert pytest.approx(double_the_difference([1, 3, 5])) == 1 + 9 + 25
    assert pytest.approx(double_the_difference([2, 4, 6])) == 4 + 16
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5])) == 1 + 9 + 25 + 49
    assert pytest.approx(double_the_difference([1, 3, 5, 7])) == 1 + 9 + 25 + 49
    assert pytest.approx(double_the_difference([2, 4, 6, 8])) == 4 + 16
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6])) == 1 + 9 + 16 + 25 + 36
    assert pytest.approx(double_the_difference([1, 3, 5, 7, 9])) == 1 + 9 + 25 + 49 + 81
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
    assert pytest.approx(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])) == 1 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100