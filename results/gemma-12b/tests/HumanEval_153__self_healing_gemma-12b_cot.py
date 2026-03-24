
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
    if not extensions:
        return class_name + "."
    
    strongest_extension = ""
    max_strength = float('-inf')
    
    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap_count += 1
            elif 'a' <= char <= 'z':
                sm_count += 1
        
        strength = cap_count - sm_count
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    
    return class_name + "." + strongest_extension

import pytest

class TestStrongestExtension:
    def test_example_1(self):
        assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

    def test_example_2(self):
        assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

    def test_empty_extensions(self):
        assert Strongest_Extension("MyClass", []) == "MyClass."

    def test_single_extension(self):
        assert Strongest_Extension("MyClass", ["Extension"]) == "MyClass.Extension"

    def test_equal_strength(self):
        assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

    def test_negative_strength(self):
        assert Strongest_Extension("MyClass", ["aA", "bB", "cC"]) == "MyClass.aA"

    def test_mixed_case(self):
        assert Strongest_Extension("MyClass", ["MiXeD", "CaSe"]) == "MyClass.MiXeD"

    def test_all_uppercase(self):
        assert Strongest_Extension("MyClass", ["UPPERCASE"]) == "MyClass.UPPERCASE"

    def test_all_lowercase(self):
        assert Strongest_Extension("MyClass", ["lowercase"]) == "MyClass.lowercase"

    def test_numbers_and_letters(self):
        assert Strongest_Extension("MyClass", ["A1", "b2", "C3"]) == "MyClass.A1"

    def test_special_characters(self):
        assert Strongest_Extension("MyClass", ["!@#", "$%^"]) == "MyClass.!@#"

    def test_long_extensions(self):
        assert Strongest_Extension("MyClass", ["VeryLongExtensionName", "Short"]) == "MyClass.VeryLongExtensionName"

    def test_class_name_with_special_characters(self):
        assert Strongest_Extension("My_Class!", ["Extension"]) == "My_Class!.Extension"

    def test_class_name_with_numbers(self):
        assert Strongest_Extension("Class123", ["Extension"]) == "Class123.Extension"