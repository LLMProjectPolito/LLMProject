
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
    
    def calculate_strength(extension):
        cap = 0
        sm = 0
        for char in extension:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1
        return cap - sm

    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        strength = calculate_strength(extension)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


class TestStrongest_Extension:

    def test_empty_extensions(self):
        assert Strongest_Extension("my_class", []) == "my_class."

    def test_single_extension(self):
        assert Strongest_Extension("my_class", ["AA"]) == "my_class.AA"
        assert Strongest_Extension("my_class", ["Be"]) == "my_class.Be"
        assert Strongest_Extension("my_class", ["CC"]) == "my_class.CC"
        assert Strongest_Extension("my_class", ["STuFfed"]) == "my_class.STuFfed"
        assert Strongest_Extension("my_class", ["SErviNGSliCes"]) == "my_class.SErviNGSliCes"

    def test_multiple_extensions_same_strength(self):
        assert Strongest_Extension("my_class", ["AA", "Be"]) == "my_class.AA"
        assert Strongest_Extension("my_class", ["CC", "EE"]) == "my_class.CC"
        assert Strongest_Extension("my_class", ["STuFfed", "STuFfed"]) == "my_class.STuFfed"

    def test_mixed_case_extensions(self):
        assert Strongest_Extension("my_class", ["SErviNGSliCes", "Cheese"]) == "my_class.SErviNGSliCes"
        assert Strongest_Extension("my_class", ["StuFfed", "Cheese"]) == "my_class.StuFfed"

    def test_all_lowercase(self):
        assert Strongest_Extension("my_class", ["be", "ce"]) == "my_class.be"

    def test_all_uppercase(self):
        assert Strongest_Extension("my_class", ["AA", "BB"]) == "my_class.AA"

    def test_complex_case(self):
        assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

    def test_empty_class_name(self):
        assert Strongest_Extension("", ["AA", "BB"]) == ""

    def test_extension_with_special_characters(self):
        assert Strongest_Extension("my_class", ["!@#$%^", "aBcDeFg"]) == "my_class.!@#$%^"