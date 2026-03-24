
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

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