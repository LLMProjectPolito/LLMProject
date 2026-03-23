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
            strongest_extension = class_name
    return strongest_extension

# Focus: Type Scenarios
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
            strongest_extension = class_name
    return strongest_extension

# Focus: Logic Branches
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
            strongest_extension = class_name
    return strongest_extension