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
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function takes a class name and a list of extensions.
# It calculates the strength of each extension based on the difference between uppercase and lowercase letters.
# It returns a string in the format "ClassName.StrongestExtensionName".
# If multiple extensions have the same strength, it returns the first one in the list.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_extensions: Test with an empty list of extensions.
# test_single_extension: Test with a single extension.
# test_multiple_extensions_different_strengths: Test with multiple extensions having different strengths.
# test_multiple_extensions_same_strength: Test with multiple extensions having the same strength.
# test_class_name_with_uppercase: Test with a class name containing uppercase letters.
# test_class_name_with_lowercase: Test with a class name containing lowercase letters.
# test_extension_with_no_uppercase: Test with an extension containing no uppercase letters.
# test_extension_with_no_lowercase: Test with an extension containing no lowercase letters.
# test_extension_with_mixed_case: Test with an extension containing a mix of uppercase and lowercase letters.
# test_edge_case_all_uppercase: Test with an extension containing only uppercase letters.
# test_edge_case_all_lowercase: Test with an extension containing only lowercase letters.

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("class_name, extensions, expected", [
    ("MyClass", [], "MyClass.None"),
    ("MyClass", ["Extension1"], "MyClass.Extension1"),
    ("MyClass", ["Extension1", "Extension2"], "MyClass.Extension1"),
    ("MyClass", ["Extension1", "Extension2", "Extension3"], "MyClass.Extension1"),
    ("MyClass", ["AA", "Be", "CC"], "MyClass.AA"),
    ("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"], "Slices.SErviNGSliCes"),
    ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
    ("ClassName", ["ExtensionA", "extensionB", "ExtensionC"], "ClassName.ExtensionA"),
    ("TestClass", ["UPPERCASE", "lowercase", "MixedCase"], "TestClass.UPPERCASE"),
    ("Class123", ["Ext1", "Ext2", "Ext3"], "Class123.Ext1"),
    ("ClassWithSpaces", ["Extension A", "ExtensionB"], "ClassWithSpaces.ExtensionB"),
    ("ClassWithNumbers123", ["Ext1", "Ext2", "Ext3"], "ClassWithNumbers123.Ext1"),
    ("ClassWithSymbols!@#", ["Ext1", "Ext2", "Ext3"], "ClassWithSymbols!@#.Ext1"),
    ("MyClass", ["AAAA", "BBBB", "CCCC"], "MyClass.AAAA"),
    ("MyClass", ["aaaa", "bbbb", "cccc"], "MyClass.aaaa"),
])
def test_strongest_extension(class_name, extensions, expected):
    if not extensions:
        assert Strongest_Extension(class_name, extensions) == f"{class_name}.None"
    else:
        assert Strongest_Extension(class_name, extensions) == expected