def double_the_difference(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lst[0] * lst[1]
    if len(lst) == 3:
        return lst[0] * lst[1] * lst[2]
    return 0