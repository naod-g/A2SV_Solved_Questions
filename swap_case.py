def swap_case(s):
    swapped = []
    for char in s:
        if char.islower():
            swapped.append(char.upper())
        else:
            swapped.append(char.lower())
    return "".join(swapped)

