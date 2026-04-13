


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
from your_module import sum_squares  # Replace your_module

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == -11

def test_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 91

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 691

def test_multiples_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]) == 893

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40]) == 168900

def test_zeroes():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_single_element_neither():
    assert sum_squares([5]) == 5

def test_list_with_floats_raises_typeerror():
    with pytest.raises(TypeError):
        sum_squares([1.0, 2.0, 3.0])

def test_list_with_strings_raises_typeerror():
    with pytest.raises(TypeError):
        sum_squares(["a", "b", "c"])

class TestSumSquares:
    """
    Test suite for the sum_squares function.
    """

    def test_list_with_multiples_of_3(self):
        """Test with multiples of 3."""
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 91

    def test_list_with_multiples_of_4(self):
        """Test with multiples of 4."""
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 691

    def test_list_with_multiples_of_both_3_and_4(self):
        """Test with multiples of both 3 and 4 (i.e., multiples of 12)."""
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 893

    def test_list_with_negative_numbers(self):
        """Test with negative numbers."""
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_list_with_mixed_positive_and_negative(self):
        """Test with a mix of positive and negative numbers."""
        assert sum_squares([-1, 2, -3, 4, -5, 6]) == -11

    def test_list_with_zeros(self):
        """Test with zeros in the list."""
        assert sum_squares([0, 1, 2, 3, 4, 5]) == 91

    def test_large_list(self):
        """Test with a larger list to check performance and correctness."""
        large_list = list(range(1, 21))
        expected_sum = 0
        for i, num in enumerate(large_list):
            if i % 3 == 0:
                expected_sum += num**2
            elif i % 4 == 0:
                expected_sum += num**3
            else:
                expected_sum += num
        assert sum_squares(large_list) == expected_sum

    def test_list_with_duplicates(self):
        """Test with duplicate numbers in the list."""
        assert sum_squares([1, 1, 1, 1, 1]) == 5

    def test_list_with_floats(self):
        """Test with floats in the list. Should still work as integers."""
        assert sum_squares([1.0, 2.0, 3.0]) == 14

    def test_list_with_large_numbers(self):
        """Test with large numbers to ensure no overflow issues."""
        assert sum_squares([1000, 2000, 3000]) == 16000000

    def test_edge_case_multiple_of_12(self):
        """Test an edge case where an index is a multiple of both 3 and 4."""
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 893