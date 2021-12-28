def mutate_string (string: str, position: int, character: str) -> str:
    to_list = list (string)
    to_list[position] = character
    to_string = ''.join (to_list)
    return to_string


"""
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    s = input ()
    i, c = input ().split ()
    s_new = mutate_string (s, int (i), c)
    print (s_new)
