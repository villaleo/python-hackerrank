from itertools import permutations

"""
You are given a string S. Your task is to print all possible permutations of size k of the string in
lexicographic sorted order. The string contains only UPPERCASE characters.

Further details are provided in the info.pdf file provided within this directory. 
"""
if __name__ == '__main__':
    string, k = tuple (input ().upper ().split ())
    string: list = [c for c in string]
    k: int = int (k)

    permute = permutations (string, k)
    out: list = []

    [out.append (''.join (entry)) for entry in permute]
    [print (entry) for entry in sorted (out)]
