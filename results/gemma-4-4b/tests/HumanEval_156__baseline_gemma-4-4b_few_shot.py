
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    i = 1
    result = ''
    while number > 0:
        if i in roman_map and i <= number:
            result += roman_map[i]
            number -= i
        elif i + 1 in roman_map and i <= number and i + 1 <= number:
            if i == 1 and i + 1 == 5:
                result += 'v'
                number -= 5
            elif i == 10 and i + 1 == 50:
                result += 'l'
                number -= 50
            elif i == 100 and i + 1 == 500:
                result += 'c'
                number -= 500
            elif i == 1000 and i + 1 == 1000:
                result += 'm'
                number -= 1000
            else:
                result += roman_map[i+1]
                number -= (i+1)
        else:
            i += 1
    return result


def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(2023) == 'mmxxiii'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(18) == 'xviii'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(3999) == 'mmmmmcmxciii'