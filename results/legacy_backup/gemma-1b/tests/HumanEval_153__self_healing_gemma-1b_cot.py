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
            strongest_extension = class_name
    return strongest_extension