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
    pass

class TestStrongestExtension:

    def test_empty_extensions(self):
        assert Strongest_Extension("MyClass", []) == "MyClass."

    def test_single_extension(self):
        assert Strongest_Extension("MyClass", ["Extension"]) == "MyClass.Extension"

    def test_multiple_extensions_different_strengths(self):
        assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

    def test_multiple_extensions_same_strengths(self):
        assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

    def test_negative_strength(self):
        assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

    def test_mixed_case_extensions(self):
        assert Strongest_Extension("MyClass", ["aA", "Bb", "cC"]) == "MyClass.aA"

    def test_extension_with_numbers(self):
        assert Strongest_Extension("MyClass", ["A1", "b2", "C3"]) == "MyClass.A1"

    def test_extension_with_special_characters(self):
        assert Strongest_Extension("MyClass", ["A!", "b?", "C#"]) == "MyClass.A!"

    def test_class_name_with_special_characters(self):
        assert Strongest_Extension("My_Class!", ["A", "B", "C"]) == "My_Class!.A"

    def test_long_extensions(self):
        assert Strongest_Extension("MyClass", ["VeryLongExtension1", "Short"]) == "MyClass.Short"

    def test_all_uppercase(self):
        assert Strongest_Extension("MyClass", ["AAAA", "BBBB", "CCCC"]) == "MyClass.AAAA"

    def test_all_lowercase(self):
        assert Strongest_Extension("MyClass", ["aaaa", "bbbb", "cccc"]) == "MyClass.aaaa"