
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
    if not extensions:
        return f"{class_name}."
    
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        low_count = sum(1 for char in extension if char.islower())
        strength = cap_count - low_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


class TestStrongestExtension:
    def test_empty_extensions(self):
        assert Strongest_Extension("MyClass", []) == "MyClass."

    def test_single_extension(self):
        assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

    def test_multiple_extensions_different_strengths(self):
        assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"
        assert Strongest_Extension("MyClass", ["AA", "Be", "CC", "DD"]) == "MyClass.AA"
        assert Strongest_Extension("MyClass", ["AA", "Be", "CC", "DD", "EE"]) == "MyClass.AA"

    def test_multiple_extensions_same_strength(self):
        assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"
        assert Strongest_Extension("MyClass", ["Be", "De", "Fe"]) == "MyClass.Be"

    def test_zero_strength_extensions(self):
        assert Strongest_Extension("MyClass", ["Aa", "Bb", "Cc"]) == "MyClass.Aa"

    def test_negative_strength_extensions(self):
        assert Strongest_Extension("MyClass", ["aA", "bB", "cC"]) == "MyClass.aA"
        assert Strongest_Extension("MyClass", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "MyClass.SErviNGSliCes"

    def test_class_name_with_special_characters(self):
        assert Strongest_Extension("My_Class!", ["Extension1"]) == "My_Class!.Extension1"

    def test_empty_class_name(self):
        assert Strongest_Extension("", ["Extension1"]) == ".Extension1"

    def test_mixed_case_extensions(self):
        assert Strongest_Extension("MyClass", ["ExTeNsIoN", "extensiON"]) == "MyClass.ExTeNsIoN"