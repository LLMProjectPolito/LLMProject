
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xix', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if 1000 <= number <= 333:
        return int_to_mini_roman_helper(number, 333)
    elif 334 <= number <= 500:
        return int_to_mini_roman_helper(number, 500)
    elif 501 <= number <= 666:
        return int_to_mini_roman_helper(number, 666)
    elif 667 <= number <= 833:
        return int_to_mini_roman_helper(number, 833)
    elif 834 <= number <= 1000:
        return int_to_mini_roman_helper(number, 1000)
    else:
        return int_to_mini_roman_helper(number, 1000)


def int_to_mini_roman_helper(number, limit):
    result = ""
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symbols = ['m', 'cm', 'd', 'cd', 'c', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    i = 0
    while number > 0:
        if number >= roman_values[i]:
            result += roman_symbols[i]
            number -= roman_values[i]
        else:
            i += 1
    return result