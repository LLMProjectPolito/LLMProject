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

    return f"{class_name}.{strongest_extension}"

class TestStrongestExtension:

    def test_empty_extensions_list(self):
        assert Strongest_Extension("MyClass", []) == "MyClass.None"

    def test_single_extension(self):
        assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

    def test_multiple_extensions_different_strengths(self):
        assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

    def test_multiple_extensions_same_strengths(self):
        assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

    def test_extensions_with_mixed_case(self):
        assert Strongest_Extension("TestClass", ["ExAmPlE", "anotherExample", "MiXeD"]) == "TestClass.ExAmPlE"

    def test_extensions_with_no_uppercase(self):
        assert Strongest_Extension("TestClass", ["lowercase", "anotherlowercase"]) == "TestClass.lowercase"

    def test_extensions_with_no_lowercase(self):
        assert Strongest_Extension("TestClass", ["UPPERCASE", "ANOTHERUPPERCASE"]) == "TestClass.UPPERCASE"

    def test_extensions_with_numbers_and_symbols(self):
        assert Strongest_Extension("TestClass", ["Ext123", "Ext!@#", "ExtABC"]) == "TestClass.ExtABC"

    def test_class_name_with_underscores(self):
        assert Strongest_Extension("my_class_name", ["ExtensionA", "ExtensionB"]) == "my_class_name.ExtensionA"

    def test_extension_names_with_spaces(self):
        assert Strongest_Extension("TestClass", ["Extension One", "ExtensionTwo"]) == "TestClass.ExtensionTwo"