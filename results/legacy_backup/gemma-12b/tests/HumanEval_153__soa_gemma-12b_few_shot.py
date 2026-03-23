import pytest

def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('MyClass', []) == 'MyClass.'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('Class', ['AAAA', 'BBB', 'CCCC']) == 'Class.AAAA'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('Class', ['aaaa', 'bbbb', 'cccc']) == 'Class.aaaa'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Class', ['aA', 'Bb', 'Cc']) == 'Class.aA'

def test_strongest_extension_negative_strength():
    assert Strongest_Extension('Class', ['abc', 'ABC', 'def']) == 'Class.ABC'

def test_strongest_extension_zero_strength():
    assert Strongest_Extension('Class', ['ab', 'AB', 'cd']) == 'Class.ab'

def test_strongest_extension_class_with_underscore():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_class_with_numbers():
    assert Strongest_Extension('Class123', ['AA', 'Be', 'CC']) == 'Class123.AA'

def test_strongest_extension_extension_with_numbers():
    assert Strongest_Extension('Class', ['A1A', 'B2B', 'C3C']) == 'Class.A1A'

def test_strongest_extension_complex_extensions():
    assert Strongest_Extension('MyClass', ['Ext123', 'ext456', 'EXT789']) == 'MyClass.EXT789'