
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
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_strongest_extension_same_strength():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension("TestClass", ['AAAA', 'BBBB', 'CCCC']) == "TestClass.AAAA"

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension("TestClass", ['aaaa', 'bbbb', 'cccc']) == "TestClass.aaaa"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("MyClass", ['aA', 'Bb', 'Cc']) == "MyClass.aA"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Class", ['abc', 'DEF', 'ghi']) == "Class.DEF"

def test_strongest_extension_zero_strength():
    assert Strongest_Extension("Class", ['ab', 'CD', 'ef']) == "Class.CD"

def test_strongest_extension_class_with_underscore():
    assert Strongest_Extension("my_class_name", ['AA', 'Be', 'CC']) == "my_class_name.AA"

def test_strongest_extension_extension_with_underscore():
    assert Strongest_Extension("Class", ['A_A', 'B_b', 'C_c']) == "Class.A_A"

def test_strongest_extension_class_and_extension_with_underscore():
    assert Strongest_Extension("my_class_name", ['A_A', 'B_b', 'C_c']) == "my_class_name.A_A"