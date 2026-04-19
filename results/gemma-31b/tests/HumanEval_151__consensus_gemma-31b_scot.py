
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

def test_provided_examples():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_odd_positives():
    # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([1, 3, 5]) == 35

def test_all_even_positives():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_negative_numbers():
    # Negative odd numbers should be ignored
    assert double_the_difference([-1, -3, -5]) == 0
    # Mix of negative and positive
    assert double_the_difference([-1, 1, -3, 3]) == 10

def test_non_integer_types():
    # Floats should be ignored even if they are "odd" (e.g., 3.0) or positive
    assert double_the_difference([1, 3.0, 5.5, 3]) == 10
    # Mixed types that might be in a list
    assert double_the_difference([1, "3", None, 3]) == 10

def test_large_numbers():
    # 101^2 = 10201
    assert double_the_difference([101]) == 10201

def test_mixed_scenario():
    # 1 (odd, pos) -> 1
    # 2 (even, pos) -> ignore
    # 3 (odd, pos) -> 9
    # -5 (odd, neg) -> ignore
    # 4.0 (float) -> ignore
    # 7 (odd, pos) -> 49
    # Sum: 1 + 9 + 49 = 59
    assert double_the_difference([1, 2, 3, -5, 4.0, 7]) == 59

def test_type_stability():
    # Ensure the function handles tuple input
    assert double_the_difference((1, 3)) == 10

@pytest.mark.parametrize("input_lst, expected", [
    ([1, 1, 1], 3),
    ([2, 2, 2], 0),
    ([-1, -1, -1], 0),
    ([0, 0, 0], 0),
    ([1.1, 2.2, 3.3], 0),
    ([7], 49),
    ([11], 121),
    ([1, 2, 3, 4, 5], 35),
    ([0, -1, 2, -3, 5], 25),
])
def test_parametrized_cases(input_lst, expected):
    assert double_the_difference(input_lst) == expected