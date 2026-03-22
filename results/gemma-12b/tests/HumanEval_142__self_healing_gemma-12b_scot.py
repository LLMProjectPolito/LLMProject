import pytest

def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    sum_of_squares = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            sum_of_squares += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            sum_of_squares += num ** 3
        else:
            sum_of_squares += num
    return sum_of_squares


def test_empty_list():
    """Test case for an empty list."""
    assert sum_squares([]) == 0

def test_list_with_no_multiples():
    """Test case for a list with no multiples of 3 or 4."""
    assert sum_squares([1, 2, 4, 5]) == 1 + 2 + 4 + 5 == 12

def test_list_with_multiples_of_3():
    """Test case for a list with multiples of 3."""
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 4 + 5 + 36 == 59

def test_list_with_multiples_of_4():
    """Test case for a list with multiples of 4."""
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512 == 590

def test_list_with_multiples_of_3_and_4():
    """Test case for a list with multiples of both 3 and 4."""
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 9 + 10 + 11 + 144 == 700

def test_list_with_negative_numbers():
    """Test case for a list with negative numbers."""
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + (-125) + 4 + 1 + (-125) == -244

def test_list_with_mixed_positive_and_negative_numbers():
    """Test case for a list with mixed positive and negative numbers."""
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + (-125) + 4 + 1 + (-125) == -244

def test_list_with_zeros():
    """Test case for a list with zeros."""
    assert sum_squares([0, 1, 2, 3, 4]) == 0 + 1 + 4 + 9 + 16 == 30

def test_example_1():
    """Test case from the problem description."""
    assert sum_squares([1, 2, 3]) == 1 + 4 + 9 == 14

def test_example_2():
    """Test case from the problem description."""
    assert sum_squares([]) == 0

def test_example_3():
    """Test case from the problem description."""
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + (-125) + 4 + 1 + (-125) == -244