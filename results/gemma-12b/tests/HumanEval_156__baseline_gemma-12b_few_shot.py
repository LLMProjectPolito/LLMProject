
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

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(6) == "vi"
    assert int_to_mini_roman(7) == "vii"
    assert int_to_mini_roman(8) == "viii"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(10) == "x"

def test_int_to_mini_roman_intermediate():
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(39) == "xxxix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(49) == "xlix"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(59) == "lvix"
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(69) == "lxix"
    assert int_to_mini_roman(70) == "lxx"
    assert int_to_mini_roman(79) == "lxxix"
    assert int_to_mini_roman(80) == "lxxx"
    assert int_to_mini_roman(89) == "lxxxix"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(99) == "xciiiix"
    assert int_to_mini_roman(100) == "c"

def test_int_to_mini_roman_complex():
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(999) == "cmxciiiix"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_restrictions():
    assert int_to_mini_roman(0) == None # Should ideally raise an exception, but the prompt doesn't specify
    assert int_to_mini_roman(1001) == None # Should ideally raise an exception, but the prompt doesn't specify