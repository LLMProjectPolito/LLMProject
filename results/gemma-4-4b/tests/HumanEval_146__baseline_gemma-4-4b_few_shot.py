
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([2, 4, 6, 8]) == 0

def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple_matches():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_mixed():
    assert specialFilter([11, 22, 33, 44, 55]) == 3

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33, -55]) == 3

def test_specialFilter_large_numbers():
    assert specialFilter([101, 123, 456, 789]) == 1

def test_specialFilter_zero():
    assert specialFilter([1, 3, 5, 7, 9, 0]) == 5