
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

def test_docstring_examples():
    """Verify the examples provided in the function docstring."""
    assert double_the_difference([1, 3, 2, 0]) == 10  # 1^2 + 3^2 = 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81       # 9^2 = 81
    assert double_the_difference([0]) == 0

def test_empty_and_null_cases():
    """Test empty lists or lists that should result in 0."""
    assert double_the_difference([]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 0  # All even
    assert double_the_difference([-1, -3, -5]) == 0  # All negative odd

def test_filtering_logic():
    """Ensure only positive odd integers are squared and summed."""
    # Only positive odd: 1, 5 -> 1 + 25 = 26
    # Ignore: 2 (even), -1 (negative), -3 (negative), 0 (even)
    assert double_the_difference([1, 2, -1, 5, -3, 0]) == 26

def test_type_validation():
    """Ensure non-integer types are ignored without raising exceptions."""
    # 3 is the only positive odd integer. 3^2 = 9.
    # Ignore: 3.1 (float), "3" (string), None, [1] (list)
    assert double_the_difference([3, 3.1, "3", None, [1], 2]) == 9
    
    # Test with only invalid types
    assert double_the_difference([1.5, 2.7, "odd", None]) == 0

def test_large_values():
    """Test with larger odd integers to ensure mathematical correctness."""
    # 101^2 = 10201; 201^2 = 40401. Sum = 50602
    assert double_the_difference([101, 201]) == 50602

@pytest.mark.parametrize("input_list, expected", [
    ([1, 1, 1], 3),              # Multiple of the same odd number
    ([1, 3, 5], 1 + 9 + 25),     # Sequence of odd numbers
    ([10, 20, 30], 0),           # Sequence of even numbers
    ([-1, -3, -5], 0),           # Sequence of negative odd numbers
    ([1, "a", 3, "b", 5], 35),   # Mixed alphanumeric
])
def test_parametrized_cases(input_list, expected):
    """Run a variety of scenarios using parametrization."""
    assert double_the_difference(input_list) == expected