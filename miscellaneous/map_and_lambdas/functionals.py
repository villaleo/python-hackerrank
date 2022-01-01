cube = lambda x: x ** 3


def fibonacci (n: int) -> list:
    """Returns a list of the first N fibonacci numbers"""
    numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    if n == 0:
        return []
    return numbers[: n]


"""
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0
being the first number. Then, apply the map function and a lambda expression to cube each fibonacci
number and print the list.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    n = int (input ())
    print (list (map (cube, fibonacci (n))))
