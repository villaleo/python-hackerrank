from collections import defaultdict

"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""
if __name__ == '__main__':
    n, m = tuple (map (int, input ().split ()))
    data = defaultdict (list)
    out: list = []

    group_a = data['group-A']
    group_b = data['group-B']

    [group_a.append (input ()) for _ in range (n)]
    [group_b.append (input ()) for _ in range (m)]

    for word in group_b:
        if word in group_a:
            indices = []

            for i, entry in enumerate (group_a):
                if entry == word:
                    indices.append (i + 1)
            out.append (indices)
        else:
            out.append ([-1])

    [print (*entry) for entry in out]
