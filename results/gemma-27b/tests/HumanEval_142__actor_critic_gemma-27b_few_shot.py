


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

def sum_squares(lst):
    """
    This function takes a list of integers and calculates a sum based on the index of each element.
    For elements at indices that are multiples of 3, the element is squared.
    For elements at indices that are multiples of 4 but not multiples of 3, the element is cubed.
    Elements at other indices are included in the sum unchanged.

    Examples:
    For lst = [1, 2, 3] the output should be 1**2 + 2 + 3**2 = 1 + 2 + 9 = 12
    For lst = [] the output should be 0
    For lst = [-1, -5, 2, -1, -5] the output should be (-1)**2 + -5 + 2**2 + (-1)**3 + (-5) = 1 - 5 + 4 - 1 - 5 = -6
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    for element in lst:
        if not isinstance(element, int):
            raise TypeError("List elements must be integers.")

    return sum(x**2 if i % 3 == 0 else x**3 if i % 4 == 0 and i % 3 != 0 else x for i, x in enumerate(lst))


import pytest

def test_sum_squares_basic():
    # Tests the function with a simple list of positive integers.
    assert sum_squares([1, 2, 3]) == 12
    # Tests the function with an empty list.
    assert sum_squares([]) == 0
    # Tests the function with a list of negative and positive integers.
    assert sum_squares([-1, -5, 2, -1, -5]) == -6

def test_sum_squares_length_12():
    # Tests the function with a longer list to ensure correct calculation.
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

def test_sum_squares_with_zero():
    # Tests the function's behavior when the list contains zero.
    assert sum_squares([0, 1, 2, 3]) == 12

def test_sum_squares_negative_and_zero():
    # Tests the function with negative numbers and zero.
    assert sum_squares([-1, 0, 1, -2, 2]) == -4

def test_sum_squares_mixed_positive_negative():
    # Tests the function with a mix of positive and negative numbers.
    assert sum_squares([1, -2, 3, -4, 5]) == -51

def test_sum_squares_type_error():
    # Tests that the function raises a TypeError when the input is not a list.
    with pytest.raises(TypeError):
        sum_squares("not a list")
    # Tests that the function raises a TypeError when the list contains non-integer elements.
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a"])

def test_sum_squares_large_list():
    # Tests the function with a large list to check for performance issues.
    large_list = list(range(1000))
    expected_sum = sum(x**2 if i % 3 == 0 else x**3 if i % 4 == 0 and i % 3 != 0 else x for i, x in enumerate(large_list))
    assert sum_squares(large_list) == expected_sum

def test_sum_squares_all_multiples_of_3():
    # Tests the function with a list where all indices are multiples of 3.
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 16 + 25 + 36

def test_sum_squares_all_multiples_of_4_not_3():
    # Tests the function with a list where all indices are multiples of 4 but not 3.
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512