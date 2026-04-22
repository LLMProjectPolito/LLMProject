


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

    def test_single_element(self):
        assert sum_squares([5]) == 5

    def test_multiple_elements_no_modifications(self):
        assert sum_squares([1, 2, 4, 5]) == 12

    def test_multiple_elements_squares(self):
        assert sum_squares([1, 2, 3]) == 1 + 4 + 9

    def test_multiple_elements_cubes(self):
        assert sum_squares([1, 2, 4]) == 1 + 2 + 64

    def test_multiple_elements_squares_and_cubes(self):
        assert sum_squares([1, 2, 3, 4]) == 1 + 4 + 27 + 64

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_positive_and_negative(self):
        assert sum_squares([1, -2, 3, -4]) == 1 + 4 + 27 + (-64)

    def test_zero_in_list(self):
        assert sum_squares([0, 1, 2, 3]) == 0 + 1 + 4 + 9

    def test_large_numbers(self):
        assert sum_squares([100, 200, 300]) == 10000 + 40000 + 90000

    def test_all_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 16 + 25 + 36

    def test_all_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 8]) == 1 + 4 + 9 + 64 + 25 + 36
    
    def test_complex_case(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 4 + 9 + 64 + 25 + 36 + 49 + 512 + 81 + 100 + 121 + 144