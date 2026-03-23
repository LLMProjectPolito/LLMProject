def test_Strongest_Extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_Strongest_Extension_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_Strongest_Extension_empty_extensions():
    assert Strongest_Extension('my_class', []) == 'my_class'

def test_Strongest_Extension_single_extension():
    assert Strongest_Extension('my_class', ['AA']) == 'my_class.AA'

def test_Strongest_Extension_uppercase_only():
    assert Strongest_Extension('my_class', ['A', 'B', 'C']) == 'my_class.A'

def test_Strongest_Extension_lowercase_only():
    assert Strongest_Extension('my_class', ['a', 'b', 'c']) == 'my_class.a'

def test_Strongest_Extension_mixed_case():
    assert Strongest_Extension('my_class', ['aA', 'bB', 'cC']) == 'my_class.aA'

def test_Strongest_Extension_complex_extension():
    assert Strongest_Extension('my_class', ['aB1C', 'dE2F', 'gH3I']) == 'my_class.aB1C'

def test_Strongest_Extension_numeric_extension():
    assert Strongest_Extension('my_class', ['123', '456', '789']) == 'my_class.123'