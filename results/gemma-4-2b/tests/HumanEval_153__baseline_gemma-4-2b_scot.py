
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
# The function `Strongest_Extension` takes a class name and a list of extensions as input.
# It calculates the strength of each extension based on the difference between uppercase and lowercase letters.
# It returns the class name followed by the strongest extension name.
# The strength is calculated as (CAP - SM), where CAP is the number of uppercase letters and SM is the number of lowercase letters in the extension name.
# If multiple extensions have the same strength, the extension that appears first in the input list is chosen.

# Test cases:
# 1. Basic test case with a single extension.
# 2. Test case with multiple extensions and different strengths.
# 3. Test case with extensions having the same strength.
# 4. Test case with an empty list of extensions.
# 5. Test case with an extension name containing special characters.
# 6. Test case with an extension name containing numbers.
# 7. Test case with an extension name containing both uppercase and lowercase letters.
# 8. Test case with an empty class name.
# 9. Test case with a class name containing special characters.
# 10. Test case with a class name containing numbers.



# STEP 2: PLAN
# The pytest suite will include the following test functions:
# - test_basic_case: Checks the function with a single extension.
# - test_multiple_extensions: Checks the function with multiple extensions and different strengths.
# - test_same_strength: Checks the function with extensions having the same strength.
# - test_empty_extensions: Checks the function with an empty list of extensions.
# - test_special_characters: Checks the function with an extension name containing special characters.
# - test_numbers: Checks the function with an extension name containing numbers.
# - test_mixed_case: Checks the function with an extension name containing both uppercase and lowercase letters.
# - test_empty_class_name: Checks the function with an empty class name.
# - test_special_class_name: Checks the function with a class name containing special characters.
# - test_numbers_class_name: Checks the function with a class name containing numbers.

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
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = 0
        sm = 0
        for char in extension:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1

        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = class_name + "." + extension
        elif strength == max_strength and extensions.index(extension) < extensions.index(strongest_extension):
            strongest_extension = class_name + "." + extension

    return strongest_extension


def test_basic_case():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_multiple_extensions():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_same_strength():
    assert Strongest_Extension('ClassA', ['A', 'B']) == 'ClassA.A'

def test_empty_extensions():
    assert Strongest_Extension('ClassB', []) == 'ClassB. '

def test_special_characters():
    assert Strongest_Extension('ClassC', ['!@#$%^', 'Special']) == 'ClassC.Special'

def test_numbers():
    assert Strongest_Extension('ClassD', ['123', 'Numbers']) == 'ClassD.Numbers'

def test_mixed_case():
    assert Strongest_Extension('ClassE', ['MiXeD', 'Case']) == 'ClassE.MiXeD'

def test_empty_class_name():
    assert Strongest_Extension('', ['A', 'B']) == ''

def test_special_class_name():
    assert Strongest_Extension('ClassF', ['!@#']) == 'ClassF.!'

def test_numbers_class_name():
    assert Strongest_Extension('ClassG', ['123']) == 'ClassG.123'