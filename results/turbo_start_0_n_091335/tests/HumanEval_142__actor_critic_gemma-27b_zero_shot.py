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
    for i, num in enumerate(lst):
        if i % 3 == 0:
            new_lst.append(num**2)
        elif i % 4 == 0 and i % 3 != 0:
            new_lst.append(num**3)
        else:
            new_lst.append(num)
    return sum(new_lst)

def test_empty_list():
    assert sum_squares([]) == 0

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == -82

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_list_with_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 1000000

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == -233

def test_single_element_list():
    assert sum_squares([5]) == 5

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_long_list():
    lst = list(range(20))
    assert sum_squares(lst) == 4490

def test_no_multiples_of_3_or_4():
    assert sum_squares([1, 2, 5, 7]) == 15

def test_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 605

def test_large_negative_numbers():
    assert sum_squares([-1000, -2000, -3000]) == 14000000

def test_mixed_large_positive_and_negative():
    assert sum_squares([1000, -2000, 3000, -4000]) == -8000000