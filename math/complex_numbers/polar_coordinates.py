from cmath import phase, sqrt

"""
You are given a complex z. Your task is to convert it to polar coordinates. Input is a single line
containing the complex number, z. For output, the first line should contain the value of r. The
second line should contain the value of φ.

Further details are provided in the info.pdf file provided within this directory.
"""
if __name__ == '__main__':
    number = complex (input ())
    magnitude = abs (number)
    phase_angle = phase (number)

    print (f'{magnitude}\n{phase_angle}')
