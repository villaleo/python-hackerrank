if __name__ == '__main__':
    """
    Given the names and grades for each student in a class of N students, store them
    in a nested list and print the name(s) of any student(s) having the second-lowest grade.
    
    Note: If there are multiple students with the second-lowest grade, order their names
    alphabetically and print each name on a new line.
    
    Further details are provided in the info.pdf file provided within this directory.
    """
    students = []
    scores = []
    result = []
    for _ in range (int (input ())):
        name = input ()
        score = float (input ())

        students.append ([name, score])
        scores.append (score)

    [result.append (x) for x in scores if x not in result]

    # Find second-lowest score:
    sorted_scores = sorted (scores)

    iterate = 0
    current = sorted_scores[0]
    while sorted_scores[iterate] == current:
        iterate += 1

    second_lowest = sorted_scores[iterate]
    # Reuse 'result' variable
    result.clear ()

    for entry in students:
        if entry[1] == second_lowest:
            result.append (entry[0])

    for val in sorted (result):
        print (val)
