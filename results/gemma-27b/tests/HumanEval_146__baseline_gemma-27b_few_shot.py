
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

def test_special_filter_empty():
    assert specialFilter([]) == 0

def test_special_filter_no_match():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_special_filter_single_match():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_multiple_matches():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_special_filter_mixed_numbers():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99, 101]) == 5

def test_special_filter_large_numbers():
    assert specialFilter([111, 123, 135, 147, 159, 171, 191]) == 0

def test_special_filter_edge_case_10():
    assert specialFilter([10]) == 0

def test_special_filter_edge_case_11():
    assert specialFilter([11]) == 1

def test_special_filter_edge_case_99():
    assert specialFilter([99]) == 1