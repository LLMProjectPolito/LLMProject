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
        if num > 10 and (num % 10 == 1 or num % 10 == 3 or num % 10 == 5 or num % 10 == 7 or num % 10 == 9):
            if num % 10 == 1:
                if num > 0:
                    count += 1
            elif num % 10 == 3:
                if num > 0:
                    count += 1
            elif num % 10 == 5:
                if num > 0:
                    count += 1
            elif num % 10 == 7:
                if num > 0:
                    count += 1
            elif num % 10 == 9:
                if num > 0:
                    count += 1
    return count

def test_specialFilter_example1():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([11, 22, 33, 44, 55]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([1, 3, 5, 7, 9]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 5
    assert specialFilter([]) == 0
    assert specialFilter([1]) == 0
    assert specialFilter([2]) == 0
    assert specialFilter([11]) == 5
    assert specialFilter([1, 11]) == 1
    assert specialFilter([1, 3, 5, 7, 9]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 5
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 5
    print("All test cases passed")