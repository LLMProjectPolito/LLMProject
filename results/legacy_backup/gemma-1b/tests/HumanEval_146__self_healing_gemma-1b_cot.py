count = 0
    for num in nums:
        s = str(num)
        if len(s) == 1:
            if int(s[0]) % 2 != 0 and int(s[-1]) % 2 != 0:
                count += 1
        else:
            first_digit = int(s[0])
            last_digit = int(s[-1])
            if first_digit > 10 and last_digit % 2 != 0:
                count += 1
    return count