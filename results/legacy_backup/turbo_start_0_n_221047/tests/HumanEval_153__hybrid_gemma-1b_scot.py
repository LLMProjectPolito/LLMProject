import pytest
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    """
    Finds the strongest extension from a list of extensions.

    Args:
        class_name: The name of the class.
        extensions: A list of extension strings.

    Returns:
        The name of the strongest extension.
    """
    strongest_extension = None
    max_strength = -1

    for extension in extensions:
        uppercase_count = 0
        lowercase_count = 0
        for char in extension:
            if char.isupper():
                uppercase_count += 1
            else:
                lowercase_count += 1

        strength = uppercase_count - lowercase_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return strongest_extension

def test_strongest_extension_basic():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_strongest_extension_uppercase():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_strongest_extension_lowercase():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_strongest_extension_mixed():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC", "EE"]) == "my_class.AA"

def test_strongest_extension_empty():
    assert Strongest_Extension("my_class", []) == None

def test_strongest_extension_empty_list():
    assert "my_class" in ["AA", "Be", "CC"]