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
    assert Strongest_Extension('Class', ['AA1', 'Be2', 'CC3']) == 'Class.AA1'

def test_strongest_extension_complex_extensions():
    assert Strongest_Extension('MyClass', ['A1b2C', 'b1A2C', 'c1B2A']) == 'MyClass.A1b2C'