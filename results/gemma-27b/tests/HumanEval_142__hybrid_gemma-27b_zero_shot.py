


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
    new_lst = []
    for i in range(len(lst)):
        if i % 3 == 0:
            new_lst.append(lst[i]**2)
        elif i % 4 == 0 and i % 3 != 0:
            new_lst.append(lst[i]**3)
        else:
            new_lst.append(lst[i])
    return sum(new_lst)

class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_example_1(self):
        assert sum_squares([1, 2, 3]) == 6

    def test_example_2(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_list_with_only_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

    def test_list_with_only_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

    def test_list_with_multiples_of_3_and_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

    def test_list_with_negative_numbers(self):
        assert sum_squares([-1, -2, -3, -4, -5, -6]) == 1 + 4 + 9 + (-64) + 25 + 36

    def test_list_with_zeroes(self):
        assert sum_squares([0, 0, 0, 0, 0, 0]) == 0

    def test_large_numbers(self):
        assert sum_squares([100, 200, 300, 400, 500]) == 10000 + 200 + 90000 + 64000000 + 500

    def test_mixed_positive_and_negative(self):
        assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + 4 + 9 + (-64) + 5 + 36

    def test_single_element_list(self):
        assert sum_squares([5]) == 5

    def test_single_element_multiple_of_3(self):
        assert sum_squares([3]) == 9

    def test_single_element_multiple_of_4(self):
        assert sum_squares([4]) == 64

    def test_long_list(self):
        lst = list(range(20))
        expected_sum = 0
        for i in range(20):
            if i % 3 == 0:
                expected_sum += i**2
            elif i % 4 == 0 and i % 3 != 0:
                expected_sum += i**3
            else:
                expected_sum += i
        assert sum_squares(lst) == expected_sum

    def test_list_with_mixed_multiples(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

    def test_list_with_negative_numbers_2(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126