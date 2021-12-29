"""
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical
characters, digits, lowercase and uppercase characters.

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    s = input ()

    flags = [False, False, False, False, False]
    for char in s:
        if char.isalnum ():
            flags[0] = True
        if char.isalpha ():
            flags[1] = True
        if char.isdigit ():
            flags[2] = True
        if char.islower ():
            flags[3] = True
        if char.isupper ():
            flags[4] = True

    print (*flags, sep='\n')
