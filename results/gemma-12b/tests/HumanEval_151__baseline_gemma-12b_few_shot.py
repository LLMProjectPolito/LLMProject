
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

def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_single_odd():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_single_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([1, -2, 3, 0, 5]) == 1 + 9 + 25

def test_double_the_difference_floats():
    assert double_the_difference([1.5, 2, 3.0]) == 0

def test_double_the_difference_strings():
    assert double_the_difference([1, "a", 3]) == 1 + 9

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_double_the_difference_large_numbers():
    assert double_the_difference([101, 203]) == 10201 + 41209

def test_double_the_difference_negative_and_odd():
    assert double_the_difference([-1, 3, -5]) == 0