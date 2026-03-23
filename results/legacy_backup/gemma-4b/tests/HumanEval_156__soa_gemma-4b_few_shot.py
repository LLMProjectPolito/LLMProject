def test_int_to_mini_roman_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_4():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_9():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_14():
    assert int_to_mini_roman(14) == 'xiv'

def test_int_to_mini_roman_19():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_42():
    assert int_to_mini_roman(42) == 'xxiv'

def test_int_to_mini_roman_49():
    assert int_to_mini_roman(49) == 'xlix'

def test_int_to_mini_roman_58():
    assert int_to_mini_roman(58) == 'lviii'

def test_int_to_mini_roman_67():
    assert int_to_mini_roman(67) == 'lxxvii'

def test_int_to_mini_roman_99():
    assert int_to_mini_roman(99) == 'xcii'

def test_int_to_mini_roman_100():
    assert int_to_mini_roman(100) == 'c'

def test_int_to_mini_roman_149():
    assert int_to_mini_roman(149) == 'cxlix'

def test_int_to_mini_roman_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_199():
    assert int_to_mini_roman(199) == 'cxcix'

def test_int_to_mini_roman_200():
    assert int_to_mini_roman(200) == 'cc'

def test_int_to_mini_roman_400():
    assert int_to_mini_roman(400) == 'cd'

def test_int_to_mini_roman_449():
    assert int_to_mini_roman(449) == 'cdxlix'

def test_int_to_mini_roman_499():
    assert int_to_mini_roman(499) == 'cdxcix'

def test_int_to_mini_roman_500():
    assert int_to_mini_roman(500) == 'd'

def test_int_to_mini_roman_600():
    assert int_to_mini_roman(600) == 'dc'

def test_int_to_mini_roman_700():
    assert int_to_mini_roman(700) == 'dcc'

def test_int_to_mini_roman_800():
    assert int_to_mini_roman(800) == 'dccc'

def test_int_to_mini_roman_900():
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'