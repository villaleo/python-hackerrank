def print_formatted (number: int) -> None:
    width: int = len (str (bin (number))[2:])
    values: list[int] = list (range (1, number + 1))

    for value in values:
        print (
            str (value).rjust (width),
            str (oct (value))[2:].rjust (width),
            str (hex (value))[2:].upper ().rjust (width),
            str (bin (value))[2:].rjust (width)
        )


"""
Given an integer, n, print the following values for each integer i from 1 to n in:
    * Decimal
    * Octal
    * Hexadecimal (capitalized)
    * Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n.
Each value should be space-padded to match the width of the binary value of n and the values should be
separated by a single space.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    n = int (input ())
    print_formatted (n)
