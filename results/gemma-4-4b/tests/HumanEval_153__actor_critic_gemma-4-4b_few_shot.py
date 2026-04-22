
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
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = 0
        sm = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap += 1
            elif 'a' <= char <= 'z':
                sm += 1

        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = f"{class_name}.{extension}"

    return strongest_extension
import pytest

def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('MyClass', []) == 'MyClass.'

def test_strongest_extension_all_same_strength():
    assert Strongest_Extension('MyClass', ['AA', 'BB', 'CC']) == 'MyClass.AA'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('MyClass', ['aA', 'bB', 'cC']) == 'MyClass.aA'

def test_strongest_extension_no_uppercase():
    assert Strongest_Extension('MyClass', ['aaa', 'bbb', 'ccc']) == 'MyClass.aaa'

def test_strongest_extension_no_lowercase():
    assert Strongest_Extension('MyClass', ['AAA', 'BBB', 'CCC']) == 'MyClass.AAA'

def test_strongest_extension_empty_class_name():
    assert Strongest_Extension('', ['AA', 'BB', 'CC']) == '.AA'

def test_strongest_extension_class_name_with_uppercase():
    assert Strongest_Extension('MyClass', ['aa', 'BB', 'cc']) == 'MyClass.BB'

def test_strongest_extension_complex_extensions():
    assert Strongest_Extension('TestClass', ['ExAmPlE', 'NoCase', 'ALLCAPS']) == 'TestClass.ALLCAPS'