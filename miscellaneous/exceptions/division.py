from collections import deque

"""
You are given two values a and b. Perform integer division and print a / b.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    out: deque = deque ()
    result: float
    t = int (input ())

    for _ in range (t):
        a, b = tuple (input ().split ())
        try:
            result = int (a) // int (b)
            out.append (result)
        except ZeroDivisionError as div_zero_error:
            out.append (f'Error Code: {div_zero_error}')
        except ValueError as value_error:
            out.append (f'Error Code: {value_error}')

    [print (entry) for entry in out]
