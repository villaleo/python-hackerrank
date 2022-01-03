def print_rangoli (size):
    letters = [chr (x) for x in range (ord ('a'), ord ('z') + 1)]

    # Width of the pattern from the middle is (size * 2) - 2
    # Height of pattern is size - 1 up until middle

    # Dash (-) pattern
    pattern = []
    staircase_break = 0
    letters_index = 1

    for _ in range (size):
        __first_iter = _ == 0

        letters_list = letters[: size]
        letters_list.reverse ()

        dashes = '-' * ((size * 2) - 2 - staircase_break)
        l_letters = '-'.join (letters_list[:letters_index])

        r_letters: str
        if __first_iter:
            r_letters = ""
        else:
            temp = letters_list[:letters_index]
            temp.reverse ()
            r_letters = '-' + '-'.join (temp[1:])

        curr = dashes + l_letters + r_letters + dashes

        pattern.append (curr)
        print (curr)

        staircase_break += 2
        letters_index += 1

    __first_iter = 0
    for e in reversed (pattern):
        if __first_iter == 0:
            __first_iter = 1
        else:
            print (e)


"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    n = int (input ())
    print_rangoli (n)
