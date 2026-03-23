import pytest

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

    return f"{class_name}.{strongest_extension}"