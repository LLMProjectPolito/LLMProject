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
    strongest_extension = ""
    max_strength = float('-inf')
    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for char in extension:
            if char.isupper():
                cap_count += 1
            elif char.islower():
                sm_count += 1
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + "." + strongest_extension

class TestStrongestExtension:
    def test_example_1(self):
        assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

    def test_example_2(self):
        assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

    def test_empty_extensions(self):
        assert Strongest_Extension("MyClass", []) == "MyClass."

    def test_all_uppercase(self):
        assert Strongest_Extension("TestClass", ['AAAA', 'BBB', 'CCCC']) == "TestClass.AAAA"

    def test_all_lowercase(self):
        assert Strongest_Extension("TestClass", ['aaaa', 'bbbb', 'cccc']) == "TestClass.aaaa"

    def test_mixed_case(self):
        assert Strongest_Extension("TestClass", ['aA', 'bB', 'cC']) == "TestClass.aA"

    def test_same_strength(self):
        assert Strongest_Extension("TestClass", ['AA', 'BB', 'CC']) == "TestClass.AA"

    def test_negative_strength(self):
        assert Strongest_Extension("TestClass", ['abc', 'def', 'ghi']) == "TestClass.abc"

    def test_class_name_with_special_chars(self):
        assert Strongest_Extension("My_Class!", ['AA', 'Be', 'CC']) == "My_Class!.AA"

    def test_extension_with_special_chars(self):
        assert Strongest_Extension("MyClass", ['A!A', 'B!e', 'C!C']) == "MyClass.A!A"

    def test_long_extensions(self):
        assert Strongest_Extension("MyClass", ['ThisIsALongExtension', 'AnotherLongExtension']) == "MyClass.ThisIsALongExtension"

    def test_numbers_in_extensions(self):
        assert Strongest_Extension("MyClass", ['123', 'ABC', 'def']) == "MyClass.ABC"

    def test_empty_string_extension(self):
        assert Strongest_Extension("MyClass", ['', 'ABC', 'def']) == "MyClass.ABC"

    def test_class_name_empty_string(self):
        assert Strongest_Extension("", ['AA', 'Be', 'CC']) == ".AA"