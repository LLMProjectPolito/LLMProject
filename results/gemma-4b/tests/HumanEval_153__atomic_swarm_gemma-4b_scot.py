import pytest
import math

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
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def test_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

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
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `Strongest_Extension` takes a class name and a list of extensions.
### It calculates the strength of each extension based on the difference between
### uppercase and lowercase letters. It returns the name of the strongest extension
### in the format "ClassName.StrongestExtensionName". If multiple extensions have
### the same strength, it returns the one that appears first in the list.
### The edge case to test is an empty list of extensions. In this case, the function
### should return the original class name.

### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_extensions - Test with an empty list of extensions.
### test_single_extension - Test with a single extension.
### test_multiple_extensions_different_strengths - Test with multiple extensions
### with different strengths.
### test_multiple_extensions_same_strengths - Test with multiple extensions
### with the same strength.

### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `Strongest_Extension` takes a class name and a list of extensions.
### It calculates the strength of each extension based on the difference between
### uppercase and lowercase letters. It returns the name of the strongest extension
### in the format "ClassName.StrongestExtensionName". If multiple extensions have
### the same strength, it returns the one that appears first in the list.
### The edge case to test is an empty list of extensions. In this case, the function
### should return the original class name.

### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_extensions - Test with an empty list of extensions.
### test_single_extension - Test with a single extension.
### test_multiple_extensions_different_strengths - Test with multiple extensions
### with different strengths.
### test_multiple_extensions_same_strengths - Test with multiple extensions
### with the same strength.

### STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class."

def test_single_extension():
    assert Strongest_Extension("my_class", ["AA"]) == "my_class.AA"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_multiple_extensions_same_strengths():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

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
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

### SCoT Steps:
# STEP 1: REASONING - The function needs to be tested for an unusual case: an empty list of extensions.
# The expected behavior is to return the original class name.
# STEP 2: PLAN - Test function name: test_empty_extensions.
# Scenario: Pass an empty list of extensions.
# STEP 3: CODE - Write the pytest suite.
def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class."