def swap_case (s: str) -> str:
    out = ""
    for c in s:
        if c.isalpha ():
            if c.isupper ():
                out += c.lower ()
            elif c.islower ():
                out += c.upper ()
        else:
            out += c
    return out


"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters
to uppercase letters and vice versa.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    s = input ()
    result = swap_case (s)
    print (result)
