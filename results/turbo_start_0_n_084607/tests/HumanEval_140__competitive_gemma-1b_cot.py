def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    result = ""
    count = 0
    for char in text:
        if char == " ":
            count += 1
        else:
            if count > 2:
                result += "_"
            else:
                result += char
            count = 0
    return result