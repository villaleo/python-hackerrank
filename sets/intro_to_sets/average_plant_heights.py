def average (array) -> float:
    query: set = set (array)
    size: int = len (query)

    return sum (query) / size


"""
Ms. Gabriel Williams is a botany professor at District College. One day, she asked
her student Mickey to compute the average of all the plants with distinct heights
in her greenhouse.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    n = int (input ())
    arr = list (map (int, input ().split ()))
    result = average (arr)
    print (result)
