import pytest

def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_equal_strength_first():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_list():
    assert Strongest_Extension('my_class', []) == 'my_class.'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('Class', ['EXT1', 'EXT2', 'EXT3']) == 'Class.EXT1'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('Class', ['ext1', 'ext2', 'ext3']) == 'Class.ext1'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Class', ['ExT1', 'eXt2', 'EXT3']) == 'Class.EXT3'

def test_strongest_extension_negative_strength():
    assert Strongest_Extension('Class', ['aA', 'bB', 'cC']) == 'Class.aA'

def test_strongest_extension_same_strength():
    assert Strongest_Extension('Class', ['Aa', 'aA']) == 'Class.Aa'

def test_strongest_extension_long_names():
    assert Strongest_Extension('Class', ['VeryLongExtensionName', 'ShortExtension']) == 'Class.VeryLongExtensionName'

def test_strongest_extension_with_numbers():
    assert Strongest_Extension('Class', ['Ext123', 'ext456', 'ExT789']) == 'Class.Ext123'

def test_strongest_extension_all_same_strength():
    assert Strongest_Extension('my_class', ['aa', 'bb', 'cc']) == 'my_class.aa'

def test_strongest_extension_all_uppercase_2():
    assert Strongest_Extension('my_class', ['AAA', 'BBB', 'CCC']) == 'my_class.AAA'

def test_strongest_extension_all_lowercase_2():
    assert Strongest_Extension('my_class', ['aaa', 'bbb', 'ccc']) == 'my_class.aaa'

def test_strongest_extension_mixed_case_2():
    assert Strongest_Extension('my_class', ['aA', 'bB', 'cC']) == 'my_class.aA'

def test_strongest_extension_with_numbers_2():
    assert Strongest_Extension('my_class', ['a1A', 'b2B', 'c3C']) == 'my_class.a1A'

def test_strongest_extension_with_symbols():
    assert Strongest_Extension('my_class', ['a!A', 'b@B', 'c#C']) == 'my_class.a!A'

def test_strongest_extension_long_names_2():
    assert Strongest_Extension('my_class', ['VeryLongExtensionName', 'ShortExtension', 'AnotherLongExtension']) == 'my_class.ShortExtension'