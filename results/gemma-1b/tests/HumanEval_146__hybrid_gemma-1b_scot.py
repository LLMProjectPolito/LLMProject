
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

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
        s = str(num)
        if len(s) == 1:
            if int(s[0]) % 2 != 0 and int(s[-1]) % 2 != 0:
                count += 1
        else:
            first_digit = int(s[0])
            last_digit = int(s[-1])
            if first_digit > 10 and last_digit % 2 != 0:
                count += 1
    return count

def test_specialFilter_example1():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([11, 22, 33, 44, 55]) == 0
    assert specialFilter([1, 3, 5, 7, 9]) == 5
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19, 21]) == 1
    print("All test cases passed")