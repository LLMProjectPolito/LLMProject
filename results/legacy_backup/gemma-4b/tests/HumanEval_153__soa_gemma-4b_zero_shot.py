import pytest

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
    strongest_extension = None
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    if strongest_extension is None:
        return class_name + "." + extensions[0] if extensions else class_name
    else:
        return class_name + "." + strongest_extension

def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class"

def test_single_extension():
    assert Strongest_Extension("Slices", ["SErviNGSliCes"]) == "Slices.SErviNGSliCes"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_mixed_case_extensions():
    assert Strongest_Extension("my_class", ["sErvIngsLiCes", "Cheese", "StuFfed"]) == "my_class.sErvIngsLiCes"

def test_all_uppercase_extensions():
    assert Strongest_Extension("my_class", ["ABC", "DEF", "GHI"]) == "my_class.ABC"

def test_all_lowercase_extensions():
    assert Strongest_Extension("my_class", ["abc", "def", "ghi"]) == "my_class.abc"

def test_empty_class_name():
    assert Strongest_Extension("", ["AA", "BB"]) == ""

def test_complex_extension_names():
    assert Strongest_Extension("Data", ["DataAnalysis", "DataProcessing", "DataMining"]) == "Data.DataAnalysis"

def test_extension_with_numbers():
    assert Strongest_Extension("Test", ["Test123", "Test456", "Test"]) == "Test.Test123"

def test_extension_with_special_characters():
    assert Strongest_Extension("Example", ["Ex!mpl3", "Ex@mpl4", "Ex#mpl5"]) == "Example.Ex!mpl3"

def test_class_name_with_numbers():
    assert Strongest_Extension("123Test", ["123AA", "123BB", "123CC"]) == "123Test.123AA"

def test_class_name_with_special_characters():
    assert Strongest_Extension("!@#Test", ["!@#AA", "!@#BB", "!@#CC"]) == "!@#Test.!@#AA"