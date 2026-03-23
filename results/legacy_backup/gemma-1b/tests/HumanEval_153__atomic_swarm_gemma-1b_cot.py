import pytest
import math

def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    max_strength = -1
    for extension in extensions:
        uppercase_count = 0
        lowercase_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                uppercase_count += 1
            elif 'a' <= char <= 'z':
                lowercase_count += 1
        strength = uppercase_count - lowercase_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return strongest_extension

strongest_extension = None
    max_strength = -1

    for extension in extensions:
        uppercase_count = 0
        lowercase_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                uppercase_count += 1
            elif 'a' <= char <= 'z':
                lowercase_count += 1

        strength = uppercase_count - lowercase_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return strongest_extension

def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    max_strength = -1
    for extension in extensions:
        uppercase_count = 0
        lowercase_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                uppercase_count += 1
            elif 'a' <= char <= 'z':
                lowercase_count += 1
        strength = uppercase_count - lowercase_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = class_name
    return strongest_extension