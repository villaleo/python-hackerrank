"""
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps
in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    amount_stamps: int = int (input ())
    stamps: set = set ([])

    [stamps.add (input ()) for _ in range (amount_stamps)]
    print (len (stamps))
