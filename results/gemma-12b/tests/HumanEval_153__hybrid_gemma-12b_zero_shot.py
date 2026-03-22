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
        assert Strongest_Extension("TestClass", ['aA', 'Bb', 'Cc']) == "TestClass.aA"

    def test_equal_strength_first_wins(self):
        assert Strongest_Extension("TestClass", ['AA', 'BB', 'CC']) == "TestClass.AA"

    def test_negative_strength(self):
        assert Strongest_Extension("TestClass", ['abc', 'def', 'ghi']) == "TestClass.abc"

    def test_class_name_with_underscores(self):
        assert Strongest_Extension("my_class_name", ['AA', 'Be', 'CC']) == "my_class_name.AA"

    def test_extension_with_numbers(self):
        assert Strongest_Extension("TestClass", ['A1', 'B2', 'C3']) == "TestClass.A1"

    def test_extension_with_special_characters(self):
        assert Strongest_Extension("TestClass", ['A!', 'B@', 'C#']) == "TestClass.A!"

    def test_multiple_extensions_same_strength(self):
        assert Strongest_Extension("TestClass", ['AA', 'BB', 'CC', 'DD']) == "TestClass.AA"

    def test_long_extensions(self):
        assert Strongest_Extension("TestClass", ['ThisIsALongExtension', 'AnotherLongExtension']) == "TestClass.ThisIsALongExtension"

    def test_class_name_empty(self):
        assert Strongest_Extension("", ['AA', 'BB', 'CC']) == ".AA"

    def test_single_extension(self):
        assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

    def test_multiple_extensions_different_strengths(self):
        assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

    def test_multiple_extensions_same_strength_first_wins(self):
        assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

    def test_negative_strength_2(self):
        assert Strongest_Extension("MyClass", ["SErviNGSliCes"]) == "MyClass.SErviNGSliCes"

    def test_positive_strength(self):
        assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

    def test_mixed_case_extensions(self):
        assert Strongest_Extension("MyClass", ["aA", "Bb", "Cc"]) == "MyClass.aA"

    def test_extension_with_numbers_2(self):
        assert Strongest_Extension("MyClass", ["A1", "b2", "C3"]) == "MyClass.A1"

    def test_extension_with_symbols(self):
        assert Strongest_Extension("MyClass", ["A!", "b#", "C$"]) == "MyClass.A!"

    def test_class_name_with_underscores_2(self):
        assert Strongest_Extension("My_Class", ["AA", "Be", "CC"]) == "My_Class.AA"

    def test_class_name_with_spaces(self):
        assert Strongest_Extension("My Class", ["AA", "Be", "CC"]) == "My Class.AA"

    def test_complex_extensions_2(self):
        extensions = ["SErviNGSliCes", "Cheese", "StuFfed"]
        assert Strongest_Extension("Slices", extensions) == "Slices.SErviNGSliCes"

    def test_all_extensions_have_zero_strength(self):
        assert Strongest_Extension("MyClass", ["ab", "cd", "ef"]) == "MyClass.ab"

    def test_extension_with_only_uppercase_2(self):
        assert Strongest_Extension("MyClass", ["AAAA"]) == "MyClass.AAAA"

    def test_extension_with_only_lowercase_2(self):
        assert Strongest_Extension("MyClass", ["aaaa"]) == "MyClass.aaaa"

    def test_extension_with_mixed_case_and_same_strength(self):
        assert Strongest_Extension("MyClass", ["aA", "Aa"]) == "MyClass.aA"

    def test_long_extensions_2(self):
        extensions = ["ThisIsALongExtension", "AnotherLongExtension", "YetAnotherLongExtension"]
        assert Strongest_Extension("MyClass", extensions) == "MyClass.ThisIsALongExtension"

    def test_extension_with_special_characters_2(self):
        assert Strongest_Extension("MyClass", ["A@B", "b$c"]) == "MyClass.A@B"