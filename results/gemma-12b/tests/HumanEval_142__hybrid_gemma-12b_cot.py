


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
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total += num**3
        else:
            total += num
    return total

class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_basic_list(self):
        assert sum_squares([1, 2, 3]) == 6

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_positive_negative(self):
        assert sum_squares([1, -2, 3, -4, 5]) == 33

    def test_multiples_of_3(self):
        assert sum_squares([3, 6, 9, 1, 2, 4]) == 126

    def test_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 100

    def test_multiples_of_both_3_and_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 210

    def test_large_numbers(self):
        assert sum_squares([10, 20, 30, 40]) == 10000

    def test_zeroes(self):
        assert sum_squares([0, 0, 0, 0, 0]) == 0

    def test_zero_in_list(self):
        assert sum_squares([0, 1, 2, 3, 4]) == 0 + 1 + 2 + 9 + 4

    def test_list_with_zeros_at_indices_3_and_4(self):
        assert sum_squares([1, 2, 3, 0, 0, 6]) == 1 + 2 + 9 + 0 + 0 + 36

    def test_list_with_duplicate_numbers(self):
        assert sum_squares([2, 2, 2, 2, 2]) == 4 + 4 + 8 + 8 + 2

    def test_single_element_list_multiple_of_3(self):
        assert sum_squares([3]) == 9

    def test_single_element_list_multiple_of_4(self):
        assert sum_squares([4]) == 64

    def test_single_element_list_not_multiple_of_3_or_4(self):
        assert sum_squares([5]) == 5

    def test_list_with_floats(self):
        with pytest.raises(TypeError):
            sum_squares([1.0, 2.0, 3.0])

    def test_list_with_strings(self):
        with pytest.raises(TypeError):
            sum_squares(["a", "b", "c"])