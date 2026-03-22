def fix_spaces(text):
    result = ""
    count = 0
    for char in text:
        if char == ' ':
            count += 1
        else:
            if count > 2:
                result += '-'
                count = 0
            result += char
    return result