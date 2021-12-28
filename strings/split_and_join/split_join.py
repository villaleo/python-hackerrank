def split_and_join (line: str) -> str:
    to_list = line.split ()
    add_hyphen = "-".join (to_list)
    return add_hyphen


"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function description:
Complete the split_and_join function in the editor below.
split_and_join has the following parameters:
    string line: a string of space-separated words
Returns:
    string: the resulting string

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    line = input ()
    result = split_and_join (line)
    print (result)
