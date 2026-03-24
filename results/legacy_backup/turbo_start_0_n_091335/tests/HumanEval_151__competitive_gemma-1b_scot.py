def double_the_difference(lst):
    if not lst:
        return 0
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares