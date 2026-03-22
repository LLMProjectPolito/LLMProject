def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.  Negative numbers
    are treated as distinct values and sorted based on their digit sum
    and original index.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    >>> order_by_points([1, 1, 2]) == [1, 1, 2]
    """
    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    # Store original indices
    original_indices = list(range(len(nums)))

    # Sort based on digit sum and original index
    return sorted(nums, key=lambda x: (sum_digits(x), original_indices[nums.index(x)]))


### Problem:
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """

### Tests (Pytest):