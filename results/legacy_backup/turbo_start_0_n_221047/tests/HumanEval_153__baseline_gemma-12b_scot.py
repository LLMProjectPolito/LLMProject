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

# STEP 1: REASONING
# The function `Strongest_Extension` takes a class name and a list of extensions as input.
# It calculates the strength of each extension based on the difference between the number of uppercase and lowercase letters.
# It returns the class name concatenated with the strongest extension name.
# The test suite should cover various scenarios, including:
# - Empty extension list
# - List with one extension
# - List with multiple extensions with different strengths
# - List with multiple extensions with the same strength (should return the first one)
# - Extensions with only uppercase letters
# - Extensions with only lowercase letters
# - Extensions with a mix of uppercase and lowercase letters
# - Class name with special characters

# STEP 2: PLAN
# Test functions:
# - test_empty_extensions: Test with an empty list of extensions.
# - test_single_extension: Test with a single extension.
# - test_multiple_extensions_different_strengths: Test with multiple extensions with different strengths.
# - test_multiple_extensions_same_strength: Test with multiple extensions with the same strength.
# - test_uppercase_only: Test with extensions containing only uppercase letters.
# - test_lowercase_only: Test with extensions containing only lowercase letters.
# - test_mixed_case: Test with extensions containing a mix of uppercase and lowercase letters.
# - test_class_name_special_characters: Test with a class name containing special characters.

# STEP 3: CODE
class TestStrongestExtension:
    def test_empty_extensions(self):
        assert Strongest_Extension("MyClass", []) == "MyClass."

    def test_single_extension(self):
        assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

    def test_multiple_extensions_different_strengths(self):
        assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"
        assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

    def test_multiple_extensions_same_strength(self):
        assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

    def test_uppercase_only(self):
        assert Strongest_Extension("MyClass", ["AAAA"]) == "MyClass.AAAA"

    def test_lowercase_only(self):
        assert Strongest_Extension("MyClass", ["aaaa"]) == "MyClass.aaaa"

    def test_mixed_case(self):
        assert Strongest_Extension("MyClass", ["aA", "Bb", "cC"]) == "MyClass.aA"

    def test_class_name_special_characters(self):
        assert Strongest_Extension("My_Class!", ["AA", "Be", "CC"]) == "My_Class!.AA"

    def test_negative_strength(self):
        assert Strongest_Extension("TestClass", ["abc", "DEF"]) == "TestClass.DEF"

    def test_zero_strength(self):
        assert Strongest_Extension("TestClass", ["abC", "DeF"]) == "TestClass.abC"