import pytest
import math

def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    max_strength = -1
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
            strongest_extension = extension
    return strongest_extension

def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    max_strength = -1
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
    return class_name + '.' + strongest_extension

def test_strongest_extension_1():
    assert Strongest_Extension(str, [1, 2]) == "1."
    assert Strongest_Extension(str, [1, 2, 3]) == "1.2."
    assert Strongest_Extension(str, [1, 2, 3, 4]) == "1.2.4."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5]) == "1.2.3.4.5."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6]) == "1.2.3.4.5.6."

def test_strongest_extension_2():
    assert Strongest_Extension(str, [1, 2, 3]) == "1."
    assert Strongest_Extension(str, [1, 2, 3, 4]) == "1.2."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5]) == "1.2.4."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6]) == "1.2.3.4.5."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6, 7]) == "1.2.3.4.5.6.7."

def test_strongest_extension_3():
    assert Strongest_Extension(str, [1, 2, 3, 4, 5]) == "1."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6]) == "1.2."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6, 7]) == "1.2.4."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6, 7, 8]) == "1.2.3.4.5.6.7.8."

def test_strongest_extension_4():
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6, 7, 8]) == "1."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == "1.2."
    assert Strongest_Extension(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "1.2.3.4.5.6.7.8.9."