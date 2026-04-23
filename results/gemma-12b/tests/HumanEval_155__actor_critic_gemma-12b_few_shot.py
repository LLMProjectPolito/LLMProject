
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def even_odd_count(num):
    """Given an integer, return a tuple containing the count of even and odd digits in its absolute value.
    The function handles negative numbers by taking the absolute value before processing.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
        even_odd_count(0) ==> (1, 0)
        even_odd_count(2468) ==> (4, 0)
        even_odd_count(13579) ==> (0, 5)
    """
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))  # Handle negative numbers

    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)


### Tests (Pytest):
def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_mixed_digits():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_negative_number():
    assert even_odd_count(-1234) == (2, 2)

def test_even_odd_count_another_larger_number():
    assert even_odd_count(987654321) == (4, 6)

def test_even_odd_count_large_negative_number():
    assert even_odd_count(-12345678901234567890) == (10, 10)

def test_even_odd_count_large_number():
    # Test with a number containing 100 digits.  This helps check for string conversion and iteration performance.
    large_number = "1" * 100
    assert even_odd_count(int(large_number)) == (0, 100)

# The overflow check is difficult to implement directly in pytest without
# resorting to mocking or external libraries.  It's better handled in
# production code with appropriate data type considerations.  This test
# serves as a reminder to consider overflow in production.
# def test_even_odd_count_overflow():
#     # This test is commented out because it's difficult to reliably test
#     # overflow in Python without external libraries or mocking.
#     # The intention is to highlight the need to consider overflow in
#     # production code when dealing with extremely large numbers.
#     pass