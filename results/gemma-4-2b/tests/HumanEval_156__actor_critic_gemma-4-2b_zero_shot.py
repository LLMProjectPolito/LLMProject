
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

```python
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xix', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if 1000 <= number <= 333:
        return ""
    roman_string = ''
    num_str = str(number)
    for i in range(len(num_str)):
        if num_str[i] == '1':
            if i + 1 < len(num_str) and num_str[i+1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
                roman_string += 'i'
                i += 1
            else:
                roman_string += 'i'
        elif num_str[i] == '2':
            roman_string += 'ii'
        elif num_str[i] == '3':
            roman_string += 'iii'
        elif num_str[i] == '4':
            roman_string += 'iv'
        elif num_str[i] == '5':
            roman_string += 'v'
        elif num_str[i] == '6':
            roman_string += 'vi'
        elif num_str[i] == '7':
            roman_string += 'vii'
        elif num_str[i] == '8':
            roman_string += 'viii'
        elif num_str[i] == '9':
            roman_string += 'ix'
        else:
            roman_string += 'x'
    return roman_string


def test_int_to_mini_roman():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(58) == 'lvviii'
    assert int_to_mini_roman(60) == 'si'
    assert int_to_mini_roman(64) == 'lvxiv'
    assert int_to_mini_roman(69) == 'lvix'
    assert int_to_mini_roman(70) == 'lxx'
    assert int_to_mini_roman(73) == 'lxxiii'
    assert int_to_mini_roman(80) == 'lviii'
    assert int_to_mini_roman(89) == 'lviii'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(99) == 'xciii'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(104) == 'civ'
    assert int_to_mini_roman(109) == 'ciix'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(150) == 'cl'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(160) == 'lx'
    assert int_to_mini_roman(169) == 'xciix'
    assert int_to_mini_roman(170) == 'xlxx'
    assert int_to_mini_roman(173) == 'xlxiii'
    assert int_to_mini_roman(180) == 'xviii'
    assert int_to_mini_roman(189) == 'xciix'
    assert int_to_mini_roman(190) == 'xix'
    assert int_to_mini_roman(199) == 'xciix'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(203) == 'ccciii'
    assert int_to_mini_roman(209) == 'cccix'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(304) == 'ccciv'
    assert int_to_mini_roman(309) == 'ccix'
    assert int_to_mini_roman(333) == ''
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1001) == 'm'
    assert int_to_mini_roman(1002) == 'mcii'
    assert int_to_mini_roman(1003) == 'mccciii'
    assert int_to_mini_roman(1004) == 'mcccciv'
    assert int_to_mini_roman(1005) == 'mccccv'
    assert int_to_mini_roman(1006) == 'mccccvi'
    assert int_to_mini_roman(1007) == 'mccccvii'
    assert int_to_mini_roman(1008) == 'mccccviii'
    assert int_to_mini_roman(1009) == 'mccccix'
    assert int_to_mini_roman(1010) == 'mxc'
    assert int_to_mini_roman(1011) == 'mxci'
    assert int_to_mini_roman(1012) == 'mxcxii'
    assert int_to_mini_roman(1013) == 'mxcxiii'
    assert int_to_mini_roman(1014) == 'mxcxiv'
    assert int_to_mini_roman(1015) == 'mxcxv'
    assert int_to_mini_roman(1016) == 'mxcvi'
    assert int_to_mini_roman(1017) == 'mxcvii'
    assert int_to_mini_roman(1018) == 'mxcviii'
    assert int_to_mini_roman(1019) == 'mxcix'
    assert int_to_mini_roman(1020) == 'mcccxx'
    assert int_to_mini_roman(1021) == 'mcccxxi'
    assert int_to_mini_roman(1022) == 'mcccxxii'
    assert int_to_mini_roman(1023) == 'mcccxxiii'
    assert int_to_mini_roman(1024) == 'mcccxxiv'
    assert int_to_mini_roman(1025) == 'mcccxxv'
    assert int_to_mini_roman(1026) == 'mcccxxvi'
    assert