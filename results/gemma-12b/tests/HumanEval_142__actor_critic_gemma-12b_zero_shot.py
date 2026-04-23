


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
    sum_val = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            sum_val += num**2
        elif i % 4 == 0 and i % 3 != 0:
            sum_val += num**3
        else:
            sum_val += num
    return sum_val

class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_basic_list(self):
        assert sum_squares([1, 2, 3]) == 6

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_numbers(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 140

    def test_index_zero_is_multiple_of_3(self):
        assert sum_squares([3, 1, 2]) == 12

    def test_multiples_of_12(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16]) == 216

    def test_large_numbers(self):
        assert sum_squares([1000, 2000, 3000, 4000]) == 3000000

    def test_zero_in_list(self):
        assert sum_squares([0, 1, 2, 3, 4]) == 6

    def test_list_with_zeros_and_negatives(self):
        assert sum_squares([-1, 0, 2, -3, 4]) == -4

    def test_single_element_multiple_of_3(self):
        assert sum_squares([3]) == 9

    def test_single_element_multiple_of_4(self):
        assert sum_squares([4]) == 64

    def test_single_element_not_multiple_of_3_or_4(self):
        assert sum_squares([5]) == 5

    def test_floating_point_numbers(self):
        with pytest.raises(TypeError):
            sum_squares([1.0, 2.0, 3.0])

    def test_string_in_list(self):
        with pytest.raises(TypeError):
            sum_squares([1, 2, "a"])