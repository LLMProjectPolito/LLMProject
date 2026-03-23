import pytest
import math


# Focus: Boundary Values
def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    max_strength = -1
    for extension in extensions:
        cap_letters = 0
        lower_letters = 0
        for letter in extension:
            if letter.isupper():
                cap_letters += 1
            else:
                lower_letters += 1
        strength = cap_letters - lower_letters
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + "." + strongest_extension

# Focus: Type Scenarios
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
    return class_name + "." + strongest_extension

# Focus: Logic Branches
def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    max_strength = -1
    for extension in extensions:
        cap = 0
        sm = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap += 1
            else:
                sm += 1
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + '.' + strongest_extension