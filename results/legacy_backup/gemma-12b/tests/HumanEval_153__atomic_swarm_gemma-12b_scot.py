import pytest
import math

def test_basic():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_empty_extensions():
    """Test with an empty list of extensions."""
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

import pytest

def test_empty_extensions_list(class_name):
    """Test case: Empty extensions list should return ClassName."""
    assert Strongest_Extension(class_name, []) == f"{class_name}.None"

def test_all_extensions_same_strength(class_name, extensions):
    """Test case: All extensions have the same strength, return the first one."""
    result = Strongest_Extension(class_name, extensions)
    assert result == f"{class_name}.{extensions[0]}"

def test_extension_with_only_uppercase(class_name, extensions):
    """Test case: Extension with only uppercase letters."""
    result = Strongest_Extension(class_name, extensions)
    assert result == f"{class_name}.{extensions[0]}"

def test_extension_with_only_lowercase(class_name, extensions):
    """Test case: Extension with only lowercase letters."""
    result = Strongest_Extension(class_name, extensions)
    assert result == f"{class_name}.{extensions[0]}"

def test_extension_with_numbers(class_name, extensions):
    """Test case: Extension with numbers."""
    result = Strongest_Extension(class_name, extensions)
    assert result == f"{class_name}.{extensions[0]}"