import pytest

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

    i = 12
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result


def test_int_to_mini_roman_1():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_2():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_4():
    assert int_to_mini_roman(3) == 'iii'

def test_int_to_mini_roman_5():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_6():
    assert int_to_mini_roman(5) == 'v'

def test_int_to_mini_roman_7():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_8():
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_9():
    assert int_to_mini_roman(40) == 'xl'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(50) == 'l'

def test_int_to_mini_roman_11():
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_12():
    assert int_to_mini_roman(100) == 'c'

def test_int_to_mini_roman_13():
    assert int_to_mini_roman(400) == 'cd'

def test_int_to_mini_roman_14():
    assert int_to_mini_roman(500) == 'd'

def test_int_to_mini_roman_15():
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_16():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_17():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_18():
    assert int_to_mini_roman(2) == 'ii'

def test_int_to_mini_roman_19():
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_20():
    assert int_to_mini_roman(20) == 'xx'

def test_int_to_mini_roman_21():
    assert int_to_mini_roman(39) == 'xxxix'

def test_int_to_mini_roman_22():
    assert int_to_mini_roman(49) == 'xlii'

def test_int_to_mini_roman_23():
    assert int_to_mini_roman(59) == 'lviii'

def test_int_to_mini_roman_24():
    assert int_to_mini_roman(69) == 'lxix'

def test_int_to_mini_roman_25():
    assert int_to_mini_roman(79) == 'lxxix'

def test_int_to_mini_roman_26():
    assert int_to_mini_roman(89) == 'lxxxix'

def test_int_to_mini_roman_27():
    assert int_to_mini_roman(99) == 'xcix'

def test_int_to_mini_roman_28():
    assert int_to_mini_roman(14) == 'xiv'

def test_int_to_mini_roman_29():
    assert int_to_mini_roman(16) == 'xvi'

def test_int_to_mini_roman_30():
    assert int_to_mini_roman(24) == 'xxiv'

def test_int_to_mini_roman_31():
    assert int_to_mini_roman(6) == 'vi'

def test_int_to_mini_roman_32():
    assert int_to_mini_roman(7) == 'vii'

def test_int_to_mini_roman_33():
    assert int_to_mini_roman(8) == 'viii'

def test_int_to_mini_roman_34():
    assert int_to_mini_roman(11) == 'xi'

def test_int_to_mini_roman_35():
    assert int_to_mini_roman(12) == 'xii'

def test_int_to_mini_roman_36():
    assert int_to_mini_roman(13) == 'xiii'

def test_int_to_mini_roman_37():
    assert int_to_mini_roman(14) == 'xiv'

def test_int_to_mini_roman_38():
    assert int_to_mini_roman(15) == 'xv'

def test_int_to_mini_roman_39():
    assert int_to_mini_roman(16) == 'xvi'

def test_int_to_mini_roman_40():
    assert int_to_mini_roman(17) == 'xvii'

def test_int_to_mini_roman_41():
    assert int_to_mini_roman(18) == 'xviii'

def test_int_to_mini_roman_42():
    assert int_to_mini_roman(19) == 'xix'