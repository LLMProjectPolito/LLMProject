import pytest
import math

def test_strongest_extension_same_strength_first_wins():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"