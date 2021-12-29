def count_substring (string: str, sub_string: str) -> int:
    # count number of occurrences of a substring (including overlapping substrings)

    overlap: bool = False
    if len (string) > 2:
        overlap = sub_string[0] == sub_string[-1]

    if not overlap:
        return string.count (sub_string)

    num_occurrences = 0
    string_size = len (string)
    substring_index = 0
    sub_string_size = len (sub_string)

    for string_index in range (string_size):
        if string[string_index] == sub_string[substring_index]:
            if substring_index == sub_string_size - 1:
                num_occurrences += 1
                substring_index = 1
                continue
            substring_index += 1
        else:
            substring_index = 0

    return num_occurrences


"""
In this challenge, the user enters a string and a substring. You have to print the number of times that
the substring occurs in the given string. String traversal will take place from left to right, not from
right to left.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    string = input ().strip ()
    sub_string = input ().strip ()

    count = count_substring (string, sub_string)
    print (count)
