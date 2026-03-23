def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    new_text = text.replace(" ", "_")
    while "__" in new_text:
        new_text = new_text.replace("__", "-")
    while "___" in new_text:
        new_text = new_text.replace("___", "-")
    while new_text.count(" ") > 0:
        new_text = new_text.replace(" ", "_")
    
    consecutive_spaces = 0
    result = ""
    for char in new_text:
        if char == ' ':
            consecutive_spaces += 1
        else:
            if consecutive_spaces > 2:
                result += "-"
            else:
                result += char
            consecutive_spaces = 0
    if consecutive_spaces > 2:
        result += "-"
    return result