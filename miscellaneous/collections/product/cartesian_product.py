from itertools import product

"""
The first line contains the space separated elements of list A. The second line contains the space separated
elements of list B. Both lists have no duplicate integer elements. Output the space separated tuples of the
cartesian product.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    A = [int (x) for x in input ().split ()]
    B = [int (x) for x in input ().split ()]

    print (*list (product (A, B)))
