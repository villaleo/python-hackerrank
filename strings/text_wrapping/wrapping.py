import textwrap


def wrap (string, max_width) -> str:
    wrapped = textwrap.TextWrapper (width=max_width)
    words = wrapped.wrap (text=string)
    out = '\n'.join (words)
    return out


"""
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Returns a single string with newline characters ('\n') where the breaks should be.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    string, max_width = input (), int (input ())
    result = wrap (string, max_width)
    print (result)
