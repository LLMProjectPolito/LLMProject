
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

```python
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
        num_str = str(abs(num))
        if len(num_str) > 0 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
            count += 1
    return count

def test_empty_array():
    assert specialFilter([]) == 0

def test_single_element():
    assert specialFilter([15]) == 1

def test_positive_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 13]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 15]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 17]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 21]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 23]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 25]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 27]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 29]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 31]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 33]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 35]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 37]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 39]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 41]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 43]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 45]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 47]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 49]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 51]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 53]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 55]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 57]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 59]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 61]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 63]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 65]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 67]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 69]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 71]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 73]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 75]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 77]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 79]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 81]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 83]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 85]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 87]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7