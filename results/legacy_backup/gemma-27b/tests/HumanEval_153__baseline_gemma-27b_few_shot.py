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
    assert Strongest_Extension('Class', ['VeryLongExtensionName', 'AnotherVeryLongExtensionName']) == 'Class.VeryLongExtensionName'