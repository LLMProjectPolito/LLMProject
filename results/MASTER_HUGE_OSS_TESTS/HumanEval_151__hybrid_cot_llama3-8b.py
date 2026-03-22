import pytest
from your_module import double_the_difference  # Import the function

def test_empty_list():
    assert double_the_difference([]) == 0

def test_list_with_only_even_numbers():
    assert double_the_difference([2, 4, 6, 0]) == 0

def test_list_with_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == (1**2 + 3**2 + 5**2)

def test_list_with_mix_of_odd_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4]) == (1**2 + 3**2)

def test_list_with_negative_odd_numbers():
    assert double_the_difference([-1, 3, -5]) == (3**2)

def test_list_with_non_integer_values():
    assert double_the_difference([1.5, 2, 3]) == 0

def test_list_with_single_number():
    assert double_the_difference([5]) == 5**2
    assert double_the_difference([4]) == 0
    assert double_the_difference([-4]) == 0

def test_list_with_single_odd_number():
    assert double_the_difference([5]) == 5**2

def test_list_with_single_even_number():
    assert double_the_difference([4]) == 0

def test_list_with_single_non_integer_value():
    assert double_the_difference([3.5]) == 0

def test_positive_integers():
    # Test a list with multiple odd numbers
    assert double_the_difference([1, 3, 2, 0]) == 10
    
    # Test a list with a single odd number
    assert double_the_difference([9]) == 81
    
    # Test a list with no odd numbers
    assert double_the_difference([2, 4, 0]) == 0

def test_negative_integers():
    # Test a list with a single negative odd number
    assert double_the_difference([-1]) == 1
    
    # Test a list with multiple negative odd numbers
    assert double_the_difference([-1, -3, -2, 0]) == 1 + 9 + 0 + 0
    
    # Test a list with no negative odd numbers
    assert double_the_difference([-2, 0]) == 0

def test_mixed_types():
    # Test a list with a mix of integers and non-integers
    assert double_the_difference([1, 'a', 0]) == 1

def test_zero():
    # Test a list with a single zero
    assert double_the_difference([0]) == 0
    
    # Test a list with multiple zeros
    assert double_the_difference([0, 0, 0]) == 0
    
    # Test a list with no zeros
    assert double_the_difference([1, 3, 2]) == 1**2 + 3**2 + 2**2

def test_non_integer_values():
    # Test a list with a single non-integer value
    assert double_the_difference([1, 3.4, 0]) == 1**2 + 3.4**2 + 0**2
    
    # Test a list with multiple non-integer values
    assert double_the_difference([1, 3.4, 0.9, 0]) == 1**2 + 3.4**2 + 0.9**2 + 0**2