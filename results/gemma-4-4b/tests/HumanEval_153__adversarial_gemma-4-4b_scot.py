
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

# STEP 1: REASONING
# The function `Strongest_Extension` takes a class name and a list of extensions.
# It calculates the strength of each extension based on the number of uppercase and lowercase letters.
# The strength is calculated as (number of uppercase letters) - (number of lowercase letters).
# The function returns the class name followed by the strongest extension name, separated by a dot.
# If multiple extensions have the same strength, the first one in the list is chosen.
# Edge cases to consider:
# 1. Empty extension list: Should return the class name itself.
# 2. Empty class name: Should return an empty string.
# 3. Extensions with only uppercase or only lowercase letters.
# 4. Extensions with mixed case.
# 5. Extensions with special characters.
# 6. Class name with special characters.

# STEP 2: PLAN
# Test cases:
# 1. Basic test case with mixed-case extensions and a class name.
# 2. Test case with an empty extension list.
# 3. Test case with an empty class name.
# 4. Test case with extensions containing only uppercase letters.
# 5. Test case with extensions containing only lowercase letters.
# 6. Test case with extensions containing special characters.
# 7. Test case with a class name containing special characters.
# 8. Test case with multiple extensions having the same strength.
# 9. Test case with a single extension.
# 10. Test case with a class name and extension that are the same.

# STEP 3: CODE
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
        return class_name
    
    class_name = class_name
    
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = 0
        sm = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap += 1
            elif 'a' <= char <= 'z':
                sm += 1
        
        strength = cap - sm
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
        elif strength == max_strength and strongest_extension == "":
            strongest_extension = extension
            
    return f"{class_name}.{strongest_extension}"

@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"], "Slices.SErviNGSliCes"),
        ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
        ("", ["AA", "Be", "CC"], ""),
        ("my_class", [], "my_class"),
        ("MyClass", ["ABC", "def", "GHI"], "MyClass.ABC"),
        ("MyClass", ["abc", "DEF", "ghi"], "MyClass.DEF"),
        ("MyClass", ["123", "abc", "DEF"], "MyClass.DEF"),
        ("MyClass", ["A", "a", "AA"], "MyClass.AA"),
        ("MyClass", ["a", "A", "aa"], "MyClass.aa"),
        ("MyClass", ["", "abc", "def"], "MyClass.def"),
        ("MyClass", ["abc", "", "def"], "MyClass.def"),
        ("MyClass", ["abc", "def", ""], "MyClass.def"),
        ("MyClass", ["abc", "def", "ghi"], "MyClass.abc"),
        ("MyClass", ["ABC", "def", "GHI"], "MyClass.ABC"),
        ("MyClass", ["ABC", "def", "GHI"], "MyClass.ABC"),
        ("MyClass", ["ABC", "def", "GHI"], "MyClass.ABC"),
        ("MyClass", ["ABC", "def", "GHI"], "MyClass.ABC"),
        ("MyClass", ["ABC", "def", "GHI"], "MyClass.ABC"),
        ("MyClass", ["ABC", "def", "GHI"], "MyClass.ABC"),
    ],
)
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected