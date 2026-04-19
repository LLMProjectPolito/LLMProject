
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

@pytest.mark.parametrize("lst, expected", [
    ([1, 3, 2, 0], 10),                 # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),                   # Negatives and evens ignored
    ([9, -2], 81),                      # 9^2 = 81
    ([0], 0),                           # Even ignored
    ([], 0),                            # Empty list
    ([1, 5, 7], 75),                    # All odd: 1 + 25 + 49 = 75
    ([2, 4, 6], 0),                     # All even
    ([-1, -3, -5], 0),                  # All negative odd
    ([1.5, 3.0, 2.1], 0),               # Non-integers (floats) ignored
    (["1", "3", None], 0),              # Non-integers (strings/None) ignored
    ([1, 2, 3.0, 5], 26),               # Mixed types: 1^2 + 5^2 = 26
    ([11], 121),                        # Single odd
    ([101, 103], 101**2 + 103**2),      # Larger odds
    ([1, -1, 2, 3.5, 'a', None, 7], 50),# Mixed: 1^2 + 7^2 = 50
    ([None, [], {}], 0),                 # Non-integer elements
])
def test_double_the_difference_parametrized(lst, expected):
    assert double_the_difference(lst) == expected

def test_double_the_difference_complex_mix():
    """Test a comprehensive mix of all invalid and valid inputs."""
    # Odd positive: 1, 7, 11 -> 1^2 + 7^2 + 11^2 = 1 + 49 + 121 = 171
    # Even positive: 2, 10 -> ignore
    # Negative: -1, -7 -> ignore
    # Non-int: 3.0, "5", None -> ignore
    input_list = [1, 2, -1, 3.0, 7, "5", 10, -7, None, 11]
    assert double_the_difference(input_list) == 171

def test_double_the_difference_floats_as_ints():
    """Ensure that floats (even those representing whole numbers) are ignored."""
    assert double_the_difference([3.0, 5.0]) == 0