
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
        try:
            if isinstance(num, (int, float)) and num > 10:
                num_str = str(num)
                if num_str[0] in '13579' and num_str[-1] in '13579':
                    count += 1
            elif isinstance(num, (int, float)) and num <= 10:
                # Consider single-digit numbers if they meet criteria
                num_str = str(num)
                if len(num_str) > 0 and num_str[0] in '13579' and num_str[-1] in '13579':
                    count += 1
        except (TypeError, IndexError):
            # Handle non-numeric or invalid input gracefully
            pass  # Or log the error, raise a custom exception, etc.
    return count