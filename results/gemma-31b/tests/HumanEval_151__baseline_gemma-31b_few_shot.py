
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

def test_double_the_difference_provided_examples():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_double_the_difference_all_odd():
    # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([1, 3, 5]) == 35

def test_double_the_difference_negative_odds():
    # Negative numbers should be ignored even if they are odd
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_non_integers():
    # Floats, strings, and None should be ignored
    assert double_the_difference([1, 3.0, 3, "5", None, 5.5]) == 10 # 1^2 + 3^2 = 10

def test_double_the_difference_mixed_types():
    # Mix of valid odds, evens, negatives, and non-ints
    # Valid odds: 7, 11 -> 49 + 121 = 170
    assert double_the_difference([7, 2, -7, 11, 4.2, "13", -1]) == 170

def test_double_the_difference_large_numbers():
    assert double_the_difference([101]) == 10201