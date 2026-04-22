


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
            total += num * num
        elif i % 4 == 0 and i % 3 != 0:
            total += num * num * num
        else:
            total += num
    return total

class TestSumSquares(pytest.PythonTest):
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_single_element(self):
        assert sum_squares([1]) == 1

    def test_example_1(self):
        assert sum_squares([1, 2, 3]) == 6

    def test_example_2(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_list(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81

    def test_all_zeros(self):
        assert sum_squares([0, 0, 0]) == 0

    def test_negative_numbers(self):
        assert sum_squares([-1, -2, -3]) == 14