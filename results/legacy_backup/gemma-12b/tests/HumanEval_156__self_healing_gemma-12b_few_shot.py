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
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = len(integers) - 1
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_teen():
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(13) == 'xiii'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(17) == 'xvii'
    assert int_to_mini_roman(18) == 'xviii'
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_twenties():
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(21) == 'xxi'
    assert int_to_mini_roman(22) == 'xxii'
    assert int_to_mini_roman(23) == 'xxiii'
    assert int_to_mini_roman(24) == 'xxiv'
    assert int_to_mini_roman(25) == 'xxv'
    assert int_to_mini_roman(26) == 'xxvi'
    assert int_to_mini_roman(27) == 'xxvii'
    assert int_to_mini_roman(28) == 'xxviii'
    assert int_to_mini_roman(29) == 'xxix'

def test_int_to_mini_roman_larger():
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(41) == 'xli'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(999) == 'cmxciii'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'