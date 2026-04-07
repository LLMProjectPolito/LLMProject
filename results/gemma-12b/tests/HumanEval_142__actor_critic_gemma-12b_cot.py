


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
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            sum += lst[i]**3
        else:
            sum += lst[i]
    return sum

class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_basic_list(self):
        assert sum_squares([1, 2, 3]) == 6

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_mixed_positive_negative(self):
        assert sum_squares([1, -2, 3, -4, 5]) == 15

    def test_multiples_of_3(self):
        assert sum_squares([3, 6, 9, 1, 2]) == 129

    def test_multiples_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 193

    def test_multiples_of_both_3_and_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1982

    def test_large_numbers(self):
        assert sum_squares([100, 200, 300]) == 8090000

    def test_zeroes(self):
        assert sum_squares([0, 0, 0, 0, 0]) == 0

    def test_single_element(self):
        assert sum_squares([5]) == 5

    def test_single_element_multiple_of_3(self):
        assert sum_squares([3]) == 9

    def test_single_element_multiple_of_4(self):
        assert sum_squares([4]) == 64

    def test_non_integer_input(self):
        with pytest.raises(TypeError) as excinfo:
            sum_squares([1, 2, "a"])
            assert "Input list must contain only integers." in str(excinfo.value)

    def test_mixed_data_types(self):
        with pytest.raises(TypeError) as excinfo:
            sum_squares([1, 2, 3.14, "a"])
            assert "Input list must contain only integers." in str(excinfo.value)

    def test_negative_multiples(self):
        assert sum_squares([-3, -4, 1]) == 1

    def test_large_list(self):
        large_list = list(range(1, 101))
        expected_sum = 0
        for i in range(len(large_list)):
            if i % 3 == 0:
                expected_sum += large_list[i]**2
            elif i % 4 == 0 and i % 3 != 0:
                expected_sum += large_list[i]**3
            else:
                expected_sum += large_list[i]
        assert sum_squares(large_list) == expected_sum