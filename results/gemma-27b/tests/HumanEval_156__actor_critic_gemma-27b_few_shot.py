
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
    >>> int_to_mini_roman(1) == 'i'
    >>> int_to_mini_roman(1000) == 'm'
    >>> int_to_mini_roman(3) == 'iii'
    >>> int_to_mini_roman(7) == 'vii'
    >>> int_to_mini_roman(8) == 'viii'
    >>> int_to_mini_roman(39) == 'xxxix'
    >>> int_to_mini_roman(41) == 'xli'
    >>> int_to_mini_roman(89) == 'lxxxix'
    >>> int_to_mini_roman(91) == 'xci'
    >>> int_to_mini_roman(399) == 'cccxcix'
    >>> int_to_mini_roman(401) == 'cdi'
    >>> int_to_mini_roman(899) == 'dcccxcix'
    >>> int_to_mini_roman(901) == 'cmi'
    >>> int_to_mini_roman(0)
    ValueError: Number must be between 1 and 1000 inclusive.
    >>> int_to_mini_roman(1001)
    ValueError: Number must be between 1 and 1000 inclusive.
    """
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}

    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000 inclusive.")

    result = ""
    for value, numeral in sorted(roman_map.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result.lower()