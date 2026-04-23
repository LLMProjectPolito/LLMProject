
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

```python
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

def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 3, 5, 7, 9]) == 0
    assert specialFilter([11, 33, 55, 77, 99]) == 5
    assert specialFilter([-15, -33, -55, -77, -99]) == 5
    assert specialFilter([15, -73, 15, -15]) == 2
    assert specialFilter([10, 11, 13]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 2
    assert specialFilter([12, 14, 16, 18]) == 0
    assert specialFilter([15, 17, 19]) == 3
    assert specialFilter([-15, -17, -19]) == 3
    assert specialFilter([100, 101, 103]) == 2
    assert specialFilter([100, 102, 104]) == 0
    assert specialFilter([111, 113, 115]) == 3
    assert specialFilter([-111, -113, -115]) == 3
    assert specialFilter([15, 15, 15]) == 3
    assert specialFilter([-15, -15, -15]) == 3
    assert specialFilter([15, 15, 14]) == 2
    assert specialFilter([15, 14, 15]) == 2
    assert specialFilter([15, 14, 14]) == 0
    assert specialFilter([15, 15, 15, 15]) == 4
    assert specialFilter([15, 15, 15, 14]) == 3
    assert specialFilter([15, 14, 15, 14]) == 2
    assert specialFilter([15, 14, 14, 15]) == 2
    assert specialFilter([15, 15, 14, 15]) == 3
    assert specialFilter([15, 14, 15, 15]) == 3
    assert specialFilter([15, 15, 15, 15, 15]) == 5
    assert specialFilter([15, 15, 15, 14, 15]) == 4
    assert specialFilter([15, 14, 15, 15, 15]) == 4
    assert specialFilter([15, 15, 14, 15, 14]) == 3
    assert specialFilter([15, 15, 15, 14, 14]) == 3
    assert specialFilter([15, 15, 15, 15, 14]) == 4
    assert specialFilter([15, 15, 15, 15, 15]) == 5
    assert specialFilter([15, 15, 15, 15, 15, 15]) == 6
    assert specialFilter([15, 15, 15, 15, 15, 14]) == 5
    assert specialFilter([15, 15, 15, 15, 14, 15]) == 5
    assert specialFilter([15, 15, 15, 15, 14, 14]) == 4
    assert specialFilter([15, 15, 15, 15, 15, 15]) == 6
    assert specialFilter([15, 15, 15, 15, 15, 15, 15]) == 7
    assert specialFilter([15, 15, 15, 15, 15, 15, 14]) == 6
    assert specialFilter([15, 15, 15, 15, 15, 14, 15]) == 6
    assert specialFilter([15, 15, 15, 15, 15, 14, 14]) == 5
    assert specialFilter([15, 15, 15, 15, 15, 15, 15]) == 7
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15]) == 8
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 14]) == 7
    assert specialFilter([15, 15, 15, 15, 15, 15, 14, 15]) == 7
    assert specialFilter([15, 15, 15, 15, 15, 15, 14, 14]) == 6
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15]) == 8
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 15]) == 9
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 14]) == 8
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 14, 15]) == 8
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 14, 14]) == 7
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 15]) == 9
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 10
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 15, 14]) == 9
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 14, 15]) == 9
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 14, 14]) == 8
    assert specialFilter([15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 10
    assert specialFilter([15, 15