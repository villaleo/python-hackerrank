"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the
following specifications:

* Mat size must be MxN. (N is an odd natural number, and M is 3 times N.)
* The design should have 'WELCOME' written in the center.
* The design pattern should only use the following characters:
    * |
    * .
    * -

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    N, M = tuple ([int (x) for x in input ().split ()])

    latter_negation_counter = 0
    latter_pattern = '.|.'
    latter_pattern_counter = 1

    row_pattern = []

    for _ in range (N // 2):
        row = '-' * ((M // 2) - latter_negation_counter - 1)
        this_pattern = row + (latter_pattern * latter_pattern_counter) + row.rjust (1)
        row_pattern.append (this_pattern)

        print (this_pattern)

        latter_negation_counter += 3
        latter_pattern_counter += 2

    print (('-' * ((M // 2) - 3)) + 'WELCOME' + ('-' * ((M // 2) - 3)))

    [print (_) for _ in reversed (row_pattern)]
