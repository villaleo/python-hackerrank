if __name__ == '__main__':
    """
    The provided code stub will read in a dictionary containing key/value pairs of name:[marks]
    for a list of students. Print the average of the marks array for the student name provided,
    showing 2 places after the decimal.
    
    Further details are provided in the info.pdf file provided within this directory.
    """
    n = int (input ())
    student_marks = {}
    for _ in range (n):
        name, *line = input ().split ()
        scores = list (map (float, line))
        student_marks[name] = scores
    query_name = input ()

    query = student_marks[query_name]
    average = sum (query) / len (query)
    # Display average with 2 decimal precision
    print ('{:.2f}'.format (average))
